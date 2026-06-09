# Compliance Action Tracker

**Version:** 1.3.0  
**Date:** 2026-06-09  
**Owner:** ISMS Lead  
**Machine-readable:** [compliance/compliance_action_tracker.yaml](../../compliance/compliance_action_tracker.yaml)  
**Procedure:** [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)

---

## 1. Purpose

Tracks open compliance gaps, remediation owners, and due dates. Referenced by [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md) §9 and quarterly compliance reviews.

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Artefact or process exists in Magna Carta |
| 🎯 **External validation** | Requires signed contract, fee, audit, or operational run |

---

## 2. Open actions

| ID | Title | Owner | Due | Priority | Status | Validation |
|----|-------|-------|-----|----------|--------|------------|
| ACT-001 | Execute signed DPA with authorised PSP (SUP-003) | Legal / Procurement | 2026-08-31 | P0 | Open | 🎯 |
| ACT-002 | Countersign health connector BAA/DPA (SUP-005) | Legal / DPO | 2026-09-30 | P0 | Open | 🎯 |
| ACT-003 | Pay ICO fee; record live registration number | DPO | 2026-07-31 | P1 | Open | 🎯 |
| ACT-005 | Commission external penetration test | Security Ops | 2026-12-31 | P1 | Open | 🎯 |
| ACT-006 | Tranc3 HIPAA Tier A copy remediation PR | Platform Engineering | 2026-07-15 | P1 | In progress | 🎯 (local ✅; upstream merge pending) |
| ACT-007 | Policy attestation cycle (privileged roles) | HR / ISMS Lead | 2026-08-31 | P2 | Open | 🎯 |
| ACT-008 | SOC 2 observation period evidence collection | ISMS Lead | 2026-10-01 | P1 | Open | 🎯 |
| ACT-009 | magna_carta.py request-boundary enforcement | Platform Engineering | 2026-09-30 | P2 | Open | 🎯 |
| ACT-010 | SUP-004 US AI fallback DPA or disable decision | DPO / AI Lead | 2026-10-31 | P2 | Open | 🎯 |
| ACT-012 | Expand BCP restore tests (all P0 DBs) | Operations | 2027-06-07 | P2 | Open | 🎯 |
| ACT-016 | Appoint named individuals to 13 defined roles in HRIS | HR / Executive | 2026-09-30 | P2 | Open | 🎯 |
| ACT-017 | Complete premises fire risk assessment (FRA) | Facilities / H&S | 2026-10-31 | P2 | Open | 🎯 |
| ACT-018 | Activate payroll provider and live RTI reporting | Finance | 2026-12-31 | P2 | Open | 🎯 |
| ACT-019 | Name H&S officer and execute RIDDOR reporting drill | HR / H&S | 2026-09-30 | P2 | Open | 🎯 |

---

## 3. Recently closed actions (programme baselines)

| ID | Title | Closed | Evidence | Notes |
|----|-------|--------|----------|-------|
| ACT-004 | First PROC-AI-002 fairness/bias measurement run | 2026-06-09 | [FTR-2026-001](../evidence/reports/FTR-2026-001-baseline-fairness.md) (EEV-001) | ✅ Programme baseline; recurring PROC-AI-002 and production cohort testing remain 🎯 |
| ACT-011 | First internal audit (ISO programme) | 2026-06-09 | [IA-2026-01](../evidence/reports/IA-2026-01-baseline-internal-audit.md) (EEV-002) | ✅ Desk review; independent auditor and CAPA closure remain 🎯 |
| ACT-013 | First PROC-AI-003 AI security threat assessment (per model) | 2026-06-09 | [AST-2026-001–003](../evidence/proc-ai-003/) (EEV-003–005) | ✅ All three registered models; pen test (ACT-005) remains 🎯 |
| ACT-014 | First quarterly EU EUR-Lex delegated-act scan | 2026-06-09 | [EU-LEGISLATION-MONITORING §6](EU-LEGISLATION-MONITORING.md) SCAN-2026-Q2-01 (EEV-006) | ✅ Baseline scan; next quarterly due 2026-09-30 |
| ACT-015 | First semi-annual harmonised standards / ETSI watch | 2026-06-09 | [HARMONISED-STANDARDS-MONITORING §6](HARMONISED-STANDARDS-MONITORING.md) WATCH-2026-H1-01; [ETSI gap checklist](ETSI-EN-304-223-GAP-CHECKLIST.md) (EEV-007–008) | ✅ Baseline watch; OJEU adoption monitoring continues |

---

## 4. Programme milestones (selected)

| ID | Title | Closed | Notes |
|----|-------|--------|-------|
| PM-014 | Execution evidence wave (baseline ACT closures, external-action playbooks) | 2026-06-09 | `execution_evidence_register.yaml`, [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md) |
| PM-015 | Department packs (12 domains + HR bible) | 2026-06-09 | 16 bibles, 25 PROC/COOK/HYMN triads |
| PM-016 | Job description library (13 roles) | 2026-06-09 | `docs/job-descriptions/` |
| PM-017 | Programme layer 100% completion register | 2026-06-09 | [COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md](COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md) |
| — | Phase 3 supplier DPA register | 2026-06-07 | ✅ Programme; signed DPAs remain 🎯 |
| — | POL-AI-001 authored (framework) | 2026-06-07 | ✅ Programme; BoardRoom approval 🎯 |
| — | BCP baseline restore test BCP-RT-001 | 2026-06-07 | ✅ Programme baseline; annual repeat 🎯 |
| — | AI Governance Committee charter | 2026-06-07 | ✅ Programme |
| — | Phase 5 Tranc3 integration bridge (MC-011) | 2026-06-07 | ✅ Programme; ACT-009 staging 🎯 |

---

## 5. External validation playbook

Open 🎯 actions (ACT-001–003, ACT-005, ACT-007–010, ACT-012, ACT-016–019) use step-by-step playbooks in [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md). Machine-readable packages: `compliance/execution_evidence_register.yaml` → `external_action_packages`.

---

## 6. Workflow

1. **Raise** — New gap from audit, obligation review, incident, or risk register → assign ACT-### row.
2. **Track** — Owner updates status in quarterly PROC-CMP-001; YAML and this doc updated together.
3. **Close** — Evidence linked; status → Closed; change log in obligations register if applicable.
4. **Escalate** — P0 past due → CAB / executive notification.

---

## 7. Related documents

- [RISK-REGISTER.md](RISK-REGISTER.md)
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)
- [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md)
- [SOC2-EVIDENCE-SCHEDULE.md](SOC2-EVIDENCE-SCHEDULE.md)
- [../governance/INTERNAL-AUDIT-PROGRAMME.md](../governance/INTERNAL-AUDIT-PROGRAMME.md)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md)
- [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md)
- [HARMONISED-STANDARDS-MONITORING.md](HARMONISED-STANDARDS-MONITORING.md)
- [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md)
- [ETSI-EN-304-223-GAP-CHECKLIST.md](ETSI-EN-304-223-GAP-CHECKLIST.md)
- [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md)
- [EUR-LEX-ELI-REFERENCE.md](EUR-LEX-ELI-REFERENCE.md)
- [execution_evidence_register.yaml](../../compliance/execution_evidence_register.yaml)
- [../engineering/TRANC3-INTEGRATION-GUIDE.md](../engineering/TRANC3-INTEGRATION-GUIDE.md)

**Next review:** 2026-09-06 (PROC-CMP-001)
