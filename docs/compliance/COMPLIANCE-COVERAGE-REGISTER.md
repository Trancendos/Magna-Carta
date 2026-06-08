# Compliance Coverage Register — Honest Status

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** ISMS Lead / DPO  
**Purpose:** Single source of truth for every ⚠️, 📋, and ❌ in the compliance programme — why it is not operationally ✅, what programme artefact covers future scenarios, and what blocks external validation.

---

## How to read this register

| Symbol | Meaning in this document |
|--------|--------------------------|
| ✅ **Programme** | Policy, procedure, register, or alignment doc **exists and is maintained** in Magna Carta (layer 2) |
| ✅ **Operational** | Demonstrated in production, signed contract, paid fee, completed test, or external attestation |
| ⚠️ | Applicable but **partial** — programme and/or operations incomplete |
| 📋 | **Mapping only** — trigger not active or implementation deferred; readiness doc prepared |
| ❌ **N/A** | Not applicable today — **future-readiness annex** added where geographic/sector expansion is plausible |
| 🎯 | External validation pending (Legal, DPO, HR, vendor, auditor, Tranc3 upstream) |

**Rule:** We do not mark operational ✅ without evidence. Programme ✅ is not certification.

---

## 1. Privacy & data protection

| Item | Matrix status | Honest state | Why not operational ✅ | Programme coverage | Blocker / next step |
|------|---------------|--------------|------------------------|-------------------|---------------------|
| UK GDPR / DPA 2018 | ✅ | ✅ Operational (Tranc3) + ✅ Programme | — | ROPA, PIA, PROC-DSR-001 | Maintain annual ROPA review |
| EU GDPR | ✅ | ✅ Programme | SCCs for US AI fallback need TIA before enable | [GDPR-ALIGNMENT.md](GDPR-ALIGNMENT.md), [TEMPLATE-TIA-US-AI-FALLBACK.md](../templates/TEMPLATE-TIA-US-AI-FALLBACK.md) | ACT-010; complete TIA if SUP-004 enabled |
| PECR | ⚠️ | ✅ Programme / 🎯 UI | Cookie banner not deployed until non-essential cookies used | [PECR-ALIGNMENT.md](PECR-ALIGNMENT.md) | Deploy consent UI when marketing/analytics cookies added |
| ePrivacy Directive | ⚠️ | ⚠️ Partial | Same as PECR; EU marketing cookies | PECR programme + privacy notice | EU deployment review |
| CCPA / CPRA | ⚠️ / 📋 | ✅ Programme (readiness) | No material CA user base; no CPRA-specific notices | [CCPA-CPRA-ALIGNMENT.md](CCPA-CPRA-ALIGNMENT.md) | Activate if CA users > threshold; legal review |
| LGPD | ❌ N/A | ✅ Programme (future) | No Brazil operations | [LGPD-READINESS.md](LGPD-READINESS.md) | Trigger: BR data subjects or entity |
| POPIA | ❌ N/A | ✅ Programme (future) | No South Africa operations | [POPIA-READINESS.md](POPIA-READINESS.md) | Trigger: ZA data subjects or entity |

---

## 2. Information security & assurance

