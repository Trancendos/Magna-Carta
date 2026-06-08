# Compliance Maintenance Programme

**Version:** 1.1.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Procedure:** [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)  
**Automation:** `scripts/compliance_health_check.py` · `scripts/weekly_compliance_health.sh` · `compliance/maintenance_monitor.yaml`

---

## 1. Purpose

Keep Magna Carta documentation **accurate, linked, and timely** without relying on memory. Combines:

- **Proactive** automated checks (local weekly + on-demand)
- **Reactive** quarterly human review
- **Adaptive** triggers on regulatory or architecture change

This is **not** operational certification monitoring — see ACT-001–012 for layer 3.

**Cost policy:** Weekly monitoring runs **locally** (cron on ISMS machine or manual). **No GitHub Actions** — avoids CI minute charges across org repos.

---

## 2. Monitoring layers

```
┌─────────────────────────────────────────────────────────┐
│  LAYER A — Automated (weekly local / on-demand)         │
│  weekly_compliance_health.sh → health_check_history.yaml│
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER B — Quarterly human (PROC-CMP-001)             │
│  COOK-CMP-001 + HYMN-CMP-001                          │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER C — Triggered (regulatory change, incident, audit)│
└─────────────────────────────────────────────────────────┘
```

---

## 3. Automated checks (MON-###)

| Check | What | Severity | Remediation |
|-------|------|----------|-------------|
| MON-001 | Required register files exist | error | Restore from git / create |
| MON-002 | `last_updated` / review dates stale > 120 days | warning | PROC-CMP-001 update |
| MON-003 | Open ACT actions past `due_date` | warning | Escalate per REVIEWERS-REGISTER |
| MON-004 | README policy/procedure counts match INDEX | error | Fix README drift |
| MON-005 | Cookbook/hymn index references resolve | error | Fix broken links |
| MON-006 | YAML registers parseable | error | Fix syntax |
| MON-007 | Programme milestone docs exist (artifact model) | warning | Create missing artefact |
| MON-008 | Last logged health check within 7 days | warning | Run weekly script |
| MON-009 | YAML registers match JSON Schema structure (8 pairs) | error | Fix register fields |
| MON-010 | Every PROC-* has COOK-* and HYMN-* | error | Create missing cookbook/hymn sheet |

Full config: `compliance/maintenance_monitor.yaml`

---

## 4. Cadence

| Activity | When | Tool / owner |
|----------|------|--------------|
| Weekly health check | Monday (local cron or manual) | `scripts/weekly_compliance_health.sh` — ISMS |
| Health check before quarterly review | T-7 days | ISMS Lead |
| Full register human review | Quarterly | PROC-CMP-001 |
| Artifact model gap scan | Quarterly | DOCUMENTATION-ARTIFACT-MODEL §7 |
| Bible annual refresh | Annual | MAGNACARTA-GOVERNANCE-BIBLE |
| Schema doc update | On new YAML register | REGISTER-SCHEMAS |

---

## 5. Weekly run (zero cloud CI cost)

```bash
# From repo root — logs to compliance/health_check_history.yaml
./scripts/weekly_compliance_health.sh

# Optional: user crontab on ISMS workstation (Mondays 08:00)
./scripts/install_local_weekly_cron.sh
```

Human-readable mirror: [COMPLIANCE-HEALTH-LOG.md](../evidence/COMPLIANCE-HEALTH-LOG.md)

**Pre-merge / pre-review (on demand):**

```bash
python3 scripts/compliance_health_check.py --report --strict
```

`--strict` exits non-zero on `error` severity — use before quarterly review or doc merges; not required in cloud CI.

---

## 6. Triggers (adaptive)

| Event | Action | Within |
|-------|--------|--------|
| New regulation in LEGISLATION watch list | Add alignment/readiness doc; update matrix | 30 days |
| New sub-processor | SUPPLIER-DPA-REGISTER + YAML | Before processing |
| Major Tranc3 architecture change | SYSTEMS-REGISTER + AS-BUILT | 14 days |
| P1 incident | IR cookbook + CAPA; risk register | Per COOK-IR-001 |
| Failed health check (error) | Ticket to ISMS + doc owner | 5 business days |
| Customer audit request | Evidence pack PROC-CMP-001 §4 | Per request |

---

## 7. Roles

| Role | Responsibility |
|------|----------------|
| ISMS Lead | Owns programme; runs weekly check; chairs quarterly review |
| Platform Engineering | Fixes register drift; SYSTEMS-REGISTER |
| DPO | Legislation, regulators, privacy registers |
| All doc owners | Keep `last_updated` and review dates honest |

---

## 8. Metrics (report quarterly)

| Metric | Target |
|--------|--------|
| Health check error count | 0 |
| Open warnings at quarter end | < 5 with owners |
| ACT P0 past due | 0 |
| Cookbook coverage (all procedures) | 100% |
| Weekly runs logged (52/year) | ≥ 48 |
| Register review on time | 100% |

---

## 9. Review

| Activity | Next |
|----------|------|
| Programme review | 2026-09-06 |
| First weekly log entry after merge | ISMS Lead |

**Related:** [CONTINUOUS-IMPROVEMENT-PROGRAMME.md](CONTINUOUS-IMPROVEMENT-PROGRAMME.md) · [DOCUMENTATION-ARTIFACT-MODEL.md](DOCUMENTATION-ARTIFACT-MODEL.md)
