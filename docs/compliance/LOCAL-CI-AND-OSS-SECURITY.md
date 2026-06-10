# Local CI and OSS Security Stack

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** Security Ops  
**Registers:** `compliance/zero_cost_tooling_register.yaml`, `compliance/security_testing_register.yaml`

---

## 1. Policy: no mandatory cloud CI

This programme does **not** use **GitHub Actions** (or any metered cloud CI) for mandatory Layer B gates.

| Approach | Cost model | Used here? |
|----------|------------|------------|
| `scripts/run_layer_b_local_ci.sh` | £0 / $0 local | **Yes — recommended** |
| `scripts/weekly_compliance_health.sh` + cron | £0 / $0 local | **Yes** |
| GitHub Actions | Free minutes then billing | **No — prohibited for mandatory Layer B** |
| Aikido MCP (SEC-001) | Free tier with limits; paid tiers exist | **Optional only — deprioritised** |
| OSS stack SEC-006 | 100% free OSS | **Yes — recommended Aikido alternative** |

---

## 2. OSS security stack (SEC-006)

Replaces paid or SaaS-dependent scanning (including Aikido paid features) with open-source tools:

| Tool | ZCT | Capability |
|------|-----|------------|
| Gitleaks | ZCT-007 | Secret detection |
| Bandit | ZCT-008 | Python SAST |
| Semgrep (community) | ZCT-009 | Multi-language SAST |
| pip-audit | ZCT-010 | Python dependency CVEs |

### Install (one-time, free)

```bash
./scripts/install_zero_cost_security_stack.sh
```

### Run

```bash
./scripts/run_oss_security_scans.sh
```

Tools not installed are skipped gracefully. **SEC-002** (`run_security_testing.py`) still satisfies Layer B alone.

---

## 3. Local CI runner

Single entry point for all Layer B checks — use instead of pushing to GitHub to trigger Actions:

```bash
./scripts/run_layer_b_local_ci.sh
```

Includes: compliance health, readiness score, DPA check, SEC-002, ZCT verifier, SEC-006 OSS scans.

### Optional pre-commit hook

```bash
./scripts/install_local_pre_commit_hook.sh
```

Runs `run_layer_b_local_ci.sh` before each local commit. No cloud cost.

---

## 4. Aikido vs OSS

| Need | Mandatory | Recommended free path |
|------|-----------|----------------------|
| Layer B pass | SEC-002 local script | Always |
| Secrets + SAST depth | No | SEC-006 OSS stack |
| IDE-integrated SaaS scan | No | SEC-001 Aikido Free (optional) |

If Aikido introduces cost, account limits, or unavailable MCP: use **SEC-006** only. Layer B score is unchanged.

---

## 5. Related

- [ZERO-COST-SECURITY-TOOLING.md](ZERO-COST-SECURITY-TOOLING.md)
- [AIKIDO-SECURITY-TESTING-FRAMEWORK.md](AIKIDO-SECURITY-TESTING-FRAMEWORK.md) (optional appendix)
