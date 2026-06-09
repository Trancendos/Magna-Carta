# Standards Register

**Version:** 2.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Review cycle:** Quarterly (PROC-CMP-001)  
**Purpose:** Curated list of standards actively adopted or targeted by Magna Carta (STD-IDs). For the full customer-requested catalogue (112 frameworks, FW-001–FW-130), see [STANDARDS-AND-FRAMEWORKS-REGISTER.md](STANDARDS-AND-FRAMEWORKS-REGISTER.md) and `compliance/frameworks_register.yaml`.

---

## 1. How to use this register

- **Adopted** — we claim alignment and maintain a mapping doc in `docs/compliance/`
- **Mapped** — reference for customer questionnaires; no certification claim
- **Target** — roadmap item with owner and date
- **Monitor** — watch for applicability change

Status symbols match [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md): ✅ Programme ≠ certified.

---

## 2. Information security and assurance

| STD-ID | Standard | Edition | Status | Mapping doc | Certification / validation |
|--------|----------|---------|--------|-------------|---------------------------|
| STD-001 | ISO/IEC 27001 | 2022 | Target 🎯 | [ISO27001-ALIGNMENT.md](ISO27001-ALIGNMENT.md) | External audit Q2 2027 |
| STD-002 | ISO/IEC 27002 | 2022 | Mapped | ISO27001-ALIGNMENT | Control implementation via SOA |
| STD-003 | SOC 2 | TSC 2017 | Target 🎯 | [SOC2-ALIGNMENT.md](SOC2-ALIGNMENT.md) | Type II observation from 2026-10 |
| STD-004 | DEF STAN 05-138 | Current | Adopted ✅ | [DEFSTAN-ALIGNMENT.md](DEFSTAN-ALIGNMENT.md) | CI gate in Tranc3 |
| STD-005 | NIST Cybersecurity Framework | 2.0 | Mapped | [NIST-CSF-ALIGNMENT.md](NIST-CSF-ALIGNMENT.md) | Self-assessment |
| STD-006 | CIS Controls | v8 | Partial ⚠️ | REGULATION-MATRIX | MDM/DLP gap |
| STD-007 | OWASP Top 10 | 2021 | Adopted ✅ | REGULATION-MATRIX, PROC-VUL-001 | CI + pen test programme |
| STD-008 | OWASP ASVS | L2 | Partial ⚠️ | — | Optional gap assessment |
| STD-009 | PCI DSS | 4.0 | N/A | [PCI-DSS-POSITION.md](PCI-DSS-POSITION.md) | No CHD environment |
| STD-010 | FedRAMP | — | Future | [FEDRAMP-READINESS.md](FEDRAMP-READINESS.md) | Trigger: US gov RFP |
| STD-011 | CMMC | 2.0 | Future | [CMMC-READINESS.md](CMMC-READINESS.md) | Trigger: DoD CUI |

---

## 3. Privacy and data protection

| STD-ID | Standard / framework | Status | Mapping doc |
|--------|------------------------|--------|-------------|
| STD-020 | UK GDPR / EU GDPR | Adopted ✅ | [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md) |
| STD-021 | UK PECR | Programme ✅ | [PECR-ALIGNMENT.md](PECR-ALIGNMENT.md) |
| STD-022 | HIPAA Security Rule | Programme ✅ | [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md) |
| STD-023 | CCPA / CPRA | Readiness ✅ | [CCPA-CPRA-ALIGNMENT.md](CCPA-CPRA-ALIGNMENT.md) |
| STD-024 | LGPD | Future ✅ | [LGPD-READINESS.md](LGPD-READINESS.md) |
| STD-025 | POPIA | Future ✅ | [POPIA-READINESS.md](POPIA-READINESS.md) |
| STD-026 | NHS DSPT | Future ✅ | [NHS-DSPT-READINESS.md](NHS-DSPT-READINESS.md) |

---

## 4. AI, quality, and continuity

| STD-ID | Standard | Status | Mapping doc |
|--------|----------|--------|-------------|
| STD-030 | EU AI Act | Programme ✅ | [AI-GOVERNANCE.md](AI-GOVERNANCE.md) |
| STD-031 | ISO/IEC 42001 | Target 🎯 | GENAI-MATURITY-ASSESSMENT |
| STD-032 | NIST AI RMF | Mapped ✅ | AI-GOVERNANCE.md |
| STD-033 | ISO 22301 (BCM) | Target 🎯 | PROC-BCP-001, POL-OPS-003 |
| STD-034 | ISO 9001 | N/A | DEFSTAN substitutes for QA |
| STD-035 | ITIL 4 | Programme ✅ | Town Hall ITSM |
| STD-036 | PRINCE2 7 | Programme ✅ | BoardRoom stage gates |
| STD-037 | OWASP AI Exchange | Adopted ✅ | [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md) |
| STD-038 | OWASP GenAI / LLM Top 10 | Mapped ✅ | OWASP-AI-EXCHANGE-ALIGNMENT, PEN-TEST-FUTURE-SCOPE-ANNEX §5 |
| STD-039 | EUR-Lex / ELI legislative monitoring | Programme ✅ | [EUR-LEX-ELI-REFERENCE.md](EUR-LEX-ELI-REFERENCE.md), [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md), `compliance/legislation_register.yaml` |

---

## 5. Sector and research

| STD-ID | Standard | Status | Mapping doc |
|--------|----------|--------|-------------|
| STD-040 | FCA Handbook (supplier perimeter) | Programme ✅ | [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md) |
| STD-041 | UK Research Data Concordat | Future ✅ | [RESEARCH-DATA-CONCORDAT-ANNEX.md](RESEARCH-DATA-CONCORDAT-ANNEX.md) |

---

## 6. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-08 | STD-039 — EUR-Lex / ELI monitoring standard; legislation_register.yaml (PM-012) | ISMS Lead |
| 2026-06-08 | STD-037/038 — OWASP AI Exchange + GenAI LLM Top 10 mapping (PM-011) | ISMS Lead |
| 2026-06-08 | v2.0 — cross-reference to master FW catalogue (PM-009) | ISMS Lead |
| 2026-06-07 | Initial standards register (artifact model wave) | ISMS Lead |

**Next review:** 2026-09-06 (PROC-CMP-001)
