# Compliance Health Check Log

**Owner:** ISMS Lead  
**Cadence:** Weekly (local — no CI minutes)  
**Automation:** `scripts/weekly_compliance_health.sh`  
**Machine log:** `compliance/health_check_history.yaml`

---

## Purpose

Human-readable audit trail of weekly documentation health checks. Each run executes `compliance_health_check.py --report --log` on an ISMS-maintained machine (developer workstation, ISMS VM, or scheduled local cron). **No GitHub Actions** — zero cloud CI cost.

---

## How to run

```bash
# One-off
./scripts/weekly_compliance_health.sh

# Optional: install local cron (Monday 08:00, user crontab only)
./scripts/install_local_weekly_cron.sh
```

---

## Run history

| Date | Errors | Warnings | Operator | Notes |
|------|--------|----------|----------|-------|
| — | — | — | — | First run after merge — populate via weekly script |

*Detailed entries are appended automatically to `compliance/health_check_history.yaml`.*

---

## Escalation

| Finding | Action | Within |
|---------|--------|--------|
| Any error | ISMS + doc owner ticket | 5 business days |
| Warnings > 5 at week end | Add to ISMS stand-up agenda | Next stand-up |
| No run in 7+ days | MON-008 warning in next manual check | Immediate |

**Related:** [COMPLIANCE-MAINTENANCE-PROGRAMME.md](../governance/COMPLIANCE-MAINTENANCE-PROGRAMME.md)
