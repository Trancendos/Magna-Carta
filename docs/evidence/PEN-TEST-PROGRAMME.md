# Penetration Test Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Security Ops  
**Procedure:** [PROC-VUL-001](../procedures/PROC-VUL-001-Vulnerability-Management.md)  
**Action:** ACT-005

---

## 1. Purpose

Defines scope, frequency, and remediation workflow for external penetration testing. Complements continuous vulnerability scanning (CI) with adversarial validation.

| Symbol | Meaning |
|--------|---------|
| ✅ | Programme documented |
| 🎯 | External test execution and report pending |

---

## 2. Scope

| Layer | In scope | Notes |
|-------|----------|-------|
| External perimeter | ✅ | Traefik, TLS, public APIs |
| Authentication | ✅ | Zero Trust IAM, JWT, MFA |
| API / workers | ✅ | Representative P0 services |
| Internal segmentation | ⚠️ Optional | Docker network isolation |
| Social engineering | ❌ | Out of scope unless contracted |
| Denial of service | ❌ | Coordinated with ops only |

**Environment:** Staging mirror of production; production only with written approval and change window.

---

## 3. Frequency

| Test type | Frequency | Next due |
|-----------|-----------|----------|
| Full external pen test | Annual | 2026-12-31 (🎯 ACT-005) |
| Targeted retest (critical findings) | Within 30 days of fix | Per finding |
| Pre-certification test | Before ISO/SOC audit | 2026-Q4 |

---

## 4. Provider criteria

- CREST / CHECK / equivalent recognised methodology
- NDA and rules of engagement signed
- Safe harbour / authorisation letter from Trancendos
- Deliverables: executive summary, technical report, CVSS-rated findings, retest letter

---

## 5. Remediation SLA

| Severity | Remediation target | Escalation |
|----------|-------------------|------------|
| Critical | 7 days | P1 incident if exploited |
| High | 30 days | CAB visibility |
| Medium | 90 days | Vuln backlog |
| Low | Next release or accept | Risk register if deferred |

Findings tracked in vulnerability backlog and [COMPLIANCE-ACTION-TRACKER.md](../compliance/COMPLIANCE-ACTION-TRACKER.md) when compliance-impacting.

---

## 6. Related documents

- [PEN-TEST-LOG.md](PEN-TEST-LOG.md)
- [PROC-VUL-001](../procedures/PROC-VUL-001-Vulnerability-Management.md)
- [SOC2-EVIDENCE-SCHEDULE.md](../compliance/SOC2-EVIDENCE-SCHEDULE.md) — EV-SOC-005
