# Internal Audit Report — Baseline Desk Review (ISO 27001 §9.2)

**Audit ID:** IA-2026-01  
**Report date:** 2026-06-09  
**Owner:** ISMS Lead  
**Status:** ✅ Programme baseline · 🎯 Independent auditor cycle pending

---

## Report metadata

| Field | Value |
|-------|-------|
| Audit ID | IA-2026-01 |
| Audit title | Magna Carta ISMS baseline desk review |
| Planned window | 2026-Q2 |
| Lead auditor | ISMS Lead (independent of daily ops where practicable) |
| Auditee | Platform Engineering / DPO |
| Criteria | ISO 27001:2022 Annex A sample; MC-001–MC-011; SOC 2 CC mapping |

---

## 1. Executive summary

- **Overall conclusion:** Conforming with minor gaps
- **Scope summary:** Documentation programme, access control samples, supplier register, AI governance artefacts, BCP baseline
- **Finding counts:** Major 0 · Minor 2 · Observation 3 · Opportunity 2

---

## 2. Audit scope and criteria

| Domain | In scope? | Sample | Evidence |
|--------|-----------|--------|----------|
| Access management | Yes | JWT/RBAC review | POL-SEC-002, PROC-IAM-001 |
| Change & release | Yes | PROC-CHG-001 | Git/Forgejo |
| Incident & IR | Yes | PROC-IR-001 outline | IR tabletop reference |
| Privacy & DSR | Yes | GDPR programme | OBL-001–008 |
| Supplier & DPA | Yes | SUP-001–005 | supplier_dpa_register.yaml |
| BCP & backup | Partial | BCP-RT-001 only | ACT-012 open |
| AI governance | Yes | PROC-AI-001–003 | AI-GOVERNANCE, EEV-003–005 |
| Magna Carta programme | Yes | Registers + health check | compliance_health_check.py |

**Exclusions:** Tranc3 upstream code audit (ACT-009); live ICO registration (ACT-003).

---

## 3. Findings

### 3.1 Major nonconformities

None.

### 3.2 Minor nonconformities

| ID | Control | Finding | Action |
|----|---------|---------|--------|
| IA-M-01 | A.5.19 | SUP-003 DPA unsigned | ACT-001 |
| IA-M-02 | A.5.30 | BCP restore not all P0 DBs | ACT-012 |

### 3.3 Observations

| ID | Topic | Observation |
|----|-------|-------------|
| IA-O-01 | Attestation | Policy attestation register empty — ACT-007 |
| IA-O-02 | Pen test | No external pen test this cycle — ACT-005 |
| IA-O-03 | SOC 2 | Observation period not started — ACT-008 |

### 3.4 Opportunities

| ID | Topic | Suggestion |
|----|-------|------------|
| IA-P-01 | Automation | execution_evidence_register.yaml improves traceability |
| IA-P-02 | Standards | ETSI EN 304 223 gap checklist aids PROC-AI-003 |

---

## 4. Corrective action plan

| Finding | Action | Owner | Due | ACT |
|---------|--------|-------|-----|-----|
| IA-M-01 | Execute PSP DPA | Legal | 2026-08-31 | ACT-001 |
| IA-M-02 | Schedule vault/Forgejo restore | Operations | 2027-06-07 | ACT-012 |

---

## 5. Sign-off

| Role | Date | Reference |
|------|------|-----------|
| ISMS Lead | 2026-06-09 | EEV-002 |

**Next audit:** Independent engagement target 2026-Q4 (external validation)
