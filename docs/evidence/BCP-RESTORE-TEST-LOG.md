# BCP Restore Test Log

**Version:** 1.0.0  
**Owner:** Operations  
**Procedure:** [PROC-BCP-001](../procedures/PROC-BCP-001-Backup-Restore.md)  
**Obligation:** OBL-062

---

## 1. Purpose

Records backup restore tests to demonstrate BCP capability. Satisfies PROC-BCP-001 §3 annual P0 database restore requirement.

---

## 2. Test log

| Test ID | Date | Asset | Environment | RTO target | RTO achieved | RPO target | RPO achieved | Result | Issues | Owner | Sign-off |
|---------|------|-------|-------------|------------|--------------|------------|--------------|--------|--------|-------|----------|
| BCP-RT-001 | 2026-06-07 | P0 SQLite (infinity-auth sample) | Isolated DR staging | 4h | 2h 15m | 24h | 12h | ✅ Pass | None — checksum verified; smoke tests green | Operations | ISMS Lead |

### BCP-RT-001 detail

| Step | Outcome |
|------|---------|
| 1. Select latest daily backup | Backup dated 2026-06-06 02:00 UTC |
| 2. Provision clean container | `dr-staging` per AS-BUILT-ARCHITECTURE |
| 3. Restore database volume | Completed 47 min |
| 4. Verify AES-GCM integrity | Checksum match |
| 5. Start worker smoke tests | Auth login, JWT validation — pass |
| 6. Run compliance checker | DEFSTAN gate ≥70% — pass |
| 7. Document RTO/RPO | See table above |

**Note:** This entry documents the **programme baseline restore test**. Repeat annually for all P0 databases and after material architecture changes.

---

## 3. Scheduled tests

| Asset class | Frequency | Next due |
|-------------|-----------|----------|
| P0 SQLite databases | Annual | 2027-06-07 |
| Vault data | Annual | 2027-06-07 |
| Forgejo repos | Annual | 2027-06-07 |
| Full DR exercise | Annual | 2027-06-07 |

---

## 4. Failure handling

Restore test failure = P1 incident if production backup integrity at risk. Track via PROC-IR-001.

---

## 5. Related documents

- [PROC-BCP-001](../procedures/PROC-BCP-001-Backup-Restore.md)
- [POL-OPS-003](../policies/POL-OPS-003-Business-Continuity.md)
- [OBLIGATIONS-REGISTER.md](../compliance/OBLIGATIONS-REGISTER.md) — OBL-062
