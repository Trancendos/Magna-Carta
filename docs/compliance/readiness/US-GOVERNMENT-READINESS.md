# US Government & Defence — Readiness

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Covers:** FW-050–FW-069

---

## 1. Cloud authorisation

### FedRAMP (FW-050)

| Phase | Status | Reference |
|-------|--------|-----------|
| Readiness mapping | ✅ Programme | [FEDRAMP-READINESS.md](../FEDRAMP-READINESS.md) |
| 3PAO assessment | ❌ Not started | Trigger: federal agency RFP |
| Authority to Operate | ❌ | Requires FedRAMP PMO sponsorship |

**Control baseline:** NIST 800-53 Rev 5 moderate; maps to ISO 27001 SOA and SOC 2 CC.

### GovRAMP (FW-051) / FISMA (FW-052)

State and federal agency variants. **Position:** If FedRAMP path initiated, extend control evidence pack; GovRAMP state listings are customer-specific.

---

## 2. Defence (FW-053–FW-059)

| Framework | Status | Notes |
|-----------|--------|-------|
| CMMC 2.0 (FW-053) | ✅ Programme future | [CMMC-READINESS.md](../CMMC-READINESS.md) |
| DoD IL2–IL5 (FW-055–057) | 📋 Readiness | Requires FedRAMP + CUI boundary |
| DoD IL6 (FW-058) | ❌ N/A | Classified — out of scope |
| DFARS 252.204-7012 (FW-059) | 📋 Readiness | Flow-down if CUI subcontract |

**Trigger:** Defence prime or subcontract with CUI.

---

## 3. Cryptography (FW-060 FIPS 140-3)

Use **FIPS 140-3 validated modules** from cloud providers (AWS-LC, Azure, GCP BoringSSL modules) when:

- FedRAMP moderate/high control families require FIPS-validated crypto
- Customer contract specifies FIPS mode

Document module selection in [SYSTEMS-REGISTER.md](../SYSTEMS-REGISTER.md).

---

## 4. Sector-specific US regimes

| FW-ID | Framework | Trigger | Programme artefact |
|-------|-----------|---------|-------------------|
| FW-061 | CJIS | US criminal justice data | Enhanced logging, personnel screening — future annex |
| FW-062 | HIPAA | US PHI | [HIPAA-ALIGNMENT.md](../HIPAA-ALIGNMENT.md), BAA templates |
| FW-063 | FERPA | US education records | Privacy programme + DPA addendum |
| FW-064 | IRS 1075 | Federal tax info | Dedicated handling rules — legal trigger |
| FW-065 | SEC 17a-4(f) | Broker-dealer WORM | Immutable retention architecture review |
| FW-066 | CLOUD Act | US legal process for data | GDPR alignment § transfer mechanisms |
| FW-067 | EAR | Export-controlled tech | Legal review of crypto / dual-use |
| FW-068 | ITAR | Defence articles | ❌ N/A |
| FW-069 | VPAT / Section 508 | Federal accessibility procurement | Accessibility statement + WCAG roadmap |

---

## 5. Layer 3 checklist (when US gov customer emerges)

1. Confirm data residency and sovereignty requirements
2. Select authorisation path (FedRAMP Moderate vs agency ATO)
3. Gap assessment: NIST 800-53 vs current SOA
4. Engage 3PAO / agency sponsor
5. Update marketing and contracts — no claims until ATO

---

**Next review:** 2026-09-06
