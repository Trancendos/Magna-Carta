# POL-OPS-003 — Business Continuity Policy

**Version:** 1.0.0 · **Effective:** 2026-06-07 · **Owner:** Operations · **Review:** Annual

---

## 1. Purpose

Maintain essential Tranc3 services during disruption and recover within defined objectives.

## 2. Scope

P0 and P1 services per AS-BUILT-ARCHITECTURE.md.

## 3. Objectives

| Tier | RTO | RPO |
|------|-----|-----|
| P0 | 1 hour | 15 minutes |
| P1 | 4 hours | 1 hour |
| P2 | 24 hours | 24 hours |

## 4. Requirements

- Encrypted backups per PROC-BCP-001
- Annual restore test for P0 databases
- Documented DR runbook maintained with as-built architecture
- Forgejo and vault included in backup scope

## 5. Activation

Operations Lead declares disaster; CAB coordinates recovery; WarRoom if customer-impacting.

## 6. Related documents

PROC-BCP-001, AS-BUILT-ARCHITECTURE.md, PROC-IR-001
