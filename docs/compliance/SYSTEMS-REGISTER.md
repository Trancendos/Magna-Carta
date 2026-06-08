# Systems Register (CMDB-lite)

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Platform Engineering  
**Review cycle:** Quarterly + on major architecture change  
**Source of truth for detail:** [AS-BUILT-ARCHITECTURE.md](../architecture/AS-BUILT-ARCHITECTURE.md)

---

## 1. Purpose

Lightweight configuration management for compliance, BCP, and supplier reviews. Not a full enterprise CMDB — sufficient for auditors and incident commanders.

---

## 2. Platform systems

| SYS-ID | System | Type | Criticality | Data class | Owner | Compliance controls |
|--------|--------|------|-------------|------------|-------|---------------------|
| SYS-001 | Traefik ingress | Infrastructure | P0 | Metadata | Platform Eng | TLS, rate limits |
| SYS-002 | infinity-auth | Application | P0 | Credentials, PII | Platform Eng | MFA, JWT, PROC-IAM-001 |
| SYS-003 | infinity-ws (Nexus) | Application | P0 | Session, messages | Platform Eng | AuthZ, logging |
| SYS-004 | users-service | Application | P1 | PII | Platform Eng | ROPA, PROC-DSR-001 |
| SYS-005 | vault-service / OpenBao | Security | P0 | Secrets | Security Ops | POL-SEC-001, encryption |
| SYS-006 | audit-service | Security | P1 | Audit logs | Security Ops | Immutable logs |
| SYS-007 | infinity-ai / tranc3-ai | Application | P1 | Prompts, outputs | AI Lead | AI-GOVERNANCE, model cards |
| SYS-008 | payments-service | Application | P2 | Payment metadata (no CHD) | Platform Eng | PCI-DSS-POSITION |
| SYS-009 | files-service | Application | P2 | User files | Platform Eng | Encryption at rest |
| SYS-010 | Forgejo (SCM/CI) | DevOps | P1 | Source code | Platform Eng | DEFSTAN CI, branch protection |

---

## 3. Data stores

| SYS-ID | Store | Encryption | Backup (PROC-BCP-001) | Restore tested |
|--------|-------|------------|----------------------|----------------|
| SYS-020 | SQLite per service | AES-GCM | Daily automated | ⚠️ Partial — ACT-012 |
| SYS-021 | Vault data volume | At rest + transit | Daily | 🎯 Scheduled |
| SYS-022 | Log storage (Loki) | Volume encryption | Retention policy | I |

---

## 4. Observability and security tooling

| SYS-ID | System | Function | Owner |
|--------|--------|----------|-------|
| SYS-030 | Prometheus | Metrics | Security Ops |
| SYS-031 | Grafana | Dashboards | Security Ops |
| SYS-032 | Loki | Log aggregation | Security Ops |
| SYS-033 | DEFSTAN checker (CI) | Compliance gate | Platform Eng |
| SYS-034 | Magna Carta checker (Tranc3) | Runtime policy | Platform Eng — 🎯 ACT-009 |

---

## 5. Governance and documentation systems

| SYS-ID | System | Function | Owner |
|--------|--------|----------|-------|
| SYS-040 | Magna Carta repo (this) | Layer 2 documentation | ISMS Lead |
| SYS-041 | Town Hall / BoardRoom | ITSM, meetings, stage gates | ISMS Lead |
| SYS-042 | compliance_health_check.py + weekly_compliance_health.sh | Local register freshness monitor (MON-001–010; no GHA) | ISMS Lead |

---

## 6. Third-party systems (sub-processors)

See [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md) and `compliance/supplier_dpa_register.yaml` for SaaS and cloud processors. Key entries: PSP (SUP-003), US AI fallback (SUP-004), health connectors (SUP-005).

---

## 7. BCP priority mapping

| Tier | Systems | RTO target | RPO target |
|------|---------|------------|------------|
| P0 | SYS-001, 002, 003, 005 | 4 h | 1 h |
| P1 | SYS-004, 006, 007, 010 | 8 h | 4 h |
| P2 | Remaining application services | 24 h | 24 h |

Drill evidence: [BCP-RESTORE-TEST-LOG.md](../evidence/BCP-RESTORE-TEST-LOG.md)

---

## 8. Change log

| Date | Change | Author |
|------|--------|--------|
| 2026-06-07 | Initial CMDB-lite from AS-BUILT | Platform Engineering |

**Next review:** 2026-09-06
