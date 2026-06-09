# Standards & Frameworks Register — Master Catalogue

**Version:** 1.1.0  
**Date:** 2026-06-09  
**Owner:** ISMS Lead / DPO  
**Review cycle:** Quarterly (PROC-CMP-001)  
**Purpose:** Canonical inventory of every external standard, certification, regulation, and assurance framework requested for Magna Carta coverage — with honest applicability and programme status.

**Related:** [STANDARDS-REGISTER.md](STANDARDS-REGISTER.md) (legacy STD-IDs), [REGULATION-MATRIX.md](REGULATION-MATRIX.md), [readiness/INDEX.md](readiness/INDEX.md), `compliance/frameworks_register.yaml`

---

## Legend

| Symbol | Programme layer | Meaning |
|--------|-----------------|---------|
| ✅ Programme | Layer 2 | Mapping doc, policy, procedure, or register maintained |
| ✅ Operational | Layer 3 | Live evidence — certificate, authorisation, signed contract, completed assessment |
| ⚠️ Partial | — | Applicable; gaps remain |
| 📋 Readiness | Layer 2 | Trigger not active; future-scenario doc prepared |
| ❌ N/A | — | Not applicable today (justification recorded) |
| 🎯 | — | External certification or validation target date |

**Machine-readable mirrors:** `compliance/frameworks_register.yaml` (MON-009), `compliance/framework_implementation_catalog.yaml` (MON-009 / MON-018), `compliance/framework_triggers.yaml`, `compliance/proactive_signals.yaml`.

---

## 1. ISO and management system standards

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-001 | ISO/IEC 27001:2022 | ✅ Applicable | ⚠️ SOA draft | 🎯 Q2 2027 | [ISO27001-ALIGNMENT.md](ISO27001-ALIGNMENT.md) |
| FW-002 | ISO/IEC 27017 (cloud security) | ✅ Applicable | ⚠️ Mapped via SOA | — | [readiness/ISO-FAMILY-READINESS.md](readiness/ISO-FAMILY-READINESS.md) |
| FW-003 | ISO/IEC 27018 (PII in public cloud) | ✅ Applicable | ⚠️ Mapped via SOA | — | readiness/ISO-FAMILY-READINESS |
| FW-004 | ISO/IEC 27701 (privacy extension) | ⚠️ Conditional | 📋 Readiness | 🎯 with 27001 | readiness/ISO-FAMILY-READINESS |
| FW-005 | ISO/IEC 42001 (AI MS) | ⚠️ Target | ✅ Programme | 🎯 2027 | [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md) |
| FW-006 | ISO 22301 (BCM) | ⚠️ Target | ✅ Programme | 🎯 drills | PROC-BCP-001, POL-OPS-003 |
| FW-007 | ISO 9001 (QMS) | ❌ N/A | — | — | QA via DEFSTAN 05-086 |
| FW-008 | ISO/IEC 20000 (ITSM) | ⚠️ Reference | 📋 Readiness | — | readiness/ISO-FAMILY-READINESS |
| FW-009 | ISO 14001 (environment) | ❌ N/A | 📋 Readiness | — | No EHS certification scope; monitor if facilities expand |
| FW-010 | ISO 45001 (OH&S) | ❌ N/A | 📋 Readiness | — | HR H&S policies; no cert scope |
| FW-011 | ISO 50001 (energy) | ❌ N/A | ❌ N/A | — | Cloud-hosted; no owned data centres |
| FW-012 | SNI ISO/IEC 27001 (Indonesia) | ❌ N/A | 📋 Readiness | — | readiness/ISO-FAMILY-READINESS |
| FW-013 | SNI ISO/IEC 27017 | ❌ N/A | 📋 Readiness | — | readiness/ISO-FAMILY-READINESS |
| FW-014 | SNI ISO/IEC 27018 | ❌ N/A | 📋 Readiness | — | readiness/ISO-FAMILY-READINESS |
| FW-015 | SNI ISO 9001 | ❌ N/A | 📋 Readiness | — | readiness/ISO-FAMILY-READINESS |
| FW-016 | K-ISMS (Korea) | ❌ N/A | 📋 Readiness | — | readiness/ISO-FAMILY-READINESS |

