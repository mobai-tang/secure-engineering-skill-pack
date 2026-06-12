# Release Acceptance and Authorized Security Testing

## Contents

- Purpose and authorization gate
- Authorization record and stop conditions
- Release acceptance gate
- Functional acceptance
- Quality and operations
- Security acceptance
- Authorized attack simulation
- OWASP-aligned verification matrix
- User and administrator capability boundaries
- Password, credential, and account protection
- Registration bot and automation abuse defense
- Defensive attacker mindset
- Finding lifecycle and report format
- Release decision
- Unauthorized-request handling
- Required report

## Purpose

Use this guide before a production release or when the user requests security testing, penetration testing, attack simulation, adversarial testing, or a release-readiness review.

Security testing must be defensive, authorized, scoped, and evidence-driven. Never test systems, accounts, networks, or data without explicit permission.

## Authorization Gate

Do not begin active security testing until all items are known:

- written authorization and the responsible owner;
- in-scope applications, APIs, hosts, accounts, environments, and dates;
- explicitly excluded targets and techniques;
- permitted test intensity and rate limits;
- approved test data and accounts;
- monitoring, incident contacts, stop conditions, and rollback plan;
- rules for storing, transmitting, and deleting collected evidence.

Prefer a staging environment that accurately represents production. Test production only when explicitly authorized and when safeguards are agreed upon.

Immediately stop and notify the responsible owner if testing causes instability, exposes real secrets or personal data, crosses the approved scope, or may damage data or services.

### Authorization Record

Record authorization before active testing:

| Field | Required detail |
|---|---|
| Requestor and accountable owner | Names, roles, and contact methods |
| Written approval | Ticket, email, contract, or signed rules of engagement |
| Business purpose | Release validation, compliance, remediation retest, or controlled assessment |
| In-scope assets | Exact applications, domains, APIs, IP ranges, repositories, cloud accounts, and environments |
| In-scope identities | Approved roles, tenants, test accounts, API keys, and service accounts |
| Time window | Start, end, timezone, maintenance windows, and prohibited periods |
| Permitted actions | Passive review, safe active tests, automation limits, and explicitly approved higher-risk actions |
| Exclusions | Systems, users, data, techniques, vendors, and geographic regions that must not be touched |
| Safety limits | Request rates, concurrency, resource thresholds, and maximum proof required |
| Monitoring contacts | Operations, security, incident commander, and escalation contacts |
| Data handling | Approved test data, evidence storage, redaction, retention, transfer, and deletion rules |
| Recovery plan | Backups, rollback owner, recovery objective, and validation steps |

If any required field is missing, perform passive analysis only and ask for the missing authorization before active testing.

### Stop, Escalate, and Resume Conditions

Stop active testing immediately when:

- the target, identity, technique, time window, or observed data falls outside the approved scope;
- production availability, latency, error rate, resource use, or business processing degrades unexpectedly;
- a test may alter or delete real data, trigger payments, contact real users, or affect a third party;
- real credentials, secrets, personal data, regulated data, or unrelated tenant data become accessible;
- monitoring or incident contacts become unavailable;
- the observed impact is materially greater than the minimum proof needed;
- the responsible owner requests a pause.

After stopping:

1. Stop generating new traffic or changes.
2. Preserve minimal evidence without collecting additional sensitive data.
3. Record the time, action, affected asset, symptoms, and current system state.
4. Notify the agreed contact using the authorized channel.
5. Assist containment or rollback only when requested and authorized.
6. Resume only after the accountable owner explicitly approves a revised scope or confirms safe conditions.

## Release Acceptance Gate

A release is ready only when the applicable checks have evidence and no release-blocking issue remains.

For each check, record:

- requirement or risk being verified;
- environment, build, commit, configuration, and test-data version;
- owner and execution time;
- method, command, tool, or manual procedure;
- expected result and observed result;
- evidence location;
- pass, fail, blocked, or not-applicable status;
- linked defect, risk acceptance, and retest result when needed.

`Not applicable` requires a written reason. `Skipped`, `unknown`, and `not tested` are not passes.

### Functional Acceptance

- [ ] Acceptance criteria and critical user journeys pass.
- [ ] Permissions and role-specific behavior are verified.
- [ ] Validation, empty states, errors, retries, and recovery paths behave correctly.
- [ ] Data creation, updates, migrations, rollback, and compatibility are verified.
- [ ] Supported platforms, devices, browsers, locales, and accessibility requirements are checked.

#### Functional Verification Detail

