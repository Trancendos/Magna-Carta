# DEFSTAN Alignment (Civilian Discipline Model)

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Platform Engineering  
**Source of truth:** [Tranc3 `compliance/register.yaml`](https://github.com/Trancendos/Tranc3/blob/main/compliance/register.yaml)  
**Classification:** UNCLASSIFIED — PUBLIC

---

## 1. Purpose

Trancendos voluntarily applies **DEF STAN-inspired engineering discipline** to the Tranc3 platform. This is **not** MOD accreditation or classified systems compliance. It is a civilian quality and assurance model drawing from:

| Standard | Theme | Tranc3 application |
|----------|-------|-------------------|
| DEF STAN 00-700 | Information assurance | Auth, secrets, TLS, validation, audit |
| DEF STAN 00-055 | Safety / hazard | AI safety, cascade failure prevention |
| DEF STAN 00-056 | Safety cases | Threat model, risk register |
| DEF STAN 00-600 | Reliability | HA targets, DR, monitoring |
| DEF STAN 00-044 | Environmental | Resource limits, container sizing |
| DEF STAN 05-086 | Quality assurance | CI gates, test evidence, code review |
| DEF STAN 05-057 | Configuration management | Version control, change control, SBOM |

---

## 2. Register summary

| Metric | Value |
|--------|-------|
| Total requirements | 53 |
| COMPLIANT | Majority (see live register) |
| PARTIAL | Documented with remediation |
| NON_COMPLIANT | Tracked with waiver or sprint |
| CI gate threshold | ≥70% compliant |
| Review cycle | Quarterly |

**Live status:** Run `python -m compliance.checker` in Tranc3 repository.

---

## 3. Requirement categories

### 3.1 Information assurance (REQ-IA-*)

| ID | Title | Status | Key evidence |
|----|-------|--------|--------------|
| REQ-IA-001 | Authentication & access control | COMPLIANT | `src/auth/zero_trust.py`, `dependencies.py` |
| REQ-IA-002 | Secrets management | COMPLIANT | `vault-service`, Infinity Void |
| REQ-IA-003 | Transport security | COMPLIANT | Traefik TLS |
| REQ-IA-004 | Input validation | COMPLIANT | Pydantic, `sanitize.py`, penetration tests |
| REQ-IA-005 | Rate limiting | COMPLIANT | `rate-limit-service`, billing tiers |
| REQ-IA-006 | Audit logging | COMPLIANT | Audit worker, append-only logs |
| REQ-IA-007 | Session management | COMPLIANT | JWT rotation, refresh tokens |

### 3.2 Operational assurance (REQ-OPS-*)

| Theme | Examples | Evidence |
|-------|----------|----------|
| Monitoring | Health checks, Prometheus | `monitoring` worker, Grafana |
| Backup & DR | SQLite backup, restore runbook | PROC-BCP-001 |
| Change control | CAB, Forgejo CI | PROC-CHG-001 |
| Incident response | WarRoom, IR procedure | PROC-IR-001 |

### 3.3 Software assurance (REQ-SW-*)

| Theme | Examples | Evidence |
|-------|----------|----------|
| Secure SDLC | SAST, dependency scan | Bandit, Semgrep, pip-audit |
| Test evidence | `test_evidence.yaml` | CI pipeline |
| Configuration management | Git, tagged releases | Forgejo |
| Supply chain | SBOM, licence audit | Trivy, Gitleaks |

### 3.4 AI assurance (REQ-AI-*)

| Theme | Examples | Evidence |
|-------|----------|----------|
| Model registry | Luminous, Turing's Hub | `ai_governance.py` |
| Risk classification | EU AI Act tiers | Model cards API |
| Cascade prevention | Loop validator | `loop_validator.py` |
| Human oversight | High-risk escalation | POL-AI-001 |

---

## 4. CI/CD enforcement

```
Forgejo pipeline
    → compliance/checker.py (register.yaml)
    → tests/test_compliance.py
    → tests/test_penetration.py
    → Gate: compliance_score >= 0.70
```

**Waivers:** Documented in register `notes` or risk register with expiry date and compensating controls.

---

## 5. Magna Carta extensions

Additional Magna Carta-specific requirements extend the DEFSTAN register in [compliance/magna_carta_register.yaml](../../compliance/magna_carta_register.yaml):

| ID | Title | Maps to |
|----|-------|---------|
| MC-001 | Digital rights transparency | REQ-IA-006, GDPR Art. 13 |
| MC-002 | Zero-cost sovereignty check | REQ-SW-010 |
| MC-003 | Town Hall governance gate | REQ-OPS-005 |
| MC-004 | Magna Carta runtime rules | REQ-IA-001 |

---

## 6. Threat model linkage

STRIDE analysis in Tranc3 `ARCHITECTURE_THREAT_MODEL.md` maps threats to DEFSTAN controls:

| STRIDE | Example threat | Mitigating REQ |
|--------|----------------|----------------|
| Spoofing | JWT forgery | REQ-IA-001 |
| Tampering | SQLite corruption | REQ-IA-002, REQ-OPS-003 |
| Repudiation | Missing audit | REQ-IA-006 |
| Information disclosure | Secret in logs | REQ-IA-002, REQ-IA-004 |
| Denial of service | API flood | REQ-IA-005 |
| Elevation of privilege | RBAC bypass | REQ-IA-001, REQ-IA-007 |

---

## 7. Gap and remediation

| Gap | REQ | Action | Owner |
|-----|-----|--------|-------|
| Wazuh SIEM integration | REQ-OPS-002 | Deploy Wazuh agent | Security Ops |
| Formal safety case document | REQ-SW-015 | Publish safety case v1 | Architecture |
| MDM for endpoints | REQ-IA-008 | Evaluate for remote staff | ISMS |

---

## 8. Review cadence

| Activity | Frequency |
|----------|-----------|
| Register status update | Each release |
| Quarterly compliance review | Quarterly (CAB) |
| Penetration test | Annual |
| Threat model refresh | Quarterly |

**Next DEFSTAN review:** 2026-09-06 (aligned with Tranc3 register `meta.review_cycle`)
