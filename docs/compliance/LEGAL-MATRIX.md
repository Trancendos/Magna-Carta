# Legal Matrix

**Version:** 1.0.1
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Legal / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate
**Register:** MC-016
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`legal` section)

**2026-07-25 re-audit:** every code-grounded claim in this matrix was re-verified against current source — `docs/governance/ACCEPTABLE-USE-POLICY.md` and `CURRENT_TERMS_VERSION`/the subscribe-history API in `src/access/registry.py` still exist as described in §3; a repo-wide search still finds no standalone Terms of Service, Privacy Policy, Cookie Policy, or EULA document in either repo; no Companies House registration number or registered address has been added anywhere in either repo since the original scan; `compliance/legislation_register.yaml` still tracks exactly 10 active items (LEG-001–010) plus 6 watch-list items (WATCH-001–006). No drift found — this matrix's findings hold unchanged.

## 1. Purpose

Tracks, per Service/Solution/Application/AI, whether the correct legal instruments (terms, policies, tracked legislation) actually exist and are enforced — distinct from [LEGAL-BIBLE.md](../bibles/LEGAL-BIBLE.md), which documents the *process* (contract management procedure) rather than per-entity coverage, and from [REGULATION-MATRIX.md](REGULATION-MATRIX.md), which is the estate-wide regulatory catalogue.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim legal compliance in product copy unless the corresponding row is ✅ with evidence. This matrix cannot substitute for real legal counsel — several rows below are explicitly 🎯/📋 because that requires it.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — real instrument exists and is enforced in code or process |
| ⚠️ | Exists, with a documented caveat |
| 📋 | Not yet assessed |
| ❌ | Confirmed gap |
| 🎯 | Requires real legal counsel — this framework cannot self-certify |

---

## 3. Customer/user-facing legal instruments

| Instrument | Status | Evidence |
|---|---|---|
| Platform Acceptable Use Policy | ✅ | `docs/governance/ACCEPTABLE-USE-POLICY.md` (Tranc3, v1.0) — genuinely code-enforced via `CURRENT_TERMS_VERSION` in `src/access/registry.py`, with a real subscribe/version-history API (`/access/{location}/subscribe`, `/access/{location}/history`) and immutable acceptance records |
| Terms of Service (external, customer-facing) | ❌ | No standalone ToS document found in either repo — the AUP above governs platform *conduct*, not a full commercial terms agreement |
| Privacy Policy (external, customer-facing) | ❌ | Only `docs/privacy/PRIVACY_IMPACT_ASSESSMENT.md` exists (Tranc3) — an internal DPIA, not a published customer-facing privacy notice |
| Cookie Policy | ❌ | Not found in either repo |
| EULA | ❌ | Not found in either repo |
| Internal employee Acceptable Use Policy | ✅ | `docs/policies/POL-SEC-002-Acceptable-Use.md` (Magna-Carta) — a distinct, real document from the platform AUP above; internal staff/device conduct only |

**Action:** the absence of an external ToS/Privacy Policy/Cookie Policy is a genuine gap, not previously surfaced this explicitly — flagged for real legal drafting before any customer-facing commercial launch, not something this framework can author on its own authority.

---

## 4. Company/entity legal status

| Question | Status | Finding |
|---|---|---|
| Is there a registered legal entity behind the platform? | ⚠️ | "Trancendos Ltd" appears repeatedly across both repos (`docs/00-EXECUTIVE-SUMMARY.md`, `docs/compliance/ISO27001-ALIGNMENT.md`, `docs/compliance/GDPR-ALIGNMENT.md`) as an asserted trading name |
| Companies House registration number / registered office address? | 🎯 | Not found anywhere in either repo. Treat "Trancendos Ltd" as an asserted trading name only until a real CRN and registered address are confirmed and recorded — this is a real gap, not a documentation oversight this framework can close itself |
| Incorporation date? | 🎯 | Not found — same caveat as above |

---

## 5. Tracked legislation (real register, not fabricated)

`compliance/legislation_register.yaml` genuinely tracks 10 active items plus a 6-item watch list:

| ID | Legislation |
|---|---|
| LEG-001 | UK GDPR |
| LEG-002 | Data Protection Act 2018 |
| LEG-003 | EU GDPR |
| LEG-004 | Computer Misuse Act 1990 |
| LEG-005 | Privacy and Electronic Communications Regulations (PECR) 2003 |
| LEG-006 | EU AI Act (2024/1689) |
| LEG-007 | Copyright, Designs and Patents Act 1988 |
| LEG-008 | Companies Act 2006 |
| LEG-009 | HIPAA |
| LEG-010 | FCA Handbook |

**Watch list (not yet tracked as active, 6 items):** Online Safety Act 2023, Digital Markets, Competition and Consumers Act 2024, EU Data Act, NIS2, DORA, CCPA/CPRA.

This is a real, substantive legislation register — not something this matrix needs to duplicate or re-derive. Cross-referenced, not repeated in full here.

---

## 6. Per-entity legal exposure (not exhaustive — flagged entities only)

| Entity | Legal question | Status |
|---|---|---|
| Royal Bank of Arcadia / Arcadian Exchange | Financial services regulation | See [Financial Matrix](FINANCIAL-MATRIX.md) (MC-017) — not duplicated here |
| Sashas Photo Studio | Generated-image copyright/training-data provenance | See [INTELLECTUAL-PROPERTY-MATRIX.md](INTELLECTUAL-PROPERTY-MATRIX.md) §4 — not duplicated here |
| Every entity processing personal data | UK/EU GDPR (LEG-001/002/003) | ⚠️ Programme-level coverage is real and verified via `docs/compliance/GDPR-ALIGNMENT.md`; per-entity enforcement has not been individually audited in this pass — do not read the programme-level ✅ as per-entity verification |

All other entities carry no distinct legal exposure beyond the estate-wide baseline (LEG-001–010) — a deliberate scoping choice, matching the pattern used in the Intellectual Property Matrix.

---

## 7. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| External ToS/Privacy Policy/Cookie Policy drafting | Before any commercial customer launch | 🎯 Requires real legal counsel — not self-certifiable |
| Company registration confirmation (CRN, address) | Immediate | 🎯 Requires a real corporate records check |
| Legislation register review | Quarterly | Aligned with `legislation_register.yaml`'s existing cycle |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 8. Cross-references

- [REGULATION-MATRIX.md](REGULATION-MATRIX.md) — estate-wide regulatory catalogue
- [LEGAL-BIBLE.md](../bibles/LEGAL-BIBLE.md) — process-level legal/contract management
- [FINANCIAL-MATRIX.md](FINANCIAL-MATRIX.md) — FCA-specific financial regulation (MC-017)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-016 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
