# Compliance Maturity & External Benchmark

**Version:** 1.2.0  
**Date:** 2026-06-09  
**Owner:** ISMS Lead  
**Purpose:** Honest completion percentages, Vanta-class CCM comparison, and what cannot be closed inside this repository alone.

---

## 1. How to read completion percentages

| Layer | What it measures | Honest % (2026-06-09) |
|-------|------------------|------------------------|
| **Layer A — Programme** | Policies, procedures, bibles, registers, mappings, local monitors | **100%** ✅ |
| **Layer B — Automation & systems** | Scripts, registers, gates, templates, cert vault slots — agent-verifiable | **100%** ✅ (run `scripts/readiness_automation_score.py`) |
| **Layer C — Owner go-live gates** | ICO fee, signed DPAs, HRIS names, external pen test, cert uploads | **Open** (not scored; see action tracker `executor: owner`) |
| **End-to-end assurance** | Programme + automation + live operations | **~58%** 🎯 |

See [COMPLIANCE-READINESS-MODEL.md](COMPLIANCE-READINESS-MODEL.md) for the A/B/C split. **Layer B is the agent scope; Layer C is yours at go-live.**

**We claim 100% programme (in-repo).** We do **not** claim 100% operational or certification. Inventory: [COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md](COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md).

---

## 2. Programme completion by domain

| Domain | Bible | Procedure triad | Policies linked | Programme % | Operational blocker |
|--------|-------|-----------------|-----------------|-------------|---------------------|
| Governance | BIB-GOV-001 ✅ | PROC-CMP-001 ✅ | All | 100% | BoardRoom approvals 🎯 |
| Privacy | BIB-PRI-001 ✅ | PROC-DSR-001 ✅ | POL-PRI-001 ✅ | 100% | ICO fee, live PECR UI 🎯 |
| Security | BIB-SEC-001 ✅ | PROC-IR/IAM/VUL ✅ | POL-SEC-* ✅ | 100% | Pen test, MDM 🎯 |
| AI | AI-GOVERNANCE ✅ | PROC-AI-002/003 ✅ | POL-AI-001 ✅ | 100% | Board AI policy approval 🎯 |
| HR | HR-BIBLE ✅ | PROC-HR-001 ✅ | POL-SEC-* ✅ | 100% | HRIS + screening vendor 🎯 ACT-016 |
| Health & Safety | HSE-BIBLE ✅ | PROC-HSE-001 ✅ | POL-SEC-001 (interim) | 100% | H&S officer; RIDDOR drill 🎯 ACT-019 |
| Finance | FINANCE-BIBLE ✅ | PROC-FIN-001 ✅ | COMPANIES-ACT alignment | 100% | External accountant sign-off 🎯 |
| Procurement | PROCUREMENT-BIBLE ✅ | PROC-PRM-001 ✅ | POL-SUP-001 ✅ | 100% | Signed supplier DPAs 🎯 ACT-001/002 |
| Legal | LEGAL-BIBLE ✅ | PROC-LEG-001 ✅ | Templates ✅ | 100% | Contract playbook in CLM 🎯 |
| Intellectual Property | IP-BIBLE ✅ | PROC-IP-001 ✅ | — | 100% | IP register in legal system 🎯 |
| Payroll | PAYROLL-BIBLE ✅ | PROC-PAY-001 ✅ | — | 100% | Payroll provider + RTI live 🎯 ACT-018 |
| Building Regulations | BUILDING-BIBLE ✅ | PROC-BLD-001 ✅ | — | 100% | Premises survey / FRA 🎯 ACT-017 |
| IT | IT-BIBLE ✅ | PROC-IT-001 ✅ | POL-SEC-001 ✅ | 100% | ITSM tickets in production 🎯 |
| Wellbeing | WELLBEING-BIBLE ✅ | PROC-WLB-001 ✅ | — | 100% | Wellbeing programme launch 🎯 |
| Mental Health | MENTAL-HEALTH-BIBLE ✅ | PROC-MHL-001 ✅ | — | 100% | MH first aiders trained 🎯 |
| User Management | USER-MANAGEMENT-BIBLE ✅ | PROC-UMG-001 ✅ | POL-SEC-001 ✅ | 100% | Tranc3 admin SOP in prod 🎯 ACT-009 |
| Data Management | DATA-MANAGEMENT-BIBLE ✅ | PROC-DAT-001 ✅ | POL-PRI-001 ✅ | 100% | Data steward roster 🎯 |
| Framework catalogue | 127 FW register ✅ | Catalog + triggers ✅ | — | 100% | External cert audits 🎯 |

**Department pack wave (PM-015):** All domains now have bible + PROC/COOK/HYMN at programme 100%. Operational gaps tracked in ACT-016–019.

---

## 3. Comparison to Vanta (and Drata / Secureframe class)

**Note:** The codebase contains **no Vanta integration**. User query referenced "Vanta and Akido" — **Akido is not referenced in this repo**; treat as Vanta-class **continuous compliance monitoring (CCM)** unless clarified (e.g. Aikido security scanning is a different product category).

