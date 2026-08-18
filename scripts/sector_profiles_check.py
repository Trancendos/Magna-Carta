#!/usr/bin/env python3
"""Sector profiles register validation — Layer B check.

Validates compliance/sector_profiles.yaml against its documented invariants:

  * every sector carries sector_id, name, description, signals, data_types,
    typical_clients, stakeholder_roles, delivery_notes
  * sector_id values are unique and slug-shaped (lowercase, underscores)
  * every signal_id referenced exists in proactive_signals.yaml — a sector
    cannot imply a signal the estate does not define
  * every referenced signal is reachable from at least one trigger in
    framework_triggers.yaml, so a sector cannot claim to activate frameworks
    that no trigger would ever apply

That last check is a drift guard rather than an active finding: as of 2026-08-17
all 22 defined signals are referenced by a trigger, so it cannot currently fire.
It exists because the failure it prevents is silent — a sector profile pointing
at an untriggered signal would promise framework coverage that activates
nothing, and nobody would notice. Kept as an ERROR so that adding a signal
without a trigger and then claiming it from a sector fails the build.

Signals defined in proactive_signals.yaml but claimed by no sector are reported
as INFO only — plenty of signals are platform-wide (SIG-CORE-001) or
certification-track (SIG-ISO-001) rather than sector-driven, so that is normal
and not a defect.

Exit 0 on success (warnings and info allowed), 1 on structural error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SECTORS = ROOT / "compliance" / "sector_profiles.yaml"
SIGNALS = ROOT / "compliance" / "proactive_signals.yaml"
TRIGGERS = ROOT / "compliance" / "framework_triggers.yaml"

REQUIRED_FIELDS = [
    "sector_id",
    "name",
    "description",
    "signals",
    "data_types",
    "typical_clients",
    "stakeholder_roles",
    "delivery_notes",
]

SLUG = re.compile(r"^[a-z][a-z0-9_]*$")

_errors: list[str] = []
_warnings: list[str] = []
_info: list[str] = []


def _err(msg: str) -> None:
    """Record a failure. Any error makes the check exit 1."""
    _errors.append(msg)


def _warn(msg: str) -> None:
    """Record a caveat worth surfacing that must not fail the build.

    Used for a sector with recorded `known_gaps`: partial coverage is a fact
    about the register, not a defect in it, and failing on it would make
    honest gap-recording more painful than leaving gaps undocumented — the
    opposite of the intended incentive.
    """
    _warnings.append(msg)


def _load(path: Path) -> dict:
    """Load one register, recording load failures via `_err` rather than raising.

    Returns `{}` on any failure so the caller can keep validating the registers
    that did load and report everything at once.
    """
    if not path.is_file():
        _err(f"missing register: {path.relative_to(ROOT)}")
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        _err(f"{path.relative_to(ROOT)}: invalid YAML — {exc}")
        return {}
    if not isinstance(data, dict):
        _err(f"{path.relative_to(ROOT)}: root must be a mapping")
        return {}
    return data


def main() -> int:
    """Validate every sector profile against the defined signal set.

    Returns 0 when the register is structurally sound, 1 on any error. A sector
    declaring `known_gaps` warns but passes — see `_warn`.
    """
    sectors_doc = _load(SECTORS)
    signals_doc = _load(SIGNALS)
    triggers_doc = _load(TRIGGERS)
    if _errors:
        _report()
        return 1

    known_signals = {
        s.get("signal_id")
        for s in (signals_doc.get("signals") or [])
        if isinstance(s, dict) and s.get("signal_id")
    }
    triggered_signals = {
        t.get("signal_id")
        for t in (triggers_doc.get("triggers") or [])
        if isinstance(t, dict) and t.get("signal_id")
    }

    sectors = sectors_doc.get("sectors")
    if not isinstance(sectors, list) or not sectors:
        _err("sector_profiles.yaml: 'sectors' must be a non-empty list")
        _report()
        return 1

    seen_ids: set[str] = set()
    claimed_signals: set[str] = set()

    for index, sector in enumerate(sectors):
        label = f"sectors[{index}]"
        if not isinstance(sector, dict):
            _err(f"{label}: each sector must be a mapping")
            continue

        sector_id = sector.get("sector_id")
        if sector_id:
            label = f"sector '{sector_id}'"

        for field in REQUIRED_FIELDS:
            value = sector.get(field)
            if value is None or (isinstance(value, (list, str)) and not value):
                _err(f"{label}: missing or empty required field '{field}'")

        if sector_id:
            if not SLUG.match(str(sector_id)):
                _err(
                    f"{label}: sector_id must be lowercase slug with underscores "
                    f"(got {sector_id!r})"
                )
            if sector_id in seen_ids:
                _err(f"duplicate sector_id: {sector_id!r}")
            seen_ids.add(sector_id)

        signals = sector.get("signals")
        if isinstance(signals, list):
            for signal_id in signals:
                if not isinstance(signal_id, str) or not signal_id.strip():
                    # `set.add()` on a mapping or list raises TypeError
                    # (unhashable), killing the check with a traceback rather
                    # than naming the sector that has the malformed entry.
                    _err(
                        f"{label}: every 'signals' entry must be a non-empty string, "
                        f"got {type(signal_id).__name__}"
                    )
                    continue
                claimed_signals.add(signal_id)
                if signal_id not in known_signals:
                    _err(
                        f"{label}: references unknown signal {signal_id!r} — "
                        f"not defined in proactive_signals.yaml"
                    )
                elif signal_id not in triggered_signals:
                    _err(
                        f"{label}: signal {signal_id!r} exists but no trigger in "
                        f"framework_triggers.yaml references it, so it activates "
                        f"no frameworks — this profile would promise coverage it "
                        f"cannot deliver"
                    )
        elif signals is not None:
            _err(f"{label}: 'signals' must be a list")

    # Informational only — most signals are platform-wide or certification-track
    # rather than sector-driven, so being unclaimed is expected.
    unclaimed = sorted(known_signals - claimed_signals)
    if unclaimed:
        _info.append(
            f"{len(unclaimed)} signal(s) claimed by no sector profile "
            f"(normal for platform-wide/certification signals): "
            f"{', '.join(unclaimed)}"
        )

    # Sectors that record a known gap are surfaced so they are not mistaken for
    # complete coverage. Read from the structured `known_gaps` list, never by
    # searching prose: an earlier version looked for the literal "GAP:" in
    # `notes`, which made a validator's behaviour depend on an author's wording
    # and would have gone quiet the moment someone wrote "Gap:" or reworded the
    # sentence — failing open on exactly the profiles most needing the warning.
    for sector in sectors:
        if not isinstance(sector, dict):
            continue
        gaps = sector.get("known_gaps")
        sid = sector.get("sector_id")
        if gaps is None:
            continue
        if not isinstance(gaps, list) or not gaps:
            _err(
                f"sector '{sid}': 'known_gaps' must be a non-empty list of strings. "
                f"Omit the key entirely for a profile with no known gaps."
            )
            continue
        for entry in gaps:
            if not isinstance(entry, str) or not entry.strip():
                _err(f"sector '{sid}': every 'known_gaps' entry must be a non-empty string")
        _warn(
            f"sector '{sid}' records {len(gaps)} known gap(s) — treat its coverage "
            f"as partial"
        )

    # Catch the reverse drift: gap prose left in `notes` where no validator and
    # no reader scanning `known_gaps` will find it.
    for sector in sectors:
        if not isinstance(sector, dict):
            continue
        if "gap" in str(sector.get("notes", "")).lower() and not sector.get("known_gaps"):
            _err(
                f"sector '{sector.get('sector_id')}': 'notes' mentions a gap but "
                f"'known_gaps' is absent. Move the gap into 'known_gaps' so it is "
                f"machine-readable."
            )

    _report()
    print(
        f"\nsector_profiles_check: {len(seen_ids)} sector(s), "
        f"{len(claimed_signals)} signal reference(s) checked against "
        f"{len(known_signals)} defined signal(s)"
    )
    return 1 if _errors else 0


def _report() -> None:
    """Print collected output in severity order: info, then warnings, then errors.

    Errors go to stderr so a CI log filtered to stderr shows only what actually
    failed the run.
    """
    for msg in _info:
        print(f"INFO:  {msg}")
    for msg in _warnings:
        print(f"WARN:  {msg}")
    for msg in _errors:
        print(f"ERROR: {msg}", file=sys.stderr)
    if not _errors:
        print("sector_profiles_check OK")


if __name__ == "__main__":
    sys.exit(main())
