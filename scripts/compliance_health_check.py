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
import json
import os
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


def _validate_object_fields(
    cid: str,
    rel: str,
    obj: dict,
    required_fields: list[str],
    label: str,
    findings: list[Finding],
) -> None:
    for field in required_fields:
        if field not in obj:
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"{rel} {label} missing field: {field}",
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
        if not reg_path.is_file():
            findings.append(Finding(cid, "error", f"Register missing for schema check: {rel}"))
            continue
        if not schema_path.is_file():
            findings.append(Finding(cid, "error", f"Schema missing: {schema_rel}"))
            continue
        if yaml is None:
            continue
        with schema_path.open(encoding="utf-8") as f:
            schema = json.load(f)
        with reg_path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        for key in schema.get("required", []):
            if key not in data:
                findings.append(
                    Finding(cid, "error", f"{rel} missing required top-level key: {key}")
                )
        properties = schema.get("properties", {})
        meta_props = properties.get("meta", {})
        if isinstance(data.get("meta"), dict) and meta_props.get("type") == "object":
            _validate_object_fields(
                cid,
                rel,
                data["meta"],
                meta_props.get("required", []),
                "meta",
                findings,
            )
        for prop_name, prop_schema in properties.items():
            if prop_name == "meta":
                continue
            if prop_schema.get("type") != "array":
                continue
            items_schema = prop_schema.get("items", {})
            if items_schema.get("type") != "object":
                continue
            required_item_fields = items_schema.get("required", [])
            if not required_item_fields:
                continue
            items = data.get(prop_name)
            if not isinstance(items, list):
                findings.append(
                    Finding(cid, "error", f"{rel} missing or invalid array: {prop_name}")
                )
                continue
            id_field = next(
                (f for f in required_item_fields if f.endswith("_id") or f == "id"),
                None,
            )
            for idx, item in enumerate(items):
                if not isinstance(item, dict):
                    findings.append(
                        Finding(
                            cid,
                            "error",
                            f"{rel} {prop_name}[{idx}] is not an object",
                        )
                    )
                    continue
                label = prop_name
                if id_field and id_field in item:
                    label = f"{prop_name} item {item[id_field]}"
                _validate_object_fields(
                    cid,
                    rel,
                    item,
                    required_item_fields,
                    label,
                    findings,
                )


def check_procedure_coverage(cfg: dict, findings: list[Finding]) -> None:
    """Ensure every PROC-* has matching COOK-* and HYMN-* artefacts (MON-010)."""
    block = cfg.get("procedure_coverage", {})
    if not block:
        return
    cid = block.get("check_id", "MON-010")
    proc_dir = ROOT / block.get("procedures_dir", "docs/procedures")
    cook_dir = ROOT / block.get("cookbooks_dir", "docs/cookbooks")
    hymn_dir = ROOT / block.get("hymn_sheets_dir", "docs/hymn-sheets")
    pattern = block.get("code_pattern", r"PROC-([A-Z]+-\d+)")
    for proc in sorted(proc_dir.glob("PROC-*.md")):
        match = re.match(pattern, proc.name)
        if not match:
            findings.append(
                Finding(cid, "warning", f"Procedure filename not matched by MON-010: {proc.name}")
            )
            continue
        code = match.group(1)
        if not list(cook_dir.glob(f"COOK-{code}-*.md")):
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"No cookbook for {proc.name} (expected docs/cookbooks/COOK-{code}-*.md)",
                )
            )
        if not list(hymn_dir.glob(f"HYMN-{code}-*.md")):
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"No hymn sheet for {proc.name} (expected docs/hymn-sheets/HYMN-{code}-*.md)",
                )
            )


