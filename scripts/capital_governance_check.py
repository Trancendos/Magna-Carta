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

# Controls a binding may never relax. Kept as one constant because the register,
# CAPITAL-GOVERNANCE.md and this check must agree on the list: an earlier version
# hardcoded only two of the three named at the time here, so an adopter could have
# dropped `demotion` from must_not_override and passed CI — quietly acquiring the
# ability to keep a failing operator's permissions. `evidence` was added later for
# the same reason it belongs here: progression_gates decide promotion from the
# decision journal evidence describes, so a binding that could weaken the journal
# defeats gate integrity without ever touching a gate.
NON_OVERRIDABLE_CONTROLS = ("ledger_separation", "demotion", "kill_switches", "evidence")

# Proper nouns belonging to specific adopters rather than to governance. This
# list is the enforcement of the "generic layer" principle, so it is deliberately
# concrete: a vague rule would not catch anything.
#
# MAINTENANCE: this is a denylist, and its honest limitation is that it cannot
# catch an adopter name nobody has added to it. That is unavoidable — a layer
# that is generic by definition cannot enumerate the adopters it does not know
# about. It is still worth having, because the realistic failure mode is not an
# unknown platform appearing: it is *this* estate's own vocabulary leaking in
# while someone edits the file. Add a term whenever a new adopter-specific proper
# noun enters the wider repository, and prefer over-listing to under-listing —
# a false positive costs one rename, a false negative costs portability.
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

# Whole-word matching, not substring containment. "Porter" as a bare substring
# also fires inside "reporter", "supporter" and "transporter", which would fail
# the build on ordinary prose and make the register hostile to edit — and a check
# people learn to work around is worse than no check. \b handles the multi-word
# terms too, anchoring only at the outer edges.
_TERM_PATTERNS = [
    (term, re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE))
    for term in PLATFORM_SPECIFIC_TERMS
]


def _check_is_generic(raw: str) -> list[str]:
    """No adopter-specific proper noun may appear anywhere in the register.

    Scans the raw line, including inside `<placeholder>` text. An earlier
    version stripped `<...>` content before scanning on the theory that
    placeholders only ever say "an adopter fills this in" — but that also
    exempted a placeholder that names a real adopter, e.g. `<bound by
    Trancendos>`, from the check whose entire job is to catch exactly that.
    """
    errors: list[str] = []
    for lineno, line in enumerate(raw.splitlines(), start=1):
        for term, pattern in _TERM_PATTERNS:
            if pattern.search(line):
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
    # Literal True, not truthiness. A quoted "false" is a non-empty string —
    # truthy in Python — and `not sep.get("enforced")` would have let it pass
    # as if the control were still switched on.
    if sep.get("enforced") is not True:
        errors.append("ledger_separation.enforced must be true")
    # Must be the literal boolean False, not merely falsy. A missing `transfers`
    # block or a missing `permitted` key would previously pass this check by
    # never being truthy, leaving the one exception to ledger separation with no
    # stated default at all — silence must not read as "not permitted".
    if (sep.get("transfers") or {}).get("permitted") is not False:
        errors.append(
            "ledger_separation.transfers.permitted must be false — transfers are an "
            "exception requiring named authority, not a default"
        )
    return errors


def _check_required_flags(doc: dict) -> list[str]:
    """`enforced` / `required` flags gate the register's other load-bearing
    controls, the same way ledger_separation.enforced does. Checked against
    the literal boolean True for the same reason: a quoted "false" is a
    truthy string and must not read as the control still being on.
    """
    errors: list[str] = []
    checks = [
        (doc.get("demotion") or {}, "enforced", "demotion.enforced"),
        (
            (doc.get("evidence") or {}).get("decision_journal") or {},
            "required",
            "evidence.decision_journal.required",
        ),
        (doc.get("binding") or {}, "required", "binding.required"),
    ]
    for container, key, label in checks:
        if container.get(key) is not True:
            errors.append(f"{label} must be true")
    return errors


def _check_unique_ids(doc: dict) -> list[str]:
    """Every *_id field is a reference key used elsewhere in the register. A
    set comprehension (as roles/gates lookups use to build their reference
    sets) silently discards duplicates, so a second entry sharing an ID would
    pass every "is this ID declared" check while leaving the reference
    genuinely ambiguous — nothing says which of the two entries a rule that
    names that ID actually means.
    """
    errors: list[str] = []
    id_specs = [
        ("roles", "role_id"),
        ("function_types", "function_id"),
        ("capital_tiers", "tier_id"),
        ("progression_gates", "gate_id"),
        ("kill_switches", "switch_id"),
    ]
    for list_key, id_key in id_specs:
        seen: set = set()
        for item in doc.get(list_key) or []:
            value = item.get(id_key)
            if value is None:
                continue
            if value in seen:
                errors.append(
                    f"{list_key}: duplicate {id_key} {value!r} — every entry "
                    "needs a unique id, or references to it are ambiguous"
                )
            seen.add(value)
    return errors


