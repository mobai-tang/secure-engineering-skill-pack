# Secure Modular Release Engineering

An evidence-driven instruction set for AI coding agents that combines maintainable software architecture, disciplined implementation, production release acceptance, and defensive security review.

The skill helps AI agents build software that is modular, testable, reviewable, operationally ready, and safer to release. It supports Codex, Claude Code, Cursor, Trae, Windsurf, GitHub Copilot, and other tools that accept reusable skills, project rules, or custom instructions.

## What This Skill Enforces

- Clear business-module and dependency boundaries.
- One primary responsibility and reason to change per file.
- A hard limit of 800 physical lines for handwritten source files.
- Repository evidence before implementation claims or architectural decisions.
- Relevant process and technology skills before writing code.
- Focused tests, validation commands, and evidence before completion.
- A stop-and-research process for unresolved bugs instead of repeated blind attempts.
- Production acceptance checks with explicit release evidence.
- Defensive, authorized security testing and attacker-minded threat review.

## When to Use

Use this skill when:

- implementing a feature or business workflow;
- fixing a bug or investigating unexpected behavior;
- refactoring large, mixed-responsibility, or tightly coupled code;
- reviewing architecture, module ownership, or dependency direction;
- preparing a build for staging or production;
- performing release-readiness, security, or penetration-test reviews;
- validating user, administrator, tenant, or service-account permissions;
- designing authentication, password recovery, registration, or abuse controls.

## Development Principles

### Modular Ownership

Every responsibility must have a clear owner. UI, orchestration, state, data access, domain logic, types, constants, formatting, and configuration should not be mixed without a strong reason.

Business modules expose intentional public contracts. Other modules must not depend on private implementation files.

### File Responsibility and Size

Each handwritten source file should have one primary responsibility and one primary reason to change.

The hard limit is 800 physical lines. Review responsibilities around 250-350 lines and proactively plan a split around 600 lines. Existing files over the limit must be split before adding more behavior.

### Evidence-First Implementation

Do not invent files, APIs, fields, commands, dependencies, requirements, behavior, or test results.

Verify decisions using repository code, contracts, schemas, configuration, runtime output, tests, or official documentation. Clearly label assumptions that cannot be verified.

## Unresolved Bugs

Do not spend excessive time repeatedly trying the same failed approaches.

After a small number of evidence-driven local attempts:

1. Stop trial-and-error.
2. Search exact errors, official documentation, upstream repositories, release notes, and authoritative technical sources.
3. Confirm that guidance applies to the project's actual versions and environment.
4. Safely test credible findings.
5. Tell the user when the bug remains unresolved.

The final report must explain the observed behavior, evidence, attempted approaches, research sources, likely cause, remaining blocker, and smallest required next action.

## Production Release Acceptance

Before release, every applicable check must be recorded as:

- `Pass`
- `Fail`
- `Blocked`
- `Not Applicable` with a written reason

Skipped, unknown, and untested checks are not passes.

Release acceptance covers:

- critical user journeys and acceptance criteria;
- roles, permissions, tenant isolation, and negative-path behavior;
- validation, errors, retries, recovery, and compatibility;
- unit, integration, end-to-end, regression, and static validation;
- performance, concurrency, reliability, and resource use;
- deployment, configuration, migrations, feature flags, and rollback;
- logs, metrics, traces, alerts, backups, recovery, and incident response;
- security findings, remediation, retesting, and residual risk.

The final recommendation must be `Go`, `Conditional Go`, or `No-Go`, supported by evidence.

## User and Administrator Boundaries

Before release, inventory every UI action, API endpoint, RPC method, job, webhook, import, export, and administrative operation.

For every capability, document:

- allowed actors and roles;
- permitted data and tenant scope;
- authentication and verification requirements;
- server-side authorization policy;
- sensitive effects and required audit events;
- abuse controls and negative test evidence.

Ordinary users must not be able to call administrative APIs, change trusted fields, elevate permissions, cross tenant boundaries, access unrelated data, disable security controls, or invoke maintenance and destructive operations.

Administrator capabilities require least privilege, strong MFA, recent reauthentication, audit records, revocation, and approval controls for high-risk actions.

