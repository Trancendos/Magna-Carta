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
    _errors.append(msg)


def _warn(msg: str) -> None:
    _warnings.append(msg)


def _load(path: Path) -> dict:
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
    # complete coverage.
    for sector in sectors:
        if isinstance(sector, dict) and "GAP:" in str(sector.get("notes", "")):
            _warn(
                f"sector '{sector.get('sector_id')}' records a known gap in its "
                f"notes — treat its coverage as partial"
            )

    _report()
    print(
        f"\nsector_profiles_check: {len(seen_ids)} sector(s), "
        f"{len(claimed_signals)} signal reference(s) checked against "
        f"{len(known_signals)} defined signal(s)"
    )
    return 1 if _errors else 0


def _report() -> None:
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
