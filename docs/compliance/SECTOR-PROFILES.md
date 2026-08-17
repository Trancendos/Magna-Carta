# Sector Profiles — reading the sector lens

**Version:** 1.0.0
**Date:** 2026-08-17
**Owner:** ISMS Lead
**Register:** [`compliance/sector_profiles.yaml`](../../compliance/sector_profiles.yaml)
**Validated by:** `scripts/sector_profiles_check.py` + `scripts/trigger_alignment_check.py` (Layer B CI)

---

## What this adds, and what it does not

The estate already activated frameworks conditionally before this register existed.
`proactive_signals.yaml` defines 22 scope signals, `framework_triggers.yaml` maps each
signal to the `framework_ids` it activates and the enforcement posture it demands, and
`frameworks_register.yaml` holds all 127 frameworks. That machinery works and none of it
was replaced.

What was missing was the **lens**. Those signals are named after frameworks
(`SIG-HIPAA-001`, `SIG-DORA-001`, `SIG-CMMC-001`), not after the sectors that require
them. So the question an engagement actually opens with —

> "we are delivering into healthcare; what turns on?"

— could only be answered by someone who already knew that healthcare implies HIPAA plus
NHS DSPT plus GDPR. That mapping lived in a person's head. The register writes it down.

A sector profile is a **named bundle of existing signals**, plus the engagement context a
delivery team needs. It adds no detection mechanism: signals keep their own detection
(config file or environment variable), triggers keep owning enforcement, and the profile
only records which signals a sector implies.

It is **not**:

- a source of truth for which frameworks apply — that is `framework_triggers.yaml`,
  reached through the signals named here;
- legal advice — `data_types` and `notes` describe what is typically encountered, and a
  specific client may carry obligations no register predicts;
- exhaustive — a sector absent here has no profile *yet*; absence means "not mapped",
  never "nothing applies".

## The chain, end to end

```text
sector_profiles.yaml     "healthcare implies these signals"
        ↓
proactive_signals.yaml   HIPAA_PROFILE=enabled  →  SIG-HIPAA-001 active
        ↓
framework_triggers.yaml  TRG-HIPAA-001 → FW-062, enforcement_mode: enforce,
                         MC-RULE-009 required, SUP-005 DPA, ACT-002/ACT-006
        ↓
frameworks_register.yaml FW-062 = HIPAA Security Rule
```

Each signal is switched on either through `config/magna_carta_config.json`
(`profiles.<KEY>`) or through the matching environment variable. The variable name is the
practical answer to "how do I turn this on", so it is listed per sector below.

## The nine profiles

Every framework listed is what the trigger **actually activates today**, read from the
registers rather than from intent.

### Healthcare & Life Sciences — `healthcare`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-HIPAA-001` | `HIPAA_PROFILE` | FW-062 HIPAA Security Rule |
| `SIG-NHS-001` | `NHS_DSPT_SCOPE` | FW-089 NHS DSPT |
| `SIG-GDPR-001` | `GDPR_SCOPE` | FW-004 ISO/IEC 27701, FW-110 GDPR (EU/UK) |

Both the UK and US signals are listed because engagements frequently span both. Activate
only what the client's footprint genuinely requires — a UK-only trust does not need HIPAA.
Expect information governance review before system access; NHS work commonly requires DSPT
evidence and may require a DPIA before processing begins. Clinical safety cases
(DCB0129/DCB0160) apply where software influences care decisions, but that is a
clinical-safety discipline rather than a security one and is out of scope unless
explicitly contracted.

### Financial Services — `financial_services`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-DORA-001` | `DORA_SCOPE` | FW-100 DORA |
| `SIG-PCI-001` | `PCI_SCOPE` | FW-030 PCI DSS v4.0, FW-031 PCI 3-D Secure, FW-032 PCI P2PE, FW-033 PCI PIN |
| `SIG-PAYMENTS-001` | `PAYMENTS_LIVE` | FW-030 PCI DSS v4.0 |
| `SIG-GDPR-001` | `GDPR_SCOPE` | FW-004 ISO/IEC 27701, FW-110 GDPR (EU/UK) |

