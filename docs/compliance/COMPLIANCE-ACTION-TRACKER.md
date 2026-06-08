# Compliance Action Tracker

**Version:** 1.0.0  
**Date:** 2026-06-07  
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
| ACT-004 | First PROC-AI-002 fairness/bias measurement run | AI Lead | 2026-09-30 | P1 | Open | 🎯 |
| ACT-005 | Commission external penetration test | Security Ops | 2026-12-31 | P1 | Open | 🎯 |
| ACT-006 | Tranc3 HIPAA Tier A copy remediation PR | Platform Engineering | 2026-07-15 | P1 | In progress | 🎯 (local ✅; upstream merge pending) |
| ACT-007 | Policy attestation cycle (privileged roles) | HR / ISMS Lead | 2026-08-31 | P2 | Open | 🎯 |
| ACT-008 | SOC 2 observation period evidence collection | ISMS Lead | 2026-10-01 | P1 | Open | 🎯 |
| ACT-009 | magna_carta.py request-boundary enforcement | Platform Engineering | 2026-09-30 | P2 | Open | 🎯 |
| ACT-010 | SUP-004 US AI fallback DPA or disable decision | DPO / AI Lead | 2026-10-31 | P2 | Open | 🎯 |
| ACT-011 | First internal audit (ISO programme) | ISMS Lead | 2026-12-31 | P2 | Open | 🎯 |
| ACT-012 | Expand BCP restore tests (all P0 DBs) | Operations | 2027-06-07 | P2 | Open | 🎯 |

---

## 3. Recently closed (programme milestones)

| ID | Title | Closed | Notes |
|----|-------|--------|-------|
| — | Phase 3 supplier DPA register | 2026-06-07 | ✅ Programme; signed DPAs remain 🎯 |
| — | POL-AI-001 authored (framework) | 2026-06-07 | ✅ Programme; BoardRoom approval 🎯 |
| — | BCP baseline restore test BCP-RT-001 | 2026-06-07 | ✅ Programme baseline; annual repeat 🎯 |
| — | AI Governance Committee charter | 2026-06-07 | ✅ Programme |
| — | Phase 5 Tranc3 integration bridge (MC-011) | 2026-06-07 | ✅ Programme; ACT-009 staging 🎯 |

---

## 4. Workflow

1. **Raise** — New gap from audit, obligation review, incident, or risk register → assign ACT-### row.
2. **Track** — Owner updates status in quarterly PROC-CMP-001; YAML and this doc updated together.
3. **Close** — Evidence linked; status → Closed; change log in obligations register if applicable.
4. **Escalate** — P0 past due → CAB / executive notification.

---

## 5. Related documents

- [RISK-REGISTER.md](RISK-REGISTER.md)
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)
- [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md)
- [SOC2-EVIDENCE-SCHEDULE.md](SOC2-EVIDENCE-SCHEDULE.md)
- [../governance/INTERNAL-AUDIT-PROGRAMME.md](../governance/INTERNAL-AUDIT-PROGRAMME.md)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md)
- [../engineering/TRANC3-INTEGRATION-GUIDE.md](../engineering/TRANC3-INTEGRATION-GUIDE.md)

**Next review:** 2026-09-06 (PROC-CMP-001)
