#!/usr/bin/env python3
"""Prove a refactor of a validator changed nothing, by breaking its input.

A validator run against a valid estate exercises none of its error branches, so
"the script still exits 0" is nearly no evidence that a refactor preserved
behaviour -- and every script under scripts/ is a validator with no unit tests.
This runs the working tree's copy and a committed copy of the same script side
by side against deliberately broken registers, and reports any difference in
what they say.

    python3 scripts/refactor_equivalence_probe.py                 # vs HEAD
    python3 scripts/refactor_equivalence_probe.py origin/main
    python3 scripts/refactor_equivalence_probe.py HEAD capital    # one target

Written on 2026-09-14 while taking the queue of refactor pull requests. It is
also the gate on the one that was deferred: #41 restructures
_check_tier_ladder, whose branches enforce that the first capital tier starts at
zero, that the final band is open, and that tier 0 is simulated_only -- none of
which fire on a valid register. Extend CASES to cover a branch before touching
the code that carries it.
"""

from __future__ import annotations

import copy
import difflib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Iterator

import yaml

ROOT = Path(__file__).resolve().parents[1]

#: target -> (script under scripts/, [(input file, case name, mutation)])
Mutation = tuple[str, str, Callable[[Any], Any]]
CASES: dict[str, tuple[str, list[Mutation]]] = {
    "capital": (
        "capital_governance_check.py",
        [
            ("compliance/capital_governance.yaml", f"drop-{key}",
             (lambda k: lambda d: {x: y for x, y in d.items() if x != k})(key))
            for key in ("capital_tiers", "roles", "function_types", "progression_gates",
                        "kill_switches", "ledger_separation", "demotion", "binding")
        ] + [
            ("compliance/capital_governance.yaml", "band_min-as-string",
             lambda d: _tier(d, 0, band_min_units="20")),
            ("compliance/capital_governance.yaml", "first-tier-floor-not-zero",
             lambda d: _tier(d, 0, band_min_units=5)),
            ("compliance/capital_governance.yaml", "first-tier-live",
             lambda d: _tier(d, 0, external_execution="live_permitted")),
            ("compliance/capital_governance.yaml", "final-tier-closed",
             lambda d: _tier(d, -1, band_max_units=999)),
            ("compliance/capital_governance.yaml", "tier-without-id",
             lambda d: _tier(d, 0, tier_id=None)),
            ("compliance/capital_governance.yaml", "band-gap",
             lambda d: _tier(d, 1, band_min_units=99999)),
        ],
    ),
    "health": (
        "compliance_health_check.py",
        [
            ("compliance/compliance_action_tracker.yaml", "tracker-drop-actions",
             lambda d: {k: v for k, v in d.items() if k != "actions"}),
            ("compliance/compliance_action_tracker.yaml", "tracker-actions-not-a-list",
             lambda d: {**d, "actions": {"nope": 1}}),
            ("compliance/compliance_action_tracker.yaml", "tracker-entry-not-an-object",
             lambda d: {**d, "actions": ["a string", *d["actions"]]}),
            ("compliance/compliance_action_tracker.yaml", "tracker-duplicate-id",
             lambda d: {**d, "actions": [*d["actions"], copy.deepcopy(d["actions"][0])]}),
            ("compliance/risk_register.yaml", "risk-drop-everything", lambda d: {}),
            ("compliance/framework_implementation_catalog.yaml", "catalog-empty",
             lambda d: {**d, "entries": []}),
            ("compliance/framework_implementation_catalog.yaml", "catalog-unknown-signal",
             lambda d: _entry(d, signal_id="SIG-NOPE-999")),
            ("compliance/framework_implementation_catalog.yaml", "catalog-unknown-trigger",
             lambda d: _entry(d, trigger_id="TRG-NOPE-999")),
            ("compliance/framework_implementation_catalog.yaml", "catalog-orphan-entry",
             lambda d: {**d, "entries": [*d["entries"], {**d["entries"][0], "framework_id": "FW-ORPHAN"}]}),
            ("compliance/framework_implementation_catalog.yaml", "catalog-drop-first-framework",
             lambda d: {**d, "entries": d["entries"][1:]}),
            ("config/magna_carta_config.json", "runtime-config-emptied", lambda d: {}),
            ("compliance/proactive_signals.yaml", "signals-emptied",
             lambda d: {**d, "signals": []}),
            ("compliance/framework_triggers.yaml", "triggers-emptied",
             lambda d: {**d, "triggers": []}),
            ("compliance/framework_triggers.yaml", "trigger-loses-framework_ids",
             lambda d: {**d, "triggers": [
                 {k: v for k, v in d["triggers"][0].items() if k != "framework_ids"},
                 *d["triggers"][1:]]}),
        ],
    ),
}


