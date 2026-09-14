"""The two guards added after the 2026-09-06 legislation lapse.

On 2026-09-06 ten of eleven entries in the legislation register fell due on the
same day. MON-011 turned every pull request in the repository red for eight days,
and the 30-PR queue sat behind it. The cause was not ten oversights: the register
was generated on 2026-06-08 and every item stamped with one review date 90 days
out, so they came due together and failed together.

Two defects made that possible, and each is pinned here:

  * the check had no warning band -- `max_overdue_days: 0` with nothing before
    it, so it was silent until the day it hard-failed;
  * nothing stopped dates re-clustering, and the shape had ALREADY been
    recreated: all five `standards_watch` entries shared 2026-12-08, a second
    cliff primed to fire in December.

These are also the repository's first tests, which is not incidental. PR #50 added
a unit-test step to `run_layer_b_local_ci.sh` that stays a visible SKIP until a
`tests/` directory appears and then activates itself, with pytest already in
`requirements.txt` so CI can run it. This file is what turns that step on.
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location(
    "compliance_health_check", ROOT / "scripts" / "compliance_health_check.py"
)
assert _SPEC and _SPEC.loader
chc = importlib.util.module_from_spec(_SPEC)
# Registered before exec: the script defines a @dataclass, and dataclasses
# resolves annotations via sys.modules[cls.__module__], which is None for a
# module loaded by spec alone.
sys.modules[_SPEC.name] = chc
_SPEC.loader.exec_module(chc)

BLOCK = {
    "check_id": "MON-TEST",
    "register": "compliance/legislation_register.yaml",
    "items_key": "active_legislation",
    "review_field": "review_date",
    "max_overdue_days": 0,
    "warn_within_days": 30,
    "max_shared_review_date": 2,
    "exclude_status": ["N/A"],
}


def _items(*dates: str) -> dict:
    return {
        "active_legislation": [
            {"legislation_id": f"LEG-{i:03d}", "review_date": d, "status": "Programme"}
            for i, d in enumerate(dates, 1)
        ]
    }


def _run(data: dict, block: dict | None = None) -> list:
    findings: list = []
    cfg = dict(BLOCK, **(block or {}))
    chc.check_register_review_dates(cfg, findings, default_cid="MON-TEST")
    return findings


@pytest.fixture(autouse=True)
def _no_disk(monkeypatch):
    """Drive the check from synthetic data, not the live register."""
    monkeypatch.setattr(chc, "_load_yaml", lambda rel: _no_disk.data)


class TestTheWarningHorizon:
    """It must speak while there is still time to act."""

    def test_a_review_inside_the_horizon_warns(self):
        _no_disk.data = _items(str(date.today() + timedelta(days=10)))
        findings = _run(_no_disk.data)
        assert [f.severity for f in findings] == ["warning"]
        assert "due in 10d" in findings[0].message

    def test_a_review_beyond_the_horizon_is_silent(self):
        _no_disk.data = _items(str(date.today() + timedelta(days=90)))
        assert _run(_no_disk.data) == []

    def test_an_overdue_review_still_errors(self):
        """The horizon adds a warning band; it must not soften the failure."""
        _no_disk.data = _items(str(date.today() - timedelta(days=3)))
        findings = _run(_no_disk.data)
        assert [f.severity for f in findings] == ["error"]
        assert "overdue by 3d" in findings[0].message

    def test_the_horizon_can_be_switched_off(self):
        """warn_within_days: 0 restores the old silent-then-fail behaviour."""
        _no_disk.data = _items(str(date.today() + timedelta(days=10)))
        assert _run(_no_disk.data, {"warn_within_days": 0}) == []

    def test_the_boundary_day_warns(self):
        _no_disk.data = _items(str(date.today() + timedelta(days=30)))
        assert [f.severity for f in _run(_no_disk.data)] == ["warning"]


class TestTheAntiCliffRule:
    """Staggering fixes one outage; only this stops the next one."""

    def test_clustered_dates_error(self):
        same = str(date.today() + timedelta(days=200))
        _no_disk.data = _items(same, same, same)
        errors = [f for f in _run(_no_disk.data) if f.severity == "error"]
        assert errors, "three items sharing one date were not reported"
        assert "3 items share" in errors[0].message
        assert "limit is 2" in errors[0].message

    def test_staggered_dates_pass(self):
        base = date.today() + timedelta(days=200)
        _no_disk.data = _items(*(str(base + timedelta(days=7 * i)) for i in range(5)))
        assert _run(_no_disk.data) == []

    def test_the_limit_is_inclusive(self):
        """max_shared_review_date: 2 permits two, not three."""
        same = str(date.today() + timedelta(days=200))
        _no_disk.data = _items(same, same)
        assert [f for f in _run(_no_disk.data) if f.severity == "error"] == []

    def test_it_can_be_switched_off(self):
        same = str(date.today() + timedelta(days=200))
        _no_disk.data = _items(same, same, same, same)
        cfg = {"max_shared_review_date": 0}
        assert [f for f in _run(_no_disk.data, cfg) if f.severity == "error"] == []

    def test_excluded_items_do_not_count_toward_the_cluster(self):
        same = str(date.today() + timedelta(days=200))
        _no_disk.data = _items(same, same, same)
        _no_disk.data["active_legislation"][2]["status"] = "N/A"
        assert [f for f in _run(_no_disk.data) if f.severity == "error"] == []


class TestTheGuardsCannotPassVacuously:
    """A rule whose subject never occurs reports what a clean estate reports."""

    def test_the_real_registers_are_actually_covered(self):
        """Both registers must declare both rules, or the guards guard nothing."""
        import yaml

        cfg = yaml.safe_load(
            (ROOT / "compliance" / "maintenance_monitor.yaml").read_text(encoding="utf-8")
        )
        for name in ("legislation_watch", "standards_watch"):
            block = cfg.get(name) or {}
            assert block.get("warn_within_days"), f"{name} has no warning horizon"
            assert block.get("max_shared_review_date"), f"{name} has no anti-cliff limit"

    def test_no_live_register_is_clustered(self):
        """The condition that caused the outage must be absent from the tree."""
        import collections

        import yaml

        for rel, key in (
            ("compliance/legislation_register.yaml", "active_legislation"),
            ("compliance/standards_watch.yaml", "active_standards"),
        ):
            data = yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))
            items = data.get(key) or next(
                (v for v in data.values() if isinstance(v, list)), []
            )
            assert items, f"{rel}: {key} is empty — nothing was checked"
            counts = collections.Counter(str(i.get("review_date")) for i in items)
            worst, n = counts.most_common(1)[0]
            assert n <= 2, f"{rel}: {n} items share review_date {worst}"

    def test_every_item_declares_a_cadence(self):
        """Without it the next date is hand-stamped, which is how this started."""
        import yaml

        data = yaml.safe_load(
            (ROOT / "compliance" / "legislation_register.yaml").read_text(encoding="utf-8")
        )
        missing = [
            i.get("legislation_id")
            for i in data["active_legislation"]
            if not i.get("review_cycle")
        ]
        assert not missing, f"no review_cycle on: {missing}"
