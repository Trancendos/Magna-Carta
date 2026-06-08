# RUN-OMB-001 — Ombudsman and Regulator Escalation

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** Legal / DPO  
**Register:** [REGULATORS-OMBUDSMEN-REGISTER.md](../compliance/REGULATORS-OMBUDSMEN-REGISTER.md)  
**Related:** PROC-DSR-001, PROC-IR-001, COOK-IR-001

---

## 1. When to use

Customer or data subject escalation beyond internal resolution, or mandatory regulator notification (breach, inquiry letter).

| Trigger | Path | OMB / REG |
|---------|------|-----------|
| Data subject unhappy with DSR outcome | Internal review → ICO complaint | OMB-002 / REG-001 |
| Reportable personal data breach (UK) | PROC-IR-001 → ICO notification | REG-001 |
| HIPAA PHI breach (BAA customer) | PROC-IR-001 → HHS per BAA | REG-007 |
| Financial services complaint (if FCA scope) | Complaints procedure → FOS | OMB-001 |
| Misleading advertising claim | ASA CAP Code | OMB-005 |
| Regulatory inquiry letter | Legal intake within 24h | Per authority |

---

## 2. Internal escalation (all cases)

1. **Log** incident or complaint ID in Town Hall / case management
2. **Notify** DPO (privacy) or Legal (contract/regulatory) within **4 business hours**
3. **Preserve** evidence — do not delete tickets, emails, or logs
4. **Assign** owner from [REVIEWERS-REGISTER.md](../governance/REVIEWERS-REGISTER.md)
5. **Document** timeline in case record

---

## 3. Data subject → ICO (OMB-002)

**Preconditions:** PROC-DSR-001 completed; final response issued; complainant still dissatisfied.

| Step | Action | Owner |
|------|--------|-------|
| 1 | Confirm internal process exhausted | DPO |
| 2 | Provide complainant ICO complaint link and summary of our position | DPO |
| 3 | Prepare case file: DSR request, ID check, response, correspondence | DPO |
| 4 | If ICO contacts Trancendos directly, Legal leads response within **5 business days** | Legal |
| 5 | CAPA if systemic issue found | ISMS Lead / PROC-CAPA-001 |

ICO portal: https://ico.org.uk

---

## 4. Reportable breach → ICO (REG-001)

Execute **in parallel** with COOK-IR-001 Phase 3.

| Step | Action | Window |
|------|--------|--------|
| 1 | DPO assesses reportability (risk to rights/freedoms) | Within 24h of awareness |
| 2 | If reportable, draft ICO notification | **72h** from awareness |
| 3 | Notify affected individuals if high risk | Without undue delay |
| 4 | Record in breach register / incident ticket | Same day |
| 5 | Post-incident review and CAPA | Within 14 days |

---

## 5. Financial Ombudsman (OMB-001) — conditional

**Today:** N/A unless Trancendos holds FCA authorisation or acts as payment institution.

If scope changes:

1. Internal complaints procedure with **8-week** final response
2. Refer complainant to FOS if unresolved
3. Legal maintains FOS contact and DISP rules alignment

---

## 6. Evidence and closure

| Output | Location |
|--------|----------|
| Escalation decision record | Town Hall / ticket |
| Regulator correspondence | Legal secure store |
| CAPA items | compliance/compliance_action_tracker.yaml |
| Register update | REGULATORS-OMBUDSMEN-REGISTER annual review |

**Next review:** 2026-09-06
