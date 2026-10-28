# Website intake-to-publication SOP

**Status:** Provisional adaptation of an existing Website quick-update/new-page request process.

## Step 1 — Intake and triage

Requester provides a complete [website brief](../../templates/WEBSITE-REQUEST.md) including campus, target audience, actual required date, the link/page affected, content, before/after examples, design assets, privacy requirements and department approver.

Website Lead determines whether this is a quick edit, a new page, ticketing, global campaign, or a custom app. If custom development, payment or sensitive data is involved, involve Engineering and Data/Security Owners before committing to a date.

**Do not schedule development based on an incomplete brief.**

## Step 2 — Content and approvals

- [ ] Confirm ministry owner, campus scope and named content approver.
- [ ] Check titles, names, event details, legal consent, accessibility and copyright.
- [ ] Obtain content/marketing approval where required.
- [ ] For cross-campus/global pages, route to all affected campus stakeholders.
- [ ] Confirm local-language versions and language ownership if applicable.
- [ ] Define acceptance criteria and actual requested launch time.

## Step 3 — Design and implementation

- [ ] Obtain approved mobile and desktop designs or reuse an approved component.
- [ ] Verify approved design assets and image permissions.
- [ ] Create changes in a private local/development/staging environment as appropriate.
- [ ] Avoid staging exposure of production customer/member data; use redacted fixtures.
- [ ] Preserve a rollback reference (prior page revision, deployment, or backup per platform).
- [ ] Track version, assigned developer and change request link.

## Step 4 — QA and release

The reviewer runs [QA](QA.md) against content, design, mobile/desktop, navigation, forms, performance and access control. Ticketing pages additionally test approved end-to-end purchase or registration with nonproduction test data.

Release is authorized by the designated Website/Platform Owner and the accountable content owner. Privileged DNS, hosting and security changes are reviewed through the system-owner process, not inferred from Website editor access.

## Step 5 — Post-publication verification

- [ ] Independently open production page from at least one mobile and desktop viewport.
- [ ] Verify metadata, canonical links, navigation, primary action, page load and relevant integrations.
- [ ] Check registration, confirmation and automated emails only with approved test accounts.
- [ ] Notify the requester, ask them to verify expected outcome, and record the release.
- [ ] Close the task with evidence; preserve the rollback route if incident follow-up remains.

## Urgent publishing

Urgency changes prioritization, not security, privacy or go/no-go gates. If too late for safe full QA, the approver may authorize **only** a low-risk bounded correction or defer the requested launch; record the reason. Never rush payment, access control or data-processing changes under an ordinary content-edit exception.

## Rollback

If production deviates from approved behavior, stop further edits, notify the release owner, restore the approved known-good version using the platform runbook, verify the prior function, and file a [redacted incident](../../templates/INCIDENT-REPORT.md). Escalate if reverting could affect payments, user data or shared services.
