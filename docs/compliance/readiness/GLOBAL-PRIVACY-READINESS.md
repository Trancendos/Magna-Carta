# Global Privacy — Readiness

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** DPO  
**Covers:** FW-110–FW-130

---

## 1. Approach

Magna Carta maintains a **GDPR-first privacy programme** (UK/EU). Other jurisdictions are mapped for:

- Expansion triggers (entity, data subjects, marketing)
- Customer DPA / SCC requirements
- Questionnaire response consistency

**Programme ✅ ≠ legal compliance in that jurisdiction** until triggers activate and local notices/contracts are deployed.

---

## 2. Core programmes (active)

| FW-ID | Law | Status | Primary artefact |
|-------|-----|--------|------------------|
| FW-110 | GDPR (UK/EU) | ✅ Programme / ✅ Operational (Tranc3) | [GDPR-ALIGNMENT.md](../GDPR-ALIGNMENT.md), POL-PRI-001, PROC-DSR-001 |
| FW-112 | CCPA/CPRA | ✅ Programme | [CCPA-CPRA-ALIGNMENT.md](../CCPA-CPRA-ALIGNMENT.md) |
| FW-116 | Brazil LGPD | ✅ Programme (future) | [LGPD-READINESS.md](../LGPD-READINESS.md) |
| FW-130 | South Africa POPIA | ✅ Programme (future) | [POPIA-READINESS.md](../POPIA-READINESS.md) |

---

## 3. Transfer mechanisms (FW-111 EU-U.S. DPF)

| Mechanism | When used | Status |
|-----------|-----------|--------|
| UK IDTA / EU SCCs | UK/EU → third countries | ✅ Programme |
| EU-U.S. Data Privacy Framework | US suppliers on DPF list | 📋 Verify per subprocessor |
| BCRs | Group transfers | ❌ Not adopted |

Before enabling US AI fallback (SUP-004): complete TIA per [TEMPLATE-TIA-US-AI-FALLBACK.md](../../templates/TEMPLATE-TIA-US-AI-FALLBACK.md) — ACT-010.

---

## 4. Future jurisdiction matrix

| FW-ID | Jurisdiction | Key themes | Activation trigger | Baseline control |
|-------|--------------|------------|-------------------|------------------|
| FW-113 | Canada | PIPEDA, Quebec Law 25 | CA users / entity | GDPR programme + local notice |
| FW-114 | Australia | Privacy Act, APPs | AU users / entity | GDPR + breach notification |
| FW-115 | Argentina | PDPA | AR operations | GDPR mapping |
| FW-117 | Chile | Law 19.628 / new bill | CL operations | GDPR mapping |
| FW-118 | Mexico | LFPDPPP | MX operations | GDPR mapping |
| FW-119 | Hong Kong | PDPO | HK data subjects | GDPR mapping |
| FW-120 | India | DPDP Act 2023 | IN operations / significant users | DPO appointment, consent |
| FW-121 | Indonesia | PDP Law | ID operations | GDPR + SNI readiness |
| FW-122 | Japan | APPI | JP operations | Privacy programme + ISMAP if gov |
| FW-123 | Korea | PIPA | KR operations | GDPR + K-ISMS if required |
| FW-124 | Malaysia | PDPA 2010 | MY operations | GDPR mapping |
| FW-125 | New Zealand | Privacy Act 2020 | NZ operations | GDPR mapping |
| FW-126 | Philippines | DPA 2012 | PH operations | GDPR mapping |
| FW-127 | Singapore | PDPA | SG operations | MTCS if government |
| FW-128 | Taiwan | PDPA | TW operations | GDPR mapping |
| FW-129 | Thailand | PDPA | TH operations | GDPR mapping |

---

## 5. Implementation playbook (on trigger)

1. **Legal assessment** — Confirm controller/processor role and local representative need
2. **ROPA update** — Add jurisdiction in Tranc3 ROPA
3. **Notice update** — Privacy policy / local language annex
4. **Rights procedure** — Extend PROC-DSR-001 timelines per local law
5. **Contract** — DPA/SCC or local equivalent in customer agreements
6. **Register** — Update [LEGISLATION-REGISTER.md](../LEGISLATION-REGISTER.md) and FW row to ⚠️ Applicable

---

## 6. Cross-reference

- [LEGISLATION-REGISTER.md](../LEGISLATION-REGISTER.md)
- [OBLIGATIONS-REGISTER.md](../OBLIGATIONS-REGISTER.md)
- [PRIVACY-BIBLE.md](../../bibles/PRIVACY-BIBLE.md)

---

**Next review:** 2026-09-06