| Area | Verify | Required evidence | Release blocker examples |
|---|---|---|---|
| Critical journeys | Primary customer and operator flows from entry to completion | Executed scenarios, screenshots/logs, and resulting records | Login, checkout, payment, publishing, or other critical journey cannot complete |
| Requirements | Every acceptance criterion maps to at least one test | Requirement-to-test mapping and results | Required behavior is absent or ambiguous |
| Roles and permissions | Each role can perform only intended actions | Role matrix and positive/negative test results | Unauthorized role can view or change protected data |
| Validation and errors | Invalid, missing, duplicate, boundary, and malformed input fails safely | Test cases and user-visible/server-side results | Data corruption, unsafe acceptance, or unusable error path |
| Recovery | Retry, timeout, cancellation, partial failure, reconnect, and restart behavior | Controlled failure results and final state | Duplicate processing, lost work, or unrecoverable state |
| Data lifecycle | Create, read, update, archive/delete, export, import, and retention behavior | Before/after data evidence and cleanup confirmation | Incorrect migration, irreversible loss, or privacy violation |
| Compatibility | Supported clients, versions, APIs, integrations, and stored data remain compatible | Compatibility matrix and contract results | Existing supported client or integration breaks |
| Accessibility and localization | Keyboard, focus, labels, contrast, screen reader basics, locale, timezone, and formats | Automated and manual results | Critical task inaccessible or materially misleading |

Test the happy path, realistic failure paths, and boundary conditions. Verify server-side state rather than relying only on the visible interface.

### Quality and Operations

- [ ] Unit, integration, end-to-end, and regression tests relevant to the change pass.
- [ ] Performance, concurrency, resource use, and expected load are acceptable.
- [ ] Logging, metrics, traces, alerts, health checks, backups, and recovery are verified.
- [ ] Deployment, configuration, secrets, feature flags, rollback, and incident procedures are ready.
- [ ] Release notes, known limitations, owners, and support handoff are documented.

#### Quality Verification Detail

| Area | Verify | Required evidence | Release blocker examples |
|---|---|---|---|
| Test coverage | Changed behavior and regression-prone boundaries have appropriate automated tests | Test list, commands, results, and known gaps | Critical behavior has no reliable validation |
| Static quality | Type checks, linting, formatting, builds, and contract generation succeed | Exact commands and clean outputs | Build fails or generated contracts are inconsistent |
| Performance | Response time, throughput, startup, memory, CPU, database, and external-call budgets | Baseline comparison and measured results | Material regression or exhausted capacity |
| Concurrency | Simultaneous actions, locking, idempotency, queues, and eventual consistency | Controlled concurrency results | Duplicates, lost updates, deadlocks, or inconsistent balances |
| Reliability | Timeouts, retries, circuit breakers, degradation, restart, and dependency failure | Failure-injection or controlled outage evidence | Cascading failure or unrecoverable processing |
| Compatibility | Upgrade, downgrade where supported, schema evolution, and mixed-version operation | Migration and compatibility results | Unsafe rollout order or irreversible migration without approval |

#### Operational Readiness Detail

| Area | Verify | Required evidence | Release blocker examples |
|---|---|---|---|
| Deployment | Repeatable procedure, permissions, ordering, health checks, and smoke tests | Deployment record and smoke-test results | Deployment cannot be repeated or validated |
| Configuration | Production values, defaults, environment separation, and feature flags | Reviewed configuration diff and owner approval | Debug mode, unsafe default, or missing required setting |
| Observability | Logs, metrics, traces, dashboards, alerts, and correlation identifiers | Example signals and alert test | Critical failure would be invisible |
| Rollback | Code, configuration, schema, and feature rollback procedure | Successful rehearsal or documented verified procedure | No safe recovery path |
| Backup and recovery | Backup integrity, restore process, recovery time, and recovery point | Recent restore-test evidence | Backups exist but cannot be restored |
| Incident response | On-call owner, runbooks, escalation, communications, and kill switches | Named contacts and exercised runbook | No responsible responder or containment method |
| Support handoff | Release notes, known issues, customer impact, and troubleshooting guidance | Published handoff artifact | Support cannot recognize or respond to expected issues |

### Security Acceptance

- [ ] Authentication, authorization, session management, and account recovery are verified.
- [ ] Inputs, uploads, outputs, redirects, and API parameters are validated safely.
- [ ] Secrets, personal data, logs, caches, backups, and error messages do not expose sensitive data.
- [ ] Dependencies, containers, infrastructure, and configuration are scanned and reviewed.
- [ ] Encryption, transport security, security headers, and trust boundaries are appropriate.
- [ ] Abuse cases, business-logic bypasses, rate limits, and privilege boundaries are tested.
- [ ] Relevant findings are reproduced, risk-rated, fixed or explicitly accepted, and retested.

#### Security Verification Detail

| Area | Verify | Required evidence | Release blocker examples |
|---|---|---|---|
| Identity | Registration, login, recovery, MFA, SSO, session rotation, revocation, and termination | Positive/negative results across approved roles | Account takeover path or unrecoverable session revocation |
| Authorization | Object, function, role, tenant, and administrative boundaries | Access-control matrix and server-side denial evidence | Cross-user, cross-tenant, or privilege escalation |
| Input and output | Validation, parameterization, encoding, uploads, parsing, and redirects | Safe controlled test results and code/config evidence | Untrusted input reaches an unsafe interpreter or sensitive sink |
| Data protection | Classification, minimization, encryption, redaction, retention, deletion, and access logging | Data-flow review and observed storage/transmission behavior | Sensitive data exposed or retained without authorization |
| Secrets and keys | Storage, access, rotation, revocation, and absence from logs/artifacts/clients | Secret scan and configuration review | Live secret exposed or impossible to revoke |
| Dependencies and supply chain | Provenance, vulnerabilities, build integrity, signing, and deployment permissions | Scan results, lockfiles, and release provenance | Known exploitable critical dependency or compromised release path |
| Infrastructure | Least privilege, network exposure, secure defaults, tenancy, backups, and metadata protections | Configuration review and authorized validation | Publicly exposed sensitive service or excessive privileged access |
| Abuse resistance | Rate limits, quotas, automation controls, costly actions, fraud paths, and business invariants | Misuse scenarios and monitoring evidence | Low-effort abuse causes material loss or disruption |
| Detection and response | Security logs, alerts, containment, revocation, investigation, and recovery | Alert exercise and response record | Critical abuse would not be detected or contained |

