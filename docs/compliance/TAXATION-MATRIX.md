# Taxation Matrix

**Version:** 1.0.0
**Date:** 2026-07-24
**Owner:** Finance / ISMS Lead
**Scope:** Every Service, Solution, Application in the Trancendos estate with a tax obligation
**Register:** MC-020
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`taxation` section)

---

## 1. Purpose

Tracks whether the platform's tax and cost frameworks are followed — real code capability vs. actual filed/registered tax status. This is the matrix where the gap between "code exists" and "compliance achieved" is widest and most important to keep separate: `src/monetisation/billing.py`'s `TaxMonitor` class is genuinely well-built, but **code logic is not proof of an actual VAT registration, filed CT600, or claimed R&D credit.**

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim tax compliance in product copy unless the corresponding row is ✅ with evidence. This matrix cannot substitute for a real accountant or tax advisor — nearly every row below is 🎯 for that exact reason.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — real, evidenced (e.g. code logic confirmed present and correct) |
| ⚠️ | Real mechanism exists, with a documented gap between capability and actual filed status |
| 📋 | Not yet assessed |
| ❌ | Confirmed gap |
| 🎯 | Requires a real accountant/tax advisor — this framework cannot self-certify |

---

## 3. VAT (Value Added Tax) — code capability vs. actual registration

`TaxMonitor` (`src/monetisation/billing.py`) is genuinely implemented, not a stub:

| Item | Status | Finding |
|---|---|---|
| UK VAT rate/threshold logic | ❌ | The 20% rate is current, but `UK_VAT_THRESHOLD_GBP = 85_000` is **stale** — HMRC raised the UK VAT registration threshold to £90,000 effective 1 April 2024 (The Value Added Tax (Increase of Registration Limits) Order 2024). The code has not been updated to reflect this and will under-flag registration obligations for businesses between £85,000–£90,000 turnover |
| EU VAT-OSS per-country rate table | ❌ | Most rates verified current, but `"FI": 0.24` is **stale** — Finland raised its standard VAT rate to 25.5% effective 1 September 2024. Other rates in the table (DE 19%, FR 20%, IT 22%, ES 21%, NL 21%, BE 21%, AT 20%, PL 23%, SE 25%, DK 25%, IE 23%, PT 23%, RO 19%, HU 27%, CZ 21%) were not individually re-verified in this pass — the Finland finding alone is enough to warrant a full re-audit of this table against current national rates before trusting it |
| EU VAT number validation | ✅ | Real VIES SOAP API integration (`validate_eu_vat_number`) — a genuine external call, not a mock |
| Stripe Tax integration | ✅ | Enabled in checkout per the module's own comments; handles collection automatically once real Stripe price IDs are configured |
| **Actual UK VAT registration** | 🎯 | Not found anywhere in either repo — no VAT registration number recorded. Do not assume registration has occurred just because the threshold-tracking code exists |
| **Actual EU VAT-OSS registration** | 🎯 | Same caveat — no registration evidence found |

---

## 4. Corporation tax and reliefs — descriptive only, not evidence of a claim

`TaxMonitor.tax_benefit_summary()` genuinely describes several real UK tax schemes: HMRC R&D Tax Credit, Annual Investment Allowance (100% first-year deduction on qualifying capital expenditure), Patent Box, trading allowance, VAT flat-rate scheme, SEIS/EIS.

| Scheme | Status | Finding |
|---|---|---|
| HMRC R&D Tax Credit | 🎯 | Described generically in code; **no evidence of an actual claim filed**. Do not represent this as a realized tax benefit |
| Annual Investment Allowance | 🎯 | Same caveat — generic description, no evidence of actual capital-expenditure claim |
| Patent Box | 🎯 | Same caveat — and contingent on having a registered patent, which is a separate open item under the Intellectual Property Matrix |
| SEIS/EIS | 🎯 | Same caveat — investor tax relief schemes require a real cap table and HMRC advance assurance, neither evidenced here |
| Corporation Tax registration (UTR) | 🎯 | No Unique Taxpayer Reference found anywhere in either repo |

**This section exists specifically to prevent a documentation-to-reality gap**: the code's generic descriptions of these schemes must never be read as evidence Trancendos has actually claimed them.

---

## 5. What's genuinely absent (confirmed, not assumed)

Per direct search of both repos:

- `compliance/frameworks_register.yaml` (Magna-Carta): **zero** tax-related entries.
- `compliance/legislation_register.yaml` (Magna-Carta): **zero** VAT Act / Corporation Tax Act entries — the only tax-adjacent legislative entry is the Companies Act 2006 (LEG-008), tagged to Finance/OBL-063, which is a company-law statute, not a tax statute.
- The only real tax-*adjacent* item tracked anywhere in Magna-Carta is **payroll** (HMRC RTI/PAYE, ACT-018 in `compliance/compliance_action_tracker.yaml`, referenced in `docs/bibles/FINANCE-BIBLE.md`) — employer payroll reporting, not corporate/VAT tax.

This confirms the taxation domain is a genuine, currently-unaddressed compliance gap at the real-world registration/filing level, despite good underlying code.

---

## 6. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Update `UK_VAT_THRESHOLD_GBP` to £90,000 and re-verify the full `EU_VAT_RATES` table (starting with Finland's 25.5%) | Immediate | Real engineering fix in `src/monetisation/billing.py` (Tranc3) — this matrix caught genuinely stale constants, not a hypothetical risk |
| VAT registration status confirmation | Immediate | 🎯 Requires a real accountant — confirm whether UK VAT registration has actually occurred given current/projected turnover vs. the (corrected) £90,000 threshold |
| Corporation tax / UTR confirmation | Immediate | 🎯 Requires real corporate tax records |
| R&D credit / AIA / Patent Box claim assessment | On next accounting period close | 🎯 Requires a real accountant — do not self-assess |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 7. Cross-references

- [REVENUE-MATRIX.md](REVENUE-MATRIX.md) — the revenue this matrix's tax obligations apply to (MC-019)
- [FINANCIAL-MATRIX.md](FINANCIAL-MATRIX.md) — FCA/regulatory posture (MC-017)
- `docs/bibles/FINANCE-BIBLE.md` — payroll/PAYE tracking (ACT-018)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-020 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
