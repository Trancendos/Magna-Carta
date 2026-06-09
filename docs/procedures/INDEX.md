# Procedure Library Index

**Version:** 1.0.0  
**Date:** 2026-06-08  
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
| [PROC-AI-003](PROC-AI-003-AI-Security-Threat-Assessment.md) | AI Security Threat Assessment | POL-AI-001, POL-SEC-001 | AI Lead / Security Ops |
| [PROC-CHG-002](PROC-CHG-002-Post-Implementation-Review.md) | Post-Implementation Review | POL-OPS-002 | CAB |
| [PROC-TRN-001](PROC-TRN-001-Security-Awareness-Attestation.md) | Security Awareness & Attestation | POL-SEC-001, POL-SEC-002 | HR / ISMS |
| [PROC-HR-001](PROC-HR-001-Staff-Lifecycle.md) | Staff Lifecycle (screening / offboarding) | POL-SEC-001, POL-SEC-002 | HR / ISMS |
| [PROC-CAPA-001](PROC-CAPA-001-Corrective-Action.md) | Corrective & Preventive Action | POL-SEC-001, POL-OPS-001 | ISMS Lead |
| [PROC-HSE-001](PROC-HSE-001-Workplace-Health-Safety.md) | Workplace Health & Safety | POL-SEC-001 | H&S Lead |
| [PROC-FIN-001](PROC-FIN-001-Financial-Controls-Reporting.md) | Financial Controls & Reporting | Companies Act / FCA (perimeter) | Finance Controller |
| [PROC-PRM-001](PROC-PRM-001-Procurement-Supplier-Engagement.md) | Procurement & Supplier Engagement | POL-SUP-001 | Procurement |
| [PROC-LEG-001](PROC-LEG-001-Legal-Contract-Management.md) | Legal & Contract Management | Templates | Legal |
| [PROC-IP-001](PROC-IP-001-Intellectual-Property-Management.md) | Intellectual Property Management | — | Legal / Engineering |
| [PROC-PAY-001](PROC-PAY-001-Payroll-Compensation-Administration.md) | Payroll & Compensation | — | Finance / HR |
| [PROC-BLD-001](PROC-BLD-001-Building-Regulations-Premises.md) | Building Regulations & Premises | — | Facilities |
| [PROC-IT-001](PROC-IT-001-IT-Service-Management.md) | IT Service Management | POL-SEC-001 | IT Ops |
| [PROC-WLB-001](PROC-WLB-001-Employee-Wellbeing.md) | Employee Wellbeing | — | HR |
| [PROC-MHL-001](PROC-MHL-001-Mental-Health-Psychological-Safety.md) | Mental Health & Psychological Safety | — | HR |
| [PROC-UMG-001](PROC-UMG-001-Platform-User-Administration.md) | Platform User Administration | POL-SEC-001 | IT / Product |
| [PROC-DAT-001](PROC-DAT-001-Enterprise-Data-Management.md) | Enterprise Data Management | POL-PRI-001 | DPO / Data Gov |

**Department bibles:** [bibles/INDEX.md](../bibles/INDEX.md) · **Job descriptions:** [job-descriptions/INDEX.md](../job-descriptions/INDEX.md)

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
| PROC-AI-003 | Model change; annual security assessment; new agentic routes; post-AI incident |
| PROC-CHG-002 | Major production change closure (CAB) |
| PROC-TRN-001 | Onboarding; annual refresh; policy version change |
| PROC-HR-001 | Joiner / mover / leaver; screening before privileged access |
| PROC-CAPA-001 | Audit finding; pen test; incident; compliance gap |
| PROC-HSE-001 | Incident; annual H&S review; new site / homeworking policy |
| PROC-FIN-001 | Month-end; audit; material control change |
| PROC-PRM-001 | New supplier; contract renewal; spend threshold breach |
| PROC-LEG-001 | Contract intake; litigation hold; regulatory notice |
| PROC-IP-001 | New product; OSS dependency; employee invention |
| PROC-PAY-001 | Payroll run; compensation change; RTI submission |
| PROC-BLD-001 | Premises change; fire drill; accessibility review |
| PROC-IT-001 | Service request; patch cycle; SaaS onboarding |
| PROC-WLB-001 | Wellbeing programme review; ER case |
| PROC-MHL-001 | Psychological risk assessment; critical incident |
| PROC-UMG-001 | Tenant admin change; privileged user grant |
| PROC-DAT-001 | Retention review; data quality issue; archive project |

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
