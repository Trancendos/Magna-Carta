"""The OSS_SCAN_REQUIRED gate in scripts/run_oss_security_scans.sh.

The gate exists because Layer B CI installed no scanner at all and the script
exited 0 having looked at nothing. sourcery-ai then found the same shape inside
the fix: an unrecognised name in OSS_SCAN_REQUIRED was silently ignored, so
`OSS_SCAN_REQUIRED=pip_audi` required a scanner that does not exist, found
nothing missing, and passed. A gate that is configured, reports, and cannot act
is the defect it was written to remove.

The scanners are invoked only when present on PATH, so every case here runs with
PATH emptied: each block takes its SKIP branch and the whole script finishes in
milliseconds while still exercising the gate.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "run_oss_security_scans.sh"
KNOWN = ("gitleaks", "bandit", "semgrep", "pip-audit")


#: Resolved before PATH is emptied, and passed to subprocess absolutely -- the
#: child's PATH is what the script searches, not what finds the interpreter.
BASH = shutil.which("bash") or "/bin/bash"


def _run(required: str | None = None, script: Path = SCRIPT) -> subprocess.CompletedProcess:
    # Empty PATH and a HOME with no .local/bin: the script prepends both, and
    # every `command -v` then misses, so each scanner takes its SKIP branch and
    # the run finishes in milliseconds without installing or invoking anything.
    env = dict(os.environ, PATH="", HOME="/nonexistent")
    env.pop("OSS_SCAN_REQUIRED", None)
    if required is not None:
        env["OSS_SCAN_REQUIRED"] = required
    return subprocess.run(
        [BASH, str(script)], cwd=ROOT, env=env,
        capture_output=True, text=True, timeout=120,
    )


class TestTheRequiredScannerGate:
    def test_with_nothing_required_an_empty_run_still_passes(self):
        """A developer without the stack installed gets skips, not failures."""
        assert _run().returncode == 0

    @pytest.mark.parametrize("name", KNOWN)
    def test_every_known_scanner_can_be_required(self, name):
        result = _run(name)
        assert result.returncode == 1
        assert f"not installed: {name}" in result.stderr

    def test_an_unrecognised_name_fails_rather_than_being_ignored(self):
        result = _run("bandit,pip_audi")
        assert result.returncode == 1
        assert "does not run: pip_audi" in result.stderr

    def test_the_failure_names_what_it_would_have_accepted(self):
        """Otherwise the reader has to go and read the script to fix a typo."""
        result = _run("nonsense")
        assert all(name in result.stderr for name in KNOWN)

    def test_a_blind_run_is_reported_even_when_nothing_is_required(self):
        assert "BLIND" in _run().stderr


class TestTheKnownScannerListCannotFallBehind:
    """KNOWN_SCANNERS is what OSS_SCAN_REQUIRED is validated against."""

    def test_a_scanner_missing_from_the_list_is_a_failure(self, tmp_path):
        """Otherwise it would be silently un-requirable -- optional forever."""
        drifted = tmp_path / "drifted.sh"
        drifted.write_text(
            SCRIPT.read_text(encoding="utf-8").replace(
                'KNOWN_SCANNERS="gitleaks bandit semgrep pip-audit"',
                'KNOWN_SCANNERS="gitleaks bandit semgrep"',
            ),
            encoding="utf-8",
        )
        result = _run(script=drifted)
        assert result.returncode == 1
        assert "missing from KNOWN_SCANNERS" in result.stderr

    def test_a_listed_scanner_with_no_block_is_a_failure(self, tmp_path):
        drifted = tmp_path / "drifted.sh"
        drifted.write_text(
            SCRIPT.read_text(encoding="utf-8").replace(
                'KNOWN_SCANNERS="gitleaks bandit semgrep pip-audit"',
                'KNOWN_SCANNERS="gitleaks bandit semgrep pip-audit trivy"',
            ),
            encoding="utf-8",
        )
        result = _run(script=drifted)
        assert result.returncode == 1
        assert "no block here runs or skips it" in result.stderr

    def test_the_workflows_only_require_names_the_script_knows(self):
        """The gate is useless if CI's own value is one of the typos it rejects."""
        import re

        for rel in (".github/workflows/layer-b-ci.yml", ".forgejo/workflows/layer-b-ci.yml"):
            text = (ROOT / rel).read_text(encoding="utf-8")
            values = re.findall(r"OSS_SCAN_REQUIRED:\s*(\S+)", text)
            assert values, f"{rel} sets no OSS_SCAN_REQUIRED"
            for value in values:
                for name in value.split(","):
                    assert name in KNOWN, f"{rel} requires unknown scanner {name!r}"
