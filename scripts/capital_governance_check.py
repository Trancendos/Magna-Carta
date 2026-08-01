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

import math
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

# CAPITAL-GOVERNANCE.md §2 names the same four controls in prose. That prose
# and this constant are two independent copies of one fact, and only this
# constant is checked against the register (must_not_override, above) — the
# doc could drift from both without CI noticing. _check_docs_name_non_overridable_controls
# closes that gap by checking the doc text too, so all three copies stay
# machine-verified against each other rather than trusting the doc by hand.
CAPITAL_GOVERNANCE_DOC = ROOT / "docs" / "governance" / "CAPITAL-GOVERNANCE.md"

# The doc's prose doesn't always spell a control's identifier verbatim — it
# says "the kill switches", not "kill_switches" — so a literal substring
# search needs a stand-in phrase for any control whose readable-prose form
# differs from its identifier.
DOC_PROSE_FOR_CONTROL = {"kill_switches": "kill switches"}

# The fixed pair of function types ledger_separation depends on. Not just
# "function_types must be non-empty" (the existing check): an adopter could
# satisfy that with only INTERNAL, silently dropping external capital
# handling — the higher-risk half of what this register governs — from the
# model entirely, with the ledger-separation check having nothing to compare
# it against.
REQUIRED_FUNCTION_IDS = ("INTERNAL", "EXTERNAL")

# The fixed four-role contract every rule below assumes exists, even for the
# one role (risk_authority) no rule references *by name* yet — its pre-action
# check is Stage 7.3 runtime enforcement, staged ahead of the rules that will
# use it. Because nothing currently names it, an adopter could delete it from
# roles and every existing _require_role check would still pass.
REQUIRED_ROLE_IDS = ("capital_operator", "risk_authority", "presiding_authority", "human_owner")

# The only two values capital_tiers.external_execution may hold. Checked as
# an enum, not just "is it simulated_only", because _check_hard_authorities
# identifies which gates need the strict human_owner requirement by matching
# this field against the literal string "simulated_only" — a typo or renamed
# value would silently fail that match and downgrade a tier's progression
# gate to the weaker "if set" check instead of failing loud.
VALID_EXTERNAL_EXECUTION = ("simulated_only", "live_permitted")

# The four hard-kill switches CAPITAL-GOVERNANCE.md and this register's own
# comments treat as structural, not optional: ledger_boundary_violation and
# insolvency_breach are named directly in the doc's prose (§4, §5, §6) as
# load-bearing halts; daily_loss_breach and limit_override_attempt share the
# same scope: ALL / auto_release: never hard-kill profile _check_hard_authorities
# already enforces human_owner release on. "kill_switches is non-empty" (the
# existing check) is satisfied by any single switch, including a soft,
# narrow-scope one — an adopter could drop all four of these and keep, say,
# only a low-impact switch, and still pass.
REQUIRED_KILL_SWITCH_IDS = (
    "daily_loss_breach",
    "ledger_boundary_violation",
    "limit_override_attempt",
    "insolvency_breach",
)

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
    # Bare, not "The Observatory": an earlier version only matched the
    # two-word phrase, so a lowercase field like `observatory_event_prefix`
    # slipped straight past it — the estate's Observatory concept leaking
    # into the generic register through the very field that was supposed to
    # be a portable audit-event namespace. Bare "Observatory" catches that
    # and the two-word phrase both.
    "Observatory",
]

# Whole-word matching, not substring containment. "Porter" as a bare substring
# also fires inside "reporter", "supporter" and "transporter", which would fail
# the build on ordinary prose and make the register hostile to edit — and a check
# people learn to work around is worse than no check.
#
# Not \b: regex word boundaries treat underscore as a word character, so
# \bObservatory\b does not match "observatory_event_prefix" — there is no
# boundary between "y" and "_". That gap is exactly how this register's own
# observatory_event_prefix field slipped past this check once (before it was
# renamed). The lookaround below excludes only letters and digits, so
# underscores, dots, and other punctuation all count as boundaries while
# "reporter"/"supporter" still don't false-positive on "Porter".
_TERM_PATTERNS = [
    (term, re.compile(rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])", re.IGNORECASE))
    for term in PLATFORM_SPECIFIC_TERMS
]