Security acceptance is not satisfied by a scanner result alone. Combine architecture review, code/configuration review, automated analysis, and controlled behavioral validation.

## User and Administrator Capability Boundaries

Before release, inventory every callable action and classify it by actor, purpose, data scope, and required authorization. Do not rely on hidden buttons, client-side routes, mobile application logic, or undocumented URLs as access controls.

### Capability Inventory

Record every UI action, API endpoint, RPC method, background action, webhook, import/export, file operation, support tool, and administrative command:

| Field | Required detail |
|---|---|
| Capability | Precise action name and owning module |
| Interface | UI route, API endpoint, RPC method, job, webhook, or command |
| Allowed actors | Anonymous user, authenticated user, owner, operator, support, administrator, service account, or other role |
| Allowed data scope | Own record, assigned records, tenant records, selected fields, or global scope |
| Preconditions | Authentication, verified contact, MFA, approval, account state, subscription, or feature flag |
| Server-side control | Authorization policy and enforcement location |
| Sensitive effect | Data access, permission change, money movement, deletion, export, impersonation, or configuration change |
| Required audit event | Actor, target, action, reason, result, timestamp, and correlation identifier |
| Abuse controls | Rate limit, quota, approval, reauthentication, cooldown, alert, or anomaly detection |
| Test evidence | Positive and negative role/scope results |

### User-Callable Capabilities

Users may call only documented capabilities required for their intended workflows. Verify:

- anonymous users can access only explicitly public content and onboarding actions;
- authenticated users can access only their own account, authorized tenant, assigned resources, and permitted fields;
- users cannot supply or override trusted fields such as owner, tenant, role, permission, approval state, price, balance, internal status, or audit metadata;
- users cannot call internal jobs, administrative APIs, debug endpoints, maintenance operations, or privileged exports;
- users cannot change another user's identity, permissions, sessions, MFA, credentials, billing, or protected records;
- bulk actions, exports, searches, reports, and file access enforce the same authorization as individual records;
- asynchronous jobs and callbacks preserve the initiating user's authorization and tenant context;
- disabled, suspended, deleted, unverified, or expired accounts lose the correct capabilities immediately;
- API errors do not reveal whether unrelated resources or accounts exist.

For every user-facing action, test:

1. the intended user and valid data;
2. another user in the same tenant;
3. a user in another tenant;
4. a lower-privilege or suspended user;
5. no authentication, expired authentication, and revoked authentication;
6. direct API invocation without the UI;
7. modified identifiers, trusted fields, and unexpected object references.

### User-Prohibited Capabilities

Ordinary users must not be able to:

- create, assign, or elevate roles and permissions;
- view global user lists, sensitive profiles, secrets, internal identifiers, or unrelated tenant data;
- impersonate users or support staff;
- access administrative dashboards, logs, audit trails, infrastructure, monitoring, or configuration;
- disable security controls, audit logging, MFA policy, rate limits, or alerts;
- modify pricing rules, payment status, balances, refunds, settlement, quotas, or approval outcomes without an explicitly designed authorized workflow;
- execute arbitrary queries, commands, templates, scripts, jobs, or outbound requests;
- access raw backups, unrestricted exports, private files, signing keys, credentials, or production secrets;
- bypass moderation, approval, verification, retention, deletion, or legal-hold rules;
- invoke emergency, recovery, migration, maintenance, or destructive operations.

Attempt each prohibited capability safely using controlled accounts and verify server-side denial, no state change, no sensitive leakage, and an appropriate audit or alert event.

### Administrator-Only Capabilities

Explicitly classify and protect capabilities such as:

- user, tenant, role, permission, and policy administration;
- account suspension, recovery assistance, session revocation, and MFA reset;
- impersonation, support access, and break-glass emergency actions;
- configuration, feature flags, integrations, webhooks, secrets, and key management;
- moderation, approval, refund, payout, billing adjustment, and quota override;
- global search, sensitive reports, bulk exports, audit logs, and compliance operations;
- deployment, migration, maintenance, backup, restore, and destructive operations.

Administrator capabilities require:

- dedicated server-side authorization with default deny;
- least-privilege roles instead of one universal administrator role;
- strong MFA and recent reauthentication for sensitive actions;
- separate privileged accounts where practical, not daily-use user accounts;
- reason capture, immutable audit records, and alerts for high-risk actions;
- approval or two-person control for irreversible, broad, financial, or security-sensitive actions;
- scoped and time-limited support access;
- immediate revocation when the role, employment, incident, or task ends;
- protection against self-approval, self-escalation, and unauthorized role assignment;
- periodic access review and removal of stale privileges.

