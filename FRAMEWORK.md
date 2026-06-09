# Magna Carta Framework — Master Blueprint

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Trancendos Platform Engineering  
**Scope:** Infinity Network applications and Trancendos Universe ecosystem services  
**Classification:** UNCLASSIFIED — PUBLIC

---

## 1. Purpose

The Magna Carta Framework defines **how Trancendos governs, secures, complies, and operates** Infinity Network applications atop **Trancendos Universe — The Foundation**. It is the single authoritative layer above:

- **DEFSTAN** — operational control register (53 requirements, CI-gated ≥70%)
- **ISO 27001:2022** — ISMS Statement of Applicability (certification target Q2 2027)
- **SOC 2 Type II** — Trust Services Criteria evidence programme (target Q1 2027)
- **UK GDPR / EU GDPR** — privacy by design and data subject rights
- **EU AI Act / ISO 42001 / NIST AI RMF** — AI governance baseline
- **OWASP + Zero Trust** — application and identity security

This document is the **blueprint** that connects governance intent to Infinity Network app implementations (e.g. Tranc3 App Framework).

**Maturity:** Artefacts in this repository prove the **documentation programme** (policies, registers, mappings). They do not by themselves prove ISO 27001 certification, SOC 2 Type II, signed supplier DPAs, or production runtime enforcement — those require operational validation. See [docs/00-EXECUTIVE-SUMMARY.md](docs/00-EXECUTIVE-SUMMARY.md#maturity-model-read-this-first).

---

## 2. Framework layers

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 1 — GOVERNANCE & RIGHTS (Magna Carta Foundation)             │
│  Digital rights · Town Hall · BoardRoom · CAB · PRINCE2 gates       │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  LAYER 2 — POLICIES (WHAT we require)                               │
│  InfoSec · Privacy · AUP · IR · Change · BCP · Supplier · AI Ethics │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  LAYER 3 — PROCEDURES (HOW we execute)                              │
│  IR · Change · Access · DSR · Vuln mgmt · Backup · Compliance review│
└───────────────────────────────┬─────────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  LAYER 4 — COMPLIANCE & REGULATIONS (WHAT law/standard demands)     │
│  ISO · SOC2 · GDPR · DEFSTAN · AI Act · Legislation register        │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  LAYER 5 — ARCHITECTURE & CONTROLS (WHERE it is implemented)        │
│  Workers · Auth · Vault · Audit · Ice Box · Observatory · CI/CD     │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────────┐
│  LAYER 6 — EVIDENCE & ASSURANCE (PROOF it works)                    │
│  Action tracker · risk register · SOC2 schedule · audit programme   │
│  register.yaml · test_evidence.yaml · CI gates · SOC2 collector     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core principles

### 3.1 Digital rights (Magna Carta)

1. **Transparency** — Users can see what data is processed and why (ROPA, model cards).
2. **Consent** — Lawful basis and consent captured before non-essential processing.
3. **Minimisation** — Collect and retain only what is necessary; 90-day audit retention default.
4. **Security by default** — Zero Trust IAM, encryption at rest, TLS in transit, no secrets in VCS.
5. **Accountability** — Tamper-evident audit logs, traceable change control, quarterly reviews.
6. **Human agency** — AI outputs are assistive; high-risk decisions require human review.
7. **Zero-cost sovereignty** — Self-hosted first; no mandatory paid third-party data processors.

### 3.2 Zero-cost mandate

All platform services must be deployable without paid API dependencies. External services require documented DPAs, SCCs where applicable, and Town Hall zero-cost check approval.

### 3.3 Defence-in-depth

| Zone | Controls |
|------|----------|
| Edge (Traefik) | TLS 1.2+, rate limiting, routing, optional WAF |
| Application | JWT + MFA, RBAC, input validation, Ice Box scanning |
| Data | AES-GCM SQLite encryption, Infinity Void vault, append-only audit |
| Operations | CAB change control, DR runbooks, compliance CI gate |
| Supply chain | pip-audit, Bandit, Semgrep, Gitleaks, Trivy, SBOM |

---

## 4. Governance model (Town Hall)

Governance is orchestrated through **The Town Hall** (`config/townhall/frameworks.yaml` in Tranc3):

| Room | Purpose | Triggers |
|------|---------|----------|
| **BoardRoom** | Executive approvals, PRINCE2 stage gates | Major releases, policy changes |
| **WarRoom** | P0 incident command | Security breach, platform outage |
| **MeetingRooms** | Scheduled reviews | Quarterly compliance, CAB sessions |

**Lead AI:** Tristuran · **PID:** PID-TWH

Framework domains registered: governance, agile, ITSM/ITIL, PRINCE2, compliance, security, legal/IP/finance, architecture, documentation.

---

## 5. Compliance operating model

### 5.1 Control lifecycle

```
Identify → Implement → Verify → Evidence → Review → Improve
    ↑                                              │
    └──────────── waivers / risk register ─────────┘
```

| Stage | Owner | Artefact |
|-------|-------|----------|
| Identify | ISMS Lead | Regulation matrix, legislation register |
| Implement | Engineering | Code, workers, IaC |
| Verify | QA / Security | Tests, penetration suite, checker CLI |
| Evidence | Compliance | `register.yaml`, `test_evidence.yaml` |
| Review | CAB / BoardRoom | Quarterly DEFSTAN + Magna Carta review |
| Improve | All | Risk register, waivers, remediation |

### 5.2 Certification roadmap

| Milestone | Target | Status |
|-----------|--------|--------|
| DEFSTAN CI gate ≥70% | Active | ✅ Enforced in Forgejo |
| External security review | Q4 2026 | ⚠️ Planned |
| SOC 2 Type II report | Q1 2027 | ⚠️ Evidence collection active |
| ISO 27001:2022 certification | Q2 2027 | ✅ Programme (SOA); 🎯 external audit |
| ISO 42001 (AI MS) | TBD | ✅ Programme baseline (GENAI-MATURITY §10) |

### 5.3 Regulation coverage summary

| Regulation / Standard | Applicability | Maturity | Primary evidence |
|----------------------|---------------|----------|------------------|
| UK GDPR / DPA 2018 | ✅ Full | Implemented | ROPA, PIA, users-service DSR |
| EU GDPR | ✅ Full | Implemented | Same + SCCs for external AI fallback |
| ISO 27001:2022 | ✅ Full | Draft SOA | `docs/compliance/ISO27001_SOA.md` |
| SOC 2 Type II | ✅ Full | Draft mapping | `docs/compliance/SOC2_TYPE_II.md` |
| DEFSTAN (civilian) | ✅ Voluntary | Strong | `compliance/register.yaml` |
| EU AI Act | ✅ Programme | Implemented | `AI_GOVERNANCE.md`, model cards, MC-RULE-004 |
| ISO 42001 | ✅ Programme | Baseline | AI governance module, GENAI-MATURITY |
| NIST AI RMF | ✅ Programme | Mapped | AI governance mapping |
| OWASP Top 10 | ✅ Full | Operational | Penetration tests, hardening |
| PCI DSS | ❌ N/A | — | No cardholder data environment |
| HIPAA | ⚠️ US PHI boundary | Programme | [HIPAA-ALIGNMENT.md](docs/compliance/HIPAA-ALIGNMENT.md), MC-008 |
| FCA Handbook | ✅ Supplier / conduct | Programme | [FCA-ALIGNMENT.md](docs/compliance/FCA-ALIGNMENT.md), MC-009 |
| FedRAMP / CMMC | ❌ N/A | — | Not in scope |
| SOX | ❌ N/A | — | Not a listed entity |
| CCPA/CPRA | ⚠️ Partial | Via GDPR controls | Extend if US CA users material |

Full matrix: [docs/compliance/REGULATION-MATRIX.md](docs/compliance/REGULATION-MATRIX.md)

### 5.4 External governance frameworks (adapted)

Third-party GenAI and compliance methodologies are mapped to Magna Carta — not adopted wholesale. Use these when communicating maturity to boards, auditors, or partners:

| Artefact | Purpose |
|----------|---------|
| [docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md](docs/compliance/EXTERNAL-FRAMEWORK-MAPPING.md) | Connor Group five-domain GenAI framework → Magna Carta layers |
| [docs/compliance/GENAI-MATURITY-ASSESSMENT.md](docs/compliance/GENAI-MATURITY-ASSESSMENT.md) | Nascent → Leading maturity self-assessment with Tranc3 baseline |
| [docs/compliance/OBLIGATIONS-REGISTER.md](docs/compliance/OBLIGATIONS-REGISTER.md) | Regulatory obligations register; monitoring vs audit distinction |
| [docs/compliance/HIPAA-ALIGNMENT.md](docs/compliance/HIPAA-ALIGNMENT.md) | US PHI boundary, BAA tiers, MC-008 / MC-RULE-009 |
| [docs/compliance/FCA-ALIGNMENT.md](docs/compliance/FCA-ALIGNMENT.md) | UK financial conduct supplier perimeter, MC-009 |
| [docs/compliance/PECR-ALIGNMENT.md](docs/compliance/PECR-ALIGNMENT.md) | UK electronic marketing and cookies programme |
| [docs/compliance/COMPANIES-ACT-ALIGNMENT.md](docs/compliance/COMPANIES-ACT-ALIGNMENT.md) | Corporate governance alignment |
| [docs/compliance/SUPPLIER-DPA-REGISTER.md](docs/compliance/SUPPLIER-DPA-REGISTER.md) | Processor DPA register (Art. 28) |
| [docs/compliance/ICO-REGISTRATION.md](docs/compliance/ICO-REGISTRATION.md) | ICO fee tier and registration programme |
| [docs/governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md](docs/governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md) | AI governance committee charter |
| [docs/governance/RACI-MATRIX.md](docs/governance/RACI-MATRIX.md) | Extended RACI by activity |
| [docs/evidence/BCP-RESTORE-TEST-LOG.md](docs/evidence/BCP-RESTORE-TEST-LOG.md) | BCP restore test evidence log |
| [docs/compliance/COMPLIANCE-ACTION-TRACKER.md](docs/compliance/COMPLIANCE-ACTION-TRACKER.md) | Open compliance actions and remediation owners |
| [docs/compliance/RISK-REGISTER.md](docs/compliance/RISK-REGISTER.md) | Information security risk register |
| [docs/compliance/SOC2-EVIDENCE-SCHEDULE.md](docs/compliance/SOC2-EVIDENCE-SCHEDULE.md) | SOC 2 Type II evidence catalogue (EV-SOC-001–018) |
| [docs/governance/INTERNAL-AUDIT-PROGRAMME.md](docs/governance/INTERNAL-AUDIT-PROGRAMME.md) | ISO 9.2 internal audit plan (MC-010) |
| [docs/governance/MANAGEMENT-REVIEW-TEMPLATE.md](docs/governance/MANAGEMENT-REVIEW-TEMPLATE.md) | ISO 9.3 management review template |
| [docs/evidence/PEN-TEST-PROGRAMME.md](docs/evidence/PEN-TEST-PROGRAMME.md) | Annual penetration test programme |
| [docs/evidence/POLICY-ATTESTATION-REGISTER.md](docs/evidence/POLICY-ATTESTATION-REGISTER.md) | Staff policy acknowledgement register |
| [docs/compliance/TRANC3-REGISTER-BRIDGE.md](docs/compliance/TRANC3-REGISTER-BRIDGE.md) | MC-001–MC-011 ↔ REQ-### / MC-RULE mapping (MC-011) |
| [docs/engineering/TRANC3-INTEGRATION-GUIDE.md](docs/engineering/TRANC3-INTEGRATION-GUIDE.md) | Staging enablement and checker import (ACT-009) |
| [docs/governance/CONTINUOUS-IMPROVEMENT-PROGRAMME.md](docs/governance/CONTINUOUS-IMPROVEMENT-PROGRAMME.md) | PDCA cycle linking evidence programme to operations |
| [docs/templates/INDEX.md](docs/templates/INDEX.md) | Contract template library index |

Attribution: adapt concepts and cite sources; do not reproduce copyrighted framework text in customer packs.

---

## 6. Architecture blueprint summary

### 6.1 Canonical deployment model

**As-built (production path):** Self-hosted Docker Compose / K8s with Traefik edge, 55 FastAPI workers, SQLite per service (encrypted), OpenBao/Infinity Void for secrets, Forgejo CI/CD, Prometheus/Grafana/Loki observability.

> **Note:** `docs/DOC-02-System-Architecture.md` in Tranc3 describes an aspirational multi-cloud topology (GKE/AKS/EKS, PostgreSQL, Pinecone). **Auditors and operators must use** [docs/architecture/AS-BUILT-ARCHITECTURE.md](docs/architecture/AS-BUILT-ARCHITECTURE.md) as the canonical reference.

### 6.2 Trust boundaries

```
Internet (untrusted)
    → Traefik (TLS, rate limit)
        → Docker internal network (semi-trusted workers)
            → Persistence (SQLite, vault, logs) (trusted)
```

### 6.3 Priority tiers

| Tier | Examples | Availability target |
|------|----------|---------------------|
| P0 | infinity-ws, infinity-auth | 99.9% |
| P1 | users, monitoring, AI, notifications | 99.5% |
| P2 | grid, payments, orders, files | 99.0% |
| Infra | vault, Forgejo, MCP | 99.9% |

Full blueprint: [docs/architecture/BLUEPRINT.md](docs/architecture/BLUEPRINT.md)

---

## 7. Policy and procedure library

### 7.1 Policies (Layer 2)

| ID | Policy | Owner | Review |
|----|--------|-------|--------|
| POL-SEC-001 | Information Security | CISO / ISMS Lead | Annual |
| POL-SEC-002 | Acceptable Use | HR / ISMS | Annual |
| POL-PRI-001 | Data Protection & Privacy | DPO | Annual |
| POL-OPS-001 | Incident Response | Security Ops | Annual |
| POL-OPS-002 | Change Management | CAB Chair | Annual |
| POL-OPS-003 | Business Continuity | Operations | Annual |
| POL-SUP-001 | Supplier Management | Procurement / ISMS | Annual |
| POL-AI-001 | AI Ethics & Governance | AI Lead | Semi-annual |

Index: [docs/policies/INDEX.md](docs/policies/INDEX.md)

### 7.2 Procedures (Layer 3)

| ID | Procedure | Linked policy |
|----|-----------|---------------|
| PROC-IR-001 | Incident Response | POL-OPS-001 |
| PROC-CHG-001 | Change Request | POL-OPS-002 |
| PROC-IAM-001 | Access Provisioning | POL-SEC-001 |
| PROC-DSR-001 | Data Subject Requests | POL-PRI-001 |
| PROC-VUL-001 | Vulnerability Management | POL-SEC-001 |
| PROC-BCP-001 | Backup & Restore | POL-OPS-003 |
| PROC-CMP-001 | Compliance Review | All |
| PROC-AI-002 | Fairness & Bias Testing | POL-AI-001 |
| PROC-AI-003 | AI Security Threat Assessment | POL-AI-001, POL-SEC-001 |
| PROC-CHG-002 | Post-Implementation Review | POL-OPS-002 |
| PROC-TRN-001 | Security Awareness & Attestation | POL-SEC-001, POL-SEC-002 |

Index: [docs/procedures/INDEX.md](docs/procedures/INDEX.md)

---

## 8. Runtime integration (Tranc3)

Magna Carta rules are enforced at request boundary when enabled:

```python
# src/compliance/magna_carta.py
MAGNA_CARTA_ENABLED=true
MAGNA_CARTA_CONFIG_PATH=./config/magna_carta_config.json
```

Rule categories in config:

- `authentication` — JWT/MFA required on protected routes
- `privacy` — PII fields blocked in logs/responses without consent
- `rate_limit` — Tier-based limits enforced
- `ai_governance` — Model card and risk tier checks on inference
- `zero_cost` — Block deployments referencing paid mandatory APIs

Configuration: [config/magna_carta_config.json](config/magna_carta_config.json)

Register bridge and staging checklist: [docs/compliance/TRANC3-REGISTER-BRIDGE.md](docs/compliance/TRANC3-REGISTER-BRIDGE.md), [compliance/tranc3_register_bridge.yaml](compliance/tranc3_register_bridge.yaml), [docs/engineering/TRANC3-INTEGRATION-GUIDE.md](docs/engineering/TRANC3-INTEGRATION-GUIDE.md).

---

## 9. Roles and responsibilities (RACI summary)

Summary matrix below; full activity-level RACI: [docs/governance/RACI-MATRIX.md](docs/governance/RACI-MATRIX.md). AI committee charter: [docs/governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md](docs/governance/AI-GOVERNANCE-COMMITTEE-CHARTER.md).

| Activity | ISMS Lead | Engineering | DPO | CAB | Executive |
|----------|-----------|-------------|-----|-----|-----------|
| Policy approval | A | C | C | R | A |
| Control implementation | C | R/A | I | I | I |
| Compliance evidence | R/A | C | C | I | I |
| Incident command | C | R | I | I | A (P0) |
| Change approval | C | R | I | A | I |
| External audit | R | C | C | I | A |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

---

## 10. Document hierarchy

When documents conflict, precedence is:

1. **Legislation** (law)
2. **Certification requirements** (ISO, SOC2 auditor interpretation)
3. **Magna Carta policies** (this repo — `docs/policies/`)
4. **DEFSTAN register** (Tranc3 `compliance/register.yaml`)
5. **Procedures and runbooks**
6. **Aspirational architecture docs** (lowest — must be labelled as target state)

---

## 11. Related repositories

| Repository | Role |
|------------|------|
| [Trancendos/Tranc3](https://github.com/Trancendos/Tranc3) | Platform implementation |
| [Trancendos/trancendos-ecosystem](https://github.com/Trancendos/trancendos-ecosystem) | Ecosystem CI/CD and security infra |
| **Trancendos/Magna-Carta** (this repo) | Foundation documentation framework |

---

## 12. Maintenance

| Action | Frequency | Responsible |
|--------|-----------|-------------|
| DEFSTAN register review | Quarterly | Platform Engineering |
| Magna Carta policy review | Annual | ISMS Lead |
| SOA / SOC2 mapping update | Quarterly | ISMS Lead |
| Architecture as-built refresh | On major release | Architecture Lead |
| Legislation register scan | Quarterly | Legal / DPO |
| Penetration test | Annual | Security Ops |

**Next Magna Carta review:** 2026-09-06
