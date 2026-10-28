# Governance and document ownership

**Decision:** distributed ownership with centrally governed standards.

## Sources of truth

| Artifact | Canonical owner/location | Other copies |
| --- | --- | --- |
| Master roles, policy, launch stages, certification standard | This public toolkit, Central Tech | Slides, PDFs, and onboarding decks are generated views or teaching aids |
| Detailed Internet Sunday operations | Existing Internet Playbook repository, Internet Lead | This toolkit contains the portable overview and checklists only |
| Website workflow | Toolkit Website playbook, Website Lead | Campus-specific request systems and design assets are referenced, not duplicated |
| Cross-application engineering lifecycle | Toolkit App Development playbook, Engineering Lead | Individual repo READMEs own build commands, integration specifics, and tests |
| System and service configuration | The owning system's authorized private config management | Public docs only identify what category of record exists |
| Campus roster, site details, local recovery contacts | Campus-controlled private addendum, Campus Tech Lead | Public repo receives only sanitized examples |
| Live credentials / tokens | Approved enterprise credential vault, system owner | Never in Markdown, slides, tickets, screenshots, or Git history |
| Readiness evidence and certification decisions | Designated restricted evidence register, Central Tech certifier | Public forms are blank reusable templates |

## Change authority

| Change type | Proposes | Approves | Minimum validation |
| --- | --- | --- | --- |
| Typo or clarification with no operational impact | Any contributor | Functional lead or delegate | Link and content check |
| Local venue/Sunday setup change | Campus Tech Lead | Internet Lead or delegated local authority within standards | Rehearsal or known-good comparison |
| Public website content | Requester/editor | Designated content/brand owner plus authorized publisher | Mobile/desktop QA; content approval |
| Global SOP, security, shared release process | Functional Lead | Central Tech designated approver | Cross-campus impact and security review |
| Production app change | Engineering contributor | Authorized release owner under repo-specific gates | Tests, independent review, release/rollback checks |
| Secret, privileged access, or infrastructure identity | System owner | Designated security/administrative authority | Authorized private change; never published |

## Review cadence

- **Quarterly** owner attestations on playbooks and launch templates.
- **Immediately** after a major incident, significant system migration, a newly approved capability, or an actual safety/security change.
- **Before every campus launch** verify the selected guides against the site environment and record a dated sign-off.
- Mark stale sections clearly. Never silently copy historical service schedules, endpoint configurations, or prices forward.

## Contribution workflow

~~~mermaid
flowchart LR
  A[Identify gap] --> B[Open scoped issue or change request]
  B --> C[Owner drafts update]
  C --> D{Public-safe and portable?}
  D -- No --> E[Private addendum or vault process]
  D -- Yes --> F[PR plus evidence]
  F --> G[Lead review and automated checks]
  G --> H[Publish and notify affected campuses]
  H --> I[Update training and readiness templates]
~~~

## Quality of evidence

An instruction is **Verified** when the functional owner recently observed or tested it in a representative environment. It is **Provisional** when derived from existing source documentation but not yet field-tested. It is **Proposed** when created as a reusable default. It is **Deprecated** when superseded and should not be followed. These labels must be applied to high-risk procedures; a merged documentation PR does not automatically become a verified operating practice.

## How campuses propose variation

A campus can suggest a global improvement through a PR. Local-only details stay in restricted addenda. If a site cannot meet a mandatory safety or security gate, the issue must be escalated to the global standard owner rather than edited out locally.

## Continuing ownership

A lead leaving the role must transfer sources, access requests, outstanding incidents, document review dates, and training responsibility using the [handover template](../templates/TEAM-HANDOVER.md). Document custody is not the same as possessing credentials.
