# COOK-CMP-001 — Quarterly Compliance Review Playbook

**Version:** 1.0.0  
**Owner:** ISMS Lead  
**Procedure:** [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)  
**Hymn sheet:** [HYMN-CMP-001](../hymn-sheets/HYMN-CMP-001-Quarterly-Review-Checklist.md)

---

## When to use

Every 90 days, or within 14 days of a material regulatory change, pre-audit, or executive request.

---

## Pre-flight (T-7 days)

1. Run maintenance health check:
   ```bash
   python3 scripts/compliance_health_check.py --report
   ```
2. Export open actions from `compliance/compliance_action_tracker.yaml`
3. Pull DEFSTAN CI score from latest Tranc3 pipeline (if available)
4. Book Town Hall MeetingRoom; invite per PROC-CMP-001 §1

---

## Agenda execution (90-minute session)

### Block 1 — Registers (30 min)

| Step | Action | Artefact |
|------|--------|----------|
| 1 | Chair opens; confirm quorum | Minutes template |
| 2 | Review COMPLIANCE-COVERAGE-REGISTER deltas | Update symbols if needed |
| 3 | Legislation + obligations scan (UK + EU) | LEGISLATION-REGISTER, `legislation_register.yaml`, EU-LEGISLATION-MONITORING, OBLIGATIONS-REGISTER |
| 4 | Standards + regulators review | STANDARDS-REGISTER, REGULATORS-OMBUDSMEN-REGISTER |
| 5 | Systems register vs AS-BUILT drift | SYSTEMS-REGISTER |

### Block 2 — Programmes (30 min)

| Step | Action | Artefact |
|------|--------|----------|
| 6 | ISO 27001 SOA gap progress | ISO27001-ALIGNMENT |
| 7 | SOC 2 evidence schedule status | SOC2-EVIDENCE-SCHEDULE |
| 8 | AI governance: model cards, bias status | AI-GOVERNANCE, ACT-004 |
| 9 | Supplier DPA register | SUPPLIER-DPA-REGISTER |
| 10 | Pen test / vuln programme | PEN-TEST-PROGRAMME, PROC-VUL-001 |

### Block 3 — Actions (30 min)

| Step | Action | Artefact |
|------|--------|----------|
| 11 | Walk ACT-001–014; assign/close | compliance_action_tracker.yaml |
| 12 | Risk register top 5 | RISK-REGISTER |
| 13 | Tranc3 bridge / ACT-009 status | TRANC3-REGISTER-BRIDGE |
| 14 | Document decisions; set next review date | PROC-CMP-001 calendar |

---

## Post-meeting (T+14 days)

1. Publish minutes to Town Hall MeetingRooms
2. Update COMPLIANCE-ACTION-TRACKER.md and YAML
3. Merge any register.yaml / magna_carta_register.yaml changes within 2 weeks
4. File evidence pack items per PROC-CMP-001 §4

---

## Decision tree

```
Material regulatory change detected?
  ├─ Yes → Schedule triggered review within 14 days
  └─ No → Continue quarterly cadence

Any P0 action past due?
  ├─ Yes → Escalate to Executive same day
  └─ No → Note in minutes

Health check failures?
  ├─ Yes → Assign owner; target fix before next quarter
  └─ No → Log clean run in minutes
```

**Next review:** 2026-09-06
