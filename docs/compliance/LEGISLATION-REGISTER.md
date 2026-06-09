# Legislation Register

**Version:** 1.1.0  
**Date:** 2026-06-08  
**Owner:** DPO / Legal  
**Review cycle:** Quarterly  
**Machine-readable:** [compliance/legislation_register.yaml](../../compliance/legislation_register.yaml)  
**EU citation guide:** [EUR-LEX-ELI-REFERENCE.md](EUR-LEX-ELI-REFERENCE.md)  
**EU monitoring:** [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md)

---

## Active legislation

| ID | Legislation | Jurisdiction | CELEX | ELI / UK URI | Applies to | Owner | Status | Next review |
|----|-------------|--------------|-------|--------------|------------|-------|--------|-------------|
| LEG-001 | UK GDPR | UK | — | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2018/12/contents) | All PII processing | DPO | ✅ Compliant | 2026-09-06 |
| LEG-002 | Data Protection Act 2018 | UK | — | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2018/12/contents) | All PII processing | DPO | ✅ Compliant | 2026-09-06 |
| LEG-003 | EU GDPR | EU | 32016R0679 | [eli/reg/2016/679/oj/eng](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | EU data subjects | DPO | ✅ Compliant | 2026-09-06 |
| LEG-004 | Computer Misuse Act 1990 | UK | — | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/1990/18/contents) | Platform security | CISO | ✅ Compliant | 2026-09-06 |
| LEG-005 | UK PECR | UK | — | [legislation.gov.uk](https://www.legislation.gov.uk/uksi/2003/2426/contents) | Electronic marketing | DPO | ✅ Programme | 2026-09-06 |
| LEG-006 | EU AI Act | EU | 32024R1689 | [eli/reg/2024/1689/oj/eng](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) | AI system deployment | AI Lead | ✅ Programme | 2026-09-06 |
| LEG-007 | Copyright, Designs and Patents Act 1988 | UK | — | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/1988/48/contents) | Software/IP | Legal | ✅ Compliant | 2026-09-06 |
| LEG-008 | Companies Act 2006 | UK | — | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2006/46/contents) | Corporate governance | Finance | ✅ Programme | 2026-09-06 |
| LEG-009 | HIPAA (US) | US | — | HHS/OCR guidance | PHI when BAA-scoped | DPO / CISO | ✅ Programme | 2026-09-06 |
| LEG-010 | FCA Handbook (PRIN, COBS, PS21/3) | UK | — | FCA handbook | Financial conduct as supplier | Legal / ISMS | ✅ Programme | 2026-09-06 |

**EU acts:** CELEX and ELI URIs are authoritative for citation and change tracking. Article-level anchors for LEG-006 are in `legislation_register.yaml` → `article_anchors` and [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §3.

---

## Watch list

| WATCH-ID | Legislation | Jurisdiction | CELEX / URI | Potential impact | Monitor from |
|----------|-------------|--------------|-------------|------------------|--------------|
| WATCH-001 | Online Safety Act 2023 | UK | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2023/50/contents) | User-generated content if enabled | 2026-09-06 |
| WATCH-002 | Digital Markets, Competition and Consumers Act 2024 | UK | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2024/13/contents) | Consumer AI services | 2026-09-06 |
| WATCH-003 | EU Data Act | EU | [32023R2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng) | Data portability, IoT | 2026-09-06 |
| WATCH-004 | NIS2 Directive | EU | [32022L2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng) | Critical digital infrastructure | 2026-09-06 |
| WATCH-005 | DORA | EU | [32022R2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng) | ICT third-party risk (financial customers) | 2026-09-06 |
| WATCH-006 | CCPA / CPRA | California | — | US state privacy | If US expansion |

**EU secondary legislation** (delegated/implementing acts under LEG-006): tracked in `legislation_register.yaml` → `secondary_legislation_watch` and [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md); first operational scan 🎯 ACT-014.

**EU harmonised technical standards** (CEN/CENELEC JTC21 under LEG-006): tracked in `compliance/standards_watch.yaml` and [HARMONISED-STANDARDS-MONITORING.md](HARMONISED-STANDARDS-MONITORING.md); ETSI EN 304 223 reference alignment in [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md); first operational watch 🎯 ACT-015.

---

## Regulatory contacts

> **Extended register:** Supervisory authorities, sector regulators, and ombudsmen are maintained in [REGULATORS-OMBUDSMEN-REGISTER.md](REGULATORS-OMBUDSMEN-REGISTER.md). This section retains legislation-to-authority quick reference only.

| Authority | Contact purpose | Status |
|-----------|-----------------|--------|
| ICO (UK) | Data protection registration, breach notification | ✅ Programme — fee payment 🎯 |
| DSIT / AI Office | AI Act conformity | Monitor |
| FCA | Financial promotions, supplier resilience (if serving regulated firms) | Advisory / engagement as needed |
| NCSC (UK) | Security guidance | Advisory only |

---

## Contractual obligations

| Contract type | Requirement | Register location |
|---------------|-------------|-------------------|
| Customer SLA | Availability, support response | Per customer agreement |
| Supplier DPA | Art. 28 GDPR processor terms | [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md), `compliance/supplier_dpa_register.yaml` |
| Employee / contractor | Confidentiality, data handling | HR files |

---

## Obligations register

Statutory and contractual obligations are tracked in detail in [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md), including EUR-Lex source links for EU obligations, monitoring cadence, evidence owners, and regulatory change log.

**Next full review:** 2026-09-06
