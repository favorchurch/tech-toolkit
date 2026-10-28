# Contributing to the Favor Tech Toolkit

We welcome portable improvements from campus operators, volunteers, engineers, and other churches. Please keep this repository reusable and safe for public sharing.

## Before proposing a change

1. Search the existing guide and open issues for the same problem.
2. Decide whether the proposed information is **public-safe**. If it contains live configurations, identities, security details or credentials, use an authorized private channel instead.
3. Identify the functional owner from [governance](docs/GOVERNANCE.md).
4. Open a focused issue or PR describing the operator problem, current behavior, proposed change and evidence (redacted).

## Pull request checklist

- [ ] Only portable, non-sensitive content.
- [ ] Describes the outcome and its responsible role, not just tool clicks.
- [ ] Includes a positive completion check and a stop/escalation condition.
- [ ] Does not claim a test or certification happened unless evidence is recorded.
- [ ] Uses relative links for this repository; external sources are approved and classified.
- [ ] Maintains the source-of-truth boundary: do not copy per-app READMEs or private campus addenda.
- [ ] Run the local validation script and obtain the appropriate functional-lead review.

### Writing conventions

- Use concise headings, ordered steps, short checklists and explicit role names.
- Prefer vendor-neutral instructions where functionality is portable.
- Label unverified estimates as **Proposed**, not established policy.
- Use placeholders instead of real names, addresses, IPs, SSIDs, passwords or contact details.
- Explain failure behavior and safe rollback with every operationally impactful procedure.
- Add a dated owner review entry when changing a critical SOP.

## Review and publication

Public docs can be contributed widely, but only authorized lead maintainers should approve normative changes. For security issues, **do not** disclose exploitation detail in a public GitHub issue. Follow the private escalation method in [security](docs/SECURITY.md).

This repository has a permissive MIT license; existing brand logos and media are not automatically included.
