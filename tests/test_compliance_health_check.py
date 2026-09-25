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

ROOT = Path(__file__).resolve().parent.parent


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


class TestRegisterIdUniqueness:
    """MON-019. ACT-016 was issued twice and nothing looked.

    MON-019 and not MON-016, because MON-016 was already enforcement_alignment's:
    the check that finds id collisions shipped with one. Caught by sourcery-ai.
    """

    CFG = {
        "register_id_uniqueness": {
            "check_id": "MON-TEST",
            "registers": [
                {
                    "source": "compliance/compliance_action_tracker.yaml",
                    "items_key": "actions",
                    "id_field": "action_id",
                }
            ],
        }
    }

    def _register(self, *ids) -> dict:
        return {"actions": [{"action_id": i, "title": f"t{i}"} for i in ids]}

    def test_a_repeated_id_is_an_error(self, monkeypatch, tmp_path):
        import yaml as _y

        monkeypatch.setattr(chc, "ROOT", tmp_path)
        (tmp_path / "compliance").mkdir()
        (tmp_path / "compliance" / "compliance_action_tracker.yaml").write_text(
            _y.safe_dump(self._register("ACT-001", "ACT-002", "ACT-001"))
        )
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        assert [f.severity for f in findings] == ["error"]
        assert "ACT-001 is used by 2 entries" in findings[0].message

    def test_distinct_ids_pass(self, monkeypatch, tmp_path):
        import yaml as _y

        monkeypatch.setattr(chc, "ROOT", tmp_path)
        (tmp_path / "compliance").mkdir()
        (tmp_path / "compliance" / "compliance_action_tracker.yaml").write_text(
            _y.safe_dump(self._register("ACT-001", "ACT-002", "ACT-003"))
        )
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        assert findings == []

    def test_an_empty_register_is_an_error_not_a_pass(self, monkeypatch, tmp_path):
        """A check that reports clean because it looked at nothing is the bug."""
        import yaml as _y

        monkeypatch.setattr(chc, "ROOT", tmp_path)
        (tmp_path / "compliance").mkdir()
        (tmp_path / "compliance" / "compliance_action_tracker.yaml").write_text(
            _y.safe_dump({"actions": []})
        )
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        assert [f.severity for f in findings] == ["error"]
        assert "nothing was checked" in findings[0].message

    def test_a_missing_register_is_an_error(self, monkeypatch, tmp_path):
        monkeypatch.setattr(chc, "ROOT", tmp_path)
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        assert [f.severity for f in findings] == ["error"]
        assert "not readable" in findings[0].message

    def test_the_live_registers_are_actually_covered(self):
        """Three registers are named in the config; all three must still parse."""
        import yaml as _y

        cfg = _y.safe_load(
            (ROOT / "compliance" / "maintenance_monitor.yaml").read_text(encoding="utf-8")
        )
        specs = (cfg.get("register_id_uniqueness") or {}).get("registers") or []
        assert len(specs) >= 3, "MON-019 covers fewer registers than it was given"
        for spec in specs:
            data = _y.safe_load((ROOT / spec["source"]).read_text(encoding="utf-8"))
            items = data.get(spec["items_key"])
            assert items, f"{spec['source']}: {spec['items_key']} is empty"
            ids = [i.get(spec["id_field"]) for i in items if isinstance(i, dict)]
            assert all(ids), f"{spec['source']}: an entry has no {spec['id_field']}"
            assert len(ids) == len(set(ids)), f"{spec['source']}: duplicate ids {ids}"


class TestTheCheckIdsAreThemselvesUnique:
    """The check that finds id collisions shipped with one. Caught by sourcery-ai."""

    def test_no_two_checks_share_a_check_id(self):
        """A duplicate id makes two unrelated findings indistinguishable."""
        import collections

        import yaml

        cfg = yaml.safe_load(
            (ROOT / "compliance" / "maintenance_monitor.yaml").read_text(encoding="utf-8")
        )
        # A check_id repeated across the ENTRIES of one check is correct -- twenty
        # required files all report as MON-001. A check_id claimed by two different
        # top-level checks is not.
        owner: dict[str, str] = {}
        clashes = []
        for name, block in cfg.items():
            if not isinstance(block, dict):
                continue
            cid = block.get("check_id")
            if not cid:
                continue
            if cid in owner and owner[cid] != name:
                clashes.append(f"{cid}: {owner[cid]} and {name}")
            owner.setdefault(cid, name)
        assert not clashes, f"check_id claimed by two checks: {clashes}"


