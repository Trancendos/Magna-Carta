# COOK-AI-002 — Fairness & Bias Test Run Playbook

**Version:** 1.0.0  
**Owner:** AI Governance Lead  
**Procedure:** [PROC-AI-002](../procedures/PROC-AI-002-Fairness-Bias-Testing.md)  
**Hymn sheet:** [HYMN-AI-002](../hymn-sheets/HYMN-AI-002-Fairness-Test-Checklist.md)

---

## When to use

Before production release of model-affecting change, quarterly model review, or ACT-004 milestone.

---

## Prepare

1. Confirm **model card** current for target model
2. Select **evaluation dataset** — documented, representative, no PII leakage
3. Define **protected attributes** and fairness metrics per POL-AI-001

---

## Run

1. Execute bias/fairness test suite (automated + manual spot checks)
2. Record disparity metrics vs thresholds
3. Human review of edge-case failures
4. Document limitations in model card

---

## Decide

| Outcome | Action |
|---------|--------|
| Pass | CAB / AI board sign-off for deploy |
| Conditional | Mitigations + monitoring before release |
| Fail | Block release; CAPA; retrain or rule adjustment |

Update AI-GOVERNANCE evidence and COMPLIANCE-COVERAGE-REGISTER AI row.
