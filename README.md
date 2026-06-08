# Magna Carta — Foundation Document Framework

The **Trancendos Magna Carta** is the governance and compliance foundation for the Tranc3 platform. It unifies policies, procedures, regulatory alignment, architectural controls, and operational blueprints into a single auditable framework.

This repository is the **canonical documentation home** for Magna Carta. Runtime enforcement hooks live in [Tranc3](https://github.com/Trancendos/Tranc3) (`src/compliance/magna_carta.py`).

## Status

| Artifact | Version | Status |
|----------|---------|--------|
| Foundation Framework | 1.0.0 | Active |
| Compliance Blueprint | 1.0.0 | Active |
| Architecture Blueprint | 1.0.0 | Active |
| Policy Library | 1.0.0 | Active (baseline set) |
| Procedure Library | 1.0.0 | Active (baseline set) |
| Tranc3 Integration Config | 1.0.0 | Ready for `MAGNA_CARTA_ENABLED=true` |

**Platform baseline:** Tranc3 v2.1.0-rc1 (as of 2026-05-22)  
**Owner:** Trancendos Platform Engineering  
**Classification:** UNCLASSIFIED — PUBLIC

## Quick navigation

| Document | Purpose |
|----------|---------|
| [FRAMEWORK.md](FRAMEWORK.md) | Master blueprint — how all pieces fit together |
| [docs/00-EXECUTIVE-SUMMARY.md](docs/00-EXECUTIVE-SUMMARY.md) | Executive overview and certification roadmap |
| [docs/01-MAGNACARTA-FOUNDATION.md](docs/01-MAGNACARTA-FOUNDATION.md) | Digital rights, governance principles, Town Hall alignment |
| [docs/compliance/REGULATION-MATRIX.md](docs/compliance/REGULATION-MATRIX.md) | All regulations mapped to Tranc3 controls |
| [docs/compliance/COMPLIANCE-BLUEPRINT.md](docs/compliance/COMPLIANCE-BLUEPRINT.md) | End-to-end compliance operating model |
| [docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md](docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md) | Third-party GenAI/compliance frameworks → Magna Carta |
| [docs/compliance/GENAI-MATURITY-ASSESSMENT.md](docs/compliance/GENAI-MATURITY-ASSESSMENT.md) | GenAI governance maturity self-assessment |
| [docs/compliance/OBLIGATIONS-REGISTER.md](docs/compliance/OBLIGATIONS-REGISTER.md) | Regulatory and contractual obligations register |
| [docs/architecture/BLUEPRINT.md](docs/architecture/BLUEPRINT.md) | Platform architecture blueprint |
| [docs/architecture/AS-BUILT-ARCHITECTURE.md](docs/architecture/AS-BUILT-ARCHITECTURE.md) | Canonical as-built architecture (auditor-facing) |
| [docs/architecture/CONTROL-TO-COMPONENT-MAP.md](docs/architecture/CONTROL-TO-COMPONENT-MAP.md) | Control traceability to code and workers |
| [config/magna_carta_config.json](config/magna_carta_config.json) | Runtime rule configuration for Tranc3 |

## Directory structure

```
magna-carta/
├── FRAMEWORK.md                 # Master blueprint
├── README.md                    # This file
├── config/
│   └── magna_carta_config.json
├── compliance/
│   └── magna_carta_register.yaml
└── docs/
    ├── 00-EXECUTIVE-SUMMARY.md
    ├── 01-MAGNACARTA-FOUNDATION.md
    ├── architecture/
    │   ├── BLUEPRINT.md
    │   ├── AS-BUILT-ARCHITECTURE.md
    │   └── CONTROL-TO-COMPONENT-MAP.md
    ├── compliance/
    │   ├── REGULATION-MATRIX.md
    │   ├── COMPLIANCE-BLUEPRINT.md
    │   ├── LEGISLATION-REGISTER.md
    │   ├── ISO27001-ALIGNMENT.md
    │   ├── SOC2-ALIGNMENT.md
    │   ├── GDPR-ALIGNMENT.md
    │   ├── DEFSTAN-ALIGNMENT.md
    │   └── AI-GOVERNANCE.md
    ├── policies/
    │   ├── INDEX.md
    │   ├── information-security-policy.md
    │   ├── acceptable-use-policy.md
    │   ├── data-protection-privacy-policy.md
    │   ├── incident-response-policy.md
    │   ├── change-management-policy.md
    │   ├── business-continuity-policy.md
    │   ├── supplier-management-policy.md
    │   └── ai-ethics-policy.md
    └── procedures/
        ├── INDEX.md
        ├── incident-response-procedure.md
        ├── change-request-procedure.md
        ├── access-provisioning-procedure.md
        ├── data-subject-request-procedure.md
        ├── vulnerability-management-procedure.md
        ├── backup-restore-procedure.md
        └── compliance-review-procedure.md
```

## Relationship to Tranc3

| Magna Carta (this repo) | Tranc3 (implementation) |
|-------------------------|-------------------------|
| Policies, procedures, blueprints | Workers, services, CI gates |
| `magna_carta_config.json` | `MAGNA_CARTA_CONFIG_PATH` env var |
| `magna_carta_register.yaml` | Extends `compliance/register.yaml` |
| Governance narrative | Town Hall API (`/townhall/*`) |
| Architecture blueprint | `ARCHITECTURE_THREAT_MODEL.md`, workers |

## Enabling in Tranc3

```bash
export MAGNA_CARTA_ENABLED=true
export MAGNA_CARTA_CONFIG_PATH=/path/to/magna-carta/config/magna_carta_config.json
```

## Review cycle

- **Quarterly:** Full framework review aligned with DEFSTAN register review
- **On change:** Major architecture, new worker, security incident, or regulatory change
- **Next review due:** 2026-09-06
