# PCI DSS Position Statement

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead / Legal  
**Status:** ❌ Not applicable — ✅ Programme (position documented)

---

## 1. Position

Tranc3 **does not** store, process, or transmit cardholder data (CHD) in a cardholder data environment (CDE). Payment acceptance, if offered, is intended to route through **authorised third-party payment service providers** (e.g. PSP under SUP-003) using hosted fields or redirect flows.

---

## 2. Scope boundaries

| Element | Tranc3 position |
|---------|-----------------|
| PAN / CVV storage | ❌ Not in scope |
| Payment forms on platform | Redirect or PSP tokenisation only |
| SAQ type | Not applicable unless scope changes |
| Network segmentation for CDE | N/A |

---

## 3. Trigger checklist (re-assess if)

- [ ] Direct card capture on Tranc3-owned UI
- [ ] Storage of payment tokens outside PSP vault
- [ ] Merchant-of-record status for Trancendos

---

## 4. Related documents

- [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md) — SUP-003 PSP
- [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md) §2
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md) §2
