#!/usr/bin/env python3
"""
Layer B automation & systems readiness scorer.

Verifies agent-executable controls in compliance/readiness_automation_register.yaml.
Owner go-live gates (Layer C) are listed but excluded from the percentage.

Usage:
  python3 scripts/readiness_automation_score.py [--report] [--json]
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class ItemResult:
    item_id: str
    title: str
    status: str
    passed: bool
    detail: str


def _load_yaml(rel: str) -> dict:
    path = ROOT / rel
    if not path.is_file() or yaml is None:
        return {}
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _path_exists(rel: str | None) -> bool:
    if not rel:
        return False
    return (ROOT / rel).exists()


def _verify_item(item: dict) -> ItemResult:
    item_id = item.get("item_id", "?")
    title = item.get("title", "")
    declared = item.get("status", "pending")
    verification = item.get("verification", "")
    evidence = item.get("evidence")

    if declared == "not_applicable":
        return ItemResult(item_id, title, declared, True, "not applicable")

    paths_to_check: list[str] = []
    if verification:
        paths_to_check.append(verification)
    if evidence:
        paths_to_check.append(evidence)

    if not paths_to_check:
        return ItemResult(
            item_id,
            title,
            declared,
            declared == "implemented",
            "no verification path configured",
        )

    missing = [p for p in paths_to_check if not _path_exists(p)]
    if missing:
        return ItemResult(
            item_id,
            title,
            declared,
            False,
            f"missing: {', '.join(missing)}",
        )

    return ItemResult(item_id, title, declared, True, "verified on disk")


def scan_certification_vault() -> dict:
    cert_reg = _load_yaml("compliance/certification_evidence_register.yaml")
    root_rel = cert_reg.get("meta", {}).get("evidence_root", "docs/evidence/certifications")
    root = ROOT / root_rel
    uploaded = 0
    pending = 0
    slots = cert_reg.get("slots", [])
    slot_results: list[dict] = []

    files_on_disk: list[str] = []
    if root.is_dir():
        files_on_disk = [p.name for p in root.iterdir() if p.is_file() and not p.name.startswith(".")]

    for slot in slots:
        status = slot.get("status", "pending_upload")
        pattern = slot.get("expected_filename_pattern", "*")
        matched = [f for f in files_on_disk if fnmatch.fnmatch(f.lower(), pattern.lower())]
        if status == "not_applicable":
            slot_results.append(
                {
                    "cert_id": slot.get("cert_id"),
                    "status": status,
                    "files": [],
                }
            )
            continue
        if matched:
            uploaded += 1
            slot_results.append(
                {
                    "cert_id": slot.get("cert_id"),
                    "status": "uploaded",
                    "files": matched,
                }
            )
        else:
            pending += 1
            slot_results.append(
                {
                    "cert_id": slot.get("cert_id"),
                    "status": status,
                    "files": [],
                }
            )

    return {
        "evidence_root": root_rel,
        "uploaded": uploaded,
        "pending": pending,
        "not_applicable": sum(1 for s in slots if s.get("status") == "not_applicable"),
        "slots": slot_results,
        "layer": "C",
        "notes": "Cert uploads are owner gates; they do not reduce Layer B percent.",
    }


def count_owner_gates() -> dict:
    tracker = _load_yaml("compliance/compliance_action_tracker.yaml")
    open_statuses = {"Open", "In progress", "Blocked"}
    owner_open = 0
    system_open = 0
    for action in tracker.get("actions", []):
        if action.get("status") not in open_statuses:
            continue
        executor = action.get("executor", "owner")
        if executor == "owner":
            owner_open += 1
        else:
            system_open += 1
    return {
        "owner_gates_open": owner_open,
        "system_actions_open": system_open,
        "layer": "C",
    }


def score_readiness() -> dict:
    reg = _load_yaml("compliance/readiness_automation_register.yaml")
    items = reg.get("items", [])
    results = [_verify_item(item) for item in items]
    scorable = [r for r in results if r.status != "not_applicable"]
    passed = [r for r in scorable if r.passed]
    total = len(scorable)
    pct = round((len(passed) / total) * 100, 1) if total else 0.0

    return {
        "layer": "B",
        "layer_name": reg.get("meta", {}).get("layer", "automation_systems_readiness"),
        "target_percent": reg.get("meta", {}).get("target_percent", 100),
        "automation_readiness_percent": pct,
        "items_total": total,
        "items_passed": len(passed),
        "items_failed": total - len(passed),
        "items": [
            {
                "item_id": r.item_id,
                "title": r.title,
                "status": r.status,
                "passed": r.passed,
                "detail": r.detail,
            }
            for r in results
        ],
        "certification_vault": scan_certification_vault(),
        "owner_gates": count_owner_gates(),
    }


def print_report(report: dict) -> None:
    pct = report["automation_readiness_percent"]
    print(f"Layer B automation readiness: {pct}% ({report['items_passed']}/{report['items_total']})")
    print(f"Target: {report['target_percent']}% — agent-verifiable scope only")
    print()
    failed = [i for i in report["items"] if not i["passed"] and i["status"] != "not_applicable"]
    if failed:
        print("Failed items:")
        for item in failed:
            print(f"  - {item['item_id']}: {item['detail']}")
        print()
    vault = report["certification_vault"]
    print(
        f"Certification vault (Layer C): {vault['uploaded']} uploaded, "
        f"{vault['pending']} pending_upload, {vault['not_applicable']} N/A"
    )
    gates = report["owner_gates"]
    print(
        f"Owner go-live gates open (Layer C): {gates['owner_gates_open']} "
        f"(not scored against Layer B)"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Layer B automation readiness scorer")
    parser.add_argument("--report", action="store_true", help="Print human-readable report")
    parser.add_argument("--json", action="store_true", help="Print JSON report")
    args = parser.parse_args()

    if yaml is None:
        print("FATAL: PyYAML required", file=sys.stderr)
        return 1

    report = score_readiness()
    if args.json:
        print(json.dumps(report, indent=2))
    if args.report or not args.json:
        print_report(report)

    target = report.get("target_percent", 100)
    if report["automation_readiness_percent"] < target:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
