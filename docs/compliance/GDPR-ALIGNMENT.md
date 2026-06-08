# UK GDPR / EU GDPR Alignment

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Data Protection Officer (DPO)  
**Scope:** Tranc3 platform and Trancendos-operated processing activities  
**Certification context:** Supports ISO 27001 A.5.34 and SOC 2 Privacy criteria

---

## 1. Scope and lawful basis

| Processing activity | Lawful basis | Data categories | Retention |
|---------------------|--------------|-----------------|-----------|
| User account management | Contract (Art. 6(1)(b)) | Identity, contact, credentials | Account lifetime + 90 days |
| Authentication & security logs | Legitimate interest (Art. 6(1)(f)) | IP, device, session metadata | 90 days default |
| AI inference & model interaction | Contract / consent | Prompts, outputs, usage metadata | Per tenant policy; 90-day audit default |
| Billing & subscriptions | Contract | Payment references (no CHD) | 7 years (financial) |
| Marketing communications | Consent (Art. 6(1)(a)) | Email, preferences | Until withdrawal |
| Compliance audit logs | Legal obligation / legitimate interest | Event metadata | 90 days–1 year |

**Records of Processing Activities (ROPA):** Maintained in Tranc3 compliance module; Magna Carta references this document and [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md).

---

## 2. Data subject rights (DSR)

| Right | Article | Tranc3 implementation | Magna Carta procedure |
|-------|---------|----------------------|---------------------|
| Access | Art. 15 | `users-service` export API | PROC-DSR-001 |
| Rectification | Art. 16 | Profile update endpoints | PROC-DSR-001 |
| Erasure | Art. 17 | Account deletion workflow | PROC-DSR-001 |
| Restriction | Art. 18 | Manual flag + processing pause | PROC-DSR-001 |
| Portability | Art. 20 | JSON export | PROC-DSR-001 |
| Objection | Art. 21 | Marketing opt-out; processing review | PROC-DSR-001 |
| Automated decisions | Art. 22 | Model cards; human review for high-risk | POL-AI-001 |

**SLA:** Acknowledge within 72 hours; fulfil within 30 days (extendable to 90 with notice).

---

## 3. Privacy by design and default

| Principle | Implementation |
|-----------|----------------|
| Data minimisation | Pydantic schemas; optional fields; no unnecessary PII in logs (`Dimensional/sanitize.py`) |
| Purpose limitation | ROPA defines purposes; Magna Carta config blocks cross-purpose use without basis |
| Storage limitation | 90-day audit retention; tenant-configurable AI history |
| Integrity & confidentiality | AES-GCM SQLite encryption; TLS 1.2+; vault for secrets |
| Accountability | Append-only audit; DPO review; PIA for new features |

**Privacy Impact Assessment (PIA):** Required for new processing involving special category data, large-scale profiling, or systematic monitoring.

---

## 4. International transfers

| Scenario | Mechanism | Status |
|----------|-----------|--------|
| UK-only hosting | No transfer | ✅ Default self-hosted |
| EU hosting | Adequacy / UK extension | ✅ If EU region selected |
| US AI fallback (if enabled) | SCCs + transfer impact assessment | ⚠️ Document in ROPA before enable |
| Sub-processors | DPA + Article 28 terms | ✅ Programme — [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md); signed DPAs 🎯 |

**Rule:** No transfer to inadequate country without documented safeguards and DPO approval.

---

## 5. Breach notification

| Step | Timeline | Owner |
|------|----------|-------|
| Detect & contain | Immediate | Security Ops |
| Assess risk to rights/freedoms | Within 24 hours | DPO + ISMS Lead |
| Notify ICO (if required) | Within 72 hours of awareness | DPO |
| Notify data subjects (if high risk) | Without undue delay | DPO + Communications |
| Document | Within 5 business days | DPO |

Linked procedure: [PROC-IR-001](../procedures/PROC-IR-001-Incident-Response.md)

---

## 6. Controller / processor roles

| Role | Entity | Responsibility |
|------|--------|----------------|
| Controller | Trancendos Ltd (for platform SaaS) | Determines purposes; DPO appointed |
| Processor | Trancendos (for customer data in multi-tenant) | Processes per customer instructions |
| Sub-processor | Documented suppliers only | [SUPPLIER-DPA-REGISTER.md](SUPPLIER-DPA-REGISTER.md), `compliance/supplier_dpa_register.yaml` |

Customer self-hosted deployments: Customer is controller; Trancendos provides software only.

---

## 7. Technical and organisational measures (TOMs)

| TOM | Tranc3 control | DEFSTAN ref |
|-----|----------------|-------------|
| Access control | Zero Trust IAM, MFA, RBAC | REQ-IA-001 |
| Encryption at rest | AES-GCM SQLite, vault | REQ-IA-002 |
| Encryption in transit | TLS via Traefik | REQ-IA-003 |
| Logging & monitoring | Audit service, Loki, Prometheus | REQ-IA-006 |
| Pseudonymisation | User IDs; no raw PII in metrics | REQ-IA-004 |
| Backup & recovery | PROC-BCP-001 | REQ-OPS-003 |

---

## 8. Gap register

| Gap | Priority | Remediation | Target |
|-----|----------|-------------|--------|
| Formal cookie consent UI | Medium | Implement if marketing cookies deployed | Q3 2026 |
| CCPA-specific disclosures | Low | Extend privacy policy if CA users material | TBD |
| Automated DSR SLA dashboard | Medium | Monitoring alert on DSR queue age | Q4 2026 |
| DPIA template for AI features | High | Publish template; require for new models | Q3 2026 |

---

## 9. Evidence locations

| Artefact | Location |
|----------|----------|
| ROPA | Tranc3 `docs/compliance/` (operational) |
| PIA records | Town Hall compliance room |
| DSR log | `users-service` + ticketing |
| Breach register | Incident management system |
| Privacy policy | Public website / tenant portal |
| Magna Carta privacy policy | [POL-PRI-001](../policies/POL-PRI-001-Data-Protection-Privacy.md) |

---

## 10. Review

| Activity | Frequency | Owner |
|----------|-----------|-------|
| ROPA update | On processing change | DPO |
| Privacy policy review | Annual | DPO + Legal |
| Transfer mechanism review | Annual | DPO |
| DSR metrics review | Quarterly | DPO |

**Next review:** 2026-09-07