| Item | Matrix status | Honest state | Why not operational ✅ | Programme coverage | Blocker / next step |
|------|---------------|--------------|------------------------|-------------------|---------------------|
| ISO 27001:2022 | ⚠️ Draft SOA | ✅ Programme / 🎯 cert | Certificate requires external audit Q2 2027 | [ISO27001-ALIGNMENT.md](ISO27001-ALIGNMENT.md), [RISK-TREATMENT-PLAN.md](RISK-TREATMENT-PLAN.md), Tranc3 SOA | ACT-011 internal audit; close HR/MDM gaps |
| ISO 27002:2022 | ⚠️ | ⚠️ Partial | Implemented via SOA; org controls partial | Same + POL-SEC-003, PROC-HR-001 | See ISO gaps table §4 |
| SOC 2 Type II | ⚠️ Draft | ✅ Programme / 🎯 report | 6-month observation not started | [SOC2-ALIGNMENT.md](SOC2-ALIGNMENT.md), evidence schedule | ACT-008 from 2026-10-01 |
| DEFSTAN 05-138 | ✅ Strong | ✅ Operational | CI gate active in Tranc3 | register.yaml, tests | Maintain quarterly review |
| NIST CSF 2.0 | 📋 Reference | ✅ Programme (mapped) | Reference framework only | [NIST-CSF-ALIGNMENT.md](NIST-CSF-ALIGNMENT.md) | Use for customer questionnaires |
| CIS Controls v8 | ⚠️ Partial | ⚠️ Partial | MDM/DLP not deployed | POL-SEC-003, technical controls in Tranc3 | Endpoint policy rollout |
| OWASP Top 10 | ✅ | ✅ Operational | Pen test execution pending | CI + PROC-VUL-001 | ACT-005 |
| OWASP ASVS L2 | ⚠️ Partial | ⚠️ Partial | Not full L2 checklist attestation | Auth, validation, logging strong | Optional ASVS gap assessment |
| PCI DSS | ❌ N/A | ✅ Programme (position) | No cardholder data environment | Payments via third-party only; no CHD storage | Re-assess if direct card processing |
| HIPAA | ✅ Programme | ✅ Programme / 🎯 Tier C | Per-customer BAAs not signed | [HIPAA-ALIGNMENT.md](HIPAA-ALIGNMENT.md), templates | ACT-002, ACT-006 |
| FedRAMP | ❌ N/A | ✅ Programme (future) | Not US government cloud | [FEDRAMP-READINESS.md](FEDRAMP-READINESS.md) | Trigger: federal customer RFP |
| CMMC 2.0 | ❌ N/A | ✅ Programme (future) | Not defence CUI contractor | [CMMC-READINESS.md](CMMC-READINESS.md) | Trigger: DoD supply chain |

---

## 3. AI & emerging technology

| Item | Matrix status | Honest state | Why not operational ✅ | Programme coverage | Blocker / next step |
|------|---------------|--------------|------------------------|-------------------|---------------------|
| EU AI Act | ✅ Programme | ✅ Programme | High-risk conformity assessment if in scope | AI-GOVERNANCE, model cards | Monitor delegated acts |
| ISO 42001 | ⚠️ Target | ✅ Programme | No ISO 42001 certificate | GENAI-MATURITY, POL-AI-001 | Target 2027 |
| NIST AI RMF | ✅ Mapped | ✅ Programme | Self-assessment only | AI-GOVERNANCE.md | Annual refresh |
| UK AI legislation | 📋 Monitor | ✅ Programme | Bill not final; no statutory duties yet | [UK-AI-LEGISLATION-MONITORING.md](UK-AI-LEGISLATION-MONITORING.md) | Quarterly LEGISLATION-REGISTER scan |
| Algorithmic transparency | ⚠️ | ✅ Programme / 🎯 measure | Bias run not executed | PROC-AI-002, model cards | ACT-004 |
| US AI fallback transfer | ⚠️ | ⚠️ Partial | SUP-004 DPA unsigned | TIA template, ROPA entry | ACT-010 |

---

## 4. ISO 27001 partial controls (why ⚠️)

| Gap area | Why not done | Programme artefact | Operational blocker |
|----------|--------------|-------------------|---------------------|
| HR screening / training | No formal HR procedure until ISMS wave | [PROC-HR-001](../procedures/PROC-HR-001-Staff-Lifecycle.md) | HR to adopt; background checks vendor |
| Offboarding checklist | Covered in PROC-IAM-001 only | PROC-HR-001 §3 | HR + IT joint execution |
| MDM / DLP | Cloud-remote workforce; not deployed | [POL-SEC-003](../policies/POL-SEC-003-Endpoint-Data-Protection.md) | Endpoint tooling selection |
| Malware (Wazuh) | Planned observability stack | PROC-VUL-001, DEFSTAN | Ops deployment |
| HA / resilience | Partial; BCP drills incomplete | PROC-BCP-001, BCP log | ACT-012 all P0 DBs |
| Risk treatment plan | Risks in register; no formal RTP doc | [RISK-TREATMENT-PLAN.md](RISK-TREATMENT-PLAN.md) | ISMS sign-off quarterly |
| Internal audit | Scheduled Q4 2026 | INTERNAL-AUDIT-PROGRAMME | ACT-011 |
| Management review | Template only | MANAGEMENT-REVIEW-TEMPLATE | First annual session |
| Corrective action (CAPA) | Informal via CAB + IR | [PROC-CAPA-001](../procedures/PROC-CAPA-001-Corrective-Action.md) | Link to audit findings |

