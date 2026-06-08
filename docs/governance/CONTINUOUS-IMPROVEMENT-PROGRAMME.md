# Continuous Improvement Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Procedure:** [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)  
**Management review:** [MANAGEMENT-REVIEW-TEMPLATE.md](MANAGEMENT-REVIEW-TEMPLATE.md)

---

## 1. Purpose

Defines the Plan–Do–Check–Act (PDCA) cycle connecting Magna Carta policies, Phase 4 evidence artefacts, and Tranc3 operational controls. Complements MC-010 (evidence programme) and MC-011 (integration bridge).

---

## 2. PDCA cycle

```
┌──────────── PLAN ────────────┐
│ Risk register · Obligations  │
│ Action tracker · Audit plan  │
└──────────────┬───────────────┘
               ▼
┌──────────── DO ──────────────┐
│ Policies · Procedures        │
│ Tranc3 controls · Training   │
└──────────────┬───────────────┘
               ▼
┌──────────── CHECK ───────────┐
│ Internal audit · Monitoring  │
│ SOC 2 evidence · DEFSTAN CI  │
└──────────────┬───────────────┘
               ▼
┌──────────── ACT ─────────────┐
│ CAPA · Action tracker close  │
│ Management review · Register │
└──────────────┬───────────────┘
               │
               └────► next quarter PLAN
```

---

## 3. Cadence

| Activity | Frequency | Owner | Artefact |
|----------|-----------|-------|----------|
| DEFSTAN + Magna Carta register review | Quarterly | Platform Engineering | `register.yaml`, `magna_carta_register.yaml` |
| Compliance review (PROC-CMP-001) | Quarterly | ISMS Lead | MeetingRooms minutes |
| Risk register refresh | Quarterly | ISMS Lead | [RISK-REGISTER.md](../compliance/RISK-REGISTER.md) |
| Action tracker triage | Monthly | Action owners | [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md) |
| Internal audit | Annual | ISMS Lead | [INTERNAL-AUDIT-PROGRAMME.md](INTERNAL-AUDIT-PROGRAMME.md) |
| Management review | Annual | Executive / ISMS | [MANAGEMENT-REVIEW-TEMPLATE.md](MANAGEMENT-REVIEW-TEMPLATE.md) |
| Policy attestation | Annual | HR / ISMS | [POLICY-ATTESTATION-REGISTER.md](../evidence/POLICY-ATTESTATION-REGISTER.md) |
| Penetration test | Annual | Security Ops | [PEN-TEST-PROGRAMME.md](../evidence/PEN-TEST-PROGRAMME.md) |
| BCP restore drill | Annual (expand) | Operations | [BCP-RESTORE-TEST-LOG.md](../evidence/BCP-RESTORE-TEST-LOG.md) |
| Fairness / bias test | Semi-annual | AI Lead | [PROC-AI-002](../procedures/PROC-AI-002-Fairness-Bias-Testing.md) |

**Next quarterly review:** 2026-09-06

---

## 4. Input sources

| Source | Feeds |
|--------|-------|
| Incidents (PROC-IR-001) | Risk register, action tracker |
| Change post-implementation review (PROC-CHG-002) | Control map, audit findings |
| Supplier DPA register | Obligations register, ACT-001–002 |
| SOC 2 evidence schedule | Observation period gaps |
| GenAI maturity assessment | AI governance committee agenda |
| Tranc3 compliance CI gate | DEFSTAN score trends |
| Customer / auditor feedback | Management review |

---

## 5. Output artefacts

| Output | When | Stored |
|--------|------|--------|
| Updated action tracker rows | Each review | `compliance/compliance_action_tracker.yaml` |
| Risk treatment decisions | Quarterly | `compliance/risk_register.yaml` |
| Internal audit report | Annual | Evidence folder + ACT-011 |
| Management review minutes | Annual | Town Hall / BoardRoom |
| Register version bump | On material change | MC-### `last_reviewed` fields |

---

## 6. Improvement priorities (2026 H2)

| Priority | Theme | Actions |
|----------|-------|---------|
| P0 | Supplier contracts | ACT-001, ACT-002 |
| P1 | External assurance | ACT-003, ACT-005, ACT-008 |
| P1 | Product copy integrity | ACT-006 (Tranc3 PR) |
| P2 | Runtime integration | ACT-009 (staging enablement) |
| P2 | People controls | ACT-007 (attestations) |

---

## 7. Related documents

- [FRAMEWORK.md](../../FRAMEWORK.md) §5
- [COMPLIANCE-BLUEPRINT.md](../compliance/COMPLIANCE-BLUEPRINT.md)
- [TRANC3-REGISTER-BRIDGE.md](../compliance/TRANC3-REGISTER-BRIDGE.md)
- [EXTERNAL-FRAMEWORK-MAPPING.md](../compliance/EXTERNAL-FRAMEWORK-MAPPING.md) — Connor domain 5
