# COOK-IR-001 — P1 Incident Response Playbook

**Version:** 1.0.0  
**Owner:** Security Ops  
**Procedure:** [PROC-IR-001](../procedures/PROC-IR-001-Incident-Response.md)  
**Hymn sheet:** [HYMN-IR-001](../hymn-sheets/HYMN-IR-001-P1-Incident-Checklist.md)

---

## When to use

Severity P1: active breach, authentication compromise, data exfiltration suspicion, or complete outage of P0 systems (SYS-001–003, 005 per [SYSTEMS-REGISTER](../compliance/SYSTEMS-REGISTER.md)).

---

## Phase 1 — Detect and declare (0–15 min)

1. **Confirm** alert via monitoring (SYS-030–032) or user report
2. **Open** incident record in Town Hall / ticket system
3. **Notify** incident commander (Security Ops) and ISMS Lead
4. **Declare** P1 if: confidentiality impact, availability of auth/nexus, or regulator-reportable breach suspected
5. **Assemble** war room (voice + shared doc)

---

## Phase 2 — Contain (15–60 min)

| Scenario | Immediate action |
|----------|------------------|
| Credential leak | Rotate secrets in SYS-005; invalidate sessions in SYS-002 |
| Suspected exfiltration | Isolate affected worker; preserve logs (Loki) |
| Ransomware / malware | Isolate host; do not pay; preserve forensic image |
| DDoS | Engage ops; Traefik rate limits; upstream provider |

**Do not** destroy logs. Enable extended retention if needed.

---

## Phase 3 — Assess breach notification (parallel)

| Jurisdiction | Trigger | Owner | Window |
|--------------|---------|-------|--------|
| UK GDPR | Risk to rights/freedoms | DPO | ICO 72h from awareness |
| HIPAA | PHI compromise (if BAA) | DPO | Per BAA / HHS rules |
| Customers | Contractual SLA / DPA | Legal | Per agreement |

Reference: [REGULATORS-OMBUDSMEN-REGISTER.md](../compliance/REGULATORS-OMBUDSMEN-REGISTER.md)

---

## Phase 4 — Eradicate and recover

1. Root cause analysis with Engineering
2. Patch / redeploy via PROC-CHG-001 (emergency change path)
3. Validate restore if data affected — PROC-BCP-001
4. Re-enable services in dependency order: vault → auth → ws → domain services

---

## Phase 5 — Close and learn

1. CAPA if systemic gap — [PROC-CAPA-001](../procedures/PROC-CAPA-001-Corrective-Action.md)
2. Update RISK-REGISTER if new threat
3. Post-incident review within 5 business days
4. Customer/regulator notifications as determined in Phase 3

---

## Escalation

| Condition | Escalate to |
|-----------|-------------|
| Personal data breach confirmed | DPO + Legal immediately |
| P0 unresolved > 4 hours | Executive |
| Media / regulator contact | Legal + Executive within 1 hour |

**Related:** POL-OPS-001 Incident Response Policy
