# Regulation & Standards Matrix

**Version:** 1.1.0  
**Date:** 2026-06-08  
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
| PECR | UK | ⚠️ | ✅ Programme | [PECR-ALIGNMENT.md](PECR-ALIGNMENT.md), POL-PRI-001 | Cookie UI if marketing cookies deployed 🎯 |
| ePrivacy Directive | EU | ⚠️ | ⚠️ | Same | Privacy policy |
| CCPA / CPRA | California, US | ⚠️ | ✅ Programme | GDPR baseline; [CCPA-CPRA-ALIGNMENT.md](CCPA-CPRA-ALIGNMENT.md) | Activate if CA users material 🎯 |
| LGPD | Brazil | ❌ N/A | ✅ Programme (future) | No BR operations today | [LGPD-READINESS.md](LGPD-READINESS.md) |
| POPIA | South Africa | ❌ N/A | ✅ Programme (future) | No ZA operations today | [POPIA-READINESS.md](POPIA-READINESS.md) |

---

## 2. Information security & assurance

| Standard | Applicability | Status | Target | Evidence |
|----------|---------------|--------|--------|----------|
| ISO/IEC 27001:2022 | ✅ | ⚠️ Draft SOA | 🎯 Q2 2027 | Tranc3 `ISO27001_SOA.md`, policies |
| ISO/IEC 27002:2022 | ✅ | ⚠️ | — | Control implementation via SOA |
| SOC 2 Type II (TSC) | ✅ | ⚠️ Draft | 🎯 Q1 2027 | `SOC2_TYPE_II.md`, evidence collector |
| DEFSTAN (civilian) | ✅ Voluntary | ✅ Strong | Active | `register.yaml`, CI gate |
| NIST CSF 2.0 | ⚠️ Reference | ✅ Programme | — | [NIST-CSF-ALIGNMENT.md](NIST-CSF-ALIGNMENT.md) |
| CIS Controls v8 | ⚠️ Reference | ⚠️ Partial | — | IAM, logging, vuln mgmt implemented |
| OWASP Top 10 (2021) | ✅ | ✅ | Active | Penetration tests, hardening |
| OWASP ASVS L2 | ⚠️ Target | ⚠️ Partial | — | Auth, validation, logging strong |
| OWASP AI Exchange | ✅ | ✅ Programme | — | [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md), PROC-AI-003 |
| OWASP GenAI LLM Top 10 | ⚠️ Reference | ✅ Mapped | — | PT-AI scope; AI-SECURITY-THREAT-MODEL |
| PCI DSS v4.0 | ❌ N/A | ✅ Programme (position) | — | No CHD; [PCI-DSS-POSITION.md](PCI-DSS-POSITION.md) |
| HIPAA | ⚠️ US PHI boundary | ✅ Programme | 🎯 Tier C on customer path | [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md), MC-008, MC-RULE-009 |
| FedRAMP | ❌ N/A | ✅ Programme (future) | — | [FEDRAMP-READINESS.md](FEDRAMP-READINESS.md) |
| CMMC 2.0 | ❌ N/A | ✅ Programme (future) | — | [CMMC-READINESS.md](CMMC-READINESS.md) |

---

## 3. AI & emerging technology

