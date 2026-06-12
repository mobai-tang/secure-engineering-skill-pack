# Threat Modeling Lite Playbook

## Scope

Use before implementation for security-sensitive or externally reachable behavior. Keep the review proportionate to the feature risk.

## Discovery

Document:

- business purpose and critical user outcomes;
- anonymous, authenticated, privileged, service, and third-party actors;
- sensitive data, money, privileges, availability, reputation, and compliance assets;
- UI, API, webhook, upload, import, export, job, queue, callback, and administrative entry points;
- browser, mobile, service, tenant, network, storage, third-party, and administrative trust boundaries;
- expected normal flow and failure flow.

## Abuse Questions

Ask:

- Can an actor access another user, tenant, role, object, or workflow?
- Can trusted fields, prices, states, permissions, destinations, or identifiers be manipulated?
- Can requests be replayed, reordered, duplicated, automated, or raced?
- Can uploaded or supplied content reach an interpreter, parser, browser, file path, query, or downstream service?
- Can sensitive data enter logs, clients, exports, analytics, third parties, caches, or backups?
- Can a low-impact weakness combine with another weakness?
- What happens when a dependency, verification provider, queue, or datastore fails?
- Which action would be difficult to detect, contain, reverse, or investigate?

## Control Mapping

For each meaningful abuse case, record:

| Field | Required detail |
|---|---|
| Asset and attacker goal | What the attacker gains |
| Preconditions | Access, role, knowledge, timing, or capability required |
| Attack path | Entry point, failed assumption, and trust boundary crossed |
| Prevent | Server-side authorization, validation, isolation, approval, limit, or safer design |
| Detect | Audit event, metric, alert, anomaly, or investigation signal |
| Contain | Revocation, quota, kill switch, tenant isolation, or circuit breaker |
| Recover | Rollback, repair, notification, backup, or reconciliation |
| Required test | Safe positive, negative, boundary, or abuse-case validation |
| Residual risk | Remaining impact, owner, deadline, and acceptance |

## Prioritization

Prioritize paths that:

- require little attacker capability;
- cross privilege or tenant boundaries;
- affect sensitive data, money, many users, or core availability;
- are difficult to detect or reverse;
- exploit default or common configurations;
- combine with other weaknesses.

## Completion Gate

Do not begin implementation when a high-impact trust boundary has no owner, required control, required test, or accepted residual risk.
