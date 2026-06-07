# PROC-BCP-001 — Backup & Restore Procedure

**Version:** 1.0.0 · **Owner:** Operations · **Policy:** POL-OPS-003

---

## 1. Backup scope

| Asset | Frequency | Retention | Encryption |
|-------|-----------|-----------|------------|
| SQLite DBs (P0/P1) | Daily | 30 days | AES-GCM (at rest) |
| Vault data | Daily | 30 days | Native vault encryption |
| Forgejo repos | Daily | 90 days | Transport + volume encryption |
| Prometheus (optional) | Weekly | 14 days | Volume encryption |
| Configuration (compose, env templates) | On change | Git history | N/A |

## 2. Backup execution

1. Quiesce or snapshot consistent state where possible
2. Copy to secondary volume or off-host storage
3. Verify checksum
4. Log success/failure in operations log

## 3. Restore test

- **P0 databases:** Annual full restore to isolated environment
- Document: RTO/RPO achieved, issues found

## 4. Disaster recovery

1. Operations Lead declares DR
2. Provision clean environment from AS-BUILT-ARCHITECTURE
3. Restore latest verified backup
4. Run compliance checker and smoke tests
5. Redirect Traefik traffic
6. Post-incident review per PROC-IR-001

## 5. Failure handling

Backup failure = P1 incident if persists >24h.
