# App support, incidents, deployments and recovery

## Support routing

1. Local requester/campus tester captures what failed, who is affected (redacted), time, browser/device and safe reproduction.
2. Campus Tech Lead confirms service impact and whether the issue belongs to a local device, network, website, or application.
3. The app owning team investigates production signals; data/security owner joins for access or privacy incidents.
4. Release owner decides mitigation, rollback or controlled forward fix.
5. Requester verifies business recovery and the issue records evidence and prevention.

Campus operators do not need privileged production access to provide high-quality triage evidence.

## Incident response

~~~mermaid
flowchart TD
  A[Observed failure] --> B[Classify impact and data exposure]
  B --> C{Privacy, auth or irreversible change?}
  C -- Yes --> D[Escalate to security/system owner; contain]
  C -- No --> E[Compare logs and baseline]
  E --> F{Known-good rollback available?}
  F -- Yes --> G[Release owner authorizes rollback]
  F -- No --> H[Limit blast radius; use approved fallback]
  D --> I[Verify restored safe state]
  G --> I
  H --> I
  I --> J[Record evidence and assign postmortem owner]
~~~

## Before a deployment

- Check permissions, CI, independent final-SHA review and branch policy.
- Confirm deploy environment, change/feature flag scope, migration plan and health checks.
- Confirm monitored critical dependencies (database, auth, notifications, provider APIs, message queues).
- Validate rollback is technically feasible **before** introducing a non-backward-compatible change.

## After deployment

- Verify request/build/deploy success from actual provider state.
- Exercise authorized happy and negative paths with test identities.
- Compare error rate, latency and key user outcomes to known baseline.
- Observe cross-campus isolation and dependency health if shared.
- Set/verify owner for any delayed effects; rollback promptly if required.

## Failures that need specialist handling

- **Authentication or data isolation:** security owner; immediate containment before disclosure.
- **Shared database saturation:** system owner reviews app pools, queueing and other consumers; do not restart shared infrastructure as a first unapproved step.
- **Print/relay/venue-specific device:** reproduce on supported device/driver, check local connectivity, escalate to app and device owners.
- **Registration/financial transactions:** stop uncontrolled retries; verify final state and duplicate effects with authorized owners.
- **Unexpected permission or webhook behavior:** capture redacted request metadata, review signing/claims, avoid redistributing tokens.

## Disaster recovery

Each app's **private** runbook must identify backup location, restore authorization, recovery and data-loss objectives, required platform credentials in vault, owner succession and rehearsal history. This public document does not assert any numerical RTO/RPO.

## Handover

Use [team handover](../../templates/TEAM-HANDOVER.md). Transfer unresolved incidents, queue owners, deployment notes and renewal dependencies; never hand over a password in a document.
