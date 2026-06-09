# Security Bible

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Classification:** Internal — security reference  
**Audience:** Security Ops, Platform Engineering, auditors

---

## 1. What this Bible is

Canonical reference for **information security operations** — access control, vulnerability management, incident response, BCP, and secure engineering. Strategic context: [FRAMEWORK.md](../../FRAMEWORK.md); governance cadence: [MAGNACARTA-GOVERNANCE-BIBLE.md](MAGNACARTA-GOVERNANCE-BIBLE.md).

**Honesty rule:** ✅ = programme artefact. Pen tests, restore drills, and SOC 2 observation are layer 3 (ACT-005, ACT-012).

---

## 2. Security policies

| ID | Title | Focus |
|----|-------|-------|
| POL-SEC-001 | Information Security | ISMS scope, roles |
| POL-SEC-002 | Access Control | Least privilege, MFA |
| POL-SEC-003 | Endpoint & Data Protection | Device and data handling |

---

## 3. Procedures and playbooks

| Domain | Procedure | Cookbook | Hymn sheet |
|--------|-----------|----------|------------|
| Incidents | PROC-IR-001 | COOK-IR-001 | HYMN-IR-001 |
| Access | PROC-IAM-001 | COOK-IAM-001 | HYMN-IAM-001 |
| Vulnerabilities | PROC-VUL-001 | COOK-VUL-001 | HYMN-VUL-001 |
| Change | PROC-CHG-001, PROC-CHG-002 | COOK-CHG-001, COOK-CHG-002 | HYMN-CHG-001, HYMN-CHG-002 |
| BCP / restore | PROC-BCP-001 | COOK-BCP-001 | HYMN-BCP-001 |
| CAPA | PROC-CAPA-001 | COOK-CAPA-001 | HYMN-CAPA-001 |
| HR lifecycle | PROC-HR-001 | COOK-HR-001 | HYMN-HR-001 |
| AI security | PROC-AI-003 | COOK-AI-003 | HYMN-AI-003 |

---

## 4. Standards and assessments

| Standard | Register | Assessment artefact |
|----------|----------|-------------------|
| ISO 27001 | STANDARDS-REGISTER STD-001 | ISO27001-ALIGNMENT.md |
| OWASP Top 10 | STD-007 | PROC-VUL-001, pen-test programme |
| OWASP ASVS L2 | STD-008 | [ASVS-GAP-CHECKLIST.md](../compliance/ASVS-GAP-CHECKLIST.md) |
| OWASP AI Exchange | STD-037 | [OWASP-AI-EXCHANGE-ALIGNMENT.md](../compliance/OWASP-AI-EXCHANGE-ALIGNMENT.md), [AI-SECURITY-THREAT-MODEL.md](../compliance/AI-SECURITY-THREAT-MODEL.md) |
| OWASP GenAI LLM Top 10 | STD-038 | PT-AI scope; PROC-AI-003 |
| DEFSTAN (Tranc3) | Tranc3 register | CI gate SYS-033 |

---

## 5. Systems (security-critical)

See [SYSTEMS-REGISTER.md](../compliance/SYSTEMS-REGISTER.md) — P0: SYS-001 (Traefik), SYS-002 (auth), SYS-003 (Nexus), SYS-005 (vault).

| Capability | System | Control |
|------------|--------|---------|
| Secrets | SYS-005 | Rotation, access audit |
| Audit logs | SYS-006 | Immutable retention |
| Monitoring | SYS-030–032 | Alerting to Security Ops |
| Compliance gate | SYS-033, SYS-034 | DEFSTAN + Magna Carta checker |

---

## 6. Incident severity model

| Severity | Examples | Response |
|----------|----------|----------|
| P1 | Active breach, auth compromise, P0 outage | COOK-IR-001 within 15 min |
| P2 | Contained vuln, partial degradation | PROC-IR-001 standard track |
| P3 | Low impact, informational | Ticket + weekly review |

---

## 7. Assurance calendar

| Activity | Frequency | Evidence |
|----------|-----------|----------|
| Access review | Quarterly | PROC-IAM-001 |
| Vulnerability scan / triage | Continuous + weekly | PROC-VUL-001 |
| Penetration test | Annual | PEN-TEST-LOG.md (ACT-005) |
| BCP restore drill | Semi-annual | BCP-RESTORE-TEST-LOG.md |
| ASVS gap review | Annual | ASVS-GAP-CHECKLIST.md |
| AI security threat assessment | Annual per model | PROC-AI-003 (ACT-013) |

---

## 8. Platform integration

Tranc3 layer 1 controls: encryption, auth, DEFSTAN CI. Magna Carta bridge: [TRANC3-REGISTER-BRIDGE.md](../compliance/TRANC3-REGISTER-BRIDGE.md) (ACT-009 pending full import).

**Next review:** 2026-09-06
