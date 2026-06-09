# AI Security Threat Assessment — luminous

**Assessment ID:** AST-2026-001  
**Model:** luminous (Luminous — Core AI Engine)  
**Risk tier:** Limited  
**Date:** 2026-06-09  
**Procedure:** PROC-AI-003 · Checklist: HYMN-AI-003  
**Status:** ✅ Baseline complete · 🎯 Annual re-assessment + pen-test PT-AI scope

---

## HYMN-AI-003 checklist

### Development-time

- [x] Training/fine-tune data provenance documented
- [x] Dataset access controls reviewed
- [x] Third-party model supply chain verified (SUP register)
- [x] CI/CD secrets and artefact integrity confirmed

### Input / inference

- [x] Direct prompt injection controls assessed — MC-RULE-004
- [x] Indirect injection paths identified (RAG, email, web)
- [x] Zero-model-trust blast-radius review completed
- [x] Rate limits and cost caps verified — RISK-012
- [x] Extraction / probing mitigations documented
- [x] High-risk output human review in place (escalation path)

### Runtime conventional

- [x] Prompt/log storage encryption and retention reviewed
- [x] API AuthN/Z verified on AI routes

### Agentic

- [x] Tool allowlist / least model privilege documented
- [x] Lethal trifecta analysis — human approval for irreversible tool calls
- [x] Human-in-the-loop for irreversible actions

### Close-out

- [x] TM-AI threats recorded below
- [x] Model card security annex updated (baseline)
- [ ] PT-AI offensive scope — scheduled with ACT-005
- [ ] CAPA — none critical at baseline

---

## TM-AI mapping

| Threat | Status | Control |
|--------|--------|---------|
| TM-AI-001 Indirect injection | Mitigated | MC-RULE-004, input sanitisation |
| TM-AI-002 Model extraction | Partial | Rate limits; monitor probing |
| TM-AI-003 Data poisoning | Mitigated | Provenance + access control |
| TM-AI-010 DoW / cost abuse | Mitigated | MC-RULE-005 |
| TM-AI-011 Supply chain | Partial | SUP-004 ACT-010 open |

**ETSI EN 304 223:** See [ETSI-EN-304-223-GAP-CHECKLIST.md](../../compliance/ETSI-EN-304-223-GAP-CHECKLIST.md) — lifecycle phases Design through Operation covered; Verification gaps tied to ACT-005.

**Sign-off:** AI Lead · Security Ops · 2026-06-09 (EEV-003)
