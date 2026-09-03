import pytest
import sys
import os
from pathlib import Path

# Add the project root to the python path so we can import from scripts
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.trigger_alignment_check import anchor_matches

@pytest.mark.parametrize(
    "token, name, expected",
    [
        # Exact match
        ("AI", "AI Framework", True),
        ("GDPR", "GDPR compliance", True),

        # Case insensitivity
        ("ai", "AI framework", True),
        ("AI", "ai framework", True),

        # Substring in larger word should NOT match
        ("AI", "Spain", False),
        ("AI", "Taiwan", False),
        ("AI", "Thailand", False),
        ("AI", "BAIDU", False),
        ("HIPAA", "HIPAAbad", False),

        # Matching at ends of string
        ("AI", "Framework for AI", True),
        ("AI", "AI", True),

        # Punctuation boundaries
        ("AI", "OWASP GenAI / LLM Top 10", False),
        ("AI", "OWASP AI / LLM", True),
        ("AI", "AI, ML, and Data", True),
        ("AI", "(AI)", True),
        ("AI", "AI-driven", True),

        # Multiple occurrences
        ("AI", "AI and more AI", True),

        # Additional tokens
        ("DORA", "DORA Regulation", True),
        ("ISO", "ISO 27001", True),
        ("NIST", "NIST SP 800-53", True)
    ]
)
def test_anchor_matches(token, name, expected):
    """Test that anchor_matches correctly identifies whole-word substrings."""
    assert anchor_matches(token, name) == expected
