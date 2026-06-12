# Quickstart: Before and After

This example shows how the skill pack changes an agent's behavior on the same task.

## Task

> Add a CSV user export endpoint and prepare it for production.

## Without the Skill Pack

> I added `/export-users`, queried all users, returned a CSV, and the feature should be ready to deploy.

### Problems

- No repository evidence or module ownership.
- No authorization or tenant-boundary validation.
- No privacy review of exported fields.
- No large-export, memory, timeout, or abuse analysis.
- No tests, observability, rollback, or release evidence.
- Claims readiness without validation.

## With the Skill Pack

### Skills Selected

- `threat-modeling-lite`
- `modular-evidence-implementation`
- `data-privacy-review`
- `release-readiness-evidence`

### Evidence Checked

- Located the existing export module, role policy, tenant filter, audit-event pattern, and test conventions.
- Confirmed which user fields are approved for export and the retention policy for generated files.

### Design and Controls

- Keep export orchestration in the existing export module.
- Enforce server-side administrator permission and tenant scope.
- Use an approved field allowlist and exclude secrets and unnecessary sensitive data.
- Generate exports asynchronously with size limits, expiration, audit events, and download authorization.
- Add progress, failure, and completion signals.

### Tests and Validation

- Positive administrator export.
- Negative ordinary-user and cross-tenant attempts.
- Field allowlist and CSV-safe output.
- Large export, retry, expiration, and failed-job behavior.
- Release checks recorded as `Pass`, `Fail`, `Blocked`, or `Not Applicable`.

### Release Decision

`No-Go` until cross-tenant negative tests, generated-file expiration, and production alert validation pass.

## Expected Result

The skill pack does not merely produce more text. It changes the decision quality by requiring evidence, selecting focused reviews, identifying missing controls, and refusing unsupported readiness claims.
