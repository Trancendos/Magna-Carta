# AI Governance Committee Charter

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Effective:** 2026-06-07  
**Owner:** AI Lead  
**Approver:** BoardRoom (Town Hall)  
**Review cycle:** Annual

---

## 1. Purpose

Establishes a cross-functional **AI Governance Committee** to oversee Tranc3 AI systems in line with EU AI Act, ISO 42001, POL-AI-001, and [AI-GOVERNANCE.md](../compliance/AI-GOVERNANCE.md).

Addresses GenAI maturity Domain 1 gap: formal governance committee charter.

---

## 2. Authority

The Committee advises BoardRoom on:

- AI risk classification and model registry changes
- High-risk AI feature approvals
- Fairness/bias testing results (PROC-AI-002)
- AI incidents and remediations
- External framework maturity (GENAI-MATURITY-ASSESSMENT)

The Committee does **not** replace CAB for production deployments or Legal for regulatory interpretation.

---

## 3. Membership

| Role | Representative | Responsibility |
|------|----------------|----------------|
| Chair | AI Lead | Agenda, registry, risk tiers |
| Deputy | ISMS Lead | Security and compliance alignment |
| Privacy | DPO | DPIA, Art. 22, special category data |
| Security | Security Ops | Adversarial testing, Ice Box |
| Engineering | Platform Engineering delegate | Implementation feasibility |
| Product | Product delegate | User-facing AI transparency |
| Legal | Legal (as needed) | Regulatory interpretation |
| Executive sponsor | BoardRoom nominee | Escalation, resource allocation |

**Quorum:** Chair + DPO + one of (Security Ops, ISMS Lead).

---

## 4. Meetings

| Type | Frequency | Output |
|------|-----------|--------|
| Standing review | Quarterly | Minutes, action log |
| Ad hoc | On high-risk model or P1 AI incident | Decision record |
| Annual | AI programme review | GENAI maturity update |

Minutes stored in Town Hall MeetingRooms with retention per PROC-CMP-001.

---

## 5. Standing agenda

1. Model registry changes since last meeting
2. Open AI incidents and CAPA status
3. Fairness/bias test results (PROC-AI-002)
4. Regulatory change (EU AI Act, UK DSIT)
5. Marketing and transparency claims (model cards, HIPAA/FCA tiers)
6. Resource and certification roadmap items

---

## 6. Decision rights

| Decision | Committee | BoardRoom | CAB |
|----------|-----------|-----------|-----|
| New model registration (limited risk) | Recommend | Inform | — |
| High-risk AI feature | Recommend approve | Approve if material | Deploy gate |
| Prohibited use exception | **Deny** (no exceptions) | — | — |
| Bias test failure remediation | Assign owner | Escalate if unresolved >90d | — |

---

## 7. Deliverables

| Deliverable | Frequency |
|-------------|-----------|
| Committee minutes | Each meeting |
| Model risk summary | Quarterly |
| Input to GENAI-MATURITY-ASSESSMENT | Annual |
| POL-AI-001 review recommendation | Semi-annual |

---

## 8. Related documents

- [POL-AI-001](../policies/POL-AI-001-AI-Ethics-Governance.md)
- [AI-GOVERNANCE.md](../compliance/AI-GOVERNANCE.md)
- [GENAI-MATURITY-ASSESSMENT.md](../compliance/GENAI-MATURITY-ASSESSMENT.md)
- [PROC-AI-002](../procedures/PROC-AI-002-Fairness-Bias-Testing.md)
- [RACI-MATRIX.md](RACI-MATRIX.md)

**Next charter review:** 2027-06-07
