# AI Security Threat Assessment — mlflow_experiments

**Assessment ID:** AST-2026-003  
**Model:** mlflow_experiments (MLflow Experiment Tracker)  
**Risk tier:** Minimal  
**Date:** 2026-06-09  
**Procedure:** PROC-AI-003 · Checklist: HYMN-AI-003  
**Status:** ✅ Baseline complete

---

## HYMN-AI-003 checklist (dev-time focus)

### Development-time

- [x] Training data provenance — experiment metadata only
- [x] Dataset access controls — Ice Box / internal network
- [x] Third-party supply chain — minimal external model pull
- [x] CI/CD secrets confirmed

### Input / inference

- [N/A] No public inference endpoint — internal MLOps only

### Runtime conventional

- [x] MLflow auth and network segmentation reviewed
- [x] Audit logging for experiment mutations

### Agentic

- [N/A]

### Close-out

- [x] TM-AI-003, TM-AI-011 dev-environment focus
- [x] Model card notes internal-only scope

**Primary gap:** Ensure experiment artefacts do not contain production PII — ongoing PROC-DAT-001 alignment.

**Sign-off:** AI Lead · MLOps · 2026-06-09 (EEV-005)
