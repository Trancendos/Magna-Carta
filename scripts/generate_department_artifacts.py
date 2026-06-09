#!/usr/bin/env python3
"""Generate department PROC/COOK/HYMN triads and bibles for Magna Carta."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# code, bible filename stem, procedure title, owner, policy refs, domain summary
DOMAINS = [
    (
        "HSE",
        "HEALTH-SAFETY-BIBLE",
        "Workplace Health & Safety",
        "Health & Safety Lead / ISMS",
        "POL-SEC-001, ISO 45001 alignment",
        "Workplace hazards, risk assessments, incident reporting (RIDDOR), DSE, contractor H&S induction.",
    ),
    (
        "FIN",
        "FINANCE-BIBLE",
        "Financial Controls & Reporting",
        "Finance Controller",
        "COMPANIES-ACT-ALIGNMENT, FCA-ALIGNMENT (perimeter)",
        "Month-end close, segregation of duties, expenses, invoicing, audit trail, HMRC obligations.",
    ),
    (
        "PRM",
        "PROCUREMENT-BIBLE",
        "Procurement & Supplier Engagement",
        "Procurement / Legal",
        "POL-SUP-001",
        "Purchase authorisation, tender thresholds, supplier due diligence, contract storage.",
    ),
    (
        "LEG",
        "LEGAL-BIBLE",
        "Legal & Contract Management",
        "Legal Counsel",
        "Templates in docs/templates/",
        "Contract intake, review tiers, signature authority, litigation hold, regulatory correspondence.",
    ),
    (
        "IP",
        "IP-BIBLE",
        "Intellectual Property Management",
        "Legal / Engineering Lead",
        "—",
        "Copyright, trade secrets, OSS licence compliance, employee invention assignment, brand assets.",
    ),
    (
        "PAY",
        "PAYROLL-BIBLE",
        "Payroll & Compensation Administration",
        "Finance / HR",
        "—",
        "Payroll runs, RTI, pensions auto-enrolment, expense reimbursement, confidentiality of pay data.",
    ),
    (
        "BLD",
        "BUILDING-BIBLE",
        "Building Regulations & Premises",
        "Facilities / ISMS",
        "—",
        "Fire safety, accessibility, electrical safety, homeworking ergonomics, visitor access.",
    ),
    (
        "IT",
        "IT-BIBLE",
        "IT Service Management",
        "IT Operations Lead",
        "POL-SEC-001, ITIL alignment",
        "Service desk, asset inventory, patch cadence, backup verification, SaaS admin, change linkage to CAB.",
    ),
    (
        "WLB",
        "WELLBEING-BIBLE",
        "Employee Wellbeing",
        "HR / People Lead",
        "—",
        "Wellbeing resources, reasonable adjustments, leave policies, workload reviews, ergonomic support.",
    ),
    (
        "MHL",
        "MENTAL-HEALTH-BIBLE",
        "Mental Health & Psychological Safety",
        "HR / Mental Health First Aiders",
        "—",
        "MHFA roster, crisis escalation, stigma-free reporting, return-to-work plans, occupational health referral.",
    ),
    (
        "UMG",
        "USER-MANAGEMENT-BIBLE",
        "Platform User Administration",
        "Platform Engineering / ISMS",
        "POL-SEC-001, PROC-IAM-001",
        "Customer tenant admin, role templates, privileged support access, break-glass, audit of admin actions.",
    ),
    (
        "DAT",
        "DATA-MANAGEMENT-BIBLE",
        "Enterprise Data Management",
        "DPO / Data Governance Lead",
        "POL-PRI-001, ROPA",
        "Data classification, retention schedules, master data ownership, quality metrics, archive/deletion.",
    ),
]

HR_BIBLE_ONLY = True  # PROC-HR-001 already exists

BIBLE_MAP = {
    "HSE": "HEALTH-SAFETY-BIBLE",
    "FIN": "FINANCE-BIBLE",
    "PRM": "PROCUREMENT-BIBLE",
    "LEG": "LEGAL-BIBLE",
    "IP": "IP-BIBLE",
    "PAY": "PAYROLL-BIBLE",
    "BLD": "BUILDING-BIBLE",
    "IT": "IT-BIBLE",
    "WLB": "WELLBEING-BIBLE",
    "MHL": "MENTAL-HEALTH-BIBLE",
    "UMG": "USER-MANAGEMENT-BIBLE",
    "DAT": "DATA-MANAGEMENT-BIBLE",
}


def slugify(title: str) -> str:
    return (
        title.replace(" & ", "-")
        .replace("&", "and")
        .replace(" ", "-")
        .replace("--", "-")
    )


def write_proc(code: str, title: str, owner: str, policies: str, summary: str) -> None:
    slug = slugify(title)
    path = ROOT / f"docs/procedures/PROC-{code}-001-{slug}.md"
    if path.exists():
        return
    bible = BIBLE_MAP[code]
    content = f"""# PROC-{code}-001 — {title}

