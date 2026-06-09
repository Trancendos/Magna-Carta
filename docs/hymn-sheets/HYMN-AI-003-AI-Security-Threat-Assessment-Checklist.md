# HYMN-AI-003 — AI Security Threat Assessment Checklist

**Version:** 1.0.0 · **Procedure:** PROC-AI-003 · **Cookbook:** COOK-AI-003

**Model:** _________________ **Version:** _________________ **Date:** _________________

## Development-time

- [ ] Training/fine-tune data provenance documented
- [ ] Dataset access controls reviewed
- [ ] Third-party model supply chain verified (SUP register)
- [ ] CI/CD secrets and artefact integrity confirmed

## Input / inference

- [ ] Direct prompt injection controls assessed
- [ ] Indirect injection paths identified (RAG, email, web)
- [ ] Zero-model-trust blast-radius review completed
- [ ] Rate limits and cost caps verified
- [ ] Extraction / probing mitigations documented
- [ ] High-risk output human review in place

## Runtime conventional

- [ ] Prompt/log storage encryption and retention reviewed
- [ ] API AuthN/Z verified on AI routes

## Agentic (if applicable)

- [ ] Tool allowlist / least model privilege documented
- [ ] Lethal trifecta analysis — at least one leg broken
- [ ] Human-in-the-loop for irreversible actions

## Close-out

- [ ] TM-AI threats recorded (mitigated / gap / accepted)
- [ ] Model card security annex updated
- [ ] PT-AI scope updated if offensive gaps remain
- [ ] CAPA raised for critical gaps

**AI Lead:** _________________ **Security Ops:** _________________
