# ETSI SAI Alignment (EN 304 223)

**Version:** 1.1.0  
**Date:** 2026-06-09  
**Owner:** AI Lead / CISO  
**Source:** [ETSI EN 304 223](https://www.etsi.org/deliver/etsi_en/304200_304299/304223/) (TC SAI, V2.1.1)  
**Review cycle:** Semi-annual (with AI-GOVERNANCE and PROC-CMP-001)

---

## 1. Purpose

Maps **ETSI EN 304 223** — baseline cybersecurity requirements for AI models and AI systems across the lifecycle — to existing Magna Carta programme artefacts. ETSI work complements (does not replace) [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md) and [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md).

**Important limitations:**

| Claim | Programme position |
|-------|-------------------|
| EN 304 223 is an EU **harmonised standard** | **No** — not OJEU-listed for EU AI Act presumption of conformity (monitor via [HARMONISED-STANDARDS-MONITORING.md](HARMONISED-STANDARDS-MONITORING.md)) |
| Certification to EN 304 223 | **No claim** — reference alignment only |
| Substitute for OWASP AI Exchange | **No** — both retained; OWASP remains primary threat/control vocabulary |

**Supporting deliverables:** ETSI TS 104 223 (implementation guide), ETSI TR 104 065 (EU AI Act mapping, informative).

---

## 2. Scope and applicability

| In scope | Out of scope (unless product changes) |
|----------|--------------------------------------|
| Magna Carta AI models (Luminous, Turings Hub, MLflow experiments) | Consumer IoT products (see ETSI EN 303 645 — STD-WATCH-005) |
| Training, fine-tuning, deployment, inference pipelines | Full high-risk conformity assessment (future if tier escalates) |
| Third-party model/API supply chain (SUP-004) | Formal notified-body certification |

Machine-readable watch list: `compliance/standards_watch.yaml` → STD-WATCH-001.

---

## 3. Lifecycle mapping (EN 304 223 → Magna Carta)

EN 304 223 organises requirements around AI lifecycle phases. Programme expression:

| Lifecycle phase | EN 304 223 intent | Magna Carta artefact |
|-----------------|-------------------|----------------------|
| **Design / planning** | Threat analysis; security requirements | AI-SECURITY-THREAT-MODEL; PROC-AI-003 §4 planning |
| **Data acquisition** | Training data integrity, poisoning resistance | RISK-010; supplier DPAs; Ice Box access control |
| **Model development** | Secure dev environment; IP protection | PROC-CHG-001; CI signing; RISK-011 |
| **Verification / validation** | Security testing before release | PROC-AI-003; pen-test programme (PT-AI scope) |
| **Deployment** | Hardening; configuration management | Magna Carta ai_governance rules; MC-RULE-004 |
| **Operation / monitoring** | Runtime detection; incident response | PROC-IR-001; logging; rate limits (RISK-012) |
| **Maintenance / update** | Patch model weights; re-assessment | Model registry; PROC-AI-003 on material change |
| **End of life** | Secure decommission | Model card archive; data retention POL-DAT-001 |

---

## 4. Threat themes → existing controls

| EN 304 223 theme (paraphrased) | Exchange / threat model ID | Programme control |
|-------------------------------|----------------------------|-------------------|
| Data poisoning | TM-AI-003, RISK-010 | Data provenance; access control; PROC-AI-003 §4.1 |
| Model obfuscation / extraction | TM-AI-002, RISK-011 | API rate limits; output filtering; SUP register |
| Indirect prompt injection | TM-AI-001, RISK-009 | Zero-model-trust; MC-RULE-004; human review |
| Supply-chain compromise | TM-AI-011 | POL-SUP-001; SUP-004 TIA (ACT-010) |
| Availability / DoW abuse | TM-AI-010, RISK-012 | Cost caps; MC-RULE-005 |
| Conventional IT on AI infrastructure | — | POL-SEC-001; PROC-VUL-001; ISO 27001 programme |

Full threat inventory: [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md).

---

## 5. EU AI Act relationship

| Instrument | Role |
|------------|------|
| **LEG-006** (EU AI Act) | Legal obligations — [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §3 |
| **ETSI TR 104 065** | Informative mapping EN 304 223 ↔ AI Act articles (reference only) |
| **CEN/CENELEC prEN 18286** | Harmonised QMS track (Art. 17) — monitor, not adopted |
| **ACT-014** | EUR-Lex delegated acts and implementing measures |
| **ACT-015** | Semiannual harmonised + ETSI standards watch |

Do **not** cite EN 304 223 as satisfying a specific AI Act article unless supported by TR 104 065 analysis and legal review.

---

## 6. Gap assessment approach

Use PROC-AI-003 as the operational assessment vehicle:

1. For each registered model, walk PROC-AI-003 checklist.
2. Where a gap is identified, note whether EN 304 223 clause (from TS 104 223) or OWASP Exchange control is the better reference.
3. Record outcome in model card security annex; link to ACT-013 evidence.
4. Escalate material gaps to CAPA per PROC-CAPA-001.

**Baseline checklist:** [ETSI-EN-304-223-GAP-CHECKLIST.md](ETSI-EN-304-223-GAP-CHECKLIST.md) — first programme assessment completed 2026-06-09 (EEV-008; ACT-015 baseline closed). Per-model PROC-AI-003 records: `docs/evidence/proc-ai-003/AST-2026-001` through `AST-2026-003` (EEV-003–005; ACT-013 closed as programme baseline).

**Re-assessment:** On material model or infrastructure change; cross-ref semi-annual watch (ACT-015 recurring) and external pen test (ACT-005).

---

## 7. Related documents

- [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md)
- [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md)
- [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md)
- [HARMONISED-STANDARDS-MONITORING.md](HARMONISED-STANDARDS-MONITORING.md)
- [ETSI-EN-304-223-GAP-CHECKLIST.md](ETSI-EN-304-223-GAP-CHECKLIST.md)
- [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md)
- [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md)
- `compliance/standards_watch.yaml`
- `compliance/execution_evidence_register.yaml`

---

## 8. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-08 | Initial ETSI SAI alignment (PM-013 programme wave) | ISMS Lead |
| 2026-06-09 | First gap checklist baseline; ACT-013/015 programme closures (PM-014) | ISMS Lead |

**Next review:** 2026-12-08 (PROC-CMP-001 semi-annual window)