---

## 2. SOC, CSA, and assurance programmes

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-020 | SOC 2 Type II (TSC) | ✅ Applicable | ⚠️ Observation pending | 🎯 Q1 2027 | [SOC2-ALIGNMENT.md](SOC2-ALIGNMENT.md) |
| FW-021 | SOC 1 Type II | ❌ N/A | 📋 Readiness | — | No financial reporting controls service |
| FW-022 | SOC 3 | ⚠️ Conditional | 📋 Readiness | — | Publish after SOC 2 report available |
| FW-023 | CSA STAR (Level 1/2) | ⚠️ Conditional | 📋 Readiness | — | readiness/SOC-AND-ASSURANCE-READINESS |
| FW-024 | HITRUST CSF | ⚠️ Conditional | 📋 Readiness | — | Trigger: US healthcare enterprise RFP |
| FW-025 | KY3P (vendor risk) | ⚠️ Conditional | 📋 Readiness | — | Customer questionnaire platform |
| FW-026 | ProcessUnity | ⚠️ Conditional | 📋 Readiness | — | Customer GRC portal mapping |
| FW-027 | CyberVadis | ⚠️ Conditional | 📋 Readiness | — | Supplier assessment responses |
| FW-028 | Uptime Institute Tiers | ❌ N/A | ❌ N/A | — | We do not operate Tier-certified facilities |

---

## 3. PCI family

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-030 | PCI DSS v4.0 | ❌ N/A | ✅ Programme (position) | — | [PCI-DSS-POSITION.md](PCI-DSS-POSITION.md) |
| FW-031 | PCI 3-D Secure (3DS) | ❌ N/A | 📋 Readiness | — | [readiness/PCI-FAMILY-POSITION.md](readiness/PCI-FAMILY-POSITION.md) |
| FW-032 | PCI P2PE | ❌ N/A | ❌ N/A | — | No POI / CHD environment |
| FW-033 | PCI PIN | ❌ N/A | ❌ N/A | — | No PIN transaction processing |

---

## 4. NIST family

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-040 | NIST Cybersecurity Framework 2.0 | ⚠️ Reference | ✅ Programme | — | [NIST-CSF-ALIGNMENT.md](NIST-CSF-ALIGNMENT.md) |
| FW-041 | NIST SP 800-53 Rev 5 | ⚠️ Reference | 📋 Readiness | — | [readiness/NIST-FAMILY-READINESS.md](readiness/NIST-FAMILY-READINESS.md) |
| FW-042 | NIST SP 800-171 / 800-172 (CUI) | ❌ N/A | 📋 Readiness | — | readiness/NIST-FAMILY-READINESS |
| FW-043 | NIST SP 800-162 (ABAC) | ❌ N/A | 📋 Readiness | — | readiness/NIST-FAMILY-READINESS |
| FW-044 | NIST SP 800-34 (contingency) | ⚠️ Reference | ✅ Programme | — | PROC-BCP-001 maps contingency concepts |
| FW-045 | NIST SP 800-64 (security in SDLC) | ✅ Applicable | ✅ Programme | — | DEFSTAN + PROC-CHG-001 + CI gates |
| FW-046 | NIST Risk Management Framework | ⚠️ Reference | 📋 Readiness | — | readiness/NIST-FAMILY-READINESS |

---

