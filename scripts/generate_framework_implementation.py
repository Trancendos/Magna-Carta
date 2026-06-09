#!/usr/bin/env python3
"""Generate framework_implementation_catalog.yaml and validate FW coverage."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# New matrix-only frameworks (STD-* without FW-*)
NEW_FRAMEWORKS = [
    {
        "framework_id": "FW-133",
        "name": "EU AI Act (2024/1689)",
        "category": "eu_industry",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/AI-GOVERNANCE.md",
    },
    {
        "framework_id": "FW-134",
        "name": "UK PECR",
        "category": "global_privacy",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/PECR-ALIGNMENT.md",
    },
    {
        "framework_id": "FW-135",
        "name": "CIS Controls v8",
        "category": "nist",
        "applicability": "reference",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/readiness/NIST-FAMILY-READINESS.md",
    },
    {
        "framework_id": "FW-136",
        "name": "OWASP Top 10 (2021)",
        "category": "nist",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/REGULATION-MATRIX.md",
    },
    {
        "framework_id": "FW-137",
        "name": "OWASP ASVS Level 2",
        "category": "nist",
        "applicability": "conditional",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/ASVS-GAP-CHECKLIST.md",
    },
    {
        "framework_id": "FW-138",
        "name": "NIST AI RMF 1.0",
        "category": "nist",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/AI-GOVERNANCE.md",
    },
    {
        "framework_id": "FW-139",
        "name": "ITIL 4",
        "category": "iso_ms",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/REGULATION-MATRIX.md",
    },
    {
        "framework_id": "FW-140",
        "name": "PRINCE2 7",
        "category": "iso_ms",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/REGULATION-MATRIX.md",
    },
    {
        "framework_id": "FW-141",
        "name": "UK Research Integrity Concordat",
        "category": "eu_industry",
        "applicability": "reference",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/REGULATION-MATRIX.md",
    },
    {
        "framework_id": "FW-142",
        "name": "ISO/IEC 27002:2022",
        "category": "iso_ms",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/readiness/ISO-FAMILY-READINESS.md",
    },
    {
        "framework_id": "FW-143",
        "name": "UK Companies Act 2006 (governance)",
        "category": "global_privacy",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/COMPANIES-ACT-ALIGNMENT.md",
    },
    {
        "framework_id": "FW-144",
        "name": "OWASP GenAI / LLM Top 10",
        "category": "eu_industry",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/AI-SECURITY-THREAT-MODEL.md",
    },
    {
        "framework_id": "FW-145",
        "name": "DEF STAN 05-138 (standalone)",
        "category": "nist",
        "applicability": "applicable",
        "programme_status": "programme",
        "readiness_doc": "docs/compliance/DEFSTAN-ALIGNMENT.md",
    },
]

NA_DOC = "docs/compliance/readiness/NOT-APPLICABLE-POSITION.md"

# Signal groups: prefix match on framework_id ranges / explicit lists
SIGNAL_GROUPS: list[dict] = [
    {
        "signal_id": "SIG-CORE-001",
        "trigger_id": "TRG-CORE-001",
        "name": "Platform baseline",
        "config_key": "CORE_PLATFORM",
        "default_active": True,
        "framework_filter": lambda fw: fw.get("applicability") == "applicable"
        and fw.get("framework_id")
        not in {
            "FW-110",
            "FW-133",
            "FW-134",
            "FW-138",
            "FW-144",
            "FW-132",
            "FW-131",
            "FW-005",
        },
    },
    {
        "signal_id": "SIG-GDPR-001",
        "trigger_id": "TRG-GDPR-001",
        "name": "UK/EU GDPR scope",
        "config_key": "GDPR_SCOPE",
        "default_active": True,
        "framework_ids": ["FW-110", "FW-004"],
    },
    {
        "signal_id": "SIG-AI-001",
        "trigger_id": "TRG-AI-001",
        "name": "AI governance scope",
        "config_key": "AI_GOVERNANCE",
        "default_active": True,
        "framework_ids": [
            "FW-005",
            "FW-131",
            "FW-132",
            "FW-133",
            "FW-138",
            "FW-144",
        ],
    },
    {
        "signal_id": "SIG-PECR-001",
        "trigger_id": "TRG-PECR-001",
        "name": "UK PECR / ePrivacy",
        "config_key": "PECR_SCOPE",
        "default_active": True,
        "framework_ids": ["FW-134"],
    },
    {
        "signal_id": "SIG-ISO-001",
        "trigger_id": "TRG-ISO-001",
        "name": "ISO certification pursuit",
        "config_key": "ISO_CERTIFICATION_SCOPE",
        "default_active": False,
        "category": "iso_ms",
        "exclude_applicability": ["not_applicable"],
    },
    {
        "signal_id": "SIG-SOC-001",
        "trigger_id": "TRG-SOC-001",
        "name": "SOC assurance track",
        "config_key": "SOC_AUDIT_SCOPE",
        "default_active": False,
        "category": "soc_assurance",
        "exclude_applicability": ["not_applicable"],
    },
    {
        "signal_id": "SIG-NIST-001",
        "trigger_id": "TRG-NIST-001",
        "name": "NIST family baseline",
        "config_key": "NIST_BASELINE",
        "default_active": True,
        "category": "nist",
        "exclude_applicability": ["not_applicable"],
    },
    {
        "signal_id": "SIG-GLOBAL-PRIVACY-001",
        "trigger_id": "TRG-GLOBAL-PRIVACY-001",
        "name": "International privacy pack",
        "config_key": "GLOBAL_PRIVACY_PACK",
        "default_active": False,
        "category": "global_privacy",
        "applicability": ["not_applicable", "conditional"],
        "exclude_ids": ["FW-110", "FW-112", "FW-116", "FW-130", "FW-134"],
    },
    {
        "signal_id": "SIG-INTL-ASSURANCE-001",
        "trigger_id": "TRG-INTL-ASSURANCE-001",
        "name": "International assurance bids",
        "config_key": "INTL_ASSURANCE_SCOPE",
        "default_active": False,
        "category": "international_assurance",
    },
    {
        "signal_id": "SIG-US-GOV-001",
        "trigger_id": "TRG-US-GOV-001",
        "name": "US government readiness",
        "config_key": "US_GOV_SCOPE",
        "default_active": False,
        "category": "us_government",
        "exclude_applicability": ["not_applicable"],
    },
    {
        "signal_id": "SIG-EU-INDUSTRY-001",
        "trigger_id": "TRG-EU-INDUSTRY-001",
        "name": "EU industry sector",
        "config_key": "EU_INDUSTRY_SCOPE",
        "default_active": False,
        "category": "eu_industry",
        "exclude_ids": ["FW-005", "FW-131", "FW-132", "FW-133", "FW-144"],
    },
    {
        "signal_id": "SIG-PCI-001",
        "trigger_id": "TRG-PCI-001",
        "name": "Cardholder data environment",
        "config_key": "PCI_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-030", "FW-031", "FW-032", "FW-033"],
    },
    {
        "signal_id": "SIG-HIPAA-001",
        "trigger_id": "TRG-HIPAA-001",
        "name": "HIPAA health data profile",
        "config_key": "HIPAA_PROFILE",
        "default_active": False,
        "framework_ids": ["FW-062", "FW-063"],
    },
    {
        "signal_id": "SIG-CCPA-001",
        "trigger_id": "TRG-CCPA-001",
        "name": "California consumer data scope",
        "config_key": "CCPA_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-112"],
    },
    {
        "signal_id": "SIG-FEDRAMP-001",
        "trigger_id": "TRG-FEDRAMP-001",
        "name": "US federal government workload",
        "config_key": "FEDRAMP_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-050", "FW-051", "FW-052"],
    },
    {
        "signal_id": "SIG-LGPD-001",
        "trigger_id": "TRG-LGPD-001",
        "name": "Brazil data subject scope",
        "config_key": "LGPD_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-116"],
    },
    {
        "signal_id": "SIG-POPIA-001",
        "trigger_id": "TRG-POPIA-001",
        "name": "South Africa POPIA",
        "config_key": "POPIA_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-130"],
    },
    {
        "signal_id": "SIG-AI-US-001",
        "trigger_id": "TRG-AI-US-001",
        "name": "US AI inference fallback",
        "config_key": "US_AI_FALLBACK",
        "default_active": False,
        "framework_ids": ["FW-004", "FW-112"],
    },
    {
        "signal_id": "SIG-PAYMENTS-001",
        "trigger_id": "TRG-PAYMENTS-001",
        "name": "Production payment routing",
        "config_key": "PAYMENTS_LIVE",
        "default_active": False,
        "framework_ids": ["FW-030"],
    },
    {
        "signal_id": "SIG-DORA-001",
        "trigger_id": "TRG-DORA-001",
        "name": "DORA financial sector",
        "config_key": "DORA_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-090", "FW-091"],
    },
    {
        "signal_id": "SIG-NHS-001",
        "trigger_id": "TRG-NHS-001",
        "name": "NHS DSPT / health UK",
        "config_key": "NHS_DSPT_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-064", "FW-065"],
    },
    {
        "signal_id": "SIG-CMMC-001",
        "trigger_id": "TRG-CMMC-001",
        "name": "CMMC defense contractors",
        "config_key": "CMMC_SCOPE",
        "default_active": False,
        "framework_ids": ["FW-055", "FW-056", "FW-057"],
    },
]

ON_ACTIVATE_BASELINE = {
    "enforcement_mode": "enforce",
    "fail_closed_on_violation": True,
    "rules_required_enabled": ["MC-RULE-001", "MC-RULE-002", "MC-RULE-006"],
    "programme_status_expect": "programme",
}

ON_ACTIVATE_ADVISORY = {
    "enforcement_mode": "advisory",
    "fail_closed_on_violation": False,
    "programme_status_expect": "programme",
}


def load_frameworks() -> dict:
    path = ROOT / "compliance" / "frameworks_register.yaml"
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def assign_frameworks_to_groups(frameworks: list[dict]) -> dict[str, str]:
    """Map framework_id -> signal_id (first match wins)."""
    fw_by_id = {f["framework_id"]: f for f in frameworks}
    assignment: dict[str, str] = {}
    for group in SIGNAL_GROUPS:
        sig = group["signal_id"]
        if "framework_ids" in group:
            for fid in group["framework_ids"]:
                if fid in fw_by_id and fid not in assignment:
                    assignment[fid] = sig
        elif "framework_filter" in group:
            for fw in frameworks:
                fid = fw["framework_id"]
                if fid not in assignment and group["framework_filter"](fw):
                    assignment[fid] = sig
        else:
            for fw in frameworks:
                fid = fw["framework_id"]
                if fid in assignment:
                    continue
                if group.get("category") and fw.get("category") != group["category"]:
                    continue
                if fid in group.get("exclude_ids", []):
                    continue
                app = fw.get("applicability")
                if "applicability" in group and app not in group["applicability"]:
                    continue
                if app in group.get("exclude_applicability", []):
                    continue
                assignment[fid] = sig
    return assignment


def update_frameworks_register(data: dict) -> None:
    frameworks = data["frameworks"]
    existing_ids = {f["framework_id"] for f in frameworks}
    for nf in NEW_FRAMEWORKS:
        if nf["framework_id"] not in existing_ids:
            frameworks.append(nf)
    na_ids = {"FW-011", "FW-028", "FW-058", "FW-068"}
    for fw in frameworks:
        if fw["framework_id"] in na_ids:
            fw["readiness_doc"] = NA_DOC
        if fw.get("programme_status") == "readiness" and fw.get("readiness_doc"):
            if fw.get("applicability") != "not_applicable":
                fw["programme_status"] = "programme"
    data["meta"]["framework_count"] = len(frameworks)
    data["meta"]["last_updated"] = "2026-06-09"
    path = ROOT / "compliance" / "frameworks_register.yaml"
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True, width=120)


def build_catalog(frameworks: list[dict], assignment: dict[str, str]) -> dict:
    entries = []
    for fw in frameworks:
        fid = fw["framework_id"]
        app = fw.get("applicability", "")
        status = fw.get("programme_status", "")
        if app == "not_applicable" and status == "not_applicable":
            tier = "excluded"
            sig = None
            trig = None
        elif app in ("reference", "awareness"):
            tier = "reference"
            sig = assignment.get(fid)
            trig = f"TRG-{sig.split('-')[1]}-{sig.split('-')[2]}" if sig else None
        elif assignment.get(fid):
            sig = assignment.get(fid)
            tier = "signal_gated"
            trig = next(
                (g["trigger_id"] for g in SIGNAL_GROUPS if g["signal_id"] == sig),
                None,
            )
        else:
            tier = "baseline"
            sig = "SIG-CORE-001"
            trig = "TRG-CORE-001"
        group = next((g for g in SIGNAL_GROUPS if g["signal_id"] == sig), None) if sig else None
        entries.append(
            {
                "framework_id": fid,
                "name": fw.get("name"),
                "implementation_tier": tier,
                "signal_id": sig,
                "trigger_id": trig,
                "auto_checks": ["MON-013", "MON-018"],
                "readiness_doc": fw.get("readiness_doc"),
                "programme_status": status,
                "applicability": app,
                "config_profile": group["config_key"] if group else None,
            }
        )
    return {
        "meta": {
            "register_version": "1.0.0",
            "owner": "ISMS Lead",
            "last_updated": "2026-06-09",
            "review_cycle": "quarterly",
            "frameworks_register": "compliance/frameworks_register.yaml",
            "signals_register": "compliance/proactive_signals.yaml",
            "triggers_register": "compliance/framework_triggers.yaml",
            "entry_count": len(entries),
        },
        "schema": {
            "implementation_tier": "baseline | signal_gated | reference | excluded",
            "signal_id": "SIG-XXX-### when scope-gated",
            "trigger_id": "TRG-XXX-### when scope-gated",
        },
        "entries": entries,
    }


def build_signals() -> dict:
    signals = []
    for g in SIGNAL_GROUPS:
        signals.append(
            {
                "signal_id": g["signal_id"],
                "name": g["name"],
                "description": f"Scope signal for {g['name']}",
                "default_state": "active" if g.get("default_active") else "inactive",
                "detection": [
                    {
                        "source": "config",
                        "path": "config/magna_carta_config.json",
                        "json_path": f"profiles.{g['config_key']}",
                        "active_values": ["enabled", "true", "1"],
                    },
                    {
                        "source": "env",
                        "variable": g["config_key"],
                        "active_values": ["enabled", "true", "1"],
                    },
                ],
            }
        )
    return {
        "meta": {
            "register_version": "1.1.0",
            "owner": "ISMS Lead",
            "last_updated": "2026-06-09",
            "review_cycle": "quarterly",
            "runtime_config": "config/magna_carta_config.json",
            "trigger_register": "compliance/framework_triggers.yaml",
        },
        "schema": {
            "signal_id": "SIG-XXX-### unique identifier",
            "state": "inactive | active | unknown",
        },
        "signals": signals,
    }


def build_triggers(frameworks: list[dict], assignment: dict[str, str]) -> dict:
    # Group framework ids by signal
    by_signal: dict[str, list[str]] = {}
    for fid, sig in assignment.items():
        by_signal.setdefault(sig, []).append(fid)
    # Unassigned applicable/conditional get CORE
    for fw in frameworks:
        fid = fw["framework_id"]
        if fid in assignment:
            continue
        if fw.get("applicability") in ("applicable", "conditional") and fw.get(
            "programme_status"
        ) != "not_applicable":
            by_signal.setdefault("SIG-CORE-001", []).append(fid)

    triggers = []
    existing_special = {
        "TRG-HIPAA-001",
        "TRG-CCPA-001",
        "TRG-PCI-001",
        "TRG-FEDRAMP-001",
        "TRG-LGPD-001",
        "TRG-AI-US-001",
        "TRG-PAYMENTS-001",
    }
    for g in SIGNAL_GROUPS:
        fids = sorted(set(by_signal.get(g["signal_id"], g.get("framework_ids", []))))
        if not fids:
            continue
        on_act = dict(ON_ACTIVATE_BASELINE)
        if g["signal_id"] in ("SIG-CORE-001", "SIG-GDPR-001", "SIG-AI-001", "SIG-NIST-001", "SIG-PECR-001"):
            # Baseline signals default active — advisory until operator enables enforce profile
            on_act = dict(ON_ACTIVATE_ADVISORY)
            on_act["rules_required_enabled"] = ["MC-RULE-001", "MC-RULE-002"]
        if g["signal_id"] == "SIG-HIPAA-001":
            on_act.update(
                {
                    "rules_required_enabled": ["MC-RULE-009"],
                    "supplier_dpa_required": ["SUP-005"],
                    "linked_actions": ["ACT-002", "ACT-006"],
                }
            )
        if g["signal_id"] == "SIG-PCI-001":
            on_act.update(
                {
                    "rules_required_enabled": ["MC-RULE-001", "MC-RULE-002", "MC-RULE-006"],
                    "supplier_dpa_required": ["SUP-003"],
                    "linked_actions": ["ACT-001"],
                    "programme_status_expect": "partial",
                }
            )
        if g["signal_id"] == "SIG-CCPA-001":
            on_act.update(
                {
                    "readiness_doc": "docs/compliance/CCPA-CPRA-ALIGNMENT.md",
                    "rules_required_enabled": ["MC-RULE-002", "MC-RULE-008"],
                }
            )
        if g["signal_id"] == "SIG-FEDRAMP-001":
            on_act.update(
                {
                    "readiness_doc": "docs/compliance/readiness/US-GOVERNMENT-READINESS.md",
                    "rules_required_enabled": ["MC-RULE-001", "MC-RULE-006", "MC-RULE-007"],
                }
            )
        if g["signal_id"] == "SIG-LGPD-001":
            on_act.update(
                {
                    "readiness_doc": "docs/compliance/LGPD-READINESS.md",
                    "rules_required_enabled": ["MC-RULE-002", "MC-RULE-008"],
                }
            )
        if g["signal_id"] == "SIG-AI-US-001":
            on_act.update(
                {
                    "rules_required_enabled": ["MC-RULE-004", "MC-RULE-005"],
                    "supplier_dpa_required": ["SUP-004"],
                    "linked_actions": ["ACT-010"],
                }
            )
        if g["signal_id"] == "SIG-PAYMENTS-001":
            on_act = {
                "enforcement_mode": "enforce",
                "fail_closed_on_violation": True,
                "supplier_dpa_required": ["SUP-003"],
                "linked_actions": ["ACT-001"],
                "rules_required_enabled": ["MC-RULE-001", "MC-RULE-006"],
            }
        triggers.append(
            {
                "trigger_id": g["trigger_id"],
                "signal_id": g["signal_id"],
                "framework_ids": fids,
                "on_activate": on_act,
                "scan_checks": [
                    {"check_id": "MON-016", "severity": "error"},
                    {"check_id": "MON-018", "severity": "error"},
                ],
            }
        )
    return {
        "meta": {
            "register_version": "1.1.0",
            "owner": "ISMS Lead",
            "last_updated": "2026-06-09",
            "review_cycle": "quarterly",
            "signals_register": "compliance/proactive_signals.yaml",
            "frameworks_register": "compliance/frameworks_register.yaml",
            "implementation_catalog": "compliance/framework_implementation_catalog.yaml",
            "runtime_config": "config/magna_carta_config.json",
        },
        "defaults": {
            "enforcement_mode": "advisory",
            "fail_closed_on_violation": False,
            "description": (
                "Safe default — optional frameworks remain programme until an operator "
                "enables a scope signal. Health check escalates when signal is active "
                "but enforcement profile does not match on_activate requirements."
            ),
        },
        "triggers": triggers,
        "proactive_scans": {
            "description": (
                "Scheduled programme scans independent of scope signals. "
                "Health check enforces recurrence via execution_evidence_register."
            ),
            "items": [
                {
                    "scan_id": "SCAN-LEG-001",
                    "register": "compliance/legislation_register.yaml",
                    "field": "review_date",
                    "max_overdue_days": 0,
                    "check_id": "MON-011",
                    "cadence_days": 90,
                    "linked_evidence": "EEV-006",
                },
                {
                    "scan_id": "SCAN-STD-001",
                    "register": "compliance/standards_watch.yaml",
                    "field": "review_date",
                    "max_overdue_days": 0,
                    "check_id": "MON-012",
                    "cadence_days": 180,
                    "linked_evidence": "EEV-007",
                },
            ],
        },
    }


def update_config_profiles() -> None:
    path = ROOT / "config" / "magna_carta_config.json"
    with path.open(encoding="utf-8") as f:
        cfg = json.load(f)
    profiles = cfg.setdefault("profiles", {})
    for g in SIGNAL_GROUPS:
        key = g["config_key"]
        if key not in profiles:
            profiles[key] = "enabled" if g.get("default_active") else "disabled"
    cfg["meta"]["last_updated"] = "2026-06-09"
    with path.open("w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
        f.write("\n")


def main() -> None:
    data = load_frameworks()
    update_frameworks_register(data)
    data = load_frameworks()
    frameworks = data["frameworks"]
    assignment = assign_frameworks_to_groups(frameworks)
    catalog = build_catalog(frameworks, assignment)
    signals = build_signals()
    triggers = build_triggers(frameworks, assignment)
    update_config_profiles()

    for rel, content in [
        ("compliance/framework_implementation_catalog.yaml", catalog),
        ("compliance/proactive_signals.yaml", signals),
        ("compliance/framework_triggers.yaml", triggers),
    ]:
        path = ROOT / rel
        with path.open("w", encoding="utf-8") as f:
            yaml.dump(content, f, sort_keys=False, allow_unicode=True, width=120)

    covered = len(assignment)
    unassigned = [
        f["framework_id"]
        for f in frameworks
        if f["framework_id"] not in assignment
        and f.get("applicability") in ("applicable", "conditional")
    ]
    print(f"Frameworks: {len(frameworks)}")
    print(f"Assigned to signals: {covered}")
    print(f"Unassigned applicable/conditional: {unassigned}")


if __name__ == "__main__":
    main()
