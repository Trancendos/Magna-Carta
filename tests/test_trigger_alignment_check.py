"""`anchor_matches` -- whole-word, case-insensitive anchor matching.

The cases that matter are the near-misses. A substring match would tie the AI
framework anchor to Spain, Taiwan and Thailand, and HIPAA to anything merely
starting with those letters -- so a register entry would report itself aligned
to an obligation it has nothing to do with. The word-boundary cases below are
the ones that would pass under a naive `in` test and must not.
"""

from __future__ import annotations

import pytest

from scripts.trigger_alignment_check import anchor_matches


@pytest.mark.parametrize(
    "token, name",
    [
        ("AI", "AI Framework"),
        ("GDPR", "GDPR compliance"),
        # Case-insensitive in both directions.
        ("ai", "AI framework"),
        ("AI", "ai framework"),
        # Either end of the string, and the whole string.
        ("AI", "Framework for AI"),
        ("AI", "AI"),
        # Punctuation is a boundary.
        ("AI", "OWASP AI / LLM"),
        ("AI", "AI, ML, and Data"),
        ("AI", "(AI)"),
        ("AI", "AI-driven"),
        ("AI", "AI and more AI"),
        ("DORA", "DORA Regulation"),
        ("ISO", "ISO 27001"),
        ("NIST", "NIST SP 800-53"),
    ],
)
def test_a_whole_word_anchor_matches(token, name):
    assert anchor_matches(token, name) is True


@pytest.mark.parametrize(
    "token, name",
    [
        ("AI", "Spain"),
        ("AI", "Taiwan"),
        ("AI", "Thailand"),
        ("AI", "BAIDU"),
        ("HIPAA", "HIPAAbad"),
        # "GenAI" is a different anchor from "AI"; a substring test conflates them.
        ("AI", "OWASP GenAI / LLM Top 10"),
    ],
)
def test_an_anchor_buried_inside_a_word_does_not_match(token, name):
    assert anchor_matches(token, name) is False


def test_a_token_is_escaped_rather_than_read_as_a_pattern():
    """`.` is a literal dot here, not "any character"."""
    assert anchor_matches("ISO.27001", "ISO 27001") is False
    assert anchor_matches("ISO.27001", "ISO.27001 controls") is True


def test_a_token_ending_in_a_non_word_character_can_never_match():
    """A recorded limit of `\\b`, not a wish -- and one with a live guard below.

    `\\b` needs a word character on the inside of the boundary, so a trailing
    `+` or a leading `.` puts two non-word characters either side of the
    boundary position and no match is possible anywhere. `anchor_matches` then
    returns False for every framework name, and the trigger reads as
    unanchored rather than as broken -- the silent kind of wrong.
    """
    assert anchor_matches("C++", "C++ secure coding") is False
    assert anchor_matches(".NET", ".NET hardening") is False


def test_no_live_anchor_trips_that_limit():
    """The limit above is harmless only while this holds. It is checked, not assumed."""
    from scripts.trigger_alignment_check import ANCHORS

    unmatchable = [
        token
        for token in ANCHORS.values()
        if not (token[:1].isalnum() or token[:1] == "_")
        or not (token[-1:].isalnum() or token[-1:] == "_")
    ]
    assert not unmatchable, (
        f"anchors that \\b can never match: {unmatchable} — "
        "these silently match nothing instead of failing"
    )
