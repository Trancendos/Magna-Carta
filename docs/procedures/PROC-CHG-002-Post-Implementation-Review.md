# PROC-CHG-002 — Post-Implementation Review (PIR)

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** CAB Chair · **Policy:** POL-OPS-002

---

## 1. Purpose

Ensures production changes are reviewed after deployment for success, unintended impact, and control effectiveness. Closes the change loop required by ISO 27001 A.8.32 and SOC 2 CC8.1.

---

## 2. Scope

| Change type | PIR required |
|-------------|--------------|
| Standard — production-impacting | Yes, within 5 business days |
| Emergency change | Yes, within 2 business days |
| Security patch (routine) | Simplified PIR (checklist only) |
| Documentation-only | Optional |

---

## 3. PIR template

| Field | Content |
|-------|---------|
| Change ID | Link to PROC-CHG-001 record |
| Deployment date/time | UTC |
| Implementer | Name / role |
| Summary | What changed |
| Success criteria | Met? Y/N |
| Monitoring period | e.g. 24–72h post-deploy |
| Incidents linked | None / IDs |
| Rollback required | Y/N |
| Security/compliance impact | None / describe |
| Lessons learned | Free text |
| CAPA items | Owner + date |
| Reviewer | CAB delegate |
| Sign-off date | |

---

## 4. Process

1. CAB or implementer schedules PIR after deployment window
2. Review Observatory metrics, error rates, compliance checker
3. Complete template; attach to change record
4. Escalate failures to WarRoom if P1 criteria met
5. Aggregate PIR themes quarterly in PROC-CMP-001

---

## 5. Records

| Record | Retention |
|--------|-----------|
| Completed PIR forms | 3 years (with change records) |
| Quarterly PIR summary | 5 years |

---

## 6. Related documents

- [PROC-CHG-001](PROC-CHG-001-Change-Request.md)
- [POL-OPS-002](../policies/POL-OPS-002-Change-Management.md)
- [ISO27001-ALIGNMENT.md](../compliance/ISO27001-ALIGNMENT.md)
