# Engineering quality standards and acceptance

**Applicability:** all apps; individual repository policies can be stricter. Do not weaken existing gates by citing this generic checklist.

## Reliability and performance

- [ ] Major user journeys tested from the correct environment and permission role.
- [ ] API errors, timeouts and retries are bounded; duplicate submissions behave safely.
- [ ] Representative load/degraded behavior tested for operations-critical endpoints.
- [ ] Database connections, batching and query cost considered under multiple app instances.
- [ ] Monitoring, logs and alert owners identified; no PII/secrets leaked into logs.
- [ ] Document baseline, regression threshold and environment before claiming performance improvements.

## Authorization and data boundaries

- [ ] Authenticate caller securely and authorize **server-side** per action.
- [ ] Restrict to the caller's permitted people/campuses/groups, not client-provided IDs alone.
- [ ] Ensure sensitive child, family, pastoral, financial and identity records have explicit policy and negative tests.
- [ ] Audit integration scopes, rate limiting, webhook authenticity and least privilege.
- [ ] Distinguish unknown, unauthenticated and unauthorized outcomes correctly.
- [ ] Test read/write ownership across campus partitions; absence of UI controls does not prove protection.

## Change safety

- [ ] Test new code and relevant regression paths, including failure and rollback.
- [ ] Use environment-specific secrets in approved vault/store, not source files.
- [ ] Check dependency and license risks.
- [ ] Use migration controls for existing schemas, with compatibility and safe backout planning.
- [ ] Run lint/typecheck/tests according to the current project standard.
- [ ] For production change, obtain independent last-SHA review and explicit release authorization.

## User experience

- [ ] Loading, error, empty and offline states are clear and recoverable.
- [ ] Important user actions are discoverable on mobile and desktop.
- [ ] Accessible names, focus order, sufficient contrast and semantic elements used.
- [ ] Destructive operations require appropriate user intent and confirmation.
- [ ] Privacy-aware analytics and useful diagnostics allow support without exposing records.

## Release evidence

Attach a concise evidence record: tested revision, test command(s) and actual result, representative user role, deployment ID/status, smoke checks, observed incidents, rollback reference and authorized approver. An AI-generated statement is not evidence.

## Review scope

1. **Spec review:** acceptance criteria met, no unexpected behavior.
2. **Security review:** role/data/tenant boundaries.
3. **Standards review:** code, testing, maintainability.
4. **Release review:** correct target, readiness and recovery.

Severe risks block deployment; noncritical follow-ups have named owners and due dates.
