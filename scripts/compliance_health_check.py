#!/usr/bin/env python3
"""
Magna Carta compliance documentation health check.

Reads compliance/maintenance_monitor.yaml and validates register freshness,
file existence, YAML parseability, README/index drift, and overdue actions.

Usage:
  python3 scripts/compliance_health_check.py [--report] [--strict] [--log] [--weekly-report]
  ./scripts/weekly_compliance_health.sh   # preferred weekly wrapper (zero CI cost)

Exit codes:
  0 — no errors (warnings allowed unless --strict treats warnings as errors)
  1 — one or more error-severity findings (or warnings with --strict)
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import UTC, date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


ROOT = Path(__file__).resolve().parent.parent


@dataclass
class Finding:
    check_id: str
    severity: str  # error | warning | info
    message: str


def load_monitor_config() -> dict:
    path = ROOT / "compliance" / "maintenance_monitor.yaml"
    if yaml is None:
        raise RuntimeError("PyYAML required: pip install pyyaml")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_required_files(cfg: dict, findings: list[Finding]) -> None:
    for item in cfg.get("required_files", []):
        rel = item["path"]
        full = ROOT / rel
        cid = item.get("check_id", "MON-001")
        if not full.is_file():
            findings.append(Finding(cid, "error", f"Missing required file: {rel}"))


def check_yaml_registers(cfg: dict, findings: list[Finding]) -> None:
    for item in cfg.get("yaml_registers", []):
        rel = item["path"]
        full = ROOT / rel
        cid = item.get("check_id", "MON-006")
        if not full.is_file():
            findings.append(Finding(cid, "error", f"Missing YAML register: {rel}"))
            continue
        try:
            with full.open(encoding="utf-8") as f:
                yaml.safe_load(f)
        except Exception as exc:  # noqa: BLE001
            findings.append(Finding(cid, "error", f"YAML parse failed {rel}: {exc}"))


def count_markdown_entries(index_path: Path, prefix: str) -> int:
    """Count procedure/policy files by glob; fallback to INDEX table rows."""
    if prefix == "count_policy_files":
        files = list((ROOT / "docs/policies").glob("POL-*.md"))
        return len(files)
    if prefix == "count_procedure_files":
        files = list((ROOT / "docs/procedures").glob("PROC-*.md"))
        return len(files)
    return 0


def check_index_drift(cfg: dict, findings: list[Finding]) -> None:
    for item in cfg.get("index_drift_checks", []):
        cid = item.get("check_id", "MON-004")
        readme = ROOT / item["readme_path"]
        pattern = item["pattern"]
        method = item["count_method"]
        if not readme.is_file():
            findings.append(Finding(cid, "error", f"README missing: {item['readme_path']}"))
            continue
        text = readme.read_text(encoding="utf-8")
        m = re.search(pattern, text)
        if not m:
            findings.append(Finding(cid, "warning", f"README pattern not found: {pattern}"))
            continue
        readme_count = int(m.group(1))
        actual = count_markdown_entries(ROOT / item["index_path"], method)
        if readme_count != actual:
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"README claims {readme_count} but found {actual} files ({method})",
                )
            )


def parse_dates_from_file(path: Path, patterns: list[str]) -> list[date]:
    text = path.read_text(encoding="utf-8")
    dates: list[date] = []
    for pat in patterns:
        for m in re.finditer(pat, text):
            try:
                dates.append(datetime.strptime(m.group(1), "%Y-%m-%d").date())
            except ValueError:
                continue
    return dates


def check_stale_reviews(cfg: dict, findings: list[Finding]) -> None:
    today = date.today()
    for block in cfg.get("stale_review_patterns", []):
        cid = block.get("check_id", "MON-002")
        max_age = block.get("max_age_days", cfg.get("settings", {}).get("default_max_age_days", 120))
        patterns = block.get("patterns", [])
        glob_pat = block.get("glob", "docs/**/*.md")
        for rel in ROOT.glob(glob_pat):
            if not rel.is_file():
                continue
            dates = parse_dates_from_file(rel, patterns)
            if not dates:
                continue
            latest = max(dates)
            age = (today - latest).days
            if age > max_age:
                findings.append(
                    Finding(
                        cid,
                        "warning",
                        f"Review date stale ({age}d > {max_age}d): {rel.relative_to(ROOT)} → {latest}",
                    )
                )


def check_overdue_actions(cfg: dict, findings: list[Finding]) -> None:
    block = cfg.get("action_overdue", {})
    if not block:
        return
    cid = block.get("check_id", "MON-003")
    src = ROOT / block["source"]
    statuses = set(block.get("statuses", ["Open"]))
    if not src.is_file() or yaml is None:
        return
    with src.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    today = date.today()
    for action in data.get("actions", []):
        if action.get("status") not in statuses:
            continue
        due_raw = action.get("due_date")
        if not due_raw:
            continue
        try:
            due = datetime.strptime(str(due_raw), "%Y-%m-%d").date()
        except ValueError:
            continue
        if due < today:
            aid = action.get("action_id", "?")
            findings.append(
                Finding(
                    cid,
                    "warning",
                    f"Overdue action {aid}: due {due}, status {action.get('status')}",
                )
            )


def load_health_history() -> dict:
    path = ROOT / "compliance" / "health_check_history.yaml"
    if not path.is_file() or yaml is None:
        return {"runs": [], "meta": {"cadence_days": 7}}
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("runs", [])
    return data


def append_health_log(
    findings: list[Finding],
    operator: str,
    exit_code: int,
) -> None:
    if yaml is None:
        return
    path = ROOT / "compliance" / "health_check_history.yaml"
    data = load_health_history()
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = sum(1 for f in findings if f.severity == "warning")
    run = {
        "timestamp": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "operator": operator,
        "errors": errors,
        "warnings": warnings,
        "exit_code": exit_code,
        "findings": [
            {"check_id": f.check_id, "severity": f.severity, "message": f.message}
            for f in findings
        ],
    }
    data["runs"].append(run)
    if len(data["runs"]) > 52:
        data["runs"] = data["runs"][-52:]
    if "meta" not in data:
        data["meta"] = {}
    data["meta"]["last_updated"] = date.today().isoformat()
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def check_weekly_cadence(cfg: dict, findings: list[Finding]) -> None:
    block = cfg.get("weekly_cadence", {})
    if not block:
        return
    cid = block.get("check_id", "MON-008")
    history = load_health_history()
    runs = history.get("runs", [])
    if not runs:
        findings.append(
            Finding(
                cid,
                "warning",
                "No weekly health check logged yet — run scripts/weekly_compliance_health.sh",
            )
        )
        return
    last_ts = runs[-1].get("timestamp", "")
    try:
        last_dt = datetime.strptime(last_ts[:10], "%Y-%m-%d").date()
    except ValueError:
        return
    cadence = block.get(
        "max_gap_days",
        history.get("meta", {}).get("cadence_days", 7),
    )
    gap = (date.today() - last_dt).days
    if gap > cadence:
        findings.append(
            Finding(
                cid,
                "warning",
                f"Last health check {gap}d ago (>{cadence}d cadence) — run weekly script",
            )
        )


def validate_register_schema(cfg: dict, findings: list[Finding]) -> None:
    """Lightweight structural validation without external jsonschema dependency."""
    import json

    for block in cfg.get("schema_validation", []):
        cid = block.get("check_id", "MON-009")
        rel = block["register"]
        schema_rel = block["schema"]
        reg_path = ROOT / rel
        schema_path = ROOT / schema_rel
        if not reg_path.is_file() or not schema_path.is_file() or yaml is None:
            continue
        with schema_path.open(encoding="utf-8") as f:
            schema = json.load(f)
        with reg_path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)
        required_top = schema.get("required", [])
        for key in required_top:
            if key not in data:
                findings.append(
                    Finding(cid, "error", f"{rel} missing required top-level key: {key}")
                )
        item_schema = (
            schema.get("properties", {})
            .get("actions", {})
            .get("items", {})
            .get("required", [])
        )
        if item_schema and "actions" in data:
            for action in data["actions"]:
                for field in item_schema:
                    if field not in action:
                        aid = action.get("action_id", "?")
                        findings.append(
                            Finding(
                                cid,
                                "error",
                                f"{rel} action {aid} missing field: {field}",
                            )
                        )


def check_cookbook_links(cfg: dict, findings: list[Finding]) -> None:
    for block in cfg.get("cookbook_links", []):
        cid = block.get("check_id", "MON-005")
        index_path = ROOT / block["index"]
        base = ROOT / block["base_dir"]
        if not index_path.is_file():
            findings.append(Finding(cid, "error", f"Missing index: {block['index']}"))
            continue
        text = index_path.read_text(encoding="utf-8")
        for m in re.finditer(r"\]\(([^)]+\.md)\)", text):
            target = m.group(1)
            if target.startswith("http"):
                continue
            full = (index_path.parent / target).resolve()
            if not full.is_file():
                findings.append(Finding(cid, "error", f"Broken link in {block['index']}: {target}"))


def run_checks(*, include_weekly_cadence: bool = False) -> list[Finding]:
    findings: list[Finding] = []
    cfg = load_monitor_config()
    if not include_weekly_cadence:
        cfg = {**cfg, "weekly_cadence": {}}
    check_required_files(cfg, findings)
    check_yaml_registers(cfg, findings)
    check_index_drift(cfg, findings)
    check_stale_reviews(cfg, findings)
    check_overdue_actions(cfg, findings)
    check_cookbook_links(cfg, findings)
    check_weekly_cadence(cfg, findings)
    validate_register_schema(cfg, findings)
    return findings


def print_report(findings: list[Finding]) -> None:
    if not findings:
        print("OK — no compliance documentation health findings.")
        return
    by_sev: dict[str, list[Finding]] = {"error": [], "warning": [], "info": []}
    for f in findings:
        by_sev.setdefault(f.severity, []).append(f)
    for sev in ("error", "warning", "info"):
        for f in by_sev.get(sev, []):
            print(f"[{sev.upper()}] {f.check_id}: {f.message}")
    print(f"\nSummary: {len(by_sev['error'])} errors, {len(by_sev['warning'])} warnings")


def main() -> int:
    parser = argparse.ArgumentParser(description="Magna Carta compliance health check")
    parser.add_argument("--report", action="store_true", help="Print human-readable report")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on warnings as well as errors",
    )
    parser.add_argument(
        "--log",
        action="store_true",
        help="Append run to compliance/health_check_history.yaml",
    )
    parser.add_argument(
        "--weekly-report",
        action="store_true",
        help="Include weekly cadence (MON-008) check in this run",
    )
    parser.add_argument(
        "--operator",
        default="local",
        help="Operator id recorded with --log (default: local)",
    )
    args = parser.parse_args()

    try:
        findings = run_checks(include_weekly_cadence=args.weekly_report)
    except Exception as exc:  # noqa: BLE001
        print(f"FATAL: {exc}", file=sys.stderr)
        return 1

    if args.report or findings:
        print_report(findings)

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]
    exit_code = 1 if errors or (args.strict and warnings) else 0

    if args.log:
        append_health_log(findings, args.operator, exit_code)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
