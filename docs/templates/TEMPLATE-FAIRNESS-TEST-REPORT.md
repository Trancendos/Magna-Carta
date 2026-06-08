# Template — Fairness & Bias Test Report (PROC-AI-002)

**Version:** 1.0.0 (outline)  
**Date:** 2026-06-08  
**Owner:** AI Lead  
**Use:** ACT-004, quarterly model review, high-risk model release  
**Status:** ✅ Programme outline · 🎯 First executed test cycle pending

---

## Report metadata

| Field | Value |
|-------|-------|
| Report ID | FTR-YYYY-### |
| Model name | |
| Model version / registry ID | |
| Risk tier (POL-AI-001) | High / Limited / Minimal |
| Test date | YYYY-MM-DD |
| Tester | Name / role |
| Reviewer | AI Lead |
| DPO review required? | Yes / No — rationale |

---

## 1. Scope and objective

- **Purpose of test:** (annual cycle · pre-release · incident-driven · customer audit)
- **Affected populations / use case:**
- **Protected attributes evaluated:** (e.g. age band, gender, language, geography)
- **Out of scope:** (experimental models, internal-only tooling)

---

## 2. Test plan summary

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| Demographic parity difference | ≤ 5% | Default per PROC-AI-002 §4.1 |
| Equalised odds difference | | |
| Calibration by group | | |
| Toxicity / harm rate | | |
| Language fairness | | |

**Test dataset:** Source · anonymisation · DPO approval reference

---

## 3. Results

| Metric | Group A | Group B | Delta | Pass / Investigate / Fail |
|--------|---------|---------|-------|-------------------------|
| | | | | |

**Summary narrative:** (2–3 sentences on material findings)

---

## 4. Disparities and mitigations

| Finding ID | Description | Severity | Mitigation / CAPA | Owner | Due date |
|------------|-------------|----------|-------------------|-------|----------|
| | | | | | |

If threshold exceeded → open CAPA per PROC-CAPA-001; escalate to AI Governance Committee within 5 business days.

---

## 5. Model card and registry updates

- [ ] Model card annex updated
- [ ] MLflow / Observatory record linked
- [ ] COMPLIANCE-ACTION-TRACKER updated (if ACT-004 milestone)
- [ ] Customer-facing documentation reviewed (if applicable)

---

## 6. Sign-off

| Role | Name | Date | Signature / ticket ref |
|------|------|------|------------------------|
| AI Lead | | | |
| DPO (if required) | | | |
| AI Governance Committee (if material) | | | |

---

## Execution checklist

- [ ] Test plan aligned to PROC-AI-002 §4
- [ ] No production PII in fixtures without DPO approval
- [ ] Results stored in evidence repository (retention: life of model + 3 years)
- [ ] Linked from [COOK-AI-002-Fairness-Bias-Test.md](../cookbooks/COOK-AI-002-Fairness-Bias-Test.md)

**Related:** [PROC-AI-002-Fairness-Bias-Testing.md](../procedures/PROC-AI-002-Fairness-Bias-Testing.md) · ACT-004 · RISK-005
