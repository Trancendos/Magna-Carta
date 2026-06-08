# Supplier & DPA Register

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** DPO / Procurement  
**Policy:** [POL-SUP-001](../policies/POL-SUP-001-Supplier-Management.md)  
**Machine-readable source:** [compliance/supplier_dpa_register.yaml](../../compliance/supplier_dpa_register.yaml)

---

## 1. Purpose

Tracks third-party suppliers that process personal data on behalf of Trancendos or Tranc3 customers, satisfying:

- UK GDPR Art. 28 processor agreements (**OBL-003**)
- Supplier DPA contractual terms (**OBL-081**)
- HIPAA BAA requirements where US PHI is in scope (see [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md))

**Programme status:** ✅ Register and onboarding checklist implemented. Individual **signed** DPAs remain per-supplier legal execution (🎯 external validation where not yet signed).

---

## 2. Register summary

| SUP-ID | Supplier | Risk | DPA status | Transfer | Next review |
|--------|----------|------|------------|----------|-------------|
| SUP-001 | Self-hosted Tranc3 | Critical | N/A (first-party) | N/A | 2026-09-06 |
| SUP-002 | Forgejo (self-hosted) | High | Not required | N/A | 2026-09-06 |
| SUP-003 | Authorised PSP | Critical | Template issued | UK IDTA | 2026-09-06 |
| SUP-004 | Optional US AI fallback | High | In negotiation | SCCs | 2026-09-06 |
| SUP-005 | Health connectors (Sync-Bot) | Critical | Template issued | SCCs / BAA | 2026-09-06 |

Full detail: `compliance/supplier_dpa_register.yaml`.

---

## 3. DPA template requirements (Art. 28)

All processor DPAs must include:

| Clause | Requirement |
|--------|-------------|
| Subject matter & duration | Scope of processing and contract term |
| Nature and purpose | Service description aligned to ROPA |
| Personal data types | Categories per ROPA |
| Data subject categories | Users, employees, customers as applicable |
| Controller instructions | Documented in order form / SOW |
| Confidentiality | Personnel confidentiality obligations |
| Security | Art. 32 measures (reference POL-SEC-001) |
| Sub-processors | Prior notice / general authorisation with objection right |
| Data subject rights | Assistance with DSRs (PROC-DSR-001) |
| Breach notification | Without undue delay; PROC-IR-001 |
| Deletion/return | End of contract data handling |
| Audit rights | Reasonable audit / SOC 2 / ISO evidence |
| International transfers | IDTA or SCCs with TIA where required |

**Template location:** Legal / Town Hall document store (execute per customer and supplier).

---

## 4. Onboarding workflow

```
Identify supplier → Risk tier → Security evidence → DPA/BAA draft → Legal sign-off
       → ROPA update → Sub-processor disclosure → Register row → Annual review
```

See onboarding checklist in `supplier_dpa_register.yaml`.

---

## 5. Monitoring vs signing

| Activity | Owner | Cadence |
|----------|-------|---------|
| Register accuracy | DPO | Quarterly (PROC-CMP-001) |
| Critical supplier review | ISMS + Procurement | Annual |
| DPA execution (new supplier) | Legal | Per onboarding |
| Sub-processor change notification | DPO | Within 30 days of change |

---

## 6. Related documents

- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md) — OBL-003, OBL-081
- [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md)
- [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md) — BAA tier
- [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md) — PSP authorisation
- [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md)

**Next review:** 2026-09-06
