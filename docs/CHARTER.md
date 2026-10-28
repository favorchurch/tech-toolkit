# Department overview, vision and organizational roles

## Purpose

Favor Tech equips ministry through reliable connectivity, thoughtful digital experiences, and secure, maintainable systems. Our aim is to help campuses reach and serve people well with technology, without making local ministry hostage to a single specialist or location.

The 2026 Tech volunteer onboarding material expresses the team's ethos through **Serve, Share, Shape**. We translate that into three habits: serve people first; share knowledge and train successors; shape better systems rather than hoarding know-how.

## What good looks like

- **Reliable ministry:** systems work at the moment people need them.
- **Clear ownership:** a named accountable role exists for normal operations, incidents, and changes.
- **Safe access:** least privilege, supervised progression, and recovery readiness.
- **Multiplication:** a new volunteer or campus learns a documented process and demonstrates competence.
- **Continuous improvement:** incidents, volunteer feedback, and platform changes flow back into the guide.

## Organizational structure

~~~mermaid
flowchart TD
  CT[Central Tech Leadership] --> IL[Internet Lead]
  CT --> WL[Website Lead]
  CT --> EL[Engineering Lead]
  CT --> SO[Shared Data and Security Owners]
  IL -. standards and mentoring .-> CL[Campus Tech Lead]
  WL -. standards and mentoring .-> CL
  EL -. shared applications and support .-> CL
  CL --> IC[Internet Captains and Volunteers]
  CL --> WE[Authorized Website Editors]
  CL --> LO[Local App Requesters and Testers]
~~~

The diagram describes **responsibility**, not an HR reporting line. A person may cover multiple roles in a smaller campus; independent approval gates still need an appropriately authorized reviewer.

## Role charter

| Role | Owns | Must not assume |
| --- | --- | --- |
| Central Tech Leadership | Organization-wide standards, risk acceptance, cross-campus architecture, certification | Responsibility for every routine local task |
| Internet Lead | Reusable network/stream playbooks, training, equipment standards | Authority to publish secrets or override venue safety |
| Website Lead | Publishing process, CMS practices, QA and release checklists | Automatic permission to alter all DNS and security settings |
| Engineering Lead | Technical standards, testing, app releases, incident engineering | Unreviewed changes to shared or sensitive systems |
| Data / Security Owner | Information classification, privileged access, data-handling rules | Public release of operational secrets |
| Campus Tech Lead | Local rosters, asset custody, rehearsals, live-service readiness | Authority to change global platform policy |
| Internet Captain | Service start/stop decisions, safety checks, first response | Privileged infrastructure changes beyond delegated runbooks |
| Volunteer / Editor / Developer | Defined tasks within documented access | Production approval merely by being technically capable |

## Working agreements

1. A safe fallback is better than an improvised unapproved production change.
2. Volunteers should know their first escalation point before their first independent shift.
3. Campus-specific variation is documented as an addendum; the master standard is not silently forked.
4. Resolve conflicts between instructions by consulting the current system owner.
5. Treat checklists as evidence of performed checks, not as boxes to tick afterward.

## Interfaces with other teams

- **Production and service operations:** agree signal paths, streaming schedule, venue and handover boundaries before event day.
- **Creative and marketing:** approve public-facing brand, copy and design before website implementation.
- **Database and pastoral systems:** review data classifications, permissions, and Rock-connected integrations.
- **Events / hospitality / kids:** collect requirements and ensure published forms, registration and check-in workflows are tested.
