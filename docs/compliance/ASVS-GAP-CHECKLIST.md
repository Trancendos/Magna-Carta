# OWASP ASVS Level 2 Gap Checklist

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** Security Ops  
**Standard:** STANDARDS-REGISTER STD-008 (OWASP ASVS L2 — Partial)  
**Procedure:** PROC-VUL-001

---

## 1. Purpose

Structured gap assessment against [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) Level 2. Supports pen-test preparation (ACT-005) and ISO 27001 control evidence. **Not** a certification claim — internal readiness tracker.

**Legend:** ✅ Implemented · ⚠️ Partial · 📋 Planned · ❌ Gap · N/A Not applicable

---

## 2. V1 — Architecture, design, and threat modelling

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V1.1 | Secure SDLC documented | ✅ | FRAMEWORK, PROC-CHG-001 |
| V1.2 | Authentication architecture | ✅ | infinity-auth, POL-SEC-002 |
| V1.4 | Access control architecture | ✅ | JWT, RBAC in Tranc3 |
| V1.5 | Input and output architecture | ⚠️ | DEFSTAN; per-service validation |
| V1.14 | Configuration integrity | ✅ | Git + Forgejo SYS-010 |

---

## 3. V2 — Authentication

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V2.1 | Password security | ✅ | Auth service policies |
| V2.2 | General authenticator security | ✅ | MFA available |
| V2.7 | Session management | ✅ | JWT expiry, refresh |
| V2.8 | Single factor | N/A | MFA encouraged |

---

## 4. V3 — Session management

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V3.1 | Fundamental session | ✅ | Server-side session invalidation |
| V3.3 | Session timeout | ⚠️ | Verify per-client timeouts |
| V3.4 | Cookie-based sessions | ✅ | Secure, HttpOnly flags |

---

## 5. V4 — Access control

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V4.1 | General access control | ✅ | PROC-IAM-001 |
| V4.2 | Operation level access | ⚠️ | Service-level review quarterly |
| V4.3 | Other access control | 📋 | Document admin break-glass |

---

## 6. V5 — Validation, sanitisation, encoding

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V5.1 | Input validation | ⚠️ | DEFSTAN lint; expand coverage |
| V5.2 | Sanitisation and sandboxing | ⚠️ | AI prompt boundaries POL-AI-001 |
| V5.3 | Output encoding | ⚠️ | Framework defaults |

---

## 7. V7 — Error handling and logging

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V7.1 | Log content | ✅ | SYS-006 audit-service |
| V7.2 | Log processing | ✅ | Loki SYS-032 |
| V7.4 | Error handling | ⚠️ | No stack traces to users — verify |

---

## 8. V8 — Data protection

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V8.1 | General data protection | ✅ | Encryption at rest/transit |
| V8.2 | Client-side data | ⚠️ | Local storage audit |
| V8.3 | Sensitive private data | ✅ | Vault SYS-005 |

---

## 9. V9 — Communications

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V9.1 | Client communication | ✅ | TLS 1.2+ Traefik |
| V9.2 | Server communication | ✅ | mTLS internal where configured |

---

## 10. V10 — Malicious code

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V10.1 | Code integrity | ✅ | SCM, signed commits policy |
| V10.2 | Malicious code search | ⚠️ | Dependency scanning — expand |

---

## 11. V11 — Business logic

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V11.1 | Business logic security | ⚠️ | Per-feature review in CAB |

---

## 12. V12 — Files and resources

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V12.1 | File upload | ⚠️ | files-service limits |
| V12.4 | ZIP bombs / size | 📋 | Add explicit tests |

---

## 13. V13 — API and web service

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V13.1 | Generic web service | ✅ | OpenAPI + auth |
| V13.2 | RESTful Web Service | ⚠️ | Rate limits Traefik |
| V13.4 | GraphQL | N/A | Not in scope |

---

## 14. V14 — Configuration

| ASVS | Control | Status | Evidence / notes |
|------|---------|--------|------------------|
| V14.1 | Build and deploy | ✅ | Forgejo CI |
| V14.2 | Dependency | ⚠️ | Supply chain programme |
| V14.5 | HTTP security headers | ⚠️ | Verify CSP/HSTS on all routes |

---

## 15. Summary and actions

| Metric | Count |
|--------|-------|
| ✅ Implemented | 22 |
| ⚠️ Partial | 14 |
| 📋 Planned | 2 |
| ❌ Gap | 0 |

**Priority gaps for ACT-005 pen test:**

1. V5 input validation coverage across all public APIs  
2. V14.5 security headers consistency  
3. V10.2 dependency / SCA automation  

Update after each pen test and annually. Owner: Security Ops.

**Next review:** 2026-09-06