Change freezes around reporting periods are common. Evidence often has to satisfy an
external auditor rather than the client alone, so produce artefacts to audit standard from
the outset. DORA brings third-party risk obligations that put the supplier — us — in
scope, not merely the client. PCI-DSS applies only where cardholder data genuinely is in
scope; descoping via tokenisation is usually cheaper than compliance, and that is worth
saying before assuming a full assessment is needed.

### US Government & Federal — `government_us`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-FEDRAMP-001` | `FEDRAMP_SCOPE` | FW-050 FedRAMP, FW-051 GovRAMP, FW-052 FISMA |
| `SIG-US-GOV-001` | `US_GOV_SCOPE` | FW-060 FIPS 140-3, FW-066 US CLOUD Act, FW-069 VPAT / Section 508 |
| `SIG-CMMC-001` | `CMMC_SCOPE` | FW-042 NIST SP 800-171/172, FW-053 CMMC 2.0, FW-055/056/057 DoD IL2/IL4/IL5, FW-059 DFARS flow-down |

Authorisation timelines run in months, not weeks, and are the dominant scheduling
constraint. Personnel may need citizenship status or clearance. Data residency is
frequently mandated to US soil, which interacts directly with the Library bridge's
jurisdiction gate. FedRAMP authorisation is a programme, not an assessment — do not scope
it as a one-off engagement.

### Defence & National Security — `defence`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-CMMC-001` | `CMMC_SCOPE` | FW-042, FW-053, FW-055/056/057, FW-059 (as above) |
| `SIG-US-GOV-001` | `US_GOV_SCOPE` | FW-060, FW-066, FW-069 (as above) |

Export control (ITAR/EAR and UK equivalents) can restrict who may see technical data
regardless of clearance, including on our side. Establish nationality and location
constraints on the delivery team before assigning anyone; export control is a legal regime
distinct from security classification, and clearance is not sufficient.

**Gap:** US EAR (FW-067) and US ITAR (FW-068) sit in the framework register but no trigger
references either, so neither activates from any signal. ITAR carries a deliberate
not-applicable position; EAR does not, and a genuine export-controlled engagement needs a
signal for it.

### Retail & E-commerce — `retail_ecommerce`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-PCI-001` | `PCI_SCOPE` | FW-030/031/032/033 PCI family |
| `SIG-CCPA-001` | `CCPA_SCOPE` | FW-112 CCPA / CPRA |
| `SIG-GDPR-001` | `GDPR_SCOPE` | FW-004, FW-110 |
| `SIG-PAYMENTS-001` | `PAYMENTS_LIVE` | FW-030 PCI DSS v4.0 |

Peak trading periods are hard change freezes — scope delivery around them. Consumer-facing
changes may need marketing and legal sign-off on wording as well as technical review.

### Telecommunications — `telecommunications`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-PECR-001` | `PECR_SCOPE` | FW-134 UK PECR |
| `SIG-EU-INDUSTRY-001` | `EU_INDUSTRY_SCOPE` | FW-101, FW-102, FW-103, FW-104, FW-105, FW-106, FW-107, FW-108, FW-141 |
| `SIG-GDPR-001` | `GDPR_SCOPE` | FW-004, FW-110 |

Communications metadata carries obligations distinct from ordinary personal data, and
lawful intercept systems are usually out of scope entirely for commercial engagements —
confirm that boundary in writing.

**Gap:** `SIG-EU-INDUSTRY-001` is a category sweep over the register's `eu_industry`
category rather than a sector signal, so it activates a mixed set (FINMA, Japan FISC, UAE
IAR, GxP among others) with little bearing on telecommunications. PECR and GDPR carry the
real weight here.

### Manufacturing & Industrial — `manufacturing_industrial`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-EU-INDUSTRY-001` | `EU_INDUSTRY_SCOPE` | the `eu_industry` sweep (as above) |
| `SIG-GDPR-001` | `GDPR_SCOPE` | FW-004, FW-110 |

OT is not IT. Availability and safety outrank confidentiality, active scanning of
production control systems can be genuinely dangerous, and maintenance windows may be
quarterly.

**Gap:** IEC 62443 is the governing standard for industrial control security and has no
signal. Combined with the `eu_industry` sweep issue above, GDPR is the only substantive
activation this profile currently delivers.

