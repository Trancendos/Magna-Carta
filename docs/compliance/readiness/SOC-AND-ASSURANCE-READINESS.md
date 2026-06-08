# SOC & Assurance Programmes — Readiness

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Covers:** FW-020–FW-028

---

## 1. SOC reports (FW-020–FW-022)

### SOC 2 Type II (FW-020) — primary assurance target 🎯 Q1 2027

| TSC category | Magna Carta coverage | Evidence schedule |
|--------------|---------------------|-------------------|
| Security (CC) | POL-SEC-*, PROC-VUL-001, DEFSTAN | [SOC2-EVIDENCE-SCHEDULE.md](../SOC2-EVIDENCE-SCHEDULE.md) |
| Availability (A) | PROC-BCP-001, SLA monitoring | BCP log, uptime metrics |
| Confidentiality (C) | Encryption, access control | Cryptex, IAM |
| Processing integrity (PI) | Change control, validation | PROC-CHG-001, CI |
| Privacy (P) | GDPR programme | GDPR-ALIGNMENT, DSR procedure |

**Status:** Observation period starts ACT-008 (2026-10-01). Programme ✅; report is layer 3.

### SOC 1 (FW-021)

**N/A** — Trancendos does not provide services that affect customers' financial statement internal controls (no payroll/benefits processing as a service).

### SOC 3 (FW-022)

**Conditional** — Public-facing trust report derived from SOC 2 after Type II completion. Prepare summary for website/trust centre.

---

## 2. Cloud assurance (FW-023 CSA STAR)

| Level | Requirement | Our position |
|-------|-------------|--------------|
| STAR Level 1 | CAIQ self-assessment | 📋 Map CAIQ to SOC 2 + ISO SOA when US enterprise customers request |
| STAR Level 2 | Third-party attestation | Follows SOC 2 / ISO cert path |

**Trigger:** Enterprise cloud RFP listing CSA STAR.

---

## 3. Healthcare assurance (FW-024 HITRUST)

HITRUST CSF consolidates HIPAA, NIST, ISO, and PCI controls.

| Approach | Artefact |
|----------|----------|
| Baseline | [HIPAA-ALIGNMENT.md](../HIPAA-ALIGNMENT.md) |
| Security | ISO 27001 SOA, SOC 2 CC |
| i1 / r2 validified assessment | Layer 3 — trigger: US health system procurement |

**Honest status:** Programme readiness via HIPAA + ISO mapping; HITRUST validified assessment not started.

---

## 4. Vendor risk platforms (FW-025–FW-027, FW-093–FW-094)

| Platform | Use | Magna Carta response source |
|----------|-----|---------------------------|
| KY3P | Bank/vendor DDQ | SOC 2 report, ISO SOA, policies index |
| ProcessUnity | GRC questionnaires | [COMPLIANCE-BLUEPRINT.md](../COMPLIANCE-BLUEPRINT.md) pack |
| CyberVadis | ESG/security rating | Supplier security policy, pen-test programme |
| Pinakes / PiTuKri | Customer catalogues | This readiness set + STANDARDS-AND-FRAMEWORKS-REGISTER |

**Process:** Maintain **trust pack** folder (policies, SOC bridge letter, architecture summary) for export to these portals — owner ISMS Lead.

---

## 5. Uptime Institute Tiers (FW-028)

**N/A** — Trancendos does not design or operate customer-facing data centre facilities. Infrastructure is cloud-hosted (provider Tier certifications apply to hyperscaler, not Trancendos).

---

**Next review:** 2026-09-06
