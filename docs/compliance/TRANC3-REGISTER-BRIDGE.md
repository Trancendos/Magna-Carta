# Tranc3 Register Bridge

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Platform Engineering / ISMS Lead  
**Machine-readable:** [compliance/tranc3_register_bridge.yaml](../../compliance/tranc3_register_bridge.yaml)  
**Integration guide:** [TRANC3-INTEGRATION-GUIDE.md](../engineering/TRANC3-INTEGRATION-GUIDE.md)  
**Register:** MC-011

---

## 1. Purpose

Maps Magna Carta requirements (MC-001–MC-011) to Tranc3 DEFSTAN requirements (REQ-###), runtime rules (MC-RULE-###), policies, and obligations. Used when:

- Importing Magna Carta rows into Tranc3 compliance reporting
- Tracing audit questions from certification scope to code paths
- Planning ACT-009 staging enablement

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Mapping artefact exists |
| 🎯 **External validation** | Tranc3 import, staging run, or signed evidence pending |

---

## 2. Register relationship

```
Magna Carta (this repo)              Tranc3 (implementation)
─────────────────────────            ─────────────────────────
magna_carta_register.yaml     ──►    compliance/register.yaml (DEFSTAN)
        │                                      │
        └──── tranc3_register_bridge.yaml ─────┘
                      │
              MC-### ↔ REQ-### ↔ MC-RULE-###
```

**Precedence:** Legislation → certification → Magna Carta policies → Tranc3 `register.yaml` → procedures → aspirational architecture.

---

## 3. Mapping summary

| MC ID | Title | Primary REQ | Runtime rules | Key Tranc3 path |
|-------|-------|-------------|---------------|-----------------|
| MC-001 | Digital Rights Transparency | REQ-IA-006 | MC-RULE-008 | `src/compliance/magna_carta.py` |
| MC-002 | Zero-Cost Sovereignty | REQ-IA-002 | MC-RULE-005 | `workers/vault-service/` |
| MC-003 | Town Hall Governance Gate | REQ-SW-003 | MC-RULE-007 | `config/townhall/frameworks.yaml` |
| MC-004 | Magna Carta Runtime Rules | REQ-IA-001/004/005/006 | MC-RULE-001–009 | `src/compliance/magna_carta.py` |
| MC-005 | AI Ethics and Human Agency | REQ-AI-001 | MC-RULE-004 | `src/compliance/ai_governance.py` |
| MC-006 | Policy and Procedure Library | — | — | Magna Carta `docs/policies/` |
| MC-007 | Architecture Evidence Pack | — | — | `ARCHITECTURE_THREAT_MODEL.md` |
| MC-008 | HIPAA Alignment Programme | — | MC-RULE-009 | `src/entities/platform.py` |
| MC-009 | FCA Alignment Programme | — | — | `src/compliance/ai_governance.py` |
| MC-010 | Evidence & Assurance Programme | — | — | `scripts/soc2_evidence_collector.py` |
| MC-011 | Tranc3 Integration Bridge | — | — | This document |

Full detail: [tranc3_register_bridge.yaml](../../compliance/tranc3_register_bridge.yaml).

---

## 4. Integration status (🎯)

| Item | Status | Action |
|------|--------|--------|
| Bridge YAML published | ✅ Programme | MC-011 |
| Tranc3 checker imports MC rows | 🎯 Pending | ACT-009 |
| `MAGNA_CARTA_ENABLED=true` in staging | 🎯 Pending | ACT-009 |
| HIPAA Tier A copy in Tranc3 main | 🎯 Pending | ACT-006 (verified locally) |
| SOC 2 collector + evidence schedule merge | 🎯 Pending | ACT-008 |

---

## 5. Related documents

- [magna_carta_register.yaml](../../compliance/magna_carta_register.yaml)
- [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md)
- [FRAMEWORK.md](../../FRAMEWORK.md) §8
- [TRANC3-HIPAA-COPY-REMEDIATION.md](../engineering/TRANC3-HIPAA-COPY-REMEDIATION.md)

**Next review:** 2026-09-06 (PROC-CMP-001)
