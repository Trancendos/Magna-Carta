# PROC-DSR-001 — Data Subject Request Procedure

**Version:** 1.0.0 · **Owner:** DPO · **Policy:** POL-PRI-001

---

## 1. Intake

Accept via: privacy@, in-app form, or written request. Log: date received, requester identity, request type.

## 2. Verify identity

Confirm requester is the data subject or authorised agent (reasonable evidence).

## 3. Acknowledge

Within **72 hours** — confirm receipt and expected completion date (max 30 days).

## 4. Fulfil

| Right | Action | System |
|-------|--------|--------|
| Access (Art. 15) | Export JSON bundle | users-service |
| Rectification (Art. 16) | Update profile | users-service |
| Erasure (Art. 17) | Delete account + cascaded data | users-service workflows |
| Portability (Art. 20) | Machine-readable export | users-service |
| Restriction (Art. 18) | Flag account; pause processing | Manual + DB flag |
| Objection (Art. 21) | Review lawful basis; stop if required | DPO decision |

## 5. Third parties

Notify processors/sub-processors if data shared; confirm their deletion/export.

## 6. Response

Deliver securely (encrypted link or authenticated portal). Document completion in DSR log.

## 7. Extension

If complex: notify within 30 days; extend up to 90 days with reasons (Art. 12(3)).

## 8. Refusal

If manifestly unfounded or excessive: document rationale; inform requester of complaint right to ICO.
