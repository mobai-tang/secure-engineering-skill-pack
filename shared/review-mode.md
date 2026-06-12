# PR Review Mode

Use this output mode when reviewing a pull request, patch, commit, or proposed change.

Prioritize correctness, behavioral regressions, security, data integrity, release risk, maintainability, and missing tests.

Do not nitpick style unless it affects correctness, maintainability, security, accessibility, performance, or repository consistency.

## Output Structure

```markdown
## Blocking Issues

## High-Risk Issues

## Maintainability Issues

## Missing Tests

## Security Concerns

## Release Concerns

## Questions

## Suggested Patch
```

For every finding, include severity, affected file or responsibility, evidence, impact, and a concrete correction. If no findings exist, say so clearly and identify remaining test gaps or residual risk.
