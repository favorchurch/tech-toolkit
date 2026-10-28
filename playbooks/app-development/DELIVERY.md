# Engineering issue-to-production SOP

**Status:** Proposed common guardrails synthesized from representative app repository practices.

## 1 — Intake

Requester provides ministry problem, affected campus(es), desired outcome, urgency, reproduction/evidence (redacted), and an approver. Create or link a canonical GitHub issue. Coordinate in the accepted department tracker without maintaining contradictory technical specifications in multiple places.

## 2 — Decision and risk classification

- [ ] Identify whether change affects data permissions, children/minors, giving, identity, payments, multi-campus isolation, or shared databases.
- [ ] Identify owner of original data and owner of any derived/estimated data separately.
- [ ] Identify rollback reversibility and any required migration.
- [ ] Elevate only meaningful human decisions: product behavior, security, ownership, irreversible rollout.
- [ ] Specify acceptance scenarios and negative authorization cases.
- [ ] Determine appropriate risk class and reviewer/approval requirement.

Low-level naming, implementation and test structures can be chosen by the implementing engineer if consistent with repository standards.

## 3 — Plan and implement

- [ ] Read current code, README, source-of-truth documents and relevant issues before editing.
- [ ] Prefer the smallest cohesive change; do not widen scope with unrelated cleanup.
- [ ] Plan for cloud/remote execution by default when tool capabilities and the task allow it. Use local execution for hardware, protected environments, or tests that require actual venue equipment.
- [ ] Maintain explicit code ownership and task boundaries when parallel agents work.
- [ ] Include targeted unit/integration tests and negative cases relevant to the change.
- [ ] Never bypass authorization or generate a false test result merely to meet a deadline.
- [ ] Write migration, compatibility or feature flag notes when changing schemas.

## 4 — Pull request and review

PR explains issue/spec link, user impact, design choice, changed files, tests actually run, risk, rollout plan and rollback. Independent review checks both **standards** and **spec**, anchored to the exact final SHA. A code review pass before the final changes is not release approval.

CI must match changed risk: targeted fast feedback is preferred for routine changes, with comprehensive suite or deployment gates where risk warrants it. Failed mandatory checks are not silently ignored. A system owner may approve an explicitly documented emergency exception with compensating verification only where policy permits; data/security gates remain mandatory.

## 5 — Release

- [ ] Correct destination and deployment identity verified.
- [ ] Source/target revision recorded; approved change window known if needed.
- [ ] Backups/migration safety and rollback prerequisites confirmed.
- [ ] Authorized release owner explicitly confirms all gates.
- [ ] Deploy through the repo's approved pipeline; don't edit live production by hand without policy exception.
- [ ] Run smoke tests on representative workflows and campus partitions.
- [ ] Check error, latency and resource signals against pre-release baseline.
- [ ] Notify the relevant campus requester and on-call owner.

## 6 — Close the loop

Close the issue only with read-back evidence of the resulting state, not by PR creation. Document any remaining follow-up, link incidents, identify monitoring ownership, and revise the right README/runbook. For work delegated to a local agent, provide a directly executable handoff stating the exact remaining work and observed repository state — not a request to launch another orchestrator.

## Explicit stop points

Missing data authority; unresolved privacy/child-safety risk; untested database migration; inability to roll back critical changes; mandatory CI/review failure; unclear production owner; potential cross-campus data leak.
