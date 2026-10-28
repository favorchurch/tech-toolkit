# Campus Launch & Replication Pack

**Decision 3: phased readiness.** A new campus progresses **Prepare → Assisted Launch → Certified Independent Operations**. This standard applies to Internet, Website and App Development support, with different scope and local staffing.

## Scope

The toolkit must work in permanent campuses, temporary venues and cross-campus events. A launch is not certified because one good service happened or because central staff fixed everything behind the scenes.

## Stage 1 — Prepare

**Owner:** Campus Tech Lead, with functional leads.

1. Complete [site and service survey](CAMPUS-SURVEY.md).
2. Define the local service package: critical connectivity, stream, publishing and app workflows.
3. Assign accountable local operators and Central Tech escalation owner.
4. Review venue safety, inventory, authorized access, data classification and fallback modes.
5. Train primary and backup operators with supervised practice.
6. Rehearse mandatory checks and record actual results in [readiness matrix](../templates/CAMPUS-READINESS.md).
7. Central Tech performs Prepare gate review.

**Exit:** essential controls pass; any unresolved noncritical risks have an accountable owner and accepted operating limitation. Critical failures block a live launch decision.

## Stage 2 — Assisted Launch

**Owner:** Campus Captain/local operators; Central Tech observes, coaches and takes only escalated or reserved actions.

1. Brief local operators and declare service critical paths.
2. Execute documented setup, website publishing responsibilities, and app-support routing under live conditions.
3. Run prescribed end-to-end checks, not just device status checks.
4. Record issues, external intervention, time-to-detect and outcomes.
5. Repeat with gradually less Central Tech intervention as readiness improves.
6. Hold structured debrief, update training, repair documentation and reassess.

**Exit:** local team demonstrates reliable routine service and safe incident escalation, with evidence rather than assumed competence. No fixed number of Sundays substitutes for demonstration.

## Stage 3 — Certified Independent Operations

**Owner:** Central Tech authorizes after functional-lead review.

- Primary and backup operators demonstrate required competencies.
- Local team reliably executes safe preflight, ongoing monitoring, shift handovers and packdown.
- At least one representative degraded-service scenario is safely rehearsed and verified.
- Authorized content publishing and app issue escalation work without routine Central Tech intervention.
- Current private addendum, access review, emergency contacts and evidence register exist.
- Remaining risks are accepted explicitly by the right owner; critical security or safety gaps cannot be accepted locally.

**Certificate:** record campus, scope (Internet/Website/App Support), assessed date, assessor, evidence IDs, restrictions, corrective actions and next review. Certification is scoped and revocable after material environment changes.

## Pathway

~~~mermaid
flowchart LR
  P[Prepare] --> G1{Mandatory checks clear?}
  G1 -- No --> P
  G1 -- Yes --> A[Assisted Launch]
  A --> G2{Demonstrated local competence?}
  G2 -- No --> A
  G2 -- Yes --> C[Certified]
  C --> M[Quarterly review and change-triggered recheck]
  M -->|Material change| P
~~~

## Supporting tools

- [Site survey](CAMPUS-SURVEY.md)
- [Evidence-based certification](CERTIFICATION.md)
- [Readiness matrix](../templates/CAMPUS-READINESS.md)
- [Asset inventory](../templates/ASSET-INVENTORY.csv)
- [Training](../training/README.md)
- [Incident report](../templates/INCIDENT-REPORT.md)

## Guardrails

Campus scope is never permission to control all global infrastructure. The authorized Central Tech owner remains responsible for shared platform security, releases, recovery and cross-campus impact. A private local operations addendum accompanies the public standards.
