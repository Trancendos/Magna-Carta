# SOC 2 Type II Alignment Summary

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Source of truth:** [Tranc3 `docs/compliance/SOC2_TYPE_II.md`](https://github.com/Trancendos/Tranc3/blob/main/docs/compliance/SOC2_TYPE_II.md)  
**Report target:** Q1 2027  
**Observation period:** 6 months prior to report

---

## Trust Services Criteria in scope

| TSC | In scope | Rationale |
|-----|----------|-----------|
| **Security** (CC) | ✅ Yes | Core platform requirement |
| **Availability** | ✅ Yes | SLA commitments to customers |
| **Confidentiality** | ✅ Yes | PII and secrets processing |
| **Processing Integrity** | ⚠️ Limited | AI inference accuracy — model cards, not financial processing |
| **Privacy** | ✅ Yes | GDPR-aligned privacy programme |

---

## Control environment summary

### CC1 — Control environment

| Control | Status | Evidence |
|---------|--------|----------|
| Integrity and ethical values | ⚠️ | Code of conduct, Magna Carta foundation |
| Board oversight | ⚠️ | BoardRoom governance |
| Organisational structure | ⚠️ | RACI in FRAMEWORK.md |
| Competence | ⚠️ | Training planned (Academy) |
| Accountability | ✅ | DEFSTAN register ownership |

### CC6 — Logical and physical access

| Control | Status | Tranc3 implementation |
|---------|--------|----------------------|
| Authentication | ✅ | Zero Trust IAM, MFA, JWT |
| Authorisation | ✅ | RBAC (user/admin/moderator) |
| Credential management | ✅ | Vault, bcrypt, key rotation |
| Network security | ✅ | Traefik TLS, Docker network isolation |

### CC7 — System operations

| Control | Status | Evidence |
|---------|--------|----------|
| Vulnerability management | ✅ | pip-audit, security-scan CI |
| Incident detection | ⚠️ | Observatory; formal IR planned |
| Incident response | ⚠️ | PROC-IR-001 (this repo) |
| Change management | ✅ | CAB, change-request-process |

### CC8 — Change management

| Control | Status | Evidence |
|---------|--------|----------|
| Change authorisation | ✅ | CAB approval workflow |
| Testing | ✅ | CI test suite, compliance gate |
| Deployment | ✅ | production-gate workflow |

### CC9 — Risk mitigation (vendors)

| Control | Status | Gap |
|---------|--------|-----|
| Vendor inventory | ⚠️ | ZERO_COST_VENDOR_MATRIX |
| Vendor risk assessment | ⚠️ | POL-SUP-001 |
| Vendor monitoring | ⚠️ | RSS changelog monitoring planned |

---

## Availability commitments

| Tier | Target uptime | Monitoring |
|------|---------------|------------|
| P0 services | 99.9% | Prometheus + Grafana |
| P1 services | 99.5% | Same |
| Platform overall | 99.5% | Observatory dashboards |

**RTO/RPO:** Defined in `docs/runbooks/disaster-recovery.md` (Tranc3)

---

## Evidence collection

Automated via Tranc3 `scripts/soc2_evidence_collector.py`:

| Evidence | Frequency | Source |
|----------|-----------|--------|
| Access review log | Monthly | users-service admin audit |
| Change log | Continuous | Forgejo + CAB records |
| Vulnerability scan | Weekly | dependency-audit CI |
| Uptime metrics | Continuous | Prometheus |
| Incident log | Per event | Observatory + WarRoom |
| Backup verification | Monthly | backup-service + DR drill |

---

## Magna Carta contributions

Policies and procedures in this repository close SOC 2 gaps in:

- Incident response (CC7)
- Business continuity (A1)
- Privacy notice and DSR (P1–P8)
- Acceptable use (CC1)
- Supplier management (CC9)

**Detailed TSC mapping:** See Tranc3 `SOC2_TYPE_II.md`.
