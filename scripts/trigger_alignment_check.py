#!/usr/bin/env python3
"""Trigger↔framework alignment validation — Layer B check.

The signal→trigger→framework chain is what makes conditional compliance work:
an operator enables a scope profile, the signal activates, the trigger names the
framework_ids that come into force. Nothing verified that the frameworks a
trigger names are the frameworks it is *about*.

They were not. Four triggers activated unrelated frameworks:

  * TRG-HIPAA-001 activated FW-063 (FERPA — education law), not FW-062
    (HIPAA Security Rule), while carrying HIPAA-specific enforcement
    (MC-RULE-009, SUP-005, ACT-002/006)
  * TRG-DORA-001  activated FW-090 (MPA) and FW-091 (ABS OSPAR), not FW-100 (DORA)
  * TRG-NHS-001   activated FW-064 (IRS Pub 1075) and FW-065 (SEC Rule 17a-4(f)),
    not FW-089 (NHS DSPT)
  * TRG-CMMC-001  activated the DoD Impact Levels but not FW-053 (CMMC 2.0),
    FW-042 (its NIST SP 800-171/172 control basis) or FW-059 (DFARS flow-down)

The cause was mechanical: scripts/generate_framework_implementation.py assigned
frameworks first-match-wins in SIGNAL_GROUPS order, so category sweeps that
appear earlier in the list claimed framework IDs out from under the signals that
named them explicitly, and the named signals silently inherited whatever the
sweeps had skipped. Fixed there; this check is what stops it returning.

Checks
------
ERROR   every framework_id a trigger names exists in frameworks_register.yaml
ERROR   a trigger whose ID carries a framework's name activates at least one
        framework whose register name carries that name (see ANCHORS)
WARN    frameworks in the register that no trigger references at all
WARN    catalog entries whose trigger_id does not in fact list them

The ANCHORS check is deliberately narrow. It cannot judge whether a *scope*
signal (SIG-US-GOV-001, SIG-EU-INDUSTRY-001) has drawn a sensible boundary —
that is a governance question. It only asserts the tautology that a trigger
named after a framework must activate that framework, which is the exact defect
above and is mechanically decidable.

Exit 0 on success (warnings allowed), 1 on structural error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TRIGGERS = ROOT / "compliance" / "framework_triggers.yaml"
FRAMEWORKS = ROOT / "compliance" / "frameworks_register.yaml"
CATALOG = ROOT / "compliance" / "framework_implementation_catalog.yaml"

# trigger_id -> token that must appear as a WHOLE WORD in at least one activated
# framework's register name (case-insensitive). Only triggers named after a
# specific framework or framework family belong here; scope-named triggers are
# listed in UNANCHORED below because no single framework name corresponds to
# them.
#
# Whole-word, not substring: a bare substring test is safe for the long tokens
# but wrong for short ones. "AI" appears inside "ENS High (Spain)",
# "CCN CPSTIC (Spain)", "Taiwan PDPA" and "Thailand PDPA" — so under substring
# matching TRG-AI-001 would pass while activating nothing about AI, which is
# precisely the failure this check exists to catch. Verified against the current
# register: whole-word changes the match set for "AI" only (9 substring hits to
# 4 genuine ones) and is identical for the other 14 anchors.
#
# "OWASP GenAI / LLM Top 10" is a genuine AI framework that whole-word does not
# match. That costs nothing here: the check asks whether *at least one*
# activated framework carries the token, and four others do.
ANCHORS = {
    "TRG-GDPR-001": "GDPR",
    "TRG-PECR-001": "PECR",
    "TRG-ISO-001": "ISO",
    "TRG-SOC-001": "SOC",
    "TRG-NIST-001": "NIST",
    "TRG-PCI-001": "PCI",
    "TRG-HIPAA-001": "HIPAA",
    "TRG-CCPA-001": "CCPA",
    "TRG-FEDRAMP-001": "FedRAMP",
    "TRG-LGPD-001": "LGPD",
    "TRG-POPIA-001": "POPIA",
    "TRG-DORA-001": "DORA",
    "TRG-NHS-001": "NHS",
    "TRG-CMMC-001": "CMMC",
    "TRG-AI-001": "AI",
}

# Triggers deliberately left unanchored: their name describes a *scope*, not a
# framework, so there is no token to look for in any framework name. Listed
# explicitly rather than left implicit so that a newly added trigger falls into
# neither set and gets reported — see _unanchored_warning below. A trigger must
# appear in exactly one of ANCHORS or UNANCHORED.
UNANCHORED = {
    "TRG-CORE-001",
    "TRG-US-GOV-001",
    "TRG-EU-INDUSTRY-001",
    "TRG-INTL-ASSURANCE-001",
    "TRG-GLOBAL-PRIVACY-001",
    "TRG-PAYMENTS-001",
    "TRG-AI-US-001",
}


def anchor_matches(token: str, name: str) -> bool:
    """True when `token` appears as a whole word in `name`, case-insensitively."""
    return re.search(rf"\b{re.escape(token)}\b", name, re.IGNORECASE) is not None


def _load(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f"missing register: {path.relative_to(ROOT)}")
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML — {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{path.relative_to(ROOT)}: root must be a mapping")
        return {}
    return data


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    triggers_doc = _load(TRIGGERS, errors)
    frameworks_doc = _load(FRAMEWORKS, errors)
    catalog_doc = _load(CATALOG, errors)
    if errors:
        for line in errors:
            print(f"[ERROR] {line}", file=sys.stderr)
        return 1

    fw_name = {
        f["framework_id"]: f.get("name") or ""
        for f in (frameworks_doc.get("frameworks") or [])
        if isinstance(f, dict) and f.get("framework_id")
    }
    triggers = [t for t in (triggers_doc.get("triggers") or []) if isinstance(t, dict)]
    if not triggers:
        print("[ERROR] framework_triggers.yaml: 'triggers' must be a non-empty list", file=sys.stderr)
        return 1

    referenced: set[str] = set()
    activated_by: dict[str, list[str]] = {}

    for trig in triggers:
        tid = trig.get("trigger_id") or "<unnamed trigger>"
        fids = trig.get("framework_ids")
        if not isinstance(fids, list):
            errors.append(f"{tid}: 'framework_ids' must be a list")
            continue
        activated_by[tid] = fids
        for fid in fids:
            referenced.add(fid)
            if fid not in fw_name:
                errors.append(
                    f"{tid}: references unknown framework {fid!r} — not defined in "
                    f"frameworks_register.yaml"
                )

        if tid not in ANCHORS and tid not in UNANCHORED:
            warnings.append(
                f"{tid}: classified in neither ANCHORS nor UNANCHORED, so nothing checks "
                f"that it activates what its name implies. Add it to ANCHORS with the "
                f"framework token its name refers to, or to UNANCHORED if it names a scope "
                f"rather than a framework."
            )

        anchor = ANCHORS.get(tid)
        if anchor:
            names = [fw_name.get(fid, "") for fid in fids]
            if not any(anchor_matches(anchor, n) for n in names):
                shown = ", ".join(f"{f}={fw_name.get(f, '?')}" for f in fids) or "nothing"
                errors.append(
                    f"{tid} is named after {anchor!r} but activates none of it — "
                    f"activates {shown}. Enabling this scope would enforce "
                    f"frameworks the operator did not ask for while leaving "
                    f"{anchor} inactive."
                )

    orphans = sorted(set(fw_name) - referenced)
    if orphans:
        warnings.append(
            f"{len(orphans)} framework(s) referenced by no trigger, so no scope "
            f"signal can activate them: " + ", ".join(orphans)
        )

    # The catalog names, per framework, the trigger that is supposed to activate
    # it. Where that trigger does not list the framework, the two registers
    # disagree and the catalog is the one that is wrong.
    mismatched: list[str] = []
    for entry in catalog_doc.get("entries") or []:
        if not isinstance(entry, dict):
            continue
        fid = entry.get("framework_id")
        tid = entry.get("trigger_id")
        if not fid or not tid or tid not in activated_by:
            continue
        if fid not in activated_by[tid]:
            mismatched.append(f"{fid}→{tid}")
    if mismatched:
        warnings.append(
            f"{len(mismatched)} catalog entr(ies) name a trigger that does not list "
            f"them, so their stated activation path does not exist: "
            + ", ".join(mismatched[:12])
            + (" …" if len(mismatched) > 12 else "")
            + ". Resolving this needs a governance decision on the tier vocabulary "
            "(implementation_tier has no value for 'defined but not reachable'), "
            "so it is reported rather than failed."
        )

    for line in warnings:
        print(f"[WARNING] {line}")
    for line in errors:
        print(f"[ERROR] {line}", file=sys.stderr)

    print(
        f"Trigger alignment: {len(triggers)} trigger(s), {len(referenced)} framework "
        f"reference(s) across {len(fw_name)} defined framework(s), "
        f"{len(ANCHORS)} anchored trigger(s), {len(warnings)} warning(s), "
        f"{len(errors)} error(s)"
    )
    if errors:
        print("Trigger alignment check: FAILED", file=sys.stderr)
        return 1
    print("Trigger alignment check: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
