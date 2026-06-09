# Harmonised Standards Monitoring

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** ISMS Lead / AI Lead  
**Status:** ✅ Programme — structured ETSI + CEN/CENELEC watch (replaces ad-hoc standards checks)

**ETSI alignment:** [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md)  
**EU legislation:** [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md) (ACT-014)  
**Machine-readable:** [compliance/standards_watch.yaml](../../compliance/standards_watch.yaml)

---

## 1. Purpose

Tracks **technical standards** relevant to Magna Carta compliance — especially ETSI Securing AI deliverables from [www.etsi.org/deliver/etsi_en](https://www.etsi.org/deliver/etsi_en) and **CEN/CENELEC JTC21** harmonised standards under the EU AI Act.

This register answers:

- Which ETSI EN/TS/TR editions we reference in programme docs
- Whether a standard is **harmonised** (OJEU-listed) vs **reference only**
- When to update mappings after new publications

**Architecture note:** EU AI Act harmonised standards are coordinated by **CEN/CENELEC JTC21**. ETSI TC SAI contributes security deliverables (e.g. EN 304 223) per European Commission requests; presumption of conformity follows **OJEU citation**, not ETSI publication alone.

---

## 2. ETSI deliverables in scope

| STD-WATCH | Standard | Type | Programme status | Harmonised |
|-----------|----------|------|------------------|------------|
| STD-WATCH-001 | [ETSI EN 304 223](https://www.etsi.org/deliver/etsi_en/304200_304299/304223/) V2.1.1 | EN | ✅ Programme (STD-042) | No |
| STD-WATCH-002 | ETSI TS 104 223 | TS | Reference | No |
| STD-WATCH-003 | ETSI TR 104 128 | TR | Reference (superseded) | No |
| STD-WATCH-004 | [ETSI TR 104 065](https://www.etsi.org/deliver/etsi_tr/104000_104099/104065/) | TR | Reference (AI Act map) | No |
| STD-WATCH-005 | [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) V3.1.3 | EN | Monitor | Published; OJEU status varies by context |

Full metadata: `compliance/standards_watch.yaml` → `active_standards`.

---

## 3. Harmonised standards watch (CEN/CENELEC JTC21)

| Topic | Draft / standard | Status | Programme impact |
|-------|------------------|--------|------------------|
| QMS for AI (Art. 17) | prEN 18286 | Monitor | ISO 42001 gap; future QMS evidence |
| Risk management (Art. 9) | JTC21 in development | Monitor | PROC-AI-003; RISK-009–012 |
| Cybersecurity for AI | ETSI EN 304 223 | Monitor | ETSI-SAI-ALIGNMENT; watch OJEU |
| GPAI obligations | EUR-Lex delegated acts | Monitor | ACT-014; model cards |

YAML: `standards_watch.yaml` → `harmonised_standards_watch`.

---

## 4. Semi-annual review workflow (ACT-015)

**Cadence:** Semi-annual, aligned with PROC-CMP-001 (offset from quarterly EUR-Lex scan).  
**First run due:** 2026-12-31 (see ACT-015).

### Step 1 — ETSI deliverable check (20 min)

For each `active_standards` entry with status Programme or Monitor:

1. Open `etsi_deliver_uri` (or ETSI EN index).
2. Confirm edition/version unchanged or note new publication.
3. Update `standards_watch.yaml` `version`, `published`, `review_date` if changed.

### Step 2 — Harmonised standards check (30 min)

1. Check [CEN/CENELEC JTC21](https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/) for new drafts or EN publications.
2. Cross-check EUR-Lex (LEG-006) for **OJEU references** to harmonised standards.
3. Update `harmonised_standards_watch.items[].last_checked` and `status`.

### Step 3 — Programme impact (15 min)

| If… | Then… |
|-----|-------|
| New EN 304 223 edition | Review ETSI-SAI-ALIGNMENT; schedule PROC-AI-003 delta |
| prEN 18286 → EN + OJEU | Open gap assessment vs ISO 42001; legal review for conformity claims |
| EN 303 645 relevant to new product | Assess consumer IoT scope; update REGULATION-MATRIX |
| No material change | Record "no change" in PROC-CMP-001 minutes |

### Step 4 — Cross-register sync

- Update [STANDARDS-REGISTER.md](STANDARDS-REGISTER.md) if STD-042/043 status changes
- Link findings to ACT-014 if delegated acts overlap
- Close or extend ACT-015; schedule next semi-annual run

---

## 5. Monitoring sources

| Source ID | URI | Use |
|-----------|-----|-----|
| ETSI-EN-INDEX | https://www.etsi.org/deliver/etsi_en | Browse EN deliverables |
| ETSI-SAI-WORK | https://portal.etsi.org/tb.aspx?tbid=955&SubTB=955 | TC SAI work programme |
| CEN-CENELEC-JTC21 | https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/ | Harmonised AI standards |
| EUR-LEX-HARMONISED | CELEX 32024R1689 consolidated text | OJEU harmonised standard citations |

Also in `standards_watch.yaml` → `monitoring_sources`.

---

## 6. Review log (operational)

| Date | Reviewer | Summary | Next due |
|------|----------|---------|----------|
| 2026-06-08 | Programme | Initial register; EN 304 223 V2.1.1 recorded; harmonised watch seeded | 2026-12-31 🎯 ACT-015 |

---

## 7. Related documents

- [ETSI-SAI-ALIGNMENT.md](ETSI-SAI-ALIGNMENT.md)
- [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md)
- [STANDARDS-REGISTER.md](STANDARDS-REGISTER.md) — STD-042, STD-043
- [COMPLIANCE-ACTION-TRACKER.md](COMPLIANCE-ACTION-TRACKER.md) — ACT-015
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md)
