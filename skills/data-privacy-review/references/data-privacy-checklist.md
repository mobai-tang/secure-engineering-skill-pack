# Data Privacy Review Checklist

## Data Inventory

For every field or data class, record:

| Field | Required detail |
|---|---|
| Data | Exact field or category |
| Source | User, device, employee, partner, inferred, generated, or imported |
| Purpose | Why it is required |
| Classification | Public, internal, personal, sensitive, regulated, secret, or other policy class |
| Owner | Responsible business and engineering owner |
| Storage | Databases, files, caches, logs, backups, clients, and analytics |
| Sharing | Internal teams, vendors, AI providers, processors, or public recipients |
| Retention | Duration and deletion trigger |
| User control | Access, correction, export, consent, objection, and deletion |

## Review Questions

- Is every collected field necessary for the stated purpose?
- Can collection, precision, frequency, or retention be reduced?
- Does sensitive data enter logs, traces, analytics, crash reports, prompts, or support tools?
- Do third parties receive only necessary data under an approved purpose?
- Are AI inputs and outputs reviewed for sensitive or retained data?
- Can users access, correct, export, and delete applicable data?
- Does deletion cover derived records, caches, search indexes, backups, and third parties as policy requires?
- Are retention and legal-hold rules explicit and enforceable?
- Is production data excluded from development and testing unless explicitly approved and protected?
- Are masking, tokenization, encryption, and access logging appropriate?

## Data Flow Review

Map:

```text
Source -> Collection -> Validation -> Processing -> Storage -> Sharing -> Export -> Retention -> Deletion
```

At each transition, identify purpose, authorization, minimization, protection, evidence, and failure behavior.

## Blockers

Block release when sensitive collection lacks a justified purpose, data flows or third parties are unknown, deletion or retention cannot be honored, secrets or sensitive fields leak into logs or clients, or required user controls and approvals are missing.
