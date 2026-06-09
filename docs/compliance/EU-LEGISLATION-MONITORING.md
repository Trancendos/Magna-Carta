# EU Legislation Monitoring Register

**Version:** 1.1.0  
**Date:** 2026-06-09  
**Owner:** DPO / AI Lead  
**Status:** ✅ Programme — structured EUR-Lex monitoring (replaces ad-hoc EU scans)

**Parallel (UK):** [UK-AI-LEGISLATION-MONITORING.md](UK-AI-LEGISLATION-MONITORING.md)  
**Identifiers:** [EUR-LEX-ELI-REFERENCE.md](EUR-LEX-ELI-REFERENCE.md)  
**Machine-readable:** [compliance/legislation_register.yaml](../../compliance/legislation_register.yaml)

---

## 1. Purpose

Tracks **EU legislative and sub-legislative change** (regulations, directives, delegated acts, implementing acts) so Magna Carta updates before new duties apply. Focus areas:

- EU AI Act (`32024R1689`) — delegated/implementing acts and standards
- EU GDPR (`32016R0679`) — guidance and consistency decisions (via EDPB)
- Watch-list acts: Data Act, NIS2, DORA (see `watch_list` in YAML)

This complements ICO/DSIT monitoring in the UK register; it does **not** duplicate UK AI White Paper tracking.

---

## 2. In-scope EU acts (active)

| LEG-ID | Act | CELEX | ELI (EN) | Owner |
|--------|-----|-------|----------|-------|
| LEG-003 | EU GDPR | 32016R0679 | [eli/reg/2016/679/oj/eng](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | DPO |
| LEG-006 | EU AI Act | 32024R1689 | [eli/reg/2024/1689/oj/eng](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) | AI Lead |

Full metadata: `compliance/legislation_register.yaml` → `active_legislation`.

---

## 3. Watch list (EU)

| WATCH-ID | Act | CELEX | Programme impact |
|----------|-----|-------|------------------|
| WATCH-003 | EU Data Act | 32023R2854 | Portability, cloud switching — future OBL rows |
| WATCH-004 | NIS2 Directive | 32022L2555 | Critical infrastructure scope assessment |
| WATCH-005 | DORA | 32022R2554 | FW-100; financial customer ICT supply chain |

---

## 4. Quarterly review workflow (ACT-014)

**Cadence:** Quarterly, aligned with PROC-CMP-001 (same window as UK legislation scan).  
**First baseline run:** 2026-06-09 (SCAN-2026-Q2-01 — ACT-014 closed as programme baseline). **Next quarterly run:** 2026-09-30.

### Step 1 — Parent act check (15 min)

For each active EU act in `legislation_register.yaml`:

1. Open `consolidated_text_uri` on EUR-Lex.
2. Note consolidation date; confirm no material amendment since last review.
3. Record "no change" or summary in PROC-CMP-001 minutes.

### Step 2 — Delegated & implementing acts (30 min)

**EU AI Act (priority):**

1. EUR-Lex expert search: CELEX `32024R1689` → related delegated/implementing acts.
2. Update `secondary_legislation_watch.items` in `legislation_register.yaml`:
   - `last_checked` date
   - `status`: monitor | triage | mapped
   - New topics → draft OBL-ID in OBLIGATIONS-REGISTER change log
3. Cross-check EU AI Office / Commission press pages for announcements not yet in EUR-Lex.

### Step 3 — Watch-list scan (15 min)

For WATCH-003–005:

1. Confirm applicability unchanged (customer sector, establishment, criticality).
2. If scope enters: raise ACT-### row; update REGULATION-MATRIX and COMPLIANCE-COVERAGE-REGISTER.

### Step 4 — Obligation impact (15 min)

| If change affects… | Update |
|--------------------|--------|
| AI transparency / risk / oversight | AI-GOVERNANCE §3, OBL-020–025 |
| Processor / transfer rules | GDPR-ALIGNMENT, supplier register |
| Financial ICT resilience | FCA-ALIGNMENT, FW-100 |

### Step 5 — Record outcomes

- PROC-CMP-001 minutes (Town Hall)
- OBLIGATIONS-REGISTER §5 change log
- Close or extend ACT-014; schedule next quarter

---

## 5. EUR-Lex tools

| Tool | URL | Use |
|------|-----|-----|
| ELI regulation index | [eur-lex.europa.eu/eli/reg](https://eur-lex.europa.eu/eli/reg) | Discover regulation URIs |
| Expert search | [eur-lex.europa.eu/expert-search.html](https://eur-lex.europa.eu/expert-search.html) | Delegated acts by parent CELEX |
| RSS (OJ L) | [EUR-Lex RSS help](https://eur-lex.europa.eu/content/help/oj/rss.html) | Optional automation |
| CELEX lookup | `legal-content/EN/TXT/?uri=CELEX:{id}` | Consolidated text |

Citation standards: [EUR-LEX-ELI-REFERENCE.md](EUR-LEX-ELI-REFERENCE.md).

---

## 6. Review log (operational)

| Scan ID | Date | Reviewer | Summary | Next due |
|---------|------|----------|---------|----------|
| SCAN-2026-Q2-01 | 2026-06-09 | AI Lead / DPO | No OJ-published delegated acts under CELEX 32024R1689 at scan date. GPAI Code of Practice published Jul 2025 — monitor. High-risk deadline 2 Aug 2026 — track Digital Omnibus proposals. `secondary_legislation_watch` last_checked → 2026-06-09. | 2026-09-30 |
| — | 2026-06-08 | Programme | Initial register seeded | 2026-09-30 🎯 |

**Evidence:** EEV-006 · [execution_evidence_register.yaml](../../compliance/execution_evidence_register.yaml)

---

## 7. Escalation

| Severity | Example | Action | Timeline |
|----------|---------|--------|----------|
| Informational | New delegated act proposed (consultation) | Watch list note | Next quarterly review |
| Material | Adopted delegated act affecting high-risk AI | Impact assessment | 10 business days |
| Urgent | Enforcement deadline &lt; 90 days | Executive + ACT-### | 5 business days |

---

## 8. Related documents

- [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md)
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md) §5
- [REGULATORS-OMBUDSMEN-REGISTER.md](REGULATORS-OMBUDSMEN-REGISTER.md) — REG-002, REG-003
- [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md) — ACT-014
- [HARMONISED-STANDARDS-MONITORING.md](HARMONISED-STANDARDS-MONITORING.md) — ACT-015 (semi-annual; cross-ref delegated acts)
- [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md)
- [COOK-CMP-001](../cookbooks/COOK-CMP-001-Quarterly-Compliance-Review.md)

**Next review:** 2026-09-06
