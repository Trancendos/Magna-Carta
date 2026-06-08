# COOK-DSR-001 — Data Subject Request Playbook

**Version:** 1.0.0  
**Owner:** DPO  
**Procedure:** [PROC-DSR-001](../procedures/PROC-DSR-001-Data-Subject-Requests.md)  
**Hymn sheet:** [HYMN-DSR-001](../hymn-sheets/HYMN-DSR-001-DSR-Checklist.md)

---

## When to use

Any access, rectification, erasure, restriction, portability, or objection request under UK/EU GDPR, or contractual privacy rights.

---

## Intake (0–24h)

1. **Log** request in ticket system with receipt timestamp (legal clock starts)
2. **Verify** identity per PROC-DSR-001 §2 — do not disclose without proof
3. **Classify** right type and jurisdiction (UK ICO 1 month / extensions documented)
4. **Assign** DPO owner; notify Engineering if technical export needed

---

## Execute

| Right | Primary action | Systems |
|-------|----------------|---------|
| Access | Export from ROPA-linked stores | SYS-001–003, customer DB |
| Erasure | Map retention exceptions first | Legal hold, billing, audit |
| Portability | Structured export (JSON/CSV) | Per data map |
| Rectification | Correct source + downstream sync | Customer profile services |

---

## Close

1. Respond within statutory window with audit trail
2. Update OBLIGATIONS-REGISTER if process gap found
3. CAPA if SLA miss — [PROC-CAPA-001](../procedures/PROC-CAPA-001-Corrective-Action.md)

**Escalation:** Regulator-reportable delay → DPO → Legal within 24h
