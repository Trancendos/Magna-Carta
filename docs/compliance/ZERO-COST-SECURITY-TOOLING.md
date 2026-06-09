# Zero-Cost Security Tooling

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** Security Ops  
**Register:** `compliance/zero_cost_tooling_register.yaml`  
**Security channels:** `compliance/security_testing_register.yaml`

---

## 1. Policy

**Layer B security testing must cost £0 / $0** to run in this repository. No mandatory subscriptions, credit cards, or per-seat SaaS.

| Tier | Tools | Required? |
|------|-------|-----------|
| **Mandatory (always)** | `run_security_testing.py`, `compliance_health_check.py`, `zero_cost_tooling_check.py` | Yes |
| **Optional OSS** | Gitleaks, Bandit, Semgrep community, pip-audit | No — run when installed |
| **Optional free SaaS** | Aikido Free (no CC) via MCP | No — SEC-001 enhancement only |
| **Owner gate** | Annual external pen test | Layer C — ACT-005 |

---

## 2. Is Aikido free?

**Yes — with limits.** Aikido offers a **Free plan, no credit card**:

- IDE/MCP integration (Cursor, VS Code, Windsurf)
- SAST and secrets detection for **JavaScript, TypeScript, Python**
- GitHub Action free tier focuses on **dependency/CVE** scanning; blocking on full SAST/IaC is **paid**

**Conclusion for this programme:** Aikido is an **optional enhancement** (SEC-001). Layer B readiness does **not** require Aikido connection. Local SEC-002 is the mandatory zero-cost baseline.

Paid Aikido features are **not** in scope for mandatory tooling.

---

## 3. Zero-cost alternatives (recommended stack)

| Capability | Primary (mandatory) | Optional OSS | Optional free SaaS |
|------------|---------------------|--------------|-------------------|
| Secret detection | SEC-002 patterns | Gitleaks (ZCT-007) | Aikido Free SEC-001 |
| Python SAST | SEC-002 heuristics | Bandit (ZCT-008) | Aikido Free |
| Multi-language SAST | — | Semgrep community (ZCT-009) | Aikido Free (JS/TS/Py) |
| Dependency CVEs | Register review | pip-audit (ZCT-010) | Aikido GH Action deps |
| Compliance gates | MON-014, MON-016 | — | — |
| Annual pen test | Programme doc only | — | Owner commissions (Layer C) |

### Other free options (not wired by default)

| Tool | Cost | Notes |
|------|------|-------|
| [Trivy](https://github.com/aquasecurity/trivy) | OSS | Container/IaC when apps ship images |
| [detect-secrets](https://github.com/Yelp/detect-secrets) | OSS | Yelp baseline scanner |
| `npm audit` / `yarn audit` | Free | When Node apps present |
| GitHub Dependabot | Free on GitHub | Optional when using GitHub hosting |

---

## 4. Commands

```bash
# Mandatory — Layer B
python3 scripts/run_security_testing.py --report
python3 scripts/zero_cost_tooling_check.py --report

# Optional OSS (skips tools not installed)
./scripts/run_oss_security_scans.sh

# Weekly bundle (includes all mandatory checks)
./scripts/weekly_compliance_health.sh
```

---

## 5. Aikido MCP (optional SEC-001)

Connect **Aikido** MCP in Cursor desktop (Free account token). Tools: `aikido_full_scan`, `aikido_issues_list`, `aikido_ignore_issue`.

When MCP is unavailable (cloud agent, no auth): SEC-002 runs automatically. `pending_connection` does **not** reduce Layer B %.

See also: [AIKIDO-SECURITY-TESTING-FRAMEWORK.md](AIKIDO-SECURITY-TESTING-FRAMEWORK.md) (Aikido-specific appendix).

---

## 6. Verification

```bash
python3 scripts/zero_cost_tooling_check.py --report
python3 scripts/readiness_automation_score.py --report
```

Register rows: `compliance/zero_cost_tooling_register.yaml` — verified by ZCT-005.

---

## 7. Related

- [COMPLIANCE-READINESS-MODEL.md](COMPLIANCE-READINESS-MODEL.md)
- [TRANCENDOS-UNIVERSE-AND-INFINITY-NETWORK.md](../architecture/TRANCENDOS-UNIVERSE-AND-INFINITY-NETWORK.md)
