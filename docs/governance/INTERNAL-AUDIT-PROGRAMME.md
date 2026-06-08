# Internal Audit Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Standard:** ISO 27001:2022 Clause 9.2  
**Register:** MC-010

---

## 1. Purpose

Plans independent internal audits of the ISMS and Magna Carta control environment. Supports ISO 27001 certification readiness and SOC 2 control operating effectiveness.

| Symbol | Meaning |
|--------|---------|
| ✅ | Programme documented |
| 🎯 | Audit execution and CAPA closure pending |

---

## 2. Audit universe

| Domain | Scope | Frequency | Lead auditor |
|--------|-------|-----------|--------------|
| Access management | IAM, MFA, privileged reviews | Annual | ISMS Lead (or external) |
| Change & release | CAB, CI gates, PROC-CHG-* | Annual | CAB rep (independent) |
| Incident & IR | PROC-IR-001, breach handling | Annual | Security Ops peer |
| Privacy & DSR | GDPR, ROPA, DSR log | Annual | DPO delegate |
| Supplier & DPA | Register, onboarding | Annual | DPO / Procurement |
| BCP & backup | Restore tests, DR | Annual | Operations peer |
| AI governance | POL-AI-001, PROC-AI-002 | Annual | AI Lead peer |
| Magna Carta programme | Policies, registers, evidence | Annual | ISMS Lead |

---

## 3. 2026–2027 schedule

| Audit ID | Domain | Planned window | Status |
|----------|--------|----------------|--------|
| IA-2026-01 | Magna Carta programme (baseline) | 2026-Q4 | 🎯 Scheduled — ACT-011 |
| IA-2027-01 | Access management | 2027-Q1 | 🎯 Planned |
| IA-2027-02 | Change & release | 2027-Q2 | 🎯 Planned |

---

## 4. Audit process

1. **Plan** — Scope, criteria (ISO 27001 Annex A + Magna Carta MC-001–010), sample size.
2. **Execute** — Interviews, config review, evidence sampling per [SOC2-EVIDENCE-SCHEDULE.md](../compliance/SOC2-EVIDENCE-SCHEDULE.md).
3. **Report** — Findings classified: Major · Minor · Observation · Opportunity.
4. **CAPA** — Corrective actions in [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md); verify within 90 days.
5. **Follow-up** — Management review input.

---

## 5. Auditor independence

Internal auditors must not audit their own direct responsibilities. For early-stage programmes, contracted ISO lead auditor may perform first internal audit (🎯 budget item).

---

## 6. Related documents

- [MANAGEMENT-REVIEW-TEMPLATE.md](MANAGEMENT-REVIEW-TEMPLATE.md)
- [RACI-MATRIX.md](RACI-MATRIX.md)
- [../compliance/ISO27001-ALIGNMENT.md](../compliance/ISO27001-ALIGNMENT.md)
- [../procedures/PROC-CMP-001-Compliance-Review.md](../procedures/PROC-CMP-001-Compliance-Review.md)
