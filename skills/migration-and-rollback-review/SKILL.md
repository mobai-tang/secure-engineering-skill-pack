---
name: migration-and-rollback-review
description: Use when changing database schemas, indexes, data formats, queues, caches, configuration, storage, protocols, or deployment order where compatibility, rollout safety, data repair, or rollback matters.
---

# Migration and Rollback Review

## Goal

Ensure changes can be rolled out safely across mixed versions, retried without corruption, observed, paused, repaired, and reversed when required.

Read [references/migration-rollback-checklist.md](references/migration-rollback-checklist.md) for the detailed review.

## Workflow

1. Identify affected data, schemas, services, versions, dependencies, and rollout order.
2. Verify backward and forward compatibility using expand-and-contract where appropriate.
3. Assess locks, large-table work, traffic, queue, cache, and resource risks.
4. Design idempotent batches, checkpoints, throttling, observability, pause, resume, and repair.
5. Verify backup, rollback, roll-forward, and mixed-version behavior.
6. Rehearse the migration and recovery path with representative data.

## Output

Report compatibility, rollout order, resource risks, migration procedure, evidence, pause and repair controls, rollback or roll-forward plan, blockers, and recommendation.
