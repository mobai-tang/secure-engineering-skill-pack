# Modularity Rules

## Contents

- Architecture decision
- Skill invocation gate
- Evidence-first implementation
- Responsibility placement
- Business module structure
- File size and feature boundaries
- Active split criteria
- Dependency boundaries
- Review checklist
- Rationalization traps

## Architecture Decision

Before implementation, answer:

1. Which business capability owns this change?
2. Does an existing module own it, or does it require a new module?
3. Which responsibilities are introduced: UI, orchestration, state, data access, domain rules, types, constants, formatting, configuration?
4. Where does each responsibility belong under the repository's established conventions?
5. Which public contract should other modules use?
6. Will adding the change make any existing file harder to name, test, review, or change independently?

Do not begin implementation until every introduced responsibility has an owner.

## Skill Invocation Gate

Before reading or editing implementation code:

1. Inspect the available skill metadata for relevant process and domain skills.
2. Invoke relevant process skills first, such as brainstorming for creative behavior changes, systematic debugging for bugs, and test-driven development for implementation.
3. Invoke relevant technology or domain skills next.
4. Read and follow the invoked skills before writing code.
5. Re-evaluate skill applicability whenever the task scope or technology changes.

Do not treat remembering a skill as invoking it. Do not perform a "quick edit" before the skill check.

## Evidence-First Implementation

Prohibit hallucinated implementation decisions. Before relying on a claim, find evidence in the repository, runtime output, official documentation, schemas, generated clients, contracts, or tests.

| Claim | Required evidence |
|---|---|
| A file, class, function, route, or field exists | Locate and read its definition or generated contract |
| An API accepts or returns a shape | Inspect controller/handler, schema, client, tests, or observed response |
| A dependency or command is available | Inspect manifests/lockfiles/config and run the relevant command |
| A framework pattern is used by the project | Inspect nearby working implementations and configuration |
| A bug is fixed or behavior works | Reproduce the original symptom and run relevant tests |
| A requirement is intended | Use the user's request, repository specification, or ask when not discoverable |

When evidence is unavailable:

- state the uncertainty explicitly;
- avoid presenting an assumption as fact;
- choose the smallest reversible implementation only when it is safe;
- ask the user when the unresolved choice materially changes behavior, data, security, or architecture.

Never fabricate test execution or success. Report exact commands and observed results.

## Responsibility Placement

| Responsibility | Place it in | Keep out of |
|---|---|---|
| Reusable or page UI | components/views/widgets | service and data-access logic |
| Reusable lifecycle/state coordination | hooks/composables/controllers | rendering markup |
| API calls and external systems | services/clients/repositories | UI components |
| Domain decisions and workflows | domain/use-cases/services | generic utilities |
| Shared state | domain-specific store/state module | one global catch-all store |
| Pure transformation or formatting | narrowly named utility | side effects and hidden state |
| Data contracts | domain-specific type/model files | unrelated global type files |
| Fixed values and enums | domain-specific constants/config | scattered magic values |
| Private styles | component/module-local styles | unrelated global styles |
| Cross-module access | explicit public API or interface | internal module paths |

Adapt directory names to the language and repository. For example, Flutter may use `features/`, widgets, providers, repositories, and models; Java may use domain/application/infrastructure packages; Python and Go may use packages by capability. Preserve the principle even when names differ.

## Business Module Structure

Prefer self-contained business modules once a capability has its own behavior, data contracts, state, or UI.

```text
src/
  modules/
    feature-name/
      components/
      hooks/
      services/
      types/
      constants/
      utils/
      store/
      styles/
      index.ts
```

Create only directories the feature actually needs. The structure is a responsibility map, not a quota.

The module's public entry point exposes intentional contracts. External modules must not reach into private implementation folders. Shared code belongs globally only when it is genuinely domain-neutral and reused by multiple modules.

## File Size And Feature Boundaries

Use independently understandable features and responsibilities as the primary split boundary:

- Prefer one named feature, use case, handler, service capability, component, model, or domain concept per file.
- Split large features into orchestration plus focused collaborators rather than hiding all logic in one "feature file".
- Keep tests scoped to the corresponding feature or responsibility.
- Do not combine unrelated small features merely to reduce file count.

**Hard limit: every handwritten source file must stay at or below 800 physical lines.**

The 800-line threshold is a deliberately generous guardrail, not a universal scientific boundary. It exists to force an ownership and responsibility review before a handwritten file becomes unusually difficult to navigate, test, review, and change safely. Teams may adopt a stricter documented threshold. Raising it requires repository-specific evidence and an explicit policy decision; do not bypass it ad hoc for one change.

Before editing, measure touched files. Estimate whether the change will approach the limit. At 600 lines, proactively review and plan a split; never wait until line 800 to think about structure. If an existing handwritten file exceeds 800 lines and must be changed, split it as part of the change before adding functionality.

Allowed exceptions are limited to generated code, lockfiles, machine-produced schemas, vendored code, and cohesive declarative data that cannot be safely split. Do not hand-edit generated or vendored exceptions. Document any declarative-data exception in the completion report.

