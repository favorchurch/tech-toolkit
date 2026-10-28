# Website Team Playbook

**Status: Provisional.** Derived from existing Website request templates, workshops, staging/cPanel training and offboarding materials. The actual approvals and timelines must be validated by the functional lead.

## Mission

Publish clear, accessible, current and trustworthy ministry information without risking shared website availability or users' information. Website is a publishing product, not merely someone clicking the CMS.

## Typical responsibilities

| Role | Accountable for |
| --- | --- |
| Requester / ministry department | Accurate content, objective, event dates, approved copy and acceptance |
| Content / brand approver | Voice, imagery, design, global or regional brand alignment |
| Website Lead | Intake classification, scheduling, implementation ownership and publishing discipline |
| Authorized editor / developer | Staging and implementation within permission level |
| QA reviewer | Browser/device, accessibility, functional testing and evidence |
| Platform / security owner | DNS, hosting, SSL, security, backups, privileged CMS access, incidents |
| Campus Tech Lead | Local content coordination, authorized local updates, first-line escalation |

For large projects, the requester, design team and developer are distinct roles. An individual may fill multiple low-risk tasks, but must not self-approve sensitive or high-impact releases.

## Request categories

- **Quick correction:** minor text/image/link adjustment within an approved page; expedited but still verified.
- **Simple landing page:** standard component layout, no bespoke payment/data integration.
- **Branded event page:** special design or multi-department content approval.
- **Ticketing/registration page:** payment, forms, identity, data handling or external integration.
- **Global campaign:** multi-campus coordination, translations and consolidated sign-off.
- **Custom web application / Rock integration:** transfer to App Development intake with additional architecture and security review.

These categories reflect the discovered Website request template. Specific lead times from prior documents are **historical inputs**, not universal guarantees.

## Standard workflow

~~~mermaid
flowchart LR
  A[Complete brief] --> B[Content and ministry approval]
  B --> C[Design review if needed]
  C --> D[Build on staging]
  D --> E[Functional and accessibility QA]
  E --> F{Authorized release owner approves?}
  F -- No --> D
  F -- Yes --> G[Publish]
  G --> H[Verify production and close request]
~~~

## SOPs and guidance

- [Publishing, review and release procedure](PUBLISHING.md)
- [Website QA and acceptance checklist](QA.md)
- [Platform, access and offboarding guide](PLATFORM-OPS.md)
- [Website request brief](../../templates/WEBSITE-REQUEST.md)
- [Change request](../../templates/CHANGE-REQUEST.md)
- [App Development handoff](../app-development/README.md)

## Tools and training

Existing Favor workflows use a CMS such as WordPress/Elementor, staging, design prototypes and task tracking. The portable toolkit does **not** mandate one provider or expose real admin endpoints. Editors learn content structure, asset optimization, safe links, mobile layout, consent/privacy, staged QA and rollback expectations before independent publishing.

## Non-negotiable standards

No direct production experiments, no unreviewed purchases/payment changes, no sharing privileged credentials, no live user data in training or screenshots, no bypassing brand/content approval, and no publication without a tested way to restore the prior state.
