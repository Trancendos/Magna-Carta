#!/usr/bin/env python3
"""Generate comprehensive job descriptions for Magna Carta compliance roles."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JD_DIR = ROOT / "docs/job-descriptions"

ROLES = [
    (
        "JD-ISMS-001",
        "Information Security Management System (ISMS) Lead",
        "ISMS Lead",
        "Executive / Board",
        "COMPLIANCE-BLUEPRINT §3",
        """Own the Trancendos ISMS: Statement of Applicability, risk register, internal audit liaison, compliance score, and PROC-CMP-001 quarterly reviews. Map controls to ISO 27001, SOC 2, and framework catalogue. Chair management review inputs for security and compliance.""",
        [
            "Maintain SOA, risk register, and compliance health check (MON-001–018)",
            "Coordinate external audits and pen-test remediation (CAPA)",
            "Approve policy exceptions with executive sign-off",
            "Report compliance maturity to board quarterly",
            "Assign process owners for departmental PROC-* triads",
        ],
        [
            "ISO 27001 Lead Implementer or equivalent",
            "5+ years security/compliance programme leadership",
            "Risk assessment and audit evidence management",
            "Stakeholder communication with engineering and legal",
        ],
        ["PROC-CMP-001", "PROC-CAPA-001", "COMPLIANCE-BLUEPRINT", "RACI-MATRIX"],
    ),
    (
        "JD-PRI-001",
        "Data Protection Officer (DPO)",
        "DPO",
        "Executive / Board",
        "UK GDPR Art. 37",
        """Independent privacy oversight: ROPA, PIAs, DSR workflow (PROC-DSR-001), ICO liaison, and privacy impact on product changes. Ensure POL-PRI-001 and supplier DPAs are operationally enforced.""",
        [
            "Maintain ROPA and privacy impact assessments",
            "Oversee DSR responses within statutory timelines",
            "Review new processing and cross-border transfers",
            "Advise on PECR, HIPAA customer BAAs, and CCPA readiness",
            "Report privacy risks to ISMS Lead and executive",
        ],
        [
            "CIPP/E, CIPM, or equivalent privacy certification",
            "UK/EU GDPR operational experience",
            "Vendor DPA negotiation familiarity",
            "Ability to work independently of marketing/sales pressure",
        ],
        ["PROC-DSR-001", "POL-PRI-001", "PRIVACY-BIBLE", "ROPA"],
    ),
    (
        "JD-SEC-001",
        "Chief Information Security Officer (CISO)",
        "CISO / Security Lead",
        "CEO / Board",
        "POL-SEC-001",
        """Lead technical security: threat modelling, vulnerability management (PROC-VUL-001), incident response (PROC-IR-001), pen-test programme, and Ice Box / secrets policy. Partner with AI Lead on PROC-AI-003.""",
        [
            "Own enterprise threat model and security architecture",
            "Run vuln management and patch exception process",
            "Lead severity-1 incident response",
            "Scope annual pen tests (PT-CORE, PT-AI)",
            "Review IAM and Zero Trust controls (PROC-IAM-001)",
        ],
        [
            "CISSP, CISM, or equivalent",
            "Hands-on cloud/SaaS security experience",
            "Incident response and forensics familiarity",
            "Vendor security assessment (SUP register)",
        ],
        ["PROC-IR-001", "PROC-VUL-001", "SECURITY-BIBLE", "AI-SECURITY-THREAT-MODEL"],
    ),
    (
        "JD-CAB-001",
        "Change Advisory Board (CAB) Chair",
        "CAB Chair",
        "COO / Engineering Lead",
        "POL-OPS-002",
        """Chair CAB: classify changes, approve production releases, manage emergency changes, and ensure PROC-CHG-002 post-implementation reviews for major items.""",
        [
            "Schedule and chair CAB meetings",
            "Enforce change classification and rollback plans",
            "Approve or reject production-impacting changes",
            "Escalate conflicts between speed and risk",
            "Ensure evidence linkage to DEFSTAN gates",
        ],
        [
            "ITIL change management or equivalent",
            "Production operations background",
            "Risk-based decision making under time pressure",
        ],
        ["PROC-CHG-001", "PROC-CHG-002", "POL-OPS-002"],
    ),
    (
        "JD-ENG-001",
        "Engineering Lead",
        "Engineering Lead",
        "CTO",
        "—",
        """Accountable for secure engineering practices, control implementation in code/tests, and evidence for SOC 2 CC8. Supports CAPA remediation and Magna Carta rule integration.""",
        [
            "Enforce secure SDLC and code review standards",
            "Implement controls identified in risk register",
            "Provide architecture context for AI and security assessments",
            "Own technical debt vs security trade-off escalations",
            "Support audit evidence from CI/CD and test suites",
        ],
        [
            "Senior software engineering leadership",
            "Security-aware development (OWASP ASVS familiarity)",
            "Cloud-native architecture",
        ],
        ["PROC-CHG-001", "PROC-CAPA-001", "FRAMEWORK"],
    ),
    (
        "JD-AI-001",
        "AI Governance Lead",
        "AI Lead",
        "CTO / ISMS Lead",
        "POL-AI-001",
        """Own AI model registry, risk classification, PROC-AI-002 fairness testing, PROC-AI-003 security assessments, and model card accuracy. Implement scoping matrix tiers (Answers/Connects/Acts).""",
        [
            "Maintain model cards and EU AI Act tiering",
            "Run fairness/bias and AI security assessment cycles",
            "Approve agentic tool routes and RAG trust tiers",
            "Coordinate with DPO on Art. 22 and transparency",
            "Feed incidents to AI incident API and PROC-IR-001",
        ],
        [
            "ML/LLM production experience",
            "NIST AI RMF or ISO 42001 familiarity",
            "OWASP LLM Top 10 / AI Exchange knowledge",
            "Cross-functional work with security and legal",
        ],
        ["PROC-AI-002", "PROC-AI-003", "AI-GOVERNANCE", "AI-SECURITY-SCOPING-MATRIX"],
    ),
    (
        "JD-HR-001",
        "HR / People Lead",
        "HR / People Lead",
        "CEO / COO",
        "PROC-HR-001",
        """People operations: screening tiers, onboarding/offboarding (PROC-HR-001), training attestation (PROC-TRN-001), wellbeing and mental health programme liaison.""",
        [
            "Execute staff lifecycle and background screening workflow",
            "Coordinate security training and policy attestation",
            "Maintain personnel records for audit evidence",
            "Partner with IT on joiner/mover/leaver IAM triggers",
            "Support wellbeing (PROC-WLB-001) and mental health (PROC-MHL-001)",
        ],
        [
            "HR generalist with tech/SaaS experience",
            "UK employment law basics",
            "Confidentiality and personnel data handling",
        ],
        ["PROC-HR-001", "PROC-TRN-001", "HR-BIBLE"],
    ),
    (
        "JD-FIN-001",
        "Finance Controller",
        "Finance Controller",
        "CFO / CEO",
        "PROC-FIN-001",
        """Financial controls: month-end close, SoD, expenses, invoicing, payroll oversight interface, and audit trail for SOC 2 CC1/CC2.""",
        [
            "Own PROC-FIN-001 and financial control checklist",
            "Approve spend above delegated thresholds with procurement",
            "Support external financial audit evidence",
            "Interface with payroll (PROC-PAY-001) on compensation data",
            "Report material risks to executive and ISMS",
        ],
        [
            "Qualified accountant or equivalent experience",
            "Internal controls and SoD design",
            "SaaS revenue recognition familiarity (if applicable)",
        ],
        ["PROC-FIN-001", "FINANCE-BIBLE", "PROC-PAY-001"],
    ),
    (
        "JD-LEG-001",
        "Legal Counsel",
        "Legal Counsel",
        "CEO / Board",
        "PROC-LEG-001",
        """Contract intake, review tiers, signature authority, litigation hold, regulatory correspondence, and IP programme (PROC-IP-001) coordination.""",
        [
            "Review customer, supplier, and employment contracts",
            "Maintain contract repository and approval matrix",
            "Advise on regulatory investigations and ICO matters with DPO",
            "Support procurement legal due diligence (PROC-PRM-001)",
            "Oversee OSS licence and IP assignment compliance",
        ],
        [
            "Solicitor or qualified in-house counsel (UK)",
            "SaaS/commercial contract experience",
            "Data protection and IP basics",
        ],
        ["PROC-LEG-001", "PROC-IP-001", "LEGAL-BIBLE", "POL-SUP-001"],
    ),
    (
        "JD-PRM-001",
        "Procurement Lead",
        "Procurement / Commercial",
        "Finance Controller",
        "POL-SUP-001",
        """Purchase authorisation, tender thresholds, supplier due diligence, DPA/SCC tracking, and alignment with compliance supplier register.""",
        [
            "Run PROC-PRM-001 for new and renewing suppliers",
            "Ensure SUP register and DPA status before go-live",
            "Coordinate security questionnaires with CISO",
            "Maintain approved vendor list and spend controls",
        ],
        [
            "Commercial procurement in technology sector",
            "Vendor risk and contract basics",
            "Experience with GDPR supplier clauses",
        ],
        ["PROC-PRM-001", "PROCUREMENT-BIBLE", "POL-SUP-001"],
    ),
    (
        "JD-HSE-001",
        "Health & Safety Lead",
        "Health & Safety Lead",
        "COO / ISMS Lead",
        "PROC-HSE-001",
        """Workplace H&S: risk assessments, RIDDOR reporting path, DSE, contractor induction, and alignment with ISO 45001 where applicable.""",
        [
            "Maintain H&S risk register and PROC-HSE-001 evidence",
            "Investigate incidents and near-misses",
            "Coordinate fire safety and premises with facilities (PROC-BLD-001)",
            "Report notifiable events per UK requirements",
        ],
        [
            "NEBOSH or IOSH qualification preferred",
            "UK H&S regulatory familiarity",
            "Remote/hybrid and contractor workforce experience",
        ],
        ["PROC-HSE-001", "HEALTH-SAFETY-BIBLE", "PROC-BLD-001"],
    ),
    (
        "JD-IT-001",
        "IT Operations Lead",
        "IT Operations Lead",
        "CTO / CISO",
        "PROC-IT-001",
        """ITSM: service desk, asset inventory, backup verification, patch cadence, SaaS admin, and CAB linkage for infrastructure changes.""",
        [
            "Execute PROC-IT-001 and IT bible controls",
            "Own asset inventory and endpoint management",
            "Verify backups per PROC-BCP-001",
            "Administer SaaS tenants with least privilege",
            "Support IAM provisioning workflow",
        ],
        [
            "ITIL foundation or equivalent operations experience",
            "Cloud SaaS administration",
            "Backup/restore and patch management",
        ],
        ["PROC-IT-001", "PROC-BCP-001", "PROC-IAM-001", "IT-BIBLE"],
    ),
    (
        "JD-DAT-001",
        "Data Governance Lead",
        "Data Governance Lead",
        "DPO / ISMS Lead",
        "PROC-DAT-001",
        """Enterprise data management: classification, retention, master data ownership, quality metrics, archive/deletion aligned with ROPA.""",
        [
            "Maintain data classification and retention schedules",
            "Assign data owners for key domains",
            "Coordinate deletion/archival with engineering",
            "Support DPIAs and ROPA updates with DPO",
            "Run PROC-DAT-001 quarterly reviews",
        ],
        [
            "Data governance or information management experience",
            "GDPR retention and minimisation principles",
            "Cross-functional stakeholder management",
        ],
        ["PROC-DAT-001", "DATA-MANAGEMENT-BIBLE", "ROPA", "POL-PRI-001"],
    ),
]


def render_jd(
    jd_id: str,
    title: str,
    short_name: str,
    reports_to: str,
    authority: str,
    summary: str,
    responsibilities: list[str],
    qualifications: list[str],
    artefacts: list[str],
) -> str:
    resp_lines = "\n".join(f"- {r}" for r in responsibilities)
    qual_lines = "\n".join(f"- {q}" for q in qualifications)
    art_lines = "\n".join(f"- [{a}](../{'compliance' if a.isupper() and '-' in a else 'procedures' if a.startswith('PROC') else 'bibles'}/{a}.md)" if not a.endswith(".md") else f"- {a}" for a in artefacts)
    # Fix artefact links properly
    art_links = []
    for a in artefacts:
        if a.startswith("PROC-"):
            # find file - use INDEX pattern
            art_links.append(f"- Procedure and related artefacts: `{a}` (see [procedures INDEX](../procedures/INDEX.md))")
        elif a.endswith("-BIBLE"):
            art_links.append(f"- [{a}](../bibles/{a}.md)")
        elif a in ("ROPA", "FRAMEWORK"):
            path = "ROPA.md" if a == "ROPA" else "../../FRAMEWORK.md"
            folder = "compliance" if a == "ROPA" else ""
            if folder:
                art_links.append(f"- [{a}](../compliance/{path})")
            else:
                art_links.append(f"- [{a}](../../FRAMEWORK.md)")
        else:
            art_links.append(f"- [{a}](../compliance/{a}.md)")
    art_block = "\n".join(art_links)

    return f"""# {jd_id} — {title}

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Status:** Template — requires executive appointment and compensation band  
**Reports to:** {reports_to}  
**Authority reference:** {authority}

