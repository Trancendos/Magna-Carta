# Compliance Programme Completion Register

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** ISMS Lead  
**Purpose:** Authoritative inventory of **Layer 2 (programme)** artefacts at **100% in-repo completion**. Operational (Layer 3) gaps are listed explicitly — we do not conflate programme ✅ with certification or live evidence.

---

## 1. Programme layer status

| Metric | Count | Programme status | Operational note |
|--------|-------|------------------|------------------|
| **Layer 2 — Programme** | All applicable in-repo artefacts | **100%** ✅ | Complete for Magna Carta repository scope |
| **Layer 3 — Operational** | Open ACT-001–019 | **~42%** 🎯 | Requires fees, contracts, drills, HRIS, production |
| **End-to-end assurance** | Weighted blend | **~58%** | Programme without ops is not certification |

**Definition of 100% programme:** Every domain in the compliance scope has a bible (where applicable), procedure triad (PROC + COOK + HYMN), index entry, health-check coverage, and documented operational blockers. No applicable row is missing an owner document.

---

## 2. Documentation artefact inventory (complete)

### 2.1 Policies

| Count | Location | Status |
|-------|----------|--------|
| 9 | `docs/policies/POL-*.md` | ✅ Programme |

### 2.2 Procedures

| Count | Location | Status |
|-------|----------|--------|
| 25 | `docs/procedures/PROC-*.md` + INDEX | ✅ Programme |

### 2.3 Cookbooks

| Count | Location | Status |
|-------|----------|--------|
| 25 | `docs/cookbooks/COOK-*.md` + INDEX | ✅ Programme (drill evidence 🎯) |

### 2.4 Hymn sheets

| Count | Location | Status |
|-------|----------|--------|
| 25 | `docs/hymn-sheets/HYMN-*.md` + INDEX | ✅ Programme (named signatories 🎯) |

### 2.5 Bibles

| Count | Location | Status |
|-------|----------|--------|
| 16 | `docs/bibles/*-BIBLE.md` + INDEX | ✅ Programme |

Domains: Governance, Privacy, Security, HR, Health & Safety, Finance, Procurement, Legal, IP, Payroll, Building Regulations, IT, Wellbeing, Mental Health, User Management, Data Management.

### 2.6 Job descriptions

| Count | Location | Status |
|-------|----------|--------|
| 13 roles + template | `docs/job-descriptions/` + INDEX | ✅ Programme (HRIS appointments 🎯 ACT-016) |

### 2.7 Registers & schemas

| Artefact | Location | Status |
|----------|----------|--------|
| Framework catalogue (127 FW) | `frameworks_register.yaml` | ✅ Programme |
| Legislation register | `legislation_register.yaml` | ✅ Programme |
| Standards watch | `standards_watch.yaml` | ✅ Programme |
| Execution evidence | `execution_evidence_register.yaml` | ✅ Programme |
| Action tracker | `compliance_action_tracker.yaml` | ✅ Programme |
| JSON schemas (MON-009) | `compliance/schemas/*.schema.json` | ✅ Programme |
| Proactive signals + triggers | `proactive_signals.yaml`, `framework_triggers.yaml` | ✅ Programme |

### 2.8 Alignment & readiness docs

| Category | Status |
|----------|--------|
| Regulation matrix + coverage register | ✅ Programme |
| ISO / SOC / HIPAA / AI / EU / ETSI alignments | ✅ Programme |
| Future-readiness (CCPA, LGPD, POPIA, FedRAMP, CMMC, NHS DSPT, PCI position) | ✅ Programme |
| Maturity benchmark + AI scoping matrix | ✅ Programme |
| External action playbooks | ✅ Programme |

### 2.9 Automation & monitoring

| Check | Script / config | Status |
|-------|-----------------|--------|
| MON-001–018 health checks | `scripts/compliance_health_check.py` | ✅ Programme |
| Weekly local monitor | `scripts/weekly_compliance_health.sh` | ✅ Programme |
| Department artefact generator | `scripts/generate_department_artifacts.py` | ✅ Programme |
| Job description generator | `scripts/generate_job_descriptions.py` | ✅ Programme |
| Framework catalog generator | `scripts/generate_framework_implementation.py` | ✅ Programme |

**Last health check:** 0 errors, 2 warnings (SUP-003, SUP-005 DPA template issued — expected).

---

## 3. Department domain matrix (programme 100%)

