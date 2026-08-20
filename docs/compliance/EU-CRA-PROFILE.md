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

The prompt to open it was the **2026 Open Source Security and Risk Analysis (OSSRA)
report** (Black Duck), covering 947 commercial codebases audited between November 2024
and October 2025. Its central findings map onto CRA obligations almost line for line:
93% of audited codebases carry components with no upstream development in over two
years, and 64% of components in a typical codebase are transitive. The CRA expects a
manufacturer to know both facts about its own product, continuously, across a support
period of at least five years. Those figures are cited as *motivation* for opening this
profile; no obligation below rests on them.

## 2. The dates that matter

| Date | What changes | Source |
|---|---|---|
| 10 December 2024 | CRA entered into force | European Commission |
| 11 June 2026 | Chapter IV (Arts 35–51, notification of conformity assessment bodies) applies — **already in force** | Art. 71(2) |
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
blocker is precisely that.

**"Not deployed" is weaker evidence than it sounds, and is not by itself the finding.**
Making a product available on the Union market covers more routes than a production
deployment: a public download, a release artefact, a hosted preview or pilot, or EU
customer access to a running instance can each constitute availability. Publishing
source in a public repository does not, on its own. So the honest statement is
conditional: *no supply route has been identified through which a product with digital
elements has been made available to EU users, and the production deployment that would
create one has not happened.* Confirming that positively across every channel — not just
the deployment one — is a recorded open action, not a settled conclusion.

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
| MC-042 | **SBOM covering at least top-level dependencies, kept current throughout the support period** (Annex I, Pt II, pt 1) | 🟡 | `.forgejo/workflows/security-scan.yml` `sbom-generation` runs syft producing both CycloneDX and SPDX, with grype matching and conditional Dependency-Track upload | SBOMs are CI artefacts with a retention window, not lifecycle-retained records. The CRA expects the SBOM for a *released product version* to remain available and current across the support period. Needs durable, version-keyed retention |
| MC-043 | **Product placed on the market free from known exploitable vulnerabilities** | ✅ | `scripts/vulnerability_census.py` + `--check` in the production gate; fixable vulnerabilities cap the security score below green and block the gate. Currently 0 fixable, 1 accepted (`ecdsa` PYSEC-2026-1325, documented and guarded) | Nothing structural in the control. **Scope limit:** the duty attaches at *placement*, and nothing is placed — so this evidences the gate that will apply, not a released version. Re-evidence per release once releases exist |
| MC-044 | **Component maintenance trajectory evaluated at selection and tracked continuously** (Art. 13(5) + Recital 34) | 🟡 | `scripts/obsolescence_census.py` measures upstream liveness and our lag for all 110 direct dependencies; `docs/governance/OBSOLESCENCE-ACCEPTED.md` records a reasoned disposition per dormant component; weekly scheduled run in `dependency-audit.yml` | Direct dependencies only. That satisfies the Annex I SBOM floor ("top-level dependencies") but not the full reach of Art. 13(5), whose due diligence covers integrated components generally — and OSSRA measures 64% of components as transitive. Best-covered of the six, and not complete |
| MC-045 | **Art. 14 reporting via the Art. 16 platform — 24h / 72h, then 14 days (vulnerability) or one month (severe incident)** | 🔴 | Nothing. The applicable notification endpoint is undetermined, no notification path has been exercised, no clock runs, no responsible role is named | The whole mechanism. See §5 — this is the binding gap |
| MC-046 | **Declared support period (min. 5 years absent shorter product life), transparent to users** | 🔴 | Nothing. No support period is declared anywhere | A published support-period statement per product, and the decision about what it is. Must be made *before* first placement, because it is a commitment to users |
| MC-047 | **Retention — technical documentation + EU DoC (Art. 13(13)) and security updates (Art. 13(9)), each for 10 years *or* the support period, whichever is longer** | 🔴 | Governance documentation exists and is version-controlled, which is a good start, but no retention policy targets either duration | Two retention classes, one per clock. The Observatory already has `retention_class` and `legal_hold` fields, so this is configuration, not machinery. **Corrected 2026-08-19:** an earlier draft cited Art. 13(12) + Art. 31 and described the duty as "10 years *after* the support period" — both wrong, and the second overstated the obligation |
| — | Vulnerability reported to the component's maintainer when found | 🟡 | No formal process; ad-hoc in practice | A step in the incident procedure. Cheap to add, easy to forget |
| — | Importer/distributor obligations | ⬜ | Not applicable — Trancendos manufactures rather than imports or distributes third-party products | Revisit if the API Marketplace ever redistributes third-party products |

## 5. The binding gap: the 24-hour clock

Of everything above, MC-045 is the obligation that cannot be satisfied by writing a
document, and it is the one whose deadline arrives first.

