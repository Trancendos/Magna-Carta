# AI Security Scoping Matrix

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** AI Lead / Security Ops  
**Source inspiration:** Cloud AI security scoping patterns (Answers → Connects → Acts); **vendor-neutral** — no AWS deployment required.

---

## 1. Purpose

Classify every AI use case by **capability tier** and apply **cumulative security controls**. Prevents under-scoping agentic features with chat-only controls.

---

## 2. Capability tiers

| Tier | Name | Description | Examples in Tranc3 |
|------|------|-------------|-------------------|
| **T1** | Answers | Model returns text to user; no external tools | Chat completion, summarisation |
| **T2** | Connects | Model retrieves context (RAG, APIs read-only) | Document Q&A, knowledge base search |
| **T3** | Acts | Model invokes tools that change state | Agents, write APIs, workflow automation |

**Rule:** Tier is determined by **highest** capability in the use case, not the primary UX label.

---

## 3. Cumulative control requirements

| Control domain | T1 Answers | T2 Connects | T3 Acts |
|----------------|------------|-------------|---------|
| Input assurance (injection, jailbreak) | Required | Required + source trust tiers | Required + tool input validation |
| Model assurance (weights, supply chain) | Required | Required | Required + agent registry |
| Output assurance (filtering, PII leak) | Required | Required + citation integrity | Required + action confirmation |
| Authentication / authorisation | Required | Required + data scope per tenant | Required + least model privilege |
| Logging & retention | Required | Required + retrieval audit | Required + tool call audit |
| Human oversight | High-risk outputs | High-risk + sensitive retrieval | **Mandatory** for irreversible actions |
| Rate limits / cost caps | Recommended | Required | Required |
| Threat assessment (PROC-AI-003) | Annual | Annual + on new corpus | Annual + on new tool route |
| Fairness (PROC-AI-002) | If user-facing decisions | If ranking / filtering | If automated decisions |
| Pen test (PT-AI) | Baseline | RAG extraction tests | Agentic abuse cases |

---

## 4. Input / Model / Output assurance grid

Use during PROC-AI-003 assessments and model card security annex updates.

### 4.1 Input assurance

| Check | T1 | T2 | T3 |
|-------|----|----|-----|
| Prompt injection testing | ✓ | ✓ | ✓ |
| Indirect injection (untrusted RAG docs) | — | ✓ | ✓ |
| Input length / token limits | ✓ | ✓ | ✓ |
| PII in prompts blocked or masked | ✓ | ✓ | ✓ |
| Tool argument schema validation | — | — | ✓ |

### 4.2 Model assurance

| Check | T1 | T2 | T3 |
|-------|----|----|-----|
| Model card + version pinning | ✓ | ✓ | ✓ |
| Foundation model vendor DPA/TIA | ✓ | ✓ | ✓ |
| Training data provenance | If fine-tuned | If fine-tuned | If fine-tuned |
| Agent/tool allowlist | — | — | ✓ |
| Lethal trifecta review | — | Partial (exfil via RAG) | ✓ |

### 4.3 Output assurance

| Check | T1 | T2 | T3 |
|-------|----|----|-----|
| Content safety filter | ✓ | ✓ | ✓ |
| Hallucination disclaimers | ✓ | ✓ | ✓ |
| Source citation for facts | — | ✓ | ✓ |
| Human approval before side effects | — | High-risk | ✓ irreversible |
| Output DLP (secrets, PHI) | ✓ | ✓ | ✓ |

---

## 5. Mapping to threat model

| Tier | Primary TM-AI IDs |
|------|-------------------|
| T1 | TM-AI-003, TM-AI-005, TM-AI-006, TM-AI-009 |
| T2 | + TM-AI-004, TM-AI-007 |
| T3 | + TM-AI-010, TM-AI-011 |

Reference: [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md)

---

## 6. Board / executive questions (hymn sheet)

Use in AI Governance Committee and PROC-CMP-001 reviews:

1. What is the **highest tier** (T1/T2/T3) for each production AI feature?
2. For T3: what **irreversible actions** exist and where is human approval?
3. Which **data sources** can RAG retrieve (trusted vs untrusted)?
4. What is the **blast radius** if prompt injection succeeds?
5. When did we last run **PROC-AI-003** for each tier change?

---

## 7. Related documents

- [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md) §4 assurance grid
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md)
- [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md) §8 Responsible AI dimensions
- [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md)
