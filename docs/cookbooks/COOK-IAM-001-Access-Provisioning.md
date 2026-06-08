# COOK-IAM-001 — Access Provisioning Playbook

**Version:** 1.0.0  
**Owner:** ISMS Lead  
**Procedure:** [PROC-IAM-001](../procedures/PROC-IAM-001-Access-Provisioning.md)  
**Hymn sheet:** [HYMN-IAM-001](../hymn-sheets/HYMN-IAM-001-Access-Checklist.md)

---

## When to use

New joiner, role change, contractor onboarding, privileged access grant, or quarterly access review cycle.

---

## Grant access

1. **Ticket** with manager approval and least-privilege role mapping
2. **Provision** in SYS-002 (auth) and target systems — no shared accounts
3. **MFA** enforced before production access
4. **Log** grant in access register / ticket audit trail

---

## Quarterly review

1. Export role assignments per SYSTEMS-REGISTER
2. Managers attest removals for leavers and role drift
3. Revoke stale access within 48h of attestation
4. Document exceptions with expiry date

---

## Offboarding tie-in

Leaver same day: COOK-HR-001 offboarding block — revoke all access before end of last working day.