The 800-line limit does not justify meaningless fragmentation. Extract cohesive concepts with precise names and explicit contracts.

When a team adopts a different threshold, document the value, rationale, exceptions, and enforcement location in repository policy. Preserve the underlying goal: prevent unclear ownership, mixed responsibilities, and changes that are difficult to review or validate.

## Active Split Criteria

Split or reorganize before adding behavior when any condition applies:

1. The file contains multiple layers such as UI, API access, state, and domain decisions.
2. The file has multiple independent reasons to change.
3. A component contains substantial sub-UI, branching business rules, requests, and state coordination.
4. Logic is reused or likely to require independent testing.
5. A capability has a clear independent business boundary.
6. Editing one file risks unrelated features.
7. The filename cannot precisely describe the contents.
8. A broad file such as `utils.ts`, `helpers.py`, `common.go`, `types.ts`, or `constants.ts` keeps expanding.
9. A store or service manages unrelated domains.
10. Navigation and review are becoming difficult because of file size or complexity.

Use line count as an enforceable guardrail:

- Around 250-350 handwritten lines: review responsibilities and complexity.
- At 600 handwritten lines: proactively design and schedule the split before adding substantial behavior.
- Above 800 handwritten lines: do not add functionality; split the file first.
- Generated, vendored, lock, machine-produced schema, and documented cohesive declarative-data exceptions do not permit new handwritten logic.

Avoid meaningless fragmentation. A tiny file is useful only when it creates a real boundary, isolates change, enables reuse/testing, or matches an established pattern.

## Dependency Boundaries

- Keep dependencies pointing inward toward stable domain contracts.
- Put external API and persistence details behind services, clients, repositories, or adapters.
- Avoid circular dependencies and cross-module imports of internals.
- Prefer explicit parameters and return values over hidden global state.
- Place module-specific utilities, types, and constants inside the owning module.
- Promote code to global shared space only after genuine cross-domain reuse is proven.
- Keep configuration separate from business logic.
- Keep tests aligned with the responsibility under test.

## Review Checklist

Before completion, verify:

- [ ] Relevant process and domain skills were invoked before code changes.
- [ ] Every implementation claim is supported by repository/runtime/documentation evidence.
- [ ] Assumptions are explicitly identified and resolved or reported.
- [ ] Every changed file has one clear responsibility and accurate name.
- [ ] Every handwritten source file is at or below 800 physical lines.
- [ ] Existing over-limit files touched by the change were split before expansion.
- [ ] Independently named features/use cases have focused file ownership.
- [ ] New responsibilities have explicit owners.
- [ ] UI does not contain substantial request or domain logic.
- [ ] Services, stores, types, constants, and utilities are domain-scoped.
- [ ] No catch-all file or module was introduced or enlarged.
- [ ] Business modules expose intentional public contracts.
- [ ] Cross-module dependencies do not reach into internals.
- [ ] Complex or reused logic is independently testable.
- [ ] Existing large mixed-responsibility files were split before expansion.
- [ ] Generated/declarative exceptions are documented when kept large.
- [ ] Focused and relevant repository-wide validation passed.

## Rationalization Traps

| Rationalization | Required response |
|---|---|
| "It is faster to put it in this page for now." | Create the correct responsibility owner now; temporary coupling becomes permanent. |
| "I know the framework/API, so I can assume it exists here." | Inspect this repository's actual contracts and configuration before implementation. |
| "The likely field or route name is obvious." | Locate the definition or observed response; likely is not evidence. |
| "I remember the relevant skill." | Invoke and read the current skill before acting. |
| "I will invoke the skill after this quick edit." | Stop. Skill selection and invocation happen before any code edit. |
| "It is only one more helper/type/constant." | Put it in the owning domain; do not enlarge a dumping ground. |
| "Splitting can happen after the feature works." | Split before expansion so tests and implementation follow the intended boundary. |
| "Eight hundred lines is only a guideline." | It is a hard cap for handwritten source files; split before crossing it. |
| "This is one feature, so one giant file is acceptable." | One feature may still contain multiple responsibilities; split into focused collaborators. |
| "The framework encourages one file." | Use the framework's supported extraction mechanisms and local conventions. |
| "More files are overengineering." | Judge boundaries by independent change and testability, not file count. |
| "The file is long but still works." | Working behavior does not remove navigation, review, coupling, or regression costs. |
| "A shared module is convenient." | Shared code must be domain-neutral and genuinely reused, not merely accessible. |

## Red Flags

Stop and restructure if the implementation plan includes:

- writing code before invoking relevant skills;
- claiming an API, file, field, requirement, command, or result without evidence;
- editing an over-800-line handwritten source file without first splitting it;
- creating or expanding a handwritten source file beyond 800 lines;
- adding unrelated code to an already large file;
- direct API calls embedded in presentation code;
- a new catch-all helper, common, type, constant, service, or store file;
- reaching into another module's private folders;
- mixing UI, requests, state, types, and configuration in one file;
- postponing structural work until "later";
- using file count reduction as the primary measure of simplicity.