---

## 5. Operational & legal

| Item | Matrix status | Honest state | Why not operational ✅ | Programme coverage | Blocker / next step |
|------|---------------|--------------|------------------------|-------------------|---------------------|
| ITIL 4 | ✅ Programme | ✅ Programme | Town Hall ITSM operational | PROC-IR-001, templates | — |
| PRINCE2 7 | ✅ Programme | ✅ Programme | Stage gates via BoardRoom | PROC-CHG-002 | — |
| ISO 22301 BCM | ⚠️ Target | ✅ Programme / 🎯 drills | One baseline restore only | PROC-BCP-001, BCP log | ACT-012 |
| ISO 9001 | ❌ N/A | — | QA via DEFSTAN instead | DEFSTAN-ALIGNMENT | — |
| UK Companies Act | ✅ Programme | ✅ Programme | Board minutes external to repo | COMPANIES-ACT-ALIGNMENT | — |
| FCA Handbook | ✅ Programme | ✅ Programme | Not FCA-authorised firm | FCA-ALIGNMENT (supplier perimeter) | Re-assess if regulated activities |
| Customer SLAs | ⚠️ | ⚠️ Partial | Enterprise agreements TBD | Contract templates | Sales/Legal |
| Research / Concordat | ⚠️ Partial | ✅ Programme (future) | No academic clinical research today | [RESEARCH-DATA-CONCORDAT-ANNEX.md](RESEARCH-DATA-CONCORDAT-ANNEX.md) | Trigger: university/NHS research data |
| NHS DSPT | ❌ N/A | ✅ Programme (future) | Not NHS data processor today | [NHS-DSPT-READINESS.md](NHS-DSPT-READINESS.md) | Trigger: NHS contract |
| Export controls | ❌ N/A | — | Standard crypto; no controlled export | Legal position in FRAMEWORK | — |
| AML / KYC | ❌ N/A | — | Not a financial institution | FCA supplier scope only | — |
| GitHub brand | ❌ Out of scope | — | Marketing identity only | EXTERNAL-FRAMEWORK-MAPPING | — |

---

## 6. Penetration testing scope

| Scope item | Matrix status | Honest state | Programme coverage | Notes |
|------------|---------------|--------------|-------------------|-------|
| External/API/auth | ✅ In scope | 🎯 ACT-005 | PEN-TEST-PROGRAMME | First vendor test due 2026-12-31 |
| Internal segmentation | ⚠️ Optional | Optional | PEN-TEST-PROGRAMME | Offered in annual scope |
| Social engineering | ❌ Out of scope (default) | ✅ Future-ready | [PEN-TEST-FUTURE-SCOPE-ANNEX.md](../evidence/PEN-TEST-FUTURE-SCOPE-ANNEX.md) | Add to contract if customer requires |
| Denial of service | ❌ Ops-coordinated | ✅ Future-ready | PEN-TEST-FUTURE-SCOPE-ANNEX | Separate rules of engagement with ops |

---

## 7. Open actions (external validation only)

All items require parties outside documentation-only work:

| ID | Item | Why still open | Owner |
|----|------|----------------|-------|
| ACT-001 | Signed PSP DPA | Legal countersignature | Legal / Procurement |
| ACT-002 | Health connector BAA/DPA | Per-customer legal | Legal / DPO |
| ACT-003 | ICO fee + registration number | Fee payment + portal | DPO |
| ACT-004 | First bias/fairness run | Operational test cycle | AI Lead |
| ACT-005 | External pen test | Vendor contract + budget | Security Ops |
| ACT-006 | Tranc3 HIPAA copy PR | Upstream merge | Platform Engineering |
| ACT-007 | Policy attestation cycle | HR rollout | HR / ISMS |
| ACT-008 | SOC 2 observation window | Clock not started | ISMS Lead |
| ACT-009 | magna_carta.py enforcement | Tranc3 staging code | Platform Engineering |
| ACT-010 | SUP-004 DPA or disable | Legal negotiation | DPO / AI Lead |
| ACT-011 | First internal audit | Scheduled Q4 2026 | ISMS Lead |
| ACT-012 | BCP all P0 DBs | Drill schedule through 2027 | Operations |

