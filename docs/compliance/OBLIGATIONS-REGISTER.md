# Regulatory Obligations Register

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** DPO / ISMS Lead  
**Methodology:** Adapted from NGX compliance programme — obligations management  
**Review cycle:** Quarterly (full scan); monthly (regulatory change triage)

---

## 1. Purpose

The obligations register is the **operational complement** to [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md). Where the legislation register lists *what laws apply*, this register tracks:

- Specific **obligations** extracted from law, standards, and contracts
- **Controls** that satisfy each obligation
- **Evidence** and **owners** for demonstration
- **Status** and review dates

Use this register for audit preparation, PROC-CMP-001 reviews, and regulatory engagement management.

---

## 2. Obligation lifecycle

```
Identify → Map to control → Implement → Monitor → Evidence → Review → Close/Update
     ↑                                                              │
     └──────────── regulatory change / new scope ─────────────────┘
```

| Stage | Activity | Owner |
|-------|----------|-------|
| Identify | Scan legislation, standards, contracts | DPO / Legal |
| Map | Link obligation → policy → procedure → technical control | ISMS Lead |
| Implement | Engineering + process changes | Engineering / Ops |
| Monitor | Continuous (operational) + periodic (audit) | See §6 |
| Evidence | Collect artefacts for audit window | ISMS Lead |
| Review | Quarterly PROC-CMP-001 | ISMS Lead |

---

## 3. Obligation record schema

