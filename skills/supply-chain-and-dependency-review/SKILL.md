---
name: supply-chain-and-dependency-review
description: Use when adding or upgrading dependencies, third-party SDKs, package-manager configuration, CI actions, build scripts, Docker base images, registries, signing, or release-pipeline components.
---

# Supply Chain and Dependency Review

## Goal

Prevent unnecessary, unmaintained, vulnerable, overly privileged, or unverified components from entering the build and release chain.

Read [references/supply-chain-checklist.md](references/supply-chain-checklist.md) for the detailed review matrix.

## Workflow

1. Confirm the component is necessary and existing capabilities cannot safely satisfy the need.
2. Review provenance, maintenance, ownership, license, vulnerabilities, permissions, and install or build behavior.
3. Inspect direct and transitive dependency changes, lockfiles, scripts, CI actions, images, registries, and artifacts.
4. Verify versions and immutable references are pinned appropriately.
5. Confirm secrets, credentials, and sensitive files cannot enter logs or artifacts.
6. Run relevant scans, builds, tests, and artifact inspection.
7. Report accepted risk, owners, and rollback or removal path.

## Output

Report component purpose, evidence, lockfile and transitive changes, scripts and permissions, license and vulnerability findings, build and artifact results, risks, and recommendation.
