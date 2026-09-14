#!/usr/bin/env python3
"""Matrix Suites register validation — Layer B check.

Validates compliance/matrix_suites.yaml against its documented invariants
(docs/governance/MATRIX-SUITES.md §1–§2):

  * every suite carries suite_id, name, pillar, steward_ai, steward_location,
    presiding_prime, review_cadence, next_review, observatory_events, kpi
  * pillar is one of the platform's 8 Pillar values
  * every matrix appears in exactly one suite (no orphan check is possible from
    this repo alone for Tranc3-side files, so uniqueness is the enforced half;
    magna-carta-side paths must exist on disk)
  * next_review dates that have passed are WARNINGS (overdue review), matching
    the ACT-006 precedent — structural problems are ERRORS.

Exit 0 on success (warnings allowed), 1 on structural error.
"""

from __future__ import annotations

import datetime as _dt
import sys
from pathlib import Path

import yaml
import typing

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "compliance" / "matrix_suites.yaml"

# Mirror of Tranc3 src/entities/platform.py Pillar enum values. Kept literal here
# because this repo must validate standalone; drift fails loudly in review since
# both lists are tiny and named identically.
PILLARS = {
    "Architectural",
    "Commercial / Financial",
    "Creativity",
    "Development (Code)",
    "Knowledge",
    "Security",
    "DevOps",
    "Wellbeing",
}

REQUIRED_SUITE_FIELDS = [
    "suite_id",
    "name",
    "pillar",
    "steward_ai",
    "steward_location",
    "presiding_prime",
    "review_cadence",
    "next_review",
    "observatory_events",
    "kpi",
    "matrices",
]


def check_matrix(
    m: dict[str, typing.Any],
    sid: str,
    seen_matrix_ids: dict[str, str],
    errors: list[str],
) -> None:
    mid = m.get("id")
    if not mid:
        errors.append(f"{sid}: matrix entry without id")
        return
    if mid in seen_matrix_ids:
        errors.append(
            f"matrix {mid} assigned to both {seen_matrix_ids[mid]} and {sid} "
            f"— every matrix must have exactly one governing suite"
        )
    seen_matrix_ids[mid] = sid
    if m.get("repo") == "magna-carta":
        path = ROOT / str(m.get("path", ""))
        if not path.is_file():
            errors.append(f"{sid}: {mid} path does not exist: {m.get('path')}")


def check_suite(
    suite: dict[str, typing.Any],
    seen_suite_ids: set[str],
    today: _dt.date,
    seen_matrix_ids: dict[str, str],
    errors: list[str],
    warnings: list[str],
) -> None:
    sid = suite.get("suite_id", "<missing suite_id>")
    if sid in seen_suite_ids:
        errors.append(f"duplicate suite_id {sid}")
    seen_suite_ids.add(sid)

    for field in REQUIRED_SUITE_FIELDS:
        if not suite.get(field):
            errors.append(f"{sid}: missing required field '{field}'")

    pillar = suite.get("pillar")
    if pillar and pillar not in PILLARS:
        errors.append(f"{sid}: pillar '{pillar}' is not a platform Pillar")

    nr = suite.get("next_review")
    if nr:
        try:
            due = _dt.date.fromisoformat(str(nr))
            if due < today:
                warnings.append(f"{sid}: review overdue (next_review {due})")
        except ValueError:
            errors.append(f"{sid}: next_review '{nr}' is not an ISO date")

    for m in suite.get("matrices") or []:
        check_matrix(m, sid, seen_matrix_ids, errors)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not REGISTER.is_file():
        print(f"ERROR: {REGISTER.relative_to(ROOT)} missing", file=sys.stderr)
        return 1

    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8")) or {}
    suites = data.get("suites") or []
    if not suites:
        print("ERROR: no suites defined", file=sys.stderr)
        return 1

    seen_matrix_ids: dict[str, str] = {}
    seen_suite_ids: set[str] = set()
    today = _dt.date.today()

    for suite in suites:
        check_suite(suite, seen_suite_ids, today, seen_matrix_ids, errors, warnings)

    for line in warnings:
        print(f"[WARNING] {line}")
    for line in errors:
        print(f"[ERROR] {line}", file=sys.stderr)

    print(
        f"Matrix Suites: {len(suites)} suites, {len(seen_matrix_ids)} matrices, "
        f"{len(warnings)} warning(s), {len(errors)} error(s)"
    )
    if errors:
        print("Matrix suites check: FAILED", file=sys.stderr)
        return 1
    print("Matrix suites check: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
