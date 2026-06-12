# Bad Go Decision

> Go. Unit tests passed, so the release should be safe.

## Why This Is Bad

- No evidence for migrations, rollback, permissions, monitoring, or recovery.
- Treats unknown checks as passing.
- Does not identify owners, exceptions, or residual risk.
