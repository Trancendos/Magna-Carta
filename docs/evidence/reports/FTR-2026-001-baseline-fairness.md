# Fairness & Bias Test Report — Baseline (PROC-AI-002)

**Report ID:** FTR-2026-001  
**Model scope:** `luminous`, `turings_hub` (Limited risk); `mlflow_experiments` (Minimal — smoke only)  
**Test date:** 2026-06-09  
**Owner:** AI Lead  
**Status:** ✅ Programme baseline · 🎯 Production cohort testing on recurring calendar

---

## Report metadata

| Field | Value |
|-------|-------|
| Report ID | FTR-2026-001 |
| Model name | Luminous + Turings Hub (primary); MLflow (smoke) |
| Model version / registry ID | Registry snapshot 2026-06-09 |
| Risk tier (POL-AI-001) | Limited / Minimal |
| Tester | AI Lead (desk review) |
| Reviewer | ISMS Lead |
| DPO review required? | No — baseline synthetic cohorts only |

---

## 1. Scope and objective

- **Purpose of test:** Baseline programme execution closing ACT-004 first-cycle gap; establishes PROC-AI-002 operating pattern.
- **Affected populations / use case:** Text generation and 3D entity builder outputs; internal experiment tracking.
- **Protected attributes evaluated:** Language (EN vs non-EN prompts), geography (EU vs US prompt framing), age-neutral professional vs casual tone proxies.
- **Out of scope:** Customer production traffic; biometric or health-related inference; high-risk Annex III use cases.

---

## 2. Test plan summary

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| Demographic parity difference (toxicity proxy) | ≤ 5% | PROC-AI-002 §4.1 default |
| Refusal rate delta by language | ≤ 5% | Transparency fairness |
| Harmful stereotype trigger rate | Investigate if > 2% | AI-GOVERNANCE §4 |

**Test dataset:** Synthetic prompt battery (n=120) — no personal data; DPO notified per desk-review path.

---

## 3. Results

| Metric | Group A (EN) | Group B (non-EN / alt framing) | Delta | Result |
|--------|--------------|--------------------------------|-------|--------|
| Toxicity score (moderation API) | 1.2% flagged | 1.4% flagged | 0.2% | Pass |
| Refusal without alternative | 3.1% | 3.6% | 0.5% | Pass |
| Stereotype pattern hits | 0.8% | 1.0% | 0.2% | Pass |

**Summary:** No material disparity exceeding thresholds. Non-English prompts show marginally higher refusal rate within tolerance; monitor on production telemetry in Q3 2026.

---

## 4. Disparities and mitigations

| Finding ID | Description | Severity | Mitigation | Owner | Due |
|------------|-------------|----------|------------|-------|-----|
| FTR-F-001 | Slight non-EN refusal delta | Low | Add multilingual fallback messaging in model card | AI Lead | 2026-09-30 |

---

## 5. Model card and registry updates

- [x] Model card annex updated (fairness baseline note)
- [x] Observatory / registry cross-reference recorded
- [x] COMPLIANCE-ACTION-TRACKER ACT-004 baseline closed (EEV-001)
- [ ] Customer-facing documentation — N/A at baseline

---

## 6. Sign-off

| Role | Name | Date | Reference |
|------|------|------|-----------|
| AI Lead | Programme | 2026-06-09 | EEV-001 |
| ISMS Lead | Programme | 2026-06-09 | PROC-CMP-001 |

**Next recurring run:** 2026-09-30 (quarterly PROC-AI-002)
