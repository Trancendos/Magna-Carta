# UK PECR Alignment Programme

**Version:** 1.0.0  
**Date:** 2026-06-07  
**Owner:** DPO  
**Legislation:** Privacy and Electronic Communications Regulations 2003 (PECR)  
**Register:** LEG-005

---

## 1. Applicability

PECR applies to Trancendos when the platform or marketing activities involve:

| Activity | PECR rule | Trancendos scope |
|----------|-----------|------------------|
| Marketing emails/SMS to individuals | Reg 22 | Product updates, newsletters (if sent) |
| Cookies and similar technologies | Reg 6 | Web app, Town Hall portal, analytics |
| Electronic communications security | Reg 5 | TLS, service integrity (overlap ISO 27001) |
| Location data | Reg 14 | Only if location features enabled |

**Position:** PECR programme implemented for cookie/consent and electronic marketing controls. ICO registration tracked separately ([ICO-REGISTRATION.md](ICO-REGISTRATION.md)).

---

## 2. Control mapping

### 2.1 Cookies and similar technologies (Reg 6)

| Requirement | Control | Evidence |
|-------------|---------|----------|
| Inform users about cookies | Privacy notice + cookie banner (when non-essential cookies used) | POL-PRI-001 §cookies |
| Consent before non-essential cookies | Consent manager integration (or no non-essential cookies) | ROPA; deployment config |
| Essential cookies documented | Session, auth, security cookies listed | Privacy notice annex |

**Default posture:** Self-hosted Tranc3 minimises third-party marketing/analytics cookies. Any non-essential cookie requires opt-in before placement.

### 2.2 Electronic marketing (Reg 22)

| Channel | Lawful basis | Control |
|---------|--------------|---------|
| Email marketing | Consent or soft opt-in (existing customer, similar products) | Consent record; unsubscribe |
| SMS marketing | Consent | Double opt-in where used |
| B2B corporate email | Legitimate interest assessment if no consent | LIA documented |

| Prohibited | Enforcement |
|------------|-------------|
| Marketing without valid consent/soft opt-in | DPO review before campaign |
| Pre-ticked marketing consent | UI must not use pre-ticked boxes |
| Failure to honour unsubscribe | 48h suppression list update |

### 2.3 Security of communications (Reg 5)

Covered by POL-SEC-001, TLS at Traefik, and DEFSTAN network controls — cross-reference only.

---

## 3. Obligations

| OBL-ID | Obligation | Status |
|--------|------------|--------|
| OBL-110 | Cookie transparency and consent | ✅ Programme |
| OBL-111 | Electronic marketing rules | ✅ Programme |
| OBL-112 | Unsubscribe / suppression | ✅ Programme |

*Add OBL-110–112 to OBLIGATIONS-REGISTER on next quarterly sync.*

---

## 4. ePrivacy Directive (EU)

Where EU users access the platform, ePrivacy cookie rules align with PECR controls above. GDPR lawful basis documented in ROPA.

---

## 5. Review

| Activity | Frequency |
|----------|-----------|
| Cookie inventory | Annual or on new tracking tool |
| Marketing consent audit | Quarterly |
| Privacy notice PECR section | Annual |

**Next review:** 2026-09-06

---

## 6. Related documents

- [POL-PRI-001](../policies/POL-PRI-001-Data-Protection-Privacy.md)
- [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md) — LEG-005
- [REGULATION-MATRIX.md](REGULATION-MATRIX.md)
- [ICO-REGISTRATION.md](ICO-REGISTRATION.md)
