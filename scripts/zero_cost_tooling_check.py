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


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Zero-cost tooling register check")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--strict", action="store_true", help="Fail on optional tool hints")
    return parser.parse_args()


def _check_tools(tools: list[dict], args: argparse.Namespace) -> tuple[int, list[str], list[str]]:
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

    return passed, errors, warnings


def _check_optional_binaries(args: argparse.Namespace) -> None:
    for binary, tool_id in [("gitleaks", "ZCT-007"), ("bandit", "ZCT-008"), ("semgrep", "ZCT-009")]:
        if shutil.which(binary):
            if args.report:
                print(f"  OK  {tool_id} {binary} found on PATH")
        elif args.report:
            print(f"  --  {tool_id} {binary} not installed (optional)")


def _print_report(passed: int, mandatory_count: int, errors: list[str], warnings: list[str], args: argparse.Namespace) -> None:
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


def _print_final_status(errors: list[str], warnings: list[str], args: argparse.Namespace) -> None:
    if args.report and not errors:
        print("Zero-cost tooling check: PASSED")


def main() -> int:
    args = _parse_args()

    data = _load_register()
    tools = data.get("tools", [])

    passed, errors, warnings = _check_tools(tools, args)

    # Optional OSS binaries — informational only
    _check_optional_binaries(args)

    mandatory_count = sum(1 for t in tools if t.get("mandatory"))
    _print_report(passed, mandatory_count, errors, warnings, args)

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    _print_final_status(errors, warnings, args)
    return 0

if __name__ == "__main__":
    sys.exit(main())
