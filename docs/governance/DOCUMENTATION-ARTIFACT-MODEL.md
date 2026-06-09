# Documentation Artifact Model

**Version:** 1.1.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Purpose:** Define every documentation category in Magna Carta — what it is, where it lives, who maintains it, and how it is monitored.

---

## 1. Honest scope statement

Magna Carta **layer 2** (this repository) is strong on policies, procedures, alignment docs, and machine-readable registers. It was **weaker** on operational playbooks (cookbooks), canonical reference bibles, quick checklists (hymn sheets), and automated freshness monitoring until the **artifact model wave** (2026-06-07).

**Operational layer 3** (signed contracts, drills, attestations, certification) remains tracked in [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) and ACT-001–012.

---

## 2. Artifact taxonomy

| Category | Definition | Magna Carta location | Tranc3 / Town Hall | Maintainer |
|----------|------------|----------------------|--------------------|------------|
| **Policies** | Board-level rules — what we must do | `docs/policies/` | — | ISMS Lead + DPO |
| **Procedures** | Step-by-step process — how we do it | `docs/procedures/` | Town Hall templates | Process owner |
| **Templates** | Reusable legal/contract forms | `docs/templates/` | — | Legal / DPO |
| **Alignment docs** | Framework/regulation mapping | `docs/compliance/*-ALIGNMENT.md` | `register.yaml` | ISMS Lead |
| **Registers** | Structured inventories (human + YAML) | `docs/compliance/`, `compliance/*.yaml` | Tranc3 registers | Register owner |
| **Cookbooks** | Scenario playbooks — *do this now* | `docs/cookbooks/` | `townhall/templates/cookbook.md` | Ops / ISMS |
| **Bibles** | Canonical reference — *how the system works* | `docs/bibles/` | `frameworks.yaml` (bibles-guides) | ISMS Lead |
| **Hymn sheets** | One-page aligned checklists | `docs/hymn-sheets/` | — | Procedure owner |
| **Schemas** | Field definitions for registers/YAML | `docs/schemas/` | Obligation schema in OBLIGATIONS-REGISTER §3 | ISMS Lead |
| **Standards** | External normative references | [STANDARDS-REGISTER.md](../compliance/STANDARDS-REGISTER.md) | DEFSTAN in CI | ISMS Lead |
| **Regulators** | Supervisory authorities we engage | [REGULATORS-OMBUDSMEN-REGISTER.md](../compliance/REGULATORS-OMBUDSMEN-REGISTER.md) | — | DPO / Legal |
| **Ombudsmen** | Independent dispute resolution bodies | Same register | — | Legal / Customer Success |
| **Systems** | Platform and tooling inventory | [SYSTEMS-REGISTER.md](../compliance/SYSTEMS-REGISTER.md) | AS-BUILT-ARCHITECTURE | Platform Engineering |
| **Reviewers** | Who reviews what, when | [REVIEWERS-REGISTER.md](REVIEWERS-REGISTER.md) | RACI-MATRIX | ISMS Lead |
| **Evidence** | Proof of operation | `docs/evidence/` | CI artefacts, logs | Security Ops / ISMS |
| **Governance** | Charters, audit, PDCA | `docs/governance/` | BoardRoom | ISMS Lead |
| **Architecture** | As-built truth | `docs/architecture/` | Tranc3 docs (aspirational) | Platform Engineering |

---

## 3. Relationship diagram

```
                    ┌──────────────┐
                    │   BIBLE      │  canonical "how governance runs"
                    └──────┬───────┘
                           │ informs
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   ┌──────────┐     ┌──────────┐      ┌──────────┐
   │ POLICIES │────►│PROCEDURES│─────►│COOKBOOKS │  operational playbooks
   └──────────┘     └────┬─────┘      └────┬─────┘
                         │                 │
                         ▼                 ▼
                   ┌──────────┐      ┌──────────┐
                   │ REGISTERS│      │HYMN SHEET│  quick checklists
                   │ + SCHEMA │      └──────────┘
                   └────┬─────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
   STANDARDS      REGULATORS/      SYSTEMS
                  OMBUDSMEN
                        │
                        ▼
              REVIEWERS + MAINTENANCE MONITOR
```

