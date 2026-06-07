# PROC-IAM-001 — Access Provisioning Procedure

**Version:** 1.0.0 · **Owner:** IT / ISMS · **Policy:** POL-SEC-001

---

## 1. Joiner

1. Manager submits access request with role and justification
2. ISMS verifies least-privilege role mapping
3. Provision: Forgejo, Grafana, vault (if needed), production — MFA enforced before grant
4. Log in access register

## 2. Mover

1. Manager notifies role change
2. Remove obsolete permissions within 24 hours
3. Add new permissions per least privilege
4. Re-verify MFA devices

## 3. Leaver

Within 24 hours of termination notice:
1. Disable all accounts (Forgejo, auth, vault, admin UIs)
2. Revoke API keys and tokens
3. Collect company devices per HR
4. Confirm in access register

## 4. Privileged access

- Break-glass accounts: max 2; quarterly review; usage logged
- Vault access: dual control where feasible
- Production SSH: prohibited except documented emergency

## 5. Access review

Quarterly: ISMS exports access lists; managers attest; orphan accounts removed.

## 6. Tranc3 technical mapping

| Access type | System |
|-------------|--------|
| API user | users-service + JWT roles |
| Service account | API keys in vault |
| Admin | RBAC admin scope + MFA |
