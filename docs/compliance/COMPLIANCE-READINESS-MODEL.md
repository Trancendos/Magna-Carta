# Compliance Readiness Model

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** ISMS Lead  
**Purpose:** Separate what this repository can **build and verify** from what only the **owner** can execute at go-live.

---

## 1. Three layers (read this first)

| Layer | Name | Who closes it | Honest % target |
|-------|------|---------------|-----------------|
| **A** | Programme | Documentation in git | **100%** ✅ |
| **B** | Automation & systems readiness | Scripts, registers, gates, templates — verifiable locally | **100%** (agent scope) |
| **C** | Owner go-live gates | Fees, signatures, live vendors, external audits, hiring | **Not scored for agents** |

**Rule:** Agents and local automation report **Layer B** only. Layer C is tracked in `compliance_action_tracker.yaml` with `executor: owner` but does **not** reduce the automation-readiness percentage.

---

## 2. What is a DPA?

A **Data Processing Agreement (DPA)** is the UK GDPR Art. 28 contract between controller and processor. It defines:

- Subject matter and duration of processing  
- Nature and purpose of processing  
- Types of personal data and categories of data subjects  
- Controller obligations and processor instructions  
- Sub-processor disclosure and change notification  
- Security measures, breach notification, deletion/return  
- International transfer mechanism (UK IDTA, SCCs, adequacy)

**What we can automate (Layer B):**

| Control | Artefact | Script |
|---------|----------|--------|
| Template exists | `docs/templates/TEMPLATE-DPA-UK-GDPR.md` | `dpa_readiness_check.py` |
| Supplier register | `compliance/supplier_dpa_register.yaml` | MON-006, MON-014 |
| Onboarding checklist | Register `onboarding_checklist` | Health check |
| Production gate | MON-014 warns when critical supplier unsigned **and** profile enabled | `compliance_health_check.py` |

**What only the owner does (Layer C):** countersign DPAs, upload signed PDFs, enable `PAYMENTS_LIVE` / `HIPAA_PROFILE` in production.

---

## 3. Production controls, attestations, supplier assurance

These are **systems to set up**, not agent tasks to perform on your behalf.

| Area | System (Layer B) | Owner gate (Layer C) |
|------|------------------|----------------------|
| **Production controls** | `config/magna_carta_config.json` profiles + MON-016 enforcement alignment | Flip profiles to `enabled` in prod |
| **Policy attestation** | `compliance/policy_attestation_register.yaml`, PROC-TRN-001, HYMN-TRN-001 | HR collects signatures in HRIS |
| **Supplier assurance** | `supplier_dpa_register.yaml`, POL-SUP-001, MON-014 | Signed DPAs on file |
| **Certification evidence** | `compliance/certification_evidence_register.yaml`, `docs/evidence/certifications/` | Upload audit letters / certs |

Assume named roles are filled when registers and job descriptions exist; the agent does not manage HRIS appointments.

---

## 4. Security testing (continuous vs annual)

| Type | Purpose | Layer | Tooling |
|------|---------|-------|---------|
| **Continuous SAST / secrets** | Every change; catch regressions early | B | Aikido MCP + `scripts/run_security_testing.py` |
| **Compliance health** | Register freshness, gates, coverage | B | `compliance_health_check.py` |
| **Annual external pen test** | Adversarial validation for assurance | C | ACT-005 — owner commissions provider |

Aikido is **not** a replacement for an external pen test. It is the **continuous testing framework** you asked for. See [AIKIDO-SECURITY-TESTING-FRAMEWORK.md](AIKIDO-SECURITY-TESTING-FRAMEWORK.md).

---

## 5. HRIS, FRA, payroll, RIDDOR (ACT-016–019 reinterpreted)

| Action | Was described as | Layer B (system readiness) | Layer C (owner only) |
|--------|------------------|----------------------------|----------------------|
| ACT-016 | Appoint 13 roles in HRIS | Role register + 13 JDs + REVIEWERS-REGISTER | Enter names in HRIS |
| ACT-017 | Complete premises FRA | PROC-BLD-001, BUILDING-BIBLE, premises readiness register | Commission signed FRA |
| ACT-018 | Activate payroll + RTI | PROC-PAY-001, PAYROLL-BIBLE, payroll readiness register | Contract payroll provider |
| ACT-019 | H&S officer + RIDDOR drill | PROC-HSE-001, HSE-BIBLE, drill template in evidence | Name officer; run live drill |

Programme milestones **SYS-016–019** in `compliance/readiness_automation_register.yaml` mark system readiness **closed**. ACT-016–019 remain open as owner gates.

---

## 6. External audits and certifications

The agent **cannot** confirm an external audit occurred without evidence on disk.

**Workflow:**

1. Owner drops certificate or report into `docs/evidence/certifications/` (see README there).  
2. Register row updated in `certification_evidence_register.yaml`.  
3. `scripts/readiness_automation_score.py` and optional analysis scripts verify file presence and metadata.

Until files are uploaded, status stays `pending_upload` — this is expected in pre-go-live mode.

---

## 7. How to read percentages

| Metric | Command | Meaning |
|--------|---------|---------|
| Programme layer | `compliance_action_tracker.yaml` → `programme_layer_percent` | Layer A |
| **Automation readiness** | `python3 scripts/readiness_automation_score.py` | **Layer B — agent scope** |
| Owner gates open | Count `executor: owner` actions with status Open | Layer C backlog |
| Health check | `python3 scripts/compliance_health_check.py --report` | Operational hygiene |

**We target 100% on Layer B.** Layer C items are listed but excluded from agent completion scoring.

---

## 8. Related documents

- [COMPLIANCE-MATURITY-AND-BENCHMARK.md](COMPLIANCE-MATURITY-AND-BENCHMARK.md)  
- [COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md](COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md)  
- [AIKIDO-SECURITY-TESTING-FRAMEWORK.md](AIKIDO-SECURITY-TESTING-FRAMEWORK.md)  
- [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md) — playbooks for Layer C when you choose to execute
