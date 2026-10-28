# Website QA and publication acceptance

**Use per page or campaign.** Mark each item PASS / FAIL / NOT APPLICABLE with an observed result and reviewer.

## Content and design

- [ ] Title, schedule, venue, prices, contacts and deadlines reflect approved content.
- [ ] On-brand typography and design assets are approved; no unlicensed material.
- [ ] Navigation, menus, links, anchor jumps and search references work.
- [ ] Desktop and representative narrow mobile layouts are usable; no hidden critical action.
- [ ] Images are optimized and have descriptive alternatives where informative.
- [ ] Supported locales and translations have named approvers.

## Accessibility

- [ ] Complete journey possible with keyboard alone; focus visible and ordered.
- [ ] Inputs have persistent labels, errors and accessible names.
- [ ] Contrast and text scaling support practical reading.
- [ ] Headings are semantic; meaningful images, links and icons have appropriate text.
- [ ] Video/caption requirements agreed with content owner.
- [ ] Validate applicable accessibility standard with the organization owner; do not claim formal compliance from this checklist alone.

## Forms, payments and identity (when applicable)

- [ ] Data minimization and consent approved.
- [ ] Required/optional fields, validation and error recovery work.
- [ ] Duplicate submission/retry behavior verified without charging twice.
- [ ] Test checkout/registration follows approved sandbox or safe fixture.
- [ ] Confirmation/receipt and notification tested end-to-end.
- [ ] Permission boundaries verified; pages do not expose private records or admin controls.
- [ ] Logs and analytics do not capture sensitive field contents.

## Performance, SEO and release

- [ ] Core page/action responds under approved local performance budget.
- [ ] No blocking resource, console error or obvious broken asset.
- [ ] Correct indexing and metadata for public or deliberately hidden pages.
- [ ] Staging URL not advertised as canonical production URL.
- [ ] Prior version/backups can be restored by an authorized owner.
- [ ] Release owner, approver and verification time recorded.

## Decision

**PASS:** all critical journey, accessibility and privacy checks pass. **CONDITIONAL:** only noncritical deficiencies have approved owner/deadline. **FAIL:** broken primary action, unreviewed sensitive-data/payment flow, insufficient auth, or no responsible release owner. A FAIL is a no-go.

Record evidence in the [website request](../../templates/WEBSITE-REQUEST.md) or restricted task tracker. Do not attach real attendee/payment data to public issues.
