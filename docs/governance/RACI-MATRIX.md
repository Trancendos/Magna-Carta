# RACI Matrix — Magna Carta Operating Model

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Source:** Expands FRAMEWORK.md §9

**Legend:** R = Responsible · A = Accountable · C = Consulted · I = Informed

---

## 1. Governance and policy

| Activity | ISMS Lead | Engineering | DPO | Legal | CAB | AI Lead | Security Ops | Finance | Executive |
|----------|-----------|-------------|-----|-------|-----|---------|--------------|---------|-----------|
| Policy draft & maintenance | A/R | C | C | C | I | C | C | I | I |
| Policy approval (security/privacy) | A | C | R | C | I | I | C | I | I |
| Policy approval (AI) | C | C | C | C | I | R | C | I | A |
| Annual policy attestation | R | C | C | I | I | C | C | I | A |
| Legislation register scan | C | I | R | A | I | C | I | I | I |
| Obligations register review | A/R | C | R | C | I | C | C | I | I |

---

## 2. Security and operations

| Activity | ISMS Lead | Engineering | DPO | Legal | CAB | AI Lead | Security Ops | Finance | Executive |
|----------|-----------|-------------|-----|-------|-----|---------|--------------|---------|-----------|
| Control implementation | C | A/R | I | I | I | C | C | I | I |
| DEFSTAN / register.yaml | C | A/R | I | I | I | I | C | I | I |
| Vulnerability management | C | R | I | I | I | I | A/R | I | I |
| Incident command (P1) | C | R | C | C | I | I | A/R | I | A |
| Breach notification (ICO/regulator) | C | C | A/R | R | I | I | C | I | I |
| Access provisioning (PROC-IAM-001) | A | R | C | I | I | I | C | I | I |
| Backup execution | I | R | I | I | I | I | I | I | I |
| Restore test (PROC-BCP-001) | C | R | I | I | I | I | I | I | I |

---

## 3. Change and continuity

| Activity | ISMS Lead | Engineering | DPO | Legal | CAB | AI Lead | Security Ops | Finance | Executive |
|----------|-----------|-------------|-----|-------|-----|---------|--------------|---------|-----------|
| Production change (PROC-CHG-001) | C | R | I | I | A | C | C | I | I |
| Post-implementation review | C | R | I | I | A | C | C | I | I |
| BCP / DR declaration | C | R | I | I | I | I | C | I | A |
| Supplier onboarding | C | C | R | A | I | I | C | C | I |

---

## 4. Privacy and data protection

| Activity | ISMS Lead | Engineering | DPO | Legal | CAB | AI Lead | Security Ops | Finance | Executive |
|----------|-----------|-------------|-----|-------|-----|---------|--------------|---------|-----------|
| ROPA maintenance | C | C | A/R | C | I | C | I | I | I |
| DSR handling (PROC-DSR-001) | I | C | A/R | C | I | I | I | I | I |
| DPIA (high-risk processing) | C | C | A/R | C | I | C | C | I | I |
| DPA / BAA execution | I | I | R | A | I | I | I | I | I |
| ICO registration | I | I | R | C | I | I | I | A | I |
| PECR / marketing consent | I | C | A/R | C | I | I | I | I | I |

---

## 5. AI governance

| Activity | ISMS Lead | Engineering | DPO | Legal | CAB | AI Lead | Security Ops | Finance | Executive |
|----------|-----------|-------------|-----|-------|-----|---------|--------------|---------|-----------|
| Model registry | C | R | C | I | I | A | C | I | I |
| Risk classification | C | C | C | C | I | A/R | C | I | I |
| Model cards publication | C | R | C | I | I | A | I | I | I |
| Fairness/bias testing | C | C | C | I | I | A/R | C | I | I |
| AI incident response | C | R | C | C | I | A | R | I | I |
| AI Governance Committee | C | C | R | C | I | A/R | C | I | C |

---

## 6. Compliance assurance

| Activity | ISMS Lead | Engineering | DPO | Legal | CAB | AI Lead | Security Ops | Finance | Executive |
|----------|-----------|-------------|-----|-------|-----|---------|--------------|---------|-----------|
| Compliance evidence pack | A/R | C | C | I | I | C | C | I | I |
| Quarterly PROC-CMP-001 | A/R | C | C | C | C | C | C | C | I |
| Internal audit coordination | A/R | C | C | C | I | C | C | I | I |
| External certification (ISO/SOC2) | A/R | C | C | C | I | C | C | C | A |
| Customer audit / questionnaire | R | C | R | C | I | C | C | I | I |

---

## 7. Corporate governance

| Activity | ISMS Lead | Engineering | DPO | Legal | CAB | AI Lead | Security Ops | Finance | Executive |
|----------|-----------|-------------|-----|-------|-----|---------|--------------|---------|-----------|
| Companies Act director duties | I | I | I | C | I | I | I | R | A |
| Companies House filings | I | I | I | C | I | I | I | A/R | A |
| FCA financial promotions | I | I | C | A/R | I | C | I | C | I |

---

## 8. Related documents

- [FRAMEWORK.md](../../FRAMEWORK.md) §9
- [COMPLIANCE-BLUEPRINT.md](../compliance/COMPLIANCE-BLUEPRINT.md)
- [AI-GOVERNANCE-COMMITTEE-CHARTER.md](AI-GOVERNANCE-COMMITTEE-CHARTER.md)

**Next review:** 2026-09-06
