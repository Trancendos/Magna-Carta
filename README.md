# Magna Carta — Foundation Document Framework

The **Trancendos Magna Carta** is the governance and compliance foundation for the Tranc3 platform. It unifies policies, procedures, regulatory alignment, architectural controls, and operational blueprints into a single auditable framework.

This repository is the **canonical documentation home** for Magna Carta. Runtime enforcement hooks live in [Tranc3](https://github.com/Trancendos/Tranc3) (`src/compliance/magna_carta.py`).

## Status legend

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme implemented** | Policy, procedure, register, or alignment artefact exists in this repo and is maintained |
| 🎯 **External validation pending** | Certification, fee payment, signed third-party contract, or operational evidence run not yet complete |

## Programme status

| Artifact | Version | Status |
|----------|---------|--------|
| Foundation Framework | 1.0.0 | ✅ Active |
| Compliance Blueprint | 1.0.0 | ✅ Active |
| Architecture Blueprint | 1.0.0 | ✅ Active |
| Policy Library | 1.0.0 | ✅ Active (8 policies) |
| Procedure Library | 1.0.0 | ✅ Active (10 procedures) |
| Governance artefacts | 1.0.0 | ✅ Committee charter, RACI, internal audit programme |
| Evidence & assurance programme | 1.0.0 | ✅ MC-010 (external runs 🎯) |
| Supplier DPA register | 1.0.0 | ✅ Programme (signed DPAs 🎯) |
| Tranc3 Integration Config | 1.0.0 | ✅ Ready for `MAGNA_CARTA_ENABLED=true` |
| ISO 27001 certification | — | 🎯 SOA programme complete; external audit pending |
| SOC 2 Type II | — | 🎯 Controls mapped; external audit pending |
| ICO registration (fee paid) | — | 🎯 Programme documented; live number pending |
| HIPAA Tier C attestation | — | 🎯 BAA programme; per-customer BAAs pending |

**Platform baseline:** Tranc3 v2.1.0-rc1 (as of 2026-05-22)  
**Owner:** Trancendos Platform Engineering  
**Classification:** UNCLASSIFIED — PUBLIC

## Quick navigation

### Core framework

| Document | Purpose |
|----------|---------|
| [FRAMEWORK.md](FRAMEWORK.md) | Master blueprint — how all pieces fit together |
| [docs/00-EXECUTIVE-SUMMARY.md](docs/00-EXECUTIVE-SUMMARY.md) | Executive overview and certification roadmap |
| [docs/01-MAGNACARTA-FOUNDATION.md](docs/01-MAGNACARTA-FOUNDATION.md) | Digital rights, governance principles, Town Hall alignment |

### Compliance & regulation

| Document | Purpose |
|----------|---------|
| [docs/compliance/REGULATION-MATRIX.md](docs/compliance/REGULATION-MATRIX.md) | All regulations mapped to Tranc3 controls |
| [docs/compliance/COMPLIANCE-BLUEPRINT.md](docs/compliance/COMPLIANCE-BLUEPRINT.md) | End-to-end compliance operating model |
| [docs/compliance/OBLIGATIONS-REGISTER.md](docs/compliance/OBLIGATIONS-REGISTER.md) | Regulatory and contractual obligations register |
| [docs/compliance/LEGISLATION-REGISTER.md](docs/compliance/LEGISLATION-REGISTER.md) | UK/EU legislation applicability |
| [docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md](docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md) | Third-party GenAI/compliance frameworks → Magna Carta |
| [docs/compliance/GENAI-MATURITY-ASSESSMENT.md](docs/compliance/GENAI-MATURITY-ASSESSMENT.md) | GenAI governance maturity self-assessment |

### Framework alignments

| Document | Purpose |
|----------|---------|
| [docs/compliance/ISO27001-ALIGNMENT.md](docs/compliance/ISO27001-ALIGNMENT.md) | ISO 27001:2022 control mapping |
| [docs/compliance/SOC2-ALIGNMENT.md](docs/compliance/SOC2-ALIGNMENT.md) | SOC 2 Trust Services Criteria |
| [docs/compliance/GDPR-ALIGNMENT.md](docs/compliance/GDPR-ALIGNMENT.md) | UK GDPR / EU GDPR |
| [docs/compliance/HIPAA-ALIGNMENT.md](docs/compliance/HIPAA-ALIGNMENT.md) | US PHI boundary, BAA tiers, MC-008 / MC-RULE-009 |
| [docs/compliance/FCA-ALIGNMENT.md](docs/compliance/FCA-ALIGNMENT.md) | UK financial conduct (supplier perimeter), MC-009 |
| [docs/compliance/PECR-ALIGNMENT.md](docs/compliance/PECR-ALIGNMENT.md) | Privacy and Electronic Communications Regulations |
| [docs/compliance/COMPANIES-ACT-ALIGNMENT.md](docs/compliance/COMPANIES-ACT-ALIGNMENT.md) | Companies Act 2006 governance duties |
| [docs/compliance/ICO-REGISTRATION.md](docs/compliance/ICO-REGISTRATION.md) | ICO fee tier and registration programme |
| [docs/compliance/SUPPLIER-DPA-REGISTER.md](docs/compliance/SUPPLIER-DPA-REGISTER.md) | Sub-processor DPA/BAA register (human-readable) |
| [docs/compliance/AI-GOVERNANCE.md](docs/compliance/AI-GOVERNANCE.md) | NIST AI RMF / EU AI Act alignment |
| [docs/compliance/DEFSTAN-ALIGNMENT.md](docs/compliance/DEFSTAN-ALIGNMENT.md) | DEF STAN 05-138 cyber security |

### Governance & evidence

| Document | Purpose |
|----------|---------|
| [docs/governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md](docs/governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md) | AI Governance Committee terms of reference |
| [docs/governance/RACI-MATRIX.md](docs/governance/RACI-MATRIX.md) | Control ownership RACI |
| [docs/governance/INTERNAL-AUDIT-PROGRAMME.md](docs/governance/INTERNAL-AUDIT-PROGRAMME.md) | ISO 9.2 internal audit plan (MC-010) |
| [docs/governance/MANAGEMENT-REVIEW-TEMPLATE.md](docs/governance/MANAGEMENT-REVIEW-TEMPLATE.md) | ISO 9.3 management review template |
| [docs/compliance/COMPLIANCE-ACTION-TRACKER.md](docs/compliance/COMPLIANCE-ACTION-TRACKER.md) | Open compliance actions (ACT-001–012) |
| [docs/compliance/RISK-REGISTER.md](docs/compliance/RISK-REGISTER.md) | Information security risk register |
| [docs/compliance/SOC2-EVIDENCE-SCHEDULE.md](docs/compliance/SOC2-EVIDENCE-SCHEDULE.md) | SOC 2 Type II evidence catalogue |
| [docs/evidence/BCP-RESTORE-TEST-LOG.md](docs/evidence/BCP-RESTORE-TEST-LOG.md) | BCP restore test evidence log |
| [docs/evidence/PEN-TEST-PROGRAMME.md](docs/evidence/PEN-TEST-PROGRAMME.md) | Annual penetration test programme |
| [docs/evidence/PEN-TEST-LOG.md](docs/evidence/PEN-TEST-LOG.md) | Penetration test execution log |
| [docs/evidence/POLICY-ATTESTATION-REGISTER.md](docs/evidence/POLICY-ATTESTATION-REGISTER.md) | Staff policy acknowledgement register |

### Architecture

| Document | Purpose |
|----------|---------|
| [docs/architecture/BLUEPRINT.md](docs/architecture/BLUEPRINT.md) | Platform architecture blueprint |
| [docs/architecture/AS-BUILT-ARCHITECTURE.md](docs/architecture/AS-BUILT-ARCHITECTURE.md) | Canonical as-built architecture (auditor-facing) |
| [docs/architecture/CONTROL-TO-COMPONENT-MAP.md](docs/architecture/CONTROL-TO-COMPONENT-MAP.md) | Control traceability to code and workers |

### Policies & procedures

| Document | Purpose |
|----------|---------|
| [docs/policies/INDEX.md](docs/policies/INDEX.md) | Policy library index (8 policies) |
| [docs/procedures/INDEX.md](docs/procedures/INDEX.md) | Procedure library index (10 procedures) |
| [docs/templates/TEMPLATE-DPA-UK-GDPR.md](docs/templates/TEMPLATE-DPA-UK-GDPR.md) | UK GDPR processor DPA template |
| [docs/templates/TEMPLATE-BAA-HIPAA.md](docs/templates/TEMPLATE-BAA-HIPAA.md) | HIPAA business associate agreement template |
| [docs/templates/TEMPLATE-SCC-ANNEX.md](docs/templates/TEMPLATE-SCC-ANNEX.md) | Standard contractual clauses annex template |

### Engineering handoffs (Tranc3 repo)

| Document | Purpose |
|----------|---------|
| [docs/engineering/TRANC3-HIPAA-COPY-REMEDIATION.md](docs/engineering/TRANC3-HIPAA-COPY-REMEDIATION.md) | HIPAA Tier A product copy — patch spec for Tranc3 PR |

### Runtime configuration

| Document | Purpose |
|----------|---------|
| [config/magna_carta_config.json](config/magna_carta_config.json) | Runtime rule configuration for Tranc3 |
| [compliance/magna_carta_register.yaml](compliance/magna_carta_register.yaml) | Magna Carta compliance register (MC-001–MC-010) |
| [compliance/supplier_dpa_register.yaml](compliance/supplier_dpa_register.yaml) | Machine-readable supplier DPA register |
| [compliance/compliance_action_tracker.yaml](compliance/compliance_action_tracker.yaml) | Machine-readable action tracker |
| [compliance/risk_register.yaml](compliance/risk_register.yaml) | Machine-readable risk register |
| [compliance/policy_attestation_register.yaml](compliance/policy_attestation_register.yaml) | Machine-readable policy attestation register |

## Directory structure

```
magna-carta/
├── FRAMEWORK.md
├── README.md
├── config/
│   └── magna_carta_config.json
├── compliance/
│   ├── magna_carta_register.yaml
│   ├── supplier_dpa_register.yaml
│   ├── compliance_action_tracker.yaml
│   ├── risk_register.yaml
│   └── policy_attestation_register.yaml
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
    │   ├── OBLIGATIONS-REGISTER.md
    │   ├── ISO27001-ALIGNMENT.md
    │   ├── SOC2-ALIGNMENT.md
    │   ├── GDPR-ALIGNMENT.md
    │   ├── HIPAA-ALIGNMENT.md
    │   ├── FCA-ALIGNMENT.md
    │   ├── PECR-ALIGNMENT.md
    │   ├── COMPANIES-ACT-ALIGNMENT.md
    │   ├── ICO-REGISTRATION.md
    │   ├── SUPPLIER-DPA-REGISTER.md
    │   ├── DEFSTAN-ALIGNMENT.md
    │   ├── AI-GOVERNANCE.md
    │   ├── GENAI-MATURITY-ASSESSMENT.md
    │   ├── EXTERNAL-FRAMEWORK-MAPPING.md
    │   ├── COMPLIANCE-ACTION-TRACKER.md
    │   ├── RISK-REGISTER.md
    │   └── SOC2-EVIDENCE-SCHEDULE.md
    ├── governance/
    │   ├── AI-GOVERNANCE-COMMITTEE-CHARTER.md
    │   ├── RACI-MATRIX.md
    │   ├── INTERNAL-AUDIT-PROGRAMME.md
    │   └── MANAGEMENT-REVIEW-TEMPLATE.md
    ├── engineering/
    │   └── TRANC3-HIPAA-COPY-REMEDIATION.md
    ├── evidence/
    │   ├── BCP-RESTORE-TEST-LOG.md
    │   ├── PEN-TEST-PROGRAMME.md
    │   ├── PEN-TEST-LOG.md
    │   └── POLICY-ATTESTATION-REGISTER.md
    ├── templates/
    │   ├── TEMPLATE-DPA-UK-GDPR.md
    │   ├── TEMPLATE-BAA-HIPAA.md
    │   └── TEMPLATE-SCC-ANNEX.md
    ├── policies/
    │   ├── INDEX.md
    │   └── POL-*.md (8 policies)
    └── procedures/
        ├── INDEX.md
        └── PROC-*.md (10 procedures)
```

## Relationship to Tranc3

| Magna Carta (this repo) | Tranc3 (implementation) |
|-------------------------|-------------------------|
| Policies, procedures, blueprints | Workers, services, CI gates |
| `magna_carta_config.json` | `MAGNA_CARTA_CONFIG_PATH` env var |
| `magna_carta_register.yaml` | Extends `compliance/register.yaml` |
| Governance narrative | Town Hall API (`/townhall/*`) |
| Architecture blueprint | `ARCHITECTURE_THREAT_MODEL.md`, workers |

**Document precedence:** Legislation → certification → Magna Carta policies → Tranc3 `register.yaml` → procedures → aspirational architecture.

## Enabling in Tranc3

```bash
export MAGNA_CARTA_ENABLED=true
export MAGNA_CARTA_CONFIG_PATH=/path/to/magna-carta/config/magna_carta_config.json
```

## Review cycle

- **Quarterly:** Full framework review aligned with DEFSTAN register review
- **On change:** Major architecture, new worker, security incident, or regulatory change
- **Next review due:** 2026-09-06