**Nothing blocks** further programme documentation — completed in this register's linked artefacts.

---

## 8. Programme milestones closed

### 8.1 Coverage wave (2026-06-07)

| Milestone | Status |
|-----------|--------|
| COMPLIANCE-COVERAGE-REGISTER (this doc) | ✅ Programme |
| CCPA, LGPD, POPIA readiness alignments | ✅ Programme |
| NIST CSF, FedRAMP, CMMC readiness | ✅ Programme |
| Research/Concordat annex | ✅ Programme |
| RISK-TREATMENT-PLAN | ✅ Programme |
| PROC-HR-001, PROC-CAPA-001 | ✅ Programme |
| POL-SEC-003 Endpoint/Data Protection | ✅ Programme |
| TIA template (US AI fallback) | ✅ Programme |
| PEN-TEST future scope annex | ✅ Programme |
| UK AI legislation monitoring | ✅ Programme |
| NHS-DSPT-READINESS | ✅ Programme |
| PCI-DSS-POSITION | ✅ Programme |

### 8.2 Documentation artefact model wave (2026-06-07)

| Artefact category | Milestone | Status | Honest gap |
|-------------------|-----------|--------|------------|
| **Model** | DOCUMENTATION-ARTIFACT-MODEL | ✅ Programme | — |
| **Bible** | MAGNACARTA-GOVERNANCE-BIBLE | ✅ Programme (v1) | Expand as procedures mature |
| **Cookbooks** | COOK-CMP-001, COOK-IR-001 + INDEX | ✅ Programme (starter) | Cookbook per remaining PROC-* |
| **Hymn sheets** | HYMN-CMP-001, HYMN-IR-001 + INDEX | ✅ Programme (starter) | Hymn sheet per high-frequency PROC |
| **Schemas** | REGISTER-SCHEMAS | ✅ Programme | Machine validation in CI 🎯 |
| **Standards** | STANDARDS-REGISTER | ✅ Programme | Not external certification |
| **Regulators / ombudsmen** | REGULATORS-OMBUDSMEN-REGISTER | ✅ Programme | Contact verification 🎯 |
| **Systems** | SYSTEMS-REGISTER | ✅ Programme | Production monitoring hooks 🎯 |
| **Reviewers** | REVIEWERS-REGISTER | ✅ Programme | Named individuals external 🎯 |
| **Maintenance** | COMPLIANCE-MAINTENANCE-PROGRAMME | ✅ Programme | Weekly CI job not wired 🎯 |
| **Automation** | maintenance_monitor.yaml + compliance_health_check.py | ✅ Programme | `--strict` in CI pipeline 🎯 |

**Still missing (honest backlog):** cookbooks for PROC-DSR, PROC-VUL, PROC-BCP, PROC-CHG, PROC-IAM, PROC-AI-002, PROC-TRN, PROC-HR, PROC-CAPA; hymn sheets for same; JSON Schema files per register (schemas doc is narrative only); ombudsman escalation runbooks where sector-specific.

---

## 9. Path to comprehensive ✅ (summary)

| Layer | What “done” looks like | Target |
|-------|------------------------|--------|
| Programme (layer 2) | Every applicable/future row has owner doc + artefact taxonomy | **Achieved** (starter cookbooks/hymn sheets; backlog in §8.2) |
| Maintenance (layer 2b) | Health check green in CI; quarterly PROC-CMP-001 | Wire CI + first drill 2026-09-06 |
| Operations (layer 3) | ACT-001–012 closed with evidence | 2026–2027 |
| External assurance | ISO 27001, SOC 2, ICO live | Q1–Q2 2027 |

---

## 10. Review

| Activity | Frequency | Next |
|----------|-----------|------|
| Update this register | Quarterly (PROC-CMP-001) | 2026-09-06 |
| Sync REGULATION-MATRIX symbols | After register update | Same |
| Escalate P0 actions past due | Weekly ISMS stand-up | Ongoing |

**Related:** [REGULATION-MATRIX.md](REGULATION-MATRIX.md) · [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md) · [00-EXECUTIVE-SUMMARY.md](../00-EXECUTIVE-SUMMARY.md)
