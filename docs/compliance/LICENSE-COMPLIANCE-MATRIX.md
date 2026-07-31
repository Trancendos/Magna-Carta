# License Compliance Matrix

**Version:** 1.1.0
**Date:** 2026-07-24 (re-audited 2026-07-25)
**Owner:** Platform Engineering / ISMS Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate (Tranc3 implementation + Magna Carta foundation)
**Register:** MC-012
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`license_compliance` section)

**2026-07-25 re-audit:** §3/§4's 4 UNKNOWN packages are now resolved with evidence (`cuda-toolkit`/`cuda-bindings`/`cuda-pathfinder` are confirmed transitive `torch` dependencies covered by the existing NVIDIA-proprietary bucket; `rustworkx` is a transitive `qiskit` dependency, Apache-2.0; `pygad` is BSD-3-Clause; `sentencepiece` is Apache-2.0, **correcting** this matrix's own prior draft note in §4 which had misstated it as MIT). §8's CI action item is also closed: `pip-licenses` is now wired into Tranc3's `.forgejo/workflows/dependency-audit.yml` `python-audit` job (a `pip-licenses --format=markdown` report plus a `--fail-on` gate for GPL/AGPL family strings).

---

## 1. Purpose

Tracks the open-source, third-party, and AI-model licenses this estate depends on, so that:

- No dependency or model creates unintended copyleft/redistribution obligations on proprietary code.
- No dependency license conflicts with the platform's zero-cost, self-hosted mandate ([FRAMEWORK.md](../../FRAMEWORK.md) §3.2).
- Emerging AI-specific legislation touching model licensing, training-data provenance, and output ownership is monitored on a recurring cadence, not assessed once and forgotten.

This is a distinct concern from [REGULATION-MATRIX.md](REGULATION-MATRIX.md) (regulatory/legal compliance) and [IP-BIBLE.md](../bibles/IP-BIBLE.md) (this estate's *own* IP ownership) — this matrix is about the licenses *this estate consumes* from others.

**Honesty note, per this framework's own rule (REGULATION-MATRIX.md §6):** do not claim license clearance in product copy unless the corresponding row below is ✅ with evidence.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified, no obligation conflict |
| ⚠️ | Verified, obligation exists but is satisfied (e.g. attribution present) |
| 📋 | Flagged for manual/legal review — not yet assessed |
| ❌ | Confirmed conflict — remediation required |
| 🎯 | Re-scan or review target date |

---

## 3. Dependency license summary (Tranc3, `requirements.txt`)

Scanned with `pip-licenses --format=json --with-urls` against the installed environment on
2026-07-24. 190 packages resolved; exact counts below (not rounded) — see
[compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml)'s
`license_compliance.license_family_summary` for the machine-readable equivalent, and the archived
scan JSON referenced in §7 for full per-package detail.

| License family | Count | Compliance posture |
|---|---|---|
| Permissive (MIT, BSD, Apache-2.0, ISC, PSF, Unlicense) | 158 | ✅ No redistribution obligation beyond attribution/notice — safe for a closed or open estate |
| Weak copyleft (LGPL, LGPLv2+, MPL 2.0) | 11 | ⚠️ Safe when used as an unmodified library dependency (dynamic linking equivalent for Python imports); becomes ❌ only if this estate modifies and redistributes the library itself, which it does not |
| Strong copyleft (GPL) | 1 (`python-apt`) | 📋 Ubuntu system package pulled in transitively by the sandbox/OS image, not a Tranc3-authored or Tranc3-redistributed dependency — confirm it is not bundled into any shipped container image |
| Proprietary (NVIDIA CUDA/cuDNN/NCCL bindings) | 16 (+3 folded in below) | ✅ Redistributed under NVIDIA's standard runtime-library redistribution terms as transitive `torch` GPU dependencies; these are hardware driver bindings invoked at runtime, not source code this estate modifies or redistributes standalone |
| Unknown / unclassified | 0 (was 4: `cuda-toolkit`, `pygad`, `rustworkx`, `sentencepiece`) | ✅ **Resolved 2026-07-25** — all 4 manually classified, see §4 |

Full per-package detail: `pip-licenses --format=json` output, archived per-scan in evidence (see §7).

---

## 4. Flagged packages requiring review

| Package | Version | License | Risk | Assessment |
|---|---|---|---|---|
| `python-apt` | 2.7.7+ubuntu5.2 | GNU GPL | 📋 Low (see below) | Ubuntu OS package manager binding; not imported by Tranc3 application code, not present in production container images (Docker base images use `python:slim`, not full Ubuntu) — verify per §6 action |
| `launchpadlib`, `lazr.restfulclient`, `lazr.uri`, `wadllib` | various | LGPL | 📋 Low | Ubuntu/Launchpad tooling transitively present in this dev sandbox; not a runtime dependency of any Tranc3 service — confirm absent from `requirements.txt` (it is) |
| `psycopg2-binary` | 2.9.12 | LGPL | ⚠️ Accepted | Used unmodified as the PostgreSQL driver (Supabase `DATABASE_URL`); LGPL permits this without redistribution obligation |
| `deap`, `moocore` | 1.4.4 / 0.3.2 | LGPL | 📋 Pending | Genetic-algorithm libraries — confirm which service (if any) actually imports these vs. transitive sandbox presence |
| `sentencepiece` | 0.2.1 | ✅ Apache License 2.0 | ✅ Resolved 2026-07-25 | Explicitly pinned in `requirements.txt` for tokenization (CVE-2026-1260 remediation). No bundled `LICENSE` file ships in this package's `dist-info` (which is why `pip-licenses`' SPDX detection returned UNKNOWN) — confirmed directly against the upstream `google/sentencepiece` repository's `LICENSE` file (Apache License 2.0, not MIT as an earlier draft of this row mistakenly stated). |
| `pygad` | 3.3.1 | ✅ BSD-3-Clause | ✅ Resolved 2026-07-25 | Confirmed by reading the package's bundled `dist-info` `LICENSE` file directly — permissive, no redistribution obligation beyond attribution |
| `rustworkx` | 0.18.0 | ✅ Apache License 2.0 | ✅ Resolved 2026-07-25 | Confirmed by reading the package's bundled `dist-info` `LICENSE` file directly. Not a direct `requirements.txt` entry — it is a transitive dependency of `qiskit==2.4.1` (`qiskit`'s own `Requires:` metadata lists `rustworkx` directly) |
| `cuda-toolkit`, `cuda-bindings`, `cuda-pathfinder` | 13.0.2 / 13.3.1 / 1.5.6 | Proprietary (NVIDIA) | ✅ Resolved 2026-07-25 | Not direct `requirements.txt` entries — confirmed via `pip show`'s `Requires:`/`Required-by:` chain that all three are transitive dependencies of `torch==2.13.0` (`torch` → `cuda-bindings`, `cuda-toolkit`; `cuda-bindings` → `cuda-pathfinder`). Same NVIDIA runtime-library redistribution terms as this matrix's existing 16-package proprietary bucket in §3 — folded in there rather than left as a separate UNKNOWN line item |