### Capability Boundary Release Gate

Block release when:

- any capability lacks a documented allowed actor or data scope;
- authorization exists only in the client;
- a user can invoke an administrator or cross-tenant capability;
- privileged actions lack sufficient authentication, audit evidence, or revocation;
- tests do not include negative role and scope cases;
- disabled or revoked identities retain access.

## Password, Credential, and Account Protection

Treat passwords as one part of account security. Prefer phishing-resistant MFA or passkeys for privileged and high-risk accounts where supported.

### Password Creation and Storage

- Allow long passphrases and a practical maximum length of at least 64 characters.
- Do not silently truncate passwords.
- Permit password managers, paste, and common printable characters.
- Reject commonly used, breached, context-specific, and known-compromised passwords.
- Avoid arbitrary composition rules and forced periodic changes unless compromise is suspected or policy requires it.
- Store passwords only with a modern, salted, adaptive password-hashing function configured according to current platform guidance.
- Never store plaintext passwords, reversible encrypted passwords, password hints, or passwords in logs, analytics, support tools, URLs, or client storage.
- Keep optional server-side pepper material separate from the password database and rotate it through an approved recovery plan.
- Protect password-hash parameters and support safe upgrades after successful authentication.

### Login and Authentication Defense

- Use generic failure messages that do not reveal whether an account exists.
- Apply layered throttling by account, device, network, behavior, and risk without allowing easy denial of service against a victim.
- Add increasing delays, temporary cooldowns, and risk-based challenges for suspicious attempts.
- Detect credential stuffing, password spraying, impossible travel, unusual devices, proxy abuse, and distributed low-rate attempts.
- Require MFA or step-up authentication for privileged, financial, destructive, credential, recovery, and security-setting actions.
- Rotate sessions after authentication and privilege changes.
- Revoke sessions and tokens after password reset, account compromise, suspension, or role removal as appropriate.
- Alert users and security owners about high-risk login, recovery, MFA, and credential changes.

### Password Reset and Account Recovery

- Use single-use, short-lived, securely random recovery tokens.
- Bind recovery to the intended account and invalidate older recovery attempts when appropriate.
- Do not reveal account existence through the recovery flow.
- Rate-limit recovery requests and prevent email, SMS, or notification flooding.
- Require additional verification for high-risk recovery, changed contact details, or privileged accounts.
- Do not rely solely on knowledge-based security questions.
- Notify the account owner of recovery attempts and completed changes through an independent channel when practical.
- Revoke active sessions and review sensitive changes after successful recovery.
- Provide a controlled support recovery process with identity verification, audit evidence, and no ability for support staff to learn the password.

### Credential and Secret Handling

- Never expose passwords, API keys, tokens, signing keys, or recovery codes after initial creation when avoidable.
- Store API keys and tokens hashed or encrypted according to their verification and retrieval requirements.
- Give credentials precise scopes, owners, expiry, environment, and revocation procedures.
- Use short-lived credentials and workload identity for services when available.
- Rotate credentials after exposure, role changes, vendor changes, incidents, and according to policy.
- Keep production credentials out of source code, client applications, documentation, screenshots, tickets, and test fixtures.
- Redact secrets from logs, errors, traces, analytics, crash reports, and support tools.

### Password and Credential Release Gate

Block release when:

- passwords can be recovered in plaintext or are stored using unsuitable hashing;
- authentication, recovery, or MFA flows expose account existence or permit practical takeover;
- privileged accounts lack required MFA or step-up controls;
- sessions and credentials cannot be revoked after compromise;
- secrets appear in source code, builds, logs, clients, or public artifacts;
- recovery and support processes lack auditability or identity verification.

## Registration Bot and Automation Abuse Defense

Treat automated registration as an abuse-management problem rather than relying on a single CAPTCHA. Defenses must limit fake accounts while preserving accessibility and legitimate users.

### Registration Risk Model

Identify what attackers gain from registration:

- free trials, credits, coupons, referrals, votes, messages, storage, compute, scraping access, or API quotas;
- ability to spam, impersonate, evade bans, manipulate rankings, test stolen credentials, or exhaust resources;
- access to invitations, private communities, payment flows, support channels, or trusted-user features.

Map abuse cost, expected scale, affected resources, detection signals, and the point at which additional trust should be required.

### Layered Registration Controls

- Rate-limit registration and verification actions across account, device, network, behavior, invitation, and destination.
- Apply progressive friction based on risk rather than challenging every user equally.
- Use bot challenges or proof-of-human checks only as one layer, with accessible alternatives.
- Verify email or phone ownership when justified, while accounting for disposable identities and privacy requirements.
- Delay or limit valuable capabilities until trust increases through verification, account age, successful use, payment, invitation, or review.
- Protect promotional credits, referrals, coupons, trials, voting, messaging, uploads, and API access with separate abuse controls.
- Detect repeated device, network, payment, destination, identity, and behavioral patterns while respecting privacy and legal requirements.
- Use velocity, burst, sequence, timing, repetition, and impossible-behavior signals.
- Maintain deny, challenge, review, allow, and watch decisions rather than only allow or block.
- Provide appeals and recovery paths for legitimate users affected by controls.

