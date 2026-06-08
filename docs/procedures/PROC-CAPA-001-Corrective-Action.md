# PROC-CAPA-001 — Corrective and Preventive Action

**Version:** 1.0.0 · **Owner:** ISMS Lead · **Policies:** POL-SEC-001, POL-OPS-001, POL-OPS-002

---

## 1. Purpose

Formalise corrective action (CAPA) for nonconformities from audits, incidents, pen tests, compliance reviews, and management review. Supports ISO 27001 certification prerequisites and SOC 2 CC7.

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Procedure documented |
| 🎯 **Operational** | CAPA records maintained with closure evidence |

---

## 2. Sources of nonconformity

| Source | Typical trigger | Initial owner |
|--------|---------------|---------------|
| Internal audit (ACT-011) | Audit finding | ISMS Lead |
| External audit / pen test (ACT-005) | Finding report | Security Ops |
| Incident (PROC-IR-001) | Post-incident review | Incident commander |
| Compliance review (PROC-CMP-001) | Gap in obligations matrix | ISMS Lead |
| Management review | Executive action item | Assigned owner |
| Risk register | Treatment overdue | Risk owner |
| Customer / regulator | Complaint or enquiry | DPO / ISMS |

---

## 3. CAPA workflow

```
Identify → Log (CAPA-YYYY-###) → Root cause → Action plan → Implement → Verify → Close
```

### 3.1 Log

Minimum fields: ID, source, description, severity (Critical/High/Medium/Low), owner, due date, linked ACT-### or incident ID.

### 3.2 Root cause

Use 5-Whys or equivalent; document in CAPA record. For repeat findings, escalate to CAB.

### 3.3 Action plan

| Severity | Target closure | Verification |
|----------|----------------|--------------|
| Critical | 7 days | ISMS + domain owner |
| High | 30 days | ISMS |
| Medium | 90 days | Owner attestation |
| Low | Next quarterly review | PROC-CMP-001 |

### 3.4 Implement

May require: Tranc3 change (PROC-CHG-001), policy update, training (PROC-TRN-001), supplier action (POL-SUP-001).

### 3.5 Verify and close

Verifier confirms evidence; ISMS updates [RISK-TREATMENT-PLAN.md](../compliance/RISK-TREATMENT-PLAN.md) if risk-related. Status → Closed.

---

## 4. Preventive action

Trend analysis in quarterly PROC-CMP-001: if ≥2 similar CAPAs in 12 months, open preventive action to address systemic cause.

---

## 5. Integration

| Process | Link |
|---------|------|
| CAB | Major corrective changes via PROC-CHG-001 |
| PIR | PROC-CHG-002 captures change-related lessons |
| Risk treatment | [RISK-TREATMENT-PLAN.md](../compliance/RISK-TREATMENT-PLAN.md) |
| Action tracker | [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md) |

---

## 6. Records

CAPA log maintained by ISMS; retention **5 years**. Storage: secure ISMS repository (not this public repo).

---

## 7. Related documents

- [INTERNAL-AUDIT-PROGRAMME.md](../governance/INTERNAL-AUDIT-PROGRAMME.md)
- [PROC-VUL-001](PROC-VUL-001-Vulnerability-Management.md)
- [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) §4
