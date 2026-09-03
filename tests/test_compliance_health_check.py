import unittest
from unittest.mock import patch
import tempfile
from pathlib import Path
import os

from scripts.compliance_health_check import count_markdown_entries

class TestComplianceHealthCheck(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root_path = Path(self.temp_dir.name)

        # Set up mock directory structure
        self.policies_dir = self.root_path / "docs" / "policies"
        self.procedures_dir = self.root_path / "docs" / "procedures"
        self.policies_dir.mkdir(parents=True)
        self.procedures_dir.mkdir(parents=True)

        # Create some mock policy files
        (self.policies_dir / "POL-001.md").touch()
        (self.policies_dir / "POL-002.md").touch()
        (self.policies_dir / "not-a-policy.md").touch()

        # Create some mock procedure files
        (self.procedures_dir / "PROC-001.md").touch()
        (self.procedures_dir / "PROC-002.md").touch()
        (self.procedures_dir / "PROC-003.md").touch()
        (self.procedures_dir / "not-a-procedure.md").touch()

        # Create mock index path
        self.index_path = self.root_path / "index.md"
        self.index_path.touch()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_count_markdown_entries_policies(self):
        with patch('scripts.compliance_health_check.ROOT', self.root_path):
            count = count_markdown_entries(self.index_path, "count_policy_files")
            self.assertEqual(count, 2)

    def test_count_markdown_entries_procedures(self):
        with patch('scripts.compliance_health_check.ROOT', self.root_path):
            count = count_markdown_entries(self.index_path, "count_procedure_files")
            self.assertEqual(count, 3)

    def test_count_markdown_entries_unknown(self):
        with patch('scripts.compliance_health_check.ROOT', self.root_path):
            count = count_markdown_entries(self.index_path, "unknown_prefix")
            self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()