Client-side visibility, hidden routes, disabled buttons, and UI role checks are never authorization controls.

## Passwords, Credentials, and Accounts

The skill requires secure password and credential handling:

- support long passphrases and password managers;
- reject known-compromised passwords;
- never silently truncate passwords;
- store passwords only with a modern salted adaptive password hash;
- never store plaintext or reversible passwords;
- prevent account enumeration;
- throttle and detect brute force, password spraying, and credential stuffing;
- protect password reset and account recovery with short-lived single-use tokens;
- require MFA or step-up authentication for privileged and sensitive actions;
- rotate and revoke sessions, tokens, API keys, and exposed credentials;
- keep secrets out of source code, clients, logs, builds, and support tools.

## Registration Bot and Abuse Defense

Automated registration must be handled with layered controls rather than one CAPTCHA.

Defenses include:

- server-side rate limits across accounts, devices, networks, behavior, and destinations;
- progressive friction based on risk;
- verification and single-use code protections;
- notification-flood prevention;
- conservative privileges and quotas for new accounts;
- protection for trials, rewards, referrals, messaging, voting, uploads, and APIs;
- replay resistance, idempotency, and concurrency-safe benefit issuance;
- monitoring for account farms and related abusive accounts;
- investigation, reversal, appeals, and false-positive measurement.

Release is blocked when simple automation can farm accounts, rewards, quotas, messages, or high-value capabilities.

## Authorized Security Testing

Security testing must be defensive, authorized, scoped, and evidence-driven.

Before active testing, record:

- written authorization and responsible owner;
- exact in-scope and excluded assets;
- approved identities, environments, dates, and techniques;
- request-rate and safety limits;
- monitoring and incident contacts;
- evidence-handling and deletion rules;
- rollback and recovery procedures.

Immediately stop when testing crosses scope, affects availability, exposes unrelated data, risks destructive impact, or loses monitoring and incident-response coverage.

The skill does not authorize attacks against unrelated systems. Public accessibility does not equal permission.

## Defensive Attacker Mindset

For every important feature and trust boundary, ask:

1. Which asset would an attacker target?
2. Which entry point is reachable?
3. Which assumption or control might fail?
4. Which trust boundary could be crossed?
5. How could multiple weaknesses form an attack path?
6. Which controls prevent, detect, contain, and recover from the attack?
7. What safe evidence proves those controls work?

Review reconnaissance exposure, identity abuse, privilege escalation, unsafe input handling, business-logic abuse, sensitive-data leakage, client manipulation, supply-chain risks, and incident recovery.

Use OWASP ASVS, WSTG, MASVS, MASTG, and NIST SP 800-115 as applicable.

## Installation

### Codex

```text
~/.codex/skills/secure-modular-release-engineering
```

### Claude Code

```text
~/.claude/skills/secure-modular-release-engineering
```

For repository-specific Claude Code usage, place the applicable instructions in the project's `CLAUDE.md`.

### Cursor, Trae, Windsurf, and GitHub Copilot

Add `SKILL.md` as a project rule, agent rule, workspace instruction, or custom instruction according to the tool's supported format.

Keep the `references` directory available so the agent can load detailed modularity, release, and security guidance when needed.

Native skill discovery and exact rule-file locations vary by tool and version.

## Files

- [`SKILL.md`](SKILL.md): Primary workflow and non-negotiable rules.
- [`references/modularity-rules.md`](references/modularity-rules.md): Architecture, responsibility, file-size, dependency, and evidence rules.
- [`references/release-acceptance-and-authorized-security-testing.md`](references/release-acceptance-and-authorized-security-testing.md): Release gates, capability boundaries, credential protection, anti-abuse controls, and authorized security testing.
- [`agents/openai.yaml`](agents/openai.yaml): Codex-facing display metadata and default prompt.

## Release Decision

A release is:

- **Go** when critical acceptance criteria pass and no release-blocking risk remains.
- **Conditional Go** when remaining risks are explicitly owned, time-bounded, monitored, and formally accepted.
- **No-Go** when critical behavior, security boundaries, rollback, recovery, authorization, or evidence remains incomplete.

Never claim software is fixed, secure, tested, or ready without evidence.
