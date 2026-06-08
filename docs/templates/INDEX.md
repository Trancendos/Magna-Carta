# Contract Template Library — Index

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Legal / DPO  
**Review cycle:** Annual (or on regulatory change)

---

## Purpose

Standardised contract templates for supplier onboarding and customer health integrations. Used with [SUPPLIER-DPA-REGISTER.md](../compliance/SUPPLIER-DPA-REGISTER.md) and open actions ACT-001, ACT-002, ACT-010.

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Template exists and is maintained |
| 🎯 **External validation** | Countersigned agreement on file pending |

---

## Templates

| ID | Template | Use case | Linked supplier / obligation |
|----|----------|----------|------------------------------|
| TPL-DPA-001 | [TEMPLATE-DPA-UK-GDPR.md](TEMPLATE-DPA-UK-GDPR.md) | UK GDPR Article 28 processor DPA | SUP-001–003, OBL-003 |
| TPL-BAA-001 | [TEMPLATE-BAA-HIPAA.md](TEMPLATE-BAA-HIPAA.md) | HIPAA business associate agreement | SUP-005, MC-008, OBL-090 |
| TPL-SCC-001 | [TEMPLATE-SCC-ANNEX.md](TEMPLATE-SCC-ANNEX.md) | EU/UK standard contractual clauses annex | SUP-004, OBL-020 |
| TPL-TIA-001 | [TEMPLATE-TIA-US-AI-FALLBACK.md](TEMPLATE-TIA-US-AI-FALLBACK.md) | Transfer impact assessment (US AI fallback) | SUP-004, ACT-010 |
| TPL-FTR-001 | [TEMPLATE-FAIRNESS-TEST-REPORT.md](TEMPLATE-FAIRNESS-TEST-REPORT.md) | PROC-AI-002 fairness/bias test record | ACT-004, RISK-005 |
| TPL-IAR-001 | [TEMPLATE-INTERNAL-AUDIT-REPORT.md](TEMPLATE-INTERNAL-AUDIT-REPORT.md) | ISO 27001 §9.2 internal audit report | ACT-011, MC-010 |

---

## Usage workflow

1. **Select** — Match template to supplier row in [supplier_dpa_register.yaml](../../compliance/supplier_dpa_register.yaml)
2. **Customise** — Legal reviews annexes, sub-processor schedules, and data categories
3. **Execute** — Countersign; store in secure contract repository
4. **Register** — Update SUP-### `dpa_status` → Signed; link evidence in action tracker

---

## Related documents

- [SUPPLIER-DPA-REGISTER.md](../compliance/SUPPLIER-DPA-REGISTER.md)
- [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md)
- [HIPAA-ALIGNMENT.md](../compliance/HIPAA-ALIGNMENT.md) §4
- [GDPR-ALIGNMENT.md](../compliance/GDPR-ALIGNMENT.md)

**Next review:** 2027-06-07
