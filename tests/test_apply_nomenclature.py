import pytest
from pathlib import Path
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.apply_nomenclature import should_process

def test_should_process():
    # Test valid extensions
    assert should_process(Path("test.md"))
    assert should_process(Path("test.yaml"))
    assert should_process(Path("test.yml"))
    assert should_process(Path("test.json"))

    # Test invalid extensions
    assert not should_process(Path("test.txt"))
    assert not should_process(Path("test.py"))

    # Test skip dirs
    assert not should_process(Path(".git/test.md"))
    assert not should_process(Path("venv/test.md"))
    assert not should_process(Path(".venv/test.md"))
    assert not should_process(Path("node_modules/test.md"))
    assert not should_process(Path("__pycache__/test.md"))
    assert not should_process(Path(".cursor/test.md"))

    # Test the specific file skip
    assert not should_process(Path("apply_nomenclature.py"))

    # Test valid path with subdirectories
    assert should_process(Path("docs/test.md"))
    assert should_process(Path("src/components/test.json"))
