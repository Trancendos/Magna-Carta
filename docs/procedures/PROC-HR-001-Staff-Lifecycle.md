# PROC-HR-001 — Staff Lifecycle (Screening, Training, Offboarding)

**Version:** 1.0.0 · **Owner:** HR / ISMS · **Policies:** POL-SEC-001, POL-SEC-002, POL-PRI-001

---

## 1. Purpose

Define joiner, mover, and leaver controls for personnel with access to Tranc3, customer data, or Magna Carta governance systems. Closes ISO 27001 Clause 6 gaps (screening, awareness, termination).

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Procedure documented |
| 🎯 **Operational** | HR executes with vendor contracts and attestations on file |

---

## 2. Pre-employment screening

| Role tier | Minimum checks | When |
|-----------|----------------|------|
| Standard (no prod/customer data) | Identity, right-to-work, employment references | Before start date |
| Privileged / ISMS / DPO / AI Lead | Above + enhanced background check (criminal/financial where lawful) | Before privileged access |
| Contractor (< 90 days) | Identity + NDA + sponsor attestation | Before access grant |

**Records:** HR file only; ISMS receives pass/fail outcome (no sensitive detail).

**Blocker for operational ✅:** Background-check vendor contract and HR workflow in HRIS 🎯.

---

## 3. Onboarding

1. HR issues employment/contract pack including POL-SEC-001, POL-SEC-002, POL-PRI-001, POL-AI-001 (if AI role).
2. Complete [PROC-TRN-001](PROC-TRN-001-Security-Awareness-Attestation.md) within 5 business days.
3. Manager submits access request per [PROC-IAM-001](PROC-IAM-001-Access-Provisioning.md).
4. ISMS verifies role mapping before production grant.

---

## 4. Ongoing training

| Training | Audience | Frequency |
|----------|----------|-----------|
| Security awareness | All personnel | Annual + on material policy change |
| Data protection / GDPR | All with customer data access | Annual |
| AI ethics (POL-AI-001) | AI, product, support touching AI features | Annual |
| Incident reporting | All | At onboarding |

---

## 5. Mover (role change)

1. Manager notifies HR and ISMS within 1 business day.
2. [PROC-IAM-001](PROC-IAM-001-Access-Provisioning.md) mover workflow within 24 hours.
3. Re-attest if new privileged scope.

---

## 6. Leaver / termination

Within **24 hours** of termination effective time (or notice if earlier for risk cases):

1. HR notifies ISMS with leaver list (daily cut-off 17:00 UK).
2. ISMS disables all accounts per PROC-IAM-001 §3.
3. Revoke API keys, vault access, break-glass accounts.
4. HR collects company devices; IT wipes per [POL-SEC-003](../policies/POL-SEC-003-Endpoint-Data-Protection.md).
5. HR confirms return of confidential materials.
6. ISMS signs off in access register.

**Emergency termination:** ISMS disables access immediately on HR notification; steps 4–6 follow same day.

---

## 7. Records

| Record | Retention | Owner |
|--------|-----------|-------|
| Screening outcome | Duration of employment + 2 years | HR |
| Training attestation | 3 years | HR / ISMS |
| Access provisioning log | 2 years | ISMS |

---

## 8. Related documents

- [PROC-IAM-001](PROC-IAM-001-Access-Provisioning.md)
- [PROC-TRN-001](PROC-TRN-001-Security-Awareness-Attestation.md)
- [POL-SEC-003](../policies/POL-SEC-003-Endpoint-Data-Protection.md)
- [ISO27001-ALIGNMENT.md](../compliance/ISO27001-ALIGNMENT.md) Clause 6
- [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) §4
