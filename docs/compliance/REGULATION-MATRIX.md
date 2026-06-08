# Regulation & Standards Matrix

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead / DPO  
**Scope:** Tranc3 platform and Trancendos-operated services

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Applicable and substantially implemented |
| ⚠️ | Applicable — partial / in progress |
| 📋 | Documented mapping only — not yet implemented |
| ❌ | Not applicable (with justification) |
| 🎯 | Certification target date |

---

## 1. Privacy & data protection

| Regulation | Jurisdiction | Applicability | Status | Tranc3 evidence | Magna Carta artefact |
|------------|--------------|---------------|--------|-----------------|----------------------|
| UK GDPR | UK | ✅ | ✅ | ROPA, PIA, users-service DSR | POL-PRI-001, PROC-DSR-001 |
| DPA 2018 | UK | ✅ | ✅ | Same as UK GDPR | LEGISLATION-REGISTER |
| EU GDPR | EU | ✅ | ✅ | SCCs for external AI fallback in ROPA | GDPR-ALIGNMENT.md |
| PECR | UK | ⚠️ | ⚠️ | Cookie/consent if marketing cookies used | Privacy policy |
| ePrivacy Directive | EU | ⚠️ | ⚠️ | Same | Privacy policy |
| CCPA / CPRA | California, US | ⚠️ | 📋 | GDPR controls provide baseline | Extend if CA users material |
| LGPD | Brazil | ❌ | — | No BR operations planned | — |
| POPIA | South Africa | ❌ | — | No ZA operations planned | — |

---

## 2. Information security & assurance

| Standard | Applicability | Status | Target | Evidence |
|----------|---------------|--------|--------|----------|
| ISO/IEC 27001:2022 | ✅ | ⚠️ Draft SOA | 🎯 Q2 2027 | Tranc3 `ISO27001_SOA.md`, policies |
| ISO/IEC 27002:2022 | ✅ | ⚠️ | — | Control implementation via SOA |
| SOC 2 Type II (TSC) | ✅ | ⚠️ Draft | 🎯 Q1 2027 | `SOC2_TYPE_II.md`, evidence collector |
| DEFSTAN (civilian) | ✅ Voluntary | ✅ Strong | Active | `register.yaml`, CI gate |
| NIST CSF 2.0 | ⚠️ Reference | 📋 | — | Mapped via ISO/SOC2 controls |
| CIS Controls v8 | ⚠️ Reference | ⚠️ Partial | — | IAM, logging, vuln mgmt implemented |
| OWASP Top 10 (2021) | ✅ | ✅ | Active | Penetration tests, hardening |
| OWASP ASVS L2 | ⚠️ Target | ⚠️ Partial | — | Auth, validation, logging strong |
| PCI DSS v4.0 | ❌ | — | — | No CHD; payments via third-party if any |
| HIPAA | ❌* | — | — | *Unless health boundary formally scoped |
| FedRAMP | ❌ | — | — | Not US government cloud |
| CMMC 2.0 | ❌ | — | — | Not defence contractor CUI |

---

## 3. AI & emerging technology

| Framework | Applicability | Status | Evidence |
|-----------|---------------|--------|----------|
| EU AI Act | ✅ (deploy in EU) | ⚠️ | `AI_GOVERNANCE.md`, model cards |
| ISO/IEC 42001:2023 | ⚠️ Target | ⚠️ | AI governance module |
| NIST AI RMF 1.0 | ⚠️ Reference | ⚠️ Mapped | AI-GOVERNANCE.md |
| UK AI White Paper / DSIT | ⚠️ Reference | 📋 | Monitor legislation |
| Algorithmic transparency | ⚠️ | ⚠️ | Model cards; bias metrics pending |
| Connor GenAI Governance Framework v1.0 | ✅ Reference | ⚠️ Mapped | [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md), [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md) |
| Google AI Principles | ✅ Reference | ⚠️ Mapped | [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §11 |

---

## 4. Operational & quality

| Standard | Applicability | Status | Evidence |
|----------|---------------|--------|----------|
| ITIL 4 | ✅ Internal | ⚠️ | Town Hall ITSM, incident templates |
| PRINCE2 7 | ✅ Projects | ⚠️ | Stage gates via BoardRoom |
| ISO 22301 (BCM) | ⚠️ Target | ⚠️ | DR runbook; formal BCP policy added here |
| ISO 9001 | ❌ | — | — | QA via DEFSTAN 05-086 instead |

---

## 5. Legal & financial

| Area | Applicability | Status | Artefact |
|------|---------------|--------|----------|
| UK Companies Act | ✅ | ⚠️ | Financial oversight framework (Town Hall) |
| IP / copyright | ✅ | ✅ | Proprietary code; OSS licence audit |
| Contract law (SLAs) | ✅ | ⚠️ | Customer agreements TBD |
| Export controls | ❌ | — | No controlled cryptography export |
| AML / KYC | ❌ | — | Not a financial institution |

---

## 6. Industry-specific (future)

| Regulation | Trigger | Status |
|------------|---------|--------|
| HIPAA | Health data processing with US persons | ❌ Not implemented |
| FCA / PRA | Regulated financial services in UK | ❌ Not in scope |
| NHS DSPT | NHS data handling | ❌ Not in scope |

**Rule:** Do not claim compliance in product copy (`platform.py`, marketing) unless the corresponding row is ✅ with evidence.

---

## 7. Cross-regulation control mapping (summary)

| Control domain | GDPR | ISO 27001 | SOC 2 | DEFSTAN |
|----------------|------|-----------|-------|---------|
| Authentication | Art. 32 | 5.15–5.18, 8.5 | CC6 | REQ-IA-001 |
| Encryption | Art. 32 | 8.24 | CC6 | REQ-IA-002, REQ-IA-008 |
| Logging | Art. 30, 32 | 8.15 | CC7 | REQ-IA-006 |
| Access rights | Art. 15–22 | 8.3 | CC6 | REQ-IA-001 |
| Incident response | Art. 33–34 | 5.24–5.27 | CC7 | REQ-SU-003 |
| Change control | — | 8.32 | CC8 | REQ-CM-001 |
| Supplier mgmt | Art. 28 | 5.19–5.22 | CC9 | REQ-CM-004 |
| AI governance | Art. 22, AI Act | 8.x (emerging) | PI | REQ-SA-001 |

Full component mapping: [../architecture/CONTROL-TO-COMPONENT-MAP.md](../architecture/CONTROL-TO-COMPONENT-MAP.md)

---

## 8. Review schedule

| Activity | Frequency |
|----------|-----------|
| Legislation register scan | Quarterly |
| Matrix status update | Quarterly (with DEFSTAN review) |
| New regulation assessment | On announcement |
| Certification scope review | Annual |

**Next review:** 2026-09-06
