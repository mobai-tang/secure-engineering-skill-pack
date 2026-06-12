---
name: modular-maintainable-development
description: Use when implementing features, fixing bugs, refactoring, or reviewing architecture where files may approach 800 lines, responsibilities may mix, business boundaries may blur, relevant skills must guide implementation, or assumptions need repository evidence.
---

# Modular Maintainable Development

## Core Principle

Implement the requested behavior through clear business boundaries and single-responsibility files. Treat structure, dependency direction, testability, and future change cost as acceptance criteria, not optional cleanup.

**Do not confuse fewer files with simplicity. Do not confuse more files with modularity.** Split by responsibility and change reason.

Read [references/modularity-rules.md](references/modularity-rules.md) before changing project structure or implementing a non-trivial feature.

Read [references/release-acceptance-and-authorized-security-testing.md](references/release-acceptance-and-authorized-security-testing.md) before a production release, release-readiness review, security test, penetration test, or attack simulation.

## Before Any Code

Do not write or edit production code until all gates pass:

1. Inspect the available skills and invoke every relevant process and domain skill. Follow process skills first, then implementation skills.
2. Inspect the actual repository, nearby implementations, contracts, configuration, schemas, and tests.
3. Separate verified facts from assumptions. Resolve assumptions from evidence whenever possible.
4. Define the owning business module, responsibilities, target files, public contracts, and tests.

**No relevant skill invocation, no code. No repository evidence, no implementation claim.**

## Required Workflow

1. Complete the skill, evidence, architecture, and test gates above.
2. Assign each responsibility or independently named feature/use case to an existing or new file before coding.
3. Check whether touched files already mix UI, requests, state, types, constants, transformation, or orchestration. Split them before adding more responsibility.
4. Implement through the repository's established patterns. Keep business modules self-contained and expose only intentional public APIs.
5. Put tests beside the responsibility they verify, following local conventions.
6. Review the final diff for boundary leaks, catch-all files, oversized files, unsupported assumptions, and unrelated coupling.
7. Run focused tests plus the repository's relevant validation commands.
8. When a bug remains unresolved after local diagnosis, search the exact error, relevant official documentation, upstream issues, and other authoritative sources before concluding that progress is blocked.
9. Before release, complete the applicable release acceptance and authorized security testing gates. Never perform active security testing without explicit authorization and scope.
10. For security-sensitive work and release reviews, use the defensive attacker mindset to identify valuable assets, reachable entry points, failed assumptions, trust-boundary crossings, chained weaknesses, and missing prevention, detection, or recovery controls.
11. Record each applicable release and security check as pass, fail, blocked, or not applicable with evidence. Never treat skipped, unknown, or untested checks as passing.
12. Before release, inventory user-callable, user-prohibited, and administrator-only capabilities; verify server-side authorization, credential protection, and layered registration-abuse defenses.

## Non-Negotiable Rules

- Keep one primary responsibility and one primary reason to change per file.
- Prefer one independently named feature, use case, handler, service capability, component, or domain concept per file.
- Keep every handwritten source file at or below 800 physical lines. Split before a change would exceed the limit.
- Keep UI components focused on presentation and interaction. Do not embed direct API calls or substantial request, domain, state, or transformation logic in presentation code.
- Keep services focused on one business capability or external dependency.
- Keep hooks/composables/controllers focused on reusable coordination, never presentation.
- Keep utilities pure. Business-specific helpers belong inside their business module.
- Keep types, constants, and state grouped by domain; never grow global dumping grounds.
- Access another module through its public contract, not its internal files.
- Split existing code when a new feature would make its responsibility ambiguous.
- Never invent files, APIs, fields, dependencies, commands, behavior, requirements, or test results. Verify them from repository evidence or label unresolved assumptions explicitly.
- Invoke and follow relevant skills before writing code. Re-check skills when the task changes materially.
- Preserve user changes and avoid unrelated restructuring.
- Never rely on client-side visibility, hidden routes, disabled controls, or UI role checks as authorization.
- Never release authentication, recovery, registration, or administrative workflows without negative-path and abuse-case evidence.
- Never silently abandon an unresolved bug or claim it is fixed without evidence.
- Do not grind indefinitely on a bug. After a small number of evidence-driven local attempts stop repeating experiments, research authoritative sources, and then tell the user if the bug remains unresolved.

## Unresolved Bugs

When a bug cannot be resolved after a small number of evidence-driven attempts using repository evidence, reproduction, logs, focused tests, and systematic debugging:

1. Stop local trial-and-error. Do not keep changing code, rerunning the same commands, or repeating failed approaches without new evidence.
2. Search the web using the exact error message, dependency versions, platform details, and minimal reproduction symptoms.
3. Prefer official documentation, source repositories, upstream issue trackers, release notes, and primary technical sources. Verify that guidance applies to the project's actual versions.
4. Apply and test credible findings when doing so is safe and within scope.
5. If the bug remains unresolved, tell the user promptly. Report the observed behavior, likely cause, evidence gathered, approaches attempted, research sources, remaining blocker, and the smallest next action or missing information needed.

Do not present guesses as fixes, repeat failed approaches without new evidence, hide uncertainty, or spend excessive time trying to solve the bug alone.

## Stop And Restructure

Stop before coding or continuing when:

- a relevant skill has not been invoked or followed;
- a decision depends on an unverified assumption that can be checked;
- a handwritten source file is over 800 lines or the planned change would push it over 800;
- a file mixes two or more architectural layers;
- a component contains substantial fetching, business rules, and rendering;
- a service or store owns unrelated domains;
- a generic `utils`, `helpers`, `common`, `types`, or `constants` file keeps growing;
- a filename no longer accurately describes everything inside it;
- a change requires editing unrelated functionality;
- a file is becoming difficult to navigate, test, review, or safely modify.

## Completion Report

Report:

- relevant skills invoked and how they affected the implementation;
- verified facts, remaining assumptions, and their evidence;
- module and responsibility boundaries chosen;
- files created, split, or deliberately kept together;
- line counts for files near the 800-line limit;
- public contracts and dependency direction;
- tests and validation actually run;
- release acceptance matrix, capability-boundary evidence, credential and registration-abuse results, authorized security testing scope, findings, retest results, exceptions, and final Go, Conditional Go, or No-Go recommendation when applicable;
- any remaining structural debt.
