# POL-AI-001 — AI Ethics & Governance Policy

**Version:** 1.0.0 (Draft) · **Effective:** 2026-06-07 · **Owner:** AI Lead · **Review:** Semi-annual  
**Status:** Pending BoardRoom approval

---

## 1. Purpose

Govern development and operation of AI systems on Tranc3 in line with EU AI Act, ISO 42001, and Magna Carta human agency principles.

## 2. Scope

All registered models (Luminous, Turing's Hub, MLflow, future models) and AI-integrated features.

## 3. Principles

1. **Transparency** — Users know when they interact with AI; model cards published
2. **Accountability** — Named owners per model; incidents logged
3. **Fairness** — Bias assessed where automated decisions affect people
4. **Safety** — Prohibited uses blocked; cascade/loop failures prevented
5. **Human agency** — High-risk decisions require human review
6. **Privacy** — Training/inference data minimised; DPIA where required

## 4. Requirements

- All models registered before production deployment
- Risk tier assigned per EU AI Act; unacceptable risk prohibited
- Model cards updated on material change
- Fairness metrics measured annually (minimum)
- AI incidents reported via `/compliance/ai/incidents`
- Magna Carta `ai_governance` rules enabled in production

## 5. Prohibited uses

Listed in AI-GOVERNANCE.md §5; enforced at runtime where technically feasible.

## 6. Roles

| Role | Responsibility |
|------|----------------|
| AI Lead | Registry, risk classification |
| DPO | DPIA, Art. 22 transparency |
| Security Ops | Adversarial testing, Ice Box |
| CAB | Approve new high-risk AI features |

## 7. Related documents

AI-GOVERNANCE.md, PROC-CMP-001, `ai_governance.py`, config/magna_carta_config.json
