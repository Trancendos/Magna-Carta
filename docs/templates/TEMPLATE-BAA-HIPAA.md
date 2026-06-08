# Template — HIPAA Business Associate Agreement (Outline)

**Version:** 1.0.0 (outline)  
**Date:** 2026-06-07  
**Owner:** Legal / DPO  
**Use:** SUP-005 health connectors; per-customer HIPAA profile  
**Alignment:** [HIPAA-ALIGNMENT.md](../compliance/HIPAA-ALIGNMENT.md) §4  
**Status:** ✅ Programme outline · 🎯 Legal review and per-customer execution

---

## Parties

- **Covered Entity / Business Associate upstream:** [Customer or platform customer]
- **Business Associate:** Trancendos Ltd (when processing PHI on behalf of covered entity)

## Required provisions (45 CFR §164.504(e))

1. Permitted and required uses and disclosures of PHI
2. Safeguards per §164.308, §164.312 (reference Tranc3 technical controls)
3. Report security incidents and breaches per §164.410
4. Subcontractor BAAs (flow-down to SUP-005 connectors)
5. Access to PHI for HHS audit
6. Return or destruction of PHI at termination
7. Breach notification to covered entity without unreasonable delay

## Trancendos-specific schedules

| Schedule | Content |
|----------|---------|
| A | Services and PHI categories (Sync-Bot, wellbeing tier) |
| B | Security measures (encryption, audit, Ice Box isolation) |
| C | Subcontractors (from supplier register) |

## Marketing alignment

Tier C attestation requires executed BAA before "HIPAA compliant" customer-facing claims. See HIPAA-ALIGNMENT §10.

## Execution checklist

- [ ] HIPAA profile enabled in deployment config
- [ ] BAA countersigned
- [ ] SUP-005 register row updated
- [ ] MC-RULE-009 health_data checks active

**Related:** ACT-002 · MC-008
