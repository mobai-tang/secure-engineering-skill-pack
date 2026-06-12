# Modular Maintainable Development

An AI coding-agent instruction set for building modular, maintainable software with clear responsibilities, evidence-based decisions, focused testing, and disciplined bug investigation.

It can be used with Codex, Claude Code, Cursor, Trae, Windsurf, GitHub Copilot, and other tools that support skills, project rules, or custom instructions.

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
- Complete release acceptance and authorized security testing before production release.
- Review the system from a defensive attacker perspective to identify attack paths and missing controls.
- Verify user and administrator capability boundaries, password and credential protection, and layered defenses against automated registration abuse.

## Unresolved Bugs

Do not spend excessive time repeatedly trying the same approaches.

After a small number of evidence-driven attempts:

1. Stop local trial-and-error.
2. Search official documentation, source repositories, upstream issues, and other authoritative sources.
3. Verify that suggested solutions apply to the project's actual versions.
4. Test credible findings when safe and within scope.
5. Clearly report the blocker, evidence, attempted solutions, and required next action if the bug remains unresolved.

## Supported Tools

### Codex

Place the complete directory in your Codex skills directory:

```text
~/.codex/skills/modular-maintainable-development
```

Codex can then invoke the skill when working on relevant development, debugging, refactoring, and architecture tasks.

### Claude Code

Copy the complete directory into your Claude Code skills directory:

```text
~/.claude/skills/modular-maintainable-development
```

You can also place the important rules from `SKILL.md` in a project's `CLAUDE.md` when the rules should apply only to that repository.

### Cursor

Add the contents of `SKILL.md` to a Cursor project rule. Depending on the Cursor version, create a rule through Cursor settings or place it in the project's rules directory.

Configure the rule to apply to implementation, bug fixing, refactoring, and architecture review tasks.

### Trae

Add the contents of `SKILL.md` to Trae's project rules, custom instructions, or agent rules. Enable the rule for development, debugging, refactoring, and architecture tasks.

### Windsurf

Add the contents of `SKILL.md` to the project's Windsurf rules or workspace instructions.

### GitHub Copilot

Add the relevant rules from `SKILL.md` to the repository's Copilot custom instruction file or configure them through the supported repository instruction settings.

### Other AI Coding Tools

For any tool that supports project rules, system prompts, agent instructions, or reusable skills:

1. Add the contents of `SKILL.md` as a project or global instruction.
2. Keep `references/modularity-rules.md` available to the agent when possible.
3. Configure the instruction to apply during feature implementation, bug fixing, refactoring, and architecture review.

Native skill discovery and exact rule-file locations vary by tool and version. When native skills are unavailable, use `SKILL.md` as a project rule or custom instruction.

## Main Skill File

See [`SKILL.md`](SKILL.md) for the complete workflow and rules.

See [`references/release-acceptance-and-authorized-security-testing.md`](references/release-acceptance-and-authorized-security-testing.md) for release gates and authorized attack-simulation rules.
