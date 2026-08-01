# Capital Governance — how automated actors are allowed to handle money

**Version:** 1.0.0
**Date:** 2026-08-01
**Machine-readable:** [compliance/capital_governance.yaml](../../compliance/capital_governance.yaml)
**Validated by:** `scripts/capital_governance_check.py` (runs in Layer B CI)
**Status:** Registry layer implemented; adopter bindings and runtime enforcement are staged (§7)

---

## 1. What this governs

Any automated actor that spends, allocates, risks, or earns money on behalf of an
adopting platform — regardless of method or venue.

It is deliberately **method-agnostic**. It does not know or care whether return is
sought through markets, yield, content, affiliate revenue, licensing, or a method
nobody has invented yet. It constrains *exposure* and demands *evidence*. New
methods register as functions under the same ladder rather than requiring new rules.

## 2. Why it is generic

Magna Carta is a governance layer any solution can adopt. That property only holds
if the rules name no adopter's entities. A rule that mentions one platform's AIs,
venues or locations is that platform's configuration wearing a governance rule's
clothes.

This degrades quietly: someone adds a convenient reference, nothing breaks, and the
layer stops being portable one line at a time. `capital_governance_check.py`
therefore fails the build on any adopter-specific proper noun in the register.

Adopters supply a **binding file** mapping each generic `role_id` to a real actor.
A binding may configure; it may not relax `ledger_separation`, `demotion`, or the
kill switches — the three controls that exist precisely to override local judgement
under pressure.

## 3. Two function types

The distinction that matters is not which market, but **what failure does**.

| | Internal Function | External Function |
|---|---|---|
| Intent | Cost reduction | Capital gain |
| Spends to | Reduce the platform's own operating cost | Generate return |
| Exposure | Bounded by budget line | Unbounded without controls |
| Failure mode | Overspend | Loss of principal |
| Principal at risk | No | Yes |

Both may run side by side. An adopter can operate an internal procurement function
and an external investment function simultaneously — they are different jobs with
different risk postures, not competing designs.

## 4. Ledger separation — the load-bearing rule

**No function type may draw on another's ledger, under any condition.**

If an external function can reach the internal budget, a trading loss stops being a
trading loss and becomes an *infrastructure outage*: compute that cannot be paid for
because a position moved against it. The failure crosses from the money domain into
the availability domain, and the platform loses the ability to operate at exactly the
moment it is losing money — the worst possible correlation.

Transfers are not permitted by default. An exception requires the human owner,
explicit approval, recorded justification, and a post-transfer audit entry — and it
remains a transfer between separate ledgers. There is no configuration under which
they merge.

This is stated before any tier or limit because it is very hard to retrofit once
ledgers are entangled.

## 5. Capital tiers

A ladder that is climbed, not granted.

| Tier | Band (units) | External execution | Risk/action | Daily loss | Positions | Leverage |
|---|---|---|---|---|---|---|
| TIER-0 Simulated | 0–20 | **Simulated only** | 1% | 5% | 1 | none |
| TIER-1 Constrained Live | 20–100 | Live permitted | 2% | 5% | 2 | none |
| TIER-2 Diversified | 100–500 | Live permitted | 2% | 4% | 4 | ≤2× |
| TIER-3 Established | 500+ | Live permitted | 2% | 3% | 6 | ≤3× |

**Why TIER-0 is simulation-only.** Not caution — arithmetic. At 20 units with a 1%
risk budget, an action is sized at 0.2 units, while venues commonly reject orders
below roughly 10 units of notional. A live order at this tier either cannot be placed
at all, or can only be placed by abandoning the risk limit entirely. Simulation
against real data is the only coherent behaviour, and it is also where an operator
learns what loss feels like before loss is real.

Bands are expressed in a currency-neutral unit the binding defines, so the ladder is
not tied to one currency or starting sum.

## 6. Progression and demotion are asymmetric — deliberately

**Promotion** requires recorded actions, observation days, zero limit breaches,
specific evidence, and approval. Equity crossing a boundary is necessary but never
sufficient; without that, an operator that got lucky once is promoted for it.

Evidence escalates with the tier: TIER-1 wants a complete decision journal, TIER-2
wants a demonstrated drawdown *recovery*, TIER-3 wants performance across two
distinct regimes so the record reflects adaptation rather than one good environment.

**The simulated → live transition** is the one progression the presiding authority
cannot grant alone. Only the human owner may authorise real money entering the
system for the first time.

**Demotion** requires no approval and happens immediately. A tier is held, not owned.
If promotion needs evidence but demotion needed approval too, a failing operator
would keep the permissions it earned while healthy at precisely the moment those
permissions are most dangerous.

## 7. Staged rollout

| Stage | Deliverable | Status |
|---|---|---|
| 7.1 | Registry + this doc + Layer B validator | ✅ this change |
| 7.2 | Adopter binding schema and worked example | staged |
| 7.3 | Runtime enforcement: pre-action risk evaluation against tier limits | staged |
| 7.4 | Decision-journal persistence and progression-gate assessment | staged |
| 7.5 | Observatory event emission under `governance.capital.*` | staged |

## 8. Honesty rules (inherited)

Per `REGULATION-MATRIX.md` §6:

- A function being **defined** is not a function being **profitable**.
- A tier being **permitted** is not a tier being **earned**.
- Simulated results must be labelled simulated wherever reported.
- Nothing here authorises offering capital services to third parties. Deploying an
  operator's own capital and handling other people's money are different activities
  under most financial regulation, and the second is out of scope for this layer.
