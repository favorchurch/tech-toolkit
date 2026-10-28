# Internet & Streaming Team Playbook

**Status: Provisional adaptation.** Based on the existing Internet Master SOP; all venue procedures, timings and configuration must be validated locally. The specialist [Internet Playbook](https://github.com/favorchurch/internet-playbook) owns current detailed Manila operational instructions.

## 1. Purpose and outcomes

Provide predictable connectivity, distribution, and livestream support so a campus can run services even when equipment, venue or upstream providers behave unexpectedly. Success means the service was supportable, the team knew its roles, and failures were handled through safe fallbacks.

## 2. Roles and shift structure

| Role | Responsibilities | Readiness needed |
| --- | --- | --- |
| Campus Tech Lead | Local capacity plan, equipment custodian, local incident owner and handover | Local inventory, backups, rehearsal evidence |
| Internet Captain | Calls the setup, go/no-go and packdown sequence, delegates monitoring and escalations | Can lead the approved runbook and run a simulated failure |
| Assistant Captain | Independently verifies readiness and can take over operations | Knows checklists, incident communications and shift handover |
| Network / Connectivity Operator | Tests and observes the network; follows approved switching procedure | Identifies primary/back-up status without privileged changes |
| Stream Operator | Verifies audio/video feed, stream destination, start/stop and monitoring | Runs authorized streaming checklist |
| Troubleshooter / Runner | Collects evidence and isolates a failure safely | Knows escalation limits, cable/power safety and communication |
| Setup / Packdown Team | Physical setup, labels, cable runs, inventory, reset | Demonstrates safe handling and end-of-service check |
| Accessibility / Special Operations Support | Optional roles for captioning, interpretation or special streams | Trained on assigned tool and clear owner boundary |

Smaller teams may combine low-risk roles, but the Captain cannot skip independent checks when a live-stream cutover or critical change requires a second person.

## 3. Standard flow

~~~mermaid
flowchart LR
  A[Receive event and venue plan] --> B[Inspect equipment and staffing]
  B --> C[Build and label physical network]
  C --> D[Verify connectivity and stream]
  D --> E{Mandatory checks pass?}
  E -- No --> F[Use approved fallback or no-go escalation]
  E -- Yes --> G[Service monitoring]
  G --> H[Incident response and handovers]
  H --> I[Controlled packdown and inventory]
  I --> J[Debrief, update and retrain]
~~~

## 4. SOPs and reusable checklists

- [Sunday and event service SOP](SUNDAY-SERVICE.md): preflight, service, transitions, packdown.
- [Incident response playbooks](INCIDENTS.md): connectivity, stream, local network and power failures.
- [Equipment and tool requirements](EQUIPMENT.md): a vendor-neutral bill of materials and serviceability standard.
- [Campus survey](../../launch/CAMPUS-SURVEY.md), [certification](../../launch/CERTIFICATION.md), and [incident form](../../templates/INCIDENT-REPORT.md).

## 5. Volunteer onboarding

A typical path from the existing team: interest and availability → conversation with the Captain → shadow a service → one supervised shift → documented competency demonstration → approved independent roster. A volunteer should not gain administrator privileges simply by completing a rostered shift.

## 6. Quality standard

At minimum, before admitting the campus to Assisted Launch:
- Named Captain and backup, approved communication path, full setup/packdown roster.
- Site safety and cable-run plan.
- Tested service-critical network and stream paths; recording of results.
- Approved degraded-service fallback and a way to notify Production.
- Inventoried and labeled equipment; sufficient replacement consumables.
- Training and evidence for safe escalation; no live passwords in public materials.

**Thresholds and times:** actual preflight deadlines, minimum acceptable bandwidth, platform destination visibility, and service hours are set in the restricted campus event profile. No number in an older Manila SOP becomes a global standard automatically.

## 7. Boundary with Production

Production owns program signal quality and on-stage decisions; Internet owns approved connectivity and delivery paths unless a local responsibility agreement says otherwise. Any emergency switch of the program feed must be coordinated through the agreed on-duty lead. Never independently modify unrelated production feeds.

## 8. Common failure patterns

Use the [incident decision tree](INCIDENTS.md) when primary internet is unavailable, Wi-Fi is degraded, the stream fails at a provider, a local distribution link goes down, or power becomes unsafe. Record both the **symptom** and the **customer/ministry impact**, not just the equipment that seemed broken.

## 9. Required local addendum (not public)

Venue map, known-good equipment firmware, asset identifiers, protected settings, approved channel details, contact tree, vendor SLAs, contingency routes, restricted recovery instructions and vault-record references.

## 10. Training assessment

An operator passes only after they can demonstrate setup, monitoring, one controlled failure scenario, correct communications, and safe packdown with a qualified observer. See [training](../../training/README.md).
