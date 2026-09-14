"""`count_markdown_entries` and `resolve_signal_states`.

Two separate contributions landed on this same filename -- one covering the
document counter, one covering signal resolution -- plus a third that was a
near-duplicate of the first. They are consolidated here because a test file is
a filename, and three pull requests each creating `tests/test_compliance_health_check.py`
could never have been merged as three.

The signal cases were originally driven by patching `ROOT` with a `MagicMock`
and stubbing `__truediv__`, `is_file` and `open` on it. That asserts the
function calls those three methods in that order, not that it resolves a
signal -- a refactor to `Path.read_text()` would break the test while the
behaviour stayed correct. Here `ROOT` points at a real `tmp_path` with a real
file in it, so the test fails only when the answer changes.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts import compliance_health_check as chc


@pytest.fixture
def rooted(tmp_path, monkeypatch) -> Path:
    """Point the module's ROOT at an empty tree the test owns."""
    monkeypatch.setattr(chc, "ROOT", tmp_path)
    return tmp_path


class TestCountMarkdownEntries:
    """It counts by prefix glob, so the prefix has to be the thing that counts."""

    def test_it_counts_policies_by_their_prefix(self, rooted):
        policies = rooted / "docs" / "policies"
        policies.mkdir(parents=True)
        (policies / "POL-001.md").touch()
        (policies / "POL-002.md").touch()
        (policies / "not-a-policy.md").touch()

        assert chc.count_markdown_entries(Path("INDEX.md"), "count_policy_files") == 2

    def test_it_counts_procedures_by_their_prefix(self, rooted):
        procedures = rooted / "docs" / "procedures"
        procedures.mkdir(parents=True)
        for name in ("PROC-001.md", "PROC-002.md", "PROC-003.md", "not-a-procedure.md"):
            (procedures / name).touch()

        assert chc.count_markdown_entries(Path("INDEX.md"), "count_procedure_files") == 3

    def test_an_unknown_method_counts_nothing(self, rooted):
        assert chc.count_markdown_entries(Path("INDEX.md"), "count_unknown_files") == 0

    def test_a_missing_directory_counts_nothing_rather_than_raising(self, rooted):
        """MON-004 reports drift; it must not die on a tree that has no docs/."""
        assert chc.count_markdown_entries(Path("INDEX.md"), "count_policy_files") == 0


class TestResolveSignalStates:
    """A signal is active or inactive; there is no third answer and no exception."""

    def test_no_signals_resolves_to_nothing(self):
        assert chc.resolve_signal_states({}) == {}
        assert chc.resolve_signal_states({"signals": []}) == {}

    @staticmethod
    def _env_signal(variable: str = "MY_ENV_VAR") -> dict:
        return {
            "signals": [
                {
                    "signal_id": "SIG-01",
                    "detection": [
                        {
                            "source": "env",
                            "variable": variable,
                            "active_values": ["true", "1", "yes"],
                        }
                    ],
                }
            ]
        }

    def test_an_env_var_holding_an_active_value_is_active(self, monkeypatch):
        monkeypatch.setenv("MY_ENV_VAR", "True")
        assert chc.resolve_signal_states(self._env_signal()) == {"SIG-01": "active"}

    def test_an_env_var_holding_anything_else_is_inactive(self, monkeypatch):
        monkeypatch.setenv("MY_ENV_VAR", "False")
        assert chc.resolve_signal_states(self._env_signal()) == {"SIG-01": "inactive"}

    def test_an_unset_env_var_is_inactive(self, monkeypatch):
        monkeypatch.delenv("MY_ENV_VAR", raising=False)
        assert chc.resolve_signal_states(self._env_signal()) == {"SIG-01": "inactive"}

    @staticmethod
    def _config_signal(path: str = "test_config.json") -> dict:
        return {
            "signals": [
                {
                    "signal_id": "SIG-02",
                    "detection": [
                        {
                            "source": "config",
                            "path": path,
                            "json_path": "enabled",
                            "active_values": ["true", "1", "yes"],
                        }
                    ],
                }
            ]
        }

    def test_a_config_file_saying_true_is_active(self, rooted):
        (rooted / "test_config.json").write_text(json.dumps({"enabled": True}))
        assert chc.resolve_signal_states(self._config_signal()) == {"SIG-02": "active"}

    def test_a_config_file_saying_false_is_inactive(self, rooted):
        (rooted / "test_config.json").write_text(json.dumps({"enabled": False}))
        assert chc.resolve_signal_states(self._config_signal()) == {"SIG-02": "inactive"}

    def test_a_missing_config_file_is_inactive_rather_than_an_error(self, rooted):
        assert chc.resolve_signal_states(
            self._config_signal("missing_config.json")
        ) == {"SIG-02": "inactive"}

    def test_a_json_path_that_does_not_exist_is_inactive(self, rooted):
        """An absent key must not read as an enabled feature."""
        (rooted / "test_config.json").write_text(json.dumps({"something_else": True}))
        assert chc.resolve_signal_states(self._config_signal()) == {"SIG-02": "inactive"}