---

## 1. Role summary

{summary}

This job description supports Magna Carta compliance evidence (ISO 27001 A.5/A.6, SOC 2 CC1). **Appointment and live HRIS record remain operational (🎯).**

---

## 2. Key responsibilities

{resp_lines}

---

## 3. Qualifications & experience

{qual_lines}

---

## 4. Compliance artefacts owned or consulted

{art_block}

- [RACI-MATRIX.md](../governance/RACI-MATRIX.md)
- [TEMPLATE-JOB-DESCRIPTION.md](../templates/TEMPLATE-JOB-DESCRIPTION.md)

---

## 5. Performance indicators

| Indicator | Target |
|-----------|--------|
| Procedure reviews completed on schedule | 100% of owned PROC-* annual reviews |
| Audit / CAPA items for domain | Closed within agreed SLA |
| Training & attestation | Role holder completes PROC-TRN-001 |

---

## 6. Working relationships

| Stakeholder | Interaction |
|-------------|-------------|
| ISMS Lead | Framework mapping, audit evidence |
| Executive / Board | Escalation, resource approval |
| Peer process owners | Cross-domain PROC-CMP-001 |

---

**Approved by:** _________________ **Date:** _________
"""


def main() -> None:
    JD_DIR.mkdir(parents=True, exist_ok=True)
    index_rows = []
    for row in ROLES:
        jd_id, title, short_name, reports_to, authority, summary, resp, qual, arts = row
        filename = f"{jd_id}-{title.split('(')[0].strip().replace(' / ', '-').replace(' ', '-')}.md"
        filename = filename.replace("--", "-").replace("(-", "").replace(")", "")
        # Simpler filenames
        slug_map = {
            "JD-ISMS-001": "JD-ISMS-001-ISMS-Lead.md",
            "JD-PRI-001": "JD-PRI-001-Data-Protection-Officer.md",
            "JD-SEC-001": "JD-SEC-001-CISO.md",
            "JD-CAB-001": "JD-CAB-001-CAB-Chair.md",
            "JD-ENG-001": "JD-ENG-001-Engineering-Lead.md",
            "JD-AI-001": "JD-AI-001-AI-Governance-Lead.md",
            "JD-HR-001": "JD-HR-001-HR-People-Lead.md",
            "JD-FIN-001": "JD-FIN-001-Finance-Controller.md",
            "JD-LEG-001": "JD-LEG-001-Legal-Counsel.md",
            "JD-PRM-001": "JD-PRM-001-Procurement-Lead.md",
            "JD-HSE-001": "JD-HSE-001-Health-Safety-Lead.md",
            "JD-IT-001": "JD-IT-001-IT-Operations-Lead.md",
            "JD-DAT-001": "JD-DAT-001-Data-Governance-Lead.md",
        }
        filename = slug_map[jd_id]
        path = JD_DIR / filename
        path.write_text(
            render_jd(jd_id, title, short_name, reports_to, authority, summary, resp, qual, arts),
            encoding="utf-8",
        )
        index_rows.append((jd_id, title, short_name, filename))
        print(f"Wrote {path.relative_to(ROOT)}")

    index = """# Job Descriptions Index

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** HR / ISMS Lead

---

## Purpose

Role definitions required for ISO 27001 organisational controls, SOC 2 CC1, and departmental PROC-* ownership. **Templates until named individuals are appointed in HRIS (🎯).**

Template: [TEMPLATE-JOB-DESCRIPTION.md](../templates/TEMPLATE-JOB-DESCRIPTION.md)

---

## Register

| ID | Role | Short name | Document |
|----|------|------------|----------|
"""
    for jd_id, title, short_name, filename in index_rows:
        index += f"| {jd_id} | {title} | {short_name} | [{filename}]({filename}) |\n"

    index += """
---

## Related

- [COMPLIANCE-BLUEPRINT.md](../compliance/COMPLIANCE-BLUEPRINT.md) §3
- [RACI-MATRIX.md](../governance/RACI-MATRIX.md)
- [HR-BIBLE.md](../bibles/HR-BIBLE.md)
"""
    (JD_DIR / "INDEX.md").write_text(index, encoding="utf-8")
    print("Wrote docs/job-descriptions/INDEX.md")


if __name__ == "__main__":
    main()
