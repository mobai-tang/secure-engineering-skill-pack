# Evidence-Based Output Contract

Use this contract when a structured completion report is useful. Include only applicable sections, but never omit failed, blocked, unknown, or unexecuted validation.

```markdown
## Evidence Checked

## Assumptions

## Files Changed

## Module Boundaries

## Tests Run

## Validation Not Run

## Security Impact

## Privacy Impact

## Release Impact

## Remaining Risk
```

## Rules

- Distinguish observed facts from assumptions.
- Report exact tests and validation actually run.
- Never imply skipped or unavailable validation passed.
- Link risks to owners, deadlines, evidence, and required next actions when known.
- State when a section is not applicable and why.
