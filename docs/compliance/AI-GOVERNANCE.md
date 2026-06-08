# AI Governance Alignment

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** AI Lead / ISMS Lead  
**Source of truth (operational):** [Tranc3 `docs/compliance/AI_GOVERNANCE.md`](https://github.com/Trancendos/Tranc3/blob/main/docs/compliance/AI_GOVERNANCE.md)  
**Review cadence:** Quarterly

---

## 1. Governance scope

AI systems within Tranc3 ISMS scope:

| Model ID | Name | Risk tier (EU AI Act) | Owner |
|----------|------|----------------------|-------|
| `luminous` | Luminous — Core AI Engine | Limited | AI Engineering |
| `turings_hub` | Turing's Hub — 3D Entity Builder | Limited | AI Engineering |
| `mlflow_experiments` | MLflow Experiment Tracker | Minimal | MLOps |

**API:** `GET /compliance/ai/model-cards` · `POST /compliance/ai/incidents`

---

## 2. Framework coverage

| Framework | Status | Magna Carta artefact |
|-----------|--------|----------------------|
| EU AI Act (2024/1689) | ✅ Programme | POL-AI-001, this document, OBL-020–025 |
| ISO/IEC 42001:2023 | ✅ Programme | AI governance module, GENAI-MATURITY |
| NIST AI RMF 1.0 | ✅ Mapped | Risk classification, §6 functions |
| UK AI Safety (voluntary) | ✅ Applied | Transparency principles, model cards |
| Connor GenAI five-domain | ✅ Mapped | EXTERNAL-FRAMEWORK-MAPPING, GENAI-MATURITY |
| Google AI Principles | ✅ Mapped | §11 principles alignment |
| HIPAA (US PHI) | ✅ Programme | [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md), MC-008 |
| FCA Handbook (UK) | ✅ Programme | [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md), MC-009 |
| GDPR Art. 22 | ✅ Active | Model cards, human review |

---

## 3. EU AI Act mapping

| Article | Requirement | Implementation | Gap |
|---------|-------------|----------------|-----|
| Art. 5 | Prohibited practices | Blocklist in model cards | Formal review pending |
| Art. 9 | Risk management | `classify_risk()` runtime | Annex III assessment incomplete |
| Art. 13 | Transparency | Model cards published | — |
| Art. 14 | Human oversight | High-risk → manual review | Workflow informal |
| Art. 15 | Accuracy & robustness | Fairness metrics defined | **Unmeasured** — needs dataset |
| Art. 50 | Limited-risk transparency | AI-labelled responses | — |
| Art. 16–17 | High-risk obligations | N/A unless tier escalated | — |

---

## 4. Lifecycle controls

```
Design → Register → Risk classify → Deploy → Monitor → Incident → Retire
   │         │            │            │         │          │         │
   │         │            │            │         │          │         └─ Archive model card
   │         │            │            │         │          └─ POST /compliance/ai/incidents
   │         │            │            │         └─ Fairness report API
   │         │            │            └─ Magna Carta ai_governance rules
   │         │            └─ classify_risk() + use-case rules
   │         └─ Model registry (ai_governance.py)
   └─ DPIA if profiling / special category
```

---

## 5. Prohibited and restricted uses

**Prohibited (platform-wide):**
- Social scoring affecting legal rights
- Real-time biometric identification in public spaces (without legal basis)
- Subliminal manipulation causing harm
- Exploitation of vulnerable groups
- Unacceptable-risk classification per EU AI Act Art. 5

**Restricted (require approval):**
- Automated decisions affecting employment, credit, or legal status
- Processing special category data in AI pipelines
- Deployment of third-party models without security review

---

## 6. NIST AI RMF functions

| Function | Status | Evidence |
|----------|--------|----------|
| **GOVERN** | ✅ | AI policy, registry, incident log, Magna Carta MC-001–009 |
| **MAP** | ✅ Programme | Risk tiers, EU AI Act §3 mapping, model cards, prohibited-use blocklist |
| **MEASURE** | ✅ Programme | [PROC-AI-002](../procedures/PROC-AI-002-Fairness-Bias-Testing.md) defined; **first measurement run** 🎯 Q3 2026 |
| **MANAGE** | ✅ Programme | Incident API, PROC-IR-001, PROC-CMP-001, action register §9 |

---

## 7. Runtime enforcement (Magna Carta)

When `MAGNA_CARTA_ENABLED=true`, config rules enforce:

```json
{
  "type": "ai_governance",
  "checks": [
    "model_registered",
    "risk_tier_documented",
    "prohibited_use_blocked",
    "ai_content_labelled"
  ]
}
```

See [config/magna_carta_config.json](../../config/magna_carta_config.json).

---

## 8. Human agency principles (Magna Carta)

1. AI outputs are **assistive**, not authoritative, unless explicitly configured.
2. Users must be informed when interacting with AI (Art. 50).
3. High-risk automated decisions require **human review** before effect.
4. Users may request explanation of automated logic via DSR (Art. 22).
5. Kill-switch: operators can disable AI routes via feature flags / Town Hall.

---

## 9. Action register

| Action | Priority | Owner | Target |
|--------|----------|-------|--------|
| Execute first PROC-AI-002 bias measurement run | High | AI Engineering | Q3 2026 |
| ~~Board-approve POL-AI-001~~ | — | Executive | ✅ 2026-06-07 |
| Complete Annex III assessment | Medium | DPO + AI Lead | Q4 2026 |
| ISO 42001 gap assessment | Medium | ISMS Lead | Q1 2027 |
| Formal improvement process (ISO 42001 §10) | Medium | AI Lead | Q4 2026 |

---

## 10. Related documents

- [POL-AI-001](../policies/POL-AI-001-AI-Ethics-Governance.md)
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
- [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md)
- [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md)
- [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md)
- [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md)
- Tranc3 `src/compliance/ai_governance.py`
- Tranc3 `src/compliance/magna_carta.py` (runtime hooks)

---

## 11. External principles alignment

Magna Carta AI governance aligns with widely cited public principles. These are **adapted** for Tranc3 — not copied verbatim from vendor documents.

### 11.1 Google AI Principles (reference)

| Principle | Magna Carta expression |
|-----------|------------------------|
| **Bold innovation** | AI features ship through DEFSTAN-gated CI; model cards and Observatory metrics prove outcomes |
| **Responsible development** | Human oversight (§8), bias testing (action register), kill-switch via Town Hall |
| **Collaborative progress** | Open standards (NIST AI RMF, ISO 42001 mapping); partner DPAs and SCCs documented |

### 11.2 Connor Group five-domain mapping

| Domain | Primary Magna Carta artefact |
|--------|------------------------------|
| Strategic alignment | [FRAMEWORK.md](../../FRAMEWORK.md) §3, [POL-AI-001](../policies/POL-AI-001-AI-Ethics-Governance.md) |
| Data & compliance | [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md), [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md), GDPR alignment |
| Operational & technology | [COMPLIANCE-BLUEPRINT.md](COMPLIANCE-BLUEPRINT.md), DEFSTAN register, CI gates |
| Human, ethical & social | §8 human agency, POL-AI-001, bias and transparency controls |
| Transparency & improvement | [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md), [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md) |

Full mapping: [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md)

**Next review:** 2026-09-07