| Capability | Magna Carta (this repo) | Vanta-class SaaS CCM |
|------------|-------------------------|----------------------|
| Framework catalogue | ✅ 127 FW, YAML registers, readiness index | Pre-built SOC2/ISO/HIPAA packs |
| Control mapping | ✅ Alignment docs + implementation catalog | Auto-mapped + vendor templates |
| Policy/procedure library | ✅ Authored, versioned in git | Hosted + attestation workflows |
| Continuous monitoring | ✅ Local `compliance_health_check.py` (MON-001–018) | Cloud agents, API integrations |
| Personnel / HRIS evidence | 📋 PROC-HR-001; no HRIS connector | Often integrated (BambooHR, etc.) |
| Vendor risk / DPAs | ✅ Register + MON-014 warnings | Workflow + renewal reminders |
| Evidence collection | Manual `docs/evidence/` + registers | Automated screenshots, API pulls |
| Audit preparation | ✅ Internal audit programme | Auditor collaboration portal |
| Certifications | Mapped; not obtained | Audit support bundles |
| Cost model | Zero SaaS (local scripts) | Subscription per framework |
| Custom frameworks | ✅ Full YAML extensibility | Limited to vendor catalogue |
| AI governance depth | ✅ Strong (EU AI Act, OWASP AI, PROC-AI-003) | Varies; often SOC2-first |

### Where Magna Carta is **stronger or equivalent**

- Depth of **multi-framework catalogue** (127 FW) with explicit NA/readiness posture
- **AI security programme** (threat model, scoping matrix, PROC-AI-003 assurance grid)
- **Vendor-neutral** architecture documentation tied to Tranc3 controls
- **Git-auditable** policy history without SaaS lock-in

### Where Vanta-class tools are **ahead**

- **Automated evidence** from AWS, GCP, GitHub, Okta, etc.
- **Personnel tracking** (background checks, training completion dashboards)
- **Vendor questionnaire** automation and renewal nudges
- **Customer-facing trust centre** and auditor portals
- **Real-time control monitoring** with integration health

### Honest positioning

Magna Carta at **100% programme / ~42% operational** is comparable to a **fully documented pre-Vanta organisation** that has completed GRC structure in git but not yet wired integrations or completed audit windows. It is **not** a substitute for a CCM SaaS unless integrations are built (ACT-009 Tranc3 enforce, HRIS ACT-016, IdP, cloud APIs).

---

## 4. What remains (cannot complete in-repo only)

| ID | Item | Owner | Why external |
|----|------|-------|--------------|
| ACT-001 | ICO registration fee paid | Finance / DPO | Payment + live number |
| ACT-002 | HIPAA Tier C BAAs signed | Legal | Per-customer contracts |
| ACT-003 | BoardRoom policy approvals | Executive | Board minutes |
| ACT-005 | Penetration test execution | Security Ops | Third-party tester |
| ACT-008 | SOC 2 observation window | ISMS | 6-month clock |
| ACT-009 | Tranc3 Magna Carta production enforce | Engineering | Runtime deployment |
| ACT-010 | SUP-004 DPA + TIA | Legal / DPO | Signed DPA |
| ACT-011 | ISO 27001 external certification | ISMS | CB audit |
| ACT-012 | BCP drills all P0 DBs | Operations | Executed restores |
| ACT-013 | PROC-AI-003 recurring evidence | AI Lead | Quarterly cycles |
| ACT-016 | HRIS appointments (13 roles) | HR / Executive | Live HR records |
| ACT-017 | Premises fire risk assessment | Facilities / H&S | On-site assessment |
| ACT-018 | Payroll provider + RTI live | Finance | HMRC live reporting |
| ACT-019 | H&S officer named + RIDDOR drill | HR / H&S | Training + drill log |
| — | MDM / endpoint DLP | IT | Tooling rollout |

Full tracker: [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md)

---

## 5. Path to operational parity with CCM tools

1. **Integrate evidence sources** — IdP (access reviews), HRIS (training), cloud (config drift) into `docs/evidence/` or Tranc3 collector
2. **Close ACT-001–015** in order of audit criticality (DPAs, pen test, SOC2 window)
3. **Enable Tranc3 enforcement** (ACT-009) for Magna Carta rules in staging → production
4. **Optional:** Evaluate Vanta/Drata **only if** integration labour exceeds maintenance cost of local MON-* checks

---

## 6. Review cadence

| Activity | Frequency | Next |
|----------|-----------|------|
| Update percentages in this doc | Quarterly (PROC-CMP-001) | 2026-09-30 |
| Re-benchmark vs CCM market | Annual | 2027-06-09 |

**Related:** [COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md](COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md) · [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md) · [DOCUMENTATION-ARTIFACT-MODEL.md](../governance/DOCUMENTATION-ARTIFACT-MODEL.md)
