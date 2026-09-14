"""`slugify` -- the function that turns a department title into a filename.

These are characterisation tests, and two of them pin results that look wrong:
three spaces become two hyphens, and three hyphens become two. That is what a
single non-recursive `.replace("--", "-")` does after the spaces are already
collapsed, and it is recorded rather than corrected because the filenames it
has already produced are linked from the generated artefacts. Changing the
function is a rename across those links, not a one-line fix -- so the current
behaviour is written down first, and anyone changing it will see exactly which
outputs move.
"""

from __future__ import annotations

import pytest

from scripts.generate_department_artifacts import slugify


@pytest.mark.parametrize(
    "title, expected",
    [
        ("Hello World", "Hello-World"),
        ("SimpleTitle", "SimpleTitle"),
        # " & " is a separator; a bare "&" is a word.
        ("Health & Safety", "Health-Safety"),
        ("A & B & C", "A-B-C"),
        ("Health&Safety", "HealthandSafety"),
        ("R&D", "RandD"),
        # One non-recursive collapse pass, so odd runs leave a hyphen behind.
        ("Double  Space", "Double-Space"),
        ("Multiple   Spaces", "Multiple--Spaces"),
        ("Word--Word", "Word-Word"),
        ("Word---Word", "Word--Word"),
        ("", ""),
        (" ", "-"),
        ("&", "and"),
        (" & ", "-"),
    ],
)
def test_slugify(title, expected):
    assert slugify(title) == expected
