# SOC 2 Type II Evidence Schedule

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Observation period target:** 2026-10-01 → 2027-03-31  
**Report target:** Q1 2027  
**Alignment:** [SOC2-ALIGNMENT.md](SOC2-ALIGNMENT.md) · Tranc3 `scripts/soc2_evidence_collector.py`

---

## 1. Purpose

Defines **what evidence** must be collected, **how often**, and **where it is stored** for SOC 2 Type II. Programme artefacts in Magna Carta satisfy control design; this schedule drives **operational evidence** (🎯 external validation).

---

## 2. Evidence catalogue

| Evidence ID | TSC / criteria | Description | Frequency | Source / automation | Owner | Storage |
|-------------|----------------|-------------|-----------|---------------------|-------|---------|
| EV-SOC-001 | CC6.1 | Access provisioning records | Per event | PROC-IAM-001 tickets | IT / ISMS | Town Hall + IAM log |
| EV-SOC-002 | CC6.2 | Privileged access review | Quarterly | PROC-IAM-001 §4 | ISMS Lead | Review minutes |
| EV-SOC-003 | CC6.3 | Authentication config (MFA, JWT) | Continuous | Zero Trust IAM config export | Security Ops | Git + snapshot |
| EV-SOC-004 | CC7.1 | Vulnerability scan results | Weekly | dependency-audit CI | Security Ops | CI artefacts |
| EV-SOC-005 | CC7.2 | Penetration test report | Annual | External tester | Security Ops | [PEN-TEST-LOG.md](../evidence/PEN-TEST-LOG.md) |
| EV-SOC-006 | CC7.3 | Incident tickets and closure | Per event | PROC-IR-001 | Security Ops | Observatory / WarRoom |
| EV-SOC-007 | CC8.1 | CAB change records | Per change | PROC-CHG-001, PROC-CHG-002 | CAB | Forgejo + minutes |
| EV-SOC-008 | CC8.2 | CI test and compliance gate | Per deploy | production-gate workflow | Platform Eng | CI logs |
| EV-SOC-009 | CC9.1 | Supplier inventory | Quarterly | supplier_dpa_register.yaml | DPO | Magna Carta repo |
| EV-SOC-010 | CC9.2 | Supplier risk assessment | Annual | POL-SUP-001 reviews | Procurement | Register + minutes |
| EV-SOC-011 | A1.2 | Uptime / availability metrics | Continuous | Prometheus / Grafana | Operations | Observatory |
| EV-SOC-012 | A1.3 | Backup verification | Monthly | backup-service | Operations | Backup logs |
| EV-SOC-013 | A1.3 | BCP restore test | Annual | PROC-BCP-001 | Operations | [BCP-RESTORE-TEST-LOG.md](../evidence/BCP-RESTORE-TEST-LOG.md) |
| EV-SOC-014 | C1.1 | Confidentiality — encryption config | Quarterly | Vault, TLS certs | Security Ops | Config export |
| EV-SOC-015 | P1–P8 | Privacy — DSR log | Per request | PROC-DSR-001 | DPO | DSR register |
| EV-SOC-016 | CC1.1 | Policy attestation (privileged) | Annual | PROC-TRN-001 | HR / ISMS | [POLICY-ATTESTATION-REGISTER.md](../evidence/POLICY-ATTESTATION-REGISTER.md) |
| EV-SOC-017 | CC1.2 | Compliance review minutes | Quarterly | PROC-CMP-001 | ISMS Lead | Town Hall MeetingRooms |
| EV-SOC-018 | CC1.3 | Risk register review | Quarterly | RISK-REGISTER.md | ISMS Lead | Magna Carta repo |

---

## 3. Observation period milestones

| Date | Milestone |
|------|-----------|
| 2026-10-01 | Observation period start; enable automated collector |
| 2026-12-31 | Mid-period internal audit (sample EV rows) |
| 2027-03-31 | Observation period end |
| 2027-04-30 | Auditor readiness pack assembly |
| 2027-Q1 | Type II report issuance (target) |

---

## 4. Pre-audit readiness checklist

- [ ] All EV-SOC rows have at least one sample for observation window
- [ ] Gaps logged in [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md)
- [ ] Policies and procedures version-aligned with control descriptions
- [ ] Tranc3 `SOC2_TYPE_II.md` TSC mapping cross-checked
- [ ] Management review completed ([MANAGEMENT-REVIEW-TEMPLATE.md](../governance/MANAGEMENT-REVIEW-TEMPLATE.md))

---

## 5. Related documents

- [SOC2-ALIGNMENT.md](SOC2-ALIGNMENT.md)
- [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md) — ACT-008
- [../procedures/PROC-CMP-001-Compliance-Review.md](../procedures/PROC-CMP-001-Compliance-Review.md)
