---
name: modular-evidence-implementation
description: Use when implementing features, fixing bugs, refactoring code, or reviewing architecture that requires repository evidence, clear business-module ownership, dependency-boundary checks, focused tests, or prevention of oversized mixed-responsibility files.
---

# Modular Evidence Implementation

## Goal

Implement changes through verified repository evidence, clear ownership, intentional public contracts, and focused responsibilities.

Read [references/modularity-rules.md](references/modularity-rules.md) before changing project structure or implementing a non-trivial feature.

## Required Workflow

1. Inspect nearby code, contracts, schemas, configuration, tests, and established conventions.
2. Separate verified facts from assumptions and resolve checkable assumptions.
3. Identify the owning business module and assign every introduced responsibility.
4. Split mixed-responsibility or oversized files before adding behavior.
5. Implement through existing patterns and intentional public contracts.
6. Add focused tests beside the responsibility they verify.
7. Run relevant validation commands and reproduce the original symptom for bug fixes.
8. Review the diff for boundary leaks, unsupported assumptions, and unrelated coupling.

## Non-Negotiable Rules

- Keep one primary responsibility and one primary reason to change per file.
- Keep every handwritten source file at or below 800 physical lines.
- Never invent files, APIs, fields, dependencies, commands, behavior, requirements, or test results.
- Preserve user changes and avoid unrelated restructuring.
- Do not confuse fewer files with simplicity or more files with modularity.
- Never claim code is fixed or tested without evidence.

## Unresolved Bugs

After a small number of evidence-driven attempts, stop repeated trial-and-error. Research exact errors using official documentation, upstream repositories, release notes, and authoritative sources.

If the bug remains unresolved, tell the user promptly and report the evidence, attempted approaches, research sources, likely cause, blocker, and smallest required next action.

## Completion Report

Report verified facts, unresolved assumptions, chosen module boundaries, files created or split, public contracts, relevant line counts, tests actually run, and remaining structural debt.