class TestAnIdInTheWrongListIsReported:
    """ACT-021 was recorded where no check could see it, which reads as handled."""

    SPEC = {"items_key": "actions", "id_field": "action_id"}

    def _run(self, data: dict) -> list:
        findings: list = []
        chc._check_ids_are_in_the_checked_list(
            self.SPEC, data, findings, "MON-TEST", "tracker.yaml"
        )
        return findings

    def test_an_id_that_appears_only_outside_the_checked_list_is_an_error(self):
        data = {
            "actions": [{"action_id": "ACT-001"}],
            "programme_milestones": [{"action_id": "ACT-021", "title": "stray"}],
        }
        findings = self._run(data)
        assert [f.severity for f in findings] == ["error"]
        assert "ACT-021" in findings[0].message
        assert "programme_milestones" in findings[0].message

    def test_an_id_that_also_appears_inside_it_is_a_cross_reference(self):
        """execution_evidence_register's recurrence_schedule is exactly this shape."""
        data = {
            "actions": [{"action_id": "ACT-001"}],
            "recurrence_schedule": [{"action_id": "ACT-001", "cadence_days": 90}],
        }
        assert self._run(data) == []

    def test_other_top_level_keys_are_left_alone(self):
        data = {"actions": [{"action_id": "ACT-001"}], "meta": {"owner": "x"}, "schema": "y"}
        assert self._run(data) == []

    def test_the_live_tracker_has_no_stray(self):
        import yaml

        data = yaml.safe_load(
            (ROOT / "compliance" / "compliance_action_tracker.yaml").read_text(encoding="utf-8")
        )
        assert data.get("actions"), "actions is empty — nothing was checked"
        assert self._run(data) == []


class TestMalformedRegistersAreReportedNotRaised:
    """One unparseable register must not stop every check after it."""

    CFG = {
        "register_id_uniqueness": {
            "check_id": "MON-TEST",
            "registers": [
                {
                    "source": "compliance/compliance_action_tracker.yaml",
                    "items_key": "actions",
                    "id_field": "action_id",
                }
            ],
        }
    }

    def _write(self, tmp_path, text: str):
        (tmp_path / "compliance").mkdir(exist_ok=True)
        (tmp_path / "compliance" / "compliance_action_tracker.yaml").write_text(
            text, encoding="utf-8"
        )

    def test_invalid_yaml_is_a_finding(self, monkeypatch, tmp_path):
        monkeypatch.setattr(chc, "ROOT", tmp_path)
        self._write(tmp_path, "actions: [unclosed\n")
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        assert [f.severity for f in findings] == ["error"]
        assert "cannot be read" in findings[0].message

    def test_a_non_mapping_root_is_a_finding(self, monkeypatch, tmp_path):
        monkeypatch.setattr(chc, "ROOT", tmp_path)
        self._write(tmp_path, "- just\n- a list\n")
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        assert [f.severity for f in findings] == ["error"]
        assert "expected a mapping" in findings[0].message

    def test_a_non_mapping_entry_is_reported_not_skipped(self, monkeypatch, tmp_path):
        """Skipping what it cannot read is the failure this check exists to stop."""
        monkeypatch.setattr(chc, "ROOT", tmp_path)
        self._write(tmp_path, 'actions:\n  - "a bare string"\n  - action_id: ACT-001\n')
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        assert [f.severity for f in findings] == ["error"]
        assert "actions[0] is str" in findings[0].message


