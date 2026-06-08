# RUN-PECR-001 — PECR Cookie & Consent Deployment

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** DPO / Platform Engineering  
**Alignment:** [PECR-ALIGNMENT.md](../compliance/PECR-ALIGNMENT.md) (LEG-005)  
**Policy:** POL-PRI-001

---

## 1. Purpose

Deploy and verify **PECR Reg 6** cookie controls before any release that adds or changes non-essential cookies, analytics, or third-party embeds on Tranc3, Town Hall, or marketing sites.

**Default posture:** Self-hosted stack uses **essential cookies only** (session, auth, CSRF). Any non-essential cookie requires documented consent.

---

## 2. Cookie classification

| Type | Examples | Consent required |
|------|----------|------------------|
| Strictly necessary | Session ID, auth token, load balancer | No |
| Functional | UI preferences (non-tracking) | Best practice yes; legal case-by-case |
| Analytics | Plausible, GA, PostHog (if added) | **Yes — opt-in before set** |
| Marketing | Ad pixels, retargeting | **Yes — opt-in** |

Maintain inventory in privacy notice annex and ROPA.

---

## 3. Pre-deployment checklist

| # | Check | Owner |
|---|-------|-------|
| 1 | List every cookie name, domain, purpose, expiry | DPO + Engineering |
| 2 | Classify essential vs non-essential | DPO |
| 3 | Non-essential: consent manager blocks script until opt-in | Engineering |
| 4 | Privacy notice and cookie policy updated | DPO |
| 5 | No pre-ticked marketing consent boxes | Product |
| 6 | Withdraw consent path documented | Product |
| 7 | Staging tested with browser devtools (Application → Cookies) | QA |

---

## 4. Deployment steps

1. **Branch** — feature behind flag if possible
2. **Config** — document env vars / Traefik / frontend bundle changes
3. **Consent layer** — load non-essential scripts only after `consent.analytics === true` (or equivalent)
4. **Verify staging** — incognito: no non-essential cookies before accept; essential only after reject
5. **Change record** — PROC-CHG-001 or standard CAB entry
6. **Production** — deploy; smoke test cookie banner and reject/accept paths
7. **Evidence** — screenshot + cookie table attached to change ticket

---

## 5. Marketing email / SMS (Reg 22)

Before any campaign:

| Check | Requirement |
|-------|-------------|
| Lawful basis | Consent record or documented soft opt-in |
| Unsubscribe | One-click; honoured within 48h |
| B2B cold email | LIA on file if relying on legitimate interest |
| DPO sign-off | Required for new list sources |

---

## 6. Rollback

If non-essential cookies fire without consent:

1. **Disable** feature flag or revert deployment
2. **Purge** CDN cache if script cached
3. **Incident** — P2 minimum; P1 if widespread tracking before consent
4. **CAPA** — PROC-CAPA-001 if process failure

---

## 7. Review

| Activity | Frequency |
|----------|-----------|
| Cookie inventory audit | Quarterly (PROC-CMP-001) |
| Third-party script review | On each vendor change |

**Next review:** 2026-09-06
