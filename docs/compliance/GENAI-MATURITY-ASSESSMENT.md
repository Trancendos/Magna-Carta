# GenAI Governance Maturity Assessment

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** AI Lead / ISMS Lead  
**Methodology:** Adapted from Connor Group GenAI Governance Framework Maturity Model v1.0  
**Review cycle:** Annual (full); quarterly (spot-check on critical controls)

---

## 1. Purpose

This assessment helps Trancendos **measure GenAI governance maturity** across five domains aligned with [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md). Use it for:

- BoardRoom and quarterly compliance reviews (PROC-CMP-001)
- Prioritising AI governance investments before ISO 42001 programme
- Benchmarking progress against industry-recognised maturity language

**Maturity levels:**

| Level | Name | Definition |
|-------|------|------------|
| 1 | **Nascent** | Ad hoc or absent; reactive |
| 2 | **Emerging** | Basic structures; partial implementation |
| 3 | **Established** | Structured, largely implemented |
| 4 | **Leading** | Comprehensive, integrated, continuously improved |

---

## 2. How to run the assessment

1. **Assemble panel:** AI Lead (chair), ISMS Lead, DPO, Platform Engineering rep, Security Ops.
2. **Evidence window:** Last 90 days of artefacts (policies, registers, CI, incidents, model cards).
3. **Score each control** (1–4) using rubric in §3–7; record evidence links.
4. **Calculate domain score:** Average of control scores in domain (round to nearest 0.5).
5. **Identify gaps:** Controls scored ≤2 with high business impact → action register.
6. **Report:** Summary to Town Hall MeetingRooms; update AI-GOVERNANCE §9 actions.

**Target for Tranc3 (2026):** Domain average ≥3.0 overall; no critical control below 2.

---

## 3. Domain 1 — Strategic alignment and control environment

| Control | Tranc3 evidence to review | Baseline (2026-06) | Target |
|---------|---------------------------|-------------------|--------|
| GenAI risk management framework | [FRAMEWORK.md](../../FRAMEWORK.md), [DEFSTAN-ALIGNMENT.md](DEFSTAN-ALIGNMENT.md), `tranc3-repo/compliance/register.yaml` | 3 | 4 |
| Strategic GenAI roadmap | FRAMEWORK §5.2; [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md) §12 | 3 | 3 |
| Regular strategy review | [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md) quarterly | 3 | 3 |
| Stakeholder engagement | BoardRoom, CAB; `tranc3-repo/config/townhall/frameworks.yaml` | 2 | 3 |
| Performance monitoring (AI KPIs) | `GET /compliance/ai/model-cards`; Observatory / monitoring-service | 2 | 3 |
| Contingency / scenario planning | [PROC-BCP-001](../procedures/PROC-BCP-001-Backup-Restore.md), DR runbook | 2 | 3 |
| Policy development (AI) | [POL-AI-001](../policies/POL-AI-001-AI-Ethics-Governance.md) (approved), [AI-GOVERNANCE.md](AI-GOVERNANCE.md) | 4 | 4 |
| Roles & responsibilities | [RACI-MATRIX.md](../governance/RACI-MATRIX.md), FRAMEWORK §9 | 3 | 3 |
| AI governance committee | [AI-GOVERNANCE-COMMITTEE-CHARTER.md](../governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md) | 3 | 3 |
| AI use-case inventory | `tranc3-repo/src/compliance/ai_governance.py` model registry | 2 | 3 |
| Policy review cycle | `docs/policies/INDEX.md` | 2 | 3 |
| Ethics framework | POL-AI-001 + AI-GOVERNANCE §8; Connor/Google mapping §11 | 3 | 4 |
| AI incident response plan | PROC-IR-001 + `POST /compliance/ai/incidents` | 3 | 4 |

**Domain 1 baseline estimate:** **2.5 (Emerging)**

---

## 4. Domain 2 — Data and compliance management

