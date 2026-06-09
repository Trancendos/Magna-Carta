#!/usr/bin/env python3
"""
One-shot nomenclature migration: Trancendos Universe / Infinity Network.

Replaces legacy "Tranc3 as platform foundation" phrasing in markdown and YAML.
Does not rename filenames containing tranc3 (app bridge paths stay stable).

Usage:
  python3 scripts/apply_nomenclature.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".cursor"}
EXTENSIONS = {".md", ".yaml", ".yml", ".json"}

# Order matters — longer / more specific first
REPLACEMENTS: list[tuple[str, str]] = [
    (
        "Trancendos Magna Carta",
        "Infinity Network — Magna Carta",
    ),
    (
        "the **Tranc3** is the governance and compliance foundation for the Tranc3 platform",
        "the **Infinity Network — Magna Carta** is the governance and compliance layer for applications built within the **Infinity Network**, harmonising with **Trancendos Universe — The Foundation**",
    ),
    (
        "governance and compliance foundation for the Tranc3 platform",
        "governance and compliance layer for Infinity Network applications, harmonising with Trancendos Universe — The Foundation",
    ),
    (
        "Tranc3 platform and Trancendos ecosystem services",
        "Infinity Network applications and Trancendos Universe ecosystem services",
    ),
    (
        "how Trancendos governs, secures, complies, and operates** the Tranc3 self-hosted AI platform",
        "how Trancendos governs, secures, complies, and operates** Infinity Network applications atop **Trancendos Universe — The Foundation**",
    ),
    (
        "connects governance intent to Tranc3 implementation",
        "connects governance intent to Infinity Network app implementations (e.g. Tranc3 App Framework)",
    ),
    (
        "Runtime enforcement hooks live in [Tranc3]",
        "Runtime enforcement hooks live in the [Tranc3 App Framework]",
    ),
    (
        "Tranc3 Integration Bridge",
        "Infinity App Bridge (Tranc3)",
    ),
    (
        "Tranc3 Register Bridge — Magna Carta",
        "Infinity App Bridge (Tranc3) — Magna Carta",
    ),
    (
        "Extensions to Tranc3 DEFSTAN Register",
        "Extensions to Infinity Network app DEFSTAN registers (Tranc3 exemplar)",
    ),
    (
        "Parent register: Tranc3 compliance/register.yaml",
        "Parent register (Tranc3 App): compliance/register.yaml in Tranc3 app repo",
    ),
    (
        'platform: "Tranc3 / Trancendos"',
        'platform: "Infinity Network — Magna Carta (Tranc3 App Framework exemplar)"',
    ),
    (
        "All regulations mapped to Tranc3 controls",
        "All regulations mapped to Infinity Network / Trancendos Universe controls",
    ),
    (
        "Tranc3 v2.1.0-rc1",
        "Tranc3 App Framework v2.1.0-rc1",
    ),
    (
        "Tranc3 Integration Config",
        "Infinity App (Tranc3) integration config",
    ),
    (
        "Tranc3 integration bridge",
        "Infinity App (Tranc3) bridge",
    ),
    (
        "Self-hosted Tranc3 stack",
        "Self-hosted Tranc3 App Framework stack",
    ),
    (
        "constitutional layer for digital products built on Tranc3",
        "constitutional layer for digital products built on Trancendos Universe and deployed as Infinity Network applications",
    ),
    (
        "establishes the constitutional layer for digital products built on Tranc3",
        "establishes the constitutional layer for digital products built on Trancendos Universe — The Foundation and deployed under the Infinity Network",
    ),
    (
        "(1) Tranc3 platform controls in code",
        "(1) Trancendos Universe / App Framework controls in code",
    ),
    (
        "**Scope:** Tranc3 platform and Trancendos-operated services",
        "**Scope:** Infinity Network applications and Trancendos-operated services",
    ),
    (
        "**Scope:** Tranc3 platform and Trancendos-operated processing activities",
        "**Scope:** Infinity Network applications and Trancendos-operated processing activities",
    ),
    (
        "**ISMS scope:** Tranc3 platform —",
        "**ISMS scope:** Trancendos Universe — The Foundation and Infinity Network applications —",
    ),
    (
        "across the Tranc3 platform and supporting systems",
        "across Trancendos Universe, Infinity Network applications, and supporting systems",
    ),
    (
        "to the Tranc3 platform",
        "to Trancendos Universe — The Foundation and Infinity Network App Frameworks (e.g. Tranc3)",
    ),
    (
        "| **Layer 1** Tranc3 platform |",
        "| **Layer 1** Trancendos Universe / App Framework (Tranc3 exemplar) |",
    ),
    (
        "Layer 1 Tranc3 platform",
        "Layer 1 Trancendos Universe / App Framework (Tranc3 exemplar)",
    ),
]


def should_process(path: Path) -> bool:
    if path.suffix not in EXTENSIONS:
        return False
    parts = path.parts
    if any(p in SKIP_DIRS for p in parts):
        return False
    # Skip migration script self and bridge field names (tranc3_requirements keys)
    if path.name == "apply_nomenclature.py":
        return False
    return True


def migrate_file(path: Path, dry_run: bool) -> int:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text == original:
        return 0
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or not should_process(path):
            continue
        changed += migrate_file(path, args.dry_run)
    mode = "would change" if args.dry_run else "changed"
    print(f"Nomenclature migration: {changed} files {mode}")


if __name__ == "__main__":
    main()
