# Legislation Review Log

**Version:** 1.0.0
**Owner:** DPO / Legal
**Procedure:** [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)
**Register:** [legislation_register.yaml](../../compliance/legislation_register.yaml)
**Check:** MON-011 (`scripts/compliance_health_check.py`)

---

## 1. Purpose

Records each review of the legislation register against authoritative sources, so
that a `review_date` can be shown to have been **met** rather than **moved**.

That distinction is the whole point of this file. Before it existed the register
carried a `review_date` and nothing else, and a reviewer who edited the date and a
reviewer who did the work left an identical trace. `last_reviewed` in the register
now records when an instrument was actually checked; this log records what was
found and against which source.

---

## 2. Review log

| Review ID | Date | Reviewer | Items | Findings | Sign-off |
|-----------|------|----------|-------|----------|----------|
| REV-2026-09-14 | 2026-09-14 | Claude Code (prepared) | 11 active + 1 added | 3 material, 1 open obligation | ⏳ **Owner sign-off pending** |

---

## 3. REV-2026-09-14 — detail

**Trigger.** MON-011 error: ten of eleven `active_legislation` items shared
`review_date: 2026-09-06` and fell overdue together, blocking every pull request
in the repository. Prior review: 2026-06-09 (SCAN-2026-Q2-01).

**Status of this record.** Prepared by an automated reviewer against the sources
cited below. It is **evidence for** the owner's review, not a substitute for it.
The sign-off column stays ⏳ until a named human accepts it. Nothing here should
be read as a legal opinion.

### 3.1 Material findings

#### F-1 — Data (Use and Access) Act 2025 absent from the register (**new instrument**)

The DUAA received Royal Assent 2025-06-19 and **amends** three instruments the
register already tracks: UK GDPR (LEG-001), DPA 2018 (LEG-002) and PECR (LEG-005).
It appeared nowhere in this repository.

| Commencement | Date | Effect |
|---|---|---|
| No. 1 | 2025-08-20 | Part 1 (Smart Data); s.111 amends PECR breach notification |
| No. 3 | 2025-09-05 / 2025-11-17 | s.79 legal professional privilege; ss.88–90 national security |
| No. 6 | **2026-02-05** | Bulk of Part 5 data-protection amendments |
| ICO confirmation | **2026-06-19** | All data protection provisions commenced |

The register was last reviewed **2026-06-09** — four months after the No. 6
commencement and ten days before the ICO's confirmation — and did not catch it.
Added as **LEG-012**.

**Open obligation (not yet evidenced).** s.103 inserts **s.164A DPA 2018**, a
statutory complaints-handling duty requiring a compliant complaints process. The
ICO's stated deadline was **June 2026**, which has passed. Nothing in this
repository evidences such a process. Recorded as an open gap (**ACT-020**) rather
than marked compliant.

#### F-2 — EU AI Act high-risk deadline deferred, transparency unchanged (**LEG-006**)

The Digital Omnibus on AI was published in the OJ **2026-07-24** and entered into
force **2026-07-27** — six days before the original high-risk deadline, and seven
weeks *after* this register was last reviewed.

| Provision | Was | Now |
|---|---|---|
| Art 50 transparency | 2026-08-02 | **2026-08-02 — unchanged, live now** |
| Art 50 watermarking (deployed systems) | 2026-08-02 | 2026-12-02 (grace) |
| Annex III high-risk | 2026-08-02 | **2027-12-02** |
| Annex I embedded products | 2027-08-02 | 2028-08-02 |

**The deferral is not a general reprieve.** Article 50 transparency took effect on
its original schedule and is live today; only the Annex III regime moved. A
register recording "high-risk deadline 2 Aug 2026" and nothing else would have
read as though everything had slipped.

SCAN-2026-Q2-01 explicitly said *"High-risk deadline 2 Aug 2026 — track Digital
Omnibus proposals."* The June review opened this loop; the lapsed date is what
stopped it closing.

#### F-3 — EU CRA reporting obligations now live (**LEG-011**)

Article 14 reporting obligations applied from **2026-09-11** — three days before
this review. Manufacturers must file an early warning within **24 hours** of
becoming aware of an actively exploited vulnerability or severe incident, full
notification within **72 hours**, a final vulnerability report within 14 days of a
fix, and a final incident report within one month. **Legacy products already on
the EU market are in scope.** No retroactive reporting is required for exploitation
known before 2026-09-11.

