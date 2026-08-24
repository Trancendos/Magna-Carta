import pytest
from pathlib import Path
import yaml
from trigger_alignment_check import anchor_matches, _load, ROOT

# Tests will be added here

def test_anchor_matches():
    # True positives
    assert anchor_matches("HIPAA", "HIPAA Security Rule") is True
    assert anchor_matches("hipaa", "HIPAA Security Rule") is True
    assert anchor_matches("HIPAA", "hipaa security rule") is True
    assert anchor_matches("HIPAA", "Rule for HIPAA compliance") is True
    assert anchor_matches("DORA", "DORA") is True
    assert anchor_matches("ISO 27001", "Compliance with ISO 27001 standard") is True

    # True negatives (substring but not whole word)

    assert anchor_matches("HIPAA", "NotHIPAARule") is False
    assert anchor_matches("HIPAA", "HIPAARule") is False
    assert anchor_matches("HIPAA", "RuleHIPAA") is False
    assert anchor_matches("ISO 2700", "ISO 27001") is False


import unittest.mock

def test_load_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr("trigger_alignment_check.ROOT", tmp_path)
    errors = []
    missing_file = tmp_path / "missing.yaml"
    result = _load(missing_file, errors)
    assert result == {}
    assert len(errors) == 1
    assert "missing register" in errors[0]

def test_load_invalid_yaml(tmp_path, monkeypatch):
    monkeypatch.setattr("trigger_alignment_check.ROOT", tmp_path)
    errors = []
    invalid_yaml = tmp_path / "invalid.yaml"
    invalid_yaml.write_text("invalid: yaml: content: \n - item\n  badindent")
    result = _load(invalid_yaml, errors)
    assert result == {}
    assert len(errors) == 1
    assert "invalid YAML" in errors[0]

def test_load_non_mapping_root(tmp_path, monkeypatch):
    monkeypatch.setattr("trigger_alignment_check.ROOT", tmp_path)
    errors = []
    list_yaml = tmp_path / "list.yaml"
    list_yaml.write_text("- item 1\n- item 2")
    result = _load(list_yaml, errors)
    assert result == {}
    assert len(errors) == 1
    assert "root must be a mapping" in errors[0]

def test_load_valid_yaml(tmp_path, monkeypatch):
    monkeypatch.setattr("trigger_alignment_check.ROOT", tmp_path)
    errors = []
    valid_yaml = tmp_path / "valid.yaml"
    valid_yaml.write_text("key: value\nnested:\n  - item 1")
    result = _load(valid_yaml, errors)
    assert result == {"key": "value", "nested": ["item 1"]}
    assert len(errors) == 0