def _check_hard_authorities(doc: dict) -> list[str]:
    """Some authority slots are not "any declared role" — they are the human
    checkpoints the layer is built around. _require_role (used elsewhere)
    only checks that a referenced role exists, which would let an adopter
    legally point one of these at capital_operator: the role exists, so the
    weaker check passes, while the checkpoint the field exists to provide is
    defeated. These are checked against the specific role they require.
    """
    errors: list[str] = []

    transfers = (doc.get("ledger_separation") or {}).get("transfers") or {}
    exception_authority = transfers.get("exception_authority")
    if exception_authority is not None and exception_authority != "human_owner":
        errors.append(
            "ledger_separation.transfers.exception_authority must be "
            "human_owner — the one sanctioned ledger crossing is a human "
            "checkpoint by design, not a role any declared actor may hold"
        )

    for gate in doc.get("progression_gates") or []:
        gid = gate.get("gate_id", "<unnamed>")
        req = gate.get("requires") or {}
        if req.get("approval") == "capital_operator":
            errors.append(
                f"{gid}.requires.approval is capital_operator — an operator "
                "cannot approve its own promotion"
            )
        live = req.get("live_capital_approval")
        if live is not None and live != "human_owner":
            errors.append(
                f"{gid}.requires.live_capital_approval must be human_owner "
                "when set — it exists to require a checkpoint above "
                "presiding_authority, not a delegatable role"
            )

    # The ledger boundary switch is the one release authority this register
    # names as needing human_owner specifically, in its own rationale text —
    # a crossing that trips it means the ledger_separation control itself may
    # have failed, which is not a call any automated role gets to make. Other
    # never-auto-release switches (e.g. limit_override_attempt) legitimately
    # use presiding_authority; the invariant that applies to all of them is
    # the capital_operator check below, not a blanket human_owner rule.
    HUMAN_OWNER_RELEASE_SWITCHES = ("ledger_boundary_violation",)

    for switch in doc.get("kill_switches") or []:
        sid = switch.get("switch_id", "<unnamed>")
        release_authority = switch.get("release_authority")
        if release_authority == "capital_operator":
            errors.append(
                f"kill switch {sid}.release_authority is capital_operator — "
                "the actor a switch exists to stop cannot also be the one "
                "who releases it"
            )
        elif sid in HUMAN_OWNER_RELEASE_SWITCHES and release_authority != "human_owner":
            errors.append(
                f"kill switch {sid}.release_authority must be human_owner, "
                f"got {release_authority!r} — this switch's own rationale is "
                "that a ledger-boundary crossing is not a call any automated "
                "role gets to make"
            )

    return errors


def _check_tier_ladder(doc: dict) -> tuple[list[str], list[str]]:
    """Tiers must form a contiguous ascending ladder with no gaps or overlaps,
    starting at 0 and left open (band_max_units: null) only at the final tier.

    band_max_units: null is checked by tier *position* (index == last_index),
    not by "was the previous tier's max ever None". An earlier version used
    `elif prev_max is not None and lo != prev_max`, which silently skipped the
    contiguity check for the tier right after any open-ended non-final tier —
    a gap or overlap there would pass. Restricting null to the final tier
    removes the ambiguous case entirely: prev_max is only ever None while
    checking the tier that follows it, and that can now only be the tier
    after the true final one, which doesn't exist.
    """
    errors: list[str] = []
    warnings: list[str] = []
    tiers = doc.get("capital_tiers") or []
    if not tiers:
        return ["capital_tiers is empty"], warnings

    known_functions = {ft.get("function_id") for ft in (doc.get("function_types") or [])}
    gate_ids = {g.get("gate_id") for g in (doc.get("progression_gates") or [])}
    last_index = len(tiers) - 1

    prev_max = None
    for index, tier in enumerate(tiers):
        tid = tier.get("tier_id", "<unnamed>")
        lo, hi = tier.get("band_min_units"), tier.get("band_max_units")
        is_final = index == last_index

        if lo is None:
            errors.append(f"{tid}: band_min_units is required")
        elif index == 0:
            if lo != 0:
                errors.append(
                    f"{tid}: the first tier must start at band_min_units 0 — equity "
                    "below the floor would belong to no tier, contradicting "
                    "demotion's guarantee that every equity value has one"
                )
        elif lo != prev_max:
            errors.append(
                f"{tid}: band starts at {lo} but the previous tier ends at {prev_max} — "
                "a gap leaves equity in no tier, an overlap puts it in two"
            )

        if is_final:
            if hi is not None:
                errors.append(
                    f"{tid}: the final tier must have band_max_units: null — a closed "
                    "top band leaves equity above it ungoverned"
                )
        else:
            if hi is None:
                errors.append(
                    f"{tid}: band_max_units: null is only permitted on the final tier "
                    "— on a non-final tier it lets equity above it escape every real "
                    "tier below the true final one"
                )
            elif lo is not None and hi <= lo:
                errors.append(f"{tid}: band_max_units {hi} must exceed band_min_units {lo}")

        prev_max = hi

        for fn in tier.get("permitted_functions") or []:
            if fn not in known_functions:
                errors.append(f"{tid}: permitted_functions names unknown function {fn!r}")

        gate = tier.get("progression_gate")
        if is_final:
            if gate is not None and gate not in gate_ids:
                errors.append(f"{tid}: progression_gate {gate!r} is not declared")
        elif gate is None:
            errors.append(
                f"{tid}: progression_gate is required for every non-terminal tier — "
                "without one, equity can cross the boundary with no evidence or "
                "approval control"
            )
        elif gate not in gate_ids:
            errors.append(f"{tid}: progression_gate {gate!r} is not declared")

        if tier.get("leverage_permitted") and (tier.get("max_leverage") or 0) <= 1.0:
            warnings.append(f"{tid}: leverage_permitted is true but max_leverage <= 1.0")
        if not tier.get("leverage_permitted") and (tier.get("max_leverage") or 1.0) > 1.0:
            errors.append(
                f"{tid}: leverage_permitted is false but max_leverage is "
                f"{tier.get('max_leverage')} — the cap contradicts the permission"
            )

    return errors, warnings


