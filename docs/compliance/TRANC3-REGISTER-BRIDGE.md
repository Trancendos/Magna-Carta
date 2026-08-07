# Tranc3 Register Bridge

**Version:** 1.1.0  
**Date:** 2026-06-07 (§3 mapping table extended to MC-041, §4 integration-status table refreshed 2026-08-07)  
**Owner:** Platform Engineering / ISMS Lead  
**Machine-readable:** [compliance/tranc3_register_bridge.yaml](../../compliance/tranc3_register_bridge.yaml)  
**Integration guide:** [TRANC3-INTEGRATION-GUIDE.md](../engineering/TRANC3-INTEGRATION-GUIDE.md)  
**Register:** MC-011

---

## 1. Purpose

Maps Magna Carta requirements (MC-001–MC-041) to Tranc3 DEFSTAN requirements (REQ-###), runtime rules (MC-RULE-###), policies, and obligations. Used when:

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
| MC-011 | Infinity App Bridge (Tranc3) | — | — | This document |
| MC-012 | License Compliance Matrix | REQ-IA-002 | — | `.forgejo/workflows/dependency-audit.yml` |
| MC-013 | Intellectual Property Matrix | REQ-IA-006 | — | `PLATFORM_ENTITIES.md` |
| MC-014 | Encryption Matrix | REQ-IA-001 | — | `docker-compose.production.yml` |
| MC-015 | Security Matrix | REQ-IA-001 | — | `src/security/middleware.py` |
| MC-016 | Legal Matrix | —[^legislation-refs] | — | `docs/governance/ACCEPTABLE-USE-POLICY.md` |
| MC-017 | Financial Matrix | —[^legislation-refs] | — | `src/monetisation/billing.py` |
| MC-018 | Knowledge Matrix | REQ-IA-006 | — | `src/library/knowledge_base.py` |
| MC-019 | Revenue Matrix | —[^related-mc] | — | `src/monetisation/billing.py` |
| MC-020 | Taxation Matrix | —[^legislation-refs] | — | `src/monetisation/billing.py` |
| MC-021 | Zero-Cost Matrix | —[^related-mc] | — | `src/zero_cost/registry.py` |
| MC-022 | Privacy Matrix (DSR Workflow) | REQ-PRI-001 | — | `docs/governance/PRIVACY-MATRIX.md` |
| MC-023 | AI Security Scoping Matrix | —[^no-req] | — | `docs/compliance/AI-SECURITY-SCOPING-MATRIX.md` |
| MC-024 | Permissions & Access Matrix | —[^no-req] | — | `docs/governance/PERMISSIONS-ACCESS-MATRIX.md` |
| MC-025 | Data Transfer Matrix | —[^no-req] | — | `docs/governance/DATA-TRANSFER-MATRIX.md` |
| MC-026 | Hard Stop Matrix | —[^no-req] | — | `docs/governance/HARD-STOP-MATRIX.md` |
| MC-027 | Matrix Index | —[^no-req] | — | `docs/governance/MATRIX-INDEX.md` |
| MC-028 | Code Compliance Matrix | —[^no-req] | — | `docs/governance/CODE-COMPLIANCE-MATRIX.md` |
| MC-029 | Debugging Matrix | —[^no-req] | — | `docs/governance/DEBUGGING-MATRIX.md` |
| MC-030 | Error, Vulnerability, Remediation & Self-Healing Matrix | —[^no-req] | — | `docs/governance/ERROR-REMEDIATION-MATRIX.md` |
| MC-031 | GPU Matrix | —[^no-req] | — | `docs/governance/GPU-MATRIX.md` |
| MC-032 | Token Efficiency Matrix | —[^no-req] | — | `docs/governance/TOKEN-EFFICIENCY-MATRIX.md` |
| MC-033 | Trancendos Models Matrix | —[^no-req] | — | `docs/governance/TRANCENDOS-MODELS-MATRIX.md` |
| MC-034 | AI ↔ Agent ↔ Bot Tier Matrix | —[^no-req] | — | `docs/governance/AI-AGENT-BOT-TIER-MATRIX.md` |
| MC-035 | AI-to-AI Relationship Matrix, Activity Feed & Location Brochure | —[^no-req] | — | `docs/governance/AI-RELATIONSHIP-MATRIX.md` |
| MC-036 | RACI Matrix — Magna Carta Operating Model | —[^no-req] | — | `docs/governance/RACI-MATRIX.md` |
| MC-037 | BOM Matrix — Bills of Materials Across the Platform | —[^no-req] | — | `docs/governance/BOM-MATRIX.md` |
| MC-038 | Environmental Matrix | —[^no-req] | — | `docs/governance/ENVIRONMENTAL-MATRIX.md` |
| MC-039 | Location-to-Location Traffic Matrix | —[^no-req] | — | `docs/governance/LOCATION-TRAFFIC-MATRIX.md` |
| MC-040 | Threshold Matrix | —[^no-req] | — | `docs/governance/THRESHOLD-MATRIX.md` |
| MC-041 | UX/UI Design Matrix | —[^no-req] | — | `docs/governance/UX-UI-DESIGN-MATRIX.md` |

Full detail: [tranc3_register_bridge.yaml](../../compliance/tranc3_register_bridge.yaml).

[^legislation-refs]: No Tranc3 DEFSTAN `REQ-###` requirement exists yet for this matrix's scope — `tranc3_requirements` is correctly empty (`[]`), matching the same pattern as MC-006/007/008/009/010/011. The relevant cross-reference is instead recorded in `tranc3_register_bridge.yaml`'s `legislation_refs` field (Magna Carta `legislation_register.yaml` entries), not conflated with the `REQ-###` namespace.
[^related-mc]: No Tranc3 DEFSTAN `REQ-###` requirement exists yet for this matrix's scope. The cross-reference is recorded in `tranc3_register_bridge.yaml`'s `related_mc_ids` field (a Magna Carta-internal `MC-###` reference), kept in its own field rather than the `tranc3_requirements` list to avoid mixing two different identifier namespaces.
[^no-req]: `tranc3_requirements` is correctly empty (`[]`) in `tranc3_register_bridge.yaml` — this Stage 7.3 matrix (bridged 2026-08-07) has no Tranc3 DEFSTAN `REQ-###` requirement mapped to it yet, matching the same honest-gap pattern as MC-006 through MC-010 and MC-023–MC-041's siblings above.

---

## 4. Integration status (🎯)

| Item | Status | Action |
|------|--------|--------|
| Bridge YAML published | ✅ Programme | MC-011 |
| Tranc3 checker imports MC rows | 🎯 Pending | ACT-009 |
| `MAGNA_CARTA_ENABLED=true` in staging | 🎯 Pending | ACT-009 |
| HIPAA Tier A copy in Tranc3 main | 🎯 Pending | ACT-006 (verified locally) |
| SOC 2 collector + evidence schedule merge | 🎯 Pending | ACT-008 |
| pip-licenses gate in Tranc3's dependency-audit.yml | ✅ Done (Tranc3 `389ef6ae`) | MC-012 |
| Trademark clearance search for the 43 platform entity names | 🎯 Pending (real legal input) | MC-013 |
| Traefik letsencrypt certresolver definition + P0 services on `websecure` | ✅ Done | MC-014 |
| 18-worker `dev-secret` INTERNAL_SECRET fallback removal | ✅ Done | MC-014 |
| Auth enforcement on 6 unauthenticated in-repo routers | ✅ Done | MC-015 |
| External ToS/Privacy Policy/Cookie Policy + company registration confirmation | 🎯 Pending (real legal input) | MC-016 |
| SUP-003 PSP DPA signature | 🎯 Pending (existing ACT-001) | MC-017 |
| Classification/sensitivity/retention model for The Library | ✅ Done | MC-018 |
| Activation of 7 zero-balance revenue streams | 🎯 Pending (owner decision) | MC-019 |
| VAT registration / UTR / real tax-relief claim confirmation | 🎯 Pending (real accountant) | MC-020 |
| `docs/ZERO_COST_VENDOR_MATRIX.md` creation in Tranc3 | ✅ Done | MC-021 |

---

## 5. Related documents

- [magna_carta_register.yaml](../../compliance/magna_carta_register.yaml)
- [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md)
- [FRAMEWORK.md](../../FRAMEWORK.md) §8
- [TRANC3-HIPAA-COPY-REMEDIATION.md](../engineering/TRANC3-HIPAA-COPY-REMEDIATION.md)

**Next review:** 2026-09-06 (PROC-CMP-001)
