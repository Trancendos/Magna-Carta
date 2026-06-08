# POL-SEC-003 — Endpoint & Data Protection Policy

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** ISMS Lead · **Review:** Annual

**Status:** Authored (framework) — BoardRoom approval 🎯

---

## 1. Purpose

Define requirements for endpoints (laptops, workstations, mobile) and data loss prevention (DLP) for remote and cloud-first operations. Addresses ISO 27001 gaps for MDM, DLP, and device handling.

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Policy documented |
| 🎯 **Operational** | MDM/DLP tooling deployed and monitored |

---

## 2. Scope

All company-issued and BYOD devices used to access Tranc3 production, vault, Forgejo, observability, or customer data.

---

## 3. Endpoint requirements

| Control | Requirement | Operational status |
|---------|-------------|-------------------|
| Full-disk encryption | Enabled (FileVault, BitLocker, LUKS) | 🎯 Verify at onboarding |
| OS patching | Critical patches within 14 days | 🎯 MDM or attestation |
| Screen lock | ≤5 minutes idle; password/biometric | Required |
| Anti-malware | Approved endpoint protection | 🎯 Tool selection pending |
| Firewall | Host firewall enabled | Required |
| Admin rights | Least privilege; no local admin on prod-access devices | Required |

---

## 4. Mobile device management (MDM)

When MDM is deployed 🎯:

- Enrol all devices with production access
- Remote wipe on leaver within PROC-HR-001 timeline
- Block jailbroken/rooted devices
- Application allow-list for tokens and VPN clients

**Programme position:** Policy ready; vendor selection (e.g. Intune, Kandji, Jamf) is operational blocker.

---

## 5. Data loss prevention (DLP)

| Data class | Rule |
|------------|------|
| Customer PII / PHI | No storage on personal cloud sync folders |
| Production credentials | Vault only; no plaintext in repos or chat |
| Source code | Company Forgejo only; no unapproved public repos |
| Removable media | Encrypted USB only; prohibited for PHI unless approved |

DLP tooling (endpoint agent or cloud CASB) 🎯 to enforce classification labels where feasible.

---

## 6. Remote work

- Use approved VPN or Zero Trust access paths only
- No production access from untrusted networks without MFA
- Physical privacy for sensitive calls and screen sharing

---

## 7. Device return and disposal

On leaver: wipe per NIST SP 800-88 guidelines; certificate of destruction for devices containing customer data. See [PROC-HR-001](../procedures/PROC-HR-001-Staff-Lifecycle.md) §6.

---

## 8. Exceptions

Exceptions require ISMS written approval, time-bound, logged in risk register.

---

## 9. Related documents

- POL-SEC-001, POL-SEC-002, POL-PRI-001
- [PROC-HR-001](../procedures/PROC-HR-001-Staff-Lifecycle.md)
- [PROC-IAM-001](../procedures/PROC-IAM-001-Access-Provisioning.md)
- [ISO27001-ALIGNMENT.md](../compliance/ISO27001-ALIGNMENT.md)
- [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) §4
