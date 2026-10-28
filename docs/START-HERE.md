# Orientation: how to use this toolkit

**Audience:** Central Tech leadership, functional leads, campus Tech Leads, captains, volunteers, authorized developers, and reviewers.

## Choose your route

| You are... | Start with | Then |
| --- | --- | --- |
| Launching a campus | [Launch guide](../launch/README.md) | Site survey, readiness matrix, assisted launch, evidence and sign-off |
| A new Internet volunteer | [Internet playbook](../playbooks/internet/README.md) | Shadow service, role checklist, supervised operation |
| A Website editor / requester | [Website playbook](../playbooks/website/README.md) | Request brief, content review, staged QA, publishing |
| A developer | [App Development playbook](../playbooks/app-development/README.md) | Approved issue/spec, repo-specific guide, tests and release gates |
| A Tech Lead | [Governance](GOVERNANCE.md) | Review standards, train successors, certify competencies |
| A reviewer / auditor | [Coverage](COVERAGE.md) | Check evidence, freshness, security classification |

## Two-layer documentation pattern

1. **Public reusable guide:** what needs to be achieved, required roles, order of operations, safety boundaries, acceptance criteria, and redacted example artifacts.
2. **Private campus addendum:** where, who, when, and which approved live systems — specific venue, authorized contacts, local inventories, actual configuration details, and linked vault records.

Every instruction that varies by venue should use a named local reference, never publish a copied live configuration.

## Vocabulary

- **Central Tech:** owner of shared architecture, enterprise controls, critical changes, and common standards; not necessarily physically located in Manila.
- **Campus Tech Lead:** person accountable for local implementation and first-line incident ownership.
- **Captain:** shift-level operator directing a service.
- **System owner:** accountable for one platform's access, availability, and release decisions.
- **Evidence:** recorded observation, demonstration, or test output with time, witness, and outcome.
- **Escalation:** transferring the decision or incident to an authorized owner, with enough context for action.
- **No-go:** unresolved critical risk; do not override a gate because a launch date is close.

## Before first use

- Have the functional lead review the applicable playbook and sign the [review template](../templates/DOCUMENT-REVIEW.md).
- Record an authorized local escalation path in the private campus addendum.
- Validate all linked source documents and replace any outdated instructions.
- Rehearse a failure without modifying production infrastructure.
- Run the [readiness assessment](../launch/CERTIFICATION.md) rather than self-certifying from reading alone.

## Suggested operating cycle

Request → qualify → assign owner → use SOP → record evidence → review outcome → update playbook if needed.

The owner of record must close the loop after an incident or unusual service, not merely report that a workaround succeeded.
