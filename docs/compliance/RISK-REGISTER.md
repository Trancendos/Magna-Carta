# Risk Register

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Machine-readable:** [compliance/risk_register.yaml](../../compliance/risk_register.yaml)  
**Review:** Quarterly (PROC-CMP-001) · Annual management review

---

## 1. Scoring

| Factor | Scale |
|--------|-------|
| Likelihood | 1 (rare) – 5 (almost certain) |
| Impact | 1 (negligible) – 5 (critical) |
| Inherent score | Likelihood × Impact (1–25) |

**Residual risk** is assessed after controls; external validation items remain 🎯 until evidence exists.

---

## 2. Active risks

| ID | Risk | L | I | Score | Treatment | Controls (✅ programme) | Residual / 🎯 |
|----|------|---|---|-------|-----------|-------------------------|---------------|
| RISK-001 | Architecture doc inconsistency confuses auditors | 3 | 3 | 9 | Mitigate | AS-BUILT-ARCHITECTURE.md canonical; FRAMEWORK precedence | Low after auditor briefing |
| RISK-002 | HIPAA marketing over-claim | 3 | 4 | 12 | Mitigate | HIPAA-ALIGNMENT §10 tiers; TRANC3 copy spec | 🎯 Tier A PR merge |
| RISK-003 | Unsigned supplier DPAs | 4 | 4 | 16 | Mitigate | Supplier register; POL-SUP-001; templates | 🎯 ACT-001, ACT-002 |
| RISK-004 | BCP not exercised at scale | 3 | 4 | 12 | Mitigate | PROC-BCP-001; BCP-RT-001 baseline | 🎯 ACT-012 annual drills |
| RISK-005 | AI fairness unmeasured | 3 | 3 | 9 | Mitigate | PROC-AI-002; POL-AI-001 | 🎯 ACT-004 first run |
| RISK-006 | Magna Carta runtime not enforced | 3 | 3 | 9 | Mitigate | magna_carta_config.json; MC-004 | 🎯 ACT-009 Tranc3 hook |
| RISK-007 | Policy attestation gaps | 3 | 3 | 9 | Mitigate | PROC-TRN-001; attestation register | 🎯 ACT-007 cycle |
| RISK-008 | Certification delay affects sales | 3 | 3 | 9 | Mitigate | ISO/SOC2 programmes; evidence schedules | 🎯 Q1–Q2 2027 audits |

---

## 3. Risk treatment summary

| Treatment | Count |
|-----------|-------|
| Mitigate | 8 |
| Accept | 0 |
| Transfer | 0 |
| Avoid | 0 |

---

## 4. Escalation

| Score | Action |
|-------|--------|
| ≥ 16 | Executive visibility; action tracker P0 |
| 9–15 | ISMS Lead ownership; quarterly review |
| ≤ 8 | Monitor |

---

## 5. Related documents

- [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md)
- [00-EXECUTIVE-SUMMARY.md](../00-EXECUTIVE-SUMMARY.md) — top risks
- [../governance/MANAGEMENT-REVIEW-TEMPLATE.md](../governance/MANAGEMENT-REVIEW-TEMPLATE.md)
- [ISO27001-ALIGNMENT.md](ISO27001-ALIGNMENT.md) — A.5.7

**Next review:** 2026-09-06
