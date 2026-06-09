#!/usr/bin/env python3
"""
Verify zero-cost tooling register (ZCT-###) — mandatory tools exist on disk.

Usage:
  python3 scripts/zero_cost_tooling_check.py [--report] [--strict]
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "compliance/zero_cost_tooling_register.yaml"


def _load_register() -> dict:
    if yaml is None or not REGISTER.is_file():
        return {}
    with REGISTER.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Zero-cost tooling register check")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--strict", action="store_true", help="Fail on optional tool hints")
    args = parser.parse_args()

    data = _load_register()
    tools = data.get("tools", [])
    errors: list[str] = []
    warnings: list[str] = []
    passed = 0

    for tool in tools:
        tool_id = tool.get("tool_id", "?")
        name = tool.get("name", "")
        mandatory = tool.get("mandatory", False)
        path_rel = tool.get("path")
        invoked_by = tool.get("invoked_by")

        check_path = path_rel or invoked_by
        if not check_path:
            if mandatory:
                errors.append(f"{tool_id}: mandatory tool missing path")
            continue

        full = ROOT / check_path
        if not full.is_file():
            if mandatory:
                errors.append(f"{tool_id} ({name}): missing {check_path}")
            else:
                warnings.append(f"{tool_id} ({name}): optional path missing {check_path}")
            continue

        passed += 1
        if args.report:
            tag = "mandatory" if mandatory else "optional"
            print(f"  OK  {tool_id} [{tag}] {check_path}")

    # Optional OSS binaries — informational only
    for binary, tool_id in [("gitleaks", "ZCT-007"), ("bandit", "ZCT-008"), ("semgrep", "ZCT-009")]:
        if shutil.which(binary):
            if args.report:
                print(f"  OK  {tool_id} {binary} found on PATH")
        elif args.report:
            print(f"  --  {tool_id} {binary} not installed (optional)")

    mandatory_count = sum(1 for t in tools if t.get("mandatory"))
    if args.report:
        print()
        print(f"Zero-cost register: {passed} tool paths verified")
        print(f"Mandatory tools in register: {mandatory_count}")
        if errors:
            print(f"Errors: {len(errors)}")
            for e in errors:
                print(f"  ERROR: {e}")
        if warnings and args.strict:
            for w in warnings:
                print(f"  WARN: {w}")

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    if args.report and not errors:
        print("Zero-cost tooling check: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
