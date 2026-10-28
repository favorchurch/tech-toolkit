# Volunteer training, mentoring and competency

**Status:** proposed structured curriculum adapted from existing Tech volunteer onboarding and Internet shadow-service practices.

## Culture

Lead with service, curiosity, generosity and ownership. Teach people to improve systems and transfer knowledge, not merely operate them. Training must be safe for learners and safe for the people relying on the systems.

## Standard training ladder

~~~mermaid
flowchart LR
  A[Interest and screening] --> B[Orientation and required safeguards]
  B --> C[Observe a qualified operator]
  C --> D[Supervised practice]
  D --> E[Competency demonstration]
  E --> F[Delegated role access]
  F --> G[Refresh and mentor others]
~~~

## Common orientation

1. Tech mission, campus roles, expected conduct and serving culture.
2. Privacy, safe handling of children/family/financial data, consent and the NDA process where applicable.
3. Tool access: least privilege, MFA, approved communication and handling of screenshots.
4. Incident protocol: observe, contain, escalate, record. Never guess an admin change.
5. Service teamwork: handovers, safe event-day communication and debrief.
6. Role assessment and refresher expectations.

## Role-specific learning paths

| Track | Observe | Practice supervised | Demonstrate independently |
| --- | --- | --- | --- |
| Internet volunteer | Setup, viewer check, cable safety, packdown | Perform preflight role, monitor, record issues | Safe setup; end-to-end verification; a simulated degraded-mode response |
| Internet Captain | Runbook, team briefing, role assignment | Direct setup/transition/packdown | Go/no-go call; lead escalation; verify restoration and custody |
| Website editor | Content standards, staging, request workflow | Make a nonproduction edit and run QA | Obtain approval; publish approved low-risk change with reviewer and rollback |
| Website lead/publisher | Content/brand, access and release owners | Review a multi-stakeholder page | Release/rollback decision, evidence-based acceptance, offboarding |
| App contributor | Repo README, tests, permission rules | Implement scoped change in sandbox | Tests and PR with actual evidence and secure negative cases |
| Campus app support | Bug intake and role boundaries | Reproduce in test environment | Redacted high-quality escalation and post-fix verification |

## Assessing competencies

- [ ] Trainee can explain the purpose and safety boundary of the task.
- [ ] Trainee performs the workflow unaided in a suitable rehearsal.
- [ ] Trainee recognizes a stop/escalation trigger.
- [ ] Trainee communicates an issue without sharing sensitive information.
- [ ] Assessor records observed evidence and approved role scope.
- [ ] Trainer provides feedback, outstanding tasks and next reassessment date.

Use the [skills matrix](../templates/ROLE-COMPETENCY.csv) and [document review](../templates/DOCUMENT-REVIEW.md).

## Training formats

- Short self-study guide (public)
- Shadow service or screen-share demo (restricted if it reveals live systems)
- Safe simulation or nonproduction staging exercise
- Assessed practice and teach-back
- Quarterly refresh or change-triggered rehearsal

Do not substitute a watched video for observed competency on a live-critical responsibility.

## Reuse the existing onboarding materials

The 2026 volunteer presentation and older workshops are useful source material, but completed slides may contain names, imagery or schedules not suitable for public reposting. Rebuild educational assets with approved, anonymized examples if needed; maintain the original deck in its existing permission-controlled workspace.