LEG-011's `review_date` was set to `2026-09-11` — the exact commencement date. That
was a deliberate milestone marker, and MON-011 fired correctly on the day. It read
as a nuisance failure because the check cannot distinguish "routine cadence review"
from "a legal obligation commences today" (see §5).

### 3.2 Items reviewed with no material change

LEG-003 (EU GDPR), LEG-004 (Computer Misuse Act 1990), LEG-007 (CDPA 1988),
LEG-008 (Companies Act 2006), LEG-009 (HIPAA), LEG-010 (FCA Handbook). Register
identifiers, ELI/CELEX URIs and obligation mappings checked as still resolving and
correct. No commencement or amendment in the review window changed a mapped
obligation.

> **Scope limit, stated rather than implied.** F-1 to F-3 were found by targeted
> search against the instruments with known in-window milestones. The six items
> above were checked for identifier integrity and for changes surfacing in the same
> searches; they did not receive an independent clause-by-clause re-reading. A
> reviewer wanting that assurance should say so and it can be done per instrument.

### 3.3 Sources

- [Kennedys — DUAA 2025 commencement dates and planned guidance for 2026](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-data-use-and-access-act-2025-commencement-dates-and-planned-guidance-for-2026/)
- [DLA Piper Privacy Matters — Commencement of the data protection provisions in the DUAA](https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/)
- [Mayer Brown — Preparing for the DUAA 2025: upcoming complaints procedure requirement](https://www.mayerbrown.com/en/insights/publications/2026/02/preparing-for-the-data-use-and-access-act-2025-upcoming-complaints-procedure-requirement)
- [Gibson Dunn — EU AI Act Omnibus agreement: postponed high-risk deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [Freshfields — The final Digital Omnibus on AI: key amendments](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-ai-act-unpacked-34-the-final-digital-omnibus-on-ai-key-amendments-to-the-a-102nber)
- [Jones Day — EU CRA 24-hour reporting duties start 11 September 2026](https://www.jonesday.com/en/insights/2026/07/eu-cyber-resilience-act-24hour-reporting-duties-start-september-11-2026)
- [European Commission — CRA reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- [Goodwin — Preparing for the EU CRA: key reporting obligations from 11 September 2026](https://www.goodwinlaw.com/en/insights/publications/2026/09/alerts-lifesciences-technology-preparing-for-eu-cra)

---

## 4. What changed in the register

| Change | Detail |
|---|---|
| `review_cycle` added per item | quarterly / semiannual / annual, set by how fast the instrument moves — not one blanket figure |
| `last_reviewed` added per item | separates "checked" from "next due" |
| Dates staggered | 11 items → **11 distinct dates** (was 10 on one day) |
| LEG-012 added | Data (Use and Access) Act 2025 |
| LEG-006 `key_dates` | four Omnibus dates recorded per-provision |
| `standards_watch.yaml` | 5 items → 5 distinct dates (was all 5 on 2026-12-08) |
| EEV-006 closed | quarterly EUR-Lex scan performed as part of this review |

---

## 5. Why this recurred, and what now prevents it

The ten lapses were not ten oversights. The register was generated on 2026-06-08
and every item stamped with `meta.review_cycle` (quarterly) added to that single
generation date, so they came due together and failed together.

Three defects, all fixed:

1. **No warning band.** `max_overdue_days: 0` with nothing before it — the check
   was silent until the day it hard-failed. Now `warn_within_days: 30` on MON-011,
   MON-012 and MON-015: they name the item while there is still time to act.
2. **No anti-cliff rule.** Staggering fixes today; only a rule stops recurrence —
   and it had already been recreated, with all five `standards_watch` entries
   sharing 2026-12-08. `max_shared_review_date: 2` now errors on re-clustering.
3. **No per-item cadence.** One register-level `review_cycle` meant one date for
   everything. Cadence is now per item.

**Known limitation, recorded not hidden.** MON-011 still cannot distinguish a
routine cadence review from a legal milestone (F-3). Both surface as the same
overdue error. Splitting `obligation_milestones` from `review_date` is the next
improvement; it is not done here.

---

## 6. Sign-off

| Role | Name | Date | Accepted |
|------|------|------|----------|
| DPO / Legal | _pending_ | | ⏳ |

Until this row is completed, `last_reviewed: 2026-09-14` in the register means
*"an automated review was prepared on this date"*, not *"a competent person
accepted it"*.