def _load_yaml(rel: str) -> dict:
    path = ROOT / rel
    if not path.is_file() or yaml is None:
        return {}
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _parse_iso_date(raw: str | None) -> date | None:
    if not raw:
        return None
    try:
        return datetime.strptime(str(raw)[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def _json_path_get(data: dict, dotted: str):
    cur = data
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def resolve_signal_states(signals_data: dict) -> dict[str, str]:
    """Return signal_id -> active|inactive."""
    states: dict[str, str] = {}
    for sig in signals_data.get("signals", []):
        sid = sig.get("signal_id", "")
        active = False
        for det in sig.get("detection", []):
            active_values = {str(v).lower() for v in det.get("active_values", [])}
            if det.get("source") == "config":
                cfg_path = ROOT / det.get("path", "")
                if cfg_path.is_file():
                    with cfg_path.open(encoding="utf-8") as f:
                        cfg_json = json.load(f)
                    val = _json_path_get(cfg_json, det.get("json_path", ""))
                    if val is not None and str(val).lower() in active_values:
                        active = True
                        break
            elif det.get("source") == "env":
                var = det.get("variable", "")
                val = os.environ.get(var)
                if val is not None and str(val).lower() in active_values:
                    active = True
                    break
        states[sid] = "active" if active else "inactive"
    return states


def check_register_review_dates(
    block: dict,
    findings: list[Finding],
    *,
    default_cid: str,
) -> None:
    if not block:
        return
    cid = block.get("check_id", default_cid)
    rel = block["register"]
    data = _load_yaml(rel)
    items_key = block.get("items_key", "")
    review_field = block.get("review_field", "review_date")
    exclude = {str(s).lower() for s in block.get("exclude_status", [])}
    max_overdue = block.get("max_overdue_days", 0)
    today = date.today()
    for item in data.get(items_key, []):
        status = str(item.get("status", "")).lower()
        if status in exclude:
            continue
        review_raw = item.get(review_field)
        review_dt = _parse_iso_date(review_raw)
        if review_dt is None:
            item_id = item.get("legislation_id") or item.get("standard_id") or "?"
            findings.append(
                Finding(
                    cid,
                    "warning",
                    f"{rel} item {item_id} missing or invalid {review_field}",
                )
            )
            continue
        overdue = (today - review_dt).days
        if overdue > max_overdue:
            item_id = item.get("legislation_id") or item.get("standard_id") or "?"
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"{rel} item {item_id} {review_field} overdue by {overdue}d "
                    f"(due {review_dt})",
                )
            )


def check_framework_readiness_docs(cfg: dict, findings: list[Finding]) -> None:
    block = cfg.get("framework_readiness", {})
    if not block:
        return
    cid = block.get("check_id", "MON-013")
    data = _load_yaml(block["register"])
    statuses = set(block.get("require_doc_for_status", []))
    applicabilities = set(block.get("require_doc_for_applicability", []))
    for fw in data.get(block.get("items_key", "frameworks"), []):
        status = fw.get("programme_status", "")
        applicability = fw.get("applicability", "")
        if status not in statuses and applicability not in applicabilities:
            continue
        doc = fw.get("readiness_doc")
        fid = fw.get("framework_id", "?")
        if not doc:
            findings.append(
                Finding(cid, "error", f"Framework {fid} missing readiness_doc")
            )
            continue
        if not (ROOT / doc).is_file():
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"Framework {fid} readiness_doc missing on disk: {doc}",
                )
            )


def check_supplier_dpa_gates(cfg: dict, findings: list[Finding]) -> None:
    block = cfg.get("supplier_dpa_gates", {})
    if not block:
        return
    cid = block.get("check_id", "MON-014")
    data = _load_yaml(block["register"])
    critical = set(block.get("critical_tiers", ["Critical"]))
    blocked = set(block.get("blocked_dpa_status", []))
    for sup in data.get(block.get("items_key", "suppliers"), []):
        if sup.get("risk_tier") not in critical:
            continue
        if sup.get("dpa_status") not in blocked:
            continue
        sid = sup.get("supplier_id", "?")
        findings.append(
            Finding(
                cid,
                "warning",
                f"Critical supplier {sid} ({sup.get('name')}) DPA status "
                f"'{sup.get('dpa_status')}' — gate before production scope",
            )
        )


def check_evidence_recurrence(cfg: dict, findings: list[Finding]) -> None:
    block = cfg.get("evidence_recurrence", {})
    if not block:
        return
    cid = block.get("check_id", "MON-015")
    data = _load_yaml(block["register"])
    today = date.today()
    for item in data.get(block.get("schedule_key", "recurrence_schedule"), []):
        due = _parse_iso_date(item.get("next_due"))
        if due is None:
            findings.append(
                Finding(
                    cid,
                    "warning",
                    f"Recurrence {item.get('evidence_id')} missing next_due",
                )
            )
            continue
        if due < today:
            eid = item.get("evidence_id", "?")
            overdue = (today - due).days
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"Recurring evidence {eid} overdue by {overdue}d (due {due})",
                )
            )


