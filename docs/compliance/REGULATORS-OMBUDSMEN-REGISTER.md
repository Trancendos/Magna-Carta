# Regulators and Ombudsmen Register

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** DPO / Legal  
**Review cycle:** Quarterly  
**Purpose:** Supervisory authorities, regulators, and ombudsman schemes relevant to Trancendos operations — engagement rules, escalation paths, and monitoring.

---

## 1. Regulators (supervisory authorities)

| REG-ID | Authority | Jurisdiction | Scope for Trancendos | Engagement type | Contact / portal | Status |
|--------|-----------|--------------|----------------------|-----------------|------------------|--------|
| REG-001 | **ICO** (Information Commissioner's Office) | UK | UK GDPR, PECR, breach notification | Registration, guidance, breach report | [ico.org.uk](https://ico.org.uk) | ✅ Programme — fee payment 🎯 (ACT-003) |
| REG-002 | **EU DPAs** (lead supervisory authority TBD) | EU | EU GDPR for EU data subjects | Cooperation, DPIA consultation | [EUR-Lex CELEX 32016R0679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | Monitor — establish on EU entity |
| REG-003 | **DSIT / EU AI Office** | UK / EU | AI Act conformity, GPAI | Future conformity assessment | [EUR-Lex CELEX 32024R1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng); [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md) | ✅ Programme — UK-AI-LEGISLATION-MONITORING + ACT-014 |
| REG-004 | **FCA** (Financial Conduct Authority) | UK | Supplier to regulated firms; not authorised | Advisory if serving FCA-regulated customers | [fca.org.uk](https://www.fca.org.uk) | ✅ Programme — FCA-ALIGNMENT |
| REG-005 | **NCSC** (National Cyber Security Centre) | UK | Security guidance, incident coordination | Advisory, CiSP optional | [ncsc.gov.uk](https://www.ncsc.gov.uk) | Advisory only |
| REG-006 | **CMA** (Competition and Markets Authority) | UK | Consumer protection, digital markets | Monitor DMA / DMC Act | Monitor | Watch list |
| REG-007 | **HHS OCR** (US) | US | HIPAA enforcement (when BAA in scope) | Breach notification, investigations | [hhs.gov/hipaa](https://www.hhs.gov/hipaa) | ✅ Programme — per-customer BAA 🎯 |
| REG-008 | **California CPPA** | US-CA | CCPA/CPRA if CA users material | Registration, privacy rights | [cppa.ca.gov](https://cppa.ca.gov) | 📋 Readiness — CCPA-CPRA-ALIGNMENT |
| REG-009 | **ANPD** (Brazil) | BR | LGPD if BR operations | DPO registration, sanctions | Monitor | Future — LGPD-READINESS |
| REG-010 | **Information Regulator** (SA) | ZA | POPIA if ZA operations | Enforcement | Monitor | Future — POPIA-READINESS |

---

## 2. Ombudsmen and dispute resolution

| OMB-ID | Scheme | Jurisdiction | Applies when | Escalation path | Status |
|--------|--------|--------------|--------------|-----------------|--------|
| OMB-001 | **Financial Ombudsman Service (FOS)** | UK | Customer complaint about financial service *if* Trancendos becomes FCA-authorised or payment institution | Customer → internal complaints → FOS | N/A today — monitor if regulated activities |
| OMB-002 | **ICO** (complaints function) | UK | Data subject unsatisfied with DPO response | PROC-DSR-001 → ICO complaint | ✅ Programme |
| OMB-003 | **EU ODR platform** | EU | Online dispute resolution for EU consumers | EU ODR link in terms if B2C EU | Monitor on EU B2C launch |
| OMB-004 | **Civil courts** (England & Wales) | UK | Contract / tort disputes | Legal → litigation | Standard commercial |
| OMB-005 | **Advertising Standards Authority (ASA)** | UK | Misleading marketing claims | CAP Code complaints | Monitor if paid advertising scale |

---

## 3. Engagement rules

| Scenario | Notify within | Owner | Procedure |
|----------|---------------|-------|-----------|
| Personal data breach (UK) — reportable to ICO | 72 hours of awareness | DPO | PROC-IR-001 |
| HIPAA breach (US PHI) | Per BAA / 60 days | DPO | PROC-IR-001, HIPAA-ALIGNMENT |
| Regulatory inquiry letter | 24 hours internal escalation | Legal | Legal playbook (external) |
| Customer complaint (financial) | Per SLA / FCA DISP if in scope | Customer Success | — |

---

## 4. Monitoring cadence

| Activity | Frequency | Owner | Artefact |
|----------|-----------|-------|----------|
| Legislation register scan | Quarterly | DPO | LEGISLATION-REGISTER.md |
| UK AI Bill / EU AI Act updates | Quarterly | AI Lead | UK-AI-LEGISLATION-MONITORING |
| ICO registration renewal | Annual | DPO | ICO-REGISTRATION.md |
| Regulator contact verification | Annual | Legal | This register |

Automated reminders: `compliance/maintenance_monitor.yaml` → `scripts/compliance_health_check.py`

---

## 5. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-07 | Initial register — regulators from LEGISLATION-REGISTER + ombudsmen | DPO |

**Next review:** 2026-09-06

**Related:** [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md) · [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)
