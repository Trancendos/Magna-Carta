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
    parser.add_argument(
        "--strict", action="store_true", help="Fail on optional tool hints"
    )
    return parser.parse_args()


def _check_tools(
    tools: list[dict], args: argparse.Namespace
) -> tuple[int, list[str], list[str]]:
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
                warnings.append(
                    f"{tool_id} ({name}): optional path missing {check_path}"
                )
            continue

        passed += 1
        if args.report:
            tag = "mandatory" if mandatory else "optional"
            print(f"  OK  {tool_id} [{tag}] {check_path}")

    return passed, errors, warnings


def _optional_binaries(tools: list[dict]) -> list[tuple[str, str]]:
    """(binary, tool_id) for every optional tool the OSS scan script invokes.

    Read from the register rather than hardcoded. The hardcoded list named
    ZCT-007, -008 and -009 and had fallen behind ZCT-010 (pip-audit), which is in
    the register with the same `invoked_by` as the other three and whose presence
    was therefore never reported at all (codeant-ai). A list that must be kept in
    step with a register by hand is a list that eventually is not.
    """
    out = []
    for tool in tools:
        tool_id = tool.get("tool_id")
        if tool.get("mandatory") or not tool_id:
            continue
        if "run_oss_security_scans.sh" not in str(tool.get("invoked_by", "")):
            continue
        binary = tool.get("binary")
        if not binary:
            # Named explicitly in the register, not inferred from the install
            # prose: ZCT-007's install field is a URL and a sentence, so any
            # guess at it is wrong. A tool with no `binary` is reported rather
            # than quietly dropped, which is how ZCT-010 went unnoticed.
            print(f"  --  {tool_id} has no 'binary' in the register; cannot check PATH")
            continue
        out.append((str(binary), tool_id))
    return out


def _check_optional_binaries(args: argparse.Namespace, tools: list[dict]) -> None:
    for binary, tool_id in _optional_binaries(tools):
        if shutil.which(binary):
            if args.report:
                print(f"  OK  {tool_id} {binary} found on PATH")
        elif args.report:
            print(f"  --  {tool_id} {binary} not installed (optional)")


def _print_report(
    passed: int,
    mandatory_count: int,
    errors: list[str],
    warnings: list[str],
    args: argparse.Namespace,
) -> None:
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


def main() -> int:
    args = _parse_args()

    data = _load_register()
    tools = data.get("tools", [])

    passed, errors, warnings = _check_tools(tools, args)

    # Optional OSS binaries — informational only
    _check_optional_binaries(args, tools)

    mandatory_count = sum(1 for t in tools if t.get("mandatory"))
    _print_report(passed, mandatory_count, errors, warnings, args)

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    if args.report:
        print("Zero-cost tooling check: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
