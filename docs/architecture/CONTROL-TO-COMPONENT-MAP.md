# Control-to-Component Map

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead  
**Purpose:** Trace compliance controls to Tranc3 implementation components

---

## 1. How to use this map

| Audience | Use |
|----------|-----|
| Auditors | Trace ISO/SOC2/DEFSTAN control to code and tests |
| Engineers | Find which component to change for a control gap |
| Incident response | Identify affected controls when a component fails |

**Sources:** DEFSTAN `register.yaml`, ISO 27001 SOA, Magna Carta policies.

---

## 2. ISO 27001:2022 Annex A → Components

| Control | Title | Tranc3 component(s) | Test / evidence |
|---------|-------|---------------------|---------------|
| A.5.1 | Policies for information security | Magna Carta `docs/policies/` | Board approval records |
| A.5.15 | Access control | `zero_trust.py`, `dependencies.py` | `test_zero_trust.py` |
| A.5.16 | Identity management | `infinity-auth`, `users-service` | IAM procedure |
| A.5.17 | Authentication | JWT, MFA, API keys | Penetration tests |
| A.5.23 | Cloud services security | Self-hosted model; supplier policy | POL-SUP-001 |
| A.5.28 | Collection of evidence | `compliance/register.yaml` | CI gate |
| A.5.34 | Privacy & PII protection | `sanitize.py`, ROPA, DSR APIs | GDPR alignment |
| A.8.2 | Privileged access | Admin roles, vault access | Access reviews |
| A.8.3 | Information access restriction | RBAC on routes | Penetration tests |
| A.8.5 | Secure authentication | `infinity-auth` | REQ-IA-001 |
| A.8.9 | Configuration management | Git, Forgejo, docker-compose | Change procedure |
| A.8.10 | Information deletion | DSR erasure workflow | PROC-DSR-001 |
| A.8.11 | Data masking | `sanitize.py` log redaction | Code review |
| A.8.12 | Data leakage prevention | Ice Box, output scanning | Security tests |
| A.8.15 | Logging | Audit worker, Loki | REQ-IA-006 |
| A.8.16 | Monitoring activities | `monitoring`, Prometheus | Dashboards |
| A.8.24 | Cryptography | SQLite AES-GCM, TLS | REQ-IA-002/003 |
| A.8.25 | Secure development lifecycle | CI security scans | SBOM, SAST |
| A.8.28 | Secure coding | Pydantic, Bandit, Semgrep | CI logs |

---

## 3. SOC 2 Trust Services → Components

| Criteria | Control theme | Component(s) |
|----------|---------------|--------------|
| CC6.1 | Logical access | `zero_trust.py`, auth middleware |
| CC6.2 | Registration & authorization | `users-service`, RBAC |
| CC6.3 | Role-based access | Route-level scopes |
| CC6.6 | Encryption | Traefik TLS, SQLite encryption |
| CC6.7 | Transmission security | TLS 1.2+ only at edge |
| CC7.1 | Vulnerability detection | pip-audit, Trivy, Semgrep |
| CC7.2 | Incident detection | Monitoring, Defense Engine |
| CC7.3 | Incident response | WarRoom, PROC-IR-001 |
| CC7.4 | Recovery | PROC-BCP-001, backups |
| CC8.1 | Change management | Forgejo CI, PROC-CHG-001 |
| P1–P8 | Privacy | users-service DSR, ROPA, sanitize |

---

## 4. DEFSTAN REQ → Components

