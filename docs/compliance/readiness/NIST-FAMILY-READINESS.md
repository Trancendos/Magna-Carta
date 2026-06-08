# NIST Family — Readiness & Mapping

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Covers:** FW-040–FW-046

---

## 1. Overview

NIST publications inform **US federal**, **defence (CMMC/CUI)**, and **enterprise questionnaire** responses. Magna Carta maps functionally to NIST without claiming NIST assessment completion unless contracted.

---

## 2. Framework-by-framework

### NIST CSF 2.0 (FW-040) — ✅ Programme

Primary customer-facing mapping: [NIST-CSF-ALIGNMENT.md](../NIST-CSF-ALIGNMENT.md)

| Function | Magna Carta examples |
|----------|-------------------|
| Govern (GV) | FRAMEWORK.md, policies, risk register |
| Identify (ID) | ROPA, asset/SYSTEMS-REGISTER, supplier register |
| Protect (PR) | IAM, encryption, endpoint policy |
| Detect (DE) | Logging, audit service, vuln scanning |
| Respond (RS) | PROC-IR-001 |
| Recover (RC) | PROC-BCP-001 |

### NIST SP 800-53 Rev 5 (FW-041)

**Reference baseline** for FedRAMP and FISMA. Control mapping:

- Moderate baseline ↔ ISO 27001 SOA (gap table in FEDRAMP-READINESS)
- Use when responding to US agency security plans

**Layer 3:** SSP, POA&M, continuous monitoring — not authored until FedRAMP path.

### NIST SP 800-171 / 800-172 (FW-042)

Required for **CUI** under CMMC. Mapped in [CMMC-READINESS.md](../CMMC-READINESS.md).

| Priority | Gap examples |
|----------|--------------|
| P1 | MFA everywhere, encryption at rest audit |
| P2 | Media sanitization procedure formalisation |

### NIST SP 800-162 ABAC (FW-043)

Attribute-based access control reference. Tranc3 RBAC today; ABAC extensions documented in architecture roadmap if multi-tenant attribute policies required.

### NIST SP 800-34 Contingency Planning (FW-044) — ✅ Programme

| 800-34 concept | Magna Carta |
|----------------|-------------|
| BIA | RISK-REGISTER, BCP scope in POL-OPS-003 |
| Contingency plan | PROC-BCP-001 |
| Testing | BCP-RESTORE-TEST-LOG — ACT-012 |

### NIST SP 800-64 Security in SDLC (FW-045) — ✅ Programme

| Practice | Evidence |
|----------|----------|
| Secure development | DEFSTAN REQ-CM-*, CI gates |
| Change control | PROC-CHG-001, CAB |
| Vulnerability management | PROC-VUL-001 |
| Penetration testing | PEN-TEST-PROGRAMME — ACT-005 |

### NIST Risk Management Framework (FW-046)

RMF steps (Categorize → Monitor) apply when pursuing federal ATO. **Position:** Documented as FedRAMP/CMMC dependency; RMF package not built until sponsor engaged.

---

## 3. Recommended use in sales / audit

| Audience | Lead with | Supplement with |
|----------|-----------|-----------------|
| US enterprise | NIST CSF 2.0 self-assessment | SOC 2 bridge letter |
| US federal | 800-53 moderate mapping | FedRAMP readiness doc |
| Defence supply chain | 800-171 + CMMC readiness | ISO 27001 SOA |

---

**Next review:** 2026-09-06
