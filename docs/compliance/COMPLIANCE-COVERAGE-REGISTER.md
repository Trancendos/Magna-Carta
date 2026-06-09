# Compliance Coverage Register — Honest Status

**Version:** 1.3.0  
**Date:** 2026-06-09  
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
| EU AI Act | ✅ Programme | ✅ Programme | High-risk conformity assessment if in scope | AI-GOVERNANCE, model cards, [legislation_register.yaml](../../compliance/legislation_register.yaml) | ACT-014 quarterly EUR-Lex scan |
| ISO 42001 | ⚠️ Target | ✅ Programme | No ISO 42001 certificate | GENAI-MATURITY, POL-AI-001 | Target 2027 |
| NIST AI RMF | ✅ Mapped | ✅ Programme | Self-assessment only | AI-GOVERNANCE.md | Annual refresh |
| UK AI legislation | 📋 Monitor | ✅ Programme | Bill not final; no statutory duties yet | [UK-AI-LEGISLATION-MONITORING.md](UK-AI-LEGISLATION-MONITORING.md) | Quarterly LEGISLATION-REGISTER scan |
| EU legislation (EUR-Lex / ELI) | ✅ Programme | ✅ Programme / 🎯 recurring | First quarterly scan baseline completed 2026-06-09 (SCAN-2026-Q2-01, EEV-006) | [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md), [EUR-LEX-ELI-REFERENCE.md](EUR-LEX-ELI-REFERENCE.md) | Next scan 2026-09-30 (ACT-014 recurring) |
| Algorithmic transparency | ⚠️ | ✅ Programme / 🎯 recurring | Baseline fairness run completed 2026-06-09 (FTR-2026-001, EEV-001); production cohort testing ongoing | PROC-AI-002, model cards | Quarterly PROC-AI-002 cycles |
| AI security (OWASP AI Exchange) | ✅ Programme | ✅ Programme / 🎯 recurring | Baseline PROC-AI-003 per model completed 2026-06-09 (AST-2026-001–003, EEV-003–005); pen test remains 🎯 | OWASP-AI-EXCHANGE-ALIGNMENT, AI-SECURITY-THREAT-MODEL, PROC-AI-003 | ACT-005; annual PROC-AI-003 refresh |
| ETSI EN 304 223 (Securing AI) | ✅ Programme | ✅ Programme / 🎯 recurring | Gap checklist baseline completed 2026-06-09 (EEV-008); not OJEU harmonised | [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md), [ETSI-EN-304-223-GAP-CHECKLIST.md](ETSI-EN-304-223-GAP-CHECKLIST.md) | Semi-annual watch (ACT-015 recurring) |
| EU harmonised standards (JTC21) | ✅ Programme | ✅ Programme / 🎯 recurring | First semi-annual watch baseline completed 2026-06-09 (WATCH-2026-H1-01, EEV-007) | [HARMONISED-STANDARDS-MONITORING.md](HARMONISED-STANDARDS-MONITORING.md) | Next watch 2026-12-31 |
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
| Internal audit | Baseline completed 2026-06-09 (IA-2026-01, EEV-002); annual cycle continues | INTERNAL-AUDIT-PROGRAMME | Next internal audit per programme calendar |
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

Programme baselines closed 2026-06-09 (PM-014): ACT-004, ACT-011, ACT-013, ACT-014, ACT-015 — evidence in `compliance/execution_evidence_register.yaml` (EEV-001–008). Remaining items require parties outside documentation-only work:

| ID | Item | Why still open | Owner |
|----|------|----------------|-------|
| ACT-001 | Signed PSP DPA | Legal countersignature | Legal / Procurement |
| ACT-002 | Health connector BAA/DPA | Per-customer legal | Legal / DPO |
| ACT-003 | ICO fee + registration number | Fee payment + portal | DPO |
| ACT-005 | External pen test | Vendor contract + budget | Security Ops |
| ACT-006 | Tranc3 HIPAA copy PR | Upstream merge (local verified) | Platform Engineering |
| ACT-007 | Policy attestation cycle | HR rollout | HR / ISMS |
| ACT-008 | SOC 2 observation window | Clock not started | ISMS Lead |
| ACT-009 | magna_carta.py enforcement | Tranc3 staging code | Platform Engineering |
| ACT-010 | SUP-004 DPA or disable | Legal negotiation | DPO / AI Lead |
| ACT-012 | BCP all P0 DBs | Drill schedule through 2027 | Operations |

