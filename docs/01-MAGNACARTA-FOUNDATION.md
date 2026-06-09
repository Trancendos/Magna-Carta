# Magna Carta Foundation — Digital Rights & Governance

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Trancendos Governance (Town Hall / BoardRoom)  
**Status:** Active

---

## 1. Charter

The **Infinity Network — Magna Carta** establishes the constitutional layer for digital products built on Trancendos Universe and deployed as Infinity Network applications. It defines non-negotiable rights for users, obligations for operators, and governance mechanics for the organisation.

It is registered in Town Hall as framework `magna-carta` (status: **active**) alongside governance-core, GDPR, security-framework, and blueprint documentation domains.

---

## 2. Digital bill of rights

### Article I — Right to know

Users have the right to understand what personal data is collected, the lawful basis, retention period, and subprocessors involved. This is fulfilled through:

- Privacy notices at collection points
- [ROPA](https://github.com/Trancendos/Tranc3/blob/main/docs/privacy/ROPA.md) (maintained in Tranc3)
- Model cards for AI processing

### Article II — Right to control

Users may access, rectify, erase, restrict, and port their data. Fulfilled through:

- `users-service` GDPR endpoints (SAR, erasure, consent)
- [PROC-DSR-001](procedures/data-subject-request-procedure.md)

### Article III — Right to security

User data must be protected with industry-appropriate technical and organisational measures:

- Zero Trust authentication (MFA, device posture)
- Encryption at rest (AES-GCM) and in transit (TLS 1.2+)
- Secrets in vault only — never in source code

### Article IV — Right to human oversight

Automated decisions with legal or similarly significant effects require human review. High-risk AI use cases must be classified per EU AI Act tiers and gated accordingly.

### Article V — Right to proportionality

Data collection and retention must be limited to stated purposes. Default audit log retention: **90 days** unless law or contract requires longer.

### Article VI — Right to remedy

Security and privacy incidents must be handled per [POL-OPS-001](policies/incident-response-policy.md) with notification timelines aligned to UK GDPR (72 hours to ICO where required).

### Article VII — Right to sovereignty

The platform must remain deployable on operator-controlled infrastructure without mandatory paid third-party processors (Zero-Cost Mandate). External services require documented risk acceptance.

---

## 3. Operator obligations

| Obligation | Mechanism |
|------------|-----------|
| Maintain ISMS | ISO 27001 SOA, annual review |
| Protect PII | Data Protection Policy, encryption, access control |
| Log security events | Observatory + audit-service |
| Control changes | CAB + change management policy |
| Test resilience | DR runbooks, quarterly restore drill |
| Train personnel | Security awareness (planned: The Academy LMS) |
| Report incidents | WarRoom activation, IR procedure |
| Demonstrate compliance | DEFSTAN checker, SOC2 evidence, external audit |

---

## 4. Governance structure

```
                    ┌─────────────┐
                    │  BoardRoom  │  Executive / policy approval
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼─────┐ ┌────▼────┐ ┌─────▼─────┐
       │    CAB     │ │ WarRoom │ │ Meetings  │
       │  Changes   │ │ P0 Inc  │ │ Reviews   │
       └──────┬─────┘ └────┬────┘ └─────┬─────┘
              │            │            │
              └────────────┼────────────┘
                           │
                    ┌──────▼──────┐
                    │  Town Hall  │  Framework registry, templates, Kanban
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Tranc3    │  Implementation + compliance APIs
                    └─────────────┘
```

---

## 5. Integration with Tranc3 Town Hall

| API | Magna Carta use |
|-----|-----------------|
| `GET /townhall/frameworks` | Verify magna-carta status active |
| `GET /townhall/policies` | List registered policies |
| `POST /townhall/check` | Zero-cost and governance checks |
| `POST /townhall/rooms/war-room/sessions` | P0 incident activation |
| `POST /townhall/rooms/board-room/sessions` | Policy approval sessions |

---

## 6. Relationship to DEFSTAN

DEFSTAN provides **operational rigour** (53 traceable requirements). Magna Carta provides **governance intent** (rights, policies, regulatory alignment). Every Magna Carta policy maps to one or more `REQ-*` entries in `compliance/register.yaml`.

---

## 7. Enforcement

| Layer | Enforcement |
|-------|-------------|
| Policy | HR / contractor agreements, access revocation |
| Technical | Zero Trust IAM, RBAC, Ice Box, rate limits |
| Automated | `magna_carta.py` request checks when enabled |
| CI/CD | DEFSTAN compliance gate ≥70%, security-scan workflow |
| Audit | Quarterly review, external certification |

---

## 8. Review

- **Owner:** BoardRoom / ISMS Lead
- **Frequency:** Annual policy review; quarterly control alignment check
- **Next review:** 2026-09-06