**Version:** 1.0.0 · **Owner:** {owner} · **Policies:** {policies}

---

## 1. Purpose

{summary}

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Procedure documented in Magna Carta |
| 🎯 **Operational** | Executed with vendor systems, attestations, or external sign-off |

---

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| Trancendos personnel, systems, and contractors under our control | Customer tenant policies (unless contractually required) |
| Evidence suitable for ISO 27001 / SOC 2 personnel & ops clauses | Formal legal opinion (escalate to Legal) |

---

## 3. Roles

| Role | Responsibility |
|------|----------------|
| Process owner | Maintain procedure; train practitioners; annual review |
| ISMS Lead | Map controls to frameworks; PROC-CMP-001 input |
| DPO / Security | Consult when personal data or security impact |
| Executive | Approve exceptions and resource allocation |

---

## 4. Process overview

1. **Trigger** — Scheduled review, event, or audit finding
2. **Triage** — Classify severity / regulatory reporting need
3. **Execute** — [COOK-{code}-001](../cookbooks/COOK-{code}-001-{slug}.md)
4. **Checklist** — [HYMN-{code}-001](../hymn-sheets/HYMN-{code}-001-{slug}-Checklist.md)
5. **Close** — Record evidence; raise CAPA if gap found

---

## 5. Key controls

- Segregation of duties where financial or legal commitment involved
- Documented approvals above delegated authority thresholds
- Alignment with [RACI-MATRIX.md](../governance/RACI-MATRIX.md)
- Cross-link to [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) for honest 🎯 items

---

## 6. Records

| Record | Retention | Owner |
|--------|-----------|-------|
| Workflow tickets / forms | Per statutory minimum (typically 3–7 years) | Process owner |
| Management review input | 5 years | ISMS Lead |

---

## 7. Related documents

- [{bible}](../bibles/{bible}.md)
- [COMPLIANCE-MATURITY-AND-BENCHMARK.md](../compliance/COMPLIANCE-MATURITY-AND-BENCHMARK.md)
"""
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def write_cook(code: str, title: str, slug: str | None = None) -> None:
    slug = slug or slugify(title)
    path = ROOT / f"docs/cookbooks/COOK-{code}-001-{slug}.md"
    if path.exists():
        return
    content = f"""# COOK-{code}-001 — {title} Playbook

**Version:** 1.0.0  
**Owner:** See [PROC-{code}-001](../procedures/PROC-{code}-001-{slug}.md)  
**Procedure:** PROC-{code}-001  
**Hymn sheet:** [HYMN-{code}-001](../hymn-sheets/HYMN-{code}-001-{slug}-Checklist.md)

---

## When to use

Scheduled review, audit preparation, or operational event requiring {title.lower()} workflow.

---

## Steps

1. Open hymn sheet and confirm trigger applies
2. Gather evidence from last review cycle
3. Walk control checklist with process owner
4. Log gaps in CAPA register if severity ≥ medium
5. Update domain bible § status if material change
6. File evidence reference in compliance review pack (PROC-CMP-001)

---

## Escalation

| Condition | Action |
|-----------|--------|
| Regulatory reportable event | PROC-IR-001 + Legal/DPO |
| Financial materiality | Finance Controller + Executive |
| Safety imminent danger | Stop work; escalate per HSE bible |
"""
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def write_hymn(code: str, title: str, slug: str | None = None) -> None:
    slug = slug or slugify(title)
    path = ROOT / f"docs/hymn-sheets/HYMN-{code}-001-{slug}-Checklist.md"
    if path.exists():
        return
    content = f"""# HYMN-{code}-001 — {title} Checklist

**Version:** 1.0.0 · **Procedure:** [PROC-{code}-001](../procedures/PROC-{code}-001-{slug}.md)

---

| # | Check | Done |
|---|-------|------|
| 1 | Trigger documented (date / ticket) | ☐ |
| 2 | Correct roles assigned per RACI | ☐ |
| 3 | Regulatory / contractual obligations identified | ☐ |
| 4 | Controls executed per COOK-{code}-001 | ☐ |
| 5 | Evidence stored with retention owner | ☐ |
| 6 | Gaps raised in CAPA if needed | ☐ |
| 7 | Procedure owner sign-off | ☐ |

**Sign-off:** _________________ Date: _________
"""
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def write_bible(filename: str, title: str, owner: str, proc_code: str, proc_title: str, policies: str, summary: str) -> None:
    path = ROOT / f"docs/bibles/{filename}.md"
    slug = slugify(proc_title)
    proc_file = f"PROC-{proc_code}-001-{slug}.md"
    content = f"""# {title} Bible

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** {owner}  
**Classification:** Internal — departmental reference

---

## 1. What this Bible is

Canonical reference for **{title.lower()}** at Trancendos. {summary}

**Honesty rule:** ✅ = programme artefact in Magna Carta. 🎯 = live execution, vendor contract, or external attestation required.

---

## 2. Core artefacts