| Framework | Applicability | Status | Evidence |
|-----------|---------------|--------|----------|
| EU AI Act | ✅ (deploy in EU) | ✅ Programme | [AI-GOVERNANCE.md](AI-GOVERNANCE.md), model cards, MC-RULE-004; CELEX `32024R1689` — [legislation_register.yaml](../../compliance/legislation_register.yaml), [EUR-LEX-ELI-REFERENCE.md](EUR-LEX-ELI-REFERENCE.md) |
| ISO/IEC 42001:2023 | ⚠️ Target | ✅ Programme | AI governance module, GENAI-MATURITY |
| NIST AI RMF 1.0 | ⚠️ Reference | ✅ Mapped | AI-GOVERNANCE.md |
| UK AI White Paper / DSIT | ⚠️ Reference | ✅ Programme | [UK-AI-LEGISLATION-MONITORING.md](UK-AI-LEGISLATION-MONITORING.md) |
| Algorithmic transparency | ⚠️ | ✅ Programme | Model cards; bias measurement operational target |
| AI security (OWASP AI Exchange) | ✅ | ✅ Programme / 🎯 assess | OWASP-AI-EXCHANGE-ALIGNMENT, PROC-AI-003 | ACT-013 first assessment |
| Connor GenAI Governance Framework v1.0 | ✅ Reference | ✅ Mapped | [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md), [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md) |
| Google AI Principles | ✅ Reference | ✅ Mapped | [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §11 |

---

## 4. Operational & quality

| Standard | Applicability | Status | Evidence |
|----------|---------------|--------|----------|
| ITIL 4 | ✅ Internal | ✅ Programme | Town Hall ITSM, incident templates, PROC-IR-001 |
| PRINCE2 7 | ✅ Projects | ✅ Programme | Stage gates via BoardRoom, PROC-CHG-002 PIR |
| ISO 22301 (BCM) | ⚠️ Target | ✅ Programme | POL-OPS-003, PROC-BCP-001, [BCP-RESTORE-TEST-LOG.md](../evidence/BCP-RESTORE-TEST-LOG.md) |
| ISO 9001 | ❌ | — | — | QA via DEFSTAN 05-086 instead |

---

## 5. Legal & financial

| Area | Applicability | Status | Artefact |
|------|---------------|--------|----------|
| UK Companies Act | ✅ | ✅ Programme | [COMPANIES-ACT-ALIGNMENT.md](COMPANIES-ACT-ALIGNMENT.md), BoardRoom |
| FCA Handbook (PRIN, COBS 4, PS21/3) | ✅ Supplier / conduct | ✅ Programme | [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md), MC-009 |
| IP / copyright | ✅ | ✅ | Proprietary code; OSS licence audit |
| Contract law (SLAs) | ✅ | ⚠️ | Customer agreements TBD |
| Export controls | ❌ | — | No controlled cryptography export |
| AML / KYC | ❌ | — | Not a financial institution |

---

## 6. Industry-specific (future)

| Regulation | Trigger | Status |
|------------|---------|--------|
| HIPAA | Health data processing with US persons | ✅ Programme — [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md) |
| FCA / PRA | Regulated financial services in UK | ✅ Programme (supplier/conduct) — authorisation N/A unless regulated activities |
| NHS DSPT | NHS data handling | ❌ N/A | ✅ Programme (future) | [NHS-DSPT-READINESS.md](NHS-DSPT-READINESS.md) |
| Research / Concordat | Academic or clinical research data | ✅ Programme (future) | [RESEARCH-DATA-CONCORDAT-ANNEX.md](RESEARCH-DATA-CONCORDAT-ANNEX.md) |

**Honest status register:** [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md) — explains every ⚠️, 📋, and ❌.

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

## 8. Master framework catalogue

Customer-requested assurance frameworks (CSA STAR, GxP, ISO family, PCI family, SOC, FedRAMP, CMMC, global privacy laws, NIST, sector regimes, vendor portals) are inventoried in:

| Artefact | Scope |
|----------|-------|
| [STANDARDS-AND-FRAMEWORKS-REGISTER.md](STANDARDS-AND-FRAMEWORKS-REGISTER.md) | Human master (FW-001–FW-130, 112 deduplicated entries) |
| [readiness/INDEX.md](readiness/INDEX.md) | Grouped readiness docs by domain |
| `compliance/frameworks_register.yaml` | Machine-readable mirror (MON-009 validated) |

Programme milestone **PM-009** (2026-06-08) closed Layer 2 catalogue coverage. External certification and signed evidence remain Layer 3 (**ACT-001–ACT-015**).

---

## 9. Review schedule

| Activity | Frequency |
|----------|-----------|
| Legislation register scan | Quarterly |
| Matrix status update | Quarterly (with DEFSTAN review) |
| New regulation assessment | On announcement |
| Certification scope review | Annual |

**Next review:** 2026-09-06
