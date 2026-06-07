# POL-OPS-001 — Incident Response Policy

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** Security Ops · **Review:** Annual

---

## 1. Purpose

Ensure consistent detection, response, and recovery from security and service incidents.

## 2. Scope

All incidents affecting confidentiality, integrity, availability, or safety of Tranc3 or customer data.

## 3. Incident classification

| Severity | Definition | Example |
|----------|------------|---------|
| P0 | Critical business impact or active breach | Data exfiltration, auth bypass, total outage |
| P1 | Major degradation or contained breach | Partial outage, vuln actively exploited |
| P2 | Limited impact | Single service fault, scan finding |
| P3 | Informational | Near-miss, policy violation attempt |

## 4. Response requirements

- P0: WarRoom activated within 15 minutes; executive notified
- P1: Security lead assigned within 1 hour
- All: Documented timeline, evidence preservation, root cause analysis

## 5. Communication

- Internal: Town Hall WarRoom / incident channel
- External: Customer notification per contract and GDPR if personal data affected
- Regulatory: ICO notification within 72 hours if required (DPO decision)

## 6. Post-incident

- Post-mortem within 5 business days for P0/P1
- Remediation tracked in risk register
- DEFSTAN register updated if control failure identified

## 7. Related documents

PROC-IR-001, POL-SEC-001, POL-PRI-001, GDPR-ALIGNMENT.md
