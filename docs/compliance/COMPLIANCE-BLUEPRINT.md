# Compliance Blueprint — Operating Model

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead

---

## 1. Purpose

This blueprint defines **how Trancendos achieves and demonstrates compliance** across regulations, standards, and internal policies. It is the operational companion to [FRAMEWORK.md](../../FRAMEWORK.md).

---

## 2. Compliance domains

```
┌────────────────────────────────────────────────────────────┐
│                    GOVERNANCE LAYER                         │
│  Magna Carta · Town Hall · BoardRoom · Policies            │
└─────────────────────────┬──────────────────────────────────┘
                          │
     ┌────────────────────┼────────────────────┐
     │                    │                    │
┌────▼─────┐      ┌───────▼───────┐    ┌──────▼──────┐
│ PRIVACY  │      │  SECURITY     │    │  OPERATIONS │
│ GDPR     │      │  ISO/SOC2     │    │  ITIL/CAB   │
│ ROPA/PIA │      │  OWASP/ZT     │    │  BCP/DR     │
└────┬─────┘      └───────┬───────┘    └──────┬──────┘
     │                    │                    │
     └────────────────────┼────────────────────┘
                          │
┌─────────────────────────▼──────────────────────────────────┐
│              TECHNICAL CONTROL LAYER (Tranc3)               │
│  Auth · Vault · Audit · Ice Box · Encrypted DB · CI/CD     │
└─────────────────────────┬──────────────────────────────────┘
                          │
┌─────────────────────────▼──────────────────────────────────┐
│              EVIDENCE LAYER                                 │
│  register.yaml · tests · logs · SOC2 collector · audits      │
└────────────────────────────────────────────────────────────┘
```

---

## 3. Roles

| Role | Responsibilities |
|------|------------------|
| **ISMS Lead** | SOA maintenance, audit liaison, risk register, compliance score |
| **DPO** | ROPA, PIA, DSR oversight, ICO liaison, privacy impact on changes |
| **CISO / Security Lead** | Threat model, pen test, vuln mgmt, Ice Box policy |
| **CAB Chair** | Change classification, approval workflow, emergency changes |
| **Engineering Lead** | Control implementation, evidence in code/tests |
| **AI Lead** | Model cards, AI risk classification, bias testing |

---

## 4. Control families

### 4.1 Preventive controls

- Zero Trust IAM (MFA, device posture, JWT revocation)
- Input validation (Pydantic v2, sanitisation)
- Rate limiting (per-tenant, per-IP)
- Secrets vault (Infinity Void / OpenBao)
- CI security gates (Bandit, Semgrep, Gitleaks, Trivy)
- Magna Carta request rules (when enabled)

### 4.2 Detective controls

- Observatory structured logging
- Audit service append-only trail
- Prometheus alerts + Grafana dashboards
- Dependency audit (weekly pip-audit)
- DEFSTAN compliance checker (on-demand + CI)
- Ice Box static analysis (content threats)

### 4.3 Corrective controls

- Incident response procedure (WarRoom)
- Vulnerability remediation SLAs
- Waiver register with compensating controls
- DR restore (`scripts/dr_restore.py`)
- Key rotation (`src/security/key_rotation.py`)

### 4.4 Compensating controls

Documented in `compliance/waivers.yaml` (Tranc3). All current waivers: **RESOLVED**.

---

## 5. Evidence catalogue

| Evidence type | Location | Retention |
|---------------|----------|-----------|
| Control register | Tranc3 `compliance/register.yaml` | Permanent (versioned) |
| Magna Carta extensions | `compliance/magna_carta_register.yaml` | Permanent |
| Test traceability | Tranc3 `compliance/test_evidence.yaml` | Permanent |
| Audit logs | Observatory SQLite | 90 days |
| Application logs | Loki | 30 days |
| CI scan results | Forgejo workflow artefacts | 12 months |
| SOC 2 evidence packs | `scripts/soc2_evidence_collector.py` output | 12 months |
| Policy versions | This repo (git history) | Permanent |
| Pen test reports | Secure storage (planned) | 3 years |

