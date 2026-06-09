#!/usr/bin/env python3
"""
DPA readiness check — Layer B controls for UK GDPR Art. 28 processing agreements.

Verifies templates, supplier register structure, and onboarding checklist presence.
Does not require signed DPAs (Layer C owner gate).

Usage:
  python3 scripts/dpa_readiness_check.py [--report]
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent

TEMPLATE_PATH = "docs/templates/TEMPLATE-DPA-UK-GDPR.md"
REGISTER_PATH = "compliance/supplier_dpa_register.yaml"
REQUIRED_SUPPLIER_FIELDS = [
    "supplier_id",
    "name",
    "risk_tier",
    "dpa_status",
    "transfer_mechanism",
    "review_date",
]
CRITICAL_STATUSES_OK_FOR_READINESS = {"Signed", "Template issued", "In negotiation", "Not required", "N/A"}


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def _load_register() -> dict:
    path = ROOT / REGISTER_PATH
    if not path.is_file() or yaml is None:
        return {}
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def run_checks() -> list[Check]:
    checks: list[Check] = []

    template = ROOT / TEMPLATE_PATH
    checks.append(
        Check(
            "dpa_template",
            template.is_file() and template.stat().st_size > 200,
            TEMPLATE_PATH if template.is_file() else f"missing {TEMPLATE_PATH}",
        )
    )

    data = _load_register()
    suppliers = data.get("suppliers", [])
    checks.append(
        Check(
            "supplier_register",
            bool(suppliers),
            f"{len(suppliers)} suppliers in register",
        )
    )

    missing_fields = 0
    invalid_status = 0
    critical_without_template_path = 0
    for sup in suppliers:
        for field in REQUIRED_SUPPLIER_FIELDS:
            if field not in sup:
                missing_fields += 1
        status = sup.get("dpa_status")
        if status not in CRITICAL_STATUSES_OK_FOR_READINESS:
            invalid_status += 1
        if sup.get("risk_tier") == "Critical" and status == "Template issued":
            if not sup.get("notes"):
                critical_without_template_path += 1

    checks.append(
        Check(
            "supplier_schema",
            missing_fields == 0,
            "all required fields present"
            if missing_fields == 0
            else f"{missing_fields} missing field values",
        )
    )
    checks.append(
        Check(
            "dpa_status_values",
            invalid_status == 0,
            "valid dpa_status enums"
            if invalid_status == 0
            else f"{invalid_status} invalid statuses",
        )
    )

    onboarding = data.get("onboarding_checklist")
    if onboarding is None:
        checks.append(
            Check(
                "onboarding_checklist",
                True,
                "optional onboarding_checklist not defined (register-only mode)",
            )
        )
    else:
        checks.append(
            Check(
                "onboarding_checklist",
                isinstance(onboarding, list) and len(onboarding) > 0,
                f"{len(onboarding) if isinstance(onboarding, list) else 0} checklist items",
            )
        )

    policy = data.get("meta", {}).get("policy")
    checks.append(
        Check(
            "policy_link",
            bool(policy) and (ROOT / policy).is_file(),
            policy or "missing policy reference",
        )
    )

    if critical_without_template_path:
        checks.append(
            Check(
                "critical_supplier_notes",
                False,
                f"{critical_without_template_path} critical suppliers lack negotiation notes",
            )
        )

    return checks


def print_report(checks: list[Check]) -> None:
    passed = sum(1 for c in checks if c.passed)
    print(f"DPA readiness: {passed}/{len(checks)} checks passed (Layer B)")
    for check in checks:
        mark = "OK" if check.passed else "FAIL"
        print(f"  [{mark}] {check.name}: {check.detail}")


def main() -> int:
    parser = argparse.ArgumentParser(description="DPA readiness check")
    parser.add_argument("--report", action="store_true", help="Print human-readable report")
    args = parser.parse_args()

    if yaml is None:
        print("FATAL: PyYAML required", file=sys.stderr)
        return 1

    checks = run_checks()
    if args.report or not checks:
        print_report(checks)

    if all(c.passed for c in checks):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
