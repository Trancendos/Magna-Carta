# PROC-AI-002 — Fairness & Bias Testing Procedure

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** AI Lead · **Policy:** POL-AI-001

---

## 1. Purpose

Defines how Tranc3 measures and documents **fairness and bias** for AI models that affect people, satisfying POL-AI-001 §4 and AI-GOVERNANCE MEASURE stage.

**Programme status:** ✅ Procedure implemented. **First measurement cycle** scheduled Q3 2026 (🎯 operational validation).

---

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| Models with automated or semi-automated decisions affecting individuals | Purely internal dev tooling with no user impact |
| Luminous, Turing's Hub, production MLflow models | Experimental models not registered |
| High-risk tier models (mandatory) | Unacceptable-risk (prohibited — no testing path) |

---

## 3. Roles

| Role | Action |
|------|--------|
| AI Lead | Plan, approve results, escalate failures |
| Engineering | Execute tests, implement mitigations |
| DPO | Review if special category or Art. 22 applies |
| AI Governance Committee | Review quarterly summary |

---

## 4. Test plan (minimum annual)

### 4.1 Metrics (select per model type)

| Metric | When to use |
|--------|-------------|
| Demographic parity difference | Classification affecting groups |
| Equalised odds difference | When false positive/negative costs differ by group |
| Calibration by group | Probabilistic outputs |
| Toxicity / harm rate | Generative text models |
| Language fairness | Multilingual models |

**Threshold:** Document acceptable thresholds per model in model card annex. Default: investigate if disparity >5% until calibrated.

### 4.2 Test data

- Use synthetic or anonymised datasets where possible
- No production PII in test fixtures without DPO approval
- Document data provenance in test record

### 4.3 Execution steps

1. Identify model version and risk tier from registry
2. Select metrics from §4.1
3. Run evaluation job (MLflow / Observatory notebook)
4. Record results in fairness test log (see §6)
5. Update model card if material change
6. If threshold exceeded → CAPA within 30 days; escalate to Committee

---

## 5. Triggers (in addition to annual)

- New high-risk model before production
- Material training data change
- Regulatory or incident-driven review
- Customer audit request

---

## 6. Records

| Record | Location | Retention |
|--------|----------|-----------|
| Test plan per model | Model card annex / Town Hall | Life of model + 3 years |
| Raw results | Secure engineering store | 3 years |
| Committee summary | AI Governance Committee minutes | 5 years |

**Initial log entry (baseline):**

| Date | Model | Version | Metrics | Result | Owner |
|------|-------|---------|---------|--------|-------|
| 2026-06-07 | Programme | — | Procedure established | ✅ Ready for Q3 2026 cycle | AI Lead |

---

## 7. Related documents

- [POL-AI-001](../policies/POL-AI-001-AI-Ethics-Governance.md)
- [AI-GOVERNANCE.md](../compliance/AI-GOVERNANCE.md)
- [AI-GOVERNANCE-COMMITTEE-CHARTER.md](../governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md)
- Tranc3: `src/compliance/ai_governance.py`, model cards API
