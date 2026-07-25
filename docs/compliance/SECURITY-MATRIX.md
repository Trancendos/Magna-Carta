# Security Matrix

**Version:** 1.1.0
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Platform Engineering / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate
**Register:** MC-015
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`security` section)

**2026-07-25 re-audit:** every ❌ confirmed gap from the 2026-07-24 audit below is now fixed in Tranc3 (PR #345), with a `no_wildcard_cors` CI check (`scripts/compliance_drift_audit.py`) guarding the CORS finding against regression going forward.

---

## 1. Purpose

Tracks, per Service/Solution/Application, whether the correct **non-cryptographic** protections are actually in place — authentication/authorization coverage, CORS configuration, and route-level access control — grounded in a direct code audit rather than an assumed posture. Encryption-specific findings (TLS, at-rest, secrets) live in the sibling [Encryption Matrix](ENCRYPTION-MATRIX.md) (MC-014) and are not repeated here.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim security coverage in product copy unless the corresponding row is ✅ with evidence. Several rows below are deliberately ❌, because that is what the code audit found — many of these gaps were already flagged individually in the per-entity doc-pack series (`docs/services/*/README.md` in Tranc3) but had not been consolidated into one cross-entity view until this matrix.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — auth/access control genuinely enforced |
| ⚠️ | Partial — some routes protected, others not, or protected by a weak/shared-default secret |
| 📋 | Not yet assessed |
| ❌ | Confirmed gap — no auth where sensitive data or write access is exposed |
| 🎯 | Requires an owner/architecture decision this framework cannot self-certify |

---

## 3. Authentication and authorization coverage

Two distinct implementation shapes exist per named entity — a standalone `workers/<name>/worker.py` process, and/or an in-repo router under `src/<name>/routes.py` mounted into the monolith's `api.py`. Coverage differs between the two for the same entity name, so both are tracked separately rather than assumed identical.

| Entity / Surface | Status | Finding |
|---|---|---|
| Standalone workers with `X-Internal-Secret` enforced on all non-`/health` routes (The Studio, I-Mind, Tranquility, tAimra, VRAR3D, Resonate, Sashas Photo Studio) | ✅ | **FIXED 2026-07-25:** auth was already enforced; the shared secret's `"dev-secret"` fallback (the caveat that kept this row at ⚠️) is now fixed too, per the [Encryption Matrix](ENCRYPTION-MATRIX.md) §5 — the secret is now a real, required, unguessable value |
| `workers/fabulousa-service/worker.py` | ✅ | **FIXED 2026-07-25:** `GET /fabulousa/projects` and `GET /fabulousa/assets` now require `_require_internal_auth`; `GET /fabulousa/status` remains intentionally public, matching the platform's `/health`-style convention |
| `workers/ice-box-service/worker.py` | ✅ | **FIXED 2026-07-25:** `GET /quarantine` and `GET /quarantine/{id}` now require `_require_internal_auth`; `GET /stats` remains intentionally public as a metrics-style endpoint |
| In-repo routers mounted in `api.py`: `src/imind/routes.py`, `src/vrar3d/routes.py`, `src/resonate/routes.py`, `src/artifactory/routes.py`, `src/library/routes.py`, `src/studio/routes.py` | ✅ | **FIXED 2026-07-25:** all six now require `Depends(get_current_user)` on every non-status route. `artifactory`'s and `library`'s delete endpoints require the same auth, and `library`'s delete additionally requires the caller pass the same read-clearance check as a GET (an owner/admin-only RESTRICTED article can no longer be deleted by a non-owner who merely knows its ID). `resonate` and `vrar3d` enforce self-or-admin ownership on user-scoped actions. 43 tests in `tests/test_shared_resource_routers_auth.py` cover public-status-stays-public, unauthenticated-rejected, authenticated-allowed, and ownership-denied/admin-override for all six |
| `src/tranquility/routes.py`, `src/taimra/routes.py` | ✅ | Both **do** enforce `Depends(get_current_user)` on all sensitive (non-`/status`) routes — this corrects an earlier per-entity doc-pack finding that assumed no auth existed for these two |
| `workers/library-service/router.py`, `workers/files-service/worker.py` (DocUtari) | ✅ | Both apply `Depends(_auth)` to their data routes |
| `workers/the-lab/main.py` `GET /lab/models`, `GET /workspaces`; `workers/tateking/main.py` `GET /projects` | ✅ | **FIXED 2026-07-25:** found on re-audit that these three GET routes were left open by the initial auth pass on those two workers' real deployed entrypoints (`main.py`, distinct from `worker.py`) — `/lab/models` in particular triggers a real backend request, and `/projects` enumerated in-memory job metadata. All three now require `_require_internal_auth` |

**Remediation priority (2026-07-24 audit, closed 2026-07-25):** the six unauthenticated in-repo routers were the highest-priority finding in this matrix, since two of the six exposed unauthenticated delete operations. All six are now fixed, and the re-audit additionally caught and closed three GET routes on `the-lab`/`tateking`'s real `main.py` entrypoints that the original pass had missed (see the last row of §3's table above).

