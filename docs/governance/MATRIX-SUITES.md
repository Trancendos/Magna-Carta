# Matrix Suites — bundling the estate's matrices into governed frameworks

**Version:** 1.0.0
**Date:** 2026-07-31
**Owner:** Platform Owner Trancendos / ISMS Lead
**Machine-readable:** [compliance/matrix_suites.yaml](../../compliance/matrix_suites.yaml)
**Validated by:** `scripts/matrix_suites_check.py` (runs in Layer B CI)
**Status:** Proposal implemented at registry level; runtime integrations are staged (§7)

---

## 1. Why Suites

The estate now carries **31 governance/compliance matrices** — 13 in this repository
(`docs/compliance/`, `docs/governance/`) and 18 in Tranc3 (`docs/governance/`). Each is
individually owned and versioned, but there is no layer between "one matrix" and "the
whole estate": no shared review cadence, no single place a steward sees everything they
are responsible for, and no way for the Observatory to aggregate governance health above
file level.

A **Suite** bundles related matrices into one managed framework:

```
Pillar (governs)  →  Suite (bundles)  →  Matrices (record)  →  Rows (evidence)
```

Eight suites cover all 31 matrices, each matrix assigned to **exactly one** suite (the
validator enforces this — no orphans, no double-parents):

| Suite | Pillar (governor) | Steward AI (Tier 3) | Location | Presiding Prime | Matrices |
|---|---|---|---|---|---|
| SUITE-FIN Financial | Commercial / Financial | Dorris Fontaine | Royal Bank of Arcadia | Dorris Fontaine | 4 |
| SUITE-LEG Legal & Regulatory | Architectural | Tristuran | The Town Hall | Cornelius MacIntyre | 5 |
| SUITE-SEC Security | Security | Renik | Cryptex | The Guardian (Marcus Magnolia) | 6 |
| SUITE-KNO Knowledge | Knowledge | Zimik | The Library | Norman Hawkins | 2 |
| SUITE-ENG Engineering | Development (Code) | The Dr. (Nikolai O'denhime) | The Lab | The Dr. | 5 |
| SUITE-AIG AI Governance | Architectural | Samantha Turing | Turing's Hub | Trancendos | 4 |
| SUITE-OPS Operations | DevOps | Trancendos | The Citadel | Cornelius MacIntyre | 4 |
| SUITE-EXP Experience | Creativity | Baron Von Hilton | Fabulousa | Voxx | 1 |

This satisfies the governance shape requested: **bundles are governed by their pillars**
(the Pillar enum in Tranc3 `src/entities/platform.py` is the authority), while **each
individual matrix is managed by the relevant AI within its specific Location**.

## 2. New fields introduced by the Suite layer

Per **suite** (in `matrix_suites.yaml`):

| Field | Purpose |
|---|---|
| `suite_id` | Immutable reference (`SUITE-XXX`), same convention as TRC/MC IDs |
| `pillar` | Governing pillar — must match a `Pillar` enum value exactly |
| `steward_ai` / `steward_location` | The Tier-3 Lead AI responsible day-to-day, and where they sit |
| `presiding_prime` | Tier-2 escalation authority above the steward |
| `escalation` | Ordered chain, always ending at the human owner — mirrors the model-advancement pipeline (Prime → Cornelius → Human) |
| `review_cadence` / `next_review` | Proactive-management heartbeat; staleness is a CI warning |
| `observatory_events` | Event-name prefix this suite emits under (`governance.suite.<name>.*`) |
| `kpi` | What "healthy" means for the suite, in one measurable sentence |

Per **matrix** (as referenced from a suite): `id`, `repo`, `path`, `register` (its MC-###
in `magna_carta_register.yaml`, or `null` for Tranc3-side matrices not yet bridged —
bridging them is a staged action, §7.3).

## 3. Steward assignment is runtime-mutable

The `steward_ai` values here are **designed defaults**, not hard bindings. Tranc3's Role
Assignment Registry (`src/roles/registry.py`, exposed at `/roles`) already lets operators
reassign which AI holds a Location function at runtime, with audit history. Suite
stewardship follows the same rule: the registry is authoritative at runtime; this file
records the baseline it is seeded from. A steward change therefore needs **no code or
doc change** and is captured in the registry's audit trail.

## 4. Feeding the Observatory

Each suite declares an event prefix. The staged integration (§7.2) emits:

- `governance.suite.<name>.review.completed` — steward closes a cadence review
- `governance.suite.<name>.review.overdue` — `next_review` passed without one
- `governance.suite.<name>.matrix.changed` — a member matrix file changed (CI-detected)
- `governance.suite.<name>.escalated` — an item moved up the escalation chain

This gives The Observatory a governance signal stream it currently lacks: today it sees
operational events (capacity, health) but nothing about whether *governance itself* is
being maintained. Suite events use the same `Observatory.record()` path as the existing
`capacity.threshold_crossed` events, so no new infrastructure is required.

## 5. Feeding Magna Carta

Suites strengthen this framework in three ways:

1. **Coverage accounting** — the validator proves every matrix has a governing suite,
   so a new matrix that nobody owns fails CI instead of drifting.
2. **Register bridging** — each matrix row carries its MC-### where one exists; the 14
   Tranc3-side matrices with `register: null` become visible as a worked backlog for
   `tranc3_register_bridge.yaml` instead of an unknown.
3. **Layer B integration** — `matrix_suites_check.py` runs inside
   `run_layer_b_local_ci.sh`, so suite health is checked with the same cadence and
   honesty rules as every other register (overdue = warning, structural error = failure,
   matching the ACT-006 precedent).

## 6. Strengthening The Town Hall

The Town Hall (CranBania) is the procedural surface: the staged integration (§7.4) maps
each suite to a CranBania board lane with a workshop template per review cadence, so a
suite review is a *card with an SLA*, not a calendar hope. CranBania's existing SLA
breach webhooks then give overdue suite reviews the same escalation mechanics as
incidents — which is precisely the Town Hall's PRINCE2/ITIL mandate applied to
governance work itself.

## 7. Staged rollout (what exists now vs next)

| Stage | Deliverable | Status |
|---|---|---|
| 7.1 | Registry (`matrix_suites.yaml`) + this doc + Layer B validator | ✅ this change |
| 7.2 | Observatory emission from Tranc3 (`src/compliance/` reads the registry via the submodule and emits suite events) | staged |
| 7.3 | Bridge the 14 unregistered Tranc3 matrices into `tranc3_register_bridge.yaml` with MC numbers | staged |
| 7.4 | CranBania board lane + workshop template per suite; SLA-backed review cards | staged |
| 7.5 | Role Registry seeding: create the 8 suite-steward roles at `/roles` from this file | staged |

## 8. Honesty rules (inherited)

Per REGULATION-MATRIX.md §6: a suite being *defined* is not a suite being *healthy*.
Nothing in this layer permits claiming a compliance posture that a member matrix's rows
do not evidence. The suite KPI lines state what healthy means; until the staged
integrations land, cadence enforcement is Layer B warnings only.
