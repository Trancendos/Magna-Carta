# Architecture Blueprint

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Architecture Lead  
**Classification:** Internal — Engineering & Audit  
**Canonical as-built:** [AS-BUILT-ARCHITECTURE.md](AS-BUILT-ARCHITECTURE.md)

---

## 1. Blueprint purpose

This document defines the **target operating architecture** for Tranc3 under the Magna Carta Framework. It bridges governance requirements (Layers 1–4) to deployable components (Layer 5).

**Precedence:** If this blueprint conflicts with [AS-BUILT-ARCHITECTURE.md](AS-BUILT-ARCHITECTURE.md), the as-built document wins for audits and incident response.

---

## 2. Architectural principles

| Principle | Description | Compliance driver |
|-----------|-------------|-------------------|
| Self-hosted first | No mandatory paid third-party APIs | Magna Carta zero-cost sovereignty |
| Defence in depth | Edge → app → data → ops controls | ISO 27001, DEFSTAN 00-700 |
| Service isolation | One worker per domain; SQLite per service | Blast radius containment |
| Zero Trust IAM | Verify every request; MFA; device posture | REQ-IA-001 |
| Observable by default | Metrics, logs, traces on all P0/P1 | REQ-OPS-001 |
| Compliance as code | Register in CI; Magna Carta config at runtime | Layer 6 evidence |

---

## 3. Logical architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CLIENTS & INTEGRATIONS                           │
│   Web UI · Mobile · MCP · Webhooks · External APIs                      │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │ HTTPS (TLS 1.2+)
┌───────────────────────────────────▼─────────────────────────────────────┐
│                         EDGE & INGRESS LAYER                             │
│   Traefik — TLS termination · routing · rate limit · optional WAF       │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────┐
│                      API GATEWAY / MAIN APPLICATION                      │
│   api.py — FastAPI · middleware stack · Magna Carta compliance hook    │
│   Dimensional/middleware — telemetry · rate limit · auth                  │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │ Docker internal network
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
┌───────▼────────┐         ┌────────▼────────┐        ┌────────▼────────┐
│  P0 SERVICES   │         │  P1 SERVICES    │        │  P2 SERVICES    │
│  infinity-ws   │         │  users          │        │  orders         │
│  infinity-auth │         │  monitoring     │        │  payments       │
│                │         │  notifications  │        │  files          │
│                │         │  infinity-ai    │        │  the-grid       │
└───────┬────────┘         └────────┬────────┘        └────────┬────────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────┐
│                      PLATFORM & SECURITY SERVICES                        │
│   vault-service · rate-limit-service · audit · ice-box · queue-service   │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────┐
│                      PERSISTENCE & OBSERVABILITY                           │
│   SQLite (AES-GCM) · Infinity Void · Prometheus · Grafana · Loki         │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼─────────────────────────────────────┐
│                      DEVOPS & GOVERNANCE                                   │
│   Forgejo CI/CD · compliance checker · Town Hall · MCP tooling           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Security zones

| Zone | Trust level | Controls |
|------|-------------|----------|
| Internet | Untrusted | TLS only; rate limits; no direct DB access |
| Edge (Traefik) | DMZ | Cert management; routing; optional IP allowlist |
| Application network | Semi-trusted | JWT auth; service isolation; internal DNS |
| Persistence | Trusted | Encryption; least-privilege file access |
| Admin / CI | Privileged | MFA; separate credentials; audit all actions |

---

## 5. Data architecture

| Data class | Store | Encryption | Backup |
|------------|-------|------------|--------|
| User PII | users-service SQLite | AES-GCM | Daily encrypted backup |
| Credentials / secrets | vault-service, Infinity Void | AES-GCM, PBKDF2 | Replicated vault backup |
| Audit events | audit worker / Loki | At rest encryption | 90-day retention |
| AI prompts/outputs | infinity-ai SQLite | AES-GCM | Tenant policy |
| Files | files-service volume | Volume encryption | PROC-BCP-001 |
| Metrics | Prometheus TSDB | Local disk | 30-day retention |

**Data flow rule:** PII must not appear in application logs; use `Dimensional/sanitize.py`.

---

## 6. Identity and access blueprint

```
User → infinity-auth (JWT issue)
     → Zero Trust evaluation (device, geo, risk score)
     → MFA challenge (if policy requires)
     → RBAC scope on worker endpoint
     → Audit log event
```

| Component | Path | Standard |
|-----------|------|----------|
| Zero Trust IAM | `src/auth/zero_trust.py` | REQ-IA-001 |
| FastAPI deps | `src/auth/dependencies.py` | REQ-IA-001 |
| API keys | `Dimensional/middleware/auth.py` | REQ-IA-001 |
| Vault secrets | `workers/vault-service/` | REQ-IA-002 |

---

## 7. AI architecture blueprint

| Layer | Component | Governance |
|-------|-----------|------------|
| Routing | infinity-ai, tranc3-ai workers | Model registry |
| Safety | `loop_validator.py`, Ice Box | Cascade prevention |
| Compliance | `ai_governance.py`, `magna_carta.py` | Runtime rules |
| Observability | Model cards API, incident log | EU AI Act Art. 13 |

**External LLM fallback:** Optional; requires DPA, SCCs, and Town Hall zero-cost exception approval.

---

## 8. Deployment topologies

### 8.1 Reference (production)

- Single-region Docker Compose or K8s cluster
- Traefik ingress with Let's Encrypt or org CA
- Forgejo on same or adjacent host
- Prometheus + Grafana + Loki stack

### 8.2 Development

- Reduced worker set; `MAGNA_CARTA_ENABLED=false`
- Local SQLite; mock vault

### 8.3 Aspirational (not as-built)

Tranc3 `DOC-02-System-Architecture.md` describes multi-cloud (GKE/AKS/EKS), PostgreSQL, Pinecone. **Do not use for compliance evidence** until migrated and as-built doc updated.

---

## 9. Non-functional requirements

| NFR | P0 | P1 | P2 |
|-----|----|----|-----|
| Availability | 99.9% | 99.5% | 99.0% |
| RTO | 1 hour | 4 hours | 24 hours |
| RPO | 15 min | 1 hour | 24 hours |
| Max concurrent WS | 1000 | — | — |

---

## 10. Evolution roadmap

| Phase | Change | Compliance impact |
|-------|--------|-------------------|
| Current | Self-hosted SQLite workers | DEFSTAN strong |
| H1 2027 | ISO 27001 certification | SOA formalised |
| H1 2027 | SOC 2 Type II | Evidence collector mature |
| Future | Optional PostgreSQL for scale | Schema migration plan required |
| Future | Wazuh SIEM | REQ-OPS-002 closure |

---

## 11. Related documents

- [AS-BUILT-ARCHITECTURE.md](AS-BUILT-ARCHITECTURE.md)
- [CONTROL-TO-COMPONENT-MAP.md](CONTROL-TO-COMPONENT-MAP.md)
- Tranc3 `ARCHITECTURE_THREAT_MODEL.md`
- [FRAMEWORK.md](../../FRAMEWORK.md) §6
