# External Action Execution Guide

**Version:** 1.1.0  
**Date:** 2026-06-09  
**Owner:** ISMS Lead  
**Machine-readable:** [compliance/execution_evidence_register.yaml](../../compliance/execution_evidence_register.yaml) → `external_action_packages`  
**Tracker:** [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md)

---

## 1. Purpose

Playbooks for **ACT-001–ACT-019** items that cannot close from repository work alone. Each section defines prerequisites, step-by-step execution, evidence to collect, and how to close the action in `compliance_action_tracker.yaml`.

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Templates, registers, or baseline runs exist in Magna Carta |
| 🎯 **External validation** | Requires signed contract, fee, live operation, or third-party attestation |

**Baseline executions (closed 2026-06-09):** ACT-004, ACT-011, ACT-013, ACT-014, ACT-015 — see `execution_evidence_register.yaml` records EEV-001–EEV-008.

---

## 2. How to use this guide

1. Open the action row in [compliance/compliance_action_tracker.yaml](../../compliance/compliance_action_tracker.yaml).
2. Follow the matching §3.x playbook below.
3. Store evidence under `docs/evidence/` or update the target compliance doc named in the action.
4. On completion: set `status: Closed`, `closed_date`, `evidence_ref`; mirror in COMPLIANCE-ACTION-TRACKER.md.
5. Quarterly PROC-CMP-001 reviews open external actions for overdue P0/P1 items.

---

## 3. Playbooks

### 3.1 SUP-003 PSP DPA (ACT-001)

| Field | Value |
|-------|-------|
| Owner | Legal / Procurement |
| Priority | P0 |
| Source | OBL-003, `supplier_dpa_register.yaml` SUP-003 |

**Prerequisites:** ✅ DPA template in supplier register; procurement authority identified.

**Steps:**

1. Confirm authorised payment service provider entity and processing annex.
2. Legal review against GDPR Art. 28 and UK GDPR processor requirements.
3. Execute countersigned DPA; store in contract repository (not in git).
4. Update `supplier_dpa_register.yaml`: `dpa_status: Signed`, `signed_date`, `evidence_location` (internal ref).
5. Close ACT-001; note evidence ref in PROC-CMP-001 minutes.

**Evidence target:** Signed DPA on file; SUP-003 status → Signed.

---

### 3.2 SUP-005 health connector BAA/DPA (ACT-002)

| Field | Value |
|-------|-------|
| Owner | Legal / DPO |
| Priority | P0 |
| Source | HIPAA-ALIGNMENT §4, MC-008 |

**Prerequisites:** ✅ BAA/DPA templates; customer onboarding workflow documented.

**Steps:**

1. For each health-data integration: classify PHI flow (HIPAA-ALIGNMENT).
2. Send organisation-specific BAA or UK/EU DPA as applicable.
3. Obtain countersignature before production PHI processing.
4. Log agreement ID in customer CRM / internal register (not in public repo).
5. Close ACT-002 when first production integration signed; leave row open if rolling onboarding — use per-customer sub-tracker if needed.

**Evidence target:** Per-integration signed agreements on customer onboarding.

---

### 3.3 ICO registration (ACT-003)

| Field | Value |
|-------|-------|
| Owner | DPO |
| Priority | P1 |
| Source | ICO-REGISTRATION.md, OBL-110 |

**Prerequisites:** ✅ ICO-REGISTRATION.md programme doc; fee tier guidance documented.

**Steps:**

