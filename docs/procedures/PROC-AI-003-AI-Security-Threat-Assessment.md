# PROC-AI-003 — AI Security Threat Assessment Procedure

**Version:** 1.0.0 · **Effective:** 2026-06-08 · **Owner:** AI Lead / Security Ops · **Policy:** POL-AI-001, POL-SEC-001

---

## 1. Purpose

Defines how Tranc3 identifies, assesses, and documents **AI-specific security threats** per the [OWASP AI Exchange](https://owaspai.org/docs/ai_security_overview/) model, complementing conventional application security (PROC-VUL-001, pen-test PT-CORE).

**Programme status:** ✅ Procedure implemented. **First assessment cycle** scheduled Q4 2026 (🎯 ACT-013).

**Formula:** AI security = threats to AI-specific assets (this procedure) + threats to other assets (existing ISMS).

---

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| Registered models in AI-GOVERNANCE §1 | Non-AI subsystems (conventional threat model) |
| Development-time, inference, and agentic surfaces | Pure fairness/bias (PROC-AI-002) |
| Luminous, Turing's Hub, MLflow experiments | Experimental unregistered models |

**Threat model reference:** [AI-SECURITY-THREAT-MODEL.md](../compliance/AI-SECURITY-THREAT-MODEL.md) (TM-AI-001–011).

---

## 3. Roles

| Role | Action |
|------|--------|
| AI Lead | Own assessment; approve model card security annex |
| Security Ops | Review controls; feed PT-AI scope |
| Engineering | Implement mitigations; provide architecture context |
| DPO | Review if confidentiality impacts involve personal data |
| ISMS Lead | Escalate residual high risks to risk register |

---

## 4. Assessment surfaces (minimum annual per model)

### 4.1 Development-time

| Check | Threat IDs | Evidence |
|-------|------------|----------|
| Training/fine-tune data provenance documented | TM-AI-001 | Model card; data pipeline diagram |
| Access control on datasets and experiment stores | TM-AI-001, TM-AI-002 | IAM review; MLflow permissions |
| Third-party model weights verified (checksum, vendor) | TM-AI-002 | SUP register; ACT-010 for SUP-004 |
| CI/CD secrets and artefact signing | TM-AI-002 | PROC-CHG-001; DEFSTAN gate |

### 4.2 Input / inference (runtime)

| Check | Threat IDs | Evidence |
|-------|------------|----------|
| Prompt injection controls (direct and indirect) | TM-AI-003, TM-AI-004 | Input validation; RAG trust tiers |
| Zero-model-trust blast-radius review | TM-AI-003–007 | Tool allowlists; output filtering |
| Rate limits and cost caps | TM-AI-008 | MC-RULE-005; API gateway config |
| Extraction / probing resistance | TM-AI-006, TM-AI-007 | Throttling; logging |
| High-risk output human review | TM-AI-005 | AI-GOVERNANCE §8 |

### 4.3 Runtime conventional (non-inference)

| Check | Threat IDs | Evidence |
|-------|------------|----------|
| Prompt/log storage encryption and retention | TM-AI-009 | Vault; log policy |
| API authentication and authorisation | TM-AI-009, TM-AI-011 | PROC-IAM-001 |
| Agentic tool registry (least model privilege) | TM-AI-010, TM-AI-011 | Route config; deny-by-default |

### 4.4 Agentic addendum (when applicable)

If the model invokes tools, retains session memory, or chains agents:

1. Map **lethal trifecta** legs (attacker context + sensitive access + exfil path)
2. Confirm at least one leg is broken by design
3. Document human-in-the-loop gates for irreversible actions

---

## 5. Six impacts checklist

For each in-scope model, confirm controls address:

| # | Impact | Risk register |
|---|--------|---------------|
| 1 | Training data confidentiality | RISK-010 |
| 2 | Model IP confidentiality | RISK-011 |
| 3 | Input / augmentation confidentiality | RISK-009 |
| 4 | Model behaviour integrity | RISK-009 |
| 5 | Model availability | RISK-012 |
| 6 | Non-AI asset CIA | Existing ISMS risks |

---

## 6. Execution steps

1. Select model version from registry (`GET /compliance/ai/model-cards`)
2. Complete [HYMN-AI-003](../hymn-sheets/HYMN-AI-003-AI-Security-Threat-Assessment-Checklist.md)
3. Walk surfaces §4.1–4.4 using [COOK-AI-003](../cookbooks/COOK-AI-003-AI-Security-Threat-Assessment.md)
4. Record applicable TM-AI-### threats, control status, and gaps
5. Update model card **security annex**
6. Raise CAPA for critical gaps within 30 days; link to ACT-013 evidence
7. Feed unresolved offensive gaps to PT-AI scope ([PEN-TEST-FUTURE-SCOPE-ANNEX.md](../evidence/PEN-TEST-FUTURE-SCOPE-ANNEX.md) §5)

---

## 7. Triggers (in addition to annual)

- New production model or major version
- New agentic tool routes or RAG data sources
- Material supplier change (foundation model vendor)
- Security incident involving AI (PROC-IR-001 + AI incident API)
- OWASP AI Exchange or ISO 27090 material update

---

## 8. Records

| Record | Location | Retention |
|--------|----------|-----------|
| Completed checklist | Evidence folder / model card annex | Life of model + 3 years |
| Threat assessment summary | AI Governance Committee minutes | 5 years |
| PT-AI scope additions | PEN-TEST-LOG.md | Per pen-test programme |

**Initial log entry (baseline):**

| Date | Model | Version | Result | Owner |
|------|-------|---------|--------|-------|
| 2026-06-08 | Programme | — | ✅ Procedure + threat model established | AI Lead |

---

## 9. Related documents

- [OWASP-AI-EXCHANGE-ALIGNMENT.md](../compliance/OWASP-AI-EXCHANGE-ALIGNMENT.md)
- [AI-SECURITY-THREAT-MODEL.md](../compliance/AI-SECURITY-THREAT-MODEL.md)
- [PROC-AI-002](PROC-AI-002-Fairness-Bias-Testing.md) (fairness — separate track)
- [PROC-VUL-001](PROC-VUL-001-Vulnerability-Management.md)
- [POL-AI-001](../policies/POL-AI-001-AI-Ethics-Governance.md)
- [POL-SEC-001](../policies/POL-SEC-001-Information-Security.md)
