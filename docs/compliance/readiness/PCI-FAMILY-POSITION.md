# PCI Family — Position & Readiness

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead / DPO  
**Covers:** FW-030–FW-033  
**Extends:** [PCI-DSS-POSITION.md](../PCI-DSS-POSITION.md)

---

## 1. Executive position

Trancendos **does not store, process, or transmit cardholder data (CHD)** in environments under our control. Payment acceptance is delegated to **authorised payment service providers (PSPs)** per [SUPPLIER-DPA-REGISTER.md](../SUPPLIER-DPA-REGISTER.md) (SUP-003 and successors).

Therefore:

| Framework | Status | Justification |
|-----------|--------|---------------|
| PCI DSS (FW-030) | ❌ N/A — ✅ Programme position | SAQ A / outsourced model |
| PCI 3DS (FW-031) | ❌ N/A — 📋 Readiness | PSP handles 3DS; we do not operate 3DS Server |
| PCI P2PE (FW-032) | ❌ N/A | No point-of-interaction devices |
| PCI PIN (FW-033) | ❌ N/A | No PIN processing |

---

## 2. If scope changes

Re-assess immediately if any of the following occur:

1. Direct integration that passes PAN/CVV through Tranc3 APIs
2. Custom card form hosted on Trancendos domains
3. Storage of payment tokens outside PSP vault without AOC

**Action:** Open new risk in `risk_register.yaml`; engage QSA; scope PCI DSS assessment.

---

## 3. Programme controls that support PSP model

Even without PCI scope, these controls reduce payment fraud and support customer due diligence:

| Control | Artefact |
|---------|----------|
| PSP due diligence | Supplier DPA register, legal review |
| TLS / transport | POL-SEC-002, DEFSTAN |
| Access control | PROC-IAM-001 |
| Logging | Audit service, retention policy |
| Incident response | PROC-IR-001 |

---

## 4. Customer questionnaire guidance

When customers ask "Are you PCI compliant?":

> Trancendos does not operate a cardholder data environment. Payment processing is performed by PCI DSS compliant payment service providers under separate merchant agreements. We maintain security controls aligned with ISO 27001 and SOC 2 that support our role as a software provider.

Do **not** claim PCI DSS certification for Trancendos.

---

**Next review:** Annual or on architecture change