### Registration and Verification Endpoint Protection

- Enforce limits server-side; client timers and disabled buttons are not controls.
- Apply limits to registration, login, verification resend, code verification, invitation, recovery, and promotional redemption.
- Prevent unlimited email, SMS, push, or webhook generation.
- Use short-lived, single-use verification codes or links with attempt limits.
- Do not allow attackers to use verification endpoints to enumerate accounts or harass destinations.
- Require idempotency and replay resistance for account creation and reward issuance.
- Ensure parallel requests cannot create duplicate benefits or bypass limits.
- Protect downstream services and third parties with budgets, queues, circuit breakers, and failure handling.

### Post-Registration Abuse Controls

- Give new accounts minimum privileges and conservative quotas.
- Restrict high-risk actions until required trust signals exist.
- Monitor rapid profile changes, contact changes, bulk actions, repeated identical content, unusual navigation, and account farms.
- Link enforcement across related abusive accounts using approved, privacy-conscious signals.
- Revoke rewards, sessions, tokens, and dependent resources when abuse is confirmed.
- Preserve evidence and provide analyst tooling for review, decisions, and appeals.
- Measure false positives, false negatives, challenge completion, abuse cost, user abandonment, and operational workload.

### Automation-Abuse Validation

In an authorized test environment, verify:

1. normal users can register and recover from mistakes;
2. repeated and parallel registration attempts encounter effective limits;
3. distributed low-rate abuse is detected through combined signals where appropriate;
4. verification resend and code attempts cannot create notification flooding or bypass;
5. one identity, device, payment method, invitation, or related cluster cannot repeatedly claim restricted benefits;
6. CAPTCHA or challenge failure does not become the only decision signal;
7. blocked users cannot trivially restart the same abuse path;
8. administrators can investigate, tune, reverse, and audit enforcement decisions;
9. controls fail safely when third-party anti-abuse services are unavailable;
10. monitoring alerts before abuse causes material cost or user harm.

### Registration-Abuse Release Gate

Block release when:

- registration or verification endpoints have no effective server-side limits;
- new accounts immediately receive high-value or high-impact capabilities without risk controls;
- rewards, referrals, trials, voting, messaging, uploads, or API quotas can be farmed through simple automation;
- parallel requests bypass registration, verification, reward, or quota rules;
- abuse cannot be detected, investigated, contained, or reversed;
- anti-bot controls create unacceptable accessibility barriers without alternatives;
- the system cannot distinguish legitimate growth from material automated abuse.

## Authorized Attack Simulation

Use a layered, non-destructive approach:

1. Confirm scope, authorization, safety controls, and baseline system health.
2. Review architecture, trust boundaries, assets, roles, and likely abuse cases.
3. Perform passive review first: code, configuration, dependency, secret, and infrastructure analysis.
4. Perform controlled active testing only within the approved scope.
5. Validate suspected findings with the minimum action needed to prove impact.
6. Avoid persistence, destructive payloads, uncontrolled automation, service disruption, lateral movement, and access to unrelated data unless each action is explicitly authorized.
7. Preserve evidence safely, remove test artifacts, verify recovery, and retest fixes.

Cover applicable areas from the OWASP Web Security Testing Guide and ASVS, including:

- configuration and deployment;
- identity, authentication, authorization, and sessions;
- input validation and output handling;
- error handling and sensitive-data exposure;
- cryptography and transport protection;
- business logic, client-side behavior, and APIs;
- logging, monitoring, rate limiting, and abuse resistance.

For mobile applications, use the applicable OWASP MASVS and MASTG controls.

## OWASP-Aligned Verification Matrix

Use applicable OWASP ASVS, WSTG, MASVS, and MASTG controls as traceable verification requirements. Record the exact control or test identifier when available.

