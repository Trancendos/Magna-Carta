# EU Cyber Resilience Act — Compliance Profile

**Version:** 1.0.0
**Date:** 2026-08-19
**Owner:** Platform Owner Trancendos / DPO
**Status:** 🔴 Programme — newly opened; the estate had no CRA coverage before this document
**Act:** Regulation (EU) 2024/2847 · CELEX `32024R2847` · OJ L, 2024/2847, 20.11.2024
**Register entries:** `LEG-011` (legislation register), `MC-042`–`MC-047` (Magna Carta register)

**Machine-readable:** [compliance/legislation_register.yaml](../../compliance/legislation_register.yaml)
**Related:** [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md) ·
[LICENSE-COMPLIANCE-MATRIX.md](LICENSE-COMPLIANCE-MATRIX.md) ·
Tranc3 `docs/governance/OBSOLESCENCE-ACCEPTED.md`

---

## 1. Why this exists, and why now

Until this document, the Magna Carta framework had **zero** references to the Cyber
Resilience Act. That is a real gap rather than a deliberate scoping decision: the EU
legislation register tracks the AI Act and GDPR as active, and watch-lists the Data Act,
NIS2 and DORA — but not the one EU regulation that speaks directly to what this platform
is, which is a large body of software assembled largely from open source.

The prompt to open it was the 2026 OSSRA report, whose central findings map onto CRA
obligations almost line for line: 93% of audited codebases carry components with no
upstream development in over two years, 64% of components are transitive, and the CRA
expects a manufacturer to know both facts about its own product, continuously, for at
least five years.

## 2. The dates that matter

| Date | What changes | Source |
|---|---|---|
| 10 December 2024 | CRA entered into force | European Commission |
| **11 September 2026** | **Reporting obligations for actively exploited vulnerabilities and severe incidents become mandatory** | European Commission |
| 11 December 2027 | All substantive requirements apply, with enforcement and penalties | European Commission |

Both the September 2026 and December 2027 dates were verified against the European
Commission's own CRA page rather than taken from secondary reporting, because the whole
urgency argument rests on them.

## 3. Does the CRA apply to Trancendos?

Two questions decide this, and they have different answers.

### 3.1 Is this a commercial activity? — Almost certainly yes

The CRA carves out free and open-source software supplied **outside the course of a
commercial activity**. Tranc3 is a public repository, so it is tempting to assume the
carve-out applies. It does not, on the evidence in the repository itself:
`src/monetisation/billing.py` defines paid tiers (free / pro £29 / business £149) with
Stripe price IDs wired to `STRIPE_PRO_PRICE_ID` and `STRIPE_BUSINESS_PRICE_ID`. Charging
for the service is a commercial activity, and the carve-out is not available to a product
monetised that way merely because its source is public.

**This determination should be confirmed by qualified legal advice.** It is recorded here
as the working assumption with its supporting evidence, not as settled law, and the
consequence of being wrong in the optimistic direction is severe enough to warrant the
check.

### 3.2 Has a product been placed on the EU market? — Not yet, and that is the opportunity

CRA obligations attach to a product with digital elements **placed on the market**. Per
`docs/GO_LIVE_GAP_ANALYSIS.md`, the estate is not yet deployed — the remaining go-live
blocker is precisely that. Nothing has been placed on any market.

This is the single most useful thing in this profile, so it is worth stating plainly:

> The CRA deadline is real, but its trigger is **go-live**, not the calendar. Trancendos
> is in the rare and valuable position of being able to meet the CRA at first placement
> rather than retrofitting it afterwards.

The practical consequence is a sequencing decision, not a panic: **CRA readiness belongs
in the go-live gate.** Every obligation below is cheaper to satisfy before first
placement than after, and the ones about component selection and support-period
commitment are *substantially* cheaper — OSSRA's own data shows most organisations
approach the CRA from a starting position of years of accumulated maintenance debt. This
estate does not have to.

If go-live occurs before 11 September 2026, the reporting obligations apply from that
date. If after, they apply from placement.

## 4. Obligation mapping

Status key: ✅ satisfied · 🟡 partial · 🔴 gap · ⬜ not yet triggered

| Ref | CRA obligation | Status | What exists today | What is missing |
|---|---|---|---|---|
| MC-042 | **SBOM covering at least direct dependencies, kept current throughout the support period** | 🟡 | `.forgejo/workflows/security-scan.yml` `sbom-generation` runs syft producing both CycloneDX and SPDX, with grype matching and conditional Dependency-Track upload | SBOMs are CI artefacts with a retention window, not lifecycle-retained records. The CRA expects the SBOM for a *released product version* to remain available and current across the support period. Needs durable, version-keyed retention |
| MC-043 | **Product placed on the market free from known exploitable vulnerabilities** | ✅ | `scripts/vulnerability_census.py` + `--check` in the production gate; fixable vulnerabilities cap the security score below green and block the gate. Currently 0 fixable, 1 accepted (`ecdsa` PYSEC-2026-1325, documented and guarded) | Nothing structural. The accepted-risk disposition must be reviewable by a market surveillance authority, which `SECURITY_ALERT_REGISTER.md` already provides |
| MC-044 | **Component maintenance trajectory evaluated at selection and tracked continuously** | ✅ | `scripts/obsolescence_census.py` measures upstream liveness and our lag for all 110 direct dependencies; `docs/governance/OBSOLESCENCE-ACCEPTED.md` records a reasoned disposition per dormant component; weekly scheduled run in `dependency-audit.yml` | Nothing structural. This obligation was the OSSRA finding that prompted the work, and it is now the best-covered one |
| MC-045 | **24h / 72h / 14d reporting to the CSIRT coordinator and ENISA** | 🔴 | Nothing. No designated CSIRT, no notification path, no clock, no named responsible role | The whole mechanism. See §5 — this is the binding gap |
| MC-046 | **Declared support period (min. 5 years absent shorter product life), transparent to users** | 🔴 | Nothing. No support period is declared anywhere | A published support-period statement per product, and the decision about what it is. Must be made *before* first placement, because it is a commitment to users |
| MC-047 | **Technical documentation retained 10 years; security updates available 10 years post-support-period** | 🔴 | Governance documentation exists and is version-controlled, which is a good start, but no retention policy targets these durations | A retention class for CRA technical documentation. The Observatory already has `retention_class` and `legal_hold` fields — this needs a class defined and applied |
| — | Vulnerability reported to the component's maintainer when found | 🟡 | No formal process; ad-hoc in practice | A step in the incident procedure. Cheap to add, easy to forget |
| — | Importer/distributor obligations | ⬜ | Not applicable — Trancendos manufactures rather than imports or distributes third-party products | Revisit if the API Marketplace ever redistributes third-party products |