| Field | Description |
|-------|-------------|
| **OBL-ID** | Unique identifier (OBL-###) |
| **Source** | Law, standard, or contract reference |
| **Obligation** | Plain-language requirement |
| **Applicability** | All platform / EU only / AI only / etc. |
| **Control(s)** | Policy, procedure, technical control IDs |
| **Evidence** | Artefact path or system |
| **Owner** | Role accountable |
| **Frequency** | Ongoing / annual / per-event |
| **Status** | ✅ Met / ⚠️ Partial / ❌ Gap / N/A |
| **Last verified** | Date |
| **Next review** | Date |

---

## 4. Core obligations register

### 4.1 Privacy and data protection

| OBL-ID | Source | Obligation | Control(s) | Evidence | Owner | Status |
|--------|--------|------------|------------|----------|-------|--------|
| OBL-001 | UK GDPR Art. 5 | Lawfulness, fairness, transparency | POL-PRI-001, ROPA | ROPA doc, privacy notice | DPO | ✅ |
| OBL-002 | UK GDPR Art. 25 | Privacy by design | Architecture, Ice Box | AS-BUILT, DPIA templates | DPO | ✅ |
| OBL-003 | UK GDPR Art. 28 | Processor agreements | POL-SUP-001 | DPA register | DPO | ⚠️ |
| OBL-004 | UK GDPR Art. 30 | Records of processing | ROPA | ROPA in users-service area | DPO | ✅ |
| OBL-005 | UK GDPR Art. 32 | Security of processing | POL-SEC-001, DEFSTAN | register.yaml, pen test | CISO | ✅ |
| OBL-006 | UK GDPR Art. 33–34 | Breach notification | PROC-IR-001 | Incident log template | DPO | ✅ |
| OBL-007 | UK GDPR Art. 12–23 | Data subject rights | PROC-DSR-001 | DSR workflow metrics | DPO | ✅ |
| OBL-008 | UK GDPR Art. 22 | Automated decision-making | AI-GOVERNANCE §8, POL-AI-001 | Model cards, review workflow | AI Lead | ⚠️ |

### 4.2 AI and emerging technology

| OBL-ID | Source | Obligation | Control(s) | Evidence | Owner | Status |
|--------|--------|------------|------------|----------|-------|--------|
| OBL-020 | EU AI Act Art. 13 | Transparency to deployers | Model cards API | `/compliance/ai/model-cards` | AI Lead | ✅ |
| OBL-021 | EU AI Act Art. 50 | Mark AI-generated content | ai_governance rule | Magna Carta config | AI Lead | ✅ |
| OBL-022 | EU AI Act Art. 9 | Risk management system | AI-GOVERNANCE §4 | Risk classify runtime | AI Lead | ⚠️ |
| OBL-023 | EU AI Act Art. 14 | Human oversight (high-risk) | §8 human agency | Review workflow | AI Lead | ⚠️ |
| OBL-024 | EU AI Act Art. 5 | No prohibited practices | Blocklist in model cards | ai_governance.py | AI Lead | ⚠️ |
| OBL-025 | ISO 42001 (target) | AI MS continual improvement | GENAI-MATURITY-ASSESSMENT | Assessment record | AI Lead | ⚠️ |

### 4.3 Information security

| OBL-ID | Source | Obligation | Control(s) | Evidence | Owner | Status |
|--------|--------|------------|------------|----------|-------|--------|
| OBL-040 | ISO 27001 A.5–A.8 | Organisational controls | Policies index | docs/policies/ | ISMS | ⚠️ |
| OBL-041 | ISO 27001 A.9 | Access control | PROC-IAM-001, auth workers | JWT/MFA config | CISO | ✅ |
| OBL-042 | ISO 27001 A.12 | Operations security | PROC-VUL-001, CI | Forgejo pipeline | CISO | ✅ |
| OBL-043 | ISO 27001 A.16 | Incident management | PROC-IR-001 | WarRoom runbooks | Security Ops | ✅ |
| OBL-044 | DEFSTAN register | Civilian control baseline | register.yaml | CI gate ≥70% | Platform Eng | ✅ |
| OBL-045 | SOC 2 CC6–CC8 | Logical access, change, ops | SOC2-ALIGNMENT | Evidence collector | ISMS | ⚠️ |

### 4.4 Operations and governance

| OBL-ID | Source | Obligation | Control(s) | Evidence | Owner | Status |
|--------|--------|------------|------------|----------|-------|--------|
| OBL-060 | Internal — Magna Carta | Quarterly compliance review | PROC-CMP-001 | Meeting minutes | ISMS | ✅ |
| OBL-061 | Internal — CAB | Controlled production change | PROC-CHG-001 | Change records | CAB | ✅ |
| OBL-062 | Internal — BCP | Backup and restore capability | PROC-BCP-001 | Restore test log | Ops | ⚠️ |
| OBL-063 | Companies Act 2006 | Director duties (high level) | BoardRoom governance | Board minutes | Executive | ⚠️ |

### 4.5 Contractual (template)

| OBL-ID | Source | Obligation | Control(s) | Evidence | Owner | Status |
|--------|--------|------------|------------|----------|-------|--------|
| OBL-080 | Customer SLA | Availability targets | Monitoring, BCP | SLA reports | Ops | Per contract |
| OBL-081 | Supplier DPA | Processor Art. 28 terms | POL-SUP-001 | Signed DPA | Legal | ⚠️ |

*Add rows per customer agreement and supplier contract.*

---

## 5. Regulatory change management

| Step | Action | Tool / artefact |
|------|--------|-----------------|
| 1 | Monitor sources (ICO, EU AI Office, DSIT, industry bodies) | LEGISLATION-REGISTER watch list |
| 2 | Triage impact (DPO + ISMS + AI Lead within 10 business days) | Change log below |
| 3 | Map new/changed obligations to this register | New OBL-ID rows |
| 4 | Update policies/procedures/controls | Policy index, PROC-* |
| 5 | Notify stakeholders (Town Hall, BoardRoom if material) | MeetingRooms |
| 6 | Verify implementation | PROC-CMP-001 agenda item |

### Change log

| Date | Source | Summary | Impact | Actions | Status |
|------|--------|---------|--------|---------|--------|
| 2026-06-07 | — | Register initialised | Baseline | Populate OBL-001–063 | ✅ |

---

## 6. Monitoring vs auditing

Adapted from NGX compliance programme distinction:

| Aspect | **Monitoring** | **Auditing** |
|--------|----------------|--------------|
| **Timing** | Continuous or near-real-time; in-process | Periodic; after the fact |
| **Proximity** | Close to operational activity | Independent of line management |
| **Performers** | Operators, engineering, automated CI | ISMS, internal audit, external auditors |
| **Purpose** | Early detection and correction | Independent assurance |
| **Examples** | DEFSTAN CI gate; Ice Box scans; access reviews; DSR SLA tracking; model card checks | Annual policy attestation; SOC2 evidence period; ISO certification audit; PROC-CMP-001 annual pack |

**Rule:** Operational teams **monitor**; ISMS and auditors **audit**. Monitoring results feed audit evidence packs.

Tranc3 monitoring hooks:

- `compliance/checker.py` — DEFSTAN score
- Forgejo CI — security scanners, Magna Carta tests
- Observatory / Prometheus — availability and AI route health
- Audit service — append-only logs for audit trail

---

## 7. Regulatory engagement management

| Engagement type | Process | Record |
|-----------------|---------|--------|
| ICO enquiry / breach | DPO leads; PROC-IR-001 | Incident + regulator log |
| Customer audit / questionnaire | ISMS + DPO respond | Evidence pack §PROC-CMP-001 |
| Certification audit (ISO/SOC2) | ISMS coordinates | Pre-audit checklist |
| AI conformity (future) | AI Lead + Legal | OBL-020–025 evidence |

---

## 8. Compliance solution capabilities (target state)

Manual spreadsheet maintenance is acceptable at current scale. As obligations grow, prefer tooling that supports:

- Central obligation library linked to policies and controls
- Regulatory change notifications
- Control testing and certification workflows
- Policy-to-regulation mapping
- Case/incident management integration

Until tooling is adopted, this markdown register + LEGISLATION-REGISTER + `register.yaml` constitute the system of record.

---

## 9. Quarterly review checklist

- [ ] All OBL rows status verified against evidence
- [ ] New legislation from LEGISLATION-REGISTER reflected
- [ ] Contractual obligations updated (DPAs, SLAs)
- [ ] Gaps (⚠️/❌) have owners and dates in action tracker
- [ ] Change log updated
- [ ] Summary reported in PROC-CMP-001 minutes

---

## 10. Related documents

- [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md)
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
- [COMPLIANCE-BLUEPRINT.md](COMPLIANCE-BLUEPRINT.md)
- [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)
- [EXTERNAL-FRAMEWORK-MAPPING.md](EXTERNAL-FRAMEWORK-MAPPING.md)

**Next full review:** 2026-09-06