| Domain | Review focus | Safe evidence | Typical required control |
|---|---|---|---|
| Architecture and threat modeling | Assets, trust boundaries, data flows, tenants, roles, and abuse cases | Diagrams, threat model, and reviewed attack paths | Explicit trust boundaries and owned mitigations |
| Configuration and deployment | Debug features, defaults, exposed services, headers, permissions, and environment separation | Configuration diff, exposure inventory, and deployment review | Hardened production configuration |
| Identity | Enrollment, proofing, recovery, MFA, federation, and lifecycle | Controlled identity-flow tests | Strong identity lifecycle and anti-enumeration behavior |
| Authentication | Credential handling, throttling, lockout, bot resistance, and sensitive-action checks | Positive/negative authentication results | Resistance to automated account abuse |
| Authorization | Function, object, field, tenant, and administrative access | Multi-role and multi-tenant denial results | Server-side default-deny enforcement |
| Session management | Token creation, storage, renewal, rotation, expiration, and revocation | Session lifecycle observations | Stolen or terminated sessions can be contained |
| Input validation | Structured input, parser boundaries, uploads, and canonicalization | Safe malformed/boundary cases | Reject or safely interpret untrusted input |
| Output and browser security | Encoding, CSP, cross-origin behavior, framing, redirects, and caching | Browser/configuration observations | Untrusted content cannot execute or leak data |
| Cryptography | Approved algorithms, key lifecycle, randomness, transport, and certificate handling | Configuration and implementation review | Sensitive data protected with managed keys |
| Error handling | Safe failures, exception handling, user messages, and internal details | Controlled error observations | No sensitive leakage and reliable recovery |
| Data protection | Collection, minimization, storage, logs, exports, deletion, and backups | Data-flow and lifecycle evidence | Access and retention match policy |
| Business logic | Workflow order, replay, concurrency, limits, pricing, approvals, and fraud resistance | Controlled misuse-case results | Server-enforced invariants and idempotency |
| API and integrations | Schema validation, auth, scopes, callbacks, webhooks, outbound requests, and third parties | Contract and controlled integration tests | Authenticated, authorized, validated trust transitions |
| Logging and monitoring | Security events, integrity, alerting, correlation, and response | Alert exercise and sample investigation | Actionable detection without sensitive leakage |
| Mobile and client | Local storage, deep links, exported components, backups, updates, and client trust | MASVS/MASTG-aligned observations | Sensitive decisions remain server-enforced |

For every applicable domain:

1. Select requirements based on architecture, data sensitivity, threat model, and release risk.
2. Map each requirement to a test or review method.
3. Record evidence and result.
4. Link failures to findings and owners.
5. Retest fixes and preserve the result.

## Defensive Attacker Mindset

Think in reverse before release: if an authorized adversary wanted to compromise this system, what assets would they target, which trust boundary would they cross, what weakness would make that possible, and which control should detect or stop them?

Use this perspective only for defensive threat modeling and authorized validation. Do not turn the analysis into instructions for attacking unrelated or unapproved targets.

### Attacker Questions

For every feature, endpoint, background job, integration, and administrative capability, ask:

1. What valuable outcome could an attacker pursue: account access, privilege, sensitive data, money, service disruption, fraud, persistence, or reputation damage?
2. What externally reachable or indirectly influenced entry points exist?
3. What assumptions does the implementation make about identity, authorization, input, order of operations, client behavior, and trusted dependencies?
4. Which control is expected to prevent, detect, contain, and recover from abuse?
5. How could several low-severity weaknesses combine into a meaningful attack path?
6. What evidence proves the control works under realistic misuse?

### Reconnaissance and Exposure

An attacker first looks for exposed information and forgotten entry points. Defensively review:

- public domains, applications, APIs, mobile deep links, callback URLs, webhooks, and administrative interfaces;
- development, preview, staging, legacy, debug, monitoring, documentation, and test endpoints;
- source maps, stack traces, verbose errors, API schemas, metadata, version banners, and public repositories;
- exposed secrets, tokens, credentials, private keys, internal hostnames, personal data, and backup files;
- cloud storage, database services, queues, dashboards, CI/CD systems, package registries, and third-party integrations;
- default accounts, sample data, abandoned accounts, stale DNS, unused services, and unsupported dependencies.

Validate that the documented external attack surface matches what is actually reachable. Remove unnecessary exposure and ensure monitoring covers what remains.

### Identity and Account Abuse

An attacker tries to obtain or control a valid identity. Defensively evaluate:

- registration, invitation, login, logout, password reset, account recovery, email or phone changes, and account deletion;
- multi-factor authentication enrollment, challenge, recovery, bypass resistance, and sensitive-action reauthentication;
- session creation, rotation, expiration, revocation, concurrent sessions, remembered devices, and stolen-token containment;
- user enumeration, credential stuffing resistance, brute-force protections, bot controls, and suspicious-login detection;
- OAuth, SSO, magic links, API keys, service accounts, machine identities, and delegated access;
- dormant, terminated, support, test, administrator, and emergency accounts.

Verify that identity controls fail safely, do not reveal unnecessary information, and generate actionable alerts.

### Authorization and Privilege Escalation

An attacker with a low-privilege or compromised account looks for actions intended for another user, tenant, role, or administrator. Defensively evaluate:

- every read, create, update, delete, export, approve, refund, invite, impersonate, and administrative action;
- object ownership and tenant isolation on both direct and indirect references;
- server-side authorization when clients hide or disable controls;
- role changes, group membership, delegated permissions, temporary access, and support tooling;
- batch operations, background jobs, reports, search, file access, and asynchronous workflows;
- differences between web, mobile, API, internal, legacy, and administrative interfaces.

Test with multiple controlled roles and tenants. Verify default-deny behavior and ensure authorization is enforced at the trusted server boundary.

### Input, Injection, and Unsafe Interpretation

An attacker treats every controllable value as potentially reaching a parser, interpreter, query, template, file path, browser, or downstream service. Defensively evaluate:

- URL, path, query, header, cookie, body, multipart, file, metadata, and serialized inputs;
- database queries, search filters, command execution, templates, expression languages, and dynamic configuration;
- HTML and rich text rendering, redirects, links, email content, notifications, PDFs, exports, and spreadsheets;
- file names, archive contents, image or document processing, import and export features, and content-type handling;
- server-side outbound requests, webhooks, callback URLs, integrations, and URL fetchers;
- parsing differences, encoding, canonicalization, duplicate parameters, type confusion, and unexpected nesting.

