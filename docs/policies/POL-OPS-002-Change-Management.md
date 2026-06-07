# POL-OPS-002 — Change Management Policy

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** CAB Chair · **Review:** Annual

---

## 1. Purpose

Control changes to production systems to minimise risk and maintain compliance evidence.

## 2. Scope

All changes to Tranc3 workers, infrastructure, configuration, Magna Carta policies, and DEFSTAN register.

## 3. Change categories

| Category | Approval | Examples |
|----------|----------|----------|
| Standard | Pre-approved pattern | Dependency patch via CI |
| Normal | CAB review | New worker, schema change |
| Emergency | Post-approval within 24h | P0 hotfix |

## 4. Requirements

- All production changes via version control and CI/CD
- Rollback plan documented for Normal and Emergency changes
- Security/compliance impact assessed
- Magna Carta and DEFSTAN evidence updated when controls change

## 5. Forbidden changes

- Direct production edits bypassing Git
- Disabling compliance CI gate without waiver
- Deploying with known failing penetration or compliance tests

## 6. Related documents

PROC-CHG-001, POL-SEC-001, Forgejo CI configuration
