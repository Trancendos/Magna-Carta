# Certification Evidence Vault

**Owner:** ISMS Lead  
**Register:** `compliance/certification_evidence_register.yaml`  
**Scorer:** `scripts/readiness_automation_score.py`

---

## Purpose

Drop zone for **owner-provided** certificates, signed agreements, and external audit reports. The register and folder structure are Layer B (ready). Uploading files is Layer C (go-live) and does **not** reduce automation readiness percent.

---

## How to upload

1. Name files to match the slot pattern in the register (case-insensitive glob):

| Slot | Pattern | Example filename |
|------|---------|------------------|
| CERT-001 | `ico-fee-*` | `ico-fee-2026-confirmation.pdf` |
| CERT-002 | `dpa-psp-*` | `dpa-psp-stripe-signed.pdf` |
| CERT-003 | `baa-health-*` | `baa-health-connector-v1.pdf` |
| CERT-004 | `pentest-*` | `pentest-2026-crest-report.pdf` |
| CERT-005 | `soc2-*` | `soc2-type2-2026.pdf` |
| CERT-007 | `fra-premises-*` | `fra-premises-2026-signed.pdf` |
| CERT-008 | `payroll-rti-*` | `payroll-rti-hmrc-confirmation.pdf` |
| CERT-009 | `riddor-drill-*` | `riddor-drill-2026-09-tabletop.pdf` |

2. Commit to git or store per your evidence retention policy.  
3. Re-run `python3 scripts/readiness_automation_score.py --report` — matched files show as `uploaded`.  
4. Optionally attach a cert in Cursor chat for agent review of metadata (expiry, scope, issuer).

---

## Template for RIDDOR drill

Use [TEMPLATE-RIDDOR-DRILL-MINUTES.md](../../templates/TEMPLATE-RIDDOR-DRILL-MINUTES.md), save completed minutes as `riddor-drill-YYYY-MM-description.pdf` or `.md` in this folder.

---

## What agents can and cannot do

| Can (Layer B) | Cannot (Layer C) |
|---------------|------------------|
| Maintain register slots and patterns | Pay ICO fee |
| Verify folder exists and scan filenames | Commission pen test or SOC 2 audit |
| Analyse uploaded PDF metadata when provided | Confirm HRIS appointments |
| Report pending vs uploaded counts | Countersign supplier DPAs |