## 5. US government and defence

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-050 | FedRAMP | ❌ N/A | ✅ Programme (future) | — | [FEDRAMP-READINESS.md](FEDRAMP-READINESS.md) |
| FW-051 | GovRAMP | ❌ N/A | 📋 Readiness | — | readiness/US-GOVERNMENT-READINESS |
| FW-052 | FISMA | ❌ N/A | 📋 Readiness | — | readiness/US-GOVERNMENT-READINESS |
| FW-053 | CMMC 2.0 | ❌ N/A | ✅ Programme (future) | — | [CMMC-READINESS.md](CMMC-READINESS.md) |
| FW-054 | DoD (general) | ❌ N/A | 📋 Readiness | — | readiness/US-GOVERNMENT-READINESS |
| FW-055 | DoD Impact Level 2 (IL2) | ❌ N/A | 📋 Readiness | — | readiness/US-GOVERNMENT-READINESS |
| FW-056 | DoD Impact Level 4 (IL4) | ❌ N/A | 📋 Readiness | — | readiness/US-GOVERNMENT-READINESS |
| FW-057 | DoD Impact Level 5 (IL5) | ❌ N/A | 📋 Readiness | — | readiness/US-GOVERNMENT-READINESS |
| FW-058 | DoD Impact Level 6 (IL6) | ❌ N/A | ❌ N/A | — | No classified workloads |
| FW-059 | DFARS / NIST 800-171 flow-down | ❌ N/A | 📋 Readiness | — | readiness/US-GOVERNMENT-READINESS |
| FW-060 | FIPS 140-3 (crypto modules) | ⚠️ Conditional | 📋 Readiness | — | Use FIPS-validated cloud primitives when required |
| FW-061 | CJIS Security Policy | ❌ N/A | 📋 Readiness | — | Trigger: US law enforcement data |
| FW-062 | HIPAA Security Rule | ⚠️ Conditional | ✅ Programme | 🎯 per customer | [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md) |
| FW-063 | FERPA | ❌ N/A | 📋 Readiness | — | Trigger: US education records processing |
| FW-064 | IRS Publication 1075 | ❌ N/A | 📋 Readiness | — | Trigger: federal tax information |
| FW-065 | SEC Rule 17a-4(f) | ❌ N/A | 📋 Readiness | — | Trigger: broker-dealer WORM retention |
| FW-066 | US CLOUD Act | ⚠️ Awareness | 📋 Readiness | — | Legal + DPA/SCC posture in GDPR alignment |
| FW-067 | US EAR (export) | ❌ N/A | 📋 Readiness | — | Standard crypto; no controlled tech export |
| FW-068 | US ITAR | ❌ N/A | ❌ N/A | — | No defence articles |
| FW-069 | VPAT / Section 508 | ⚠️ Conditional | 📋 Readiness | — | Trigger: US federal accessibility procurement |

---

## 6. International government and sector assurance

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-070 | IRAP (Australia) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-071 | ISMAP (Japan) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-072 | CSAP (Canada) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-073 | CCCS Medium Assessment (Canada) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-074 | CCCS PBHVA Assessment | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-075 | Canada RPAA | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-076 | UK Cyber Essentials Plus | ⚠️ Conditional | 📋 Readiness | 🎯 optional | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-077 | UK G-Cloud / Digital Marketplace | ⚠️ Conditional | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-078 | UK PASF | ⚠️ Conditional | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-079 | C5 (Germany BSI) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-080 | ENS High (Spain) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-081 | CCN CPSTIC (Spain) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-082 | CISPE Code of Conduct | ⚠️ Reference | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-083 | DESC CSP (Saudi) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-084 | ASIP HDS (France health hosting) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-085 | MeitY (India cloud empanelement) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-086 | MTCS (Singapore) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-087 | NISC Japan (cloud security) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-088 | TISAX (automotive) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-089 | NHS DSPT | ❌ N/A | ✅ Programme (future) | — | [NHS-DSPT-READINESS.md](NHS-DSPT-READINESS.md) |
| FW-090 | MPA (content security) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-091 | ABS OSPAR | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-092 | GNS (Germany) | ❌ N/A | 📋 Readiness | — | readiness/INTERNATIONAL-ASSURANCE-READINESS |
| FW-093 | Pinakes | ❌ N/A | 📋 Readiness | — | Customer assurance catalogue |
| FW-094 | PiTuKri | ❌ N/A | 📋 Readiness | — | Customer assurance catalogue |
| FW-095 | GSMA NESAS / SCAS | ❌ N/A | 📋 Readiness | — | readiness/INDUSTRY-SECTOR-READINESS |

---

