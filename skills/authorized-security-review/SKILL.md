---
name: authorized-security-review
description: Use for defensive, authorized security review of authentication, recovery, registration, authorization, administrator actions, tenant boundaries, abuse controls, sensitive data, or scoped penetration-test planning and evidence review.
---

# Authorized Security Review

## Safety Boundary

Perform only defensive review or active testing with explicit authorization, defined scope, approved environment, safety limits, and a responsible owner. Public accessibility is not permission.

Read the authorization, OWASP verification, defensive attacker mindset, finding lifecycle, and unauthorized-request sections in [references/release-and-security-playbook.md](references/release-and-security-playbook.md).

## Before Active Testing

Record written authorization, responsible owner, exact in-scope and excluded assets, approved identities, environment, dates, techniques, rate limits, monitoring contacts, evidence rules, and rollback procedures.

Stop immediately if testing crosses scope, affects availability, exposes unrelated data, risks destructive impact, or loses monitoring coverage.

## Required Review

1. Map assets, entry points, trust boundaries, roles, tenants, and likely abuse cases.
2. Review authentication, recovery, sessions, tokens, API keys, and credential handling.
3. Review ordinary-user, administrator, service-account, and tenant boundaries.
4. Review server-side authorization, input handling, business logic, and sensitive data.
5. Review registration automation, rate limits, progressive friction, and abuse response.
6. Review logging, alerts, containment, revocation, recovery, and incident response.
7. Validate suspected findings with the minimum safe action needed to prove impact.
8. Retest fixes and record residual risk.

## Defensive Attacker Mindset

For each important feature, ask which asset is valuable, which entry point is reachable, which assumption may fail, which trust boundary could be crossed, how weaknesses could chain, and which controls prevent, detect, contain, and recover.

## Output

Report authorization scope, issue, affected asset, evidence, impact, safe reproduction conditions, remediation, owner, retest result, release impact, and residual risk.
