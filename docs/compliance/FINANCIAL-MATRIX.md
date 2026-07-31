# Financial Matrix

**Version:** 1.0.1
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Finance / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate that touches money movement, billing, or financial regulation
**Register:** MC-017
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`financial` section)

**2026-07-25 re-audit:** every code-grounded claim re-verified against current source — `src/monetisation/billing.py`'s pro (£29) / business (£149) tier pricing, `StripeManager`, and the `/webhook/stripe` route (`src/monetisation/router.py:170`) are unchanged; `workers/ledger-service/worker.py` still computes a SHA-256 hash chain over `entry_id:prev_hash:actor:action:timestamp` (still a generic audit/integrity log, not a financial ledger); `compliance/supplier_dpa_register.yaml`'s SUP-003 entry is still `dpa_status: "Template issued"` with the same "Execute signed DPA before production payment routing" note. No drift found — this matrix's findings hold unchanged.

## 1. Purpose

Tracks, per Service/Solution/Application, whether UK FCA (Financial Conduct Authority) alignment and other financial-regulatory obligations are real and current — building on the existing programme-level [MC-009 FCA Alignment Programme](../../compliance/magna_carta_register.yaml) with entity-level detail, and researching global financial-regulation equivalents where relevant, per the requesting user's ask.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim financial-regulatory compliance in product copy unless the corresponding row is ✅ with evidence. This matrix cannot substitute for real regulatory/legal advice on FCA authorisation status.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — real, current, evidenced |
| ⚠️ | Verified with a documented caveat |
| 📋 | Not yet assessed |
| ❌ | Confirmed gap |
| 🎯 | Requires real regulatory/legal/accounting input — this framework cannot self-certify |

---

## 3. FCA alignment (existing MC-009 programme — entity-level detail)

The estate-wide [FCA Alignment Programme](../../compliance/magna_carta_register.yaml) (MC-009) already establishes the headline finding, confirmed real in `docs/compliance/FCA-ALIGNMENT.md`: **Trancendos operates outside direct FCA authorisation** — no client-money holding, no PSD2 authorisation, and AI outputs must never be presented as regulated financial advice. This matrix does not repeat that analysis; it adds per-entity granularity.

| Entity | Function | FCA-relevant status |
|---|---|---|
| Royal Bank of Arcadia | Billing, payments (Cloudflare Worker `arcadia-royal-bank`, no source in this repo per its charter-only doc-pack) | ⚠️ Operates as a payments *facilitator* via a PSP, not as an FCA-authorised institution itself, per MC-009's own finding — no client money is held directly |
| Arcadian Exchange | Procurement & resource trading | 📋 Not separately assessed — the resource-trading function (compute/storage/model/API-credit procurement, per its `agent_teams`) is an internal cost-optimization mechanism, not a customer-facing financial exchange in the regulated sense; this interpretation has not been confirmed by real legal/regulatory review |
| `src/monetisation/billing.py` (Tranc3) | Stripe-based subscription billing (free/pro £29/business £149 tiers) | ✅ Real, working Stripe integration (`stripe_manager`, webhook handler at `/webhook/stripe`, billing portal) — this is standard SaaS subscription billing via an authorised PSP (Stripe), not itself a regulated payment service |
| `workers/ledger-service/worker.py` | Immutable audit hash-chain (SHA-256, actor/action/resource) | ⚠️ **Not a financial ledger** — genuinely a generic audit/integrity log, not tied to money movement or balances. Flagged here to prevent the name "ledger-service" being mistaken for financial-transaction infrastructure in future audits |

---

## 4. Payment Service Provider (PSP) status

| Item | Status | Finding |
|---|---|---|
| PSP DPA (SUP-003) | ⚠️ | `compliance/supplier_dpa_register.yaml`'s SUP-003 entry status is `"Template issued"` — **not yet signed** — with an explicit note: "Execute signed DPA before production payment routing." No specific PSP (e.g. Stripe as a named legal entity) is recorded against SUP-003; treat as generic/unassigned until confirmed |
| Transfer mechanism | ✅ | UK IDTA (International Data Transfer Agreement) already specified in the SUP-003 entry |

**Action:** SUP-003 remains the same open item MC-009 already tracks (ACT-001, "Execute signed DPA with authorised PSP") — this matrix does not create a new action, it cross-references the existing one.

---

## 5. Global financial-regulation research (per the requesting user's ask)

The user asked for research into global financial regulations beyond FCA. Honest scope of what this framework can responsibly assert without real regulatory counsel:

| Jurisdiction / Regime | Relevance | Status |
|---|---|---|
| UK FCA Handbook (PRIN, PRIN 2A, COBS 4) | Primary regime given Trancendos' UK operating base | ✅ Already tracked as LEG-010 in `legislation_register.yaml` and MC-009 |
| EU PSD2 (Payment Services Directive 2) | Would apply if Trancendos ever directly processes/holds payments across the EU | 📋 Not assessed — no current EU payment-processing activity identified beyond Stripe's own PSD2-authorised infrastructure |
| US state money-transmitter licensing | Would apply only if Trancendos directly moves US customer funds | 📋 Not assessed — no evidence of direct US fund movement found; Stripe again sits as the authorised intermediary |
| Global AML/KYC (FATF-aligned regimes) | Relevant if any Location ever handles customer identity verification for financial services | 📋 Not assessed — no AML/KYC code path found in this scan |

**This is deliberately not a comprehensive global financial-regulation survey** — that requires real regulatory/legal expertise per jurisdiction Trancendos actually operates in, not something this framework can respons­ibly assert. This section names the categories worth researching further with real professional input, rather than fabricating jurisdiction-specific compliance claims.

---

## 6. Tax-adjacent note

Corporate/VAT taxation is tracked separately in the [Taxation Matrix](TAXATION-MATRIX.md) (MC-020) — not duplicated here.

---

## 7. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| SUP-003 PSP DPA signature | Immediate (existing ACT-001) | Legal / Procurement, per `compliance/compliance_action_tracker.yaml` |
| FCA authorisation-status re-check | Annual, or on any change to payment-handling architecture | Manual — `docs/compliance/FCA-ALIGNMENT.md` owner |
| Global financial-regulation deep-dive | On real expansion into a new jurisdiction's payment processing | 🎯 Requires engaging real regulatory counsel at that time |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 8. Cross-references

- [REGULATION-MATRIX.md](REGULATION-MATRIX.md) §5 (Legal & financial) — estate-wide regulatory catalogue
- `docs/compliance/FCA-ALIGNMENT.md` — the underlying FCA analysis this matrix builds on
- [TAXATION-MATRIX.md](TAXATION-MATRIX.md) — tax-specific compliance (MC-020)
- [REVENUE-MATRIX.md](REVENUE-MATRIX.md) — monetisation strategy (MC-019)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-017 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