**Action (📋 → ✅ target):** confirm the GPL/LGPL Ubuntu-tooling rows are sandbox-only artifacts absent from shipped container images (still open). The four former UNKNOWN rows are now closed as of 2026-07-25 — see above.

---

## 5. Recommended Open Source Foundations — license register

Tranc3's `CLAUDE.md` already maintains a per-Location "Recommended Open Source Foundations" table (fork/integrate candidates, not necessarily yet integrated) with a License column. That table is the source of truth for *foundation-level* license posture; this matrix does not duplicate it. Notable entries requiring attention when adopted:

| Foundation | License | Note |
|---|---|---|
| n8n-io/n8n (The Digital Grid) | Fair-code (self-host free) | Not OSI-approved open source — confirm self-hosted, non-commercial-resale use stays within n8n's Sustainable Use License terms before any commercial resale of Digital Grid workflows |
| outline/outline (The Library) | BSL (self-host free) | Business Source License — converts to Apache 2.0 after a time-delay per version; confirm which version is adopted and its conversion date |
| hashicorp/vault (The Void) | BSL (self-host free) | Same BSL caveat as above — HashiCorp's 2023 license change affects only *commercial competing offerings*, not self-hosted internal use |
| AUTOMATIC1111/stable-diffusion-webui (Sashas Photo Studio) | AGPL 3.0 | Strongest copyleft in the recommended list — if ever exposed as a modified network service, AGPL's network-use clause requires source disclosure; flag before any customer-facing deployment |
| cuckoosandbox/cuckoo (The Ice Box) | GPL 3.0 | Standard copyleft — safe as an unmodified sandboxed tool, review before any redistribution |
| paperless-ngx (DocUtari) | GPL 3.0 | Same as above |
| MISP/MISP, openvas-scanner (Cryptex) | AGPL 3.0 | Same AGPL network-use caveat as Stable Diffusion above |