---

## 6. Compliance calendar

| Month | Activity |
|-------|----------|
| Every sprint | Dependency audit, security-scan CI |
| Monthly | SOC 2 evidence collection, compliance checker report |
| Quarterly | DEFSTAN + Magna Carta review, risk register update, DR drill |
| Semi-annual | AI governance review, policy review (AI ethics) |
| Annual | Penetration test, full policy review, management review |
| 2026 Q4 | External security assessment |
| 2027 Q1 | SOC 2 Type II report |
| 2027 Q2 | ISO 27001 certification audit |

---

## 7. Compliance APIs (Tranc3)

| Endpoint | Use |
|----------|-----|
| `GET /compliance/status` | Live score and summary |
| `GET /compliance/report` | Full JSON report |
| `GET /compliance/matrix` | Traceability matrix |
| `GET /townhall/policies` | Policy registry |
| `POST /townhall/check` | Governance compliance check |

---

## 8. Gap remediation priorities

| Priority | Gap | Action | Owner | Target |
|----------|-----|--------|-------|--------|
| P1 | AUP not published | POL-SEC-002 in this repo → BoardRoom approval | ISMS | Q3 2026 |
| P1 | BCP not exercised | PROC-BCP-001 + quarterly drill | Ops | Q3 2026 |
| P1 | Supplier DPAs incomplete | DPA register + Fly.io/CF DPAs | Legal | Q3 2026 |
| P2 | RACI / SoD matrix | Formalise in ISMS docs | ISMS | Q4 2026 |
| P2 | AI bias metrics | Implement fairness test suite | AI Lead | Q4 2026 |
| P2 | HIPAA marketing claims | Remove or build HIPAA scope | Product | Q3 2026 |
| P3 | ISO 42001 cert | AI MS programme | AI Lead | 2027 |

---

## 9. Audit readiness checklist

- [ ] Canonical architecture doc agreed (AS-BUILT)
- [ ] All policies BoardRoom-approved
- [ ] RACI matrix published
- [ ] Legislation register current
- [ ] ROPA and PIA reviewed within 12 months
- [ ] DEFSTAN score ≥70% (CI enforced)
- [ ] SOC 2 evidence window complete (6 months)
- [ ] Pen test report available
- [ ] DR drill log within 12 months
- [ ] Supplier DPA register complete
- [ ] Magna Carta enabled in production staging

---

## 10. Monitoring vs audit

Compliance assurance uses two complementary modes (aligned with NGX compliance programme practice):

| Mode | When | Who | Examples in Tranc3 |
|------|------|-----|-------------------|
| **Monitoring** | Continuous or near-real-time, within operational line | Service owners, automated checks | DEFSTAN CI gate, `GET /compliance/status`, quarterly PROC-CMP-001 reviews, access reviews |
| **Audit** | Periodic, independent of day-to-day operations | ISMS lead, external auditor | ISO/SOC2 evidence packs, pen test reports, policy attestation cycles |

**Design rule:** Monitoring catches drift early; audit verifies that monitoring and controls are effective. Operational management must not override independent audit findings.

Obligations tracking: [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)  
Procedure: [PROC-CMP-001-Compliance-Review.md](../procedures/PROC-CMP-001-Compliance-Review.md)

---

## 11. References

- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
- [ISO27001-ALIGNMENT.md](ISO27001-ALIGNMENT.md)
- [SOC2-ALIGNMENT.md](SOC2-ALIGNMENT.md)
- [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md)
- [DEFSTAN-ALIGNMENT.md](DEFSTAN-ALIGNMENT.md)
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md)
- [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md)
- [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md)
- [GENAI-MATURITY-ASSESSMENT.md](GENAI-MATURITY-ASSESSMENT.md)
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)
