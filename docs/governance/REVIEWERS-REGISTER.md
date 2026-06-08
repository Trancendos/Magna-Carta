# Reviewers Register

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Source:** Extends [RACI-MATRIX.md](RACI-MATRIX.md) with named review types, cadence, and outputs  
**Review cycle:** Annual (roles) · Quarterly (cadence adherence via PROC-CMP-001)

---

## 1. Review types

| REV-ID | Review | Frequency | Chair / lead | Participants | Output artefact |
|--------|--------|-----------|--------------|--------------|-----------------|
| REV-001 | Compliance review | Quarterly | ISMS Lead | DPO, Eng lead, SecOps, AI Lead, CAB rep | PROC-CMP-001 minutes, action tracker |
| REV-002 | Legislation / obligations scan | Quarterly | DPO | Legal, AI Lead | LEGISLATION-REGISTER, OBLIGATIONS-REGISTER |
| REV-003 | Risk register review | Quarterly | ISMS Lead | Engineering, DPO | RISK-REGISTER, RISK-TREATMENT-PLAN |
| REV-004 | Internal audit | Annual (min) | ISMS Lead / external | Per audit plan | INTERNAL-AUDIT-PROGRAMME findings |
| REV-005 | Management review (ISO 9.3) | Annual | Executive | ISMS, DPO, Eng, Finance | MANAGEMENT-REVIEW-TEMPLATE |
| REV-006 | AI Governance Committee | Quarterly | AI Lead | DPO, Legal, Engineering | AI-GOVERNANCE-COMMITTEE-CHARTER minutes |
| REV-007 | CAB (change advisory) | Per change | CAB chair | Engineering, Security | PROC-CHG-001 records |
| REV-008 | Post-implementation review | Per major change | CAB | Engineering, ISMS | PROC-CHG-002 |
| REV-009 | Supplier / DPA review | Annual | DPO | Legal, Procurement | SUPPLIER-DPA-REGISTER |
| REV-010 | Access review | Quarterly | ISMS Lead | Engineering managers | PROC-IAM-001 evidence |
| REV-011 | Policy attestation | Annual | HR / ISMS | All staff | POLICY-ATTESTATION-REGISTER |
| REV-012 | BCP restore test | Semi-annual | Operations | Engineering | BCP-RESTORE-TEST-LOG |
| REV-013 | Pen test remediation | Per test | Security Ops | Engineering | PEN-TEST-LOG |
| REV-014 | Fairness / bias test | Annual | AI Lead | DPO | PROC-AI-002 report |
| REV-015 | Standards register | Quarterly | ISMS Lead | — | STANDARDS-REGISTER |
| REV-016 | Documentation artifact gap scan | Quarterly | ISMS Lead | — | DOCUMENTATION-ARTIFACT-MODEL §7 |
| REV-017 | Maintenance monitor (automated) | Weekly (CI) / on demand | ISMS Lead | — | `compliance_health_check.py` report |

---

## 2. Role-to-review matrix

| Role | Primary reviews (A/R) |
|------|------------------------|
| ISMS Lead | REV-001, 003, 004, 005, 010, 015, 016, 017 |
| DPO | REV-002, 009, breach notification |
| AI Lead | REV-006, 014, EU AI Act monitoring |
| Platform Engineering | REV-007, 008, control implementation |
| Security Ops | REV-013, vulnerability programme |
| Legal | REV-002 (consulted), DPA execution |
| CAB | REV-007, 008 |
| Executive | REV-005, BCP declaration |

Full RACI: [RACI-MATRIX.md](RACI-MATRIX.md)

---

## 3. Escalation

| Condition | Escalate to | Within |
|-----------|-------------|--------|
| Review missed (no minutes/output) | ISMS Lead → Executive | 5 business days |
| P0 action past due | Executive | Immediate |
| Regulator inquiry | Legal + Executive | 24 hours |
| Failed maintenance health check in CI | Platform Engineering + ISMS | Next stand-up |

---

## 4. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-07 | Initial reviewers register | ISMS Lead |

**Next review:** 2027-06-07 (roles) · 2026-09-06 (cadence check)
