# Privacy Bible

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** DPO  
**Classification:** Internal — privacy reference  
**Audience:** DPO, ISMS Lead, product owners, customer-facing teams

---

## 1. What this Bible is

Canonical reference for **privacy and data protection** across Trancendos — UK/EU GDPR, PECR, DSR handling, ROPA, and cross-border transfers. Complements [MAGNACARTA-GOVERNANCE-BIBLE.md](MAGNACARTA-GOVERNANCE-BIBLE.md) (governance cadence) and [FRAMEWORK.md](../../FRAMEWORK.md) (strategy).

**Honesty rule:** ✅ means programme artefact exists. Signed DPAs, ICO fee payment, and live consent UX are layer 3 (ACT-001, ACT-003).

---

## 2. Core policies and procedures

| Topic | Policy | Procedure | Cookbook | Hymn sheet |
|-------|--------|-----------|----------|------------|
| Data protection | POL-PRI-001 | PROC-DSR-001 | COOK-DSR-001 | HYMN-DSR-001 |
| Suppliers / DPAs | POL-SUP-001 | — | — | — |
| Training / attestation | — | PROC-TRN-001 | COOK-TRN-001 | HYMN-TRN-001 |

---

## 3. Registers and alignment

| Artefact | Path |
|----------|------|
| ROPA / processing | docs/compliance/ROPA.md |
| Legislation | docs/compliance/LEGISLATION-REGISTER.md |
| Obligations | docs/compliance/OBLIGATIONS-REGISTER.md |
| Suppliers (YAML) | compliance/supplier_dpa_register.yaml |
| ICO registration | docs/compliance/ICO-REGISTRATION.md |
| PECR programme | docs/compliance/PECR-ALIGNMENT.md |
| PECR deployment | docs/runbooks/RUN-PECR-001-Cookie-Deployment.md |
| CCPA readiness | docs/compliance/CCPA-CPRA-ALIGNMENT.md |
| HIPAA (customer BAA) | docs/compliance/HIPAA-ALIGNMENT.md |

---

## 4. Data subject rights flow

```
Request received → PROC-DSR-001 / COOK-DSR-001
    → Identity verification
    → 30-day response (extendable to 90)
    → Evidence in Town Hall / ticket
    → Unresolved complaint → OMB-002 (ICO) via RUN-OMB-001
```

Templates: [TEMPLATE-DPA-UK-GDPR.md](../templates/TEMPLATE-DPA-UK-GDPR.md), [TEMPLATE-SCC-ANNEX.md](../templates/TEMPLATE-SCC-ANNEX.md), [TEMPLATE-BAA-HIPAA.md](../templates/TEMPLATE-BAA-HIPAA.md)

---

## 5. PECR and cookies

| Control | Owner | Evidence |
|---------|-------|----------|
| Cookie inventory | DPO | Privacy notice annex |
| Consent before non-essential cookies | Product / Platform | RUN-PECR-001 |
| Marketing consent | Marketing / DPO | Consent records |

---

## 6. Breach and regulator engagement

| Event | Window | Procedure | Regulator |
|-------|--------|-----------|-----------|
| UK personal data breach (reportable) | 72h to ICO | PROC-IR-001 | REG-001 |
| HIPAA PHI breach | Per BAA | PROC-IR-001 | REG-007 |
| Data subject complaint escalation | Per SLA | PROC-DSR-001 | OMB-002 |

Runbook: [RUN-OMB-001-Ombudsman-Escalation.md](../runbooks/RUN-OMB-001-Ombudsman-Escalation.md)

---

## 7. Review cadence

| Activity | Frequency | Next |
|----------|-----------|------|
| ROPA update | Annual + on change | On processing change |
| Supplier DPA review | Quarterly | 2026-09-06 |
| PECR / cookie posture | Quarterly | 2026-09-06 |
| Legislation scan | Quarterly | PROC-CMP-001 |

**Next review:** 2026-09-06
