import pytest
from pathlib import Path

# Important: ensure scripts can be imported
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.compliance_health_check import count_markdown_entries

def test_count_markdown_entries_policies(monkeypatch, tmp_path):
    monkeypatch.setattr("scripts.compliance_health_check.ROOT", tmp_path)

    policies_dir = tmp_path / "docs" / "policies"
    policies_dir.mkdir(parents=True)

    (policies_dir / "POL-001.md").touch()
    (policies_dir / "POL-002.md").touch()
    (policies_dir / "NOT-POL.md").touch()

    assert count_markdown_entries(Path("dummy_index.md"), "count_policy_files") == 2

def test_count_markdown_entries_procedures(monkeypatch, tmp_path):
    monkeypatch.setattr("scripts.compliance_health_check.ROOT", tmp_path)

    procedures_dir = tmp_path / "docs" / "procedures"
    procedures_dir.mkdir(parents=True)

    (procedures_dir / "PROC-001.md").touch()
    (procedures_dir / "PROC-002.md").touch()
    (procedures_dir / "PROC-003.md").touch()
    (procedures_dir / "IGNORE-ME.md").touch()

    assert count_markdown_entries(Path("dummy_index.md"), "count_procedure_files") == 3

def test_count_markdown_entries_unknown(monkeypatch, tmp_path):
    monkeypatch.setattr("scripts.compliance_health_check.ROOT", tmp_path)

    assert count_markdown_entries(Path("dummy_index.md"), "count_unknown_files") == 0