Use safe test values and controlled destinations. Confirm allowlists, parameterized operations, output encoding, isolation, and rejection behavior.

### Business Logic and Workflow Abuse

An attacker follows valid-looking requests in an unintended order or at an unintended scale. Defensively evaluate:

- skipping required steps, repeating one-time actions, replaying requests, and changing state out of order;
- manipulating prices, quantities, discounts, credits, balances, limits, ownership, status, and timestamps;
- race conditions, duplicate submissions, concurrent updates, idempotency, and rollback behavior;
- approvals, refunds, payouts, promotions, invitations, voting, quotas, trials, and referral systems;
- abuse of automation, scraping, bulk actions, resource exhaustion, and high-cost operations;
- differences between UI restrictions and server-enforced rules.

Model misuse cases alongside normal user journeys. Verify invariants at the server and ensure suspicious patterns are observable.

### Sensitive Data and Privacy

An attacker searches for data that is overexposed, retained too long, or accessible through an unexpected channel. Defensively evaluate:

- API responses, exports, logs, traces, analytics, support tools, notifications, caches, temporary files, and backups;
- secrets in source code, configuration, CI/CD logs, artifacts, client bundles, crash reports, and mobile applications;
- tenant separation, field-level access, redaction, masking, deletion, retention, and consent behavior;
- encryption in transit and at rest, key ownership, rotation, revocation, and access logging;
- indirect leakage through counts, timing, error messages, URLs, filenames, or search results.

Use synthetic data whenever possible. Do not intentionally access unrelated real user data to prove a finding.

### Client, Browser, and Mobile Abuse

An attacker controls the client and can modify requests, local state, application files, and runtime behavior. Defensively evaluate:

- reliance on client-side validation, hidden fields, disabled buttons, local flags, and embedded role checks;
- browser storage, cookies, cross-origin behavior, framing, content security policy, and sensitive caching;
- deep links, intents, custom URL schemes, universal links, exported components, and inter-process communication;
- mobile local storage, logs, backups, screenshots, clipboard use, certificates, and update mechanisms;
- offline actions, synchronization conflicts, tampered clients, rooted or jailbroken environments, and replayed traffic.

Treat all client-provided state as untrusted. Enforce sensitive decisions on trusted services.

### Infrastructure, Supply Chain, and Deployment

An attacker looks beyond application code for weaker dependencies and operational paths. Defensively evaluate:

- dependency provenance, known vulnerabilities, abandoned packages, lockfiles, build scripts, and package registries;
- CI/CD permissions, branch protection, build artifacts, signing, release approvals, and deployment credentials;
- cloud roles, network exposure, firewall rules, storage policies, containers, orchestration, and metadata services;
- default configuration, debug mode, sample credentials, excessive permissions, and environment drift;
- third-party services, webhooks, plugins, analytics, customer support tools, and vendor access;
- backups, disaster recovery, secret rotation, incident response, and compromised-component containment.

Verify least privilege, reproducible builds, protected release paths, secure defaults, and rapid revocation capability.

### Detection, Response, and Recovery

Assume some preventive controls will fail. Defensively validate:

- security-relevant events are logged with sufficient context and protected from tampering;
- alerts detect suspicious authentication, privilege changes, data access, automation, and administrative actions;
- responders can identify affected users, sessions, tokens, data, services, and time windows;
- compromised credentials, sessions, keys, integrations, and deployments can be revoked quickly;
- backups and rollback procedures work without restoring the original weakness;
- incident contacts, escalation paths, evidence preservation, and user notification processes are ready.

Run authorized tabletop exercises for realistic attack paths and confirm owners can contain and recover from them.

### Attack-Path Review

Document plausible attack paths as defensive chains:

```text
Target asset
  -> reachable entry point
  -> required attacker capability
  -> weakness or failed assumption
  -> trust boundary crossed
  -> potential impact
  -> preventive control
  -> detection control
  -> recovery control
  -> safe validation evidence
```

Prioritize chains that require low attacker capability, cross sensitive trust boundaries, affect many users or tenants, evade detection, or combine multiple weaknesses.

For each meaningful path, assign an owner and either:

- break the path with a verified control;
- reduce impact and improve detection;
- explicitly accept the documented residual risk; or
- block release.

## Finding Format

Record every confirmed finding with:

- title, severity, affected asset, and owner;
- authorization scope and test environment;
- observed behavior and supporting evidence;
- safe reproduction conditions without unnecessary exploit detail;
- realistic impact and affected trust boundary;
- root cause and recommended remediation;
- retest result and remaining risk.

Clearly distinguish confirmed findings, unverified suspicions, accepted risks, and informational observations.

### Severity and Priority

Rate findings using evidence, not fear. Consider:

- attacker access and capability required;
- exploit reliability and prerequisite conditions;
- affected users, tenants, systems, data, money, and operations;
- confidentiality, integrity, availability, privacy, safety, and compliance impact;
- detectability, containment, recovery difficulty, and blast radius;
- whether the weakness combines with other findings;
- existing compensating controls and their verified effectiveness.