**Playbooks:** [EXTERNAL-ACTION-EXECUTION-GUIDE.md](EXTERNAL-ACTION-EXECUTION-GUIDE.md) · Machine-readable packages in `execution_evidence_register.yaml` → `external_action_packages`.

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
| **Cookbooks** | 25 cookbooks + INDEX (all PROC-*) | ✅ Programme | Operational drills not evidenced 🎯 |
| **Hymn sheets** | 25 hymn sheets + INDEX (all PROC-*) | ✅ Programme | Named signatories in production 🎯 |
| **Schemas** | REGISTER-SCHEMAS + 12 JSON schemas (MON-009) | ✅ Programme | Schema drift on new fields — monitor via health check |
| **Standards** | STANDARDS-REGISTER | ✅ Programme | Not external certification |
| **Regulators / ombudsmen** | REGULATORS-OMBUDSMEN-REGISTER | ✅ Programme | Contact verification 🎯 |
| **Systems** | SYSTEMS-REGISTER | ✅ Programme | Production monitoring hooks 🎯 |
| **Reviewers** | REVIEWERS-REGISTER | ✅ Programme | Named individuals external 🎯 |
| **Maintenance** | COMPLIANCE-MAINTENANCE-PROGRAMME v1.1 | ✅ Programme | First weekly local run logged 🎯 |
| **Automation** | weekly_compliance_health.sh + health_check_history.yaml | ✅ Programme | Optional local cron on ISMS machine 🎯 |
| **Runbooks** | RUN-OMB-001, RUN-PECR-001 + INDEX | ✅ Programme | Live escalation tickets 🎯 |
| **Domain bibles** | 16 bibles (governance, privacy, security, 12 departments) + INDEX | ✅ Programme | Tranc3 upstream sync 🎯 |
| **Job descriptions** | 13 roles + template + INDEX | ✅ Programme | HRIS appointments 🎯 ACT-016 |
| **Evidence templates** | Fairness test + internal audit report | ✅ Programme | Baseline reports filed (EEV-001–002); recurring cycles 🎯 |
| **ASVS gap tracker** | ASVS-GAP-CHECKLIST | ✅ Programme | Pen test / remediation evidence 🎯 |

**Still missing (honest backlog — operational only):** Named individuals in REVIEWERS-REGISTER and HRIS (ACT-016); operational evidence that cookbooks were exercised (drills, tickets); ACT-001–003, ACT-005–010, ACT-012, ACT-016–019 external closure; sector-specific runbooks beyond ICO/FOS/PECR starters. **Programme layer for documentation artefacts: 100%** — see [COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md](COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md).

### 8.3 Framework catalogue wave (2026-06-08 → 2026-06-09)

| Milestone | Status |
|-----------|--------|
| STANDARDS-AND-FRAMEWORKS-REGISTER (FW-001–FW-145, 127 entries) | ✅ Programme |
| Readiness groups (ISO, SOC, PCI, NIST, US gov, intl, privacy, industry) | ✅ Programme |
| frameworks_register.yaml + schema (MON-009) | ✅ Programme |
| framework_implementation_catalog.yaml + MON-018 trigger wiring | ✅ Programme |
| proactive_signals.yaml (22 scope signals) + framework_triggers.yaml (22 groups) | ✅ Programme |
| generate_framework_implementation.py (catalog regen) | ✅ Programme |
| PM-009 / PM-010 programme milestones | ✅ Programme |

**Honest gap:** Layer 3 external validation (certificates, authorisations, signed BAAs, pen test, drills) — see open ACT-001–003, ACT-005–010, ACT-012. Scope signals default **off** until operators enable profiles in `config/magna_carta_config.json`.

### 8.4 EUR-Lex / ELI programme wave (2026-06-08)

| Milestone | Status |
|-----------|--------|
| legislation_register.yaml + schema (LEG-001–010, WATCH-001–006) | ✅ Programme |
| EUR-LEX-ELI-REFERENCE.md (CELEX / ELI citation guide) | ✅ Programme |
| EU-LEGISLATION-MONITORING.md (quarterly delegated-act workflow) | ✅ Programme |
| OBLIGATIONS-REGISTER EUR-Lex anchors (OBL-020–024) | ✅ Programme |
| PM-012 / ACT-014 baseline scan | ✅ Programme / 🎯 recurring |

