# External Framework Mapping — GenAI & Compliance

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead / AI Lead  
**Purpose:** Map third-party governance methodologies to Magna Carta layers and Tranc3 controls  
**Review cycle:** Semi-annual

---

## 1. Scope and use

This document **does not replace** Trancendos policies, DEFSTAN, or certification mappings. It shows how widely used external frameworks align with Magna Carta so teams can:

- Adopt proven governance patterns without reinventing structure
- Communicate maturity to auditors, partners, and boards using familiar language
- Prioritise gaps using external risk taxonomies

**Adaptation rule:** Concepts are adapted for Tranc3; source frameworks are cited for attribution. Do not reproduce copyrighted framework text verbatim in customer-facing packs.

---

## 2. Sources assessed

| Source | Applicable to Magna Carta? | Use in Tranc3 |
|--------|---------------------------|---------------|
| Connor Group **Generative AI Governance Framework v1.0** | ✅ Yes | Five-domain structure, control considerations, maturity model |
| Connor Group **GenAI Maturity Model v1.0** | ✅ Yes | Self-assessment (see [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md)) |
| NGX / Risk Academy **Compliance Programme** | ✅ Yes | Obligations management, monitoring vs audit (see [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)) |
| University **Concordat / research legislation** | ✅ Programme (future) | [RESEARCH-DATA-CONCORDAT-ANNEX.md](RESEARCH-DATA-CONCORDAT-ANNEX.md) when research in scope |
| **Google AI Principles** | ✅ Yes | Principles layer in [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §11 |
| **GitHub Brand Guidelines** | ❌ No | Marketing/visual identity only — out of governance scope |

**Attribution:** Connor Group GenAI materials © David A. Wood et al.; NGX materials © Nigerian Exchange Limited (training context); Google AI Principles © Google.

---

## 3. Connor five domains → Magna Carta layers

```
Connor Domain                          Magna Carta Layer              Primary artefacts
─────────────────────────────────────────────────────────────────────────────────────────
1. Strategic Alignment &               Layer 1 — Governance           FRAMEWORK.md §3–5
   Control Environment                 Layer 2 — Policies             POL-AI-001, POL-SEC-001
                                       Town Hall / BoardRoom          config/townhall/

2. Data & Compliance Management        Layer 4 — Compliance           LEGISLATION-REGISTER,
                                       legislation_register.yaml,     EU-LEGISLATION-MONITORING,
                                       EUR-LEX-ELI-REFERENCE
                                       Layer 2 — Privacy              GDPR-ALIGNMENT, POL-PRI-001
                                       Technical                      Ice Box, Cryptex, ROPA

3. Operational & Technology Mgmt       Layer 5 — Architecture         AS-BUILT, CONTROL-MAP
                                       Layer 3 — Procedures           PROC-CHG-001, PROC-VUL-001
                                       Layer 6 — Evidence             register.yaml, CI gates

4. Human, Ethical & Social             Layer 2 — AI policy            POL-AI-001
                                       Layer 4 — AI governance        AI-GOVERNANCE.md §8
                                       HR / comms                     Town Hall notices

5. Transparency, Accountability &      Layer 6 — Evidence             Audit service, Observatory
   Continuous Improvement               Layer 3 — Review               PROC-CMP-001
                                       Runtime                        magna_carta_config.json
```

---

## 4. Domain 1 — Strategic alignment and control environment

| External control theme | Magna Carta implementation | Tranc3 component |
|------------------------|---------------------------|------------------|
| GenAI risk management framework | FRAMEWORK.md + DEFSTAN + ISO SOA | `compliance/register.yaml` |
| Strategic GenAI roadmap | Certification roadmap (FRAMEWORK §5.2) | Town Hall `frameworks.yaml` |
| Stakeholder engagement | BoardRoom, CAB, quarterly PROC-CMP-001 | MeetingRooms |
| Policy development & governance | `docs/policies/` (8 policies) | Magna Carta register MC-001–007 |
| GenAI inventory | Model registry in AI governance | `ai_governance.py`, model cards API |
| Incident response (AI-specific) | POL-OPS-001 + PROC-IR-001 + AI incidents API | `POST /compliance/ai/incidents` |
| Ethics framework | POL-AI-001, AI-GOVERNANCE §8 | `ai_governance` Magna Carta rules |

**Gap priorities (post-2026-06-07):** Board approval for all policies (POL-AI-001 drafted); AI governance committee **charter authored** but first meeting 🎯; centralised GenAI use-case inventory beyond registered models. **Programme artefacts (layer 2):** Connor/Google mapping doc, GENAI-MATURITY §10 baseline, HIPAA (MC-008), FCA (MC-009) alignment docs.

---

## 5. Domain 2 — Data and compliance management

| External control theme | Magna Carta implementation | Tranc3 component |
|------------------------|---------------------------|------------------|
| Data governance framework | POL-PRI-001, GDPR-ALIGNMENT, ROPA | users-service, Ice Box |
| Access control / encryption | POL-SEC-001, PROC-IAM-001 | JWT/MFA, AES-GCM SQLite |
| Data lineage | ROPA + model cards (training data field) | Compliance API |
| Legal / regulatory monitoring | LEGISLATION-REGISTER, OBLIGATIONS-REGISTER | Quarterly PROC-CMP-001 |
| Cross-border compliance | GDPR-ALIGNMENT (SCCs for AI fallback) | ROPA external processors |
| Self-learning models | AI-GOVERNANCE lifecycle §4 | Monitor + re-classify risk tier |

**Gap priorities:** Formal data-lineage tooling; automated regulatory change alerts; **signed processor DPAs** (register exists; countersignature incomplete). **Programme artefacts (layer 2):** LEGISLATION-REGISTER (LEG-006–010), OBLIGATIONS-REGISTER §4.6–4.7.

---

## 6. Domain 3 — Operational and technology management

| External control theme | Magna Carta implementation | Tranc3 component |
|------------------------|---------------------------|------------------|
| SOPs for GenAI use | PROC-CHG-001 (AI changes), AI-GOVERNANCE §4 | CAB + model deploy gate |
| Performance monitoring | Observatory, fairness report API | monitoring-service |
| Validation before deploy | Magna Carta `ai_governance` checks | `magna_carta.py` |
| Vendor / technology assessment | POL-SUP-001, supplier DPAs | Third-party model review |
| IT security for AI systems | DEFSTAN, OWASP, Zero Trust | Traefik, Ice Box, vault |
| Continuous security monitoring | PROC-VUL-001, pen test programme | CI: Bandit, Semgrep, Trivy |

**Gap priorities:** Documented AI change-management SOP; post-implementation review template for new models; supplier AI vendor assessment checklist.

---

## 7. Domain 4 — Human, ethical, and social considerations

| External control theme | Magna Carta implementation | Tranc3 component |
|------------------------|---------------------------|------------------|
| Training on limitations | AI-GOVERNANCE §8, POL-AI-001 | Internal wiki / Town Hall |
| Human-in-the-loop | High-risk → manual review | Art. 14 / Art. 22 workflows |
| Bias detection & mitigation | Fairness metrics (planned) | Fairness report API |
| Reputation / sensitive content | Human review before external publish | Content policy (operational) |
| ESG impact of AI compute | Optional sustainability note in model cards | Infrastructure metrics |

**Gap priorities:** Bias measurement suite; mandatory human review workflow for high-risk tiers; employee AI literacy programme.

---

## 8. Domain 5 — Transparency, accountability, continuous improvement

| External control theme | Magna Carta implementation | Tranc3 component |
|------------------------|---------------------------|------------------|
| Decision documentation | Model cards, audit logs | Audit service (append-only) |
| Traceability | Request IDs, model card versioning | Observability stack |
| Stakeholder reporting | PROC-CMP-001 outputs, SOC2 collector | `test_evidence.yaml` |
| Technology evolution monitoring | Legislation watch list, AI Act updates | LEGISLATION-REGISTER |
| Innovation pilots | Staging + feature flags | Town Hall zero-cost check |

**Gap priorities:** Formal GenAI decision audit trail standard; innovation lab charter for controlled pilots.

---

## 9. NGX compliance programme → Magna Carta

| NGX concept | Magna Carta equivalent |
|-------------|------------------------|
| Compliance framework (guidelines, procedures, registers) | FRAMEWORK.md + policies + procedures + registers |
| Code of conduct | POL-SEC-002 (AUP) + ethics in POL-AI-001 |
| Monitoring vs auditing | See COMPLIANCE-BLUEPRINT §11; PROC-CMP-001 §6 |
| Risk-based assessment (RBA) | DEFSTAN scoring + risk register + waivers |
| Regulatory obligations management | [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md) |
| Implementation requirements (scope, intelligence, objectives, controls) | COMPLIANCE-BLUEPRINT §3–8, PROC-CMP-001 |

---

## 10. Google AI principles → Magna Carta

| Google principle | Magna Carta expression |
|------------------|------------------------|
| **Bold innovation** | Self-hosted AI platform, open research-friendly stack; measured rollout via CAB |
| **Responsible development** | EU AI Act mapping, human agency §8, prohibited-use blocklist |
| **Collaborative progress** | Ecosystem repos, documented model cards, partner DPAs |

Detail: [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §11.

---

## 11. Research integrity (optional annex)

If Trancendos processes **research data** (human subjects, clinical trials, export-controlled dual-use, GMO, animal research), extend LEGISLATION-REGISTER with domain-specific legislation and require Concordat-aligned integrity training. Programme coverage: [RESEARCH-DATA-CONCORDAT-ANNEX.md](RESEARCH-DATA-CONCORDAT-ANNEX.md). Default Tranc3 scope is **commercial AI platform** — annex activates only when research is declared in scope statement.

---

## 11. OWASP AI Exchange → Magna Carta (security layer)

Source: [OWASP AI Exchange — AI Security Overview](https://owaspai.org/docs/ai_security_overview/) (CC0). Primary mapping: [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md).

| Exchange concept | Magna Carta expression |
|------------------|------------------------|
| **G.U.A.R.D** (Govern, Understand, Adapt, Risk evidence, Document) | AI-GOVERNANCE; PROC-AI-003; risk register RISK-009–012; model cards |
| AI-specific assets (data, model IP, prompts, I/O) | AI-SECURITY-THREAT-MODEL §4–5; supplier register; Vault |
| Three surfaces (dev-time, inference, runtime conventional) | PROC-AI-003 §4; PROC-VUL-001; pen-test PT-CORE + PT-AI |
| Six impacts (disclose ×3, deceive, disrupt ×2) | RISK-009–012; incident response PROC-IR-001 |
| Zero-model-trust | Assume prompt injection can succeed; blast-radius controls |
| Agentic AI (lethal trifecta) | AI-SECURITY-THREAT-MODEL §6; tool allowlists; human oversight |
| OWASP GenAI LLM Top 10 | Awareness + PT-AI red-team scenarios (STD-038) |

**Complements (does not replace):** Connor five-domain ethics/governance mapping (§3–8), PROC-AI-002 fairness track, conventional OWASP Top 10 (STD-007).

**Operational validation:** ACT-013 — first PROC-AI-003 assessment per registered model.

---

## 12. Implementation workflow (four steps)

Adapted from Connor framework adoption steps:

| Step | Action | Magna Carta artefact |
|------|--------|----------------------|
| 1 | Define GenAI objectives aligned to strategy | FRAMEWORK.md §3, BoardRoom charter |
| 2 | Scope framework to organisational priorities | This document §3–8; skip non-applicable domains |
| 3 | Risk assessment + maturity baseline | GENAI-MATURITY-ASSESSMENT.md; DEFSTAN + AI gaps |
| 4 | Execute roadmap, review quarterly | PROC-CMP-001; action register in AI-GOVERNANCE §9 |

---

## 13. Related documents

- [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md)
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md)
- [COMPLIANCE-BLUEPRINT.md](COMPLIANCE-BLUEPRINT.md)
- [FRAMEWORK.md](../../FRAMEWORK.md)
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
- [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md)
- [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md)
- [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md)
- [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md)

**Next review:** 2026-12-07
