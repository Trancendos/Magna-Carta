# ETSI EN 304 223 Gap Checklist (Baseline)

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** AI Lead / CISO  
**Standard:** STD-042 (ETSI EN 304 223 V2.1.1)  
**Evidence:** EEV-008 · ACT-015 baseline  
**Procedure:** PROC-AI-003, PROC-CMP-001

---

## 1. Purpose

Structured **programme baseline** gap assessment against [ETSI EN 304 223](https://www.etsi.org/deliver/etsi_en/304200_304299/304223/) lifecycle cybersecurity requirements. Supports [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md) §6 and closes the first harmonised-standards watch cycle (ACT-015).

**Legend:** ✅ Implemented · ⚠️ Partial · 📋 Planned · ❌ Gap · N/A Not applicable

**Limitations:** Not a certification claim. EN 304 223 is **not** OJEU-harmonised for EU AI Act presumption of conformity. External validation (notified body, independent pen test) remains on ACT-005 / future conformity track.

---

## 2. Scope

| In scope | Models / systems |
|----------|------------------|
| Registered AI models | `luminous`, `turings_hub`, `mlflow_experiments` |
| Lifecycle phases | Design → data → development → V&V → deployment → operation → maintenance → EOL |
| Programme artefacts | PROC-AI-003 assessments (AST-2026-001–003), AI-SECURITY-THREAT-MODEL, OWASP alignment |

| Out of scope | Reason |
|--------------|--------|
| Consumer IoT (EN 303 645) | B2B AI platform — STD-WATCH-005 monitor only |
| High-risk conformity assessment | No Annex III deployment claimed |
| Formal EN 304 223 certification | No external auditor engaged |

---

## 3. Lifecycle gap matrix

| Phase | EN 304 223 intent (paraphrased) | Status | Evidence / gap |
|-------|----------------------------------|--------|----------------|
| **Design / planning** | Threat analysis; security requirements baseline | ✅ | AI-SECURITY-THREAT-MODEL TM-AI-001–011; PROC-AI-003 §4 |
| **Data acquisition** | Training data integrity; poisoning resistance | ⚠️ | RISK-010; Ice Box access — production lineage automation 📋 |
| **Model development** | Secure dev environment; IP protection | ⚠️ | PROC-CHG-001; CI — signed model artefacts for all paths 📋 |
| **Verification / validation** | Security testing before release | ⚠️ | PROC-AI-003 baseline complete; external pen test ACT-005 open 🎯 |
| **Deployment** | Hardening; configuration management | ✅ | Magna Carta `ai_governance` rules; MC-RULE-004 |
| **Operation / monitoring** | Runtime detection; incident response | ⚠️ | PROC-IR-001; logging — AI-specific alerting rules 📋 |
| **Maintenance / update** | Re-assessment on material change | ✅ | Model registry; PROC-AI-003 trigger on material change |
| **End of life** | Secure decommission | ⚠️ | POL-DAT-001 retention — model card archive procedure 📋 |

---

## 4. Threat theme coverage

| Theme | TM / RISK | Status | Notes |
|-------|-----------|--------|-------|
| Indirect prompt injection | TM-AI-001, RISK-009 | ⚠️ | MC-RULE-004; staging enforcement ACT-009 open 🎯 |
| Model extraction / inversion | TM-AI-002, RISK-011 | ⚠️ | Rate limits; output filtering — pen-test validation pending |
| Data poisoning | TM-AI-003, RISK-010 | ⚠️ | Supplier DPAs; training pipeline provenance partial |
| Supply-chain compromise | TM-AI-011 | ⚠️ | SUP-004 ACT-010 open; TIA template exists |
| Availability / DoW abuse | TM-AI-010, RISK-012 | ✅ | Cost caps; MC-RULE-005 |
| Conventional IT on AI infra | — | ✅ | POL-SEC-001; PROC-VUL-001; ISO 27001 programme |

Per-model detail: `docs/evidence/proc-ai-003/AST-2026-001` through `AST-2026-003`.

---

## 5. Harmonised standards cross-check

| Watch item | Status at 2026-06-09 | Programme action |
|------------|----------------------|------------------|
| EN 304 223 V2.1.1 | Unchanged | This checklist; semi-annual ACT-015 recurrence |
| prEN 18286 (QMS) | Monitor | ISO 42001 gap when EN + OJEU published |
| JTC21 risk management draft | Monitor | May refine PROC-AI-003 on publication |
| OJEU harmonised AI security standard | None listed | Continue reference alignment only |

---

## 6. Summary and next steps

| Metric | Count |
|--------|-------|
| ✅ Implemented | 4 lifecycle phases + 1 threat theme |
| ⚠️ Partial | 6 lifecycle + 4 threat themes |
| ❌ Critical gap | 0 (no undeclared high-risk deployment) |

**Recommended actions (priority order):**

1. Close ACT-009 (request-boundary enforcement) — strengthens deployment/operation gaps.
2. Execute ACT-005 (external pen test) — validates V&V phase.
3. Resolve ACT-010 (SUP-004) — supply-chain theme.
4. Re-run this checklist on next semi-annual watch (due 2026-12-31) or on EN 304 223 edition change.

---

## 7. Related documents

- [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md)
- [HARMONISED-STANDARDS-MONITORING.md](HARMONISED-STANDARDS-MONITORING.md) — WATCH-2026-H1-01
- [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md)
- [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md)
- [compliance/execution_evidence_register.yaml](../../compliance/execution_evidence_register.yaml) — EEV-008
- [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md)

**Next review:** 2026-12-31 (semi-annual harmonised standards watch)
