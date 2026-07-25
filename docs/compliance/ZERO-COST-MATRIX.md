# Zero-Cost Matrix

**Version:** 1.1.0
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Platform Engineering / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate
**Register:** MC-021
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`zero_cost` section)

**2026-07-25 re-audit:** both open items from the 2026-07-24 audit are now closed — `docs/ZERO_COST_VENDOR_MATRIX.md` exists and the script's own exit code is `0` (PASS), confirmed by re-running the script directly; the script is also now wired into CI (`.forgejo/workflows/dependency-audit.yml`'s `zero-cost-audit` job) so this stops being a manual, ad-hoc check.

---

## 1. Purpose

Tracks, per Service/Solution/Application/AI, whether the platform's zero-cost architecture mandate (`CLAUDE.md` §"Zero-Cost Self-Hosted Architecture (Fortiere)") is actually being enforced in code, not just stated as policy. This is the single most code-grounded matrix in this set — Tranc3 already has a real, running enforcement mechanism (`src/zero_cost/registry.py`, `scripts/zero_cost_audit.py`), unlike Legal/Financial/Taxation where enforcement is largely aspirational pending real professional input.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §6):** do not claim zero-cost compliance in product copy unless the corresponding row is ✅ with evidence.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — zero-cost, self-hosted, or free-tier with no card required |
| ⚠️ | Free-tier with a real constraint (rate cap, soft limit, card-optional) |
| 📋 | Not yet assessed |
| ❌ | Confirmed paid dependency or gap |
| 🎯 | Requires an owner decision (funding, provider choice) this framework cannot self-certify |

---

## 3. Live audit result

Ran `python3 scripts/zero_cost_audit.py` against Tranc3 on 2026-07-24, then re-ran it directly again on 2026-07-25 to confirm the fix. This script is real and executable — not a proposed control — and validates `src/zero_cost/registry.py`'s provider registry and rotation-chain configuration.

**2026-07-24 result: ❌ FAIL (exit code 1)** — the JSON body's own `"status": "PASS"` field described rotation-chain structural validation only, not the script's overall outcome; the script's separate doc-presence check for `docs/ZERO_COST_VENDOR_MATRIX.md` failed since the file didn't exist.

**2026-07-25 re-audit result: ✅ PASS (exit code 0)** — `docs/ZERO_COST_VENDOR_MATRIX.md` was created at the script's expected path; re-running the script and checking `$?` directly (not just the JSON body) confirms a clean `0` exit.

| Metric | Value | Assessment |
|---|---|---|
| Registry version | `2026-06` | — |
| Approved self-hosted providers | 30 | ✅ |
| Approved free-tier providers | 0 | 📋 all providers are currently bucketed as self-hosted or blocked-paid; no distinct free-tier-only bucket populated |
| Blocked-paid providers | 5 (`openai`, `anthropic`, `azure-openai`, `gpt4`, `claude-api-paid`) | ✅ correctly blocked — these five are the exact paid AI APIs the zero-cost mandate exists to avoid |
| Rotation-chain structural validation | 0 errors | ✅ all 5 defined chains (`embeddings_default`, `image_default`, `stt_default`, `zero_cost_cloud`, `zero_cost_full`) pass structural validation |
| Script's own doc-presence check | ✅ `docs/ZERO_COST_VENDOR_MATRIX.md` present | **FIXED 2026-07-25** — the audit script's expected file now exists at Tranc3's repo root |
| **Overall script exit status** | **`0` (PASS)** | ✅ confirmed by direct re-run of the script on 2026-07-25 |

**Action (closed 2026-07-25):** `docs/ZERO_COST_VENDOR_MATRIX.md` was created in Tranc3 at the script's own expected path; the audit now exits 0.

---

## 4. Approved self-hosted / zero-cost providers (real registry contents)

