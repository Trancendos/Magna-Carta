# As-Built Architecture (Canonical Reference)

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Platform Engineering  
**Status:** AUTHORITATIVE for audits, incident response, and compliance evidence  
**Supersedes for operational truth:** Tranc3 `docs/DOC-02-System-Architecture.md` (aspirational)

---

## 1. Deployment model

| Attribute | Value |
|-----------|-------|
| Hosting | Self-hosted (customer or Trancendos-operated) |
| Orchestration | Docker Compose (primary) / Kubernetes (supported) |
| Ingress | Traefik reverse proxy |
| Application runtime | Python 3.11+ / FastAPI |
| Worker count | ~55 FastAPI microservices |
| Primary datastore | SQLite per service (AES-GCM encrypted) |
| Secrets | OpenBao / Infinity Void / vault-service (port 8038) |
| CI/CD | Forgejo (self-hosted) |
| Observability | Prometheus, Grafana, Loki |
| SCM | Forgejo Git |

---

## 2. Trust boundaries (as-deployed)

```
INTERNET (untrusted)
    │
    ▼
┌─────────────────┐
│ Traefik         │  TLS 1.2+, routing, rate limit headers
│ :443 / :80→443  │
└────────┬────────┘
         │
    DOCKER BRIDGE NETWORK (semi-trusted)
         │
    ┌────┴────┬────────────┬──────────────┐
    ▼         ▼            ▼              ▼
  api.py   workers     platform-svc    observability
         (8004-80xx)  vault, audit    prom, grafana
         │
    PERSISTENCE (trusted)
    SQLite volumes · vault data · log storage
```

---

## 3. Service inventory (priority tiers)

### P0 — Critical path

| Service | Port | Function |
|---------|------|----------|
| infinity-ws | 8004 | WebSocket real-time (The Nexus) |
| infinity-auth | 8005 | Authentication, JWT, MFA |

### P1 — Core platform

| Service | Port | Function |
|---------|------|----------|
| users-service | 8006 | Users, profiles, DSR |
| monitoring | 8007 | Health, metrics (The Observatory) |
| notifications | 8008 | Email/push notifications |
| infinity-ai | 8009 | AI inference routing |
| tranc3-ai | — | AI worker processes |

### P2 — Business domain

| Service | Port | Function |
|---------|------|----------|
| the-grid | 8010 | Digital grid / spatial |
| products-service | 8011 | Product catalogue |
| orders-service | 8012 | Order management |
| payments-service | 8013 | Payment orchestration |
| files-service | 8014 | File storage |
| identity-service | 8015 | Extended identity |

### Infrastructure

| Service | Port | Function |
|---------|------|----------|
| vault-service | 8038 | Secrets management |
| rate-limit-service | 8026 | Token-bucket rate limiting |
| queue-service | — | Async job queue |
| ledger-service | — | Audit ledger |
| Forgejo | — | Git + CI/CD |
| MCP Server | — | Agent tooling (The Spark) |

*Full worker list: Tranc3 `workers/` directory and `docker-compose.production.yml`.*

---

## 4. Main application entry

| File | Role |
|------|------|
| `api.py` | FastAPI application; imports Magna Carta compliance singleton |
| `src/compliance/magna_carta.py` | Runtime compliance hooks (config-driven) |
| `Dimensional/middleware/` | Telemetry, rate limit, auth middleware |
| `src/auth/zero_trust.py` | Zero Trust IAM |
| `src/validation/loop_validator.py` | AI cascade / loop prevention |

**Environment variables (compliance):**

```bash
MAGNA_CARTA_ENABLED=true|false
MAGNA_CARTA_CONFIG_PATH=./config/magna_carta_config.json
```

---

## 5. Data stores (as-built)

| Store | Technology | Location | Encryption |
|-------|------------|----------|------------|
| Per-service DB | SQLite | Docker volume per worker | AES-GCM |
| Secrets | Vault / Void | Isolated volume | AES-GCM, PBKDF2 |
| Files | Local FS / IPFS cache | Docker volume | FS-level |
| Metrics | Prometheus TSDB | `/prometheus` volume | Disk encryption recommended |
| Logs | Loki | `/loki` volume | Disk encryption recommended |

**No shared database** between workers — integration via HTTP APIs only.

---

## 6. Security controls (implemented)

| Control | Implementation | Verified by |
|---------|----------------|-------------|
| Authentication | JWT + API key + Zero Trust | `test_zero_trust.py` |
| Authorisation | RBAC per route | Penetration tests |
| Encryption transit | Traefik TLS | Inspection |
| Encryption rest | SQLite AES-GCM | Code review |
| Secrets | vault-service; no VCS secrets | Gitleaks CI |
| Input validation | Pydantic v2 | `test_validation.py` |
| Rate limiting | rate-limit-service + middleware | `test_compliance.py` |
| Audit logging | Audit worker + structured logs | REQ-IA-006 |
| Vulnerability scan | pip-audit, Bandit, Semgrep, Trivy | CI pipeline |
| Malware / content scan | Ice Box module | Security review |

---

## 7. CI/CD pipeline (as-built)

```
git push → Forgejo webhook
    → lint (ruff, mypy)
    → security scan (bandit, semgrep, gitleaks, trivy)
    → unit + integration tests
    → compliance checker (register.yaml ≥70%)
    → build Docker images
    → deploy (environment-specific)
```

Change control: PROC-CHG-001; CAB for production.

---

## 8. Network exposure

| Exposure | Default |
|----------|---------|
| Public internet | Traefik only (443) |
| Worker ports | Internal Docker network only |
| Admin UIs (Grafana, Forgejo) | VPN or IP allowlist required |
| Database files | Never exposed |

---

## 9. Known architectural deltas

| Topic | As-built | Aspirational doc (DOC-02) | Action |
|-------|----------|---------------------------|--------|
| Database | SQLite per worker | PostgreSQL cluster | Label DOC-02 as target |
| Vector store | Local / optional | Pinecone | Not production |
| Cloud | Self-hosted | GKE/AKS/EKS multi-cloud | Future phase |
| Magna Carta | Config-ready placeholder | Full enforcement | Enable with this repo's config |

---

## 10. Evidence for auditors

| Question | Answer location |
|----------|-----------------|
| What is deployed? | This document + `docker-compose.production.yml` |
| How is auth enforced? | `src/auth/`, penetration test report |
| Where are secrets? | vault-service; Gitleaks clean |
| How is compliance measured? | `compliance/register.yaml`, CI logs |
| Threat model? | Tranc3 `ARCHITECTURE_THREAT_MODEL.md` |

---

## 11. Maintenance

Update this document when:
- New worker added or port changed
- Persistence technology changes
- Ingress or TLS configuration changes
- Magna Carta runtime enabled in production

**Last verified against Tranc3:** 2026-06-07  
**Next review:** On next major release (semver minor+)
