---
name: threat-modeling-lite
description: Use before implementing security-sensitive features, new APIs, authentication flows, administrator actions, billing, file uploads, webhooks, data exports, or tenant-facing capabilities to identify assets, trust boundaries, threats, mitigations, and required evidence.
---

# Threat Modeling Lite

## Goal

Identify meaningful abuse paths and required controls before implementation begins.

Read [references/threat-modeling-playbook.md](references/threat-modeling-playbook.md) for the detailed prompts and prioritization method.

## Workflow

1. Define the feature, actors, assets, entry points, data flows, and trust boundaries.
2. Identify attacker goals, misuse cases, failed assumptions, and chained attack paths.
3. Map preventive, detective, containment, and recovery controls.
4. Define required security tests and release evidence.
5. Assign owners and record accepted residual risk.

## Output

Report:

```text
Assets:
Entry points:
Trust boundaries:
Abuse cases:
Required controls:
Required tests:
Residual risk:
```