All 30 entries from `approved_self_hosted` in `src/zero_cost/registry.py` are listed below, grouped by category (verified by counting: 3+8+2+1+3+1+5+2+4+1 = 30, matching §3's `approved_self_hosted_count`) — this is the exhaustive list, not an illustrative sample:

| Category | Providers | License / cost basis |
|---|---|---|
| AI inference | litellm, ollama, llama-cpp-python | MIT — self-hosted, zero-cost |
| AI inference (free-tier-gated) | groq, gemini, github-models, cerebras, sambanova, mistral, cohere, deepseek | Free tier when the relevant `*_API_KEY` env var is set; each carries its own real cap (e.g. GitHub Models: 50 req/day GPT-4o, 150/day gpt-4o-mini; Mistral: 500K tokens/month; Cohere: 100K tokens/month) |
| CI/CD | forgejo, woodpecker-ci | Forgejo OSS / Apache 2.0 — matches `CLAUDE.md`'s "Forgejo over GitHub Actions" principle |
| Ingress | traefik | OSS |
| Observability | prometheus, grafana, loki | OSS — matches `CLAUDE.md`'s Observability Stack |
| Secrets | vault-ce | BSL — self-hosted on The Citadel |
| Security scanning | trivy, grype, osv-scanner, semgrep, gitleaks | Apache 2.0 / MIT / OSS CLI |
| Creative | blender, penpot | GPL / MPL |
| Storage / vector DB | ipfs, qdrant, chromadb, sqlite | Self-hosted / Apache 2.0 / public domain |
| Automation | ansible-core | GPL — Citadel health probes |

This directly evidences `CLAUDE.md`'s stated architecture principles (§"Architecture principles" 1-6: SQLite over D1, in-memory rate limiting over KV, local filesystem+IPFS over R2, self-hosted FastAPI over Workers, Forgejo over GitHub Actions, Vault over Cloudflare secrets) — each principle has a real, registered provider backing it, not just a documentation claim.

---

## 5. Known tension: Cloud-Only default vs. zero-cost mandate

Per `CLAUDE.md`'s own framing, **every Location currently defaults to Cloud Only** (the ~26 live Cloudflare Workers), with Hybrid/Local-Only blocked purely on server funding — "not gated on user preference." This means:

- The **AI inference layer** (this matrix's §3-4) is genuinely zero-cost today — it runs regardless of which deployment mode a Location is in, since it's a cross-cutting service (`src/ai_gateway/`), not tied to per-Location hosting.
- The **hosting layer** (which Cloudflare Workers vs. self-hosted Python workers run a given Location) is **not** zero-cost today in the strict self-hosted sense — Cloudflare Workers' free tier has real limits (`CLAUDE.md`'s own stated reason for wanting to migrate away: "both carry rate limits that bite under prolonged/heavy use"). This is a documented, accepted gap pending funding, not a new finding — flagged here for completeness rather than treated as newly discovered.

---

## 6. Per-entity coverage note

Given the estate's scale, this matrix does not score all 43 named entities individually for zero-cost posture — the AI-inference and infrastructure-tooling layers audited in §3-5 are shared, cross-cutting concerns that apply uniformly across entities, not a per-entity variable. Entity-specific zero-cost exceptions (e.g. Sashas Photo Studio's GPU-dependent ComfyUI/Stable Diffusion backend, flagged in the DSM work referenced by `docs/services/sashas-photo-studio/`, as unrealistic on free-tier CPU hosts) are already documented in each entity's own Deployment Scope Matrix (DSM) artifact and are not repeated here.

---

## 7. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| `scripts/zero_cost_audit.py` run | Every PR (scheduled weekly too) | **Automated 2026-07-25:** wired into Tranc3's `.forgejo/workflows/dependency-audit.yml` as the `zero-cost-audit` job, with `set -o pipefail` so the script's real exit code isn't masked by the report-upload `tee` step |
| `docs/ZERO_COST_VENDOR_MATRIX.md` creation | Done | **FIXED 2026-07-25** — file created; the audit script's doc-presence check now passes |
| Cloud-Only → Hybrid/Local migration review | On funding decision | Manual, gated at `wiki-content/Architecture-CF_WORKER_MIGRATION_ROADMAP.md`'s own review points |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 8. Cross-references

- [LICENSE-COMPLIANCE-MATRIX.md](LICENSE-COMPLIANCE-MATRIX.md) — the same `pip-licenses` scan overlaps with this matrix's provider-license data; not duplicated
- [ENCRYPTION-MATRIX.md](ENCRYPTION-MATRIX.md), [SECURITY-MATRIX.md](SECURITY-MATRIX.md) — several zero-cost security tools (trivy, gitleaks, semgrep) listed here are the same tools those matrices reference
- [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md) — this matrix's §4 approved-provider list covers zero-cost/self-hosted *tooling*; it is a different lens from the Supplier register's GDPR-processor view of paid *infrastructure* vendors (Fly.io, Cloudflare, Supabase, Upstash) that the 2026-07-25 re-audit found were missing from that register entirely — see its SUP-006–009
- `CLAUDE.md` §"Zero-Cost Self-Hosted Architecture (Fortiere)" (Tranc3 repo) — the policy this matrix verifies against
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-021 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