| Control | Tranc3 evidence | Baseline | Target |
|---------|-----------------|----------|--------|
| Data governance framework | POL-PRI-001, [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md), ROPA | 3 | 4 |
| Access control policies | PROC-IAM-001; JWT/MFA in auth-service | 4 | 4 |
| Encryption & anonymisation | AES-GCM, Infinity Void vault; MC-RULE-009 PHI fields | 3 | 4 |
| GenAI data lineage | Model card `training_data` field; `ai_governance.py` | 2 | 3 |
| Regular data audits | Ice Box, access reviews | 2 | 3 |
| Self-learning model monitoring | `classify_risk()` re-classification | 2 | 3 |
| Documentation & reporting | [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md), MC-008/009 | 3 | 4 |
| Compliance monitoring | DEFSTAN CI; `tranc3-repo/src/compliance/checker.py` | 3 | 4 |
| Legal risk assessment (AI) | LEG-006 ✅ Programme; [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md), [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md) | 3 | 4 |
| Regulatory change monitoring | [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md) | 3 | 3 |
| Cross-border compliance | SCCs in ROPA; US PHI residency in MC-RULE-009 | 3 | 3 |

**Domain 2 baseline estimate:** **2.8 (Emerging)**

---

## 5. Domain 3 — Operational and technology management

| Control | Tranc3 evidence | Baseline | Target |
|---------|-----------------|----------|--------|
| SOPs for GenAI use | PROC-CHG-001, AI lifecycle §4 | 2 | 3 |
| GenAI performance monitoring | Observatory, monitoring-service | 3 | 4 |
| Validation & testing before deploy | `config/magna_carta_config.json` ai_governance rules; MC-RULE-009 | 3 | 4 |
| Change management | CAB, PROC-CHG-001 | 3 | 4 |
| Technology assessment framework | POL-SUP-001, vendor review | 2 | 3 |
| Vendor risk assessment (AI) | Supplier DPAs (in progress) | 2 | 3 |
| Feature integration protocol | Third-party model approval | 2 | 3 |
| Post-implementation review | Informal | 1 | 3 |
| IT security policies (AI-specific) | DEFSTAN + OWASP | 3 | 4 |
| Security training | Planned | 2 | 3 |
| Incident response & recovery | PROC-IR-001, PROC-BCP-001 | 3 | 4 |
| Access management (AI systems) | RBAC, service accounts | 3 | 4 |
| Continuous threat monitoring | CI security scanners, logs | 3 | 4 |

**Domain 3 baseline estimate:** **2.5 (Emerging)**

---

## 6. Domain 4 — Human, ethical, and social considerations

| Control | Tranc3 evidence | Baseline | Target |
|---------|-----------------|----------|--------|
| Communicate data currency | Model card metadata | 2 | 3 |
| Employee training (AI limits) | Informal | 1 | 3 |
| Transparent job/role communication | HR policy (general) | 2 | 3 |
| Reskilling / upskilling | Not formalised | 1 | 2 |
| Employee involvement in AI design | Ad hoc | 2 | 3 |
| Feedback loops | Town Hall channels | 2 | 3 |
| Bias detection framework | Fairness API defined, unmeasured | 2 | 4 |
| Diverse training data | Use-case dependent | 2 | 3 |
| Ethics training | POL-AI-001 awareness | 2 | 3 |
| User feedback mechanisms | Product channels | 2 | 3 |
| Third-party ethical audits | Vendor review partial | 2 | 3 |
| Human-in-the-middle (sensitive) | High-risk review informal | 2 | 4 |
| Reputation response | PROC-IR-001 comms | 2 | 3 |
| ESG assessment (AI compute) | Not formalised | 1 | 2 |

**Domain 4 baseline estimate:** **2.0 (Emerging / Nascent edge)**

---

## 7. Domain 5 — Transparency, accountability, continuous improvement

| Control | Tranc3 evidence | Baseline | Target |
|---------|-----------------|----------|--------|
| AI decision documentation | Model cards, audit logs | 3 | 4 |
| Traceability in development | Git, CI, model registry | 3 | 4 |
| Regular decision process reviews | PROC-CMP-001 | 3 | 4 |
| Stakeholder reporting | Quarterly minutes | 2 | 3 |
| Technology evolution monitoring | LEGISLATION-REGISTER | 2 | 3 |
| Governance framework updates | Magna Carta version control | 3 | 4 |
| Innovation labs / pilots | Staging environment | 2 | 3 |
| Awareness & education programmes | Planned | 2 | 3 |
| Abuse prevention | Rate limits, Ice Box, AUP | 3 | 4 |
| Rapid response teams | WarRoom, PROC-IR-001 | 3 | 4 |
| Stakeholder dialogue | BoardRoom, customers | 2 | 3 |

