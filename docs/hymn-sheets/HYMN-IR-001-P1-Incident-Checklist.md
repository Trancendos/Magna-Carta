# HYMN-IR-001 — P1 Incident Checklist

**Version:** 1.0.0 · **Procedure:** PROC-IR-001 · **Cookbook:** COOK-IR-001

---

## Declare (0–15 min)

- [ ] Incident ID opened
- [ ] Incident commander assigned (Security Ops)
- [ ] ISMS Lead notified
- [ ] P1 severity confirmed
- [ ] War room / bridge active
- [ ] Log preservation enabled — do not delete

## Contain (15–60 min)

- [ ] Affected systems identified (SYSTEMS-REGISTER)
- [ ] Containment action taken (isolate / rotate / block)
- [ ] DPO notified if personal data involved
- [ ] Legal notified if regulator/customer impact likely
- [ ] Executive notified if P0 outage > 1 hour

## Breach assessment (parallel)

- [ ] UK GDPR reportable? → ICO 72h clock started if yes
- [ ] HIPAA in scope? → BAA breach clause checked
- [ ] Customer notification required? → Legal decision

## Recover

- [ ] Root cause identified
- [ ] Emergency change approved (PROC-CHG-001)
- [ ] Services restored in order: vault → auth → ws → apps
- [ ] Monitoring green 30 min

## Close (within 5 days)

- [ ] Post-incident review scheduled
- [ ] CAPA raised if needed (PROC-CAPA-001)
- [ ] RISK-REGISTER updated
- [ ] Incident record closed with timeline

**Incident commander:** _________________ **Date/time declared:** _________________
