# HIPAA Alignment Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** DPO / CISO  
**Scope:** US health information boundary within Tranc3 (wellbeing / biometric sync features)  
**Certification context:** Programme implemented; formal BAA and third-party HIPAA attestation on customer onboarding path

---

## 1. Applicability and regulatory perimeter

| Question | Trancendos position |
|----------|---------------------|
| Is Trancendos a **Covered Entity** (CE)? | **No** — not a healthcare provider, health plan, or healthcare clearinghouse |
| Is Trancendos a **Business Associate** (BA)? | **Yes, when scoped** — when processing PHI on behalf of a CE or another BA under a BAA |
| Does HIPAA apply to EU/UK health data? | **No** — UK GDPR / special category data rules apply instead (see [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md)) |
| When is HIPAA in scope? | US persons' PHI processed via Tranc3 health integrations (e.g. Sync-Bot / wellbeing tier) |

**In-scope Tranc3 features (Tranc3 source of truth):**

| Feature | ID | Description | HIPAA relevance |
|---------|-----|-------------|-----------------|
| Sync-Bot | `NID-TMR-01` | Pulls data from health platforms with encryption | PHI ingestion if US health apps |
| Wellbeing tier | Tier 5 | Biometric sync, health data ingestion | PHI processing boundary |
| Platform copy | `src/entities/platform.py` | Marketing references HIPAA | Must match programme tier (§10) |

**Rule:** Do not claim "HIPAA compliant" in product copy unless the deployment is on the **HIPAA-enabled configuration profile** with signed BAA and evidence pack (§10).

---

## 2. HIPAA Security Rule — safeguard mapping

### 2.1 Administrative safeguards (45 CFR §164.308)

| Standard | Requirement | Tranc3 / Magna Carta control | Evidence |
|----------|-------------|------------------------------|----------|
| Security management process | Risk analysis & management | `RISK_REGISTER.md`, DEFSTAN register | `tranc3-repo/compliance/register.yaml` |
| Assigned security responsibility | Security officer | CISO role in [COMPLIANCE-BLUEPRINT.md](COMPLIANCE-BLUEPRINT.md) | FRAMEWORK §9 RACI |
| Workforce security | Access authorisation | PROC-IAM-001, RBAC | `infinity-auth`, JWT/MFA |
| Information access management | Minimum necessary | Ice Box, Pydantic schemas, log sanitisation | `Dimensional/sanitize.py` |
| Security awareness training | Workforce training | AI literacy + security awareness programme | PROC-CMP-001 calendar |
| Security incident procedures | IR workflow | PROC-IR-001, WarRoom | Observatory audit trail |
| Contingency plan | BCP/DR | PROC-BCP-001, `scripts/dr_restore.py` | DR runbook |
| Evaluation | Periodic evaluation | Quarterly PROC-CMP-001 | OBLIGATIONS-REGISTER |
| BA agreements | BAA with subcontractors | POL-SUP-001, BAA template | §4 |

### 2.2 Physical safeguards (45 CFR §164.310)

| Standard | Requirement | Implementation | Notes |
|----------|-------------|----------------|-------|
| Facility access controls | Limit physical access | Customer-controlled hosting (self-hosted default) | Tranc3 deploy model |
| Workstation use | Secure workstations | AUP POL-SEC-002, device posture (Zero Trust) | `zero_trust` evaluation |
| Device and media controls | Disposal / re-use | Encrypted volumes; secure wipe in DR procedure | PROC-BCP-001 |

### 2.3 Technical safeguards (45 CFR §164.312)

| Standard | Requirement | Tranc3 implementation | Status |
|----------|-------------|---------------------|--------|
| Access control | Unique user ID, emergency access, automatic logoff, encryption | JWT identity, MFA, session TTL, AES-GCM at rest | ✅ |
| Audit controls | Record PHI access | Append-only audit, MC-RULE-006 | ✅ |
| Integrity | PHI not improperly altered | Input validation, signed audit chain | ✅ |
| Person or entity authentication | Verify identity | Zero Trust IAM, MFA | ✅ |
| Transmission security | Encrypt in transit | TLS 1.2+ (Traefik), mTLS internal optional | ✅ |

---

## 3. HIPAA Privacy Rule (45 CFR §164.500–534)

| Obligation | Implementation |
|------------|----------------|
| Minimum necessary | Data minimisation in Sync-Bot connectors; field-level schemas |
| Individual rights (access, amendment, accounting) | PROC-DSR-001 extended for PHI export/delete |
| Notice of privacy practices | Customer-hosted privacy notice; template in POL-PRI-001 annex |
| Uses and disclosures | Purpose limitation in ROPA; BAA defines permitted uses |
| Administrative requirements | Privacy officer (DPO), workforce training, sanctions policy |

**UK/EU parallel:** Special category health data under UK GDPR Art. 9 uses the same technical controls; lawful basis and DPIA are documented separately in GDPR-ALIGNMENT.

---

## 4. Business Associate Agreements (BAA)

| Party type | BAA requirement | Magna Carta artefact |
|------------|-----------------|----------------------|
| Trancendos → CE customer | Required before PHI processing | BAA schedule (Legal template) |
| Trancendos → sub-processor | Required if sub-processor touches PHI | POL-SUP-001 + DPA with HIPAA clauses |
| CE customer → Trancendos | Customer warrants lawful collection | Customer agreement schedule |

**BAA minimum clauses:** permitted uses, safeguards, subcontractor flow-down, breach notification (without undue delay, max 60 days to CE), return/destruction of PHI, HHS access, termination.