def _tier(doc: dict, index: int, **fields: Any) -> dict:
    out = copy.deepcopy(doc)
    tier = out["capital_tiers"][index]
    for key, value in fields.items():
        if value is None:
            tier.pop(key, None)
        else:
            tier[key] = value
    return out


def _entry(doc: dict, **fields: Any) -> dict:
    out = copy.deepcopy(doc)
    out["entries"][0].update(fields)
    return out


def _run(script: Path, rel: str, text: str) -> str:
    """Run `script` with `rel` replaced by `text`, then put `rel` back.

    Both paths are checked against the tree rather than trusted. `script` comes
    from CASES and from `git show`, and `rel` from CASES, so neither is user
    input today -- but "today" is the whole weakness of that argument, and this
    function both executes one path and overwrites another. Asserting the
    invariant costs two lines and makes it true rather than intended.
    """
    resolved = script.resolve()
    if resolved.parent != (ROOT / "scripts").resolve() or resolved.suffix != ".py":
        raise SystemExit(f"refusing to execute {script}: not a script in scripts/")
    path = (ROOT / rel).resolve()
    if not path.is_relative_to(ROOT.resolve()) or not path.is_file():
        raise SystemExit(f"refusing to overwrite {rel}: not a file in this repository")
    original = path.read_text(encoding="utf-8")
    try:
        path.write_text(text, encoding="utf-8")
        # No shell, argv as a list, and both elements constrained above:
        # sys.executable is this interpreter and `resolved` is a .py file in
        # scripts/. Running a script is the entire purpose of this tool.
        result = subprocess.run(  # nosemgrep: python.lang.security.audit.dangerous-subprocess-use-audit
            [sys.executable, str(resolved)], cwd=ROOT,
            capture_output=True, text=True, timeout=300,
        )
        return f"exit={result.returncode}\n{result.stdout}{result.stderr}"
    finally:
        path.write_text(original, encoding="utf-8")


def _serialise(rel: str, data: Any) -> str:
    if rel.endswith(".json"):
        return json.dumps(data, indent=2)
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)


def _deserialise(rel: str, text: str) -> Any:
    return json.loads(text) if rel.endswith(".json") else yaml.safe_load(text)


def _probe(name: str, script_name: str, mutations: list[Mutation], ref: str) -> Iterator[bool]:
    committed = subprocess.run(
        ["git", "show", f"{ref}:scripts/{script_name}"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if committed.returncode != 0:
        print(f"  cannot read scripts/{script_name} at {ref}")
        yield False
        return
    # Run the committed copy from scripts/ so its ROOT (parents[1]) still
    # resolves to this repository rather than a temp directory.
    # A fixed name here (`_probe_<script>`) is one path two runs share: a second
    # probe, or a stale copy left by a killed one, silently becomes the baseline
    # the working tree is compared against -- and a repository file that happened
    # to carry the name would be overwritten and then deleted. mkstemp gives a
    # name nothing else holds, and refuses rather than clobbering. Caught by
    # CodeRabbit.
    handle, old_path = tempfile.mkstemp(
        prefix=f"_probe_{script_name[:-3]}_", suffix=".py", dir=ROOT / "scripts"
    )
    os.close(handle)
    old = Path(old_path)
    old.write_text(committed.stdout, encoding="utf-8")
    new = ROOT / "scripts" / script_name
    try:
        for rel, case, mutate in mutations:
            try:
                text = _serialise(rel, mutate(_deserialise(rel, (ROOT / rel).read_text("utf-8"))))
            except Exception as exc:  # a mutation that no longer fits its input
                print(f"  SKIP  {case}: {exc}")
                yield False
                continue
            before, after = _run(old, rel, text), _run(new, rel, text)
            if before == after:
                lines = len(before.splitlines()) - 1
                print(f"  same  {case:38s} ({before.splitlines()[0]}, {lines} lines)")
                yield True
            else:
                print(f"  DIFF  {case}")
                for line in list(difflib.unified_diff(
                        before.splitlines(), after.splitlines(),
                        f"{ref}", "working tree", lineterm=""))[:30]:
                    print(f"        {line}")
                yield False
    finally:
        old.unlink(missing_ok=True)


def main() -> int:
    ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    wanted = sys.argv[2:] or list(CASES)
    unknown = set(wanted) - set(CASES)
    if unknown:
        print(f"unknown target(s): {sorted(unknown)}; known: {sorted(CASES)}")
        return 2
    results: list[bool] = []
    for name in wanted:
        script_name, mutations = CASES[name]
        print(f"=== {name}: scripts/{script_name} vs {ref} ===")
        results.extend(_probe(name, script_name, mutations, ref))
    passed = sum(results)
    print(f"\n{passed} identical, {len(results) - passed} different or skipped")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