1. Log in to [ICO registration service](https://ico.org.uk/for-organisations/data-protection-fee/).
2. Pay annual data protection fee for correct tier.
3. Record registration number and renewal date in ICO-REGISTRATION.md (§2 live registration table).
4. Add calendar reminder 30 days before renewal.
5. Close ACT-003 with `evidence_ref: ICO-REGISTRATION.md`.

**Evidence target:** Live registration number in ICO-REGISTRATION.md.

---

### 3.4 External penetration test (ACT-005)

| Field | Value |
|-------|-------|
| Owner | Security Ops |
| Priority | P1 |
| Source | PEN-TEST-PROGRAMME.md, PROC-VUL-001 |

**Prerequisites:** ✅ PEN-TEST-PROGRAMME.md; PT-AI scope in PEN-TEST-FUTURE-SCOPE-ANNEX; ASVS gap checklist.

**Steps:**

1. Select CREST / CHECK accredited vendor; scope per PEN-TEST-PROGRAMME (include AI API surfaces).
2. Execute test in agreed window; receive executive summary + technical report.
3. Log entry in PEN-TEST-LOG.md; remediate findings per PROC-VUL-001.
4. Link critical findings to CAPA if required (PROC-CAPA-001).
5. Close ACT-005 when annual cycle complete; schedule next year.

**Evidence target:** PEN-TEST-LOG.md entry with executive summary and remediation status.

---

### 3.5 Tranc3 HIPAA Tier A PR (ACT-006)

| Field | Value |
|-------|-------|
| Owner | Platform Engineering |
| Priority | P1 |
| Status | In progress |
| Source | TRANC3-HIPAA-COPY-REMEDIATION.md |

**Prerequisites:** ✅ Local clone verified 2026-06-07 — Tier A wording in five files.

**Steps:**

1. Open upstream Tranc3 PR with copy remediation changes.
2. Obtain marketing / compliance sign-off on final strings.
3. Merge to Tranc3 default branch; tag release if applicable.
4. Update TRANC3-REGISTER-BRIDGE.md integration status.
5. Close ACT-006 with PR URL and sign-off reference.

**Evidence target:** Merged Tranc3 PR; marketing audit sign-off.

---

### 3.6 Policy attestation cycle (ACT-007)

| Field | Value |
|-------|-------|
| Owner | HR / ISMS Lead |
| Priority | P2 |
| Source | POLICY-ATTESTATION-REGISTER.md, PROC-TRN-001 |

**Prerequisites:** ✅ Policy library; attestation register template.

**Steps:**

1. Define privileged-role list (admin, DPO delegates, AI Lead, Security Ops leads).
2. Issue attestation requests via HR system or documented email workflow.
3. Record completion in `policy_attestation_register.yaml` and POLICY-ATTESTATION-REGISTER.md.
4. Chase non-responders at 14 and 28 days.
5. Close ACT-007 when 100% privileged roles attested for current cycle.

**Evidence target:** 100% privileged-role attestation logged.

---

### 3.7 SOC 2 Type II observation (ACT-008)

| Field | Value |
|-------|-------|
| Owner | ISMS Lead |
| Priority | P1 |
| Source | SOC2-EVIDENCE-SCHEDULE.md |

**Prerequisites:** ✅ SOC2-ALIGNMENT.md; evidence schedule; Type I readiness artefacts.

**Steps:**

1. Confirm observation period start date with auditor.
2. Collect continuous evidence per SOC2-EVIDENCE-SCHEDULE.md (access reviews, change tickets, incidents).
3. Monthly evidence hygiene check; gap remediation before auditor sampling.
4. Complete six-month observation; support auditor fieldwork.
5. Close ACT-008 when observation period ends and report issued (or extend if auditor requests).

**Evidence target:** Six-month continuous evidence per schedule; auditor report reference.

---

### 3.8 magna_carta.py boundary enforcement (ACT-009)

| Field | Value |
|-------|-------|
| Owner | Platform Engineering |
| Priority | P2 |
| Source | MC-004 notes, TRANC3-REGISTER-BRIDGE.md |

**Prerequisites:** ✅ Magna Carta rules defined; Tranc3 integration guide.

**Steps:**

1. Enable `MAGNA_CARTA_ENABLED=true` in staging Tranc3 deployment.
2. Verify request-boundary enforcement on AI routes (MC-RULE-004, MC-RULE-005).
3. Capture audit log samples demonstrating block/allow decisions.
4. Promote to production after staging sign-off.
5. Close ACT-009 with environment config reference and log samples (redacted).

**Evidence target:** Staging + production enforcement verified; audit log samples.

---

### 3.9 SUP-004 US AI fallback DPA (ACT-010)

| Field | Value |
|-------|-------|
| Owner | DPO / AI Lead |
| Priority | P2 |
| Source | supplier_dpa_register SUP-004 |

**Prerequisites:** ✅ TEMPLATE-TIA-US-AI-FALLBACK.md; SUP-004 register row.

**Steps:**

1. Complete transfer impact assessment for US AI fallback provider.
2. Negotiate SCC-based DPA or confirm feature remains disabled for EU data.
3. Document decision in supplier register and AI-GOVERNANCE supply-chain section.
4. If signed: update `dpa_status: Signed`; if disabled: document disable decision and config flag.
5. Close ACT-010 with signed DPA or formal disable record.

**Evidence target:** Signed SCC DPA or documented disable decision.

---

### 3.10 BCP restore tests — P0 databases (ACT-012)

| Field | Value |
|-------|-------|
| Owner | Operations |
| Priority | P2 |
| Source | BCP-RESTORE-TEST-LOG.md |

**Prerequisites:** ✅ BCP-RT-001 baseline (2026-06-07); restore runbook.

**Steps:**

1. Schedule restore tests for remaining P0 databases (vault, Forgejo per action text).
2. Execute restore to isolated environment; verify integrity and RTO/RPO.
3. Log BCP-RT-### entries in BCP-RESTORE-TEST-LOG.md.
4. Remediate failures; update BCP documentation.
5. Close ACT-012 when all P0 databases have successful annual restore entries.

**Evidence target:** BCP-RT-### entries for vault and Forgejo.

---

### 3.13 HRIS role appointments (ACT-016)

| Field | Value |
|-------|-------|
| Owner | HR / Executive |
| Priority | P2 |
| Source | `docs/job-descriptions/INDEX.md` |

**Prerequisites:** ✅ 13 job descriptions and template in repo.

**Steps:**

1. Executive confirms appointees for ISMS Lead, DPO, CISO, CAB Chair, and department PROC owners.
2. Create or update HRIS records; link to `docs/job-descriptions/JD-*.md` role IDs.
3. Update `REVIEWERS-REGISTER` with named individuals (internal doc, not PII in git).
4. Close ACT-016 when all 13 roles have live HRIS appointments.

**Evidence target:** HRIS export or internal roster reference; REVIEWERS-REGISTER updated.

---

### 3.14 Premises fire risk assessment (ACT-017)

| Field | Value |
|-------|-------|
| Owner | Facilities / H&S |
| Priority | P2 |
| Source | PROC-BLD-001, BUILDING-BIBLE |

**Prerequisites:** ✅ Building regulations procedure and bible in repo.

**Steps:**

1. Identify all occupied premises; commission competent assessor or use qualified internal assessor.
2. Complete FRA per Regulatory Reform (Fire Safety) Order 2005.
3. Log actions; store signed FRA off-repo (facilities file).
4. Close ACT-017 when FRA signed and action plan assigned.

**Evidence target:** FRA reference ID in PROC-BLD-001 review minutes.

---

### 3.15 Payroll provider and RTI (ACT-018)

| Field | Value |
|-------|-------|
| Owner | Finance |
| Priority | P2 |
| Source | PROC-PAY-001, PAYROLL-BIBLE |

**Prerequisites:** ✅ Payroll procedure and bible in repo.

**Steps:**

1. Select and contract payroll provider (or confirm in-house capability).
2. Register as employer with HMRC; configure RTI (FPS/EPS).
3. Run parallel payroll cycle; verify first live RTI submission.
4. Close ACT-018 on successful RTI confirmation.

**Evidence target:** Provider contract ref; HMRC submission confirmation (internal).

---

### 3.16 H&S officer and RIDDOR drill (ACT-019)

| Field | Value |
|-------|-------|
| Owner | HR / H&S |
| Priority | P2 |
| Source | PROC-HSE-001, HEALTH-SAFETY-BIBLE |

**Prerequisites:** ✅ H&S procedure and bible in repo.

**Steps:**

1. Appoint named H&S officer (or competent person); record in HRIS (links ACT-016).
2. Schedule tabletop RIDDOR reporting drill with HR and management.
3. Document drill minutes in `docs/evidence/` (sanitised scenario only).
4. Close ACT-019 when officer named and drill completed.

**Evidence target:** Drill minutes; H&S lead named in HRIS.

---

## 4. Closed baseline actions (reference)

| Action | Evidence ID | Artefact |
|--------|-------------|----------|
| ACT-004 | EEV-001 | FTR-2026-001-baseline-fairness.md |
| ACT-011 | EEV-002 | IA-2026-01-baseline-internal-audit.md |
| ACT-013 | EEV-003–005 | AST-2026-001–003 (per model) |
| ACT-014 | EEV-006 | EU-LEGISLATION-MONITORING §6 SCAN-2026-Q2-01 |
| ACT-015 | EEV-007, EEV-008 | HARMONISED-STANDARDS §6 WATCH-2026-H1-01; ETSI gap checklist |

Recurring cycles remain on PROC-CMP-001 calendar; baseline closure does not remove 🎯 external validation for production fairness, independent audit, or harmonised-standard adoption.

---

## 5. Related documents

- [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md)
- [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)
- [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md)
- [PEN-TEST-PROGRAMME.md](../evidence/PEN-TEST-PROGRAMME.md)
- [BCP-RESTORE-TEST-LOG.md](../evidence/BCP-RESTORE-TEST-LOG.md)

**Next review:** 2026-09-06 (PROC-CMP-001)
