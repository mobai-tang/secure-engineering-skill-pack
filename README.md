# Secure Engineering Skill Pack

[简体中文](README.zh-CN.md)

A focused AI skill pack for evidence-driven implementation, secure design, dependency and privacy review, operational readiness, safe migrations, release decisions, and authorized defensive security review.

## Included Skills

### `modular-evidence-implementation`

Use for feature implementation, bug fixes, refactoring, architecture boundaries, repository evidence, focused tests, and oversized mixed-responsibility files.

### `release-readiness-evidence`

Use before staging or production release, deployment approval, migration or feature-flag rollout, capability-boundary validation, rollback, recovery, and `Go` or `No-Go` decisions.

### `authorized-security-review`

Use for defensive, authorized review of authentication, recovery, authorization, administrator actions, tenant isolation, abuse controls, sensitive data, and scoped security testing.

### `threat-modeling-lite`

Use before implementing security-sensitive features to identify assets, entry points, trust boundaries, abuse cases, controls, tests, and residual risk.

### `supply-chain-and-dependency-review`

Use when adding or upgrading packages, SDKs, CI actions, build scripts, Docker images, registries, signing, and release-pipeline components.

### `data-privacy-review`

Use when collecting, storing, logging, exporting, deleting, analyzing, uploading, or sharing user and sensitive data.

### `observability-and-incident-readiness`

Use when production workflows need logs, metrics, traces, alerts, dashboards, runbooks, containment, rollback, recovery, and data repair.

### `migration-and-rollback-review`

Use for database, schema, data-format, queue, cache, configuration, storage, protocol, and mixed-version rollout changes.

## Why Focused Skills?

Each skill has a narrow trigger and loads detailed `references/` only when needed. This reduces over-triggering, keeps agent context focused, and allows each skill to be installed or used independently.

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
├── authorized-security-review/
├── threat-modeling-lite/
├── supply-chain-and-dependency-review/
├── data-privacy-review/
├── observability-and-incident-readiness/
└── migration-and-rollback-review/
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
│   ├── release-readiness-evidence/
│   ├── authorized-security-review/
│   ├── threat-modeling-lite/
│   ├── supply-chain-and-dependency-review/
│   ├── data-privacy-review/
│   ├── observability-and-incident-readiness/
│   └── migration-and-rollback-review/
├── shared/
│   ├── review-mode.md
│   └── output-contract.md
├── examples/
├── CHANGELOG.md
├── LICENSE
└── README.md
```

Every skill directory contains a short `SKILL.md`, optional `agents/openai.yaml`, and detailed guidance in `references/`.

## Shared Resources

- [`shared/review-mode.md`](shared/review-mode.md): High-signal PR review output focused on blocking issues, risk, maintainability, tests, security, and release concerns.
- [`shared/output-contract.md`](shared/output-contract.md): Standard evidence-based completion report.
- [`examples/`](examples/): Good and bad examples covering unsupported claims, false validation, over-splitting, release blockers, and unauthorized testing.

## Core Principles

- Verify repository evidence before implementation claims.
- Keep business ownership and dependency boundaries explicit.
- Keep handwritten source files at or below 800 physical lines.
- Stop repeated bug trial-and-error and research authoritative sources.
- Treat skipped, unknown, and untested release checks as not passing.
- Never treat client-side visibility as authorization.
- Perform active security testing only with explicit authorization and scope.
- Treat data minimization, dependency provenance, observability, and migration recovery as engineering requirements.
- Never claim code is fixed, secure, tested, or ready without evidence.

## Examples

- “Implement this feature with clear module ownership and focused tests.” Use `modular-evidence-implementation`.
- “Decide whether this build is ready for production.” Use `release-readiness-evidence`.
- “Review authentication and registration abuse risks in this authorized environment.” Use `authorized-security-review`.
- “Identify threats before implementing this billing webhook.” Use `threat-modeling-lite`.
- “Review this dependency and GitHub Actions upgrade.” Use `supply-chain-and-dependency-review`.
- “Review how this AI feature handles user data.” Use `data-privacy-review`.
- “Verify this service can be detected and recovered during an incident.” Use `observability-and-incident-readiness`.
- “Review this database migration and rollback plan.” Use `migration-and-rollback-review`.

## License

MIT