From 11 September 2026, Article 14 creates **two reporting paths that share their first
two deadlines and differ in the third.** Both are submitted through the single reporting
platform established under Article 16, to the electronic notification end-point of a
coordinating CSIRT, and are *simultaneously accessible to ENISA* — ENISA is not a second
submission to make.

### Which endpoint: a two-branch determination

Which coordinating CSIRT is not our choice to make, and Article 14(7) gives two branches
rather than one. The second is probably ours.

**(a) Main establishment in the Union.** The coordinating CSIRT of that Member State.
"Main establishment" means the place decisions about the cybersecurity of its products
are predominantly taken — and where *that* cannot be determined, the Regulation deems it
the Member State in which the manufacturer has the establishment with the **highest
number of employees** in the Union.

Both rungs sit inside branch (a), and the distinction matters: a manufacturer that *has*
Union establishments but cannot pinpoint where its cybersecurity decisions are taken
stays in (a) on the employee-count rung. It does not fall through to (b). Reading it the
other way would route mandatory reports to the wrong authority.

**(b) No main establishment in the Union at all.** An ordered fallback, first available
wins:

| Order | Member State determined by |
|---|---|
| 1 | where the **authorised representative** acting for the highest number of the manufacturer's products is established |
| 2 | where the **importer** placing the highest number on the market is established |
| 3 | where the **distributor** making the highest number available is established |
| 4 | where the highest number of **users** are located |

**Branch (b) is the live question, and it has an unusual consequence.** Trancendos prices
in GBP (`src/monetisation/billing.py` — free / £29 / £149) and operates from
trancendos.com, which points away from a Union establishment. That is evidence for the
determination rather than the determination itself, since establishment turns on where
cybersecurity decisions are taken and not on currency or domain — but if (b) holds, then
Trancendos has no authorised representative, no importer and no distributor, and the
chain collapses to row 4.

Row 4 means **the endpoint follows where our users are**, and therefore cannot be settled
until there are users. That makes it a go-live determination in the strict sense: not
merely something to do before go-live, but something go-live itself determines. Writing
the rule down now is what makes it answerable on day one rather than during a running
24-hour clock.

So the open work is: settle which branch applies, resolve the resulting CSIRT's endpoint,
and exercise the route once.

**(a) An actively exploited vulnerability in the product**

1. **Within 24 hours of becoming aware** — early warning.
2. **Within 72 hours** — vulnerability notification, with the product details, the nature
   of the exploit, and any corrective or mitigating measures taken.
3. **No later than 14 days after a corrective or mitigating measure is available** —
   final report.

**(b) A severe incident affecting the security of the product**

1. **Within 24 hours of becoming aware** — early warning.
2. **Within 72 hours** — incident notification.
3. **No later than one month after the *submission* of that incident notification** —
   final report. The clock runs from when the notification is actually submitted, not
   from the expiry of the 72-hour window, so notifying early shortens this deadline too.

Two details worth stating precisely, because getting either wrong sets the clock running
on the wrong event or stops it too late:

- **The trigger is "actively exploited", not "exploitable".** An earlier draft of this
  section glossed it as "for example, proof-of-concept code exists". That is not the
  test. Published proof-of-concept code is evidence that a vulnerability *could* be
  exploited; the obligation attaches to evidence that it *is being* exploited.
- **The final-report clocks differ** — 14 days from the availability of a fix for a
  vulnerability, one month from the *submission* of the notification for an incident —
  and they are anchored
  to different events. A single combined procedure will get one of them wrong.

Twenty-four hours is not a scanning interval. It is a *lookup* interval. The obligation
is unmeetable by a process that starts with "run a scan and see what we use", because a
scan takes time, may fail, and answers the question for today's `main` rather than for
the released version a customer is running.

What it actually demands is that the question **"does advisory X affect any version of
our product that is currently in the field?"** is answerable from an existing inventory in
minutes. That is why MC-042's gap — SBOMs as ephemeral CI artefacts rather than durable,
version-keyed records — is more serious than it looks.

**But MC-045 is not *conditional* on MC-042, and must not be scheduled as if it were.**
The Article 14 clocks run from awareness whether or not a good inventory exists; "we were
still building the SBOM store" is not a defence, it is a description of how the deadline
came to be missed. They are two independent go-live gates. Durable SBOM retention makes
the lookup fast and reliable; until it lands, an interim answer to "which shipped
versions contain component X?" still has to exist — and has to be **exercised at least
once against a real advisory**, because an untested reporting path is not a reporting
path.

Note also that the count starts from *awareness*, so a feed that tells you late does not
extend the clock; it shortens the part of it you have left.

### Minimum viable mechanism

Every piece has a plausible existing home. These are **candidate mappings, not verified
contracts** — each needs confirming against what the service actually does today before
this work can honestly be called integration rather than invention. Anything that fails
its check becomes an explicit go-live gap rather than an assumption:

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
