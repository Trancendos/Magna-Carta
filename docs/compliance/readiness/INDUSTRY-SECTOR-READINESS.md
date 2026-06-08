# Industry & Sector — Readiness

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Covers:** FW-100–FW-108, FW-095 (GSMA), FW-104 (FINTECH)

---

## 1. EU financial services

### DORA (FW-100) — Digital Operational Resilience Act

| Pillar | Magna Carta baseline | Gap on trigger |
|--------|---------------------|----------------|
| ICT risk management | ISO 27001, risk register | Board ICT risk policy sign-off |
| Incident reporting | PROC-IR-001 | Financial regulator notification playbooks |
| Resilience testing | PROC-BCP-001, pen-test programme | TLPT participation if in scope |
| Third-party risk | Supplier DPA register | Critical ICT provider register (EU) |
| Information sharing | — | ISAC membership if required |

**Trigger:** Trancendos becomes **critical ICT third-party provider** to EU financial entity.

### FINMA (FW-101)

Swiss financial regulator circulars for outsourcing. **Trigger:** Swiss bank customer. Baseline: FCA-ALIGNMENT supplier discipline + ISO/SOC evidence.

---

## 2. Netherlands public sector

### BIO Thema-uitwerking Clouddiensten (FW-102)

Dutch government cloud implementation themes. **Trigger:** Dutch government contract. Map BIO themes to ISO 27001 + ENS-style controls.

---

## 3. Middle East

### UAE IAR (FW-103)

UAE Information Assurance Standards. **Trigger:** UAE government or regulated entity. Baseline: ISO 27001 + local data residency review.

---

## 4. Financial technology (FW-104)

Trancendos is **not FCA-authorised**. Programme covers **supplier/conduct perimeter**:

- [FCA-ALIGNMENT.md](../FCA-ALIGNMENT.md) — PRIN, COBS 4, PS21/3 consumer duty awareness
- MC-009 Magna Carta rules for financial promotions in product copy

**Re-assess** if regulated activities (payment services, advice) are introduced.

---

## 5. Japan sector

| FW-ID | Framework | Position |
|-------|-----------|----------|
| FW-105 | Japan FISC | 📋 Financial industry security guidelines — map to ISO + SOC |
| FW-106 | Japan Medical Information Guidelines | 📋 Trigger: Japanese healthcare data |
| FW-087 | NISC Japan | See [INTERNATIONAL-ASSURANCE-READINESS](INTERNATIONAL-ASSURANCE-READINESS.md) |

---

## 6. Life sciences (FW-107 GxP)

**GxP** (GCP, GLP, GMP) and **21 CFR Part 11 / EU Annex 11** for validated systems.

| Trigger | Required additions |
|---------|-------------------|
| Customer uses Tranc3 for GxP-regulated records | Validation plan (IQ/OQ/PQ), audit trail immutability evidence, change control under PROC-CHG-001 |

**Current position:** ❌ N/A — platform not marketed as validated GxP system. Document customer responsibility if used in ancillary workflows.

---

## 7. Telecommunications (FW-095 GSMA)

GSMA NESAS/SCAS for network equipment security. **N/A** for SaaS platform unless telecom network integration.

---

## 8. UK cyber improvement (FW-108 CE+)

CE+ (Cyber Essentials Plus extension framework) — reference for control maturity beyond CE baseline. Optional alignment with DEFSTAN and Cyber Essentials Plus path (FW-076).

---

## 9. Sector trigger register

Maintain in quarterly PROC-CMP-001 review:

| Sector | Owner | Watch signal |
|--------|-------|--------------|
| EU financial | Legal / ISMS | DORA ICT register inclusion |
| UK NHS | DPO | NHS contract or health data |
| US healthcare | DPO | BAA volume, HIPAA Tier C |
| Life sciences | Quality | GxP customer audit request |
| Automotive | Sales | TISAX questionnaire |

---

**Next review:** 2026-09-06
