# Encryption Matrix

**Version:** 1.0.0
**Date:** 2026-07-24
**Owner:** Platform Engineering / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate
**Register:** MC-014
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`encryption` section)

---

## 1. Purpose

Tracks, per encryption surface (in-transit, at-rest, secrets/signing), whether the correct protocol is actually applied — grounded in a direct code/config audit of the Tranc3 implementation rather than an assumed posture. This matrix is the encryption-specific sibling of the [Security Matrix](SECURITY-MATRIX.md) (MC-015); overlapping findings are cross-referenced, not duplicated.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §5):** do not claim encryption coverage in product copy unless the corresponding row is ✅ with evidence. Several rows below are ❌ or ⚠️ deliberately, because that is what the code audit found.

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
| Traefik `websecure` (:443) entrypoint | ⚠️ | Defined in `docker-compose.production.yml` (entrypoints at lines 69–70) with a `traefik-certs` volume mounted for Let's Encrypt, but **no `--certificatesresolvers.letsencrypt.acme.*` flag exists on the Traefik service's own `command:` block** — the `letsencrypt` certresolver referenced by ~21 service labels is never actually defined. As configured today, ACME certificate automation is not wired up |
| Core P0 services routing (infinity-auth, infinity-void, tranc3-backend, tranc3-ai, api-gateway, infinity-ws) | ❌ | All six route on the plain `web` (HTTP) entrypoint, not `websecure` — the platform's most security-sensitive services (auth, vault, AI backend) are not TLS-terminated by Traefik at all in the current compose file |
| Newer P3 workers using `entrypoints=websecure` (e.g. `fabulousa-service`, `ice-box-service`) | ❌ | Reference the `websecure` entrypoint but carry **no accompanying `tls=true` or certresolver label** — Traefik would not actually terminate TLS for these routes as configured |
| Redis connection (`REDIS_URL`) | ✅ | `.env.example` uses `rediss://` (TLS) |
| Postgres connection (`DATABASE_URL`) | ❌ | `.env.example`'s example string is a plain `postgresql://` with no `sslmode` parameter, and no `sslmode`/`connect_args` SSL enforcement exists anywhere in `src/database/` — the only `sslmode` occurrence in the repo is Mattermost's *internal* DB in `docker-compose.production.yml`, explicitly set to `sslmode=disable`, unrelated to the main app |

**Remediation priority:** the P0 routing gap (auth/vault/AI-backend on plain HTTP) and the missing Traefik ACME resolver definition are the two highest-priority findings in this entire matrix — both are one-line-per-service compose fixes once a certresolver is actually defined, not architectural rewrites.

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
| Password hashing | ⚠️ | **Two different schemes coexist**: `src/auth/passwords.py` prefers argon2id (`argon2.PasswordHasher`) with a PBKDF2-SHA256 (260,000 iterations) fallback and a legacy 100,000-iteration format; `src/auth/db_user_manager.py` uses **bcrypt** directly via a custom `_BcryptContext` class instead. Both are cryptographically sound algorithms individually, but two parallel hashing paths for the same concern is a genuine consolidation gap, not a security defect per se |
| Worker-to-worker `INTERNAL_SECRET` | ❌ | **18 workers** currently fall back to the literal string `"dev-secret"` if `INTERNAL_SECRET` is unset: `basement`, `chaos-party`, `imaginarium`, `imind`, `resonate`, `sashas-photo-studio`, `taimra`, `tateking`, `the-academy`, `the-dutchy`, `the-lab`, `the-studio`, `the-void`, `tranceflow`, `tranquility`, `vrar3d`, `warp-radio`, `warp-tunnel` (each `workers/<name>/worker.py`, confirmed via direct grep on 2026-07-24). Any deployment that forgets to set `INTERNAL_SECRET` silently runs with a publicly-known shared secret across all 18 |
| The Void's own `INTERNAL_SECRET` handling (contrast case) | ✅ | `workers/infinity-void/worker.py` explicitly **rejects** both an unset value and the specific string `"internal-dev-secret"`, raising `RuntimeError` at startup rather than silently falling back — proof the safe pattern is known and used elsewhere in the same codebase, making the 18-worker gap a consistency problem, not a knowledge gap |

**Remediation priority:** the 18-worker `dev-secret` fallback is the single highest-value fix in this matrix — it is the same one-line pattern already correctly implemented in `infinity-void/worker.py`, so fixing it is copying an existing in-repo pattern, not new design work.

---

## 6. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Traefik TLS/certresolver audit | Quarterly, or on any new service's compose entry | Manual compose review — no automated check exists yet; candidate for a Forgejo CI lint step |
| `INTERNAL_SECRET`/`dev-secret` fallback grep | Every PR touching `workers/*/worker.py` | Manual today; candidate for a `security-scan.yml` grep-based gate |
| Password-hashing consolidation decision (argon2/PBKDF2 vs bcrypt) | Next security architecture review | Owner decision required — this matrix documents the split, it does not resolve it |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 7. Cross-references

- [SECURITY-MATRIX.md](SECURITY-MATRIX.md) — auth/CORS/route-level security posture (this matrix's sibling for non-cryptographic controls)
- [SECURITY-BIBLE.md](../bibles/SECURITY-BIBLE.md) — process-level security operations
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-014 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
