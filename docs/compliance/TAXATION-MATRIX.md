# Taxation Matrix

**Version:** 1.1.0
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Finance / ISMS Lead
**Scope:** Every Service, Solution, Application in the Trancendos estate with a tax obligation
**Register:** MC-020
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`taxation` section)

**2026-07-25 re-audit:** §3's two ❌ findings are now stale in the other direction — both were already fixed by Tranc3 commit `74f68cef` ("Fix stale VAT constants in TaxMonitor (UK threshold, FI/RO/SK rates)"), which appears to predate this matrix's own 2026-07-24 authoring date but wasn't reflected in it. `UK_VAT_THRESHOLD_GBP` is now `90_000`; `EU_VAT_RATES["FI"]` is now `0.255` (with an inline comment citing the 2024-09-01 effective date); Romania and Slovakia were also corrected (`RO: 0.21`, `SK: 0.23`, each with an effective-date comment) and the table has grown from 15 to 27 EU countries. See §3 for the corrected findings.

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
| UK VAT rate/threshold logic | ✅ | **FIXED** (Tranc3 `74f68cef`) — `UK_VAT_THRESHOLD_GBP` is now `90_000`, matching HMRC's threshold under The Value Added Tax (Increase of Registration Limits) Order 2024 (effective 1 April 2024). The 20% rate was already current |
| EU VAT-OSS per-country rate table | ⚠️ | **Partially fixed** (Tranc3 `74f68cef`) — Finland (`0.255`, effective 2024-09-01), Romania (`0.21`, effective 2025-08-01), and Slovakia (`0.23`, effective 2025-01-01) are now corrected, each with an inline effective-date comment; the table has also grown from 15 to 27 EU countries (adding BG, HR, LT, LV, EE, SI, GR, LU, MT, CY). The remaining ~24 rates were not individually re-verified against a live current source in this pass — same caveat as the original finding, just narrower in scope now that the 3 known-stale ones are resolved |
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
| Re-verify the remaining ~24 `EU_VAT_RATES` entries against a live current source (UK threshold + FI/RO/SK already fixed in Tranc3 `74f68cef`) | Next scheduled scan | Real engineering task in `src/monetisation/billing.py` (Tranc3) |
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
