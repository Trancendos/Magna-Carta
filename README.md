# Infinity Network — Magna Carta

**Infinity Network — Magna Carta** is the governance and compliance programme for applications built within the **Infinity Network**, harmonising with **Trancendos Universe — The Foundation** (the master generic platform template).

This repository is the **canonical documentation home** for Magna Carta. It unifies policies, procedures, regulatory alignment, architectural controls, and **zero-cost Layer B automation** into a single auditable framework.

| Layer | What it is |
|-------|------------|
| **Trancendos Universe — The Foundation** | Master template for any new platform (“The Master”) |
| **Infinity Network — Magna Carta** | This repo — compliance for all Infinity Network apps |
| **App Frameworks** | Deployable products: Tranc3, Trance-One, T2ance, Spark, Void, … |

Runtime enforcement for the **Tranc3 App Framework** lives in the [Tranc3](https://github.com/Trancendos/Tranc3) app repo (`src/compliance/magna_carta.py`). See [docs/architecture/TRANCENDOS-UNIVERSE-AND-INFINITY-NETWORK.md](docs/architecture/TRANCENDOS-UNIVERSE-AND-INFINITY-NETWORK.md).

## Status legend

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme artefact** | Policy, procedure, register, or alignment document **exists in this repo** and is maintained (documentation programme — not operational certification) |
| 🎯 **Operational validation pending** | Board approval, signed contract, certification audit, fee payment, drill, observation window, or production enforcement not yet demonstrated |

**Three layers:** (1) Trancendos Universe / App Framework controls in code · (2) Magna Carta documentation in this repo · (3) validated operations and external assurance. ✅ marks layer 2 only unless stated otherwise. See [docs/00-EXECUTIVE-SUMMARY.md](docs/00-EXECUTIVE-SUMMARY.md#maturity-model-read-this-first).

## Programme status

| Artifact | Version | Status |
|----------|---------|--------|
| Foundation Framework | 1.0.0 | ✅ Active |
| Compliance Blueprint | 1.0.0 | ✅ Active |
| Architecture Blueprint | 1.0.0 | ✅ Active |
| Policy Library | 1.0.0 | ✅ Authored (9 policies; BoardRoom approval 🎯) |
| Procedure Library | 1.1.0 | ✅ Active (25 procedures) |
| Documentation artefact model | 1.2.0 | ✅ Full cookbook/hymn coverage (25/25 procedures) |
| Department bibles & job descriptions | 1.0.0 | ✅ 16 bibles, 13 role JDs (appointments in HRIS 🎯) |
| Compliance maturity benchmark | 1.0.0 | ✅ Honest % and Vanta-class comparison |
| Compliance maintenance monitor | 1.1.0 | ✅ Local weekly health check (no cloud CI) |
| Governance artefacts | 1.0.0 | ✅ Draft charter, RACI, audit programme (operational use 🎯) |
| Evidence & assurance programme | 1.0.0 | ✅ MC-010 authored (pen test / attestations / audits 🎯) |
| Infinity App (Tranc3) bridge | 1.0.0 | ✅ MC-011 authored (staging enablement / enforcement 🎯) |
| Supplier DPA register | 1.0.0 | ✅ Register exists (**signed DPAs incomplete** 🎯) |
| Infinity App (Tranc3) integration config | 1.0.0 | ✅ Spec ready; production enablement 🎯 |
| ISO 27001 certification | — | 🎯 SOA drafted; org controls partial; external audit pending |
| SOC 2 Type II | — | 🎯 TSC mapped; 6-month observation window not started |
| ICO registration (fee paid) | — | 🎯 Programme documented; live number pending |
| HIPAA Tier C attestation | — | 🎯 BAA programme; per-customer BAAs pending |

**Platform baseline:** Tranc3 App Framework v2.1.0-rc1 (as of 2026-05-22)  
**Owner:** Trancendos Platform Engineering  
**Classification:** UNCLASSIFIED — PUBLIC

## Quick navigation

### Core framework

| Document | Purpose |
|----------|---------|
| [FRAMEWORK.md](FRAMEWORK.md) | Master blueprint — how all pieces fit together |
| [docs/architecture/TRANCENDOS-UNIVERSE-AND-INFINITY-NETWORK.md](docs/architecture/TRANCENDOS-UNIVERSE-AND-INFINITY-NETWORK.md) | Universe (Foundation) → Infinity Network → App Frameworks hierarchy |
| [docs/00-EXECUTIVE-SUMMARY.md](docs/00-EXECUTIVE-SUMMARY.md) | Executive overview and certification roadmap |
| [docs/01-MAGNACARTA-FOUNDATION.md](docs/01-MAGNACARTA-FOUNDATION.md) | Digital rights, governance principles, Town Hall alignment |
| [docs/compliance/ZERO-COST-SECURITY-TOOLING.md](docs/compliance/ZERO-COST-SECURITY-TOOLING.md) | £0/$0 Layer B tooling policy (Aikido optional; local scripts mandatory) |

### Compliance & regulation

| Document | Purpose |
|----------|---------|
| [docs/compliance/REGULATION-MATRIX.md](docs/compliance/REGULATION-MATRIX.md) | All regulations mapped to Infinity Network / Trancendos Universe controls |
| [docs/compliance/COMPLIANCE-COVERAGE-REGISTER.md](docs/compliance/COMPLIANCE-COVERAGE-REGISTER.md) | Honest ⚠️/📋/❌ status — why not operational ✅ |
| [docs/compliance/COMPLIANCE-BLUEPRINT.md](docs/compliance/COMPLIANCE-BLUEPRINT.md) | End-to-end compliance operating model |
| [docs/compliance/OBLIGATIONS-REGISTER.md](docs/compliance/OBLIGATIONS-REGISTER.md) | Regulatory and contractual obligations register |
| [docs/compliance/LEGISLATION-REGISTER.md](docs/compliance/LEGISLATION-REGISTER.md) | UK/EU legislation applicability |
| [compliance/legislation_register.yaml](compliance/legislation_register.yaml) | Machine-readable legislation register (CELEX / ELI identifiers) |
| [docs/compliance/EUR-LEX-ELI-REFERENCE.md](docs/compliance/EUR-LEX-ELI-REFERENCE.md) | EUR-Lex / ELI citation guide for EU acts |
| [docs/compliance/EU-LEGISLATION-MONITORING.md](docs/compliance/EU-LEGISLATION-MONITORING.md) | Quarterly EU delegated-act monitoring workflow |
| [docs/compliance/ETSI-SAI-ALIGNMENT.md](docs/compliance/ETSI-SAI-ALIGNMENT.md) | ETSI EN 304 223 Securing AI baseline alignment |
| [docs/compliance/HARMONISED-STANDARDS-MONITORING.md](docs/compliance/HARMONISED-STANDARDS-MONITORING.md) | Semi-annual ETSI + CEN/CENELEC harmonised standards watch |
| [compliance/standards_watch.yaml](compliance/standards_watch.yaml) | Machine-readable ETSI / harmonised standards register |
| [docs/compliance/STANDARDS-REGISTER.md](docs/compliance/STANDARDS-REGISTER.md) | ISO, NIST, DEFSTAN, OWASP and framework standards |
| [docs/compliance/STANDARDS-AND-FRAMEWORKS-REGISTER.md](docs/compliance/STANDARDS-AND-FRAMEWORKS-REGISTER.md) | Master catalogue (FW-001–FW-145, 127 frameworks) |
| [docs/compliance/readiness/INDEX.md](docs/compliance/readiness/INDEX.md) | Grouped readiness docs (ISO, SOC, PCI, NIST, privacy, gov) |
| [docs/compliance/REGULATORS-OMBUDSMEN-REGISTER.md](docs/compliance/REGULATORS-OMBUDSMEN-REGISTER.md) | Regulators, supervisory authorities, ombudsmen |
| [docs/compliance/SYSTEMS-REGISTER.md](docs/compliance/SYSTEMS-REGISTER.md) | Governance and compliance systems (Town Hall, registers, CI) |
| [docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md](docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md) | Third-party GenAI/compliance frameworks → Magna Carta |
| [docs/compliance/GENAI-MATURITY-ASSESSMENT.md](docs/compliance/GENAI-MATURITY-ASSESSMENT.md) | GenAI governance maturity self-assessment |
| [docs/compliance/COMPLIANCE-MATURITY-AND-BENCHMARK.md](docs/compliance/COMPLIANCE-MATURITY-AND-BENCHMARK.md) | Honest completion %, Vanta-class CCM comparison |
| [docs/compliance/COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md](docs/compliance/COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md) | Programme layer 100% inventory (in-repo artefacts) |
| [docs/compliance/AI-SECURITY-SCOPING-MATRIX.md](docs/compliance/AI-SECURITY-SCOPING-MATRIX.md) | AI Answers/Connects/Acts tiers and Input/Model/Output grid |

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
| [docs/governance/CONTINUOUS-IMPROVEMENT-PROGRAMME.md](docs/governance/CONTINUOUS-IMPROVEMENT-PROGRAMME.md) | PDCA cycle linking evidence programme to operations (MC-011) |
| [docs/governance/DOCUMENTATION-ARTIFACT-MODEL.md](docs/governance/DOCUMENTATION-ARTIFACT-MODEL.md) | Taxonomy: policies, cookbooks, bibles, hymn sheets, schemas |
| [docs/governance/COMPLIANCE-MAINTENANCE-PROGRAMME.md](docs/governance/COMPLIANCE-MAINTENANCE-PROGRAMME.md) | Automated freshness monitoring and review cadence |
| [docs/governance/REVIEWERS-REGISTER.md](docs/governance/REVIEWERS-REGISTER.md) | Reviewer roles, RACI, and escalation paths |
| [docs/compliance/COMPLIANCE-ACTION-TRACKER.md](docs/compliance/COMPLIANCE-ACTION-TRACKER.md) | Open compliance actions (ACT-001–015) |
| [docs/compliance/TRANC3-REGISTER-BRIDGE.md](docs/compliance/TRANC3-REGISTER-BRIDGE.md) | MC-001–MC-011 ↔ REQ-### / MC-RULE mapping (MC-011) |
| [docs/compliance/RISK-REGISTER.md](docs/compliance/RISK-REGISTER.md) | Information security risk register |
| [docs/compliance/SOC2-EVIDENCE-SCHEDULE.md](docs/compliance/SOC2-EVIDENCE-SCHEDULE.md) | SOC 2 Type II evidence catalogue |
| [docs/evidence/BCP-RESTORE-TEST-LOG.md](docs/evidence/BCP-RESTORE-TEST-LOG.md) | BCP restore test evidence log |
| [docs/evidence/PEN-TEST-PROGRAMME.md](docs/evidence/PEN-TEST-PROGRAMME.md) | Annual penetration test programme |
| [docs/evidence/PEN-TEST-LOG.md](docs/evidence/PEN-TEST-LOG.md) | Penetration test execution log |
| [docs/evidence/POLICY-ATTESTATION-REGISTER.md](docs/evidence/POLICY-ATTESTATION-REGISTER.md) | Staff policy acknowledgement register |
| [docs/evidence/COMPLIANCE-HEALTH-LOG.md](docs/evidence/COMPLIANCE-HEALTH-LOG.md) | Weekly documentation health check audit trail |

### Architecture

| Document | Purpose |
|----------|---------|
| [docs/architecture/BLUEPRINT.md](docs/architecture/BLUEPRINT.md) | Platform architecture blueprint |
| [docs/architecture/AS-BUILT-ARCHITECTURE.md](docs/architecture/AS-BUILT-ARCHITECTURE.md) | Canonical as-built architecture (auditor-facing) |
| [docs/architecture/CONTROL-TO-COMPONENT-MAP.md](docs/architecture/CONTROL-TO-COMPONENT-MAP.md) | Control traceability to code and workers |

### Operational artefacts (cookbooks, bibles, hymn sheets)

| Document | Purpose |
|----------|---------|
| [docs/bibles/INDEX.md](docs/bibles/INDEX.md) | Bible library (16 domain bibles + governance/privacy/security) |
| [docs/bibles/MAGNACARTA-GOVERNANCE-BIBLE.md](docs/bibles/MAGNACARTA-GOVERNANCE-BIBLE.md) | Governance encyclopaedia — how everything fits together |
| [docs/job-descriptions/INDEX.md](docs/job-descriptions/INDEX.md) | Role definitions for ISMS, DPO, departmental PROC owners |
| [docs/cookbooks/INDEX.md](docs/cookbooks/INDEX.md) | Step-by-step operational playbooks |
| [docs/hymn-sheets/INDEX.md](docs/hymn-sheets/INDEX.md) | Printable checklists for reviews and incidents |
| [docs/schemas/REGISTER-SCHEMAS.md](docs/schemas/REGISTER-SCHEMAS.md) | YAML/Markdown register field schemas |

### Policies & procedures

| Document | Purpose |
|----------|---------|
| [docs/policies/INDEX.md](docs/policies/INDEX.md) | Policy library index (9 policies) |
| [docs/procedures/INDEX.md](docs/procedures/INDEX.md) | Procedure library index (25 procedures) |
| [docs/templates/TEMPLATE-DPA-UK-GDPR.md](docs/templates/TEMPLATE-DPA-UK-GDPR.md) | UK GDPR processor DPA template |
| [docs/templates/TEMPLATE-BAA-HIPAA.md](docs/templates/TEMPLATE-BAA-HIPAA.md) | HIPAA business associate agreement template |
| [docs/templates/TEMPLATE-SCC-ANNEX.md](docs/templates/TEMPLATE-SCC-ANNEX.md) | Standard contractual clauses annex template |
| [docs/templates/INDEX.md](docs/templates/INDEX.md) | Contract template library index |

### Engineering handoffs (Tranc3 repo)

| Document | Purpose |
|----------|---------|
| [docs/engineering/TRANC3-INTEGRATION-GUIDE.md](docs/engineering/TRANC3-INTEGRATION-GUIDE.md) | Staging enablement for `MAGNA_CARTA_ENABLED`, checker import (ACT-009) |
| [docs/engineering/TRANC3-HIPAA-COPY-REMEDIATION.md](docs/engineering/TRANC3-HIPAA-COPY-REMEDIATION.md) | HIPAA Tier A product copy — patch spec for Tranc3 PR (ACT-006) |

### Runtime configuration

| Document | Purpose |
|----------|---------|
| [config/magna_carta_config.json](config/magna_carta_config.json) | Runtime rule configuration for Tranc3 |
| [compliance/magna_carta_register.yaml](compliance/magna_carta_register.yaml) | Magna Carta compliance register (MC-001–MC-011) |
| [compliance/tranc3_register_bridge.yaml](compliance/tranc3_register_bridge.yaml) | MC↔REQ bridge mapping (machine-readable) |
| [compliance/supplier_dpa_register.yaml](compliance/supplier_dpa_register.yaml) | Machine-readable supplier DPA register |
| [compliance/compliance_action_tracker.yaml](compliance/compliance_action_tracker.yaml) | Machine-readable action tracker |
| [compliance/risk_register.yaml](compliance/risk_register.yaml) | Machine-readable risk register |
| [compliance/policy_attestation_register.yaml](compliance/policy_attestation_register.yaml) | Machine-readable policy attestation register |
| [compliance/frameworks_register.yaml](compliance/frameworks_register.yaml) | Machine-readable frameworks catalogue (MON-009) |
| [compliance/framework_implementation_catalog.yaml](compliance/framework_implementation_catalog.yaml) | Per-framework implementation tier, signal, and trigger (MON-018) |
| [compliance/proactive_signals.yaml](compliance/proactive_signals.yaml) | Scope signals for optional/conditional frameworks |
| [compliance/framework_triggers.yaml](compliance/framework_triggers.yaml) | Enforcement and scan wiring when signals activate |
| [scripts/generate_framework_implementation.py](scripts/generate_framework_implementation.py) | Regenerate catalog, signals, and triggers from register |
| [compliance/maintenance_monitor.yaml](compliance/maintenance_monitor.yaml) | Documentation health monitor configuration |
| [compliance/health_check_history.yaml](compliance/health_check_history.yaml) | Append-only weekly health check run log |
| [scripts/compliance_health_check.py](scripts/compliance_health_check.py) | Automated drift, staleness, and link checker |
| [scripts/weekly_compliance_health.sh](scripts/weekly_compliance_health.sh) | Weekly wrapper (logs results; zero cloud CI cost) |
| [scripts/zero_cost_tooling_check.py](scripts/zero_cost_tooling_check.py) | Verifies mandatory zero-cost tooling paths (ZCT) |
| [scripts/run_oss_security_scans.sh](scripts/run_oss_security_scans.sh) | OSS security stack SEC-006 (free Aikido alternative) |
| [scripts/install_zero_cost_security_stack.sh](scripts/install_zero_cost_security_stack.sh) | Install gitleaks, bandit, semgrep, pip-audit (£0) |
| [scripts/run_layer_b_local_ci.sh](scripts/run_layer_b_local_ci.sh) | Local Layer B CI — no GitHub Actions |
| [docs/compliance/LOCAL-CI-AND-OSS-SECURITY.md](docs/compliance/LOCAL-CI-AND-OSS-SECURITY.md) | Local CI + OSS stack policy |
| [compliance/zero_cost_tooling_register.yaml](compliance/zero_cost_tooling_register.yaml) | Machine-readable zero-cost tooling register |
| [compliance/infinity_app_frameworks_register.yaml](compliance/infinity_app_frameworks_register.yaml) | Infinity Network app framework catalogue |
| [scripts/install_local_weekly_cron.sh](scripts/install_local_weekly_cron.sh) | Optional local crontab installer (Mondays 08:00) |

## Verify Layer B (zero cost)

```bash
pip install -r requirements.txt
./scripts/install_zero_cost_security_stack.sh   # optional: OSS scanners (100% free)
./scripts/run_layer_b_local_ci.sh             # local CI — no GitHub Actions
python3 scripts/readiness_automation_score.py --report
./scripts/weekly_compliance_health.sh
```

## Directory structure

```
magna-carta/
├── FRAMEWORK.md
├── README.md
├── config/
│   └── magna_carta_config.json
├── compliance/
│   ├── magna_carta_register.yaml
│   ├── tranc3_register_bridge.yaml
│   ├── supplier_dpa_register.yaml
│   ├── compliance_action_tracker.yaml
│   ├── risk_register.yaml
│   ├── policy_attestation_register.yaml
│   ├── maintenance_monitor.yaml
│   ├── health_check_history.yaml
│   └── schemas/
├── scripts/
│   ├── compliance_health_check.py
│   ├── weekly_compliance_health.sh
│   └── install_local_weekly_cron.sh
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
    │   ├── SOC2-EVIDENCE-SCHEDULE.md
    │   ├── TRANC3-REGISTER-BRIDGE.md
    │   ├── COMPLIANCE-COVERAGE-REGISTER.md
    │   ├── COMPLIANCE-MATURITY-AND-BENCHMARK.md
    │   ├── AI-SECURITY-SCOPING-MATRIX.md
    │   ├── STANDARDS-REGISTER.md
    │   ├── REGULATORS-OMBUDSMEN-REGISTER.md
    │   └── SYSTEMS-REGISTER.md
    ├── bibles/
    │   ├── INDEX.md
    │   └── *-BIBLE.md (16 domain bibles)
    ├── job-descriptions/
    │   ├── INDEX.md
    │   └── JD-*.md (13 roles)
    ├── cookbooks/
    │   ├── INDEX.md
    │   └── COOK-*.md
    ├── hymn-sheets/
    │   ├── INDEX.md
    │   └── HYMN-*.md
    ├── schemas/
    │   └── REGISTER-SCHEMAS.md
    ├── governance/
    │   ├── AI-GOVERNANCE-COMMITTEE-CHARTER.md
    │   ├── RACI-MATRIX.md
    │   ├── INTERNAL-AUDIT-PROGRAMME.md
    │   ├── MANAGEMENT-REVIEW-TEMPLATE.md
    │   ├── CONTINUOUS-IMPROVEMENT-PROGRAMME.md
    │   ├── DOCUMENTATION-ARTIFACT-MODEL.md
    │   ├── COMPLIANCE-MAINTENANCE-PROGRAMME.md
    │   └── REVIEWERS-REGISTER.md
    ├── engineering/
    │   ├── INFINITY-APP-TRANC3-INTEGRATION-GUIDE.md
    │   ├── TRANC3-INTEGRATION-GUIDE.md
    │   └── TRANC3-HIPAA-COPY-REMEDIATION.md
    ├── evidence/
    │   ├── BCP-RESTORE-TEST-LOG.md
    │   ├── PEN-TEST-PROGRAMME.md
    │   ├── PEN-TEST-LOG.md
    │   └── POLICY-ATTESTATION-REGISTER.md
    ├── templates/
    │   ├── INDEX.md
    │   ├── TEMPLATE-DPA-UK-GDPR.md
    │   ├── TEMPLATE-BAA-HIPAA.md
    │   └── TEMPLATE-SCC-ANNEX.md
    ├── policies/
    │   ├── INDEX.md
    │   └── POL-*.md (9 policies)
    └── procedures/
        ├── INDEX.md
        └── PROC-*.md (25 procedures)
```

## Infinity App bridge (Tranc3 exemplar)

| Infinity Network — Magna Carta (this repo) | Tranc3 App Framework (implementation) |
|--------------------------------------------|---------------------------------------|
| Policies, procedures, blueprints | Workers, services, CI gates |
| `magna_carta_config.json` | `MAGNA_CARTA_CONFIG_PATH` env var |
| `magna_carta_register.yaml` | Extends app `compliance/register.yaml` |
| `tranc3_register_bridge.yaml` | MC-### ↔ REQ-### crosswalk for checker import |
| Governance narrative | Town Hall API (`/townhall/*`) |
| Architecture blueprint | `ARCHITECTURE_THREAT_MODEL.md`, workers |

Other App Frameworks (Trance-One, T2ance, Spark, Void) follow the same bridge pattern when active — see [compliance/infinity_app_frameworks_register.yaml](compliance/infinity_app_frameworks_register.yaml).

**Document precedence:** Legislation → certification → Magna Carta policies → app framework `register.yaml` → procedures → aspirational architecture.

## Enabling in Tranc3 App Framework

```bash
export MAGNA_CARTA_ENABLED=true
export MAGNA_CARTA_CONFIG_PATH=/path/to/magna-carta/config/magna_carta_config.json
```

See [docs/engineering/INFINITY-APP-TRANC3-INTEGRATION-GUIDE.md](docs/engineering/INFINITY-APP-TRANC3-INTEGRATION-GUIDE.md) for staging checklist and checker import steps (ACT-009).

## Review cycle

- **Quarterly:** Full framework review aligned with DEFSTAN register review
- **On change:** Major architecture, new worker, security incident, or regulatory change
- **Next review due:** 2026-09-06
