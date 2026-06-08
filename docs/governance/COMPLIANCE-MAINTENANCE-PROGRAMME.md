# Compliance Maintenance Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Procedure:** [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)  
**Automation:** `scripts/compliance_health_check.py` · `compliance/maintenance_monitor.yaml`

---

## 1. Purpose

Keep Magna Carta documentation **accurate, linked, and timely** without relying on memory. Combines:

- **Proactive** automated checks (CI + local)
- **Reactive** quarterly human review
- **Adaptive** triggers on regulatory or architecture change

This is **not** operational certification monitoring — see ACT-001–012 for layer 3.

---

## 2. Monitoring layers

```
┌─────────────────────────────────────────────────────────┐
│  LAYER A — Automated (weekly CI / on-demand)            │
│  compliance_health_check.py → maintenance_monitor.yaml  │
└───────────────────────────┬─────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER B — Quarterly human (PROC-CMP-001)               │
│  COOK-CMP-001 + HYMN-CMP-001                            │
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

Full config: `compliance/maintenance_monitor.yaml`

---

## 4. Cadence

| Activity | When | Tool / owner |
|----------|------|--------------|
| Health check in CI | Weekly (Monday) | GitHub/Forgejo workflow — ISMS |
| Health check before quarterly review | T-7 days | ISMS Lead |
| Full register human review | Quarterly | PROC-CMP-001 |
| Artifact model gap scan | Quarterly | DOCUMENTATION-ARTIFACT-MODEL §7 |
| Bible annual refresh | Annual | MAGNACARTA-GOVERNANCE-BIBLE |
| Schema doc update | On new YAML register | REGISTER-SCHEMAS |

---

## 5. Triggers (adaptive)

| Event | Action | Within |
|-------|--------|--------|
| New regulation in LEGISLATION watch list | Add alignment/readiness doc; update matrix | 30 days |
| New sub-processor | SUPPLIER-DPA-REGISTER + YAML | Before processing |
| Major Tranc3 architecture change | SYSTEMS-REGISTER + AS-BUILT | 14 days |
| P1 incident | IR cookbook + CAPA; risk register | Per COOK-IR-001 |
| Failed health check (error) | Ticket to ISMS + doc owner | 5 business days |
| Customer audit request | Evidence pack PROC-CMP-001 §4 | Per request |

---

## 6. CI integration (recommended)

Add to Forgejo/GitHub Actions (Tranc3 or Magna Carta repo):

```yaml
- name: Compliance documentation health
  run: python3 scripts/compliance_health_check.py --strict
```

`--strict` exits non-zero on `error` severity — blocks merge if registers broken.

---

## 7. Roles

| Role | Responsibility |
|------|----------------|
| ISMS Lead | Owns programme; chairs quarterly review |
| Platform Engineering | Fixes CI failures; SYSTEMS-REGISTER |
| DPO | Legislation, regulators, privacy registers |
| All doc owners | Keep `last_updated` and review dates honest |

---

## 8. Metrics (report quarterly)

| Metric | Target |
|--------|--------|
| Health check error count | 0 |
| Open warnings at quarter end | < 5 with owners |
| ACT P0 past due | 0 |
| Cookbook coverage (P0 procedures) | 100% within 12 months |
| Register review on time | 100% |

---

## 9. Review

| Activity | Next |
|----------|------|
| Programme review | 2026-09-06 |
| Add CI workflow to Tranc3/Magna Carta | 🎯 Platform Engineering |

**Related:** [CONTINUOUS-IMPROVEMENT-PROGRAMME.md](CONTINUOUS-IMPROVEMENT-PROGRAMME.md) · [DOCUMENTATION-ARTIFACT-MODEL.md](DOCUMENTATION-ARTIFACT-MODEL.md)
