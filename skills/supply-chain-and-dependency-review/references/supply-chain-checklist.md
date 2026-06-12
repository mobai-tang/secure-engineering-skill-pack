# Supply Chain and Dependency Review Checklist

## Necessity and Ownership

- Is the dependency or service necessary?
- Can the repository's existing dependency or standard library satisfy the need?
- Is there a clear internal owner and removal path?
- Is the integration isolated behind an intentional contract?

## Provenance and Maintenance

- Verify official source, publisher, repository, registry, and package identity.
- Review release cadence, recent maintenance, unresolved security issues, deprecation, and bus factor.
- Check for suspicious ownership changes, typosquatting, abandoned packages, or unexpected binary downloads.
- Review license compatibility and attribution requirements.

## Version and Locking

- Pin dependencies according to repository policy.
- Review lockfile changes and unexpected transitive additions.
- Pin CI actions and reusable workflows to trusted immutable references when practical.
- Pin Docker base images or record controlled update policy and provenance.
- Avoid unreviewed floating tags such as `latest`.

## Scripts and Build Behavior

- Review install, postinstall, prebuild, build, publish, lifecycle, and code-generation scripts.
- Review downloaded binaries, native extensions, network access, filesystem access, and environment-variable use.
- Confirm build steps do not execute untrusted pull-request content with secrets or privileged tokens.
- Verify artifact signing, provenance, checksums, and reproducibility where required.

## Permissions and Secrets

- Grant CI jobs, actions, package registries, cloud roles, and tokens minimum permissions.
- Separate build, test, publish, and deploy credentials.
- Prevent secrets from entering logs, caches, client bundles, images, archives, reports, or source maps.
- Verify forked or external contributions cannot access protected secrets.

## Vulnerabilities and Risk

- Run ecosystem-appropriate vulnerability and license checks.
- Confirm findings apply to actual versions, runtime paths, configurations, and exposure.
- Do not ignore findings without documented rationale, owner, expiry, and compensating controls.
- Review dependency confusion, registry fallback, namespace, and private-package controls.

## Required Evidence

Record:

- why the component is needed;
- source and ownership verification;
- version and immutable reference;
- direct and transitive changes;
- license result;
- vulnerability result;
- scripts and permissions reviewed;
- build, test, and artifact-inspection results;
- rollback or removal plan;
- remaining risk.

## Blockers

Block adoption or release when provenance is uncertain, critical exploitable risk remains, secrets can reach untrusted code, privileged build steps are unsafe, artifacts cannot be verified, or license obligations are unacceptable.
