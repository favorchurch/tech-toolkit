# Website platform operations, access and recovery

## Split the privileges

**Authorized campus editors:** correct approved content, maintain designated campus pages, follow staging and QA.

**Website/Platform Owners:** manage privileged CMS configuration, hosting, DNS, TLS, CDN/security policy, site-wide plugins, backups, subscriptions and production recovery, under role-specific approval.

**Application/Database Owners:** manage user-data integrations, API permissions and custom app functionality.

An editor should never need broad cloud/domain admin permissions to publish a routine event update.

## Operating cadence

- **On intake:** record platform dependency and release owner.
- **Before each publication:** confirm staging isolation, correct destination and tested rollback.
- **After publication:** production smoke test and owner notification.
- **Periodic:** review CMS accounts, plugin/core updates, renewal calendars, backups, restored test evidence and stale content.
- **After incidents:** record impact, recover, rotate impacted secrets where needed and update training.

## Staging discipline

Staging uses its own auth boundary and sanitised data. Any production cloning must follow an approved scrub-and-restrict process. Limit indexing, prevent uncontrolled outbound emails/payment transactions, remove excess users, and verify certificate/hostname behavior. Old instructions about cloning should not be copied verbatim across providers.

## Subscriptions and renewals

A central asset/subscription owner records name, purpose, billing owner, renewal date, business continuity impact, and offboarding plan in a restricted register. The public toolkit does not disclose actual license numbers, payment methods or account details.

## Onboarding / offboarding access

1. Get manager/system-owner request and minimum role.
2. Grant a personal account and appropriate MFA; record approval privately.
3. Provide supervised nonproduction training.
4. When a person leaves or changes role, revoke CMS, hosting, DNS, task tracker, design workspace, linked accounts and recovery factors as applicable.
5. Check inherited groups, shared account use and any unattended integrations.
6. Verify removal and close an [access review](../../templates/ACCESS-REVIEW.md).

## Incident escalation

Public outage or affected donations/registration requires the Platform Owner and related ministry teams. Unauthorized content or data exposure requires immediate security escalation; do not attempt independent public-history cleanup before incident containment.

## Local addendum fields

Provider names, actual hosting architecture, private staging controls, restoration tooling, privileged contacts, DNS configuration, current certificate paths, safe cutover steps, and subscription references — all private and access controlled.