| REQ ID | Title | Primary component | Secondary |
|--------|-------|-------------------|-----------|
| REQ-IA-001 | Auth & access | `src/auth/zero_trust.py` | `dependencies.py` |
| REQ-IA-002 | Secrets | `workers/vault-service/` | Infinity Void |
| REQ-IA-003 | TLS | Traefik config | docker-compose |
| REQ-IA-004 | Input validation | Pydantic models, `sanitize.py` | `loop_validator.py` |
| REQ-IA-005 | Rate limiting | `rate-limit-service` | billing.py tiers |
| REQ-IA-006 | Audit logging | audit worker | Loki |
| REQ-OPS-001 | Monitoring | `monitoring` worker | Prometheus |
| REQ-OPS-003 | Backup/DR | Backup scripts | PROC-BCP-001 |
| REQ-SW-001 | SAST | Bandit, Semgrep | CI |
| REQ-SW-002 | Dependency scan | pip-audit | CI |
| REQ-SW-003 | Secret scan | Gitleaks | CI |
| REQ-AI-001 | Model registry | `ai_governance.py` | model cards API |
| REQ-AI-002 | Loop prevention | `loop_validator.py` | Ice Box |

*Full mapping: all 53 requirements in Tranc3 `compliance/register.yaml`.*

---

## 5. GDPR articles → Components

| Article | Requirement | Component / procedure |
|---------|-------------|----------------------|
| Art. 5 | Principles | Architecture encryption, minimisation |
| Art. 6 | Lawful basis | ROPA, consent flags in users-service |
| Art. 13–14 | Transparency | Privacy policy, model cards |
| Art. 15–22 | Data subject rights | users-service DSR APIs, PROC-DSR-001 |
| Art. 25 | Privacy by design | sanitize, encryption defaults |
| Art. 30 | ROPA | Compliance documentation |
| Art. 32 | Security | Full IA control stack |
| Art. 33–34 | Breach notification | PROC-IR-001, DPO workflow |
| Art. 35 | DPIA | Town Hall compliance gate |

---

## 6. Magna Carta runtime rules → Components

| Rule type | Enforced by | Config key |
|-----------|-------------|------------|
| authentication | `magna_carta.py` + auth middleware | `rules[].type: authentication` |
| privacy | `magna_carta.py` + `sanitize.py` | `rules[].type: privacy` |
| rate_limit | rate-limit-service | `rules[].type: rate_limit` |
| ai_governance | `magna_carta.py` + `ai_governance.py` | `rules[].type: ai_governance` |
| zero_cost | Deploy-time check | `rules[].type: zero_cost` |

Config: [config/magna_carta_config.json](../../config/magna_carta_config.json)

---

## 7. Town Hall governance → Components

| Framework domain | Town Hall room | Tranc3 hook |
|------------------|----------------|------------|
| compliance | MeetingRooms | Quarterly review calendar |
| security | WarRoom | Incident command |
| architecture | BoardRoom | Release approval |
| legal/IP | BoardRoom | Policy sign-off |

Registry: Tranc3 `config/townhall/frameworks.yaml` (magna-carta listed active).

---

## 8. Gap overlay

Controls with **policy only** (Magna Carta) but **partial implementation**:

| Control | Policy | Gap | Component to extend |
|---------|--------|-----|---------------------|
| BCP testing | POL-OPS-003 | DR drill not automated | monitoring + runbooks |
| Supplier DPA | POL-SUP-001 | Register incomplete | Town Hall supplier list |
| AI fairness metrics | POL-AI-001 | Unmeasured | infinity-ai test harness |
| MDM | ISO A.8.1 | Not deployed | Endpoint tooling TBD |

---

## 9. Change impact matrix

When modifying a component, review these controls:

| Component changed | Re-test / re-evidence |
|-------------------|----------------------|
| `zero_trust.py` | REQ-IA-001, A.8.5, CC6.1, pen test |
| `vault-service` | REQ-IA-002, A.8.24, secret scan |
| `infinity-ai` | REQ-AI-*, EU AI Act, POL-AI-001 |
| `magna_carta.py` | Magna Carta register MC-* |
| Traefik config | REQ-IA-003, CC6.6 |
| CI pipeline | REQ-SW-*, CC8.1 |

---

## 10. Related documents

- [BLUEPRINT.md](BLUEPRINT.md)
- [AS-BUILT-ARCHITECTURE.md](AS-BUILT-ARCHITECTURE.md)
- [../compliance/REGULATION-MATRIX.md](../compliance/REGULATION-MATRIX.md)
- Tranc3 `compliance/register.yaml`
