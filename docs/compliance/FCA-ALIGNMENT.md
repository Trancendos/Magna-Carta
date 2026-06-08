# FCA Alignment Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Legal / ISMS Lead / Finance  
**Scope:** UK financial conduct obligations applicable to Trancendos and Tranc3  
**Certification context:** Governance programme implemented; FCA authorisation only if regulated activities are conducted (§2)

---

## 1. Regulatory perimeter assessment

### 1.1 What Trancendos is (today)

| Role | Description | FCA implication |
|------|-------------|-----------------|
| **Technology platform provider** | Self-hosted AI / operations platform | Generally **not** authorised unless conducting regulated activities |
| **B2B software vendor** | Sells/deploys Tranc3 to business customers | Customer may be FCA-regulated; Trancendos may be **critical third party** |
| **Payment orchestration** | `payments-service` worker (architecture) | Must **not** hold client money without authorisation — use authorised PSP |

**Tranc3 source of truth:** [AS-BUILT-ARCHITECTURE.md](../architecture/AS-BUILT-ARCHITECTURE.md) — `payments-service` on port 8013; no evidence of direct FCA authorisation in codebase.

### 1.2 Regulated activities (Regulated Activities Order 2001)

| Activity | Trancendos conducts? | Position |
|----------|---------------------|----------|
| Accepting deposits | No | N/A |
| Issuing e-money | No | Use authorised partner if needed |
| Payment services (PSD2) | **No direct** — orchestration only | Partner with FCA-authorised PI/EMI |
| Arranging deals in investments | No | Unless product scope changes |
| Advising on investments | No | AI must not present as regulated advice (§6) |
| Insurance mediation | No | N/A |
| Consumer credit | No | Unless lending features added |

**Conclusion:** Trancendos operates **outside direct authorisation** for current Tranc3 feature set, but remains subject to **cross-cutting FCA expectations** (Consumer Duty, financial promotions, operational resilience as supplier, SM&CR if authorised persons join).

---

## 2. FCA Handbook — applicable rulebooks

| Handbook | Applicability | Programme status | Magna Carta artefact |
|----------|---------------|------------------|----------------------|
| **PRIN** — Principles for Businesses | ✅ Conduct baseline | ✅ | FRAMEWORK, policies |
| **PRIN 2A** — Consumer Duty | ✅ If UK retail consumers use financial features | ✅ | §3 |
| **SYSC** — Senior Management Arrangements | ⚠️ Full SYSC if authorised; principles adopted now | ✅ | COMPLIANCE-BLUEPRINT roles |
| **COBS 4** — Financial promotions | ✅ If marketing financial product features | ✅ | §4 |
| **COBS 10A** — Appropriateness (MiFID) | If investment features for retail | N/A today | Monitor |
| **PS21/3** — Operational resilience | ✅ If **critical third party** to UK financial sector | ✅ | §5 |
| **SM&CR** | Only if FCA-authorised firm | N/A today | §7 |
| **SUP** — Supervision | If authorised | N/A | — |
| **DORA** (UK onshored) | ICT third-party risk for financial entities | ✅ Supplier readiness | POL-SUP-001 |

---

## 3. Consumer Duty (PRIN 2A)

Applies when Trancendos provides products or services to **retail customers** in the UK that involve financial outcomes (subscriptions, payments UX, AI-assisted financial decisions).

| Consumer Duty outcome | Implementation |
|-----------------------|----------------|
| **Good outcomes for retail customers** | Clear product descriptions; no dark patterns in billing flows |
| **Products and services** | Features match documented capability; AI labelled assistive |
| **Price and value** | Transparent pricing in Town Hall billing config |
| **Consumer understanding** | Plain-language terms; AI disclosure (EU AI Act Art. 50 aligned) |
| **Consumer support** | Documented support channels; DSR and complaint path |