**Sub-processor register (PHI-capable — review before enable):**

| Service | PHI default | Control |
|---------|-------------|---------|
| Self-hosted Tranc3 | No external PHI egress | Default profile |
| US AI fallback (if enabled) | **Blocked** on HIPAA profile | MC-RULE-005 exception denied |
| Third-party health APIs | Per integration DPIA | Town Hall approval |

---

## 5. Breach notification (HIPAA Breach Notification Rule)

| Step | HIPAA timeline | Owner | Magna Carta link |
|------|----------------|-------|------------------|
| Discover & contain | Immediate | Security Ops | PROC-IR-001 |
| Risk assessment (4-factor test) | Without unreasonable delay | DPO + Legal | IR playbook annex |
| Notify CE customer (BA) | Without unreasonable delay, ≤60 days | DPO | Customer notification template |
| CE notifies individuals/HHS | CE responsibility | Customer | Documented in BAA |
| Document | Retain 6 years | DPO | Incident register |

Concurrent UK GDPR Art. 33–34 process applies for UK data subjects (see GDPR-ALIGNMENT §5).

---

## 6. PHI technical control profile (HIPAA-enabled deployment)

When `HIPAA_PROFILE=enabled` (customer configuration):

| Control | Setting |
|---------|---------|
| Encryption at rest | AES-GCM mandatory; no unencrypted PHI stores |
| Encryption in transit | TLS 1.2+ only; HSTS enforced |
| Log redaction | PHI fields in `blocked_fields` (MC-RULE-002 extended) |
| Audit retention | Minimum 6 years for PHI access logs (customer policy) |
| Backup encryption | Encrypted backups; restore tested per PROC-BCP-001 |
| US region | US data residency required for US PHI |
| AI on PHI | Prohibited without explicit BAA schedule + human review |

**Runtime rule (Magna Carta):** MC-RULE-009 `health_data` — see [config/magna_carta_config.json](../../config/magna_carta_config.json).

---

## 7. Obligations cross-reference

| OBL-ID | Obligation | Status |
|--------|------------|--------|
| OBL-090 | HIPAA §164.312 technical safeguards | ✅ Programme |
| OBL-091 | HIPAA §164.308 administrative safeguards | ✅ Programme |
| OBL-092 | HIPAA §164.314 BA contract | ✅ Template + process |
| OBL-093 | HIPAA Breach Notification | ✅ PROC-IR-001 annex |
| OBL-094 | Marketing accuracy (no false HIPAA claims) | ✅ §10 policy |

Full register: [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md) §4.6.

---

## 8. Gap register (operational validation — not programme gaps)

| Item | Status | Target | Owner |
|------|--------|--------|-------|
| BAA template BoardRoom approval | Ready for sign-off | Q3 2026 | Legal |
| Sync-Bot connector DPIA (US health APIs) | Per-integration | On enable | DPO |
| PHI field taxonomy in Ice Box | Extend scanner rules | Q3 2026 | Security |
| Customer HIPAA evidence pack | SOC2-style collector extension | Q4 2026 | ISMS |
| Third-party HIPAA attestation audit | On first CE customer | Per contract | ISMS |

---

## 9. Evidence catalogue

| Artefact | Location |
|----------|----------|
| Control register (security baseline) | `tranc3-repo/compliance/register.yaml` |
| Encryption implementation | `tranc3-repo/src/security/`, vault workers |
| Audit logging | Observatory, audit service |
| Access control | `infinity-auth`, PROC-IAM-001 |
| AI prohibited uses (biometric) | `tranc3-repo/src/compliance/ai_governance.py` |
| Magna Carta health rule | `config/magna_carta_config.json` MC-RULE-009 |
| Register entry | `compliance/magna_carta_register.yaml` MC-008 |

---

## 10. Product and marketing alignment

**Problem identified (Tranc3):** `platform.py`, `id_registry.json`, and `docs/matrix.md` reference "HIPAA compliant" encryption for Sync-Bot without deployment-scoped qualification.

**Policy (effective immediately):**

| Claim tier | Allowed wording | Preconditions |
|------------|-----------------|---------------|
| **Tier A — Platform capability** | "Supports HIPAA-aligned controls when deployed on HIPAA profile with BAA" | This document + customer config |
| **Tier B — Deployment qualified** | "HIPAA-ready deployment" | BAA signed, HIPAA_PROFILE enabled, evidence pack |
| **Tier C — Full compliance claim** | "HIPAA compliant" | External assessment or customer attestation + all Tier B |

**Action:** Product copy must use Tier A or B until Tier C evidence exists. Remediation specification: [TRANC3-HIPAA-COPY-REMEDIATION.md](../engineering/TRANC3-HIPAA-COPY-REMEDIATION.md) (merge to Tranc3 repo; local mirror updated for review).

---

## 11. Review schedule

| Activity | Frequency |
|----------|-----------|
| BAA register review | Quarterly |
| PHI sub-processor assessment | On onboarding |
| HIPAA programme review | Annual (with PROC-CMP-001) |
| Marketing copy audit | Quarterly |

**Next review:** 2026-09-06

---

## 12. Related documents

- [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md) — UK/EU health data (Art. 9)
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md) — HIPAA row
- [FCA-ALIGNMENT.md](FCA-ALIGNMENT.md) — separate financial perimeter
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md) — biometric / health AI restrictions
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md)
- [TRANC3-HIPAA-COPY-REMEDIATION.md](../engineering/TRANC3-HIPAA-COPY-REMEDIATION.md) — Tranc3 product copy patch spec
