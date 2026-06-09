# AI Security Threat Assessment — turings_hub

**Assessment ID:** AST-2026-002  
**Model:** turings_hub (Turing's Hub — 3D Entity Builder)  
**Risk tier:** Limited  
**Date:** 2026-06-09  
**Procedure:** PROC-AI-003 · Checklist: HYMN-AI-003  
**Status:** ✅ Baseline complete

---

## HYMN-AI-003 checklist

### Development-time

- [x] Training/fine-tune data provenance documented
- [x] Dataset access controls reviewed
- [x] Third-party model supply chain verified
- [x] CI/CD secrets and artefact integrity confirmed

### Input / inference

- [x] Direct prompt injection controls assessed
- [x] Indirect injection paths identified — low external data ingestion
- [x] Zero-model-trust blast-radius review completed
- [x] Rate limits and cost caps verified
- [x] Extraction / probing mitigations documented
- [x] High-risk output human review — 3D asset review workflow

### Runtime conventional

- [x] Prompt/log storage encryption and retention reviewed
- [x] API AuthN/Z verified

### Agentic

- [N/A] Limited agentic surface — 3D build pipeline only

### Close-out

- [x] TM-AI-001, TM-AI-002 assessed — lower indirect injection exposure
- [x] Model card security annex updated
- [ ] PT-AI — lower priority; include in ACT-005 scope annex

**ETSI lifecycle:** Operation and Deployment phases aligned; Data acquisition lower risk (structured 3D inputs).

**Sign-off:** AI Lead · 2026-06-09 (EEV-004)
