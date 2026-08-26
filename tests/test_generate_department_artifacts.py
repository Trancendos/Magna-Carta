import unittest
import sys
import os

# Add the root directory to sys.path so we can import from scripts
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.generate_department_artifacts import slugify

class TestGenerateDepartmentArtifacts(unittest.TestCase):
    def test_slugify(self):
        test_cases = [
            # Basic strings
            ("Hello World", "Hello-World"),
            ("Test", "Test"),

            # Ampersand with spaces
            ("A & B", "A-B"),
            ("Health & Safety", "Health-Safety"),

            # Ampersand without spaces
            ("A&B", "AandB"),
            ("R&D", "RandD"),

            # Multiple spaces and hyphens
            ("Hello  World", "Hello-World"),
            ("Hello   World", "Hello--World"),
            ("Hello--World", "Hello-World"),
            ("Hello---World", "Hello--World"),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(slugify(input_str), expected)

if __name__ == '__main__':
    unittest.main()
# Trigger CI rerun
# Kilo rerun 2
