# Modular Maintainable Development

A Codex skill for building modular, maintainable software with clear responsibilities, evidence-based decisions, focused testing, and disciplined bug investigation.

## When to Use

Use this skill when:

- implementing features;
- fixing bugs;
- refactoring existing code;
- reviewing software architecture;
- splitting oversized or mixed-responsibility files;
- verifying assumptions against repository evidence.

## Core Rules

- Keep one primary responsibility and one primary reason to change per file.
- Organize code around clear business and module boundaries.
- Keep handwritten source files at or below 800 physical lines.
- Verify assumptions using repository evidence before implementation.
- Preserve existing user changes and avoid unrelated restructuring.
- Run focused tests and relevant validation commands.

## Unresolved Bugs

Do not spend excessive time repeatedly trying the same approaches.

After a small number of evidence-driven attempts:

1. Stop local trial-and-error.
2. Search official documentation, source repositories, upstream issues, and other authoritative sources.
3. Verify that suggested solutions apply to the project's actual versions.
4. Test credible findings when safe and within scope.
5. Clearly report the blocker, evidence, attempted solutions, and required next action if the bug remains unresolved.

## Installation

Place the `modular-maintainable-development` directory in your Codex skills directory:

```text
~/.codex/skills/modular-maintainable-development
```

Codex can then invoke the skill when working on relevant development, debugging, refactoring, and architecture tasks.

## Main Skill File

See [`SKILL.md`](SKILL.md) for the complete workflow and rules.
