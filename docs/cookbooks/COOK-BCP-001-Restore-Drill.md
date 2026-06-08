# COOK-BCP-001 — Backup & Restore Drill Playbook

**Version:** 1.0.0  
**Owner:** Operations  
**Procedure:** [PROC-BCP-001](../procedures/PROC-BCP-001-Backup-Restore.md)  
**Hymn sheet:** [HYMN-BCP-001](../hymn-sheets/HYMN-BCP-001-Restore-Drill-Checklist.md)

---

## When to use

Semi-annual restore test, post-incident validation, or pre-audit evidence collection.

---

## Pre-drill

1. Select **non-production** target or isolated namespace
2. Confirm backup snapshot ID and RPO/RTO targets from BCP doc
3. Notify stakeholders; schedule maintenance window if needed

---

## Execute drill

1. Restore from latest verified backup
2. Validate data integrity checksums / smoke tests
3. Measure actual RTO; compare to target
4. Document failures with root cause

---

## Post-drill

1. Log result in [BCP-RESTORE-TEST-LOG.md](../evidence/BCP-RESTORE-TEST-LOG.md)
2. CAPA for miss — PROC-CAPA-001
3. Update PROC-BCP-001 if runbook gaps found
