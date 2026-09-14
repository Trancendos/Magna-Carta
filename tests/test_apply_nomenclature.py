"""`should_process` -- the filter that decides what the rename sweep may touch.

This gate is the difference between a nomenclature migration and a sweep
through `.git`, `node_modules` and every `.py` file in the tree. It has no
dry-run safety net of its own: `migrate_file` writes whatever `should_process`
admits.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.apply_nomenclature import should_process


@pytest.mark.parametrize("name", ["test.md", "test.yaml", "test.yml", "test.json"])
def test_the_four_declared_extensions_are_processed(name):
    assert should_process(Path(name)) is True


@pytest.mark.parametrize("name", ["test.txt", "test.py", "test", "test.MD"])
def test_everything_else_is_refused(name):
    """Including `.MD` -- the suffix set is case-sensitive, which is the behaviour."""
    assert should_process(Path(name)) is False


@pytest.mark.parametrize(
    "skipped", [".git", ".venv", "venv", "node_modules", "__pycache__", ".cursor"]
)
def test_the_skip_directories_are_refused_at_any_depth(skipped):
    assert should_process(Path(skipped) / "test.md") is False
    assert should_process(Path("docs") / skipped / "test.md") is False


def test_the_migration_script_never_rewrites_itself():
    assert should_process(Path("apply_nomenclature.py")) is False
    assert should_process(Path("scripts/apply_nomenclature.py")) is False


@pytest.mark.parametrize("path", ["docs/test.md", "src/components/test.json"])
def test_ordinary_nested_paths_are_processed(path):
    assert should_process(Path(path)) is True
