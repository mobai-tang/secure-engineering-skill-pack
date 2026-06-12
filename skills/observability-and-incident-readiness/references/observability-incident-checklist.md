# Observability and Incident Readiness Checklist

## Critical Path Signals

- Log meaningful state transitions, failures, retries, and security-relevant actions.
- Include request, trace, job, user, tenant, dependency, and deployment identifiers where appropriate.
- Avoid secrets and unnecessary sensitive data.
- Define service, dependency, queue, job, and business-outcome metrics.
- Trace critical cross-service and asynchronous workflows.

## Detection

- Define symptoms and thresholds that indicate user or business impact.
- Alert on actionable conditions, not raw noise.
- Assign an owner, severity, response target, and escalation path.
- Test alert delivery and include useful diagnostic context.
- Ensure dashboards show health, impact, changes, and dependencies.

## Diagnosis

- Responders can connect a user report to request, trace, job, tenant, deployment, and dependency evidence.
- Errors identify failed operation and safe context without leaking sensitive data.
- Runbooks include queries, dashboards, common causes, containment, verification, and escalation.

## Containment and Recovery

- Verify feature flags, kill switches, rate limits, circuit breakers, degradation, and dependency isolation.
- Verify code, configuration, schema, and feature rollback.
- Verify backup restoration and recovery objectives.
- Define reconciliation and data repair procedures for partial or inconsistent processing.
- Ensure rollback does not restore the original vulnerability or data corruption.

## Exercise

Run a controlled scenario such as dependency failure, queue backlog, elevated error rate, bad deployment, expired credential, or partial processing.

Record detection time, alert quality, diagnosis path, containment time, recovery result, data repair, and lessons.

## Blockers

Block release for critical workflows when failures would be invisible, no responsible responder exists, containment or rollback is unavailable, data cannot be repaired, or the tested alert and runbook fail.
