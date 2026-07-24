# Revenue Matrix

**Version:** 1.0.0
**Date:** 2026-07-24
**Owner:** Finance / Platform Engineering
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate with a monetisation surface
**Register:** MC-019
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`revenue` section)

---

## 1. Purpose

Tracks, per Service/Solution/Application, whether passive income, revenue-generating strategies, and monetisation techniques are actually implemented — not aspirational. Unlike Legal/Financial/Taxation, this matrix is grounded almost entirely in real, working code: `src/monetisation/billing.py` (Tranc3) already implements a genuine multi-stream revenue engine.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim revenue-generation coverage in product copy unless the corresponding row is ✅ with evidence — several streams below are ❌ (defined but not yet earning), not ✅.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — real, working revenue mechanism, actively integrated |
| ⚠️ | Real mechanism, with a documented caveat (e.g. not yet configured/live) |
| 📋 | Not yet assessed |
| ❌ | Code capability confirmed absent (no such mechanism exists at all) |
| 🎯 | Requires an owner decision (which streams to activate, pricing) or independent production verification this framework cannot self-certify |

---

## 3. Critical caveat: this code has no persistence, so "current status" is not observable

**`PassiveRevenueEngine.__init__`** (`src/monetisation/billing.py`) initializes `self._revenue: Dict[str, float] = dict.fromkeys(self.STREAMS, 0.0)` — every field starts at zero on every process instantiation, in memory only, with **no database or file-backed persistence**. This means:

