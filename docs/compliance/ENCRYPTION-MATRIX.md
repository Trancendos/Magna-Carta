# Encryption Matrix

**Version:** 1.2.0
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Platform Engineering / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate
**Register:** MC-014
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`encryption` section)

**2026-07-25 re-audit:** every ❌ confirmed gap from the 2026-07-24 audit below is now fixed in Tranc3 (PR #345). Rows are updated to ✅ with evidence rather than left stale — per this framework's own honesty rule, an inaccurate ❌ is as much a violation as an inaccurate ✅. The password-hashing consolidation (§5), previously the one item needing an owner decision, has since been resolved — see below.

---

## 1. Purpose

Tracks, per encryption surface (in-transit, at-rest, secrets/signing), whether the correct protocol is actually applied — grounded in a direct code/config audit of the Tranc3 implementation rather than an assumed posture. This matrix is the encryption-specific sibling of the [Security Matrix](SECURITY-MATRIX.md) (MC-015); overlapping findings are cross-referenced, not duplicated.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim encryption coverage in product copy unless the corresponding row is ✅ with evidence. Several rows below are ❌ or ⚠️ deliberately, because that is what the code audit found.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — correct protocol genuinely applied |
| ⚠️ | Applied, but with a real caveat (partial coverage, legacy fallback, unconfirmed downstream wiring) |
| 📋 | Not yet assessed |
| ❌ | Confirmed gap — no encryption where one is expected |
| 🎯 | Requires an external action (cert issuance, key-management decision) this framework cannot self-certify |

---

## 3. In-transit encryption (TLS)

| Surface | Status | Finding |
|---|---|---|
| Traefik `websecure` (:443) entrypoint | ✅ | **FIXED 2026-07-25:** `--certificatesresolvers.letsencrypt.acme.email`, `.acme.storage`, `.acme.httpchallenge`, and `.acme.httpchallenge.entrypoint=web` flags now exist on the Traefik service's `command:` block, using the already-mounted `traefik-certs` volume — the `letsencrypt` certresolver referenced by service labels is now actually defined |
| Core P0 services routing (infinity-auth, infinity-void, tranc3-backend, tranc3-ai, api-gateway, infinity-ws) | ✅ | **FIXED 2026-07-25:** all six now use `entrypoints=websecure` + `tls=true` + `tls.certresolver=letsencrypt`, plus a `Host(\`api.trancendos.com\`)` matcher (added alongside their existing `PathPrefix` rules on 2026-07-25 so Traefik's ACME resolver has a real domain to request a certificate against — a `PathPrefix`-only rule has no domain for ACME to use) |
| Newer P3 workers using `entrypoints=websecure` (e.g. `fabulousa-service`, `ice-box-service`) | ✅ | **FIXED 2026-07-25:** both now carry `tls=true` and `tls.certresolver=letsencrypt` alongside their `entrypoints=websecure` label |
| Redis connection (`REDIS_URL`) | ✅ | `.env.example` uses `rediss://` (TLS) |
| Postgres connection (`DATABASE_URL`) | ✅ | **FIXED 2026-07-25:** `.env.example`'s example string now includes `?sslmode=require`; SQLAlchemy's `create_engine()` (`src/database/schema.py`) passes the DSN straight through to psycopg2, which honors `sslmode` natively as a connection-string parameter — no code change was needed beyond the default connection string |

**Remediation priority (2026-07-24 audit):** the P0 routing gap (auth/vault/AI-backend on plain HTTP) and the missing Traefik ACME resolver definition were the two highest-priority findings in this matrix — both were one-line-per-service compose fixes once a certresolver was actually defined, and both are now closed as of the 2026-07-25 re-audit.

---

## 4. At-rest encryption

| Surface | Status | Finding |
|---|---|---|
| The Void vault (`cloudflare/infinity-void/src/index.ts`) | ✅ | Real AES-GCM + PBKDF2 (100k iterations, SHA-256), 256-bit key, random IV per secret |
| The Void, self-hosted port (`workers/infinity-void/worker.py`) | ✅ | Same scheme, using `cryptography.hazmat`'s `AESGCM`/`PBKDF2HMAC` — a genuine port, not a stub |
| Vault-service (`workers/vault-service/worker.py`) | ✅ | AES-256-GCM + PBKDF2 (100k, SHA-256) genuinely implemented; the module's own comments note it **replaced a prior insecure XOR cipher**, keeping a legacy-decrypt shim only for migrating old records — a real, documented security fix already in the codebase |
| SQLite worker databases, field-level (`src/database/encrypted_sqlite.py`) | ⚠️ | A real, working opt-in AES-GCM field encryption helper (`encrypt_field`/`decrypt_field`, `EncryptedKVStore`) exists — but this scan did not confirm it is actually applied to any sensitive column in the main Postgres/Supabase schema. Treated as an available-but-unconfirmed-adoption capability, not a platform-wide guarantee |

---

## 5. Secrets and signing

| Surface | Status | Finding |
|---|---|---|
| JWT signing algorithm | ✅ | Confirmed `HS256` (HMAC-SHA256) consistently across `src/auth/facade.py`, `src/auth/tokens.py`, and `workers/infinity-auth/config.py` |
| JWT_SECRET default handling | ✅ | No hardcoded insecure default found — `facade.py` and `infinity-auth/config.py` either fail fast or generate an ephemeral `secrets.token_hex(32)` if `JWT_SECRET` is unset, rather than falling back to a fixed string |
| Password hashing | ✅ | **FIXED 2026-07-25:** `src/auth/db_user_manager.py`'s standalone `_BcryptContext` is retired in favor of `_PasswordContext`, which hashes new passwords via `src/auth/passwords.py`'s `hash_password()` (argon2id preferred, PBKDF2-SHA256 fallback) — the same canonical implementation `infinity-auth` already used, closing the two-scheme split. Pre-existing bcrypt hashes still verify (`bcrypt.checkpw`) and are transparently upgraded to the new scheme on next successful login, in both the DB-backed and in-memory-fallback code paths — no bulk migration or forced password reset required. 5 new tests cover: new hashes aren't bcrypt, legacy bcrypt hashes still verify, a successful login upgrades the stored hash, and a failed login leaves it untouched |
| Worker-to-worker `INTERNAL_SECRET` | ✅ | **FIXED 2026-07-25:** all 18 workers (`basement`, `chaos-party`, `imaginarium`, `imind`, `resonate`, `sashas-photo-studio`, `taimra`, `tateking`, `the-academy`, `the-dutchy`, `the-lab`, `the-studio`, `the-void`, `tranceflow`, `tranquility`, `vrar3d`, `warp-radio`, `warp-tunnel`) now raise `RuntimeError` at startup if `INTERNAL_SECRET` is unset or equals `"dev-secret"` (**stripped** comparison — a bot reviewer found and got fixed a whitespace-padding bypass in the first pass, where `" dev-secret "` would have slipped through an unstripped check). Also extended to `workers/tateking/main.py`, `workers/the-lab/main.py`, `workers/imaginarium/main.py` (the real deployed entrypoints for those three, distinct from their `worker.py`) and `workers/tranceflow/config.py`, `workers/vrar3d/config.py`. The validated secret is now stored **stripped**, not raw, so incidental whitespace from secret injection (k8s/file-mounted secrets) can't silently break worker-to-worker auth even after passing validation |
| The Void's own `INTERNAL_SECRET` handling (contrast case) | ✅ | `workers/infinity-void/worker.py` explicitly **rejects** both an unset value and the specific string `"internal-dev-secret"`, raising `RuntimeError` at startup rather than silently falling back — the pattern the 18 workers above now also follow |

**Remediation priority (2026-07-24 audit):** the 18-worker `dev-secret` fallback was the single highest-value fix in this matrix — it was the same one-line pattern already correctly implemented in `infinity-void/worker.py`, and is now fixed as of 2026-07-25.

---

## 6. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Traefik TLS/certresolver audit | Every PR touching `docker-compose.production.yml` | **Automated 2026-07-25:** `scripts/compliance_drift_audit.py`'s `websecure_tls_labels` check, wired into `.forgejo/workflows/dependency-audit.yml`'s `compliance-drift-audit` job. Running it against the full compose file during this re-audit found **37 more services** beyond the originally-scoped 6 P0 + fabulousa/ice-box referencing `entrypoints=websecure` with no `tls`/`certresolver` label at all — these are now fixed too |
| Traefik Host() matcher audit | Every PR touching `docker-compose.production.yml` | **Automated 2026-07-25 (closed same day):** `scripts/compliance_drift_audit.py`'s `tls_routers_have_host_matcher` check, same CI job. All 39 routers that had `tls=true` but only a `PathPrefix` rule (the 37 above, plus fabulousa-service and ice-box-service) now carry `Host(\`<worker>.trancendos.com\`)` — subdomain-per-worker, matching the domain strategy decided for this fix |
| `INTERNAL_SECRET`/`dev-secret` fallback grep | Every PR touching `workers/*/worker.py` | **Automated 2026-07-25:** `scripts/compliance_drift_audit.py`'s `no_dev_secret_default` check, same CI job |
| Password-hashing consolidation regression check | Every PR touching `src/auth/db_user_manager.py` | **Automated 2026-07-25 (closed same day):** `scripts/compliance_drift_audit.py`'s `db_user_manager_consolidated_hashing` check, same CI job — fails if the bcrypt-only `_BcryptContext` is ever reintroduced |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Note on the 39 services fixed 2026-07-25:** the `Host()` matcher gap flagged in the previous version of this note is now closed. Every router with `tls=true` (the 37 found in the original sweep, plus `fabulousa-service` and `ice-box-service`) now carries `Host(\`<worker>.trancendos.com\`)` alongside its `PathPrefix` rule, giving Traefik's ACME resolver a real domain to request a certificate against. This does not by itself guarantee DNS records exist for each of the 39 subdomains — provisioning the actual DNS entries is an infrastructure/ops task outside this compliance pass's scope, tracked separately, not silently assumed done here.

**Next review:** 2026-10-24

---

## 7. Cross-references

- [SECURITY-MATRIX.md](SECURITY-MATRIX.md) — auth/CORS/route-level security posture (this matrix's sibling for non-cryptographic controls)
- [SECURITY-BIBLE.md](../bibles/SECURITY-BIBLE.md) — process-level security operations
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-014 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
