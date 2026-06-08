# FedRAMP Readiness Annex

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Status:** ❌ Not applicable — ✅ Programme future-readiness

---

## 1. Position

Tranc3 is **not** offered as a FedRAMP-authorised cloud service. This annex documents **what would be required** if a US federal agency customer mandates FedRAMP Moderate or High.

---

## 2. Prerequisites (high level)

| Area | Current state | FedRAMP gap |
|------|---------------|-------------|
| US data residency | Configurable; PHI rules in MC-RULE-009 | Agency-specific boundary |
| SSP / control baseline | ISO SOA, SOC2 mapping | NIST 800-53 Rev 5 full SSP |
| Continuous monitoring | Observability planned | ConMon package |
| 3PAO assessment | Not performed | Authorisation boundary audit |
| Incident reporting | PROC-IR-001 | US-CERT / agency IR timelines |

---

## 3. Trigger checklist

- [ ] Federal RFP received
- [ ] Authorisation boundary defined (IaaS/PaaS/SaaS)
- [ ] Gap assessment vs NIST 800-53 Moderate
- [ ] Budget for 3PAO and ConMon tooling
- [ ] US persons data handling legal review

---

## 4. Related documents

- [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md) — adjacent US health boundary
- [COMPLIANCE-COVERAGE-REGISTER.md](COMPLIANCE-COVERAGE-REGISTER.md)
