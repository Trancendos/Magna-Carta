# PROC-CMP-001 — Compliance Review Procedure

**Version:** 1.0.0 · **Owner:** ISMS Lead

---

## 1. Quarterly review (every 90 days)

### Agenda

1. DEFSTAN register status (`compliance/checker.py` score)
2. Magna Carta policy/procedure changes
3. ISO 27001 SOA gap progress
4. SOC 2 evidence collector status
5. GDPR: DSR metrics, breach log, ROPA updates
6. AI governance: model registry, incidents, fairness status
7. Risk register and open waivers
8. Legislation register scan ([LEGISLATION-REGISTER.md](../compliance/LEGISLATION-REGISTER.md), `compliance/legislation_register.yaml`); **EU EUR-Lex quarterly scan** ([EU-LEGISLATION-MONITORING.md](../compliance/EU-LEGISLATION-MONITORING.md), ACT-014); **harmonised / ETSI standards semi-annual watch** ([HARMONISED-STANDARDS-MONITORING.md](../compliance/HARMONISED-STANDARDS-MONITORING.md), `compliance/standards_watch.yaml`, ACT-015); regulators/ombudsmen ([REGULATORS-OMBUDSMEN-REGISTER.md](../compliance/REGULATORS-OMBUDSMEN-REGISTER.md))
9. Pen test / vuln programme status
10. Tranc3 integration bridge status (`tranc3_register_bridge.yaml`, ACT-009 staging)
11. Documentation health: confirm weekly `./scripts/weekly_compliance_health.sh` ran (see [COMPLIANCE-HEALTH-LOG.md](../evidence/COMPLIANCE-HEALTH-LOG.md)); run `python3 scripts/compliance_health_check.py --report` if needed; review [COMPLIANCE-MAINTENANCE-PROGRAMME.md](../governance/COMPLIANCE-MAINTENANCE-PROGRAMME.md)
12. Actions and owners

### Participants

ISMS Lead (chair), DPO, Platform Engineering lead, Security Ops, AI Lead (if AI changes), CAB rep.

### Outputs

- Meeting minutes in Town Hall MeetingRooms
- Updated [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md) (`compliance/compliance_action_tracker.yaml`)
- Register.yaml updates merged within 2 weeks

## 2. Annual review

- Full policy re-approval attestation
- Access review summary (PROC-IAM-001)
- BCP restore test results
- Supplier register review (POL-SUP-001)
- Certification roadmap update (FRAMEWORK.md §5.2)

## 3. Triggered reviews

- Material breach or regulatory change
- New market entry (e.g. US state privacy law)
- Major architecture change
- Pre-audit (ISO/SOC2) evidence pack assembly

## 4. Evidence pack checklist

- [ ] register.yaml export + CI score
- [ ] test_evidence.yaml
- [ ] Policy index current
- [ ] AS-BUILT-ARCHITECTURE current
- [ ] Risk register
- [ ] Sample change and incident records
- [ ] Pen test report (if within 12 months)

## 5. Calendar

| Review | Months |
|--------|--------|
| Q1 | March |
| Q2 | June |
| Q3 | September |
| Q4 | December |

Aligned with DEFSTAN `meta.review_cycle: quarterly`.

## 6. Monitoring vs audit

| Activity | Type | Owner | Cadence |
|----------|------|-------|---------|
| DEFSTAN CI score check | Monitoring | Platform Engineering | Every merge |
| `GET /compliance/status` review | Monitoring | ISMS Lead | Weekly |
| Quarterly compliance review (this procedure) | Monitoring | ISMS Lead | Quarterly |
| Policy attestation cycle | Audit | BoardRoom / Executive | Annual |
| ISO/SOC2 evidence pack assembly | Audit | ISMS Lead | Pre-audit |
| External penetration test | Audit | Security Lead | Annual |

Monitoring identifies issues for correction before audit. Findings from audit feed the next quarterly review action tracker.

References: [COMPLIANCE-BLUEPRINT.md](../compliance/COMPLIANCE-BLUEPRINT.md) §10, [OBLIGATIONS-REGISTER.md](../compliance/OBLIGATIONS-REGISTER.md), [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md), [RISK-REGISTER.md](../compliance/RISK-REGISTER.md), [SOC2-EVIDENCE-SCHEDULE.md](../compliance/SOC2-EVIDENCE-SCHEDULE.md), [TRANC3-REGISTER-BRIDGE.md](../compliance/TRANC3-REGISTER-BRIDGE.md), [CONTINUOUS-IMPROVEMENT-PROGRAMME.md](../governance/CONTINUOUS-IMPROVEMENT-PROGRAMME.md)
