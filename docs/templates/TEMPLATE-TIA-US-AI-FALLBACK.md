# Template — Transfer Impact Assessment (US AI Fallback)

**Version:** 1.0.0 (outline)  
**Date:** 2026-06-07  
**Owner:** DPO  
**Use:** SUP-004 (US-hosted AI inference fallback), ACT-010

---

## 1. When required

Complete this TIA **before** enabling transfer of personal data to a US AI sub-processor where UK/EU adequacy does not apply, per UK GDPR / EU GDPR Chapter V and [GDPR-ALIGNMENT.md](../compliance/GDPR-ALIGNMENT.md).

**Current posture:** SUP-004 DPA unsigned — fallback **disabled** until TIA approved and DPA executed 🎯.

---

## 2. Assessment record

| Field | Value |
|-------|-------|
| TIA ID | TIA-YYYY-### |
| Exporter | Trancendos Ltd |
| Importer | [US AI provider legal name] |
| Transfer mechanism | UK IDTA / EU SCCs + UK Addendum (see [TEMPLATE-SCC-ANNEX.md](TEMPLATE-SCC-ANNEX.md)) |
| Data categories | Prompts, inference metadata, account IDs (minimise PHI) |
| Special categories | Flag if health data possible — requires separate DPIA |
| Assessment date | |
| Assessor | DPO |
| Approver | DPO + ISMS Lead |

---

## 3. TIA checklist (ICO / EDPB style)

### 3.1 Know the transfer

- [ ] Importer country and legal framework documented
- [ ] Importer subprocessors listed
- [ ] Data flow diagram attached (ROPA reference)

### 3.2 Assess laws and practices

- [ ] US surveillance laws considered (FISA 702, EO 12333)
- [ ] Importer contractual commitments reviewed
- [ ] Government access transparency reports reviewed (if published)

### 3.3 Supplementary measures

| Measure | Applied? | Evidence |
|---------|----------|----------|
| Encryption in transit (TLS 1.2+) | | |
| Encryption at rest | | |
| Pseudonymisation / tokenisation | | |
| Access controls and logging | | |
| Contractual audit rights | | |
| Technical blocking of certain data classes (PHI) | MC-RULE-009 | |

### 3.4 Conclusion

- [ ] Transfer may proceed with measures in place
- [ ] Transfer prohibited — disable route (document in ACT-010)
- [ ] Re-assess on: law change, new data categories, incident, annual review

---

## 4. Linkage

| Artefact | Action |
|----------|--------|
| ROPA | Update transfer row |
| SUP-004 | DPA + SCC annex signed |
| [SUPPLIER-DPA-REGISTER.md](../compliance/SUPPLIER-DPA-REGISTER.md) | Status → Signed |
| ACT-010 | Close when DPA signed or route disabled |

---

## 5. Related documents

- [TEMPLATE-SCC-ANNEX.md](TEMPLATE-SCC-ANNEX.md)
- [TEMPLATE-DPA-UK-GDPR.md](TEMPLATE-DPA-UK-GDPR.md)
- [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) §1, §3
