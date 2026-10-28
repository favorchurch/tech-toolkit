# Internet incident and fallback playbooks

**Scope:** safe triage and communication. Specific provider controls, router settings, wireless management, admin URLs and exact stream identifiers belong in restricted runbooks.

## Universal incident protocol

1. **Protect people:** address unsafe electrical/cable or physical conditions first.
2. **State impact:** which services, streams, rooms or users are affected; which are unaffected.
3. **Select severity:** is there a complete service-critical outage, a degraded service, or a noncritical fault? Record owner and time.
4. **Confirm observation:** check from an independent device/viewpoint before declaring restored.
5. **Use preapproved fallback only.** If unavailable or unauthorized, escalate to the Captain/Lead.
6. **Communicate:** what users will notice, what is being done, who decides the next transition.
7. **Recover and verify:** prove end-to-end service; record when the issue stopped.
8. **Debrief:** identify a preventive action and update the equipment or runbook owner.

## Decision tree

~~~mermaid
flowchart TD
  A[Service impact reported] --> B{Physical safety issue?}
  B -- Yes --> C[Stop affected setup; contact authorized venue and Tech leads]
  B -- No --> D{Is remote viewer / user impact confirmed?}
  D -- No --> E[Monitor and log; verify independent path]
  D -- Yes --> F{Approved fallback tested and available?}
  F -- Yes --> G[Captain coordinates switch with Production]
  F -- No --> H[Escalate; communicate degraded or paused service]
  G --> I[Verify end to end; monitor]
  H --> I
  I --> J[Record evidence and follow-up]
~~~

## A. Primary uplink unavailable

**Observe:** approved monitoring path plus a second test device. Distinguish venue LAN issues from upstream provider failure.

**Action:** identify unaffected critical endpoints; notify the Captain; use the **documented** alternate uplink only when the approved operator confirms routing and it will not violate network segmentation. Confirm viewer output and dependent apps afterward.

**Do not:** reconfigure firewalls, bridge protected networks, expose mobile hotspots as unmanaged infrastructure, or guess credentials during service.

**Evidence:** impact start/end, affected paths, authorized switch, viewed output after switch.

## B. Slow Wi-Fi or network zone

**Observe:** scope (one device, zone, SSID class, or all connections), application behavior and whether wired paths also fail.

**Action:** reduce noncritical traffic only through approved controls; prioritize ministry-critical functions using the local runbook; relocate clients safely; escalate if infrastructure settings are required.

**Do not:** publish real SSIDs, private monitoring dashboard URLs or internal access-point maps in public incidents.

## C. Encoder, destination or livestream interruption

**Observe:** program signal, encoder output, distribution/provider status and public/unlisted viewer test separately. A platform dashboard alone is not end-to-end proof.

**Action:** coordinate stream status with Production and authorized platform operator; perform approved restart/failover; announce viewer impact as applicable; observe stable output before closing.

**Do not:** change stream credentials, audience visibility or public metadata without platform-owner approval.

## D. Local switch, cable, or room distribution outage

**Observe:** power and physical indicators, one affected segment vs campus-wide failure, trip hazards.

**Action:** use approved spare path/component with safe cable management. Keep a separate record of temporary bypasses and schedule permanent remediation.

**Do not:** insert unknown devices into protected segments or troubleshoot by disconnecting active safety-critical equipment.

## E. Power or equipment safety problem

**Action:** stop unsafe equipment, notify venue/Production, and use the approved continuity plan only if safe. Facility/electrical decisions are made by authorized personnel; a volunteer does not perform electrical repairs.

## Recovery closure

- [ ] Independent remote check passes.
- [ ] Captain and affected team confirm restored capability.
- [ ] Temporary bypasses are identified and assigned an expiry/removal owner.
- [ ] [Incident report](../../templates/INCIDENT-REPORT.md) completed with redacted evidence.
- [ ] Root cause remains **unknown** unless actually supported; next investigation owner identified.