Full table: [Tranc3 `CLAUDE.md` § Recommended Open Source Foundations](https://github.com/Trancendos/Tranc3/blob/main/CLAUDE.md).

---

## 6. AI model licensing (distinct from library licensing)

Model *weights* carry their own license terms, separate from the inference library code that loads them. The AI Gateway's 5-tier fallback (`src/ai_gateway/`, Tranc3 `CLAUDE.md` § Inference pipeline) touches multiple model sources:

| Tier | Source | License surface | Status |
|---|---|---|---|
| 1 | Ollama (local) | Per-model — varies by model pulled (e.g. Llama family = Llama Community License, Mistral = Apache 2.0) | 📋 No per-model license register exists yet — the specific models actually pulled in production need enumerating |
| 2 | HuggingFace Inference API (free tier) | Per-model, HuggingFace Hub model card license field | 📋 Same gap |
| 3 | OpenRouter free models | Per-model, provider-set | 📋 Same gap |
| 4 | TRANC3_BACKEND_URL (Fly.io) | N/A — proprietary Tranc3Engine when weights are loaded | ✅ No third-party model license risk when running the bootstrap/stub engine |
| 5 | OfflineProvider (deterministic stub) | N/A | ✅ No model, no license surface |

**Action:** this is the genuinely open item behind the "best free and license-compliant models" benchmarking work referenced in Tranc3 session history — a per-model register (model name, source, license, redistribution terms, commercial-use permission, any field-of-use restriction) should be built as its own artifact once the actual candidate model shortlist exists, rather than fabricated here ahead of that benchmarking work.

---

## 7. Emerging legislation watch

The user's framing of "isn't affected by the AI Cannibalism Act or any other acts or clauses" is treated here as **this estate's internal shorthand for a risk category** — AI-model-training-data provenance, output-ownership, and copyright-liability legislation — not a confirmed reference to a specific enacted law of that name. No statute by that exact title is in this framework's [legislation_register.yaml](../../compliance/legislation_register.yaml) as of this scan. Real, relevant instruments already tracked elsewhere in this framework that cover the same risk category:

| Instrument | Status | Where tracked |
|---|---|---|
| EU AI Act (CELEX 32024R1689) | ✅ Programme | [REGULATION-MATRIX.md](REGULATION-MATRIX.md) §3, [legislation_register.yaml](../../compliance/legislation_register.yaml) |
| US copyright/AI litigation trend (NYT v. OpenAI and similar) | 📋 Watch only | Not yet a formal register row — candidate for [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md)-equivalent US watch |
| UK AI White Paper / DSIT | ✅ Programme | [UK-AI-LEGISLATION-MONITORING.md](UK-AI-LEGISLATION-MONITORING.md) |

**Action:** if the user has a specific named act/clause in mind (jurisdiction and title), add it to [legislation_register.yaml](../../compliance/legislation_register.yaml) as a tracked row rather than this matrix asserting one exists.

---

## 8. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Dependency license scan (`pip-licenses`) | Weekly + on PRs touching `requirements*.txt`/`pyproject.toml`/`package*.json` | **Wired into CI 2026-07-25**: `python-audit` job in Tranc3's `.forgejo/workflows/dependency-audit.yml` now runs `pip-licenses --format=markdown` (report, archived as `pip-licenses-report.json`) plus a `pip-licenses --fail-on="GNU General Public License (GPL);GNU Affero General Public License v3 or later (AGPLv3+);GNU Affero General Public License v3"` gate that fails the job if a shipped dependency carries strong copyleft, alongside the existing `pip-audit`/OSV-Scanner CVE scanning it already ran |
| Foundation-license re-check (§5) | On each new foundation adoption | Manual, gated at PR review for the relevant `workers/*/` integration |
| AI model license register (§6) | On each new model added to the AI Gateway's fallback tiers | Manual, once the register in §6 is built |
| Legislation watch (§7) | Quarterly | Aligned with [legislation_register.yaml](../../compliance/legislation_register.yaml)'s existing quarterly cycle |

**Next review:** 2026-10-24 (quarterly, aligned with REGULATION-MATRIX.md's cycle)

---

## 9. Cross-references

- [REGULATION-MATRIX.md](REGULATION-MATRIX.md) — regulatory/legal compliance (this matrix's sibling for *consumed* licenses)
- [IP-BIBLE.md](../bibles/IP-BIBLE.md) — this estate's *own* IP ownership (the inverse concern)
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-012 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
