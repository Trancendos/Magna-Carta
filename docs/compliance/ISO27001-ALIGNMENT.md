# ISO 27001:2022 Alignment Summary

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Source of truth (detailed SOA):** [Tranc3 `docs/compliance/ISO27001_SOA.md`](https://github.com/Trancendos/Tranc3/blob/main/docs/compliance/ISO27001_SOA.md)  
**Certification target:** Q2 2027

---

## Scope statement

**ISMS scope:** Tranc3 platform — all self-hosted workers, infrastructure, data stores, CI/CD pipelines, and supporting observability systems operated by Trancendos Ltd.

**Exclusions:** Physical premises (cloud-hosted); customer-managed deployments outside Trancendos control.

---

## Implementation summary by clause

### Clause 5 — Organisational (37 controls)

| Status | Count | Key gaps |
|--------|-------|----------|
| ✅ Implemented | 12 | — |
| ⚠️ Partial / Planned | 22 | HR screening/training; MDM/DLP; external audit 🎯 |
| ❌ N/A | 3 | Physical asset return (cloud) |

**Magna Carta programme artefacts (Clause 5 gaps addressed in documentation):**
- POL-SEC-002 Acceptable Use Policy
- POL-OPS-003 Business Continuity Policy; PROC-BCP-001; [BCP-RESTORE-TEST-LOG.md](../evidence/BCP-RESTORE-TEST-LOG.md)
- POL-SUP-001 Supplier Management; [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md)
- PROC-IR-001 Incident Response Procedure
- [RACI-MATRIX.md](../governance/RACI-MATRIX.md); PROC-CHG-002 Post-Implementation Review

**Certification note:** Programme ✅ ≠ ISO 27001 certificate 🎯 Q2 2027.

### Clause 6 — People (8 controls)

| Status | Count | Key gaps |
|--------|-------|----------|
| ✅ Implemented | 2 | Remote working, event reporting |
| ⚠️ Partial / Planned | 6 | Screening, training, offboarding checklist |

### Clause 7 — Physical (14 controls)

**All N/A** — Justified: entirely cloud-hosted, remote workforce.

### Clause 8 — Technological (34 controls)

| Status | Count | Key highlights |
|--------|-------|----------------|
| ✅ Implemented | 18 | Auth, RBAC, logging, encryption, vuln mgmt, secure SDLC |
| ⚠️ Partial / Planned | 16 | MDM, DLP, HA, malware (Wazuh planned) |

---

## Statement of Applicability process

1. **Identify** controls from ISO 27001:2022 Annex A
2. **Assess** applicability to Tranc3 scope
3. **Map** to Tranc3 evidence (code, tests, docs)
4. **Gap** → Magna Carta policy/procedure or Tranc3 implementation
5. **Review** quarterly with DEFSTAN register

---

## Certification prerequisites

| Prerequisite | Status |
|--------------|--------|
| ISMS scope document | ✅ This doc + SOA |
| Risk assessment methodology | ✅ Risk register (Tranc3) |
| Risk treatment plan | ⚠️ Partial |
| Information security policy | ✅ POL-SEC-001 |
| Statement of Applicability | ✅ Draft in Tranc3 |
| Risk register | ✅ Tranc3 `RISK_REGISTER.md` |
| Internal audit programme | ⚠️ Planned Q4 2026 |
| Management review | ⚠️ Planned annual |
| Corrective action process | ⚠️ Via CAB + IR |
| Documented operating procedures | ✅ Nine procedures in this repo |
| External certification audit | 🎯 Q2 2027 |

---

## Magna Carta policy mapping

| ISO control area | Magna Carta policy |
|------------------|-------------------|
| 5.1 Policies | POL-SEC-001 |
| 5.10 AUP | POL-SEC-002 |
| 5.24–5.27 Incidents | POL-OPS-001, PROC-IR-001 |
| 5.29–5.30 BC/DR | POL-OPS-003, PROC-BCP-001 |
| 5.19–5.22 Suppliers | POL-SUP-001 |
| 5.34 Privacy | POL-PRI-001 |
| 8.x Technical | CONTROL-TO-COMPONENT-MAP |

**Detailed control-by-control SOA:** See Tranc3 repository (link above).
