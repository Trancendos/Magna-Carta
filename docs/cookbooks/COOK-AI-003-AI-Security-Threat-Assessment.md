# COOK-AI-003 — AI Security Threat Assessment Playbook

**Version:** 1.0.0  
**Owner:** AI Lead / Security Ops  
**Procedure:** [PROC-AI-003](../procedures/PROC-AI-003-AI-Security-Threat-Assessment.md)  
**Hymn sheet:** [HYMN-AI-003](../hymn-sheets/HYMN-AI-003-AI-Security-Threat-Assessment-Checklist.md)

---

## When to use

Before production release of an AI-affecting change, annual model security review, or ACT-013 milestone.

---

## Prepare

1. Pull current **model card** and risk tier from registry
2. Read [AI-SECURITY-THREAT-MODEL.md](../compliance/AI-SECURITY-THREAT-MODEL.md) for TM-AI catalogue
3. Identify whether **agentic** routes apply (tools, memory, multi-agent)
4. Gather architecture diagram: data flows, RAG sources, external APIs, tool registry

---

## Assess (per surface)

### Development-time

- Trace training/fine-tune data from source to artefact
- Verify vendor model integrity and SUP-004 DPA status
- Confirm experiment store access matches least privilege

### Inference

- List all user-controlled input paths (chat, uploads, email, web fetch)
- Test prompt injection scenarios in staging (document, do not automate against prod)
- Verify rate limits and cost caps under abuse simulation
- Confirm zero-model-trust controls limit blast radius if injection succeeds

### Runtime conventional

- Review what is logged (prompts, outputs, tool args) and retention
- Confirm encryption at rest for AI-related stores
- Validate AuthN/Z on all AI API routes

### Agentic (if applicable)

- Map tools to sensitivity tiers
- Check lethal trifecta: can untrusted content reach sensitive tools + exfil channel?
- Confirm human approval for high-impact tool calls

---

## Decide

| Outcome | Action |
|---------|--------|
| Pass | Update model card security annex; file evidence for ACT-013 |
| Conditional | Ship with documented compensating controls + monitoring |
| Fail | Block release; CAPA; escalate RISK-009–012 if residual high |

Update [COMPLIANCE-COVERAGE-REGISTER.md](../compliance/COMPLIANCE-COVERAGE-REGISTER.md) AI security row and feed gaps to PT-AI when offensive validation needed.

---

## Record

1. Complete HYMN-AI-003 checklist
2. Summarise TM-AI threats: mitigated / gap / accepted
3. Link evidence in model card annex or `docs/evidence/`
4. Present summary at next AI Governance Committee if material gaps
