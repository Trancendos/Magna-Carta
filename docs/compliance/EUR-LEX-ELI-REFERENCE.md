# EUR-Lex and ELI Reference Guide

**Version:** 1.0.0  
**Date:** 2026-06-08  
**Owner:** DPO / Legal  
**Machine-readable register:** [compliance/legislation_register.yaml](../../compliance/legislation_register.yaml)  
**Review cycle:** Quarterly (with PROC-CMP-001)

---

## 1. Purpose

Magna Carta obligations and alignment documents cite **authoritative legal sources**. For EU law, the preferred identifiers are:

| Identifier | Use |
|----------|-----|
| **CELEX** | Stable catalogue number (e.g. `32024R1689`) |
| **ELI URI** | European Legislation Identifier — persistent URI to authentic OJ text |
| **OJ reference** | Official Journal citation for legal certainty |
| **Consolidated text** | EUR-Lex view incorporating amendments (verify date) |

This guide does **not** introduce new controls. It improves **citation accuracy**, **change detection**, and **audit traceability** for existing EU mappings (LEG-003, LEG-006, watch-list acts).

---

## 2. What `/eli/reg` is (and is not)

The EUR-Lex index [eur-lex.europa.eu/eli/reg](https://eur-lex.europa.eu/eli/reg) lists EU **regulations** (~144k entries). It is a browse/search index, not a single statute.

**Do:**

- Use ELI URIs for in-scope acts recorded in `legislation_register.yaml`
- Link obligations (OBL-020–025) to CELEX article anchors where helpful
- Monitor delegated/implementing acts under the EU AI Act parent CELEX

**Do not:**

- Bulk-import the full `/eli/reg` catalogue into Magna Carta
- Treat consolidated EUR-Lex HTML as a substitute for legal advice

---

## 3. ELI URI patterns

| Act type | Pattern | Example |
|----------|---------|---------|
| Regulation (OJ) | `https://eur-lex.europa.eu/eli/reg/{year}/{number}/oj/{lang}` | EU AI Act: `.../eli/reg/2024/1689/oj/eng` |
| Directive (OJ) | `https://eur-lex.europa.eu/eli/dir/{year}/{number}/oj/{lang}` | NIS2: `.../eli/dir/2022/2555/oj/eng` |

**Language codes:** `eng` (English), `fra` (French), etc. Use `eng` for programme documentation unless quoting an official translation requirement.

---

## 4. CELEX numbering (quick reference)

| Prefix | Meaning | Example |
|--------|---------|---------|
| `3` | EU legislation | `32024R1689` |
| `R` | Regulation | `32016R0679` (GDPR) |
| `L` | Directive | `32022L2555` (NIS2) |

CELEX appears in EUR-Lex URLs: `uri=CELEX:32024R1689`

---

## 5. Article-level deep links

For obligation traceability, link directly to articles in the HTML consolidated view:

```
https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{CELEX}#art_{n}
```

**EU AI Act anchors** (stored in `legislation_register.yaml` → LEG-006 `article_anchors`):

| Article | Obligation IDs | Anchor |
|---------|----------------|--------|
| Art. 5 | OBL-024 | `#art_5` |
| Art. 9 | OBL-022 | `#art_9` |
| Art. 13 | OBL-020 | `#art_13` |
| Art. 14 | OBL-023 | `#art_14` |
| Art. 15 | — (gap noted in AI-GOVERNANCE) | `#art_15` |
| Art. 50 | OBL-021 | `#art_50` |

---

## 6. UK legislation

UK primary legislation is cited via [legislation.gov.uk](https://www.legislation.gov.uk) URIs in `legislation_register.yaml` (`uk_legislation_uri`). UK law is **not** on the EUR-Lex ELI scheme in the same way as EU regulations.

| Register ID | UK source |
|-------------|-----------|
| LEG-001, LEG-002 | DPA 2018 |
| LEG-004 | Computer Misuse Act 1990 |
| LEG-005 | PECR 2003 |
| LEG-007 | CDPA 1988 |
| LEG-008 | Companies Act 2006 |

---

## 7. Citation rules for Magna Carta documents

1. **Policies and procedures** — cite act name + year/number once; link ELI or legislation.gov.uk on first reference.
2. **Obligations register** — `Source` column includes CELEX or ELI for EU rows.
3. **Change log** — when EU text changes, record CELEX, OJ date, and impacted OBL-IDs.
4. **Customer-facing text** — do not imply EUR-Lex links constitute legal advice; point to counsel for interpretation.

---

## 8. Verifying authentic text

1. Open the **ELI URI** (ends in `/oj/eng`) for the authentic Official Journal publication.
2. Cross-check **OJ reference** (volume, date, page) against the ELI landing page.
3. For day-to-day programme work, use **consolidated text** but note the consolidation date in review minutes.
4. For delegated acts, use EUR-Lex expert search filtered by base act CELEX (`32024R1689`).

---

## 9. Related documents

- [LEGISLATION-REGISTER.md](LEGISLATION-REGISTER.md) — human-readable index
- [EU-LEGISLATION-MONITORING.md](EU-LEGISLATION-MONITORING.md) — quarterly EU scan workflow
- [UK-AI-LEGISLATION-MONITORING.md](UK-AI-LEGISLATION-MONITORING.md) — UK policy parallel
- [OBLIGATIONS-REGISTER.md](OBLIGATIONS-REGISTER.md) — OBL-020–025 EUR-Lex sources
- [AI-GOVERNANCE.md](AI-GOVERNANCE.md) §3 — article mapping with anchors
- [PROC-CMP-001](../procedures/PROC-CMP-001-Compliance-Review.md) — quarterly review

**Next review:** 2026-09-06
