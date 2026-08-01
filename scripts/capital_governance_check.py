#!/usr/bin/env python3
"""Validate compliance/capital_governance.yaml.

Layer B check. Structural errors FAIL; advisory observations WARN — matching the
ACT-006 precedent used by the other registers in this repository.

The unusual check here is `_check_is_generic`. Magna Carta is meant to be a
governance layer any solution can adopt, which only holds if its rules do not
name one adopter's entities. That property degrades silently: someone adds a
convenient reference to a specific platform, nothing breaks, and the layer stops
being portable one line at a time. This makes that regression a build failure.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - Layer B installs requirements first
    print("ERROR: pyyaml required", file=sys.stderr)
    raise SystemExit(2) from None

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "compliance" / "capital_governance.yaml"

# Proper nouns belonging to specific adopters rather than to governance. This
# list is the enforcement of the "generic layer" principle, so it is deliberately
# concrete: a vague rule would not catch anything.
PLATFORM_SPECIFIC_TERMS = [
    "Trancendos",
    "Tranc3",
    "trancendos.com",
    "Arcadian",
    "Porter",
    "Town Hall",
    "TownHall",
    "CranBania",
    "Dorris Fontaine",
    "Cornelius",
    "Cryptex",
    "The Observatory",
]

# Fields whose whole purpose is to say "an adopter fills this in". A placeholder
# naturally mentions the adopter concept without naming one, so scanning them
# for adopter names would flag the very mechanism that keeps the file generic.
_PLACEHOLDER_RE = re.compile(r"<[^>]+>")


def _check_is_generic(raw: str) -> list[str]:
    """No adopter-specific proper noun may appear anywhere in the register."""
    errors: list[str] = []
    for lineno, line in enumerate(raw.splitlines(), start=1):
        scannable = _PLACEHOLDER_RE.sub("", line)
        for term in PLATFORM_SPECIFIC_TERMS:
            if term.lower() in scannable.lower():
                errors.append(
                    f"line {lineno}: contains platform-specific term {term!r} — this "
                    "register must stay adoptable by any platform. Move the reference "
                    "into the adopting platform's binding file and refer to a role_id "
                    "or function_id here instead."
                )
    return errors


def _check_ledger_separation(doc: dict) -> list[str]:
    errors: list[str] = []
    fts = doc.get("function_types") or []
    if not fts:
        return ["function_types is empty — nothing is governed"]

    seen: dict[str, str] = {}
    for ft in fts:
        fid = ft.get("function_id", "<unnamed>")
        ledger = ft.get("ledger")
        if not ledger:
            errors.append(f"function_type {fid} declares no ledger")
            continue
        if ledger in seen:
            errors.append(
                f"function_type {fid} shares ledger {ledger!r} with {seen[ledger]} — "
                "separate ledgers per function type is the core control; sharing one "
                "lets a loss in the risk-bearing function consume the operating budget"
            )
        seen[ledger] = fid

    sep = doc.get("ledger_separation") or {}
    if not sep.get("enforced"):
        errors.append("ledger_separation.enforced must be true")
    if (sep.get("transfers") or {}).get("permitted"):
        errors.append(
            "ledger_separation.transfers.permitted must be false — transfers are an "
            "exception requiring named authority, not a default"
        )
    return errors


def _check_tier_ladder(doc: dict) -> tuple[list[str], list[str]]:
    """Tiers must form a contiguous ascending ladder with no gaps or overlaps."""
    errors: list[str] = []
    warnings: list[str] = []
    tiers = doc.get("capital_tiers") or []
    if not tiers:
        return ["capital_tiers is empty"], warnings

    known_functions = {ft.get("function_id") for ft in (doc.get("function_types") or [])}
    gate_ids = {g.get("gate_id") for g in (doc.get("progression_gates") or [])}

    prev_max = None
    for tier in tiers:
        tid = tier.get("tier_id", "<unnamed>")
        lo, hi = tier.get("band_min_units"), tier.get("band_max_units")

        if lo is None:
            errors.append(f"{tid}: band_min_units is required")
        elif prev_max is not None and lo != prev_max:
            errors.append(
                f"{tid}: band starts at {lo} but the previous tier ends at {prev_max} — "
                "a gap leaves equity in no tier, an overlap puts it in two"
            )
        if hi is not None and lo is not None and hi <= lo:
            errors.append(f"{tid}: band_max_units {hi} must exceed band_min_units {lo}")
        prev_max = hi

        for fn in tier.get("permitted_functions") or []:
            if fn not in known_functions:
                errors.append(f"{tid}: permitted_functions names unknown function {fn!r}")

        gate = tier.get("progression_gate")
        if gate is not None and gate not in gate_ids:
            errors.append(f"{tid}: progression_gate {gate!r} is not declared")

        if tier.get("leverage_permitted") and (tier.get("max_leverage") or 0) <= 1.0:
            warnings.append(f"{tid}: leverage_permitted is true but max_leverage <= 1.0")
        if not tier.get("leverage_permitted") and (tier.get("max_leverage") or 1.0) > 1.0:
            errors.append(
                f"{tid}: leverage_permitted is false but max_leverage is "
                f"{tier.get('max_leverage')} — the cap contradicts the permission"
            )

    if prev_max is not None:
        errors.append(
            "the final tier must have band_max_units: null — a closed top band leaves "
            "equity above it ungoverned"
        )
    return errors, warnings


def _check_roles_and_switches(doc: dict) -> list[str]:
    errors: list[str] = []
    role_ids = {r.get("role_id") for r in (doc.get("roles") or [])}
    if not role_ids:
        return ["roles is empty — every rule references a role slot"]

    def _require_role(value, where: str) -> None:
        if value and value not in role_ids:
            errors.append(f"{where} references undeclared role {value!r}")

    _require_role(
        (doc.get("ledger_separation") or {}).get("exception_authority"),
        "ledger_separation.exception_authority",
    )

    for gate in doc.get("progression_gates") or []:
        gid = gate.get("gate_id", "<unnamed>")
        req = gate.get("requires") or {}
        _require_role(req.get("approval"), f"{gid}.requires.approval")
        _require_role(req.get("live_capital_approval"), f"{gid}.requires.live_capital_approval")

    for switch in doc.get("kill_switches") or []:
        sid = switch.get("switch_id", "<unnamed>")
        if not switch.get("trigger"):
            errors.append(f"kill switch {sid} declares no trigger")
        if not switch.get("release_authority"):
            errors.append(
                f"kill switch {sid} declares no release_authority — a switch nobody is "
                "named to release either never releases or anyone releases it"
            )
        _require_role(switch.get("release_authority"), f"kill switch {sid}.release_authority")

    protected = set((doc.get("binding") or {}).get("must_not_override") or [])
    for required in ("ledger_separation", "kill_switches"):
        if required not in protected:
            errors.append(
                f"binding.must_not_override omits {required!r} — an adopter could then "
                "relax the control locally, which defeats it"
            )
    return errors


def main() -> int:
    if not REGISTER.exists():
        print(f"ERROR: {REGISTER} not found", file=sys.stderr)
        return 1

    raw = REGISTER.read_text(encoding="utf-8")
    doc = yaml.safe_load(raw) or {}

    errors: list[str] = []
    warnings: list[str] = []

    errors += _check_is_generic(raw)
    errors += _check_ledger_separation(doc)
    tier_errors, tier_warnings = _check_tier_ladder(doc)
    errors += tier_errors
    warnings += tier_warnings
    errors += _check_roles_and_switches(doc)

    for line in warnings:
        print(f"[WARNING] {line}")
    for line in errors:
        print(f"[ERROR] {line}", file=sys.stderr)

    if errors:
        print("Capital governance check: FAILED", file=sys.stderr)
        return 1

    tiers = len(doc.get("capital_tiers") or [])
    fns = len(doc.get("function_types") or [])
    print(
        f"Capital governance check: PASSED "
        f"({fns} function types, {tiers} tiers, {len(warnings)} warning(s))"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