def check_enforcement_alignment(cfg: dict, findings: list[Finding]) -> None:
    block = cfg.get("enforcement_alignment", {})
    if not block:
        return
    cid = block.get("check_id", "MON-016")
    triggers = _load_yaml(block["triggers_register"])
    signals = _load_yaml(block["signals_register"])
    config_path = ROOT / block["runtime_config"]
    if not config_path.is_file():
        findings.append(Finding(cid, "error", f"Runtime config missing: {block['runtime_config']}"))
        return
    with config_path.open(encoding="utf-8") as f:
        runtime = json.load(f)
    enforcement = runtime.get("enforcement", {})
    mode = str(enforcement.get("mode", "advisory")).lower()
    fail_closed = bool(enforcement.get("fail_closed_on_violation", False))
    rules_by_id = {r["id"]: r for r in runtime.get("rules", []) if "id" in r}
    signal_states = resolve_signal_states(signals)
    action_data = _load_yaml("compliance/compliance_action_tracker.yaml")
    open_actions = {
        a.get("action_id")
        for a in action_data.get("actions", [])
        if a.get("status") in ("Open", "In progress", "Blocked")
    }
    for trig in triggers.get("triggers", []):
        sig_id = trig.get("signal_id", "")
        if signal_states.get(sig_id) != "active":
            continue
        on_act = trig.get("on_activate", {})
        tid = trig.get("trigger_id", "?")
        sev = "error"
        for sc in trig.get("scan_checks", []):
            if sc.get("check_id") == "MON-016":
                sev = sc.get("severity", "error")
                break
        expected_mode = str(on_act.get("enforcement_mode", "enforce")).lower()
        if mode != expected_mode:
            findings.append(
                Finding(
                    cid,
                    sev,
                    f"Trigger {tid}: signal {sig_id} active but enforcement.mode "
                    f"is '{mode}' (expected '{expected_mode}')",
                )
            )
        if on_act.get("fail_closed_on_violation") and not fail_closed:
            findings.append(
                Finding(
                    cid,
                    sev,
                    f"Trigger {tid}: signal {sig_id} active but "
                    "fail_closed_on_violation is false",
                )
            )
        for rule_id in on_act.get("rules_required_enabled", []):
            rule = rules_by_id.get(rule_id)
            if not rule or not rule.get("enabled", False):
                findings.append(
                    Finding(
                        cid,
                        sev,
                        f"Trigger {tid}: required rule {rule_id} not enabled",
                    )
                )
        for act_id in on_act.get("linked_actions", []):
            if act_id in open_actions:
                findings.append(
                    Finding(
                        cid,
                        "warning" if sev == "warning" else "error",
                        f"Trigger {tid}: linked action {act_id} still open while "
                        f"scope signal {sig_id} is active",
                    )
                )


def check_trigger_integrity(cfg: dict, findings: list[Finding]) -> None:
    block = cfg.get("trigger_integrity", {})
    if not block:
        return
    cid = block.get("check_id", "MON-017")
    triggers = _load_yaml(block["triggers_register"])
    signals = _load_yaml(block["signals_register"])
    frameworks = _load_yaml(block["frameworks_register"])
    signal_ids = {s.get("signal_id") for s in signals.get("signals", [])}
    framework_ids = {f.get("framework_id") for f in frameworks.get("frameworks", [])}
    for trig in triggers.get("triggers", []):
        tid = trig.get("trigger_id", "?")
        sig = trig.get("signal_id")
        if sig and sig not in signal_ids:
            findings.append(
                Finding(
                    cid,
                    "error",
                    f"Trigger {tid} references unknown signal {sig}",
                )
            )
        for fid in trig.get("framework_ids", []):
            if fid not in framework_ids:
                findings.append(
                    Finding(
                        cid,
                        "error",
                        f"Trigger {tid} references unknown framework {fid}",
                    )
                )


def check_proactive_monitoring(cfg: dict, findings: list[Finding]) -> None:
    """Run MON-011 through MON-017 from proactive_monitoring config."""
    pm = cfg.get("proactive_monitoring", {})
    if not pm:
        return
    check_register_review_dates(cfg.get("legislation_watch", {}), findings, default_cid="MON-011")
    check_register_review_dates(cfg.get("standards_watch", {}), findings, default_cid="MON-012")
    check_framework_readiness_docs(cfg, findings)
    check_supplier_dpa_gates(cfg, findings)
    check_evidence_recurrence(cfg, findings)
    check_enforcement_alignment(cfg, findings)
    check_trigger_integrity(cfg, findings)


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
    check_procedure_coverage(cfg, findings)
    check_weekly_cadence(cfg, findings)
    validate_register_schema(cfg, findings)
    check_proactive_monitoring(cfg, findings)
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