def _check_roles_and_switches(doc: dict) -> list[str]:
    errors: list[str] = []
    role_ids = {r.get("role_id") for r in (doc.get("roles") or [])}
    if not role_ids:
        # Record and continue rather than return: an adopter that empties roles
        # entirely has also broken every kill-switch and must_not_override check
        # below, and a single run should report the whole set of defects instead
        # of hiding three of them behind the first one found.
        errors.append("roles is empty — every rule references a role slot")

    def _require_role(value, where: str) -> None:
        if value and value not in role_ids:
            errors.append(f"{where} references undeclared role {value!r}")

    # exception_authority lives under `transfers`, not directly on
    # ledger_separation. An earlier version read the wrong path, so the lookup
    # returned None, _require_role skipped on falsy, and the only role guarding
    # cross-ledger transfers was never validated at all.
    transfers = (doc.get("ledger_separation") or {}).get("transfers") or {}
    exception_authority = transfers.get("exception_authority")
    if not exception_authority:
        errors.append(
            "ledger_separation.transfers.exception_authority is missing — a transfer "
            "exception with nobody named to authorise it is either impossible or "
            "available to anyone, and the register must not leave that ambiguous"
        )
    else:
        _require_role(exception_authority, "ledger_separation.transfers.exception_authority")

    for gate in doc.get("progression_gates") or []:
        gid = gate.get("gate_id", "<unnamed>")
        req = gate.get("requires") or {}
        approval = req.get("approval")
        if not approval:
            errors.append(
                f"{gid}.requires.approval is missing — a progression gate with nobody "
                "named to approve it lets equity cross the boundary unaccountably"
            )
        else:
            _require_role(approval, f"{gid}.requires.approval")
        # live_capital_approval is intentionally null except at gate.tier0_to_tier1 —
        # unlike approval, its absence is a valid configuration, not an omission.
        _require_role(req.get("live_capital_approval"), f"{gid}.requires.live_capital_approval")
        evidence = req.get("evidence")
        if not (isinstance(evidence, str) and evidence.strip()):
            errors.append(
                f"{gid}.requires.evidence is missing or empty — a promotion gate "
                "without evidence to point to degrades into approval alone"
            )

    switches = doc.get("kill_switches") or []
    if not switches:
        errors.append(
            "kill_switches is empty — at least one emergency halt control is required; "
            "an adopter that removes them all would have no automatic stop left"
        )
    for switch in switches:
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
    for required in NON_OVERRIDABLE_CONTROLS:
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
    try:
        doc = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        print(f"ERROR: {REGISTER} is not valid YAML: {exc}", file=sys.stderr)
        return 1

    if doc is None:
        doc = {}
    elif not isinstance(doc, dict):
        print(
            f"ERROR: {REGISTER} must parse to a mapping at the top level, got "
            f"{type(doc).__name__}",
            file=sys.stderr,
        )
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    errors += _check_is_generic(raw)
    errors += _check_ledger_separation(doc)
    errors += _check_required_flags(doc)
    errors += _check_unique_ids(doc)
    tier_errors, tier_warnings = _check_tier_ladder(doc)
    errors += tier_errors
    warnings += tier_warnings
    errors += _check_roles_and_switches(doc)
    errors += _check_hard_authorities(doc)

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
