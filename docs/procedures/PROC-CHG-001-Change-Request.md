# PROC-CHG-001 — Change Request Procedure

**Version:** 1.0.0 · **Owner:** CAB · **Policy:** POL-OPS-002

---

## 1. Submit change

Create change record with:
- Description and business justification
- Affected services (reference AS-BUILT-ARCHITECTURE)
- Risk assessment (security, privacy, availability)
- Rollback plan
- Test evidence (CI run link)

## 2. Classification

| Type | Criteria | Approval |
|------|----------|----------|
| Standard | Pre-approved template (e.g. dep patch) | Automated CI |
| Normal | New feature, config, schema | CAB |
| Emergency | P0 remediation | IC + post-CAB within 24h |

## 3. CAB review (Normal)

Checklist:
- [ ] Peer review merged
- [ ] CI green including compliance ≥70%
- [ ] No open critical vulns
- [ ] Magna Carta / policy impact assessed
- [ ] Customer notification if needed

## 4. Implementation

1. Deploy via Forgejo pipeline to staging
2. Smoke test + monitoring check
3. Promote to production in change window
4. Monitor 30 minutes post-deploy

## 5. Rollback

If failure: execute rollback plan; document in change record; incident if customer-impacting.

## 6. Post-change

Update AS-BUILT-ARCHITECTURE if topology changed; update register evidence paths if controls changed.
