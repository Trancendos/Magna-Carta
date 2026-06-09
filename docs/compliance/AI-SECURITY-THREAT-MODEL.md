# AI Security Threat Model — Tranc3

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** AI Lead / Security Ops  
**Framework:** [OWASP AI Exchange](https://owaspai.org/docs/ai_security_overview/) (adapted)  
**Procedure:** [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md)  
**Review cycle:** Annual per model; after material architecture change

---

## 1. Scope

Applies to registered AI systems in [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §1:

| Model ID | Agentic? | Notes |
|----------|----------|-------|
| `luminous` | Partial (tool routes) | Core engine — highest security scrutiny |
| `turings_hub` | Low | 3D builder; limited external data |
| `mlflow_experiments` | No | Internal MLOps; dev-time surface dominant |

**Out of scope:** Non-AI subsystems (covered by conventional threat models and pen-test PT-CORE).

---

## 2. Design principle: zero-model-trust

Assume an attacker **can** mislead the model (prompt injection, evasion) or extract data. Security properties therefore rely on **blast-radius limitation**, not on model alignment alone.

| Layer | Intent |
|-------|--------|
| Prevention | Input validation, prompt hardening, tool allowlists |
| Detection | Logging, anomaly alerts, output classifiers |
| Impact limitation | Least privilege, human approval gates, rate limits, data minimisation |

---

## 3. Three threat surfaces

```
┌─────────────────────────────────────────────────────────────────┐
│  DEVELOPMENT-TIME                                                │
│  Data poisoning · supply-chain model tampering · dev-env theft   │
└────────────────────────────┬────────────────────────────────────┘
                             │ trained / deployed model
┌────────────────────────────▼────────────────────────────────────┐
│  INPUT / INFERENCE (runtime)                                     │
│  Prompt injection · evasion · extraction · resource exhaustion   │
└────────────────────────────┬────────────────────────────────────┘
                             │ alongside
┌────────────────────────────▼────────────────────────────────────┐
│  RUNTIME CONVENTIONAL (non-inference)                            │
│  API abuse · credential theft · leaking stored prompts/logs      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Six impacts and attacker goals

| # | Impact | Goal | Example Tranc3 scenario |
|---|--------|------|-------------------------|
| 1 | Training data confidentiality | Disclose | Membership inference on fine-tune set |
| 2 | Model IP confidentiality | Disclose | Parameter extraction via API probing |
| 3 | Input / augmentation confidentiality | Disclose | System prompt leak via injection |
| 4 | Model behaviour integrity | Deceive | Jailbreak causing unsafe tool invocation |
| 5 | Model availability | Disrupt | Denial-of-wallet / rate-limit exhaustion |
| 6 | Non-AI asset CIA | Disrupt / disclose | Stolen API key → broader tenant access |

Risk register: RISK-009 (integrity/confidentiality at inference), RISK-010 (data), RISK-011 (model IP), RISK-012 (availability).

---

## 5. Threat catalogue (minimum)

| Threat ID | Surface | Description | Primary controls |
|-----------|---------|-------------|------------------|
| TM-AI-001 | Development | Training data poisoning | Data provenance; access control; anomaly detection on datasets |
| TM-AI-002 | Development | Supply-chain compromised model | Vendor review; checksums; SUP register |
| TM-AI-003 | Inference | Direct prompt injection | Input sanitisation; instruction hierarchy; output review |
| TM-AI-004 | Inference | Indirect prompt injection (RAG, email, web) | Content trust tiers; sandboxed retrieval |
| TM-AI-005 | Inference | Evasion / adversarial input | Monitoring; human review for high-risk |
| TM-AI-006 | Inference | Model inversion / membership inference | Output minimisation; query rate limits |
| TM-AI-007 | Inference | Model extraction | API throttling; watermarking; legal ToS |
| TM-AI-008 | Inference | Resource exhaustion | Rate limits; cost caps; MC-RULE-005 |
| TM-AI-009 | Runtime | Leakage of logs / stored prompts | Encryption; retention limits; access reviews |
| TM-AI-010 | Agentic | Tool abuse beyond intent | Tool allowlists; least model privilege |
| TM-AI-011 | Agentic | Lethal trifecta exfiltration | Session isolation; egress controls; human-in-loop |

---

## 6. Agentic AI addendum

**Applies when:** models invoke tools, retain session memory, or chain to other agents (Luminous routes).

### 6.1 Lethal trifecta

All three must be present for high-impact data exfiltration:

1. **Attacker-controlled context** entering the session (indirect prompt injection)
2. **Access** to sensitive data via tools or retrieval
3. **Exfiltration path** (email, HTTP callback, user-visible channel)

**Mitigation pattern:** break at least one leg — e.g. no sensitive tools without approval; strip untrusted content before model context.

### 6.2 Controls (Exchange-aligned)

| Control | Implementation |
|---------|----------------|
| Least model privilege | Per-route tool registry; deny-by-default |
| Human oversight | High-risk actions require operator confirm (AI-GOVERNANCE §8) |
| Memory integrity | Session TTL; no cross-tenant state |
| Observability | AI incident API; security logging |

---

## 7. Ready-made vs custom models

Tranc3 primarily uses **ready-made** foundation models with fine-tuning / RAG — not full in-house training.

| Threat emphasis | Ready-made posture |
|-----------------|-------------------|
| Data poisoning | Lower (limited training); monitor fine-tune pipelines |
| Prompt injection | **High** — primary operational focus |
| Supply chain | Vendor DPAs (SUP-004); ACT-010 |
| Extraction | API abuse monitoring |

---

## 8. Assessment workflow

1. Select model + version from registry  
2. Run [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md) using [COOK-AI-003](../cookbooks/COOK-AI-003-AI-Security-Threat-Assessment.md)  
3. Record applicable TM-AI-### threats and control gaps  
4. Update model card security annex  
5. Feed gaps to ACT-013 / CAPA / PT-AI scope  

---

## 9. Related documents

- [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md)
- [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md)
- [PEN-TEST-FUTURE-SCOPE-ANNEX.md](../evidence/PEN-TEST-FUTURE-SCOPE-ANNEX.md) §5
- [RISK-REGISTER.md](RISK-REGISTER.md)
- OWASP GenAI LLM Top 10 (awareness reference)

**Next review:** 2026-12-08
