import unittest
from pathlib import Path
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.apply_nomenclature import should_process

class TestApplyNomenclature(unittest.TestCase):
    def test_should_process_valid_extensions(self):
        self.assertTrue(should_process(Path("test.md")))
        self.assertTrue(should_process(Path("test.yaml")))
        self.assertTrue(should_process(Path("test.yml")))
        self.assertTrue(should_process(Path("test.json")))

    def test_should_process_invalid_extensions(self):
        self.assertFalse(should_process(Path("test.txt")))
        self.assertFalse(should_process(Path("test.py")))

    def test_should_process_skip_dirs(self):
        self.assertFalse(should_process(Path(".git/test.md")))
        self.assertFalse(should_process(Path("venv/test.md")))
        self.assertFalse(should_process(Path(".venv/test.md")))
        self.assertFalse(should_process(Path("node_modules/test.md")))
        self.assertFalse(should_process(Path("__pycache__/test.md")))
        self.assertFalse(should_process(Path(".cursor/test.md")))

    def test_should_process_specific_file_skip(self):
        self.assertFalse(should_process(Path("apply_nomenclature.py")))

    def test_should_process_valid_path_with_subdirectories(self):
        self.assertTrue(should_process(Path("docs/test.md")))
        self.assertTrue(should_process(Path("src/components/test.json")))

if __name__ == '__main__':
    unittest.main()