## 7. EU financial and operational resilience

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-100 | DORA (Digital Operational Resilience Act) | ⚠️ Conditional | 📋 Readiness | — | readiness/INDUSTRY-SECTOR-READINESS |
| FW-101 | FINMA (Switzerland) | ❌ N/A | 📋 Readiness | — | readiness/INDUSTRY-SECTOR-READINESS |
| FW-102 | BIO Thema-uitwerking Clouddiensten (NL) | ❌ N/A | 📋 Readiness | — | readiness/INDUSTRY-SECTOR-READINESS |
| FW-103 | UAE IAR | ❌ N/A | 📋 Readiness | — | readiness/INDUSTRY-SECTOR-READINESS |
| FW-104 | FINTECH (sector programmes) | ❌ N/A | 📋 Readiness | — | [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md) supplier perimeter |
| FW-105 | Japan FISC | ❌ N/A | 📋 Readiness | — | readiness/INDUSTRY-SECTOR-READINESS |
| FW-106 | Japan Medical Information Guidelines | ❌ N/A | 📋 Readiness | — | readiness/INDUSTRY-SECTOR-READINESS |
| FW-107 | GxP (FDA 21 CFR Part 11 / EU Annex 11) | ❌ N/A | 📋 Readiness | — | Trigger: validated systems for life sciences |
| FW-108 | CE+ Framework | ⚠️ Reference | 📋 Readiness | — | UK cyber improvement programme reference |

---

## 8. AI security and technical standards

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-131 | ETSI EN 304 223 (Securing AI baseline) | ⚠️ Reference | ✅ Programme | — | [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md), [ETSI-EN-304-223-GAP-CHECKLIST.md](ETSI-EN-304-223-GAP-CHECKLIST.md) |
| FW-132 | OWASP AI Exchange | ✅ Applicable | ✅ Programme | — | [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md), PROC-AI-003 |

*Baseline evidence:* `compliance/execution_evidence_register.yaml` (EEV-003–008, PM-014).

---

## 9. Global privacy laws

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-110 | GDPR (EU/UK) | ✅ Applicable | ✅ Programme | — | [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md) |
| FW-111 | EU-U.S. Data Privacy Framework | ⚠️ Conditional | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-112 | CCPA / CPRA (California) | ⚠️ Conditional | ✅ Programme | — | [CCPA-CPRA-ALIGNMENT.md](CCPA-CPRA-ALIGNMENT.md) |
| FW-113 | Canada (PIPEDA / provincial) | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-114 | Australia Privacy Act | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-115 | Argentina (PDPA) | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-116 | Brazil LGPD | ❌ N/A | ✅ Programme (future) | — | [LGPD-READINESS.md](LGPD-READINESS.md) |
| FW-117 | Chile | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-118 | Mexico (LFPDPPP) | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-119 | Hong Kong PDPO | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-120 | India DPDP Act | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-121 | Indonesia PDP Law | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-122 | Japan APPI | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-123 | Korea PIPA | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-124 | Malaysia PDPA | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-125 | New Zealand Privacy Act | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-126 | Philippines DPA | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-127 | Singapore PDPA | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-128 | Taiwan PDPA | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-129 | Thailand PDPA | ❌ N/A | 📋 Readiness | — | readiness/GLOBAL-PRIVACY-READINESS |
| FW-130 | South Africa POPIA | ❌ N/A | ✅ Programme (future) | — | [POPIA-READINESS.md](POPIA-READINESS.md) |

---

## 10. Matrix-only and extended catalogue (FW-133–FW-145)

Frameworks previously referenced only in [REGULATION-MATRIX.md](REGULATION-MATRIX.md) or assurance matrices — now fully registered with proactive trigger wiring:

