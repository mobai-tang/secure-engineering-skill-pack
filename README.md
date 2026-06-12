# Secure Engineering Skill Pack

[简体中文](README.zh-CN.md)

A focused AI skill pack for evidence-driven modular implementation, release-readiness decisions, and authorized defensive security review.

## Included Skills

### `modular-evidence-implementation`

Use for feature implementation, bug fixes, refactoring, architecture boundaries, repository evidence, focused tests, and oversized mixed-responsibility files.

### `release-readiness-evidence`

Use before staging or production release, deployment approval, migration or feature-flag rollout, capability-boundary validation, rollback, recovery, and `Go` or `No-Go` decisions.

### `authorized-security-review`

Use for defensive, authorized review of authentication, recovery, authorization, administrator actions, tenant isolation, abuse controls, sensitive data, and scoped security testing.

## Why Three Skills?

Each skill has a narrow trigger and loads only the guidance needed for the current task. This reduces over-triggering, keeps agent context focused, and allows the skills to be installed or used independently.

## Installation

Copy each desired directory from [`skills/`](skills/) into the target tool's skill directory.

### Codex

User-level:

```text
$HOME/.agents/skills/
```

Repository-level:

```text
<repo>/.agents/skills/
```

Example:

```text
.agents/skills/
├── modular-evidence-implementation/
├── release-readiness-evidence/
└── authorized-security-review/
```

### Claude Code

Personal:

```text
~/.claude/skills/
```

Project:

```text
.claude/skills/
```

### Cursor, Trae, Windsurf, and GitHub Copilot

Add the relevant `SKILL.md` as a project rule, workspace instruction, agent rule, or custom instruction. Keep its `references/` directory available when the tool supports referenced files.

## Repository Structure

```text
secure-engineering-skill-pack/
├── skills/
│   ├── modular-evidence-implementation/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/modularity-rules.md
│   ├── release-readiness-evidence/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/release-and-security-playbook.md
│   └── authorized-security-review/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/release-and-security-playbook.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Core Principles

- Verify repository evidence before implementation claims.
- Keep business ownership and dependency boundaries explicit.
- Keep handwritten source files at or below 800 physical lines.
- Stop repeated bug trial-and-error and research authoritative sources.
- Treat skipped, unknown, and untested release checks as not passing.
- Never treat client-side visibility as authorization.
- Perform active security testing only with explicit authorization and scope.
- Never claim code is fixed, secure, tested, or ready without evidence.

## Examples

- “Implement this feature with clear module ownership and focused tests.” Use `modular-evidence-implementation`.
- “Decide whether this build is ready for production.” Use `release-readiness-evidence`.
- “Review authentication and registration abuse risks in this authorized environment.” Use `authorized-security-review`.

## License

MIT
