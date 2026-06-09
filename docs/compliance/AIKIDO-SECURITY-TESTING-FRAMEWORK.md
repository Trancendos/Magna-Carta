# Aikido Security Testing Framework

**Version:** 1.1.0  
**Date:** 2026-06-09  
**Owner:** Security Ops  
**Register:** `compliance/security_testing_register.yaml`  
**Readiness model:** [COMPLIANCE-READINESS-MODEL.md](COMPLIANCE-READINESS-MODEL.md) (Layer B continuous; Layer C annual pen test)

> **Primary policy:** [ZERO-COST-SECURITY-TOOLING.md](ZERO-COST-SECURITY-TOOLING.md) defines mandatory £0/$0 Layer B tooling. SEC-002 (local script) is required; Aikido (SEC-001) is an **optional free-tier enhancement** — not a blocker.

---

## 1. Purpose

Provides **continuous** security testing for this repository — SAST, secrets detection, and issue triage — distinct from the **annual external penetration test** (ACT-005, Layer C).

| Channel | ID | Layer | Status |
|---------|-----|-------|--------|
| Aikido MCP (live feed) | SEC-001 | B | `pending_connection` until MCP authenticated |
| Local security script | SEC-002 | B | Active — `scripts/run_security_testing.py` |
| Compliance health (MON-014/016) | SEC-003 | B | Active |
| PROC-AI-003 threat assessments | SEC-004 | B | Active |
| External pen test | SEC-005 | C | Owner gate — ACT-005 |

**Aikido does not replace an external pen test.** It catches regressions on every change; ACT-005 validates adversarial assumptions annually.

---

## 2. When to run

| Trigger | Commands |
|---------|----------|
| Weekly (with compliance health) | `./scripts/weekly_compliance_health.sh` |
| Pre-commit / pre-PR | `python3 scripts/run_security_testing.py --report` |
| After material code change | Aikido `aikido_full_scan` (when MCP connected) |
| Readiness score | `python3 scripts/readiness_automation_score.py --report` |

---

## 3. Aikido MCP integration (SEC-001)

Connect the **Aikido** MCP server in Cursor (desktop IDE). Tools used by this programme:

| Tool | Use |
|------|-----|
| `aikido_full_scan` | Full repository scan on demand |
| `aikido_issues_list` | List open findings for triage |
| `aikido_ignore_issue` | Document accepted risk with justification |

When MCP is unavailable (e.g. cloud agent, no auth), SEC-002 runs as fallback. `pending_connection` does **not** reduce Layer B readiness percent.

---

## 4. Local continuous testing (SEC-002)

`scripts/run_security_testing.py` scans text artefacts for:

- PEM private key blocks  
- AWS access key id patterns  
- High-entropy secret assignments in code  
- Committed `.env` files (non-example)  
- Dangerous pipe-to-shell install patterns  

```bash
python3 scripts/run_security_testing.py --report
python3 scripts/run_security_testing.py --report --strict   # fail on warnings
```

Remediation: [PROC-VUL-001](../procedures/PROC-VUL-001-Vulnerability-Management.md), [HYMN-VUL-001](../hymn-sheets/HYMN-VUL-001-Vulnerability-Triage.md).

---

## 5. Compliance framework alignment

| Framework / control | Artefact |
|---------------------|----------|
| OWASP ASVS | [ASVS-GAP-CHECKLIST.md](ASVS-GAP-CHECKLIST.md) |
| OWASP AI Exchange | [OWASP-AI-EXCHANGE-ALIGNMENT.md](OWASP-AI-EXCHANGE-ALIGNMENT.md) |
| Vulnerability management | PROC-VUL-001 |
| Annual adversarial test | [PEN-TEST-PROGRAMME.md](../evidence/PEN-TEST-PROGRAMME.md) (programme ready; execution = owner) |

---

## 6. Certification evidence slot

When an external pen test completes, upload the report to `docs/evidence/certifications/` matching pattern `pentest-*` (CERT-004). The readiness scorer detects uploads automatically; no agent can confirm execution without the file.

---

## 7. Triage workflow

1. Run SEC-002 (or Aikido scan when connected).  
2. Log findings in vulnerability register or issue tracker.  
3. Fix or document accepted risk per PROC-VUL-001.  
4. Re-run scan before merge.  
5. Weekly health check logs MON summary to `compliance/health_check_history.yaml`.
