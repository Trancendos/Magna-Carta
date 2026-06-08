# Magna Carta Governance Bible

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Classification:** Internal — governance reference  
**Audience:** ISMS Lead, DPO, Engineering leads, auditors

---

## 1. What this Bible is

The **canonical operational encyclopaedia** for running Trancendos compliance and governance. [FRAMEWORK.md](../../FRAMEWORK.md) explains the blueprint; this Bible explains **daily practice**.

**Honesty rule:** ✅ in this Bible means *programme artefact exists*. Operational certification requires layer 3 evidence.

---

## 2. Three layers

| Layer | What | Where | Maturity |
|-------|------|-------|----------|
| 1 — Platform | Technical controls in code | Tranc3 repo | Strong (DEFSTAN CI, auth, encryption) |
| 2 — Programme | Policies, procedures, registers | **This repo** | Comprehensive after 2026 waves |
| 3 — Operations | Signed contracts, drills, audits | External evidence | ACT-001–012 open |

---

## 3. Document hierarchy

```
FRAMEWORK.md (strategy)
    └── 00-EXECUTIVE-SUMMARY.md (roadmap)
    └── COMPLIANCE-BLUEPRINT.md (operating model)
    └── Policies (9) → Procedures (12) → Cookbooks → Hymn sheets
    └── Registers (human + YAML)
    └── Alignment docs (per standard/regulation)
    └── Evidence logs
```

Artifact definitions: [DOCUMENTATION-ARTIFACT-MODEL.md](../governance/DOCUMENTATION-ARTIFACT-MODEL.md)

---

## 4. Core registers (always current)

| Register | Path | YAML twin |
|----------|------|-----------|
| Coverage (honest status) | compliance/COMPLIANCE-COVERAGE-REGISTER.md | — |
| Regulation matrix | compliance/REGULATION-MATRIX.md | — |
| Legislation | compliance/LEGISLATION-REGISTER.md | — |
| Obligations | compliance/OBLIGATIONS-REGISTER.md | — |
| Standards | compliance/STANDARDS-REGISTER.md | — |
| Regulators / Ombudsmen | compliance/REGULATORS-OMBUDSMEN-REGISTER.md | — |
| Systems | compliance/SYSTEMS-REGISTER.md | — |
| Reviewers | governance/REVIEWERS-REGISTER.md | — |
| Risks | compliance/RISK-REGISTER.md | compliance/risk_register.yaml |
| Actions | compliance/COMPLIANCE-ACTION-TRACKER.md | compliance/compliance_action_tracker.yaml |
| Suppliers | compliance/SUPPLIER-DPA-REGISTER.md | compliance/supplier_dpa_register.yaml |
| Magna Carta MC items | — | compliance/magna_carta_register.yaml |
| Tranc3 bridge | compliance/TRANC3-REGISTER-BRIDGE.md | compliance/tranc3_register_bridge.yaml |

---

## 5. Cadence calendar

| Activity | Frequency | Owner | Procedure / cookbook |
|----------|-----------|-------|----------------------|
| Compliance review | Quarterly | ISMS Lead | PROC-CMP-001 / COOK-CMP-001 |
| Maintenance health check | Weekly (local) + quarterly | ISMS Lead | `scripts/weekly_compliance_health.sh` |
| Legislation scan | Quarterly | DPO | LEGISLATION-REGISTER |
| Access review | Quarterly | ISMS Lead | PROC-IAM-001 |
| Internal audit | Annual min | ISMS Lead | INTERNAL-AUDIT-PROGRAMME |
| Management review | Annual | Executive | MANAGEMENT-REVIEW-TEMPLATE |
| BCP restore test | Semi-annual | Operations | PROC-BCP-001 |
| Policy attestation | Annual | HR | PROC-TRN-001 |
| Pen test | Annual | Security Ops | PEN-TEST-PROGRAMME |

Full reviewer list: [REVIEWERS-REGISTER.md](../governance/REVIEWERS-REGISTER.md)

---

## 6. Escalation paths

1. **Control failure in production** → Security Ops → ISMS → CAB if change needed
2. **Personal data breach** → DPO within 1h → ICO assessment within 72h
3. **P0 action past due** → ISMS → Executive
4. **Regulator letter** → Legal within 24h → Executive
5. **Health check errors in weekly log** → ISMS + doc owner next stand-up

---

## 7. Tranc3 integration

| Item | Status | Action |
|------|--------|--------|
| `magna_carta.py` runtime checker | 🎯 ACT-009 | Enable in staging per TRANC3-INTEGRATION-GUIDE |
| MC-RULE-001–009 | Config in `config/magna_carta_config.json` | — |
| Register bridge MC-001–011 | Documented | Sync on Tranc3 releases |
| Town Hall cookbooks | Parallel track in Tranc3 | Keep Magna Carta cookbooks canonical for audits |

---

## 8. Path to external assurance

| Milestone | Target | Blocker |
|-----------|--------|---------|
| ICO live registration | 2026-07 | ACT-003 |
| SOC 2 observation | From 2026-10 | ACT-008 |
| ISO 27001 audit | Q2 2027 | ACT-011, org controls |
| Operational ✅ on coverage register | 2027 | ACT-001–012 |

---

## 9. How to extend this Bible

When adding a new domain (e.g. NHS DSPT operational):

1. Add readiness/alignment doc in `docs/compliance/`
2. Update REGULATION-MATRIX and COMPLIANCE-COVERAGE-REGISTER
3. Add obligations to OBLIGATIONS-REGISTER
4. Create procedure if process-heavy; cookbook + hymn sheet if operational
5. Run `compliance_health_check.py` and fix drift

---

## 10. Review

| Activity | Frequency | Next |
|----------|-----------|------|
| Bible content review | Annual | 2027-06-07 |
| Cross-link integrity | Quarterly (automated) | 2026-09-06 |

**Related:** [CONTINUOUS-IMPROVEMENT-PROGRAMME.md](../governance/CONTINUOUS-IMPROVEMENT-PROGRAMME.md)
