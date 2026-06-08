# POL-SUP-001 — Supplier Management Policy

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** Procurement / ISMS · **Review:** Annual

---

## 1. Purpose

Manage third-party risk for suppliers processing Trancendos or customer data.

## 2. Scope

All vendors with access to data, infrastructure, or integration with Tranc3.

## 3. Assessment

Before onboarding:
- Security questionnaire or SOC 2 / ISO 27001 evidence
- DPA (Art. 28) for processors handling personal data
- SCCs or UK IDTA for international transfers
- Zero-cost check: paid mandatory APIs require Town Hall exception

## 4. Ongoing management

- Annual review of critical suppliers
- Incident notification clauses in contracts
- Right to audit where feasible
- Offboarding: data return/deletion confirmed

## 5. Prohibited

- Suppliers without documented security posture for production data paths
- Sub-processors not disclosed to customers (where required)

## 6. Register

Maintain the canonical supplier and DPA register in:

- [compliance/supplier_dpa_register.yaml](../../compliance/supplier_dpa_register.yaml) (machine-readable)
- [SUPPLIER-DPA-REGISTER.md](../compliance/SUPPLIER-DPA-REGISTER.md) (auditor-facing)

Each record includes risk tier, DPA status, sub-processor disclosure, and annual review date. Town Hall may mirror summary fields for operations.

**External validation:** Individual signed DPAs (SUP-003–005 templates) remain 🎯 until countersigned.

## 7. Related documents

POL-SEC-001, POL-PRI-001, GDPR-ALIGNMENT.md, SUPPLIER-DPA-REGISTER.md
