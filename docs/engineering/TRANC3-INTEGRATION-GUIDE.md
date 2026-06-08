# Tranc3 Integration Guide — Magna Carta Runtime

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Platform Engineering  
**Register:** MC-011  
**Action:** ACT-009

---

## 1. Purpose

Step-by-step guide to enable Magna Carta runtime rules in Tranc3 staging and wire the compliance register bridge. Documentation lives in Magna Carta; enforcement lives in Tranc3.

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Configuration and guide exist |
| 🎯 **External validation** | Staging deployment and rule implementation pending |

---

## 2. Prerequisites

- Tranc3 checkout (v2.1.0-rc1 or later)
- Magna Carta repo cloned adjacent or submodule-mounted
- Staging environment with audit logging enabled

---

## 3. Environment variables

Add to `.env.staging` (or equivalent):

```bash
MAGNA_CARTA_ENABLED=true
MAGNA_CARTA_CONFIG_PATH=/path/to/magna-carta/config/magna_carta_config.json
# Optional — when checker supports dual-register import:
MAGNA_CARTA_REGISTER_PATH=/path/to/magna-carta/compliance/magna_carta_register.yaml
```

**Default behaviour:** When `MAGNA_CARTA_ENABLED=false`, `magna_carta.py` returns `framework: inactive` and all checks pass (advisory only).

---

## 4. Configuration files

| File | Role |
|------|------|
| `config/magna_carta_config.json` | Nine runtime rules (MC-RULE-001–009) |
| `compliance/magna_carta_register.yaml` | MC-001–MC-011 programme evidence |
| `compliance/tranc3_register_bridge.yaml` | MC ↔ REQ mapping |

Copy or mount from Magna Carta — do not fork rule definitions in Tranc3.

---

## 5. Request-boundary hook

`src/compliance/magna_carta.py` exposes:

```python
from src.compliance.magna_carta import magna_carta

result = magna_carta.check_request(request_data)
# {"compliant": bool, "violations": [...], "framework": "magna_carta_v1"}
```

### 5.1 Current state (2026-06-07)

- Config load: ✅ implemented
- Rule iteration: ✅ implemented
- `_apply_rule` logic: 🎯 placeholder (all rules pass)
- Audit logging: ✅ `audit_log()` when enabled

### 5.2 Implementation checklist (ACT-009)

1. Wire `check_request()` into FastAPI middleware or `api.py` request pipeline for protected routes
2. Implement rule types per `magna_carta_config.json`:
   - `authentication` — JWT + Zero Trust
   - `privacy` — blocked fields, sanitisation
   - `rate_limit` — tier enforcement
   - `ai_governance` — model card / risk tier
   - `zero_cost` — paid API dependency block
   - `governance` — CAB reference for material changes
   - `transparency` — consent / purpose metadata
   - `health_data` — HIPAA profile gate
3. Set `enforcement.fail_closed_on_violation` to `true` only after staging burn-in
4. Capture `MAGNA_CARTA_AUDIT` log samples for SOC 2 evidence (EV-SOC-003)

---

## 6. Compliance checker integration

Tranc3 `src/compliance/checker.py` currently loads `compliance/register.yaml` only.

**Recommended approach (dual register):**

1. Load DEFSTAN register as today
2. Optionally load `magna_carta_register.yaml` via `MAGNA_CARTA_REGISTER_PATH`
3. Merge MC rows into report under area `MC`
4. Use [tranc3_register_bridge.yaml](../../compliance/tranc3_register_bridge.yaml) for REQ cross-reference

**CI gate:** Keep DEFSTAN ≥70% threshold; MC rows report separately until MC evidence paths are Tranc3-relative or symlinked.

---

## 7. Verification

### 7.1 Staging smoke test

```bash
export MAGNA_CARTA_ENABLED=true
export MAGNA_CARTA_CONFIG_PATH=../magna-carta/config/magna_carta_config.json
python -c "from src.compliance.magna_carta import magna_carta; print(magna_carta.check_request({}))"
# Expect: framework magna_carta_v1, rules_checked=9
```

### 7.2 Compliance report

```bash
python -m src.compliance.checker --report
```

### 7.3 HIPAA copy audit (ACT-006)

```bash
rg -i "hipaa compliant|strict hipaa" src/ docs/
# Expected: no Tier B/C marketing claims in product copy
```

Local verification (2026-06-07): ✅ Tier A wording present in all five remediation files.

---

## 8. Related documents

- [TRANC3-REGISTER-BRIDGE.md](../compliance/TRANC3-REGISTER-BRIDGE.md)
- [TRANC3-HIPAA-COPY-REMEDIATION.md](TRANC3-HIPAA-COPY-REMEDIATION.md)
- [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md) — ACT-006, ACT-009
- [FRAMEWORK.md](../../FRAMEWORK.md) §8
