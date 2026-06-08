# Tranc3 HIPAA Marketing Copy Remediation

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Platform Engineering / DPO  
**Parent:** [HIPAA-ALIGNMENT.md](../compliance/HIPAA-ALIGNMENT.md) §10  
**Status:** ✅ Specification complete — **merge to Tranc3 repo required** (not tracked in Magna Carta)

---

## Purpose

Tranc3 product copy previously implied unconditional HIPAA compliance for wellbeing / Sync-Bot features. Per Magna Carta Tier A wording, claims must be **deployment-scoped** until Tier B/C evidence exists.

## Required wording (Tier A)

> Supports HIPAA-aligned controls when deployed on HIPAA profile with BAA

Variant for bot descriptions:

> Pulls data securely from health platforms using HIPAA-aligned encryption when on HIPAA profile with BAA.

## Files to update in [Tranc3](https://github.com/Trancendos/Tranc3)

| File | Location | Change |
|------|----------|--------|
| `src/entities/platform.py` | `tAimra` abilities + Sync-Bot | Replace "HIPAA compliant" / "strict HIPAA encryption" with Tier A wording |
| `src/config/id_registry.json` | `tAimra` abilities + `NID-TMR-01` | Same |
| `src/config/id_registry.csv` | `NID-TMR-01` row | Same |
| `docs/matrix.md` | Sync-Bot row | Same |
| `docs/DOC-17-SCAMPER-5Whys.md` | Mental health row | "HIPAA compliance layer" → "HIPAA-aligned deployment profile with BAA" |

## Verification

After merge to Tranc3:

```bash
rg -i "hipaa compliant|strict hipaa" src/ docs/
# Expected: no matches in product/marketing copy (policy docs may reference Tier C definition)
```

## Tranc3 PR checklist

- [ ] All five files updated
- [ ] `id_registry.json` and `id_registry.csv` remain in sync
- [ ] Regenerate `docs/matrix.md` if generated from registry (or edit manually)
- [ ] Link Tranc3 PR in OBL-081 evidence field when merged

---

## Related

- [HIPAA-ALIGNMENT.md](../compliance/HIPAA-ALIGNMENT.md)
- [OBLIGATIONS-REGISTER.md](../compliance/OBLIGATIONS-REGISTER.md) — OBL-081