| Domain | Bible | PROC | COOK | HYMN | Programme % | Operational blocker |
|--------|-------|------|------|------|-------------|---------------------|
| Governance | ✅ | PROC-CMP-001 | ✅ | ✅ | 100% | BoardRoom approvals 🎯 |
| Privacy | ✅ | PROC-DSR-001 | ✅ | ✅ | 100% | ICO fee, PECR UI 🎯 |
| Security | ✅ | PROC-IR/IAM/VUL | ✅ | ✅ | 100% | Pen test, MDM 🎯 |
| AI | ✅ | PROC-AI-002/003 | ✅ | ✅ | 100% | Board AI policy 🎯 |
| HR | ✅ | PROC-HR-001 | ✅ | ✅ | 100% | HRIS + screening 🎯 ACT-016 |
| Health & Safety | ✅ | PROC-HSE-001 | ✅ | ✅ | 100% | H&S lead, RIDDOR 🎯 ACT-019 |
| Finance | ✅ | PROC-FIN-001 | ✅ | ✅ | 100% | Accountant sign-off 🎯 |
| Procurement | ✅ | PROC-PRM-001 | ✅ | ✅ | 100% | Signed DPAs 🎯 ACT-001/002 |
| Legal | ✅ | PROC-LEG-001 | ✅ | ✅ | 100% | CLM playbook 🎯 |
| IP | ✅ | PROC-IP-001 | ✅ | ✅ | 100% | Legal IP register 🎯 |
| Payroll | ✅ | PROC-PAY-001 | ✅ | ✅ | 100% | RTI live 🎯 ACT-018 |
| Building Regulations | ✅ | PROC-BLD-001 | ✅ | ✅ | 100% | FRA on premises 🎯 ACT-017 |
| IT | ✅ | PROC-IT-001 | ✅ | ✅ | 100% | ITSM in production 🎯 |
| Wellbeing | ✅ | PROC-WLB-001 | ✅ | ✅ | 100% | Programme launch 🎯 |
| Mental Health | ✅ | PROC-MHL-001 | ✅ | ✅ | 100% | MH first aiders 🎯 |
| User Management | ✅ | PROC-UMG-001 | ✅ | ✅ | 100% | Tranc3 admin SOP 🎯 ACT-009 |
| Data Management | ✅ | PROC-DAT-001 | ✅ | ✅ | 100% | Data steward roster 🎯 |
| Framework catalogue | 127 FW | Catalog + triggers | — | — | 100% | External certs 🎯 |

---

## 4. Programme milestones (PM-001–PM-017)

| ID | Title | Closed |
|----|-------|--------|
| PM-001 | COMPLIANCE-COVERAGE-REGISTER | 2026-06-07 |
| PM-002 | Future-scenario readiness alignments | 2026-06-07 |
| PM-003 | ISO/SOC programme artefacts | 2026-06-07 |
| PM-004 | Pen-test future scope and TIA templates | 2026-06-07 |
| PM-005 | Full JSON Schema coverage (MON-009) | 2026-06-08 |
| PM-006 | Procedure coverage — 25 cookbooks + 25 hymn sheets (MON-010) | 2026-06-08 |
| PM-007 | Domain bibles, runbooks, ASVS gap checklist | 2026-06-08 |
| PM-008 | Evidence templates for ACT-004 and ACT-011 | 2026-06-08 |
| PM-009 | Master standards & frameworks catalogue | 2026-06-08 |
| PM-010 | Layer 3 external validation backlog documented | 2026-06-08 |
| PM-011 | OWASP AI Exchange programme wave | 2026-06-08 |
| PM-012 | EUR-Lex / ELI programme wave | 2026-06-08 |
| PM-013 | ETSI SAI / harmonised standards wave | 2026-06-08 |
| PM-014 | Execution evidence wave | 2026-06-09 |
| PM-015 | Department packs (12 domains + HR bible) | 2026-06-09 |
| PM-016 | Job description library (13 roles + template) | 2026-06-09 |
| PM-017 | Programme layer 100% — completion register published | 2026-06-09 |

---

## 5. What remains for operational 100%

These items **cannot** be closed by documentation alone. See [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md) and [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md).

| ID | Item | Owner |
|----|------|-------|
| ACT-001 | Signed PSP DPA | Legal / Procurement |
| ACT-002 | Health connector BAA/DPA | Legal / DPO |
| ACT-003 | ICO fee + registration | DPO |
| ACT-005 | External pen test | Security Ops |
| ACT-006 | Tranc3 HIPAA copy PR | Platform Engineering |
| ACT-007 | Policy attestation cycle | HR / ISMS |
| ACT-008 | SOC 2 observation window | ISMS Lead |
| ACT-009 | magna_carta.py production enforce | Platform Engineering |
| ACT-010 | SUP-004 DPA or disable | DPO / AI Lead |
| ACT-012 | BCP all P0 DBs | Operations |
| ACT-016 | HRIS appointments for 13 defined roles | HR / Executive |
| ACT-017 | Premises fire risk assessment | Facilities / H&S |
| ACT-018 | Payroll provider + RTI live | Finance |
| ACT-019 | H&S officer named + RIDDOR drill | HR / H&S |

**Closed programme baselines:** ACT-004, ACT-011, ACT-013, ACT-014, ACT-015 (evidence EEV-001–008).

---

## 6. Review

| Activity | Frequency | Next |
|----------|-----------|------|
| Reconcile this register with health check | After each major wave | On change |
| Confirm programme 100% still holds | Quarterly (PROC-CMP-001) | 2026-09-30 |
| Report operational % honestly | Quarterly | 2026-09-30 |

**Related:** [COMPLIANCE-MATURITY-AND-BENCHMARK.md](COMPLIANCE-MATURITY-AND-BENCHMARK.md) · [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md) · [DOCUMENTATION-ARTIFACT-MODEL.md](../governance/DOCUMENTATION-ARTIFACT-MODEL.md)
