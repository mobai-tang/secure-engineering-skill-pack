---
name: release-readiness-evidence
description: Use before staging or production release, deployment approval, Go or No-Go decisions, migration or feature-flag rollout, or validation of permissions, observability, rollback, recovery, and operational evidence.
---

# Release Readiness Evidence

## Goal

Make release decisions using explicit, reproducible evidence. Skipped, unknown, or untested checks are not passes.

Read the release acceptance, capability boundary, credential protection, registration-abuse, finding, and release decision sections in [references/release-and-security-playbook.md](references/release-and-security-playbook.md).

## Required Workflow

1. Record the release version, commit, environment, configuration, owners, and scope.
2. Map every applicable requirement and risk to a verification method.
3. Record each check as `Pass`, `Fail`, `Blocked`, or `Not Applicable` with evidence.
4. Validate critical journeys, roles, tenant isolation, negative paths, compatibility, and recovery.
5. Validate tests, performance, concurrency, deployment, configuration, migration, rollback, observability, backups, and incident response.
6. Inventory user-callable, user-prohibited, and administrator-only capabilities.
7. Verify password, credential, account recovery, and registration-abuse controls where applicable.
8. Link failures to owners, remediation, retest results, exceptions, and residual risk.
9. Return a supported `Go`, `Conditional Go`, or `No-Go` recommendation.

## Release Blockers

Return `No-Go` when critical journeys, authorization boundaries, migrations, rollback, recovery, monitoring, or required evidence remain unsafe or incomplete.

Never downgrade findings or treat skipped checks as passing to meet a release date.

## Completion Report

Report the acceptance matrix, evidence locations, failures, blocked and not-applicable checks, capability-boundary results, operational readiness, exceptions, owners, deadlines, residual risks, and final release recommendation.
