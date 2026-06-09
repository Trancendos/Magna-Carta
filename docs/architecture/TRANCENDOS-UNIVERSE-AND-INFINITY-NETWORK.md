# Trancendos Universe & Infinity Network — Nomenclature

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** Platform Architecture  
**Status:** Canonical — supersedes informal “Tranc3 as platform” wording in legacy documents

---

## 1. Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│  TRANCENDOS UNIVERSE — THE FOUNDATION  (“The Master”)               │
│  Generic template for any new platform — governance core,           │
│  zero-cost mandate, DEFSTAN-style controls, deployable baseline   │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ complements / harmonises
┌───────────────────────────────▼─────────────────────────────────────┐
│  INFINITY NETWORK — MAGNA CARTA  (this repository)                  │
│  Compliance, policies, procedures, registers, readiness automation  │
│  for applications built within the Infinity Network                 │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ per application
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
   Tranc3 App            Trance-One App           T2ance App
   Framework             Framework                Framework
        │                       │                       │
   Spark App              Void App                 (future apps)
   Framework              Framework
```

---

## 2. Definitions

| Term | Meaning |
|------|---------|
| **Trancendos Universe — The Foundation** | Master generic platform template. Not a single product name — the reusable base any new platform inherits. |
| **Infinity Network** | Ecosystem of applications that share Magna Carta compliance, registers, and operational patterns. |
| **Infinity Network — Magna Carta** | This repo: documentation programme, Layer B automation, supplier/DPA registers, security testing, readiness scoring. |
| **App Framework** | One deployable product under Infinity Network (e.g. Tranc3, Trance-One, T2ance, Spark, Void). Each has its own codebase and DEFSTAN/runtime register; Magna Carta maps to them via app bridges. |

---

## 3. What changed from legacy wording

| Legacy (avoid as primary) | Use instead |
|-------------------------|-------------|
| “Tranc3 platform” (as the whole stack) | **Trancendos Universe — The Foundation** |
| “Magna Carta for Tranc3” (as if Tranc3 = universe) | **Infinity Network — Magna Carta** for all Infinity apps |
| “Tranc3 integration” (compliance master) | **Infinity App bridge** (specify app: Tranc3, Spark, …) |
| Tranc3 alone as governance scope | Name the layer: Universe / Infinity Network / App Framework |

**Tranc3 remains valid** only as an **App Framework** name — not as the master foundation.

---

## 4. Registers and bridges

| Artefact | Purpose |
|----------|---------|
| `compliance/infinity_app_frameworks_register.yaml` | Catalogue of Infinity Network app frameworks |
| `compliance/tranc3_register_bridge.yaml` | MC-### ↔ Tranc3 App DEFSTAN bridge (first app; pattern for siblings) |
| `config/magna_carta_config.json` | Runtime profile gates (per app deployment) |

Future app bridges: `infinity_app_<name>_bridge.yaml` following the Tranc3 pattern.

---

## 5. Zero-cost mandate

All **Layer B** tooling in this repository must be **£0 / $0** at point of use:

- Local Python/shell scripts (no SaaS subscription required)
- OSS scanners when optionally installed (`gitleaks`, `bandit`, `semgrep`, `pip-audit`)
- Optional **Aikido Free** tier (no credit card) — not mandatory

See [ZERO-COST-SECURITY-TOOLING.md](../compliance/ZERO-COST-SECURITY-TOOLING.md) and `compliance/zero_cost_tooling_register.yaml`.

---

## 6. Related documents

- [FRAMEWORK.md](../../FRAMEWORK.md)
- [docs/01-MAGNACARTA-FOUNDATION.md](../01-MAGNACARTA-FOUNDATION.md)
- [COMPLIANCE-READINESS-MODEL.md](../compliance/COMPLIANCE-READINESS-MODEL.md)
- [INFINITY-APP-TRANC3-INTEGRATION-GUIDE.md](../engineering/INFINITY-APP-TRANC3-INTEGRATION-GUIDE.md) (Tranc3 App Framework)