| FW-ID | Framework | Applicability | Programme | Cert 🎯 | Readiness doc |
|-------|-----------|---------------|-----------|---------|---------------|
| FW-133 | EU AI Act (2024/1689) | ✅ Applicable | ✅ Programme | — | [AI-GOVERNANCE.md](AI-GOVERNANCE.md) |
| FW-134 | UK PECR | ✅ Applicable | ✅ Programme | — | [PECR-ALIGNMENT.md](PECR-ALIGNMENT.md) |
| FW-135 | CIS Controls v8 | 📚 Reference | ✅ Programme | — | readiness/NIST-FAMILY-READINESS |
| FW-136 | OWASP Top 10 (2021) | ✅ Applicable | ✅ Programme | — | [REGULATION-MATRIX.md](REGULATION-MATRIX.md) |
| FW-137 | OWASP ASVS Level 2 | ⚠️ Conditional | ✅ Programme | — | [ASVS-GAP-CHECKLIST.md](ASVS-GAP-CHECKLIST.md) |
| FW-138 | NIST AI RMF 1.0 | ✅ Applicable | ✅ Programme | — | [AI-GOVERNANCE.md](AI-GOVERNANCE.md) |
| FW-139 | ITIL 4 | ✅ Applicable | ✅ Programme | — | [REGULATION-MATRIX.md](REGULATION-MATRIX.md) |
| FW-140 | PRINCE2 7 | ✅ Applicable | ✅ Programme | — | [REGULATION-MATRIX.md](REGULATION-MATRIX.md) |
| FW-141 | UK Research Integrity Concordat | 📚 Reference | ✅ Programme | — | [REGULATION-MATRIX.md](REGULATION-MATRIX.md) |
| FW-142 | ISO/IEC 27002:2022 | ✅ Applicable | ✅ Programme | — | readiness/ISO-FAMILY-READINESS |
| FW-143 | UK Companies Act 2006 (governance) | ✅ Applicable | ✅ Programme | — | [COMPANIES-ACT-ALIGNMENT.md](COMPANIES-ACT-ALIGNMENT.md) |
| FW-144 | OWASP GenAI / LLM Top 10 | ✅ Applicable | ✅ Programme | — | [AI-SECURITY-THREAT-MODEL.md](AI-SECURITY-THREAT-MODEL.md) |
| FW-145 | DEF STAN 05-138 (standalone) | ✅ Applicable | ✅ Programme | — | [DEFSTAN-ALIGNMENT.md](DEFSTAN-ALIGNMENT.md) |

**Not-applicable position statements:** [readiness/NOT-APPLICABLE-POSITION.md](readiness/NOT-APPLICABLE-POSITION.md) (FW-011, FW-028, FW-058, FW-068).

---

## 11. Summary statistics (2026-06-09)

| Category | Count | ✅ Programme | 📋 Readiness | ❌ N/A |
|----------|-------|-------------|-------------|--------|
| ISO / MS | 16 | 4 | 9 | 3 |
| SOC / assurance | 9 | 1 | 7 | 1 |
| PCI | 4 | 1 | 2 | 1 |
| NIST | 7 | 3 | 4 | 0 |
| US gov | 20 | 3 | 16 | 1 |
| Intl assurance | 26 | 1 | 24 | 1 |
| EU / industry | 9 | 0 | 9 | 0 |
| AI security | 2 | 2 | 0 | 0 |
| Privacy | 21 | 4 | 15 | 2 |
| **Total** | **127** | **49** | **67** | **7** |

*Partial programme (4): ISO 27001 family gaps, SOC 2 Type II, PCI DSS, Cyber Essentials Plus path. Vendor catalogues (KY3P, ProcessUnity, Pinakes, PiTuKri) are readiness-mapped for questionnaire response, not certification targets. Implementation wiring validated by MON-018 against `compliance/framework_implementation_catalog.yaml`.*

---

## 12. Layer activation guide

| Layer | What "started" means | Current state |
|-------|---------------------|---------------|
| **Layer 1** Tranc3 platform | Runtime controls, CI gates, registers in code | Operational in Tranc3 upstream |
| **Layer 2** Magna Carta programme | This register + policies + procedures + readiness groups | ✅ **Complete for catalogue** — PM-009 |
| **Layer 3** External validation | SOC report, ISO cert, signed BAAs, pen test, drills | Open: ACT-001–003, ACT-005–010, ACT-012; baselines ACT-004/011/013/014/015 closed |

---

## 12. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-09 | FW-131 (ETSI EN 304 223), FW-132 (OWASP AI Exchange); execution evidence cross-ref (PM-014) | ISMS Lead |
| 2026-06-08 | Master catalogue (FW-001–FW-130) + readiness index linkage | ISMS Lead |

**Next review:** 2026-09-06