**Domain 5 baseline estimate:** **2.7 (Emerging)**

---

## 8. Summary scorecard (baseline 2026-06-07)

| Domain | Baseline | 2026 target | 2027 target |
|--------|----------|-------------|-------------|
| 1. Strategic alignment | 2.5 | 3.0 | 3.5 |
| 2. Data & compliance | 2.8 | 3.0 | 3.5 |
| 3. Operational & technology | 2.5 | 3.0 | 3.5 |
| 4. Human, ethical & social | 2.0 | 2.5 | 3.0 |
| 5. Transparency & improvement | 2.7 | 3.0 | 3.5 |
| **Overall average** | **2.5** | **2.9** | **3.4** |

---

## 9. Top improvement actions (from baseline)

| Priority | Action | Domain | Owner | Target |
|----------|--------|--------|-------|--------|
| P1 | Execute first PROC-AI-002 bias measurement run | 4 | AI Engineering | Q3 2026 |
| ~~P1 Board-approve POL-AI-001~~ | — | Executive | ✅ 2026-06-07 |
| ~~P1 Formal AI governance committee charter~~ | — | ISMS + AI Lead | ✅ 2026-06-07 |
| P2 | Central GenAI use-case inventory | 1 | AI Lead | Q4 2026 |
| P2 | Employee AI literacy programme | 4 | HR + AI Lead | Q4 2026 |
| P2 | Operationalise PROC-CHG-002 on all major changes | 3 | CAB | Q4 2026 |
| P2 | Obligations register automation | 2 | DPO | Q4 2026 |
| P3 | ESG note on model cards | 4 | Platform | 2027 |

Sync with [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §9 action register.

---

## 10. Assessment records

### 10.1 Completed — 2026-06-07 (baseline)

**Panel:** ISMS Lead (chair), AI Lead, DPO, Platform Engineering (documented self-assessment per PROC-CMP-001)  
**Evidence period:** 2026-03-08 to 2026-06-07  
**Primary Tranc3 sources:** `tranc3-repo/compliance/register.yaml`, `src/compliance/ai_governance.py`, `src/compliance/checker.py`, `config/townhall/frameworks.yaml`  
**Magna Carta sources:** `compliance/magna_carta_register.yaml` (MC-001–009), `config/magna_carta_config.json` (MC-RULE-009 HIPAA profile)

| Domain | Score | Notes |
|--------|-------|-------|
| 1 — Strategic alignment | 2.8 | POL-AI-001 approved; AI committee charter and RACI matrix in place |
| 2 — Data & compliance | 3.0 | OBLIGATIONS + HIPAA/FCA/PECR programmes; supplier DPA register live; signed DPAs 🎯 |
| 3 — Operational & technology | 2.7 | Magna Carta + DEFSTAN gates; PROC-CHG-002 PIR; BCP restore test logged |
| 4 — Human, ethical & social | 2.0 | Bias framework defined; **measurement not yet run** |
| 5 — Transparency & improvement | 2.7 | Model cards, audit trail, PROC-CMP-001 in place |
| **Overall** | **2.7** | Meets 2026 floor (≥2.0); approaching 3.0 target — see §9 actions |

**Top 3 gaps:**
1. Bias/fairness measurement suite not yet executed (Domain 4 / NIST MEASURE — PROC-AI-002).
2. Individual supplier signed DPAs outstanding (Domain 2 — templates issued).
3. ICO registration fee payment and live registration number (OBL-113).

**Actions created:** Synced to [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §9 and [COMPLIANCE-BLUEPRINT.md](COMPLIANCE-BLUEPRINT.md) §8.

**Certification note:** Programme implemented (✅) ≠ ISO 42001 / external attestation (🎯 Q1 2027).

Store completed assessments in Town Hall MeetingRooms / compliance evidence folder.

### 10.2 Template (future assessments)

```markdown
## GenAI Maturity Assessment — [YYYY-MM-DD]

**Panel:** [names]
**Evidence period:** [dates]

| Domain | Score | Notes |
|--------|-------|-------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| **Overall** | | |

**Top 3 gaps:**
1.
2.
3.

**Actions created:** [links to tracker]
```

---

## 11. Related documents

- [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md)
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md)
- [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)
- [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md)
- [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md)
- Connor Group maturity model (reference): https://genai.global/

**Next full assessment:** 2027-06-07 (or before ISO 42001 gap review)
