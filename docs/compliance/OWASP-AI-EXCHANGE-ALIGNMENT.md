# OWASP AI Exchange Alignment

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead / AI Lead  
**Source:** [OWASP AI Exchange — AI Security Overview](https://owaspai.org/docs/ai_security_overview/) (CC0 1.0)  
**Review cycle:** Semi-annual (with AI-GOVERNANCE and PROC-CMP-001)

---

## 1. Purpose

Maps the [OWASP AI Exchange](https://owaspai.org/) threat-and-control framework to Magna Carta programme artefacts. The Exchange is our **authoritative reference** for AI-specific security (complementing OWASP Top 10 / ASVS for conventional application security).

**Formula (Exchange):** AI security = threats to **AI-specific assets** (this alignment) + threats to **other assets** (existing ISMS — POL-SEC-001, PROC-VUL-001, pen-test programme).

**Relationship to other OWASP AI work:**

| Initiative | Role in Magna Carta |
|------------|---------------------|
| **OWASP AI Exchange** | Comprehensive threat/control model — primary mapping target (this doc) |
| **OWASP GenAI Security Project** | LLM Top 10 awareness; PT-AI scope; red-team scenarios |
| **OpenCRE** | Cross-standard control linking (informative) |

---

## 2. G.U.A.R.D organisational approach

The Exchange recommends five steps. Magna Carta expression:

| Step | Exchange intent | Magna Carta implementation |
|------|-----------------|----------------------------|
| **G**overn | Inventory AI use; assign ownership | AI-GOVERNANCE §1 model registry; Town Hall; MC-005 |
| **U**nderstand | Threats per use case | [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md); PROC-AI-003 |
| **A**dapt | Extend ISMS, SDLC, testing, supply chain | PROC-CHG-001, PROC-VUL-001, supplier register, PROC-AI-002/003 |
| **R**isk evidence | Document rationale and mitigation | Risk register RISK-009–012; model cards; ACT-013 |
| **D**ocument | Outcome-based assurance (EU AI Act) | AI-GOVERNANCE, GENAI-MATURITY, fairness + security test records |

---

## 3. AI-specific assets → Magna Carta controls

| Exchange asset | Primary threats | Magna Carta artefact |
|----------------|-----------------|----------------------|
| Training / validation / test data | Poisoning, leakage | Supplier DPAs; Ice Box; PROC-CHG-001; RISK-010 |
| Model parameters / IP | Extraction, supply-chain tampering | Access control; CI signing; SUP register; RISK-011 |
| Augmentation data (system prompts) | Leakage, injection | Vault; prompt governance in Tranc3; RISK-009 |
| Input (inference) | Evasion, prompt injection | Rate limits; input validation; MC-RULE-004; RISK-009 |
| Output | Untrusted content, injection to downstream | Output filtering; human review; labelling (Art. 50) |
| External data / model supply chain | Poisoned weights, compromised APIs | POL-SUP-001; SUP-004 TIA; ACT-010 |

---

## 4. Threat surfaces → procedures

| Surface | Example threats | Assessment procedure | Technical controls |
|---------|-----------------|----------------------|-------------------|
| **Development-time** | Data poisoning, dev-env model theft | PROC-AI-003 §4.1 | CI, secrets, access reviews |
| **Input / inference** | Prompt injection, evasion, extraction | PROC-AI-003 §4.2 | MC-RULE-004; rate limits; zero-model-trust |
| **Runtime conventional** | Leaking stored input, API abuse | PROC-VUL-001; PROC-IR-001 | AuthN/Z; logging; pen test PT-CORE |

Full threat model: [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md).

---

## 5. Six impacts → risk register

| Impact (Exchange) | Attacker goal | Magna Carta risk ID |
|-------------------|---------------|---------------------|
| Train/test data confidentiality | Disclose | RISK-010 |
| Model IP confidentiality | Disclose | RISK-011 |
| Input / augmentation confidentiality | Disclose | RISK-009 |
| Model behaviour integrity | Deceive | RISK-009 |
| Model availability | Disrupt | RISK-012 |
| Non-AI asset CIA | Disrupt / disclose | RISK-001–008 (existing ISMS) |

---

## 6. Agentic AI (Luminous, tool-calling, multi-agent)

Exchange attention points mapped to Tranc3:

| Property | Security implication | Control |
|----------|---------------------|---------|
| **Action** (tools, APIs) | Expanded blast radius | Least model privilege; tool allowlists |
| **Autonomy** | Emergent behaviour; memory attacks | Human oversight; session state hygiene |
| **Multi-system** | Prompt injection via instructions | Zero-model-trust; blast-radius limits |
| **Lethal trifecta** | Attacker context + sensitive access + exfil path | PROC-AI-003 §5; PT-AI scope |

---

## 7. Governance controls (Exchange §1.1) → Magna Carta

| Exchange control theme | Magna Carta artefact |
|------------------------|----------------------|
| AI PROGRAM (inventory, risk) | AI-GOVERNANCE §1, model cards API |
| SEC PROGRAM | POL-SEC-001, ISO27001-ALIGNMENT |
| SEC DEV PROGRAM | DEFSTAN, PROC-CHG-001, secure SDLC |
| DEV PROGRAM | Tranc3 CI, PROC-CHG-002 PIR |
| CHECK COMPLIANCE | PROC-CMP-001, MON-001–010 |
| SEC EDUCATE | PROC-TRN-001, AI security in awareness refresh |

---

## 8. Standards fed by the Exchange

| Standard | Magna Carta status | Mapping doc |
|----------|-------------------|-------------|
| ISO/IEC 27090 (AI security) | Monitor / align | This doc + AI-SECURITY-THREAT-MODEL |
| ISO/IEC 27091 (AI privacy) | Programme | GDPR-ALIGNMENT, AI-GOVERNANCE |
| ISO/IEC 42001 | Target 🎯 | GENAI-MATURITY, POL-AI-001 |
| EU AI Act (security outcomes) | Programme | AI-GOVERNANCE §3 |
| NIST AI RMF | Mapped | AI-GOVERNANCE §6 |

Register entry: STANDARDS-REGISTER **STD-037**.

---

## 9. Testing alignment

| Exchange testing theme | Magna Carta artefact |
|------------------------|----------------------|
| Fairness / robustness | PROC-AI-002, ACT-004 |
| Adversarial / red team | PROC-AI-003, PT-AI (PEN-TEST-FUTURE-SCOPE-ANNEX §5) |
| Conventional app security | PROC-VUL-001, ACT-005 |

**Operational validation:** ACT-013 — first PROC-AI-003 threat assessment per registered model.

---

## 10. Related documents

- [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md)
- [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md)
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md)
- [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md) §8
- [STANDARDS-REGISTER.md](STANDARDS-REGISTER.md) STD-037, STD-038
- [PEN-TEST-FUTURE-SCOPE-ANNEX.md](../evidence/PEN-TEST-FUTURE-SCOPE-ANNEX.md) §5

**Attribution:** OWASP AI Exchange content is CC0 1.0. This document adapts Exchange concepts for Tranc3/Magna Carta; cite [owaspai.org](https://owaspai.org/) when sharing externally.

**Next review:** 2026-12-08
