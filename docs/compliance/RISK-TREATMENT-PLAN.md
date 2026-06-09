# Information Security Risk Treatment Plan

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Source register:** [compliance/risk_register.yaml](../../compliance/risk_register.yaml)  
**Status:** ✅ Programme — operational treatment evidence via ACT items

---

## 1. Purpose

Formalises ISO 27001 risk treatment for risks in the Magna Carta risk register. **Risk identification** remains in Tranc3 + `risk_register.yaml`; this plan records **treatment decisions and owners**.

---

## 2. Treatment summary

| Risk ID | Title | Treatment | Control / action | Owner | Target |
|---------|-------|-----------|------------------|-------|--------|
| RISK-001 | Architecture doc inconsistency | Mitigate | AS-BUILT-ARCHITECTURE, CONTROL-TO-COMPONENT-MAP | Platform Eng | ✅ Programme |
| RISK-002 | HIPAA marketing over-claim | Mitigate | TRANC3-HIPAA-COPY-REMEDIATION | Platform Eng | ACT-006 🎯 |
| RISK-003 | Unsigned supplier DPAs | Mitigate | SUPPLIER-DPA-REGISTER, templates | Legal | ACT-001, ACT-010 🎯 |
| RISK-004 | BCP not exercised at scale | Mitigate | PROC-BCP-001, BCP log | Operations | ACT-012 🎯 |
| RISK-005 | AI fairness not measured | Mitigate | PROC-AI-002 | AI Lead | ACT-004 🎯 |
| RISK-006 | Magna Carta not enforced in prod | Mitigate | TRANC3-INTEGRATION-GUIDE, MC-011 | Platform Eng | ACT-009 🎯 |
| RISK-007 | Policy attestation gaps | Mitigate | PROC-TRN-001, attestation register | HR / ISMS | ACT-007 🎯 |
| RISK-008 | Certification delay affects sales | Mitigate | SOC2/ISO programmes | ISMS Lead | ACT-008, Q2 2027 🎯 |
| RISK-009 | AI inference integrity/confidentiality failure | Mitigate | PROC-AI-003, AI-SECURITY-THREAT-MODEL, MC-RULE-004 | AI Lead / Security Ops | ACT-013 🎯 |
| RISK-010 | AI training data poisoning or leakage | Mitigate | PROC-AI-003; data provenance controls | AI Lead | ACT-013 🎯 |
| RISK-011 | AI model IP or supply-chain compromise | Mitigate | PROC-AI-003; supplier register; rate limits | AI Lead / Security Ops | ACT-013 🎯 |
| RISK-012 | AI availability abuse | Mitigate | Rate limits; cost caps; MC-RULE-005 | Platform Eng | ACT-013 🎯 |

---

## 3. Residual risk acceptance

Risks accepted without further treatment require ISMS Lead + executive sign-off recorded in management review minutes.

---

## 4. Review

| Activity | Frequency |
|----------|-----------|
| Re-score risks | Quarterly |
| Update this plan | Quarterly (PROC-CMP-001) |
| Link new findings from audit | Per ACT-011 |

---

## 5. Related documents

- [RISK-REGISTER.md](RISK-REGISTER.md)
- [ISO27001-ALIGNMENT.md](ISO27001-ALIGNMENT.md)
- [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md)