| Type | ID | Status |
|------|-----|--------|
| Procedure | [PROC-{proc_code}-001](../procedures/{proc_file}) | ✅ Programme |
| Cookbook | [COOK-{proc_code}-001](../cookbooks/COOK-{proc_code}-001-{slug}.md) | ✅ Programme |
| Hymn sheet | [HYMN-{proc_code}-001](../hymn-sheets/HYMN-{proc_code}-001-{slug}-Checklist.md) | ✅ Programme |
| Policies | {policies} | See policies index |

---

## 3. Regulatory & framework alignment

| Framework | Relevance |
|-----------|-----------|
| ISO 27001 | Organisational controls where applicable |
| SOC 2 | CC1–CC5 depending on domain |
| UK employment / safety law | Where HR/HSE/MHL intersect |

Detail: [STANDARDS-AND-FRAMEWORKS-REGISTER.md](../compliance/STANDARDS-AND-FRAMEWORKS-REGISTER.md)

---

## 4. Key processes

```
Trigger → PROC-{proc_code}-001 → COOK-{proc_code}-001 → HYMN-{proc_code}-001 → Evidence → PROC-CMP-001
```

---

## 5. Registers & evidence

| Artefact | Path |
|----------|------|
| Coverage honesty | [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) |
| Maturity % | [COMPLIANCE-MATURITY-AND-BENCHMARK.md](../compliance/COMPLIANCE-MATURITY-AND-BENCHMARK.md) |
| RACI | [RACI-MATRIX.md](../governance/RACI-MATRIX.md) |
| Job descriptions | [job-descriptions/INDEX.md](../job-descriptions/INDEX.md) |

---

## 6. Operational gaps (honest)

| Gap | Blocker |
|-----|---------|
| Named process owner in production HRIS | 🎯 HR / exec appointment |
| Vendor or tooling integration | 🎯 Commercial selection |
| External attestation (audit, inspection) | 🎯 Schedule with third party |

---

## 7. Review

| Activity | Frequency |
|----------|-----------|
| Bible review | Annual |
| Procedure walkthrough | Quarterly sample |

**Next review:** 2027-06-09
"""
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def write_hr_bible() -> None:
    path = ROOT / "docs/bibles/HR-BIBLE.md"
    if path.exists():
        return
    content = """# Human Resources Bible

**Version:** 1.0.0  
**Date:** 2026-06-09  
**Owner:** HR / People Lead  
**Classification:** Internal — HR reference

---

## 1. What this Bible is

Canonical reference for **people operations** — screening, onboarding, training, movers, leavers, and personnel compliance evidence for ISO 27001 Clause 6 and SOC 2 CC1.

**Honesty rule:** PROC-HR-001 is ✅ programme. Background-check vendor and HRIS workflow remain 🎯.

---

## 2. Core artefacts

| Topic | Procedure | Cookbook | Hymn sheet |
|-------|-----------|----------|------------|
| Staff lifecycle | [PROC-HR-001](../procedures/PROC-HR-001-Staff-Lifecycle.md) | [COOK-HR-001](../cookbooks/COOK-HR-001-Staff-Lifecycle.md) | [HYMN-HR-001](../hymn-sheets/HYMN-HR-001-OnOffboard-Checklist.md) |
| Training | [PROC-TRN-001](../procedures/PROC-TRN-001-Security-Awareness-Attestation.md) | [COOK-TRN-001](../cookbooks/COOK-TRN-001-Policy-Attestation.md) | [HYMN-TRN-001](../hymn-sheets/HYMN-TRN-001-Policy-Attestation-Checklist.md) |
| Access | [PROC-IAM-001](../procedures/PROC-IAM-001-Access-Provisioning.md) | [COOK-IAM-001](../cookbooks/COOK-IAM-001-Access-Provisioning.md) | [HYMN-IAM-001](../hymn-sheets/HYMN-IAM-001-Access-Provisioning-Checklist.md) |

---

## 3. Screening tiers

See PROC-HR-001 §2 — standard vs privileged vs contractor paths.

---

## 4. Job descriptions

Role definitions: [job-descriptions/INDEX.md](../job-descriptions/INDEX.md)

---

## 5. Related compliance

| Framework | HR evidence |
|-----------|-------------|
| ISO 27001 A.6 | Screening, terms, disciplinary |
| SOC 2 CC1 | Integrity and competence |

---

## 6. Operational gaps

| Gap | ACT / blocker |
|-----|-------------|
| HRIS integration | Commercial HR platform 🎯 |
| Background check vendor | Contract + workflow 🎯 |
| Named HR Lead | Executive appointment 🎯 |

**Next review:** 2027-06-09
"""
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def main() -> None:
    for code, bible, title, owner, policies, summary in DOMAINS:
        slug = slugify(title)
        write_proc(code, title, owner, policies, summary)
        write_cook(code, title, slug)
        write_hymn(code, title, slug)
        write_bible(bible, title.replace(" Bible", "") if "Bible" in title else title, owner, code, title, policies, summary)
    write_hr_bible()
    print("Done.")


if __name__ == "__main__":
    main()
