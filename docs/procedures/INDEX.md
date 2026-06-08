# Procedure Library Index

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead

---

## Procedure register

| ID | Procedure | Linked policy | Owner |
|----|-----------|---------------|-------|
| [PROC-IR-001](PROC-IR-001-Incident-Response.md) | Incident Response | POL-OPS-001 | Security Ops |
| [PROC-CHG-001](PROC-CHG-001-Change-Request.md) | Change Request | POL-OPS-002 | CAB |
| [PROC-IAM-001](PROC-IAM-001-Access-Provisioning.md) | Access Provisioning | POL-SEC-001 | IT / ISMS |
| [PROC-DSR-001](PROC-DSR-001-Data-Subject-Requests.md) | Data Subject Requests | POL-PRI-001 | DPO |
| [PROC-VUL-001](PROC-VUL-001-Vulnerability-Management.md) | Vulnerability Management | POL-SEC-001 | Security Ops |
| [PROC-BCP-001](PROC-BCP-001-Backup-Restore.md) | Backup & Restore | POL-OPS-003 | Operations |
| [PROC-CMP-001](PROC-CMP-001-Compliance-Review.md) | Compliance Review | All | ISMS Lead |
| [PROC-AI-002](PROC-AI-002-Fairness-Bias-Testing.md) | Fairness & Bias Testing | POL-AI-001 | AI Lead |
| [PROC-CHG-002](PROC-CHG-002-Post-Implementation-Review.md) | Post-Implementation Review | POL-OPS-002 | CAB |
| [PROC-TRN-001](PROC-TRN-001-Security-Awareness-Attestation.md) | Security Awareness & Attestation | POL-SEC-001, POL-SEC-002 | HR / ISMS |

---

## Execution triggers

| Procedure | Trigger |
|-----------|---------|
| PROC-IR-001 | Security event, outage, data breach suspicion |
| PROC-CHG-001 | Any production-impacting change |
| PROC-IAM-001 | Joiner / mover / leaver |
| PROC-DSR-001 | DSR received via portal or email |
| PROC-VUL-001 | CVE alert, scan finding, pen test report |
| PROC-BCP-001 | Scheduled backup; disaster declaration |
| PROC-CMP-001 | Quarterly calendar |
| PROC-AI-002 | Model change; annual fairness cycle; high-risk AI feature launch |
| PROC-CHG-002 | Major production change closure (CAB) |
| PROC-TRN-001 | Onboarding; annual refresh; policy version change |

---

## Records retention

| Record type | Retention |
|-------------|-----------|
| Incident tickets | 3 years |
| Change records | 3 years |
| Access reviews | 2 years |
| DSR log | 3 years |
| Compliance review minutes | 5 years |
| Policy attestation records | 3 years |
| Pen test reports | 3 years |
