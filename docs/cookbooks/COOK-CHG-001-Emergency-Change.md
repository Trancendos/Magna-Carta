# COOK-CHG-001 — Emergency Change Playbook

**Version:** 1.0.0  
**Owner:** CAB Chair / Platform Engineering  
**Procedure:** [PROC-CHG-001](../procedures/PROC-CHG-001-Change-Request.md)  
**Hymn sheet:** [HYMN-CHG-001](../hymn-sheets/HYMN-CHG-001-Emergency-Change-Checklist.md)

---

## When to use

P1 incident fix, active security vulnerability exploitation, or outage requiring immediate deploy outside normal CAB window.

---

## Declare emergency (0–15 min)

1. **Link** to incident ticket if applicable (COOK-IR-001)
2. **Record** business justification and rollback plan
3. **Notify** CAB Chair + ISMS (async OK if overnight)
4. **Assign** implementer and verifier (four-eyes)

---

## Implement

1. Minimal diff — fix only the emergency scope
2. Deploy via standard pipeline where possible; document manual steps
3. Smoke-test P0 systems (SYS-001–003, 005)
4. Preserve logs and change artefacts for PIR

---

## Post-emergency (within 5 business days)

1. **Retroactive CAB** approval or rejection documented
2. **PIR** — [PROC-CHG-002](../procedures/PROC-CHG-002-Post-Implementation-Review.md) / COOK-CHG-002
3. Update CHANGE-LOG and risk register if new threat
