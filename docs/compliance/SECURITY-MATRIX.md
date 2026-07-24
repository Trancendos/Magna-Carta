# Security Matrix

**Version:** 1.0.0
**Date:** 2026-07-24
**Owner:** Platform Engineering / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate
**Register:** MC-015
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`security` section)

---

## 1. Purpose

Tracks, per Service/Solution/Application, whether the correct **non-cryptographic** protections are actually in place — authentication/authorization coverage, CORS configuration, and route-level access control — grounded in a direct code audit rather than an assumed posture. Encryption-specific findings (TLS, at-rest, secrets) live in the sibling [Encryption Matrix](ENCRYPTION-MATRIX.md) (MC-014) and are not repeated here.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §5):** do not claim security coverage in product copy unless the corresponding row is ✅ with evidence. Several rows below are deliberately ❌, because that is what the code audit found — many of these gaps were already flagged individually in the per-entity doc-pack series (`docs/services/*/README.md` in Tranc3) but had not been consolidated into one cross-entity view until this matrix.

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
| Standalone workers with `X-Internal-Secret` enforced on all non-`/health` routes (The Studio, I-Mind, Tranquility, tAimra, VRAR3D, Resonate, Sashas Photo Studio) | ⚠️ | Auth **is** enforced — this corrects an earlier assumption in some per-entity doc-packs that these had none — but the shared secret defaults to the vulnerable `"dev-secret"` fallback tracked in the [Encryption Matrix](ENCRYPTION-MATRIX.md) §5 if `INTERNAL_SECRET` is unset, so the control's real strength depends on that separate fix |
| `workers/fabulousa-service/worker.py` | ❌ | `GET /fabulousa/status`, `GET /fabulousa/projects`, `GET /fabulousa/assets` have **no** auth dependency at all — only the two POST routes are protected |
| `workers/ice-box-service/worker.py` | ❌ | `GET /quarantine`, `GET /quarantine/{id}`, `GET /stats` have **no** auth — only `POST /scan` and `POST /quarantine/{id}/release` are protected |
| In-repo routers mounted in `api.py`: `src/imind/routes.py`, `src/vrar3d/routes.py`, `src/resonate/routes.py`, `src/artifactory/routes.py`, `src/library/routes.py`, `src/studio/routes.py` | ❌ | **Zero** auth checks of any kind — no `Depends`, no `require_permission`, no `get_current_user`/`request.state.user` reference. The platform's global `RBACMiddleware` (`src/security/middleware.py`) only *populates* `request.state.user` from a Bearer token when present; it explicitly does not block unauthenticated requests, by design, so these six routers are genuinely open — including `DELETE /artifactory/artifacts/{id}` and `DELETE /library/articles/{id}`, both destructive operations reachable with no credential at all |
| `src/tranquility/routes.py`, `src/taimra/routes.py` | ✅ | Both **do** enforce `Depends(get_current_user)` on all sensitive (non-`/status`) routes — this corrects an earlier per-entity doc-pack finding that assumed no auth existed for these two |
| `workers/library-service/router.py`, `workers/files-service/worker.py` (DocUtari) | ✅ | Both apply `Depends(_auth)` to their data routes |

**Remediation priority:** the six unauthenticated in-repo routers (`imind`, `vrar3d`, `resonate`, `artifactory`, `library`, `studio` — the `src/` variants, distinct from any better-protected standalone-worker counterpart of the same name) are the highest-priority finding in this matrix, since two of the six expose unauthenticated delete operations.

---

## 4. CORS configuration

| Surface | Status | Finding |
|---|---|---|
| Main monolith (`api.py`) | ✅ | `CORSMiddleware(allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","))` — configurable via environment, defaults to localhost only, not a wildcard |
| Standalone workers | ❌ | **65 files** across `workers/*/worker.py` and `workers/*/main.py` use `allow_origins=["*"]` (wildcard), confirmed via direct grep on 2026-07-24 — including The Studio, I-Mind, Tranquility, the Library service, and the DocUtari files-service. Combined with the auth gaps in §3, wildcard CORS on an unauthenticated route (e.g. the six `src/` routers above are reached via `api.py`, not directly by these workers, so this specific combination does not apply to them — but several of the 65 wildcard-CORS *workers* also carry only a `dev-secret`-level auth per the Encryption Matrix, which is the more consequential compounding risk) |

---

## 5. Cross-entity risk summary (not a full per-entity table)

Given the estate's scale (43 named entities, ~90 standalone workers), this matrix does not attempt to score every entity individually — most carry the platform-wide baseline (RBACMiddleware populates but does not enforce; CORS commonly wildcard on standalone workers) with no distinct additional finding. §3 and §4 list only the entities where a direct code audit surfaced something specific (a genuine gap or a correction to an earlier assumption). Any entity not named above should be assumed to carry the platform-wide baseline posture, not a verified-clean status — this is a scoping choice made explicit here rather than implied.

---

## 6. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Full auth-coverage audit (all ~90 standalone workers + `src/*/routes.py` routers) | Not yet scheduled | This matrix's own audit covered only the 12 named workers investigated in the per-entity doc-pack series plus their `src/` counterparts — a full sweep of the remaining workers is a genuine open item, not yet resourced |
| CORS wildcard remediation | Owner decision required | Tightening 65 files' CORS policy is a real, non-trivial engineering task — tracked here as a finding, not fixed by this documentation pass |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 7. Cross-references

- [ENCRYPTION-MATRIX.md](ENCRYPTION-MATRIX.md) — TLS/at-rest/secrets posture (this matrix's sibling for cryptographic controls)
- [SECURITY-BIBLE.md](../bibles/SECURITY-BIBLE.md) — process-level security operations, incident severity model
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-015 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
