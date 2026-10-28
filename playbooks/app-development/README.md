# App Development Team Playbook

**Status: Provisional cross-repository standard.** Real commands and integration contracts remain owned by each app repository. This is an operating model for centrally governed engineering serving multiple campuses.

## Purpose

Build, maintain and responsibly retire digital systems that enable church ministry. Favor environments include web apps, Rock RMS integrations, check-in, events/ticketing, dashboards, authentication, and operations software. A successful release is **safe, reviewed, observable, supportable and reversible** — not merely code that compiles.

## Role and responsibility model

| Role | Accountable for |
| --- | --- |
| Product / ministry owner | Problem, users, priority, value and acceptance criteria |
| Campus requester / tester | Local requirements, representative usability tests, first-line defect evidence |
| Engineering Lead | Architecture, standards, prioritization and release ownership |
| Implementing developer or agent | Scoped code, docs, tests, evidence and PR |
| Independent reviewer | Verify exact final change and acceptance criteria against source |
| Data / security owner | Rock/other data authorization, sensitive-person records, integration scopes |
| Operations / system owner | Production health, deployment permissions, rollback, alerts and incident actions |

AI agents can implement and review under delegated controls, but cannot replace accountable human authorization for material risk, high-impact production access or an irreversible data operation.

## Source of truth

- **GitHub issue/spec**: implementation scope, decisions, acceptance tests and technical progress.
- **Repository README and code**: actual current behavior, commands, integration contracts and deploy paths.
- **Basecamp / department tracker**: requester collaboration, nontechnical approvals and business coordination, as applicable.
- **Central platform and security policies**: data classification, scopes, account authority and access control.
- **This toolkit**: cross-repo lifecycle, documentation and release quality standard.

Avoid copying source code or environment details into the public toolkit.

## Delivery flow

~~~mermaid
flowchart LR
  A[Issue and ministry outcome] --> B[Classify risk and clarify decisions]
  B --> C[Plan, split and assign]
  C --> D[Implement with targeted tests]
  D --> E[PR and independent review]
  E --> F{Release gates pass?}
  F -- No --> D
  F -- Yes --> G[Authorized deploy]
  G --> H[Smoke test and monitor]
  H --> I[Close issue and update docs]
~~~

## Core SOPs

- [Issue-to-production delivery](DELIVERY.md)
- [Engineering standards and release QA](QUALITY.md)
- [Production support, incident and rollback](OPERATIONS.md)
- [Project brief](../../templates/PROJECT-BRIEF.md) and [change request](../../templates/CHANGE-REQUEST.md)
- [Training pathway](../../training/README.md) and [campus launch](../../launch/README.md)

## Interfaces

A campus generally **requests and tests** shared apps, while Central Tech **implements and releases** them. Local independent development is possible only within a delegated sandbox and approved deployment contract; shared identity, sensitive data, payment and church-wide systems remain under their system owners.

## Definition of ready and done

**Ready:** problem, impact, owner, scope, risks, decision record, testable acceptance criteria and data permissions specified.

**Done:** required tests passed on the final version, independent final-change review completed, release owner approved, deployed state verified, relevant smoke tests observed, rollback documented, incident/monitoring owner assigned, and issue/doc records updated.

## Training

New contributors start with nonproduction sample data and a repository-specific tutorial. An independent release privilege is assigned by demonstrated competency and system owner approval, never only by experience or AI-assistant use.