Use the following decision guidance:

| Severity | Meaning | Default release action |
|---|---|---|
| Critical | Plausible path to catastrophic impact, broad compromise, or severe irreversible harm | No-Go; immediate containment and executive/security escalation |
| High | Plausible material compromise, privilege escalation, sensitive-data exposure, or major disruption | No-Go unless accountable owner formally accepts exceptional risk |
| Medium | Meaningful but constrained impact requiring remediation and tracked ownership | Fix before release when practical, otherwise Conditional Go with deadline and controls |
| Low | Limited impact or hard-to-reach weakness with no meaningful chain demonstrated | Track and remediate according to policy |
| Informational | Improvement opportunity without demonstrated security impact | Document and prioritize normally |

### Finding Lifecycle

1. **Observe:** Capture minimal evidence and stop once impact is proven.
2. **Validate:** Exclude false positives and confirm scope, prerequisites, and affected versions.
3. **Contain:** Immediately report urgent exposure and support authorized containment.
4. **Classify:** Assign severity, owner, affected assets, and release impact.
5. **Remediate:** Fix the root cause and related instances, not only the demonstrated symptom.
6. **Retest:** Repeat the safe validation and verify regression coverage.
7. **Close or accept:** Close with evidence or record formal, time-bounded residual-risk acceptance.

### Detailed Finding Template

```text
Finding ID:
Title:
Status:
Severity and rationale:
Affected assets, versions, roles, and tenants:
Authorization and test environment:
Discovery date and owner:

Summary:
Observed behavior:
Expected secure behavior:
Preconditions:
Safe reproduction conditions:
Evidence location:

Impact:
Trust boundary crossed:
Likely root cause:
Related weaknesses or attack paths:
Existing controls and gaps:

Recommended remediation:
Compensating controls:
Remediation owner and deadline:
Release decision impact:

Retest method:
Retest result and date:
Residual risk:
Risk acceptance owner and expiry, if applicable:
```

## Release Decision

Block release when any of the following applies unless the accountable owner formally accepts the risk:

- a critical or high-severity vulnerability remains unresolved;
- authentication, authorization, sensitive-data protection, migration, rollback, or recovery is unverified;
- a critical user journey fails;
- required monitoring, incident response, backups, or rollback controls are missing;
- testing evidence is incomplete or results cannot be reproduced;
- the release crosses an unresolved legal, privacy, compliance, or authorization boundary.

Report the final decision as one of:

- **Go**: acceptance criteria pass and no release-blocking risk remains.
- **Conditional Go**: remaining risks are documented, owned, time-bounded, and formally accepted.
- **No-Go**: release-blocking defects, security findings, missing evidence, or unsafe conditions remain.

### Decision Requirements

**Go** requires:

- all critical acceptance criteria pass;
- no unresolved critical or high finding;
- required security, migration, monitoring, rollback, and recovery evidence exists;
- failures and skipped checks have no release-blocking effect;
- accountable engineering, product, operations, and security owners agree when applicable.

**Conditional Go** requires:

- no uncontrolled critical risk;
- every exception has an owner, reason, compensating control, deadline, monitoring plan, and formal approval;
- rollback or kill-switch capability limits the remaining risk;
- the release decision states exactly what would trigger rollback or escalation.

**No-Go** is required when:

- authorization, scope, evidence, ownership, or recovery capability is missing;
- a critical journey, security boundary, data migration, rollback, or detection control fails;
- unresolved risk could cause material harm and has not been formally accepted;
- results are inconsistent, unverifiable, or based on assumptions.

Never downgrade a finding or declare a Conditional Go only to meet a release date.

## Unauthorized-Request Handling

Do not perform or provide operational assistance for attacks against systems, accounts, networks, data, or organizations without explicit authorization.

When authorization is absent, unclear, or broader than the requestor can demonstrate:

1. Do not perform active scanning, exploitation, credential testing, persistence, evasion, disruption, data access, or lateral movement.
2. Do not provide target-specific attack steps, destructive payloads, credential theft methods, or instructions intended to evade detection.
3. State that explicit authorization and scope are required.
4. Offer safe alternatives: threat modeling, secure code review, configuration review, lab setup, synthetic examples, defensive monitoring, or an authorization template.
5. Preserve no sensitive target data and do not continue reconnaissance.

Authorization for one asset, account, environment, or test window does not authorize any other target or technique. Public accessibility does not equal permission.

## Required Report

Report:

- release version, environment, scope, date, and responsible owners;
- acceptance criteria and tests performed;
- commands, tools, and evidence actually used;
- passed checks, failed checks, skipped checks, and reasons;
- security findings, severity, remediation status, and retest results;
- operational readiness, rollback readiness, and remaining risks;
- final Go, Conditional Go, or No-Go recommendation.

Never claim a release is safe, secure, tested, or ready without evidence.

## Primary References

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/)
- [OWASP Mobile Application Security Verification Standard](https://mas.owasp.org/MASVS/)
- [NIST SP 800-115: Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final)
