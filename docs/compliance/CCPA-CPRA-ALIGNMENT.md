# CCPA / CPRA Alignment Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** DPO  
**Jurisdiction:** California, USA (CCPA as amended by CPRA)  
**Status:** ✅ Programme (readiness) — activate when CA users material

---

## 1. Applicability trigger

| Trigger | Threshold | Current posture |
|---------|-----------|-----------------|
| CA residents in customer/user base | Material volume (legal assessment) | **Not activated** — GDPR baseline controls apply |
| Annual revenue / data sale | CPRA business thresholds | Monitor if US commercial scale grows |

**Position:** Trancendos UK/EU-first. GDPR programme provides **substantial overlap**. This document ensures **rapid activation** without gap if California becomes material.

---

## 2. CPRA consumer rights mapping

| Right | CPRA | Existing GDPR control | Activation step |
|-------|------|----------------------|-----------------|
| Know / access | §1798.100 | PROC-DSR-001 | Add CA-specific response text |
| Delete | §1798.105 | PROC-DSR-001 | Same workflow |
| Correct | §1798.106 | PROC-DSR-001 | Enable correction path in portal |
| Opt-out of sale/share | §1798.120 | No sale of personal data (ROPA) | Publish "Do Not Sell or Share" link if any sharing |
| Limit use of sensitive PI | §1798.121 | MC-RULE-009 PHI fields | Extend notice for CA sensitive categories |
| Non-discrimination | §1798.125 | POL-PRI-001 | Training for support staff |

---

## 3. Required notices (when activated)

1. **Privacy policy** — Add CPRA-specific section (categories, purposes, retention, rights).
2. **Notice at collection** — Point-of-collection link for web/app signup.
3. **Do Not Sell or Share** — Only if sharing for cross-context behavioural advertising (default: **not applicable**).

---

## 4. Service provider contracts

| Requirement | Control |
|-------------|---------|
| Written contract prohibiting sale | DPA template + [SUPPLIER-DPA-REGISTER](SUPPLIER-DPA-REGISTER.md) |
| Purpose limitation | Standard DPA clauses |
| Sub-processor flow-down | POL-SUP-001 |

---

## 5. Operational activation checklist

- [ ] Legal confirms CA user materiality
- [ ] Privacy notice updated (CPRA annex)
- [ ] DSR portal tags CA requests
- [ ] ROPA row for CA residents
- [ ] Vendor DPAs reviewed for CPRA service-provider language
- [ ] Staff training (PROC-TRN-001 addendum)

---

## 6. Related documents

- [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md)
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
- [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md)
