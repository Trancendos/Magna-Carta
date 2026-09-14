"""The generators must reproduce the tree, not rewrite it.

Every document under docs/bibles/, docs/procedures/, docs/cookbooks/,
docs/hymn-sheets/ and docs/job-descriptions/ is written by a script. Nothing
checked that the committed copies were what those scripts produce, and they were
not: on 2026-09-14 a clean run deleted seven matrix cross-references from four
bibles (MC-012, MC-013, MC-016, MC-017, MC-018, MC-019, MC-020), each added by
hand to a generated file and erased by the next run. The resulting diff read as
the generator working correctly, which is why it was never reported.

A hand edit to a generated document is not a small mistake to be tidied up
later: it survives until someone runs the generator, and then it is gone with no
record. It happened again in the same week -- dosubot wrote a ROPA gap row into
DATA-MANAGEMENT-BIBLE.md while this was being fixed. The row was right; the
place was not. It now lives in BIBLE_GAP_ROWS.

So this test runs the generators over a COPY of the repository and fails if
anything moves. A copy, not the working tree: a test that regenerated in place
would overwrite a developer's own uncommitted work to answer a question about
the committed state.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

#: Scripts that write documents into docs/. Order matters only in that all of
#: them run before anything is compared.
GENERATORS = (
    "generate_department_artifacts.py",
    "generate_job_descriptions.py",
    "generate_framework_implementation.py",
)


@pytest.fixture(scope="module")
def regenerated(tmp_path_factory) -> Path:
    """A copy of the repository with every generator run over it once."""
    work = tmp_path_factory.mktemp("regen") / "repo"
    shutil.copytree(
        ROOT, work,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache", "*.pyc"),
    )
    for name in GENERATORS:
        result = subprocess.run(
            [sys.executable, str(work / "scripts" / name)],
            cwd=work, capture_output=True, text=True, timeout=300,
        )
        assert result.returncode == 0, f"{name} failed:\n{result.stdout}{result.stderr}"
    return work


def _generated_files() -> list[Path]:
    roots = ("docs/bibles", "docs/procedures", "docs/cookbooks",
             "docs/hymn-sheets", "docs/job-descriptions")
    out: list[Path] = []
    for rel in roots:
        out.extend(sorted((ROOT / rel).glob("*.md")))
    assert out, "no generated documents found — this test would pass vacuously"
    return out


@pytest.mark.parametrize("path", _generated_files(), ids=lambda p: p.name)
def test_the_generators_reproduce_this_document(path: Path, regenerated: Path) -> None:
    rel = path.relative_to(ROOT)
    produced = regenerated / rel
    assert produced.is_file(), f"{rel} is committed but no generator writes it"
    assert produced.read_text(encoding="utf-8") == path.read_text(encoding="utf-8"), (
        f"{rel} differs from what the generators produce. Either the document was "
        "edited by hand -- in which case the edit belongs in the generator, or it "
        "disappears on the next run -- or the generator changed and the document "
        "needs regenerating and committing."
    )


def test_the_generators_add_no_document_that_is_not_committed(regenerated: Path) -> None:
    """A generated file nobody committed is invisible until CI or a reader trips on it."""
    missing = []
    for rel in ("docs/bibles", "docs/procedures", "docs/cookbooks",
                "docs/hymn-sheets", "docs/job-descriptions"):
        for produced in sorted((regenerated / rel).glob("*.md")):
            if not (ROOT / rel / produced.name).is_file():
                missing.append(f"{rel}/{produced.name}")
    assert not missing, f"generated but not committed: {missing}"