- Any process restart resets every stream's tracked total to £0, regardless of real-world earnings.
- Reading this class's source code cannot tell us what has actually been earned in production — only that the *mechanism* to record and query revenue exists.
- Separately, Stripe itself defaults to **"free-only mode"** (`src/monetisation/billing.py`'s own log message: `"Stripe not configured — running in free-only mode"`) unless a real `STRIPE_SECRET_KEY` is actually set in the deployment environment — which this scan has no way to confirm from source code alone.

**Corrected per review (charliecreates, P1):** an earlier version of this matrix stated SaaS subscriptions and marketplace fees were "✅ Live" and other streams were "❌ Zero balance," inferring this from the code's structure. That inference was wrong — the zero-initialization is a property of every fresh instance, not evidence about real earnings, and no durable production data was actually queried. Every status below is now downgraded to **code capability confirmed / not independently verified**, not a claim about real revenue.

---

## 4. SaaS subscription tiers (code capability, not confirmed live)

`src/monetisation/billing.py`'s `BillingTier` enum + `TIERS` dict, integrated with Stripe (primary), Lemon Squeezy, and Paddle as alternate providers:

| Tier | Price (GBP/month) | Rate limit | Status |
|---|---|---|---|
| Free | £0 | 100 req/hour | ✅ No external dependency — always active by definition |
| Pro | £29 | 1,000 req/hour | ⚠️ Code reads a Stripe price ID from `STRIPE_PRO_PRICE_ID`; whether that env var is actually set to a real, non-placeholder value in production was not independently verified |
| Business | £149 | 10,000 req/hour, 100,000 req/day | ⚠️ Same caveat as Pro |
| Enterprise/custom | Not fixed (`price_gbp: None`) | Uncapped (`req_per_hour: -1`) | ⚠️ Structurally supported but pricing is per-negotiation, not a published tier |

The webhook handler (`/webhook/stripe`), billing portal, and idempotent event booking (`record_once()`, deduped by Stripe event id, capped at 10,000 remembered ids) are real, well-built code — but their existence is evidence of capability, not evidence that a paying customer has ever completed a checkout.

---

## 5. Passive/multi-stream revenue engine (12 real streams, code capability only)

`RevenueTracker` (`src/monetisation/billing.py`) defines 12 real revenue streams with GBP tracking and a strategy-recommendation engine (fires a suggestion when a stream's in-memory balance is still £0 *at the time that process instance is queried* — not a durable historical signal, per §3). All 12 streams carry the same status for the same reason:

| Stream | Description | Status |
|---|---|---|
| SaaS subscriptions | Recurring monthly billing (§4) | ⚠️ Code capability confirmed; live-earning status not independently verified (§3) |
| API usage metering | Pay-per-request above free tier | ⚠️ Code capability confirmed; not independently verified |
| Personality packs | One-time purchases via Lemon Squeezy | ⚠️ Code capability confirmed; not independently verified |
| White-label licenses | B2B licensing fees | ⚠️ Code capability confirmed; not independently verified |
| Affiliate commissions | Referral links (Ko-fi, Gumroad, Anthropic/OpenRouter/Groq API referrals) | ⚠️ Code capability confirmed; the strategy engine's own recommendation text ("Join Anthropic / OpenRouter / Groq affiliate programmes") exists in source, but is not evidence of current real-world activation status |
| GitHub Sponsors | Open-source supporter income, 0% platform fee | ⚠️ Code capability confirmed; not independently verified |
| Ko-fi tips | Community supporter tips | ⚠️ Code capability confirmed; not independently verified |
| Marketplace fees | Arcadian Exchange 2.5% transaction fee (real calculation: `marketplace_fee()`) | ⚠️ The 2.5% fee-calculation logic itself is real and mathematically correct; whether it has ever been invoked against a real transaction was not independently verified |
| Data insights reports | Anonymised aggregate trend reports | ⚠️ Code capability confirmed; not independently verified |
| Certification fees | Trancendos developer certification programme | ⚠️ Code capability confirmed; not independently verified |
| Ad revenue | Opt-in contextual ads (Carbon Ads, free signup) | ⚠️ Code capability confirmed; not independently verified |
| Consulting | Platform consulting and integration services | ⚠️ Code capability confirmed; not independently verified |

**Not a 13th stream:** the class's own docstring numbered list also mentions "NFT/Digital assets — future: tokenised platform assets," but this is **not** one of the 12 real keys in `RevenueTracker.STREAMS` — verified by inspecting the dict directly. It is a future idea mentioned in a comment, not a defined stream like the 12 above; don't count it toward "12 revenue streams."

**Honest summary:** the *infrastructure* for 12 revenue streams plus SaaS billing is real and well-built (idempotent booking, per-stream ledger, strategy recommendations, real Stripe/VIES/tax logic elsewhere in the same module). But because `RevenueTracker` has no persistence and Stripe's live-configuration status can't be confirmed from source code, **this matrix cannot assert any stream is actually earning in production today.** Do not represent any of these 12 as "active revenue" in product copy without independently querying real production data (e.g. an actual Stripe dashboard balance, or wiring `RevenueTracker` to a persistent store first).

---

## 6. Per-entity monetisation mapping

| Entity | Monetisation role |
|---|---|
| Royal Bank of Arcadia | Billing/payments hub — hosts the Stripe integration surface |
| Arcadian Exchange | Marketplace-fee stream (2.5% transaction fee) |
| API Marketplace | Natural home for future affiliate/API-metering expansion — not yet wired to `RevenueTracker` per this scan |
| The Academy | Natural home for certification-fee stream — not yet wired to `RevenueTracker` per this scan |

Every other entity carries no distinct monetisation surface beyond the estate-wide SaaS tiers.

---

## 7. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Wire `RevenueTracker` to a persistent store so status claims become verifiable | Not yet scheduled | 🎯 Real engineering task — currently the single biggest blocker to this matrix ever reaching a verified ✅ |
| Confirm `STRIPE_SECRET_KEY` is genuinely set in production | Immediate | Manual — check deployment environment, not source code |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 8. Cross-references

- [FINANCIAL-MATRIX.md](FINANCIAL-MATRIX.md) — FCA/regulatory posture on this same billing infrastructure (MC-017)
- [TAXATION-MATRIX.md](TAXATION-MATRIX.md) — tax treatment of this revenue (MC-020)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-019 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
