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
            max_leverage_is_finite_number = (
                isinstance(max_leverage, (int, float))
                and not isinstance(max_leverage, bool)
                and math.isfinite(max_leverage)
            )
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
