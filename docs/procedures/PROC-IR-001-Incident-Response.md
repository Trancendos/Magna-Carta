# PROC-IR-001 — Incident Response Procedure

**Version:** 1.0.0 · **Owner:** Security Ops · **Policy:** POL-OPS-001

---

## 1. Detection

Sources: monitoring alerts, user reports, CI failures, pen tests, Ice Box, Wazuh (when deployed).

## 2. Triage (within 15 min for suspected P0)

1. Assign incident commander
2. Classify severity (P0–P3)
3. Open incident ticket with timestamp, affected services, initial scope
4. Preserve logs and snapshots — do not destroy evidence

## 3. Containment

| P0 actions | P1 actions |
|------------|------------|
| Activate WarRoom | Assign security lead |
| Isolate affected workers | Block malicious IPs / revoke tokens |
| Revoke compromised credentials | Enable enhanced logging |
| Notify executive + DPO | Customer comms if SLA breach |

## 4. Eradication & recovery

1. Identify root cause
2. Patch or rollback via PROC-CHG-001 (Emergency path if needed)
3. Verify integrity (compliance checker, smoke tests)
4. Restore from backup if required (PROC-BCP-001)

## 5. Breach assessment (if personal data)

DPO determines:
- Risk to individuals
- ICO notification required? (72h)
- Data subject notification required?

## 6. Closure

- Post-mortem document (5 business days for P0/P1)
- Update risk register and DEFSTAN register if control failed
- Lessons learned to CAB

## 7. Contacts

| Role | Channel |
|------|---------|
| Security Ops | WarRoom / security@ |
| DPO | privacy@ |
| On-call engineering | Pager / Town Hall |
