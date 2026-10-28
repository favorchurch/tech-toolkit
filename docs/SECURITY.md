# Security and public-documentation boundary

**Publication model:** open-source, security-sanitized, portable. This repository must be safe for anyone on the internet to clone.

## Classification decisions

| Class | Examples | Approved home |
| --- | --- | --- |
| Public/reusable | Generic roles, workflows, checklists, vendor-neutral diagrams, redacted training screenshots | This GitHub repository |
| Internal/campus | Current venue inventory, local radio or escalation contacts, exact cable routes, account ownership, detailed operational topology | Access-controlled campus records |
| Privileged/security | Administrative URLs/IPs, security rule internals, sensitive integration trust boundaries, incident recovery authority | Restricted security/system-owner documentation |
| Secret | Passwords, Wi-Fi passphrases, private keys, tokens, refresh secrets, API credentials, backup codes | Approved vault only |

Public docs may describe **what** to check, but not the live values or exploitable details **used to access** systems.

## Never commit or publish

- Any real credential, bearer token, recovery code, private key, or full environment configuration.
- A live administrative username paired with its endpoint or sensitive security settings.
- Detailed venue topology or diagrams that expose real internal network segmentation, management interfaces, or access paths.
- Personal phone numbers, private email addresses, individual availability, confidential ministry data, or sample real registrations.
- Screenshots with browser auth cookies, user records, private labels, QR codes, log lines containing tokens, or access codes.
- Third-party copyrighted material, proprietary license keys, or assets without permission to redistribute.

A Google Drive or vault link is not itself an access-control mechanism. Do not publish sensitive file URLs simply because they require login.

## Safe documentation pattern

Use plain placeholders such as **[CAMPUS]**, **[APPROVED_PRIMARY_UPLINK]**, **[STREAM_OWNER]**, **[PRIVATE_RUNBOOK_LINK]**, and **[VAULT_RECORD_ID]**. Keep the placeholder's definition private. Do not insert a functioning URL or network address as an example when documentation-only text will do.

## Authorization

- Grant access by role, not by convenience; remove access as soon as the role ends.
- Use separate personal accounts and MFA where supported; avoid shared admin credentials.
- Campus operators receive only the access needed for their approved procedures.
- Production changes, privileged DNS and security settings, and sensitive data exports require their designated owners.
- Do not rely on volunteers remembering to hide secrets in recordings, slide decks, or chat logs; use sanitized demonstration environments.

## Public release checklist

- [ ] Scope and all embedded assets reviewed for sensitive information.
- [ ] No passwords, keys, private URLs, identifying personnel details, or realistic personal records.
- [ ] No new public exposure created by diagrams, screenshots, document links, or issue comments.
- [ ] Automated document and secret-pattern checks pass.
- [ ] Functional owner reviews accuracy; security owner reviews any infrastructure or data-system material.
- [ ] Relevant Git history is reviewed before **migrating** or copying previously maintained documents.
- [ ] Any suspected prior exposure is reported privately; rotate/revoke impacted secrets and remediate history under the established response process.

## If a leak is suspected

1. Do **not** repeat the value in another issue or message.
2. Notify the designated private security channel/system owner and limit distribution.
3. Revoke or rotate compromised credentials, invalidate sessions if applicable, and assess affected data/systems.
4. Preserve minimal evidence privately, review Git history and forks, and decide whether history rewriting is warranted.
5. Publish a sanitized process improvement after containment, not an exploit recipe.

**Important:** scanning the current working tree does not prove past commits or downstream copies are safe. A full historical audit remains a separate security-owner task.

## Privacy and ministry data

Treat attendance, family, child/minor, health, giving, pastoral-care, and identity data as restricted. Never use real records in public examples, AI prompts, screenshots, or training demos. App authorization must be proven server-side; UI hiding is not sufficient.

See [access review](../templates/ACCESS-REVIEW.md), [incident report](../templates/INCIDENT-REPORT.md), and [governance](GOVERNANCE.md).