---

## 4. CORS configuration

| Surface | Status | Finding |
|---|---|---|
| Main monolith (`api.py`) | ✅ | `CORSMiddleware(allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","))` — configurable via environment, defaults to localhost only, not a wildcard |
| Standalone workers | ✅ | **FIXED 2026-07-25 (commit `3e428d35`):** all 68 files flagged in the 2026-07-24 audit no longer pass a literal `allow_origins=["*"]`; each now reads a trimmed, empty-filtered allowlist from `CORS_ORIGINS`/environment the same way `api.py` does. The code-generator template (`workers/_generate_workers.py`) carried the same wildcard as its own default and was fixed separately (`a7ae3e00`, plus a follow-up `import os` NameError fix in `0870bc71`) so regenerating a worker doesn't reintroduce it. `dimensional-nexus-service`'s wildcard-plus-credentials combination (the most consequential of the 68, since it also carried `allow_credentials=True`) now explicitly rejects a wildcard value at startup instead of letting Starlette crash on it. Verified via direct grep (zero remaining matches) and `scripts/compliance_drift_audit.py`'s `no_wildcard_cors` check, which is wired into CI |

---

## 5. Cross-entity risk summary (not a full per-entity table)

Given the estate's scale (43 named entities, ~90 standalone workers), this matrix does not attempt to score every entity individually — most carry the platform-wide baseline (RBACMiddleware populates but does not enforce) with no distinct additional finding. The CORS wildcard that used to be part of that baseline is now closed platform-wide (§4). §3 and §4 list only the entities where a direct code audit surfaced something specific (a genuine gap or a correction to an earlier assumption). Any entity not named above should be assumed to carry the platform-wide baseline posture, not a verified-clean status — this is a scoping choice made explicit here rather than implied.

---

## 6. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Full auth-coverage audit (all ~90 standalone workers + `src/*/routes.py` routers) | Not yet scheduled | This matrix's own audit covered only the named workers investigated in the per-entity doc-pack series plus their `src/` counterparts, now including the `main.py` entrypoints found on 2026-07-25 re-audit — a full sweep of the remaining ~78 unaudited workers is a genuine open item, not yet resourced |
| `dev-secret`/`INTERNAL_SECRET` fallback grep | Every PR touching `workers/*/worker.py` or `workers/*/main.py` | **Automated 2026-07-25:** `scripts/compliance_drift_audit.py`'s `no_dev_secret_default` check, wired into `.forgejo/workflows/dependency-audit.yml`'s `compliance-drift-audit` job |
| CORS wildcard regression check | Every PR touching `workers/*/worker.py` or `workers/*/main.py` | **Automated 2026-07-25:** `scripts/compliance_drift_audit.py`'s `no_wildcard_cors` check, same CI job |
| Owner decision: should health/status-style GET endpoints move behind auth too | Next security architecture review | This matrix documents the platform's current convention (status endpoints stay public); it does not mandate changing it |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 7. Cross-references

- [ENCRYPTION-MATRIX.md](ENCRYPTION-MATRIX.md) — TLS/at-rest/secrets posture (this matrix's sibling for cryptographic controls)
- [SECURITY-BIBLE.md](../bibles/SECURITY-BIBLE.md) — process-level security operations, incident severity model
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-015 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
