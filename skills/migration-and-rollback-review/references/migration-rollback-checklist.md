# Migration and Rollback Review Checklist

## Compatibility

- Can old code run with the new schema or format?
- Can new code run before every instance, worker, consumer, and client is updated?
- Are reads and writes compatible during mixed-version operation?
- Is an expand-and-contract sequence required?
- Are API, event, queue, cache, and stored-data contracts versioned safely?

## Execution Safety

- Assess table locks, index creation, transaction duration, replication lag, storage growth, and resource pressure.
- Use batches, checkpoints, throttling, maintenance windows, and pause/resume controls where needed.
- Make operations idempotent and safe to retry.
- Prevent duplicate processing, lost updates, and inconsistent derived data.
- Test representative data volume and worst-case records.

## Rollback and Repair

- Decide whether rollback, roll-forward, or restoration is safest.
- Preserve required backups and verify restoration.
- Define how to repair partial, duplicated, corrupted, or inconsistent data.
- Ensure old and new versions can coexist for the required rollout window.
- Define abort thresholds, owners, commands, and verification steps.

## Observability

Track progress, throughput, failures, retries, lock time, replication lag, queue depth, resource use, and data reconciliation.

## Evidence

Record:

- affected systems and data;
- rollout sequence and compatibility matrix;
- tested commands and environment;
- representative volume and duration;
- backup and restore evidence;
- pause, resume, abort, repair, rollback, and roll-forward results;
- owners and communication plan;
- remaining risk.

## Blockers

Block release when mixed versions are incompatible, migration may cause uncontrolled locks or resource exhaustion, operations are not safely retryable, progress is invisible, partial failure cannot be repaired, or no verified recovery path exists.
