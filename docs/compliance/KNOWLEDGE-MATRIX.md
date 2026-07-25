# Knowledge Matrix

**Version:** 1.1.0
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Platform Engineering / ISMS Lead / DPO
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate that stores, shares, or federates knowledge/data
**Register:** MC-018
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`knowledge` section)

**2026-07-25 re-audit:** the central finding (§3) — The Library had no classification/retention model — is now fixed in Tranc3 (`src/library/knowledge_base.py`'s `Article` dataclass, `fad3486e`). The Observatory → Library dead-ingest path (§5) was **not** touched this session and remains a genuinely open gap.

---

## 1. Purpose

Tracks, per Service/Solution/Application/AI, whether federated knowledge sharing across the platform actually follows a data classification, sensitivity, and retention framework — building on [DATA-MANAGEMENT-BIBLE.md](../bibles/DATA-MANAGEMENT-BIBLE.md) and [PRIVACY-BIBLE.md](../bibles/PRIVACY-BIBLE.md), both process-level pointer documents, with real code-grounded findings.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim knowledge-governance compliance in product copy unless the corresponding row is ✅ with evidence — this cuts both ways, since an inaccurate ❌ left stale after a fix is equally dishonest. §3's central finding is now closed; §5's Observatory→Library gap remains genuinely open.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — classification/sensitivity/retention genuinely enforced |
| ⚠️ | Partial — mechanism exists elsewhere but not applied here |
| 📋 | Not yet assessed |
| ❌ | Confirmed gap |
| 🎯 | Requires an owner/architecture decision |

---

## 3. Central finding: The Library's classification, sensitivity, and retention model

The Library (Zimik, Tranc3's canonical knowledge-base/wiki entity, `src/library/knowledge_base.py`) is the platform's own designated federated-knowledge hub per `CLAUDE.md`'s service table. The 2026-07-24 audit found it was a bare in-memory CRUD layer with no classification, sensitivity, or retention field — `status` (draft/published/archived) is a workflow state, not a sensitivity label.

| Concern | Status | Finding |
|---|---|---|
| Data classification (public/internal/confidential/restricted) applied to Library content | ✅ | **FIXED 2026-07-25:** `Article.classification: DataClassification`, reusing the same enum from `src/nanoservices/daas_stream/daas_stream.py` (§4) rather than inventing a parallel one. `src/library/routes.py` enforces it: `_can_read()` gates RESTRICTED/TOP_SECRET articles to the author or an admin, applied consistently across list/search/get/delete |
| Sensitivity tagging on knowledge articles | ✅ | **FIXED 2026-07-25:** the classification field above doubles as the sensitivity label; `create_article` accepts a `classification` param (default `INTERNAL`) and `get_stats()` reports an article-count breakdown `by_classification` |
| Retention schedule applied to Library content | ✅ | **FIXED 2026-07-25:** `Article.retention_days` (optional; `None` = retain forever) + `retention_expired()` + `Library.apply_retention()`, mirroring the already-proven pattern in `src/artifactory/registry.py` |

**Closed as of 2026-07-25** — The Library now reuses the DaaS Stream nanoservice's `DataClassification` enum rather than the parallel scheme this matrix's original audit suggested inventing (§4's "Action" note below is accordingly resolved, not just proposed).

---

## 4. Real classification/retention mechanisms that exist elsewhere (not yet applied to The Library)

| Mechanism | Location | Status |
|---|---|---|
| `DataClassification` enum (public/internal/confidential/restricted/top_secret) with real `retention_ms` field and jurisdiction/OPA policy enforcement | `src/nanoservices/daas_stream/daas_stream.py` (Tranc3) | ✅ Real and working — but scoped to the DaaS Stream nanoservice, not connected to The Library |
| `data_classification` string column | `src/cmdb/models.py` (Tranc3) | ⚠️ Exists on CMDB service records (infrastructure metadata), not knowledge content |
| `apply_retention()` | `src/artifactory/registry.py` (Tranc3) | ✅ Real, working retention pruning — scoped to The Artifactory, not The Library |
| Retention pruning by schedule | `src/backup/engine.py` (Tranc3) | ✅ Real — scoped to backups, not knowledge content |
| "Configurable retention pull from audit-service" | `workers/basement/worker.py` (Tranc3) | ✅ Real — scoped to The Basement's archived-info store |

**Action (closed 2026-07-25):** The Library now adopts the same `DataClassification` pattern already proven in the DaaS Stream nanoservice, rather than a new one — see §3.

---

## 5. Federated knowledge sharing (the user's specific ask)

"Federated Knowledge is Shared" — assessed against what actually moves knowledge between entities:

| Path | Status | Finding |
|---|---|---|
| The Dutchy → The Library | ✅ | Confirmed real, working integration (per the Tranc3 doc-pack series): `generate_platform_health_report()`/`generate_security_report()` genuinely call `Library.create()` to publish |
| The Observatory → The Library | ❌ | Confirmed dead code in the same doc-pack series: `ingest()` is never called, and its target `/kb/ingest` endpoint doesn't exist on either implementation |
| RAG/FAISS semantic search over Library content | ❌ | Claimed in source comments but not implemented in `src/library/*`, per the same prior audit |

**This matrix does not re-audit these findings** — they were already discovered and documented during Tranc3's per-entity doc-pack series; cross-referenced here because they're directly relevant to "is knowledge actually federated."

---

## 6. Privacy/data-management process baseline

`docs/bibles/DATA-MANAGEMENT-BIBLE.md` and `docs/bibles/PRIVACY-BIBLE.md` are real documents but, like `IP-BIBLE.md` before this matrix set, are process-level pointers (procedure/cookbook/checklist references) with the same honest self-declared gaps: no named process owner in production HRIS, no vendor/tooling integration, no external attestation. This matrix does not duplicate that content — see the bibles directly for the process layer.

---

## 7. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Classification/retention regression check for The Library | Every PR touching `src/library/knowledge_base.py` | **Automated 2026-07-25:** `scripts/compliance_drift_audit.py`'s `library_classification` check, wired into `.forgejo/workflows/dependency-audit.yml`'s `compliance-drift-audit` job |
| Fix The Observatory → Library dead ingest path | Not yet scheduled | 🎯 Real engineering task, already flagged in the Library doc-pack — genuinely still open, not touched by the 2026-07-25 re-audit |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 8. Cross-references

- [DATA-MANAGEMENT-BIBLE.md](../bibles/DATA-MANAGEMENT-BIBLE.md), [PRIVACY-BIBLE.md](../bibles/PRIVACY-BIBLE.md) — process-level data governance
- `docs/services/the-library/` (Tranc3) — The Library's own doc-pack, source of the federation findings in §5
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-018 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