## 5. The binding gap: the 24-hour clock

Of everything above, MC-045 is the obligation that cannot be satisfied by writing a
document, and it is the one whose deadline arrives first.

From 11 September 2026 a manufacturer must, on becoming aware of a vulnerability in its
product that is **known to be exploitable** (for example, proof-of-concept code exists):

1. **Within 24 hours** — early warning to the CSIRT designated as coordinator in the
   Member State of main establishment, and to ENISA.
2. **Within 72 hours** — notification following triage confirming whether the product is
   affected.
3. **Within 14 days of a corrective measure** — final report.

Twenty-four hours is not a scanning interval. It is a *lookup* interval. The obligation
is unmeetable by a process that starts with "run a scan and see what we use", because a
scan takes time, may fail, and answers the question for today's `main` rather than for
the released version a customer is running.

What it actually demands is that the question **"does advisory X affect any version of
our product that is currently in the field?"** is answerable from an existing inventory in
minutes. That is why MC-042's gap — SBOMs as ephemeral CI artefacts rather than durable,
version-keyed records — is more serious than it looks, and why it is the dependency of
MC-045 rather than a parallel item.

Note also that the count starts from *awareness*, so a feed that tells you late does not
extend the clock; it shortens the part of it you have left.

### Minimum viable mechanism

Nothing here needs new infrastructure — every piece has an existing home:

| Piece | Where it belongs |
|---|---|
| Durable per-release SBOM store | The Artifactory (`workers/artifactory-service/`, Zot OCI registry) — SBOMs are OCI referrers, which is what that service already does |
| Advisory intake (EUVD, GHSA, OSV) | Cryptex (`src/cryptex/`) — threat intel is its stated function |
| "Am I affected?" lookup | Query the SBOM store, not the repository |
| Clock, escalation, timers | The escalation FSM (`src/governance/`) already implements timed escalation |
| Immutable record of who reported what and when | The Observatory — this is the audit evidence a surveillance authority would request |
| Named accountable role | Role Assignment Registry (`/roles`) — needs a **CRA Reporting Officer** role seeded |
| Review card and SLA per incident | CranBania / The Town Hall |

The work is integration, not invention. That is a deliberate design consequence of the
platform already having these services, and it should be sequenced as one piece of work
before go-live rather than six.

## 6. Open source stewards

The CRA introduces a third category alongside manufacturer and distributor: the **open
source steward** — a legal entity that voluntarily performs security analysis, including
publishing patches, for defined open source libraries. Stewards carry reporting and
cooperation duties but not the manufacturer's penalties.

Two consequences for Trancendos, in opposite directions:

**As a consumer.** Components governed by an established foundation (Apache, Eclipse,
Linux Foundation) will have documented cybersecurity policies and a vulnerability-handling
process; components maintained by one person may not. That does not make the latter worse
software, but it does make its maintenance trajectory less predictable — which matters
directly when committing to a five-year support period. This is a criterion that belongs
in component selection, and it is exactly the judgement
`docs/governance/OBSOLESCENCE-ACCEPTED.md` is already asking for. `pyswarms`, at 2,053
days without a release, is the current worked example.

**As a potential steward.** If Trancendos ever publishes a library others depend on, the
steward role would attach. Not applicable today; recorded so it is not discovered late.

## 7. What this profile does not do

It does not claim compliance. Three of the seven mapped obligations are open gaps, one of
them (MC-045) substantial, and the applicability determination in §3.1 needs legal
confirmation. The status at the top of this document is 🔴 Programme for that reason.

It also does not set the support period. That is a business commitment about how long
Trancendos will maintain what it ships, and it is the owner's decision, not a compliance
artefact — but it must be made before first placement, because it is published to users
and cannot easily be shortened afterwards.

## 8. Review

| Trigger | Action |
|---|---|
| Before go-live | Re-read in full. CRA readiness is a go-live gate item per §3.2 |
| 11 September 2026 | Reporting obligations live. MC-045 must be operational if anything is placed on the market |
| Quarterly | Standard Magna Carta review cycle |
| On CRA delegated/implementing acts | Standards and technical specifications are still emerging; monitored via `EU-LEGISLATION-MONITORING.md` |