---

## 4. Cookbooks vs procedures vs hymn sheets

| Aspect | Procedure | Cookbook | Hymn sheet |
|--------|-----------|----------|------------|
| Audience | Auditors, compliance | Operators on call | Anyone executing a task |
| Detail | Full RACI, evidence, calendar | Step-by-step with decision trees | Checkbox only |
| Change control | CAB / policy cycle | Quarterly review | Version tied to procedure |
| Example | PROC-IR-001 | COOK-IR-001 | HYMN-IR-001 |

**Rule:** Every P0 procedure should have at least one cookbook and one hymn sheet within 12 months of procedure publication.

---

## 5. Bibles vs FRAMEWORK.md

| Document | Role |
|----------|------|
| [FRAMEWORK.md](../../FRAMEWORK.md) | Master blueprint — layers, certification roadmap |
| [MAGNACARTA-GOVERNANCE-BIBLE.md](../bibles/MAGNACARTA-GOVERNANCE-BIBLE.md) | Day-to-day governance encyclopaedia — registers, cadence, escalation |

FRAMEWORK is strategic; the Bible is operational reference.

---

## 6. Maintenance and monitoring

All artefacts are subject to [COMPLIANCE-MAINTENANCE-PROGRAMME.md](COMPLIANCE-MAINTENANCE-PROGRAMME.md):

- **Automated (local):** `scripts/compliance_health_check.py` and `scripts/weekly_compliance_health.sh` — no GitHub Actions (zero CI minute cost)
- **Optional cron:** `scripts/install_local_weekly_cron.sh` on ISMS workstation
- **Machine-readable config:** `compliance/maintenance_monitor.yaml`
- **Human cadence:** PROC-CMP-001 quarterly review
- **Checks:** MON-001–MON-010 (see [COMPLIANCE-MAINTENANCE-PROGRAMME.md](COMPLIANCE-MAINTENANCE-PROGRAMME.md))

---

## 7. Completeness checklist (artifact model)

| Category | Status (2026-06-08) | Notes |
|----------|---------------------|-------|
| Policies | ✅ 9 policies | BoardRoom approval 🎯 |
| Procedures | ✅ 13 procedures | — |
| Cookbooks | ✅ 12 + INDEX (MON-010) | Operational drills not evidenced 🎯 |
| Bibles | ✅ 3 + INDEX (gov, privacy, security) | Expand as domains mature |
| Hymn sheets | ✅ 12 + INDEX (MON-010) | Named signatories in production 🎯 |
| Schemas | ✅ REGISTER-SCHEMAS + 9 JSON schemas | MON-009 validates all YAML registers |
| Runbooks | ✅ 2 + INDEX | Ombudsman, PECR deployment |
| Evidence templates | ✅ 7 (incl. fairness + internal audit) | Execution pending ACT-004, ACT-011 🎯 |
| Standards register | ✅ | Linked from REGULATION-MATRIX |
| Regulators / Ombudsmen | ✅ | ICO, FCA, FOS, etc. |
| Systems register | ✅ | Derived from AS-BUILT |
| Reviewers register | ✅ | Named individuals external 🎯 |
| Automated monitor | ✅ | Local weekly health check + history log |

---

## 8. Review

| Activity | Frequency | Next |
|----------|-----------|------|
| Artifact model review | Annual | 2027-06-07 |
| Gap scan (cookbook/hymn coverage) | Quarterly (PROC-CMP-001) | 2026-09-06 |

**Related:** [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) · [COMPLIANCE-MAINTENANCE-PROGRAMME.md](COMPLIANCE-MAINTENANCE-PROGRAMME.md)