class TestIdentifierReferencesResolve:
    """MON-020. Renumbering ACT-016 left three documents citing the old id."""

    @staticmethod
    def _cfg(tmp_path) -> dict:
        return {
            "identifier_references": {
                "check_id": "MON-TEST",
                "identifiers": [
                    {
                        "register": "compliance/tracker.yaml",
                        "items_key": "actions",
                        "id_field": "action_id",
                        "pattern": r"ACT-[0-9]{3}",
                        "search": ["docs/*.md"],
                    }
                ],
            }
        }

    @staticmethod
    def _tree(tmp_path, doc_text: str, ids=("ACT-001",)) -> None:
        import yaml as _y

        (tmp_path / "compliance").mkdir(exist_ok=True)
        (tmp_path / "docs").mkdir(exist_ok=True)
        (tmp_path / "compliance" / "tracker.yaml").write_text(
            _y.safe_dump({"actions": [{"action_id": i} for i in ids]}), encoding="utf-8"
        )
        (tmp_path / "docs" / "note.md").write_text(doc_text, encoding="utf-8")

    def _run(self, monkeypatch, tmp_path) -> list:
        monkeypatch.setattr(chc, "ROOT", tmp_path)
        findings: list = []
        chc.check_identifier_references_resolve(self._cfg(tmp_path), findings)
        return findings

    def test_a_citation_of_an_id_that_does_not_exist_is_an_error(self, monkeypatch, tmp_path):
        self._tree(tmp_path, "Raised as ACT-016.")
        findings = self._run(monkeypatch, tmp_path)
        assert [f.severity for f in findings] == ["error"]
        assert "ACT-016" in findings[0].message

    def test_a_citation_of_a_defined_id_passes(self, monkeypatch, tmp_path):
        self._tree(tmp_path, "Raised as ACT-001.")
        assert self._run(monkeypatch, tmp_path) == []

    def test_prose_citations_are_found_not_only_structured_fields(self, monkeypatch, tmp_path):
        """The three that went stale were all in prose, not in linked_action."""
        self._tree(tmp_path, "an open gap (**ACT-016**) rather than compliant")
        assert [f.severity for f in self._run(monkeypatch, tmp_path)] == ["error"]

    def test_a_register_defining_nothing_is_an_error_not_a_pass(self, monkeypatch, tmp_path):
        self._tree(tmp_path, "no citations here", ids=())
        findings = self._run(monkeypatch, tmp_path)
        assert [f.severity for f in findings] == ["error"]
        assert "nothing to resolve against" in findings[0].message

    def test_the_live_tree_resolves(self):
        """Not a tautology: probed by reintroducing the stale reference."""
        findings: list = []
        import yaml as _y

        cfg = _y.safe_load(
            (ROOT / "compliance" / "maintenance_monitor.yaml").read_text(encoding="utf-8")
        )
        assert cfg.get("identifier_references", {}).get("identifiers"), "MON-020 covers nothing"
        chc.check_identifier_references_resolve(cfg, findings)
        assert findings == [], [f.message for f in findings]


class TestAnIdentifierMustBeANonEmptyString:
    """`""` and `123` were accepted as unique. (codex)"""

    CFG = {
        "register_id_uniqueness": {
            "check_id": "MON-TEST",
            "registers": [
                {
                    "source": "compliance/tracker.yaml",
                    "items_key": "actions",
                    "id_field": "action_id",
                }
            ],
        }
    }

    def _run(self, monkeypatch, tmp_path, actions) -> list:
        import yaml as _y

        monkeypatch.setattr(chc, "ROOT", tmp_path)
        (tmp_path / "compliance").mkdir(exist_ok=True)
        (tmp_path / "compliance" / "tracker.yaml").write_text(
            _y.safe_dump({"actions": actions}), encoding="utf-8"
        )
        findings: list = []
        chc.check_register_id_uniqueness(self.CFG, findings)
        return findings

    @pytest.mark.parametrize("bad", ["", "   ", 123, True, [], {}])
    def test_an_unusable_id_is_an_error(self, monkeypatch, tmp_path, bad):
        findings = self._run(monkeypatch, tmp_path, [{"action_id": bad}])
        assert [f.severity for f in findings] == ["error"]
        assert "non-empty string" in findings[0].message

    def test_a_real_id_passes(self, monkeypatch, tmp_path):
        assert self._run(monkeypatch, tmp_path, [{"action_id": "ACT-001"}]) == []