def _is_finite_number(value: object) -> bool:
    """True for an int/float that isn't a bool and isn't inf/nan — the
    reusable form of the isinstance+isfinite guard used throughout this file
    (bool is excluded because it's a Python int subtype, so True would
    otherwise silently pass any numeric check as 1)."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


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


# Every list-valued top-level section the checks below iterate over is
# assumed to contain mappings (function_types entries, capital_tiers
# entries, and so on) — every `.get()` call on an entry depends on it. An
# adopter who writes `function_types: [alpha]` (a string, not a mapping)
# would otherwise hit an uncaught AttributeError deep inside whichever
# check ran first, printing a Python traceback instead of a normal
# validator error line. main() runs _sanitize_list_sections before any
# other check, so every check function below can assume this shape holds.
LIST_SECTIONS = ("roles", "function_types", "capital_tiers", "progression_gates", "kill_switches")


def _sanitize_list_sections(doc: dict) -> list[str]:
    """Replace each list section with only its mapping entries, recording an
    error for anything else, so downstream checks never see a non-mapping
    entry to call .get() on.
    """
    errors: list[str] = []
    for key in LIST_SECTIONS:
        raw_value = doc.get(key)
        if raw_value is None:
            continue
        if not isinstance(raw_value, list):
            errors.append(f"{key} must be a list, got {type(raw_value).__name__}")
            doc[key] = []
            continue
        clean: list[dict] = []
        for index, item in enumerate(raw_value):
            if isinstance(item, dict):
                clean.append(item)
            else:
                errors.append(f"{key}[{index}] must be a mapping, got {type(item).__name__}")
        doc[key] = clean
    return errors


# Every top-level section below that checks read as a mapping via `doc.get(key)
# or {}` — ledger_separation, demotion, evidence, binding — has the same
# uncaught-AttributeError exposure as the list sections above if an adopter
# writes e.g. `demotion: disabled` (a string, not a mapping): `or {}` only
# rescues an absent/falsy value, not a truthy non-mapping one, so the first
# `.get()` against it crashes instead of reporting a structural error. Two
# sections nest one level deeper (ledger_separation.transfers,
# evidence.decision_journal) and share the same exposure at that nested key.
DICT_SECTIONS = ("ledger_separation", "demotion", "evidence", "binding")
NESTED_DICT_SECTIONS = (("ledger_separation", "transfers"), ("evidence", "decision_journal"))


def _sanitize_dict_sections(doc: dict) -> list[str]:
    """Replace each non-mapping dict-section value with {}, recording an
    error, so downstream checks never call .get() on something that isn't a
    mapping — the dict-section counterpart to _sanitize_list_sections above.
    """
    errors: list[str] = []
    for key in DICT_SECTIONS:
        value = doc.get(key)
        if value is not None and not isinstance(value, dict):
            errors.append(f"{key} must be a mapping, got {type(value).__name__}")
            doc[key] = {}
    for parent, child in NESTED_DICT_SECTIONS:
        parent_value = doc.get(parent) or {}
        child_value = parent_value.get(child)
        if child_value is not None and not isinstance(child_value, dict):
            errors.append(
                f"{parent}.{child} must be a mapping, got {type(child_value).__name__}"
            )
            parent_value[child] = {}
    # progression_gates[*].requires is a per-entry nested mapping, not a fixed
    # top-level path — NESTED_DICT_SECTIONS can't express "this key, inside
    # every item of a list", so it's sanitized here instead. Both
    # _check_hard_authorities and _check_roles_and_switches read it via
    # `gate.get("requires") or {}`, which only rescues an absent/falsy value;
    # a truthy non-mapping (e.g. `requires: "human_owner"`) would still crash
    # their first .get() call.
    for gate in doc.get("progression_gates") or []:
        requires = gate.get("requires")
        if requires is not None and not isinstance(requires, dict):
            gid = gate.get("gate_id", "<unnamed>")
            errors.append(f"progression_gates: gate {gid!r}.requires must be a mapping, got {type(requires).__name__}")
            gate["requires"] = {}
    return errors


def _check_ledger_separation(doc: dict) -> list[str]:
    errors: list[str] = []
    fts = doc.get("function_types") or []
    if not fts:
        return ["function_types is empty — nothing is governed"]

    declared_function_ids = {ft.get("function_id") for ft in fts}
    for required in REQUIRED_FUNCTION_IDS:
        if required not in declared_function_ids:
            errors.append(
                f"function_types is missing required function_id {required!r} — "
                "ledger_separation exists to keep INTERNAL and EXTERNAL apart; "
                "dropping either one lets the missing half of what this register "
                "governs disappear from the model with nothing left to separate it from"
            )

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
    names that ID actually means. A missing ID is the same defect by another
    route: skipping it (as an earlier version did) lets any number of
    unidentified entries accumulate silently instead of being flagged, so a
    missing id is now an error in its own right, not just excluded from the
    duplicate check.
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
            if not value:
                errors.append(f"{list_key}: entry missing required {id_key}")
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

    # A tier whose external_execution is simulated_only is the one this register's
    # own docs call "the one progression the presiding authority cannot grant
    # alone" — the gate that lifts a tier out of simulation into live money is a
    # structural fact about that tier, not a name any adopter should have to know.
    # Identifying it by that property (rather than hardcoding "gate.tier0_to_tier1")
    # means the rule still holds if the register's tier ids ever change.
    simulated_only_gate_ids = {
        tier.get("progression_gate")
        for tier in (doc.get("capital_tiers") or [])
        if tier.get("external_execution") == "simulated_only" and tier.get("progression_gate")
    }

    for gate in doc.get("progression_gates") or []:
        gid = gate.get("gate_id", "<unnamed>")
        req = gate.get("requires") or {}
        if req.get("approval") == "capital_operator":
            errors.append(
                f"{gid}.requires.approval is capital_operator — an operator "
                "cannot approve its own promotion"
            )
        live = req.get("live_capital_approval")
        if gid in simulated_only_gate_ids:
            # Checking only "if set, must be human_owner" (as an earlier version
            # did) lets an adopter delete the field from exactly this gate and
            # pass — the one place the human checkpoint is not optional.
            if live != "human_owner":
                errors.append(
                    f"{gid}.requires.live_capital_approval must be human_owner "
                    "— this gate lifts a tier out of simulated_only execution "
                    "into live money, the one progression that cannot be "
                    "delegated to presiding_authority alone"
                )
        elif live is not None and live != "human_owner":
            errors.append(
                f"{gid}.requires.live_capital_approval must be human_owner "
                "when set — it exists to require a checkpoint above "
                "presiding_authority, not a delegatable role"
            )

    for switch in doc.get("kill_switches") or []:
        sid = switch.get("switch_id", "<unnamed>")
        release_authority = switch.get("release_authority")
        if release_authority == "capital_operator":
            errors.append(
                f"kill switch {sid}.release_authority is capital_operator — "
                "the actor a switch exists to stop cannot also be the one "
                "who releases it"
            )
        # Any switch that halts everything (scope: ALL) and never auto-releases
        # is, by that combination, a hard kill — the operator has no bounded
        # blast radius and no clock to wait out. That structural profile is the
        # test, not a name: hardcoding specific switch_ids here (as an earlier
        # version did with only "ledger_boundary_violation") silently exempted
        # every other switch sharing the same profile, including one added
        # later (insolvency_breach) and one that was already here
        # (limit_override_attempt) but had been assigned presiding_authority
        # without anything here checking it belonged in this class.
        elif (
            switch.get("scope") == "ALL"
            and switch.get("auto_release") == "never"
            and release_authority != "human_owner"
        ):
            errors.append(
                f"kill switch {sid}.release_authority must be human_owner, got "
                f"{release_authority!r} — a switch that halts everything and "
                "never auto-releases is a hard kill by definition, and a hard "
                "kill is not a call any automated role gets to make"
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
        lo_raw, hi_raw = tier.get("band_min_units"), tier.get("band_max_units")
        # A non-numeric band bound (e.g. the YAML string "20") would otherwise
        # reach `hi <= lo` below and crash with an uncaught TypeError instead
        # of a structural error. Sanitize first, same as every other numeric
        # field in this file: treat an invalid value as absent for the rest
        # of this tier's checks, which still reports it (via the existing
        # "is required" branches) rather than silently accepting it.
        lo = lo_raw if (lo_raw is None or _is_finite_number(lo_raw)) else None
        hi = hi_raw if (hi_raw is None or _is_finite_number(hi_raw)) else None
        if lo_raw is not None and lo is None:
            errors.append(f"{tid}: band_min_units must be a finite number, got {lo_raw!r}")
        if hi_raw is not None and hi is None:
            errors.append(f"{tid}: band_max_units must be a finite number, got {hi_raw!r}")
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

        external_execution = tier.get("external_execution")
        if external_execution not in VALID_EXTERNAL_EXECUTION:
            errors.append(
                f"{tid}: external_execution must be one of {VALID_EXTERNAL_EXECUTION!r}, "
                f"got {external_execution!r} — _check_hard_authorities matches this field "
                "literally against 'simulated_only' to require human_owner on the tier's "
                "progression gate; an unrecognized value would silently miss that match "
                "instead of failing loud"
            )
        elif index == 0 and external_execution != "simulated_only":
            # The whole ladder could otherwise start with live_permitted:
            # _check_hard_authorities only requires human_owner on gates
            # attached to a simulated_only tier, so if no tier is
            # simulated_only, no gate is ever required to have it — the
            # entire simulation-to-live human checkpoint silently disappears,
            # not just weakens.
            errors.append(
                f"{tid}: the first tier (index 0) must have external_execution: "
                "simulated_only — this is the register's only structural "
                "guarantee that a fresh actor starts in simulation rather than "
                "live capital"
            )

        for field in ("max_risk_per_action_fraction", "max_daily_loss_fraction"):
            value = tier.get(field)
            if value is None:
                errors.append(
                    f"{tid}: {field} is required — CAPITAL-GOVERNANCE.md §5 binds Stage "
                    "7.3 runtime risk enforcement to this value; a tier that loses it "
                    "would be unconstrained with no CI signal"
                )
            elif not _is_finite_number(value):
                errors.append(f"{tid}: {field} must be a finite number, got {value!r}")
            elif not (0 <= value <= 1):
                # A fraction of equity above 1.0 (100%) authorizes risking or
                # losing more than the tier's entire equity in one action or
                # one day — the numeric cap this field exists to be would
                # itself be non-limiting.
                errors.append(
                    f"{tid}: {field} must be between 0 and 1 (a fraction of equity), "
                    f"got {value!r}"
                )

        positions = tier.get("max_concurrent_positions")
        if positions is None:
            errors.append(
                f"{tid}: max_concurrent_positions is required — CAPITAL-GOVERNANCE.md §5 "
                "binds Stage 7.3 runtime risk enforcement to this value"
            )
        elif not isinstance(positions, int) or isinstance(positions, bool) or positions < 1:
            errors.append(
                f"{tid}: max_concurrent_positions must be a positive integer, got {positions!r}"
            )

        permitted_functions = tier.get("permitted_functions") or []
        if not permitted_functions:
            # Every tier needs a function policy, not just non-terminal ones —
            # there is no "no functions permitted" tier in this design, and an
            # empty list leaves the tier's policy undefined rather than
            # deliberately empty.
            errors.append(
                f"{tid}: permitted_functions is empty — every tier must declare "
                "which function types it governs"
            )
        for fn in permitted_functions:
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

        leverage_permitted = tier.get("leverage_permitted")
        max_leverage = tier.get("max_leverage")
        # isinstance(x, bool), not truthiness: a quoted "false" is a non-empty
        # string — truthy in Python — and `if tier.get("leverage_permitted")`
        # would have treated it as leverage being permitted. bool is also
        # excluded from the numeric check below for the same class of reason:
        # True/False are ints in Python, so max_leverage: true would otherwise
        # silently pass as the number 1.
        if not isinstance(leverage_permitted, bool):
            errors.append(
                f"{tid}: leverage_permitted must be a boolean, got {leverage_permitted!r}"
            )
        else:
            max_leverage_is_finite_number = max_leverage is not None and _is_finite_number(max_leverage)
            if leverage_permitted:
                if max_leverage is None:
                    errors.append(
                        f"{tid}: leverage_permitted is true but max_leverage is not set "
                        "— a permission with no declared cap is unbounded, which is not "
                        "what 'permitted' means anywhere else in this register"
                    )
                elif not max_leverage_is_finite_number:
                    # Catches non-numeric types (a string) and non-finite floats
                    # (.inf, .nan — both valid YAML) alike: either would either
                    # crash the <= comparison below or, for inf, silently pass
                    # it (inf <= 1.0 is False, so a cap that cannot constrain
                    # anything would otherwise read as a valid, generous one).
                    errors.append(
                        f"{tid}: max_leverage must be a finite number, got "
                        f"{max_leverage!r}"
                    )
                elif max_leverage <= 1.0:
                    warnings.append(f"{tid}: leverage_permitted is true but max_leverage <= 1.0")
            elif max_leverage is not None:
                if not max_leverage_is_finite_number:
                    errors.append(
                        f"{tid}: max_leverage must be a finite number, got "
                        f"{max_leverage!r}"
                    )
                elif max_leverage > 1.0:
                    errors.append(
                        f"{tid}: leverage_permitted is false but max_leverage is "
                        f"{max_leverage} — the cap contradicts the permission"
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

    for required_role in REQUIRED_ROLE_IDS:
        if required_role not in role_ids:
            errors.append(
                f"roles is missing required role_id {required_role!r} — the register "
                "assumes this fixed four-role contract even for a role like "
                "risk_authority that no rule references by name yet (its check is "
                "Stage 7.3 runtime enforcement), so dropping it would pass every "
                "existing reference check while quietly narrowing the contract"
            )

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
        # These three numeric fields are what makes promotion earned rather
        # than approval-only — approval and evidence being present says
        # nothing if the bar they're approving against can be set to zero,
        # negative, or an arbitrarily generous breach allowance. isinstance
        # bool-exclusion for the same reason as elsewhere in this file: True
        # is an int in Python, so e.g. max_limit_breaches: true would
        # otherwise silently pass as the integer 1.
        for field in ("min_recorded_actions", "min_observation_days"):
            value = req.get(field)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                errors.append(
                    f"{gid}.requires.{field} must be a non-negative integer, got {value!r}"
                )
        max_breaches = req.get("max_limit_breaches")
        if not isinstance(max_breaches, int) or isinstance(max_breaches, bool) or max_breaches < 0:
            errors.append(
                f"{gid}.requires.max_limit_breaches must be a non-negative integer, got "
                f"{max_breaches!r}"
            )

    switches = doc.get("kill_switches") or []
    if not switches:
        errors.append(
            "kill_switches is empty — at least one emergency halt control is required; "
            "an adopter that removes them all would have no automatic stop left"
        )
    declared_switch_ids = {s.get("switch_id") for s in switches}
    for required_switch in REQUIRED_KILL_SWITCH_IDS:
        if required_switch not in declared_switch_ids:
            errors.append(
                f"kill_switches is missing required switch_id {required_switch!r} — "
                "'kill_switches is non-empty' (above) is satisfied by any single "
                "switch, including a narrow, low-impact one; an adopter could drop "
                "this hard-kill control specifically and still pass"
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
        # A time-based auto_release (anything but "never") is a clock, not a
        # fix — the condition that tripped the switch can still be true when
        # the clock runs out. Any switch that releases on a timer must name
        # what else has to hold before that release is real, or the timer
        # alone lets the halted action resume while still in breach.
        auto_release = switch.get("auto_release")
        if auto_release and auto_release != "never":
            condition = switch.get("auto_release_requires")
            if not (isinstance(condition, str) and condition.strip()):
                errors.append(
                    f"kill switch {sid} auto_release is {auto_release!r} but declares "
                    "no auto_release_requires — a time-based release with no named "
                    "condition can clear while the trigger is still true"
                )

    protected = set((doc.get("binding") or {}).get("must_not_override") or [])
    for required in NON_OVERRIDABLE_CONTROLS:
        if required not in protected:
            errors.append(
                f"binding.must_not_override omits {required!r} — an adopter could then "
                "relax the control locally, which defeats it"
            )
    return errors


def _check_docs_name_non_overridable_controls() -> list[str]:
    """CAPITAL-GOVERNANCE.md must mention every control in
    NON_OVERRIDABLE_CONTROLS, so an edit to the constant, the register's
    must_not_override list, or the doc's prose can't drift from the other
    two silently — see the constant's own comment above.
    """
    try:
        doc_text = CAPITAL_GOVERNANCE_DOC.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"cannot read {CAPITAL_GOVERNANCE_DOC} to verify it names every "
                f"non-overridable control: {exc}"]
    errors: list[str] = []
    for control in NON_OVERRIDABLE_CONTROLS:
        needle = DOC_PROSE_FOR_CONTROL.get(control, control)
        # \s+ between words, not a literal substring search: Markdown prose
        # wraps at arbitrary column widths, so "kill switches" can legitimately
        # appear in the source as "kill\nswitches" without the doc having
        # drifted from the constant at all.
        pattern = re.compile(r"\s+".join(re.escape(word) for word in needle.split()))
        if not pattern.search(doc_text):
            errors.append(
                f"{CAPITAL_GOVERNANCE_DOC.name} does not mention {control!r} (looked for "
                f"{needle!r}) — it and NON_OVERRIDABLE_CONTROLS have drifted apart"
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
    # Runs before every other check: sanitizes doc's list sections in place so
    # nothing downstream can crash on a non-mapping entry instead of reporting
    # a normal validator error.
    errors += _sanitize_list_sections(doc)
    # Same reasoning, for the top-level (and two nested) sections every check
    # below reads as a mapping rather than a list.
    errors += _sanitize_dict_sections(doc)
    errors += _check_ledger_separation(doc)
    errors += _check_required_flags(doc)
    errors += _check_unique_ids(doc)
    tier_errors, tier_warnings = _check_tier_ladder(doc)
    errors += tier_errors
    warnings += tier_warnings
    errors += _check_roles_and_switches(doc)
    errors += _check_hard_authorities(doc)
    errors += _check_docs_name_non_overridable_controls()

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
