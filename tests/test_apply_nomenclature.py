import unittest
from pathlib import Path
from scripts.apply_nomenclature import should_process

class TestApplyNomenclature(unittest.TestCase):
    def test_should_process_valid_extensions(self):
        self.assertTrue(should_process(Path("file.md")))
        self.assertTrue(should_process(Path("file.yaml")))
        self.assertTrue(should_process(Path("file.yml")))
        self.assertTrue(should_process(Path("file.json")))

    def test_should_process_invalid_extensions(self):
        self.assertFalse(should_process(Path("file.txt")))
        self.assertFalse(should_process(Path("file.py")))
        self.assertFalse(should_process(Path("file")))

    def test_should_process_skip_dirs(self):
        self.assertFalse(should_process(Path(".git/config.yaml")))
        self.assertFalse(should_process(Path(".venv/lib/package.json")))
        self.assertFalse(should_process(Path("node_modules/pkg/package.json")))
        self.assertFalse(should_process(Path("__pycache__/test.json")))
        self.assertFalse(should_process(Path(".cursor/settings.json")))

    def test_should_process_self(self):
        self.assertFalse(should_process(Path("scripts/apply_nomenclature.py")))
        self.assertFalse(should_process(Path("apply_nomenclature.py")))

if __name__ == '__main__':
    unittest.main()