class TestTheDocumentationMatchesTheConfiguration:
    """REGISTER-SCHEMAS.md documented MON-016 after the check had moved to MON-019.

    It slipped because the edit that renumbered it was a `str.replace` against
    text that had changed under it: a no-op that reported nothing, which is the
    same shape as every other defect this branch found. A check id is the handle
    a reader uses to find what fired, so a document naming the wrong one sends
    them to the wrong check. (codeant-ai)
    """

    def test_every_check_documented_in_register_schemas_names_its_configured_id(self):
        import re

        import yaml

        cfg = yaml.safe_load(
            (ROOT / "compliance" / "maintenance_monitor.yaml").read_text(encoding="utf-8")
        )
        configured = {
            name: block["check_id"]
            for name, block in cfg.items()
            if isinstance(block, dict) and block.get("check_id")
        }
        doc = (ROOT / "docs" / "schemas" / "REGISTER-SCHEMAS.md").read_text(encoding="utf-8")

        wrong = []
        # "### <check name> (MON-0xx)" is how the document titles each section.
        for heading, documented in re.findall(r"^### (\w+) \((MON-\d+)\)", doc, re.M):
            if heading in configured and configured[heading] != documented:
                wrong.append(f"{heading}: documented {documented}, configured {configured[heading]}")
        assert not wrong, wrong

    def test_at_least_one_check_is_documented_by_id(self):
        """Otherwise the test above passes by matching nothing."""
        import re

        doc = (ROOT / "docs" / "schemas" / "REGISTER-SCHEMAS.md").read_text(encoding="utf-8")
        assert re.findall(r"^### \w+ \(MON-\d+\)", doc, re.M)

    #: Checks REGISTER-SCHEMAS.md does not document, measured 2026-09-14. The
    #: document was written for register *schemas*, and these twelve predate the
    #: convention of documenting a check there; they are a real gap, recorded
    #: rather than closed in this branch. The set may shrink. It may not grow.
    UNDOCUMENTED = {
        "action_overdue",
        "enforcement_alignment",
        "evidence_recurrence",
        "framework_implementation",
        "framework_readiness",
        "legislation_watch",
        "procedure_coverage",
        "standards_watch",
        "supplier_dpa_gates",
        "trigger_integrity",
        "weekly_cadence",
    }

    def test_no_new_check_is_undocumented(self):
        """The id-matching test above compares only checks the document mentions.

        A check documented nowhere matches nothing and passes — which is what
        MON-020 did, having been added with no section of its own. (codeant-ai)
        """
        import re

        import yaml

        cfg = yaml.safe_load(
            (ROOT / "compliance" / "maintenance_monitor.yaml").read_text(encoding="utf-8")
        )
        configured = {
            name
            for name, block in cfg.items()
            if isinstance(block, dict) and block.get("check_id")
        }
        doc = (ROOT / "docs" / "schemas" / "REGISTER-SCHEMAS.md").read_text(encoding="utf-8")
        documented = {h for h, _ in re.findall(r"^### (\w+) \((MON-\d+)\)", doc, re.M)}

        new_gaps = sorted(configured - documented - self.UNDOCUMENTED)
        assert not new_gaps, f"configured but documented nowhere: {new_gaps}"


class TestStrayIdsOfTheWrongType:
    """A mixed-type register reached sorted() and took the health check down."""

    SPEC = {"items_key": "actions", "id_field": "action_id"}

    def _run(self, data: dict) -> list:
        findings: list = []
        chc._check_ids_are_in_the_checked_list(
            self.SPEC, data, findings, "MON-TEST", "tracker.yaml"
        )
        return findings

    def test_a_non_string_id_is_reported_rather_than_sorted(self):
        data = {
            "actions": [{"action_id": "ACT-001"}],
            "programme_milestones": [{"action_id": 123}, {"action_id": "ACT-999"}],
        }
        messages = [f.message for f in self._run(data)]
        assert any("123" in m and "non-empty string" in m for m in messages)
        assert any("ACT-999" in m and "nowhere in" in m for m in messages)

    @pytest.mark.parametrize("bad", [123, 1.5, ["x"], {"a": 1}])
    def test_no_id_type_makes_the_check_raise(self, bad):
        data = {"actions": [{"action_id": "ACT-001"}], "other": [{"action_id": bad}]}
        assert self._run(data)  # reports rather than raises
