# Framework Readiness Index

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Purpose:** Entry point for grouped readiness and position documents covering the full [STANDARDS-AND-FRAMEWORKS-REGISTER.md](../STANDARDS-AND-FRAMEWORKS-REGISTER.md) catalogue.

---

## How to use

1. Find your framework in the **master register** (`FW-###` ID).
2. Open the **readiness group** listed in the register's *Readiness doc* column.
3. For frameworks with dedicated alignment docs at `docs/compliance/` root, follow that link first.

**Honesty rule:** Programme ✅ in these documents means policies, procedures, registers, and mapping exist in Magna Carta (layer 2). External certification, government authorisation, or customer-specific attestation is layer 3 and requires operational evidence.

**Implementation automation:** Per-framework implementation mapping (signal, trigger, auto-checks, config profile) lives in [`compliance/framework_implementation_catalog.yaml`](../../../compliance/framework_implementation_catalog.yaml). Scope signals and group triggers are in `compliance/proactive_signals.yaml` and `compliance/framework_triggers.yaml`. MON-018 in `scripts/compliance_health_check.py` verifies catalog ↔ register ↔ trigger alignment.

---

## Not applicable (position statements)

| Document | Purpose |
|----------|---------|
| [NOT-APPLICABLE-POSITION.md](NOT-APPLICABLE-POSITION.md) | Formal NA rationale for frameworks marked `not_applicable` in the register (e.g. ITAR, EAR-only, sector-specific regimes outside current scope) |

---

## Grouped readiness documents

| Group | Path | Covers (examples) |
|-------|------|-------------------|
| ISO family | [ISO-FAMILY-READINESS.md](ISO-FAMILY-READINESS.md) | ISO 27001/27017/27018/27701/42001/22301/9001/14001/20000/45001/50001, SNI variants, K-ISMS |
| SOC & assurance | [SOC-AND-ASSURANCE-READINESS.md](SOC-AND-ASSURANCE-READINESS.md) | SOC 1/2/3, CSA STAR, HITRUST, KY3P, ProcessUnity, CyberVadis, Uptime Institute |
| PCI family | [PCI-FAMILY-POSITION.md](PCI-FAMILY-POSITION.md) | PCI DSS, 3DS, P2PE, PIN — extends [PCI-DSS-POSITION.md](../PCI-DSS-POSITION.md) |
| US government | [US-GOVERNMENT-READINESS.md](US-GOVERNMENT-READINESS.md) | FedRAMP, CMMC, DoD levels, FIPS 140-3, CJIS, FISMA, GovRAMP, HIPAA, FERPA, IRS 1075, SEC 17a-4, CLOUD Act, EAR, ITAR, VPAT |
| International assurance | [INTERNATIONAL-ASSURANCE-READINESS.md](INTERNATIONAL-ASSURANCE-READINESS.md) | IRAP, ISMAP, TISAX, C5, ENS, CCCS, UK G-Cloud, NHS DSPT, MeitY, MTCS, ASIP HDS, etc. |
| Global privacy | [GLOBAL-PRIVACY-READINESS.md](GLOBAL-PRIVACY-READINESS.md) | GDPR, CCPA, DPF, and all listed national privacy laws |
| NIST family | [NIST-FAMILY-READINESS.md](NIST-FAMILY-READINESS.md) | NIST 800-53, 800-162, 800-172, 800-34, 800-64, CSF, RMF |
| Industry & sector | [INDUSTRY-SECTOR-READINESS.md](INDUSTRY-SECTOR-READINESS.md) | GxP, DORA, FINMA, MPA, FINTECH, Japan FISC, GSMA, CE+, BIO, UAE IAR |

---

## Dedicated alignment docs (root `docs/compliance/`)

| Framework | Document |
|-----------|----------|
| ISO 27001 | [ISO27001-ALIGNMENT.md](../ISO27001-ALIGNMENT.md) |
| SOC 2 | [SOC2-ALIGNMENT.md](../SOC2-ALIGNMENT.md) |
| GDPR | [GDPR-ALIGNMENT.md](../GDPR-ALIGNMENT.md) |
| HIPAA | [HIPAA-ALIGNMENT.md](../HIPAA-ALIGNMENT.md) |
| CCPA/CPRA | [CCPA-CPRA-ALIGNMENT.md](../CCPA-CPRA-ALIGNMENT.md) |
| NIST CSF | [NIST-CSF-ALIGNMENT.md](../NIST-CSF-ALIGNMENT.md) |
| FedRAMP | [FEDRAMP-READINESS.md](../FEDRAMP-READINESS.md) |
| CMMC | [CMMC-READINESS.md](../CMMC-READINESS.md) |
| PCI DSS | [PCI-DSS-POSITION.md](../PCI-DSS-POSITION.md) |
| NHS DSPT | [NHS-DSPT-READINESS.md](../NHS-DSPT-READINESS.md) |

---

**Next review:** 2026-09-06 (PROC-CMP-001)