### Energy & Utilities — `energy_utilities`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-EU-INDUSTRY-001` | `EU_INDUSTRY_SCOPE` | the `eu_industry` sweep (as above) |
| `SIG-GDPR-001` | `GDPR_SCOPE` | FW-004, FW-110 |

Designation as critical national infrastructure brings regulator notification duties and
can restrict where data may be processed and who may access it. Assume longer approval
cycles than commercial work.

**Gap:** NERC CIP and NIS2 sector-specific duties have no signals. This is the weakest
profile in the register — a starting point for scoping, not coverage.

### Education — `education`

| Signal | Switch | Activates |
|---|---|---|
| `SIG-GDPR-001` | `GDPR_SCOPE` | FW-004, FW-110 |
| `SIG-CCPA-001` | `CCPA_SCOPE` | FW-112 CCPA / CPRA |

Children's data attracts heightened protection (UK Age Appropriate Design Code, US
FERPA/COPPA) and safeguarding records are among the most sensitive categories the estate
would ever process. Academic calendars constrain delivery windows sharply.

**Gap:** FERPA exists as FW-063 but no trigger references it, so no signal can activate it.
COPPA is absent from the register entirely.

## The trigger-alignment defect this work uncovered

Writing the lens meant checking what each signal actually resolves to, which surfaced four
triggers activating frameworks unrelated to their own names:

| Trigger | Activated | Should have activated |
|---|---|---|
| `TRG-HIPAA-001` | FW-063 FERPA | FW-062 HIPAA Security Rule |
| `TRG-DORA-001` | FW-090 MPA, FW-091 ABS OSPAR | FW-100 DORA |
| `TRG-NHS-001` | FW-064 IRS Pub 1075, FW-065 SEC Rule 17a-4(f) | FW-089 NHS DSPT |
| `TRG-CMMC-001` | DoD IL2/IL4/IL5 only | plus FW-053 CMMC 2.0, FW-042 NIST 800-171/172, FW-059 DFARS |

The HIPAA case was the sharpest: enabling `HIPAA_PROFILE` applied HIPAA-specific
enforcement (`MC-RULE-009`, the SUP-005 DPA requirement, ACT-002/ACT-006) to FERPA while
leaving the HIPAA Security Rule inactive. It activated under `US_GOV_SCOPE` instead.

The cause was mechanical rather than editorial. `scripts/generate_framework_implementation.py`
assigned frameworks to signals first-match-wins in `SIGNAL_GROUPS` order, so category
sweeps appearing earlier in that list claimed framework IDs out from under signals that
named them explicitly, and the named signals silently inherited whatever the sweeps had
skipped — which, because the sweeps excluded `not_applicable` entries, was a bin of
leftovers.

Two fixes landed:

1. Explicit `framework_ids` are now assigned in a first pass, ahead of every category
   sweep. A signal that names a framework outright is stating intent; a sweep is only
   inferring one.
2. The four triggers' framework lists were corrected at source in the generator, and the
   registers regenerated. The generator is idempotent and the committed YAML was
   byte-identical to its output beforehand, so the regeneration diff contains only these
   changes.

`scripts/trigger_alignment_check.py` now fails Layer B CI if a trigger named after a
framework stops activating it. It was verified against the pre-fix registers and catches
all four.

## Known limits

- **`SIG-EU-INDUSTRY-001` is a category sweep, not a sector.** Three profiles
  (telecommunications, manufacturing, energy) lean on it and get imprecise activation as a
  result. Splitting it into real sector signals is the single highest-value improvement
  available to this register.
- **20 frameworks are referenced by no trigger at all**, so no signal can activate them.
  `trigger_alignment_check.py` reports them as a warning. Some are deliberate
  not-applicable positions; others (EAR, FERPA) are genuine gaps named above.
- **15 catalog entries name `TRG-CORE-001` as their activation path when that trigger does
  not list them.** Resolving this needs a governance decision, because
  `implementation_tier` has no value meaning "defined but not reachable" — so the check
  reports it rather than failing on it.
- **Sector coverage is not legal coverage.** Nine profiles is a start, and a client's
  actual obligations always outrank a register's prediction of them.