**AI-specific:** Automated outputs that could influence financial decisions require human review and disclaimers — see [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §8 and `ai_governance.py` prohibited uses.

**Evidence:** Privacy notice, model cards, billing documentation, complaint handling in PROC-DSR-001 (extend for financial complaints).

---

## 4. Financial promotions (COBS 4 / FCA FG24/1)

| Rule | Requirement | Control |
|------|-------------|---------|
| Fair, clear, not misleading | All public claims verifiable | §10 claim tiers (mirrors HIPAA approach) |
| Risk warnings | Required for investment-like content | Content review before publish |
| Approval process | Financial promotions approver | Legal + Compliance sign-off |
| Social media / AI-generated marketing | Same standards apply | Ice Box + human approval |

**Prohibited without approval:**

- Claims of FCA authorisation unless true
- Guaranteed returns or risk-free financial outcomes
- AI presented as regulated financial advice

**Register:** Financial promotions log (Legal) — linked from OBL-100 series.

---

## 5. Operational resilience (PS21/3) — supplier perspective

If a UK **authorised firm** relies on Tranc3 for important business services, Trancendos may be in scope as an **ICT / operational supplier**.

| Expectation | Trancendos response |
|-------------|---------------------|
| Impact tolerances | Customer-defined; Tranc3 SLA in contract |
| Mapping important business services | Customer responsibility; Tranc3 provides architecture pack |
| Testing | DR drills (PROC-BCP-001); customer-led resilience testing |
| Third-party risk management | POL-SUP-001; SOC2/ISO evidence packs |
| Self-assessment | Customer documents Tranc3 in their register |

**Deliverables to FCA-regulated customers:**

- [AS-BUILT-ARCHITECTURE.md](../architecture/AS-BUILT-ARCHITECTURE.md)
- [CONTROL-TO-COMPONENT-MAP.md](../architecture/CONTROL-TO-COMPONENT-MAP.md)
- SOC 2 / ISO programme status
- Incident notification clauses in contract

---

## 6. AI in financial services (FCA / BoE / PRA DP24/6 context)

| Risk | Control |
|------|---------|
| AI as regulated advice | Blocked — assistive only; disclaimers mandatory |
| Algorithmic bias in credit/insurance | Prohibited use without approval (`ai_governance.py`) |
| Model explainability | Model cards API; DSR Art. 22 path |
| Third-party AI models | POL-SUP-001 security review |
| GenAI governance | [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md) |

**FCA expectation:** Governance, data quality, monitoring, and human oversight — mapped to Connor GenAI domains in EXTERNAL-FRAMEWORK-MAPPING.

---

## 7. SM&CR (Senior Managers & Certification Regime)

| Status | Action |
|--------|--------|
| **Not in scope today** | No FCA Part 4A permission held |
| **If authorisation sought** | SMF roles, responsibilities maps, certification regime for material functions |
| **Current governance** | BoardRoom, executive accountability in FRAMEWORK §9 |

---

## 8. Payments and AML

| Topic | Position |
|-------|----------|
| **Client money** | Trancendos does **not** hold client funds; payments via authorised third-party PSP |
| **AML / KYC** | Not a financial institution — **out of scope** unless business model changes |
| **PCI DSS** | No cardholder data stored (REGULATION-MATRIX) |
| **Financial crime prevention** | Supplier due diligence via POL-SUP-001 |

**payments-service rule:** Must integrate only with FCA-authorised payment institutions; document in customer deployment guide.

---

## 9. SYSC-adopted governance (pre-authorisation best practice)

| SYSC area | Adoption |
|-----------|----------|
| 4.1 — Apportionment of responsibilities | RACI in FRAMEWORK §9 |
| 4.2 — Adequate skilled resources | Role definitions in COMPLIANCE-BLUEPRINT |
| 6.1 — Compliance function | ISMS Lead + DPO |
| 7.1 — Risk assessment | Risk register (Tranc3) |
| 13 — Record keeping | Audit logs, policy version control |
| 19 — Whistleblowers | HR policy reference (planned) |

---

## 10. Marketing and claims policy

| Claim | Allowed? | Condition |
|-------|----------|-----------|
| "FCA regulated" | **Only if true** | FCA FRN displayed |
| "FCA-aligned governance" | Yes | This programme + evidence |
| "Suitable for FCA-regulated firms" | Yes | With supplier due diligence pack |
| "Provides financial advice" | **No** | Platform is not an adviser |

---

## 11. Obligations cross-reference

| OBL-ID | Obligation | Status |
|--------|------------|--------|
| OBL-100 | PRIN 2A Consumer Duty (retail financial features) | ✅ Programme |
| OBL-101 | COBS 4 fair/clear/not misleading | ✅ Programme |
| OBL-102 | PS21/3 supplier resilience support | ✅ Programme |
| OBL-103 | Payment services via authorised PI only | ✅ Architecture rule |
| OBL-104 | AI not presented as regulated advice | ✅ ai_governance |
| OBL-105 | DORA ICT third-party readiness | ✅ POL-SUP-001 |

Full register: [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md) §4.7.

---

## 12. Gap register (authorisation-dependent — not programme gaps)

| Item | Status | Trigger |
|------|--------|---------|
| FCA Part 4A permission | N/A | Only if regulated activities added |
| SM&CR responsibility maps | N/A | On authorisation |
| Formal Consumer Duty board report | Annual template ready | First UK retail financial feature launch |
| Financial promotions approver roster | Legal sign-off | Q3 2026 |
| Critical third party self-certification pack | Customer-facing doc | Q4 2026 |

---

## 13. Evidence catalogue

| Artefact | Location |
|----------|----------|
| Payments architecture | `payments-service` in AS-BUILT |
| AI governance (financial prohibited uses) | `tranc3-repo/src/compliance/ai_governance.py` |
| Governance model | Town Hall `frameworks.yaml` |
| Magna Carta register | `compliance/magna_carta_register.yaml` MC-009 |
| Consumer-facing policies | POL-PRI-001, POL-AI-001 |

---

## 14. Review schedule

| Activity | Frequency |
|----------|-----------|
| Regulatory perimeter review | Quarterly (PROC-CMP-001) |
| Financial promotions log audit | Quarterly |
| FCA policy watch (FG, CP, PS) | Monthly triage |
| Authorisation assessment | On new financial feature proposal |

**Next review:** 2026-09-06

---

## 15. Related documents

- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
- [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md)
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md)
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)
- [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md)
