# Intellectual Property Matrix

**Version:** 1.0.0
**Date:** 2026-07-24
**Owner:** Legal / Engineering Lead
**Scope:** Every Service, Solution, Application, and AI in the Trancendos estate
**Register:** MC-013
**Machine-readable:** [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) (`intellectual_property` section)

---

## 1. Purpose

Tracks, per entity, two distinct IP questions the existing [IP-BIBLE.md](../bibles/IP-BIBLE.md) and [PROC-IP-001](../procedures/PROC-IP-001-Intellectual-Property-Management.md) address only at the *process* level (how invention assignment, trade-secret handling, and OSS clearance are supposed to work), not the *per-entity* level:

1. **Estate protection** — is this entity's own original work (code, brand name, personality profile as a creative/character work, generated content) actually owned by Trancendos with no unresolved ownership ambiguity?
2. **Non-infringement** — does this entity risk infringing someone else's IP (a real third-party trademark collision on a platform entity's public-facing name, unlicensed third-party assets, AI-generated output whose training provenance creates copyright exposure)?

This matrix does **not** duplicate the [License Compliance Matrix](LICENSE-COMPLIANCE-MATRIX.md) (MC-012), which already covers open-source *dependency* licensing — that is an inbound-obligation question, not an ownership question, and its findings are cross-referenced rather than repeated here.

**Honesty note (per this framework's own rule, REGULATION-MATRIX.md §5):** do not claim IP clearance in product copy unless the corresponding row is ✅ with evidence.

---

## 2. Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Verified — Trancendos-owned, no known third-party conflict |
| ⚠️ | Owned, but with a documented caveat (naming collision risk, unverified provenance) |
| 📋 | Not yet assessed — flagged for legal/trademark review |
| ❌ | Confirmed conflict or ownership gap — remediation required |
| 🎯 | Requires an external action (trademark search, registration, legal opinion) this framework cannot self-certify |

---

## 3. Estate protection — original work ownership

| Question | Status | Basis |
|---|---|---|
| Is Tranc3's application code (the 43-entity platform, `src/`, `workers/`) Trancendos-owned work product? | ✅ | Developed under Trancendos-controlled repositories (`Trancendos/Tranc3`, `Trancendos/CranBania`, `Trancendos/magna-carta`, `Trancendos/InfinityStyles`); no external contractor IP-assignment gap identified in this scan |
| Are the 43 platform entity names (The Spark, Luminous, Infinity, tAimra, etc. — `PLATFORM_ENTITIES.md`) protectable as Trancendos brand/trade-mark assets? | 🎯 | No formal trademark search or registration has been performed for any of the 43 names as of this scan — this is a genuine open item, not a completed control. Recommend prioritizing the platform's most externally-visible names (Trancendos itself, "Infinity", "Luminous") if commercial trademark registration is ever pursued |
| Do personality profile JSONs (`src/personality/profiles/*.json` — character voice, backstory, traits) constitute original creative work owned by Trancendos? | ✅ | Authored in-house per [PERSONALITY-ARCHETYPES.md](../governance/PERSONALITY-ARCHETYPES.md); no third-party character licensing involved |
| Does AI-generated code/content (produced by Claude Code / other assistants working in this repo) create an ownership ambiguity? | ⚠️ | Current mainstream position (US Copyright Office guidance, UK CDPA 1988 s.9(3) computer-generated works provision) treats AI-assisted code with meaningful human direction/selection as ordinarily eligible for ownership by the directing party — but this has not been the subject of a specific legal opinion for this estate. Treated as a watch item, not a settled ✅, pending that opinion if commercial exposure increases |

---

## 4. Non-infringement — third-party IP risk

| Entity / Asset | Risk | Assessment |
|---|---|---|
| **Sashas Photo Studio** | ⚠️ Naming | Deliberately spelled without an apostrophe (`CLAUDE.md` naming rule: "no apostrophe — canonical; not 'Sasha's Photo Studio'") — this appears to be an intentional distinguishing choice already, which reduces (but does not eliminate) confusability risk against any third-party "Sasha's" mark. No trademark clearance search has been run to confirm no conflicting registered mark exists in any target jurisdiction |
| **TateKing** | 📋 Not assessed | Common personal-name-style brand; no clearance search performed |
| **The Nexus / Nexus-Prime** | 📋 Not assessed | Generic term, lower collision risk, but not searched |
| Third-party recommended-foundation names used in product copy (n8n, Outline, Vault, ComfyUI, etc. — `CLAUDE.md`'s Recommended Open Source Foundations table) | ✅ | These are referenced by their own project names as integration targets, not re-branded as Trancendos originals — nominative use, not a trademark risk, provided marketing copy never implies endorsement by those projects. No instance of implied endorsement found in this scan |
| AI model outputs served through the AI Gateway's 5-tier fallback (`src/ai_gateway/`) | 📋 Not assessed | Output-ownership and training-data-provenance risk for third-party-hosted models (HuggingFace Inference API, OpenRouter free models) depends on each provider's own terms of service, which have not been catalogued here — this is the same open item flagged in the [License Compliance Matrix](LICENSE-COMPLIANCE-MATRIX.md) §6 for model licensing, and is not duplicated with separate findings |
| Stock/generated imagery via Sashas Photo Studio's planned Stable Diffusion / ComfyUI backend | 🎯 | Not yet integrated (`CLAUDE.md` marks this "planned backend") — flag for IP review before go-live, since Stable Diffusion-family model training-data provenance is an active area of copyright litigation (see [LICENSE-COMPLIANCE-MATRIX.md](LICENSE-COMPLIANCE-MATRIX.md) §7) |

---

## 5. Per-Service / Solution / Application / AI coverage note

Given the estate's scale (43 named entities, ~90 standalone workers, multiple AI personas), this matrix does **not** attempt a bespoke IP row per entity — the overwhelming majority carry no distinct IP exposure beyond the general code-ownership and OSS-license posture already covered in §3 and the [License Compliance Matrix](LICENSE-COMPLIANCE-MATRIX.md). Instead, §4 lists only the entities with a *specific, non-generic* IP question (naming collision risk, third-party model/asset dependency). Any entity not listed in §4 is assessed as carrying no IP risk beyond the estate-wide baseline in §3 — this is a deliberate scoping choice, not an oversight, and is revisited whenever a new entity is added or an existing one gains a third-party integration.

---

## 6. Review and re-scan schedule

| Activity | Frequency | Mechanism |
|---|---|---|
| Trademark collision spot-check for newly named entities | On new entity naming | Manual, at naming-decision time — not yet a gated checklist item; recommend adding to the entity-creation process |
| AI model output/training-provenance watch | Aligned with License Compliance Matrix §8 | Manual, pending model shortlist |
| Full re-review of this matrix | Quarterly | Aligned with REGULATION-MATRIX.md's cycle |

**Next review:** 2026-10-24

---

## 7. Cross-references

- [LICENSE-COMPLIANCE-MATRIX.md](LICENSE-COMPLIANCE-MATRIX.md) — inbound OSS/model license obligations (this matrix's sibling for *consumed* rights)
- [IP-BIBLE.md](../bibles/IP-BIBLE.md) — process-level IP management (invention assignment, trade secrets)
- [PROC-IP-001](../procedures/PROC-IP-001-Intellectual-Property-Management.md) — the underlying procedure this matrix adds entity-level granularity to
- [TRANC3-REGISTER-BRIDGE.md](TRANC3-REGISTER-BRIDGE.md) — MC-013 bridge entry
- [compliance/estate_protection_matrices.yaml](../../compliance/estate_protection_matrices.yaml) — machine-readable register