**Honest gap:** First quarterly scan baseline completed 2026-06-09 (SCAN-2026-Q2-01). Next quarterly scan due 2026-09-30.

### 8.5 ETSI SAI / harmonised standards wave (2026-06-08)

| Milestone | Status |
|-----------|--------|
| standards_watch.yaml + schema (STD-WATCH-001–005, harmonised watch) | ✅ Programme |
| ETSI-SAI-ALIGNMENT.md (EN 304 223 ↔ OWASP / PROC-AI-003) | ✅ Programme |
| HARMONISED-STANDARDS-MONITORING.md (semi-annual workflow) | ✅ Programme |
| STD-042 / STD-043 in STANDARDS-REGISTER | ✅ Programme |
| PM-013 / ACT-015 baseline watch | ✅ Programme / 🎯 recurring |
| ETSI EN 304 223 gap checklist (EEV-008) | ✅ Programme baseline | — |

**Honest gap:** EN 304 223 is a reference standard only — not OJEU harmonised. First semi-annual watch baseline completed 2026-06-09 (WATCH-2026-H1-01). Next watch due 2026-12-31.

### 8.6 Execution evidence wave (2026-06-09)

| Milestone | Status |
|-----------|--------|
| execution_evidence_register.yaml + schema (EEV-001–008) | ✅ Programme |
| Baseline fairness report (FTR-2026-001) | ✅ Programme baseline |
| Baseline internal audit (IA-2026-01) | ✅ Programme baseline |
| PROC-AI-003 assessments (AST-2026-001–003) | ✅ Programme baseline |
| ETSI EN 304 223 gap checklist | ✅ Programme baseline |
| EXTERNAL-ACTION-EXECUTION-GUIDE.md (ACT-001–012 playbooks) | ✅ Programme |
| PM-014 programme milestone | ✅ Programme |

**Honest gap:** Closed baselines are programme evidence, not external certification. Recurring monitoring, pen test (ACT-005), and vendor/legal actions remain 🎯.

### 8.7 Department packs & programme completion wave (2026-06-09)

| Milestone | Status |
|-----------|--------|
| 12 department bibles + HR-BIBLE (16 total) | ✅ Programme |
| PROC/COOK/HYMN for HSE, FIN, PRM, LEG, IP, PAY, BLD, IT, WLB, MHL, UMG, DAT | ✅ Programme |
| Job description library (13 roles + template) | ✅ Programme |
| AI-SECURITY-SCOPING-MATRIX + maturity benchmark update | ✅ Programme |
| COMPLIANCE-PROGRAMME-COMPLETION-REGISTER (programme 100% inventory) | ✅ Programme |
| PM-015 / PM-016 / PM-017 programme milestones | ✅ Programme |
| ACT-016–019 operational actions (HRIS, FRA, payroll RTI, H&S) | ✅ Programme / 🎯 execution |

**Honest gap:** Programme documentation is **100%** for in-repo scope. Operational appointments, premises assessments, and live payroll remain 🎯.

---

## 9. Path to comprehensive ✅ (summary)

| Layer | What “done” looks like | Target |
|-------|------------------------|--------|
| Programme (layer 2) | Every applicable/future row has owner doc + artefact taxonomy | **100% achieved** — [COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md](COMPLIANCE-PROGRAMME-COMPLETION-REGISTER.md) |
| Maintenance (layer 2b) | Weekly local health check logged; quarterly PROC-CMP-001 | First weekly run + Q3 review 2026-09-06 |
| Operations (layer 3) | Open ACT-001–003, ACT-005–010, ACT-012 closed with evidence; baselines for ACT-004/011/013/014/015 done | 2026–2027 |
| External assurance | ISO 27001, SOC 2, ICO live | Q1–Q2 2027 |

---

## 10. Review

| Activity | Frequency | Next |
|----------|-----------|------|
| Update this register | Quarterly (PROC-CMP-001) | 2026-09-06 |
| Sync REGULATION-MATRIX symbols | After register update | Same |
| Escalate P0 actions past due | Weekly ISMS stand-up | Ongoing |

**Related:** [REGULATION-MATRIX.md](REGULATION-MATRIX.md) · [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md) · [00-EXECUTIVE-SUMMARY.md](../00-EXECUTIVE-SUMMARY.md)
