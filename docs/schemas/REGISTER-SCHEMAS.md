# Register Schemas

**Version:** 1.2.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead  
**Purpose:** Field definitions for machine-readable YAML registers and human register tables.

---

## 1. YAML register files

| File | Schema version | Owner |
|------|----------------|-------|
| `compliance/compliance_action_tracker.yaml` | 1.0.0 | ISMS Lead |
| `compliance/magna_carta_register.yaml` | 1.0.0 | ISMS Lead |
| `compliance/tranc3_register_bridge.yaml` | 1.0.0 | Platform Engineering |
| `compliance/supplier_dpa_register.yaml` | 1.0.0 | DPO |
| `compliance/risk_register.yaml` | 1.0.0 | ISMS Lead |
| `compliance/policy_attestation_register.yaml` | 1.0.0 | HR / ISMS |
| `compliance/maintenance_monitor.yaml` | 1.0.0 | ISMS Lead |
| `compliance/health_check_history.yaml` | 1.0.0 | ISMS Lead |
| `compliance/frameworks_register.yaml` | 1.0.0 | ISMS Lead |

---

## 2. Common meta block

```yaml
meta:
  register_version: "semver"
  owner: "role"
  last_updated: "YYYY-MM-DD"
  review_cycle: "quarterly | annual | ..."
  procedure: "docs/procedures/..."  # optional
```

---

## 3. compliance_action_tracker.yaml

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `action_id` | string | yes | `ACT-###` |
| `title` | string | yes | Short description |
| `owner` | string | yes | Role or named owner |
| `due_date` | date | yes | ISO date |
| `status` | enum | yes | Open, In progress, Blocked, Closed |
| `priority` | enum | yes | P0–P3 |
| `validation_type` | enum | yes | programme, external |
| `source` | string | no | Traceability |
| `evidence_target` | string | no | Definition of done |

---

## 4. risk_register.yaml

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `risk_id` | string | yes | `RISK-###` |
| `title` | string | yes | Risk statement |
| `likelihood` | int | yes | 1–5 |
| `impact` | int | yes | 1–5 |
| `owner` | string | yes | Accountable role |
| `treatment` | enum | yes | Accept, Mitigate, Transfer, Avoid |
| `status` | enum | yes | Open, Mitigated, Closed |
| `review_date` | date | yes | Next review |

---

## 5. supplier_dpa_register.yaml

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `supplier_id` | string | yes | `SUP-###` |
| `name` | string | yes | Legal entity |
| `purpose` | string | yes | Processing purpose |
| `data_categories` | list | yes | PII types |
| `dpa_status` | enum | yes | Unsigned, Draft, Signed, N/A |
| `baa_status` | enum | no | For HIPAA subprocessors |
| `review_date` | date | yes | Annual review |

---

## 6. magna_carta_register.yaml

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mc_id` | string | yes | `MC-###` |
| `title` | string | yes | Programme item |
| `status` | enum | yes | Draft, Active, Deprecated |
| `owner` | string | yes | Role |
| `evidence_path` | string | no | Doc link |

---

## 7. frameworks_register.yaml

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `framework_id` | string | yes | `FW-###` stable identifier |
| `name` | string | yes | Framework or regulation name |
| `category` | enum | yes | iso_ms, soc_assurance, pci, nist, us_government, international_assurance, eu_industry, global_privacy |
| `applicability` | enum | yes | applicable, conditional, reference, awareness, not_applicable |
| `programme_status` | enum | yes | programme, operational, partial, readiness, not_applicable |
| `certification_target` | string | no | Target date or note (not a certification claim) |
| `readiness_doc` | string | no | Relative path to mapping or readiness doc |

Human-readable master: [STANDARDS-AND-FRAMEWORKS-REGISTER.md](../compliance/STANDARDS-AND-FRAMEWORKS-REGISTER.md)

---

## 8. maintenance_monitor.yaml

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `check_id` | string | yes | `MON-###` |
| `type` | enum | yes | file_exists, review_stale, action_overdue, index_count |
| `target` | string | yes | Path or pattern |
| `max_age_days` | int | no | Staleness threshold |
| `severity` | enum | yes | error, warning, info |

---

## 9. Human register tables (markdown)

Standard columns used across Magna Carta registers:

| Column | Use |
|--------|-----|
| ID | Stable identifier |
| Status | ✅ / ⚠️ / 📋 / ❌ per coverage register rules |
| Owner | Role from RACI |
| Next review | ISO date |
| Related doc | Relative link |

Obligation extended schema: [OBLIGATIONS-REGISTER.md](../compliance/OBLIGATIONS-REGISTER.md) §3

---

## 10. Validation

Run schema-adjacent checks:

```bash
python3 scripts/compliance_health_check.py --report
./scripts/weekly_compliance_health.sh   # weekly cadence + append-only log
```

### JSON Schema files

Machine-readable schemas (Draft 2020-12) live in `compliance/schemas/`:

| File | Register |
|------|----------|
| `compliance_action_tracker.schema.json` | `compliance/compliance_action_tracker.yaml` |
| `health_check_history.schema.json` | `compliance/health_check_history.yaml` |
| `risk_register.schema.json` | `compliance/risk_register.yaml` |
| `supplier_dpa_register.schema.json` | `compliance/supplier_dpa_register.yaml` |
| `magna_carta_register.schema.json` | `compliance/magna_carta_register.yaml` |
| `tranc3_register_bridge.schema.json` | `compliance/tranc3_register_bridge.yaml` |
| `policy_attestation_register.schema.json` | `compliance/policy_attestation_register.yaml` |
| `maintenance_monitor.schema.json` | `compliance/maintenance_monitor.yaml` |
| `frameworks_register.schema.json` | `compliance/frameworks_register.yaml` |

`compliance_health_check.py` performs lightweight structural validation (MON-009) for all nine register/schema pairs without requiring the `jsonschema` package. Procedure coverage (MON-010) ensures every `PROC-*.md` has matching cookbook and hymn sheet.

**Next review:** 2026-09-06
