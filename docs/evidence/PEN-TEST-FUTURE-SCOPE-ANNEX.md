# Penetration Test — Future Scope Annex

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** Security Ops  
**Parent:** [PEN-TEST-PROGRAMME.md](PEN-TEST-PROGRAMME.md)

---

## 1. Purpose

Document **optional and future** penetration-test scopes so customer RFPs, ISO/SOC audits, and defence-adjacent opportunities can be covered without ad-hoc policy gaps. Default annual scope remains in PEN-TEST-PROGRAMME §2.

| Symbol | Meaning |
|--------|---------|
| ✅ **Programme** | Scope definitions ready for contract inclusion |
| 🎯 **Operational** | Test executed under signed rules of engagement |

---

## 2. Scope catalogue

| Scope ID | Test type | Default annual programme | When to add | Preconditions |
|----------|-----------|--------------------------|-------------|---------------|
| PT-CORE | External API/auth/perimeter | ✅ In scope | Always | ACT-005 |
| PT-INT | Internal segmentation | ⚠️ Optional | Multi-tenant or regulated customer | Staging VLAN mirror |
| PT-SOCENG | Phishing / vishing | ❌ Out of scope | Customer contract or insurance requirement | HR/legal approval; no production cred harvest |
| PT-DOS | Application DoS | ❌ Out of scope | Explicit customer demand | Ops window; rate-limit coordination |
| PT-PHY | Physical intrusion | ❌ N/A | Never (cloud-only) | — |
| PT-AI | Prompt injection / model abuse | ⚠️ Emerging | AI feature in scope for customer | AI red-team methodology agreed |
| PT-SUP | Supply-chain / dependency | ⚠️ Optional | Post-major vendor incident | SBOM provided |

---

## 3. Social engineering (PT-SOCENG)

If activated:

1. Legal approves scope and authorised targets list
2. HR notifies leadership; no punitive action against simulated victims
3. Provider uses Trancendos-approved domains only
4. Findings feed PROC-TRN-001 awareness refresh
5. No capture of production passwords — simulation only

---

## 4. Denial of service (PT-DOS)

If activated:

1. Written change window with Operations and Traefik owners
2. Rate limits documented; abort threshold defined
3. Conduct in staging unless production explicitly authorised
4. Post-test capacity review to CAB

---

## 5. AI / LLM testing (PT-AI)

Align with [PROC-AI-002](../procedures/PROC-AI-002-Fairness-Bias-Testing.md) and OWASP LLM Top 10:

- Prompt injection and jailbreak attempts
- Data exfiltration via tool calling
- Model denial-of-wallet (cost abuse) — coordinate with rate limits

---

## 6. Contract language (summary)

Include in pen-test SOW when extending scope:

> Optional modules PT-SOCENG, PT-DOS, PT-AI are executed only when listed in the signed Statement of Work, subject to Trancendos rules of engagement and operational approval.

---

## 7. Related documents

- [PEN-TEST-PROGRAMME.md](PEN-TEST-PROGRAMME.md)
- [PROC-VUL-001](../procedures/PROC-VUL-001-Vulnerability-Management.md)
- [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) §6
