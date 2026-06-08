# Executive Summary — Magna Carta Framework

**Organisation:** Trancendos Ltd  
**Platform:** Tranc3  
**Document version:** 1.0.0  
**Date:** 2026-06-07  
**Classification:** UNCLASSIFIED — PUBLIC

---

## What this is

The **Magna Carta Framework** is Trancendos' unified governance, compliance, and architecture documentation suite for the Tranc3 AI platform. It consolidates:

- **8 enterprise policies** covering security, privacy, operations, suppliers, and AI ethics (authored in this repo; BoardRoom approval 🎯 for several — see [COMPLIANCE-BLUEPRINT.md](compliance/COMPLIANCE-BLUEPRINT.md) §9)
- **10 operational procedures** with clear triggers, owners, and evidence requirements
- **14+ regulatory alignment documents** (ISO 27001, SOC 2, GDPR, DEFSTAN, AI, HIPAA, FCA, PECR, Companies Act, and more)
- **Governance artefacts** — AI Governance Committee charter, RACI matrix, internal audit programme, management review template
- **Evidence & assurance programme (MC-010)** — action tracker, risk register, SOC 2 evidence schedule, pen test programme, policy attestation register, contract templates
- **Tranc3 integration bridge (MC-011)** — MC↔REQ register mapping, staging integration guide, continuous improvement programme, template library index
- **3 architecture blueprints** including an auditor-facing as-built reference
- **Runtime configuration** for Tranc3 compliance enforcement

## Why it exists

Tranc3 already implements strong technical controls (Zero Trust IAM, encrypted vault, audit ledger, Ice Box threat isolation, DEFSTAN CI gate). What was missing was a **single, customer- and auditor-facing documentation layer** that:

1. States organisational intent (policies)
2. Describes execution (procedures)
3. Maps regulations to implementation (compliance matrix)
4. Defines canonical architecture (as-built vs aspirational)
5. Activates the previously placeholder Magna Carta runtime module

## Maturity model (read this first)

This framework spans **three layers**. Documents in *this repo* mostly prove layer 2. Do not confuse layer 2 with layer 3.

| Layer | What it means | Where evidence lives |
|-------|----------------|----------------------|
| **1 — Platform implementation** | Controls built and tested in Tranc3 | Tranc3 codebase, DEFSTAN register, CI gates |
| **2 — Documentation programme** | Policies, procedures, registers, mappings authored and maintained here | This Magna Carta repository (MC-001–MC-011) |
| **3 — Validated operations** | Board approval, signed contracts, drills, observation windows, external audits | Town Hall, legal, SOC 2 collector, third parties |

**Legend:** ✅ = layer 2 artefact exists in this repo · 🎯 = layer 3 not yet demonstrated

---

## Current maturity (honest baseline)

| Area | Assessment |
|------|------------|
| Technical security controls | **Strong** — implemented in Tranc3 code with automated tests (layer 1) |
| DEFSTAN traceability | **Strong** — 53 requirements, machine-readable register, CI gate (layer 1) |
| Privacy (GDPR) | **Good** — ROPA, PIA, DSR endpoints documented; **DPA register incomplete** (unsigned processor DPAs) |
| ISO 27001 | **Draft** — SOA exists; org controls (AUP, BCP, RACI) **partially planned**, not fully operational |
| SOC 2 | **Draft** — TSC mapping and evidence schedule; **6-month observation window planned**, not running |
| Policy library | **Baseline** — core policies **authored** in this framework; not all BoardRoom-operationalised |
| Evidence & assurance (MC-010) | **Baseline** — trackers, schedules, and programmes **authored**; pen test / attestations / audits 🎯 |
| Tranc3 integration (MC-011) | **Baseline** — bridge and integration guide **authored**; staging enablement / runtime enforcement 🎯 |
| HIPAA / FCA / PECR | **Baseline** — alignment docs and register entries; live attestation / BAAs 🎯 |
| Architecture clarity | **Improved** — as-built doc reduces drift vs aspirational Tranc3 architecture docs |
| External certification | **Not yet** — targets Q1–Q2 2027 |

## Certification roadmap

```
2026 Q3  ── Quarterly DEFSTAN + Magna Carta review
2026 Q4  ── External security assessment / pen test
2027 Q1  ── SOC 2 Type II observation period complete → report
2027 Q2  ── ISO 27001:2022 certification audit
```

## Key risks (top 5)

| # | Risk | Mitigation |
|---|------|------------|
| 1 | Architecture doc inconsistency confuses auditors | Use `AS-BUILT-ARCHITECTURE.md` as canonical |
| 2 | HIPAA marketing over-claim in product copy | Tier A/B wording enforced per HIPAA-ALIGNMENT §10 |
| 3 | Unsigned supplier DPAs | Register live; countersign SUP-003–005 templates |
| 4 | BCP not exercised at scale | Baseline restore test logged; expand quarterly drills |
| 5 | AI fairness metrics unmeasured | PROC-AI-002 defined; first run Q3 2026 (ACT-004) |

See also: [RISK-REGISTER.md](compliance/RISK-REGISTER.md) and [COMPLIANCE-ACTION-TRACKER.md](compliance/COMPLIANCE-ACTION-TRACKER.md) for full risk and remediation inventory.

## Immediate actions

1. Enable Magna Carta in staging per [TRANC3-INTEGRATION-GUIDE.md](engineering/TRANC3-INTEGRATION-GUIDE.md): `MAGNA_CARTA_ENABLED=true`
2. Import `magna_carta_register.yaml` and `tranc3_register_bridge.yaml` into Tranc3 compliance checker
3. Operate per [RACI-MATRIX.md](governance/RACI-MATRIX.md) and AI Governance Committee charter
4. Schedule first quarterly Magna Carta review (2026-09-06)
5. Begin SOC 2 evidence collection per [SOC2-EVIDENCE-SCHEDULE.md](compliance/SOC2-EVIDENCE-SCHEDULE.md) and Tranc3 `scripts/soc2_evidence_collector.py`
6. Execute open actions in [COMPLIANCE-ACTION-TRACKER.md](compliance/COMPLIANCE-ACTION-TRACKER.md) (signed DPAs, ICO fee, pen test, Tranc3 HIPAA upstream PR merge)

## Document map

Start at [FRAMEWORK.md](../FRAMEWORK.md) → then branch to policies, compliance, or architecture as needed.
