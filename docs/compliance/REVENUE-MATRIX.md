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
| ❌ | Defined in code but not yet generating revenue (zero-balance stream) |
| 🎯 | Requires an owner decision (which streams to activate, pricing) |

---

## 3. SaaS subscription tiers (real, working)

`src/monetisation/billing.py`'s `BillingTier` enum + `TIERS` dict, integrated with Stripe (primary), Lemon Squeezy, and Paddle as alternate providers:

| Tier | Price (GBP/month) | Rate limit | Status |
|---|---|---|---|
| Free | £0 | 100 req/hour | ✅ |
| Pro | £29 | 1,000 req/hour | ✅ Stripe price ID wired via `STRIPE_PRO_PRICE_ID` env var |
| Business | £149 | 10,000 req/hour, 100,000 req/day | ✅ Stripe price ID wired via `STRIPE_BUSINESS_PRICE_ID` env var |
| Enterprise/custom | Not fixed (`price_gbp: None`) | Uncapped (`req_per_hour: -1`) | ⚠️ Structurally supported but pricing is per-negotiation, not a published tier |

Stripe integration is real: webhook handler at `/webhook/stripe` (`src/monetisation/router.py`), billing portal, and idempotent event booking (`record_once()` dedupes by Stripe event id, capped at 10,000 remembered ids).

---

## 4. Passive/multi-stream revenue engine (real code, per-stream status)

`RevenueTracker` (`src/monetisation/billing.py`) defines 12 real revenue streams with GBP tracking, a strategy-recommendation engine (fires a suggestion when a stream's balance is still £0), and a persistent transaction ledger. Current status of each, per the class's own zero-balance detection logic:

| Stream | Description | Status |
|---|---|---|
| SaaS subscriptions | Recurring monthly billing (§3) | ✅ Live — real Stripe integration |
| API usage metering | Pay-per-request above free tier | 📋 Defined; live-usage status not independently verified in this scan |
| Personality packs | One-time purchases via Lemon Squeezy | 📋 Defined; not verified live |
| White-label licenses | B2B licensing fees | 📋 Defined; not verified live |
| Affiliate commissions | Referral links (Ko-fi, Gumroad, Anthropic/OpenRouter/Groq API referrals) | ❌ Zero balance — the code's own strategy engine recommends: "Join Anthropic / OpenRouter / Groq affiliate programmes — earn per referred API user" |
| GitHub Sponsors | Open-source supporter income, 0% platform fee | ❌ Zero balance — code's own recommendation: "Set up GitHub Sponsors (0% fee) at github.com/sponsors" |
| Ko-fi tips | Community supporter tips | ❌ Zero balance — not yet configured |
| Marketplace fees | Arcadian Exchange 2.5% transaction fee (real calculation: `marketplace_fee()`) | ⚠️ Fee-calculation logic is real and correct; actual transaction volume was below the code's own £100 "meaningful activity" threshold at last check |
| Data insights reports | Anonymised aggregate trend reports | 📋 Defined; not verified live |
| Certification fees | Trancendos developer certification programme | ❌ Zero balance — not yet configured |
| Ad revenue | Opt-in contextual ads (Carbon Ads, free signup) | ❌ Zero balance — code's own recommendation exists for this too |
| Consulting | Platform consulting and integration services | 📋 Defined; not verified live |

**Not a 13th stream:** the class's own docstring numbered list also mentions "NFT/Digital assets — future: tokenised platform assets," but this is **not** one of the 12 real keys in `RevenueTracker.STREAMS` — verified by inspecting the dict directly. It is a future idea mentioned in a comment, not a defined-but-dormant stream like the 12 above; don't count it toward "12 revenue streams."

**Honest summary:** the *infrastructure* for 12 revenue streams is real and well-built (idempotent booking, per-stream ledger, strategy recommendations), but only SaaS subscriptions and marketplace fees show any real activity signal — the rest are genuinely defined-but-dormant, not yet monetising. Do not represent all 12 as "active revenue streams" in product copy.

---

## 5. Per-entity monetisation mapping

| Entity | Monetisation role |
|---|---|
| Royal Bank of Arcadia | Billing/payments hub — hosts the Stripe integration surface |
| Arcadian Exchange | Marketplace-fee stream (2.5% transaction fee) |
| API Marketplace | Natural home for future affiliate/API-metering expansion — not yet wired to `RevenueTracker` per this scan |
| The Academy | Natural home for certification-fee stream — not yet wired to `RevenueTracker` per this scan |

Every other entity carries no distinct monetisation surface beyond the estate-wide SaaS tiers.

---

## 6. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Zero-balance stream activation review | Quarterly | `RevenueTracker`'s own strategy-recommendation output — already code-generated, just needs a regular read |
| Marketplace-fee volume re-check | Monthly | Query `RevenueTracker._revenue["marketplace_fees"]` |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 7. Cross-references

- [FINANCIAL-MATRIX.md](FINANCIAL-MATRIX.md) — FCA/regulatory posture on this same billing infrastructure (MC-017)
- [TAXATION-MATRIX.md](TAXATION-MATRIX.md) — tax treatment of this revenue (MC-020)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-019 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
