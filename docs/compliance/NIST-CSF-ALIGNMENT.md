# NIST Cybersecurity Framework 2.0 — Reference Mapping

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Status:** ✅ Programme (reference mapping) — not a certification target

---

## 1. Purpose

Maps NIST CSF 2.0 functions to Tranc3 controls and Magna Carta artefacts for **customer security questionnaires** and **US public-sector conversations**. Primary assurance paths remain ISO 27001 and SOC 2.

---

## 2. Function summary

| Function | Implementation highlights | Evidence |
|----------|---------------------------|----------|
| **GOVERN** | Policies, RACI, risk register, AI governance | POL-SEC-001, RISK-REGISTER, FRAMEWORK |
| **IDENTIFY** | Asset inventory (workers), ROPA, risk assessment | AS-BUILT-ARCHITECTURE, ROPA |
| **PROTECT** | IAM, encryption, vault, SDLC gates | auth-service, vault, CI security |
| **DETECT** | Logging, monitoring, vuln scanning | Observatory, PROC-VUL-001 |
| **RESPOND** | Incident response | PROC-IR-001, WarRoom |
| **RECOVER** | BCP/DR | PROC-BCP-001, BCP-RESTORE-TEST-LOG |

---

## 3. CSF ↔ ISO 27001 relationship

Detailed control mapping lives in Tranc3 `ISO27001_SOA.md`. NIST CSF categories align to Annex A controls — use ISO SOA as authoritative implementation record.

---

## 4. Related documents

- [ISO27001-ALIGNMENT.md](ISO27001-ALIGNMENT.md)
- [SOC2-ALIGNMENT.md](SOC2-ALIGNMENT.md)
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
