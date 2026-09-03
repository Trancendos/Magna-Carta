import pytest
import sys
from pathlib import Path

# Add scripts directory to path to import the module
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from generate_department_artifacts import slugify

@pytest.mark.parametrize(
    "title, expected",
    [
        # Normal strings
        ("Hello World", "Hello-World"),
        ("SimpleTitle", "SimpleTitle"),

        # Strings with " & "
        ("Health & Safety", "Health-Safety"),
        ("A & B & C", "A-B-C"),

        # Strings with "&" (without surrounding spaces)
        ("Health&Safety", "HealthandSafety"),
        ("R&D", "RandD"),

        # Strings with consecutive spaces or hyphens
        ("Double  Space", "Double-Space"),
        ("Multiple   Spaces", "Multiple--Spaces"), # Note: current logic turns 3 spaces to 2 hyphens
        ("Word--Word", "Word-Word"),
        ("Word---Word", "Word--Word"), # Note: replace("--", "-") once turns --- to --

        # Empty string and single character
        ("", ""),
        (" ", "-"),
        ("&", "and"),
        (" & ", "-"),
    ]
)
def test_slugify(title, expected):
    """
    Test the slugify function with various inputs.
    Verifies replacement of ' & ', '&', spaces, and consecutive hyphens.
    """
    assert slugify(title) == expected
