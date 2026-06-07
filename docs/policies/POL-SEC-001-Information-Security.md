# POL-SEC-001 — Information Security Policy

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** ISMS Lead · **Review:** Annual

---

## 1. Purpose

Establish Trancendos requirements for protecting information assets across the Tranc3 platform and supporting systems.

## 2. Scope

All employees, contractors, and systems processing Trancendos or customer data. Applies to self-hosted and Trancendos-operated deployments.

## 3. Principles

- Confidentiality, integrity, and availability of information
- Zero Trust: never trust, always verify
- Defence in depth across edge, application, data, and operations
- Security by design in all engineering work
- Compliance evidence maintained in DEFSTAN register and Magna Carta framework

## 4. Requirements

### 4.1 Access control
- Unique identities for all users; shared accounts prohibited except break-glass (logged)
- MFA required for production, vault, CI/CD, and admin interfaces
- RBAC enforced at API boundaries (`src/auth/dependencies.py`)
- Quarterly access reviews (PROC-IAM-001)

### 4.2 Cryptography
- TLS 1.2+ for all external traffic
- AES-GCM encryption for SQLite databases at rest
- Secrets only in vault-service / Infinity Void — never in source control

### 4.3 Secure development
- All changes via version control with peer review
- CI must pass: lint, tests, SAST, dependency scan, secret scan, compliance gate
- No deployment of known critical vulnerabilities without waiver

### 4.4 Logging and monitoring
- Security-relevant events logged; PII redacted (`Dimensional/sanitize.py`)
- 90-day default log retention unless law requires longer
- Alerts for auth failures, rate limit breaches, service health degradation

### 4.5 Vulnerability management
- Critical CVEs remediated within 7 days; high within 30 days (PROC-VUL-001)
- Annual penetration test

### 4.6 Incident management
- All security incidents follow PROC-IR-001
- P0 incidents activate Town Hall WarRoom

## 5. Roles

| Role | Responsibility |
|------|----------------|
| ISMS Lead | Policy owner, risk acceptance |
| CISO / Security Ops | Incident command, vuln programme |
| Engineering | Control implementation |
| All staff | Report suspected incidents within 1 hour |

## 6. Exceptions

Exceptions require documented risk assessment, compensating controls, expiry date, and ISMS Lead approval.

## 7. Related documents

PROC-IAM-001, PROC-VUL-001, PROC-IR-001, ISO27001-ALIGNMENT.md, DEFSTAN register

## 8. Compliance

Non-compliance may result in access revocation and disciplinary action per HR policy.
