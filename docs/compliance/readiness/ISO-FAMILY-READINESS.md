# ISO Family — Readiness & Mapping

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Covers:** FW-001–FW-016 in [STANDARDS-AND-FRAMEWORKS-REGISTER.md](../STANDARDS-AND-FRAMEWORKS-REGISTER.md)

---

## 1. Scope

Maps ISO/IEC and national ISO-derived management system standards to Magna Carta layer 2 artefacts. **Certification** requires external audit (layer 3).

---

## 2. Primary standards

### ISO/IEC 27001:2022 (FW-001) — 🎯 Q2 2027

| Control theme | Magna Carta artefact | Tranc3 evidence |
|---------------|---------------------|-----------------|
| ISMS scope & SOA | [ISO27001-ALIGNMENT.md](../ISO27001-ALIGNMENT.md), [RISK-TREATMENT-PLAN.md](../RISK-TREATMENT-PLAN.md) | `ISO27001_SOA.md` |
| Risk assessment | [RISK-REGISTER.md](../RISK-REGISTER.md), `compliance/risk_register.yaml` | Risk API |
| Access control | POL-SEC-001, PROC-IAM-001 | Auth service, RBAC |
| Cryptography | POL-SEC-002, DEFSTAN REQ-IA-002 | Cryptex, TLS |
| Supplier security | POL-SEC-004, [SUPPLIER-DPA-REGISTER.md](../SUPPLIER-DPA-REGISTER.md) | Supplier register |
| Incident / BC | POL-OPS-001, PROC-IR-001, PROC-BCP-001 | Incident templates |
| Internal audit | INTERNAL-AUDIT-PROGRAMME | ACT-011 |

**Gaps:** HR screening (PROC-HR-001 adoption), MDM/DLP (POL-SEC-003 deployment), management review session.

### ISO/IEC 27017 & 27018 (FW-002, FW-003)

Cloud-specific controls mapped through:

- Shared responsibility model in [SYSTEMS-REGISTER.md](../SYSTEMS-REGISTER.md)
- Subprocessor DPAs in `supplier_dpa_register.yaml`
- Encryption and logging controls shared with ISO 27001 SOA

**Position:** Implement as extensions to 27001 SOA; no separate certificate required unless customer mandates.

### ISO/IEC 27701 (FW-004)

Privacy Information Management System extension. Baseline from:

- [GDPR-ALIGNMENT.md](../GDPR-ALIGNMENT.md), POL-PRI-001, PROC-DSR-001
- ROPA and PIA processes in Tranc3

**Trigger:** Certify with 27001 if EU customers require PIMS attestation.

### ISO/IEC 42001 (FW-005) — 🎯 2027

| Theme | Artefact |
|-------|----------|
| AI policy | POL-AI-001, [AI-GOVERNANCE.md](../AI-GOVERNANCE.md) |
| Risk & impact | PROC-AI-001, PROC-AI-002, model cards |
| Maturity | [GENAI-MATURITY-ASSESSMENT.md](../GENAI-MATURITY-ASSESSMENT.md) |

### ISO 22301 (FW-006)

| Theme | Artefact |
|-------|----------|
| BC policy | POL-OPS-003 |
| BCP procedure | PROC-BCP-001 |
| Testing | [BCP-RESTORE-TEST-LOG.md](../../evidence/BCP-RESTORE-TEST-LOG.md) — ACT-012 |

---

## 3. Reference / N/A standards

| FW-ID | Standard | Position |
|-------|----------|----------|
| FW-007 | ISO 9001 | N/A — DEFSTAN 05-086 provides QA discipline |
| FW-008 | ISO 20000 | Mapped to ITIL 4 programme (Town Hall ITSM); formal cert not targeted |
| FW-009 | ISO 14001 | Monitor if physical office / hardware lifecycle expands |
| FW-010 | ISO 45001 | Workplace H&S via HR policies; no OHSMS cert |
| FW-011 | ISO 50001 | N/A — cloud provider energy responsibility |
| FW-012–015 | SNI (Indonesia) | Activate if Indonesia entity or data residency contract |
| FW-016 | K-ISMS | Activate if Korea public-sector or K-ISMS customer requirement |

---

## 4. Crosswalk to other frameworks

| ISO control domain | Also satisfies (partial) |
|------------------|-------------------------|
| 27001 Annex A | SOC 2 CC series, NIST 800-53 moderate baseline, FedRAMP moderate (future) |
| 27701 | GDPR Art. 5–32 programme evidence |
| 42001 | EU AI Act governance, NIST AI RMF |
| 22301 | NIST 800-34 contingency concepts |

---

**Next review:** 2026-09-06
