# Internet Service SOP — reusable checklist

**Status:** Proposed portable framework. Apply alongside the current [Internet Master SOP](https://github.com/favorchurch/internet-playbook) and a privately approved local service profile.

## Pre-event planning (before service day)

- [ ] Confirm venue and service times with the service/event coordinator.
- [ ] Confirm responsibility boundary with Production and stream/destination owners.
- [ ] Assign Captain, backup Captain, connectivity operator, stream operator and packdown.
- [ ] Review expected audience/devices and any special streams, multilingual feeds or uploads.
- [ ] Verify approved Internet options, data plans/quotas and venue restrictions privately.
- [ ] Review equipment inventory, batteries/power, spares, cable protection and safety.
- [ ] Review previous open incidents and changes since last successful service.
- [ ] Establish a non-secret incident and escalation contact method.

## Setup and preflight

1. Captain calls shift check-in and confirms the event profile; don't reuse another venue's channel/destination settings.
2. Verify power, safe cable placement and physical readiness.
3. Assemble approved physical topology according to the restricted site plan; do not improvise unmanaged uplinks into sensitive networks.
4. Independently confirm approved primary and fallback connectivity are present.
5. Test DNS and representative app/network availability using the approved test endpoints.
6. Validate stream **end-to-end** from permitted source through encoder/distribution to the actual viewing destination; a green local encoder light is not sufficient.
7. Observe representative audio, video, synchronization and captioning/interpretation where required.
8. Confirm expected stream visibility and metadata with the authorized publishing/production operator.
9. Record quality indicators and any deviations in the [service log](../../templates/SERVICE-LOG.md).
10. Captain and designated reviewer give go/no-go confirmation. If a mandatory gate fails, escalate; do not check it off without evidence.

## During the service

- [ ] Assign active operator(s) to watch remote output, not merely local hardware.
- [ ] Log degradations, stream interruptions, provider notices and fallback transitions.
- [ ] Communicate directly with Production before a change that may interrupt viewers.
- [ ] Keep uplink/stream parameters under approved change authority.
- [ ] At each service or operator transition, confirm the next stream destination and feed ownership.
- [ ] Maintain incident evidence without capturing tokens, personal data or privileged URLs.
- [ ] Escalate missed critical gates according to [incident playbooks](INCIDENTS.md).

## Packdown

- [ ] Obtain Production/event authorization for stream and network shutdown.
- [ ] Verify all intended streams finished; no unintended public feed remains active.
- [ ] De-energize devices using the approved safe shutdown sequence.
- [ ] Recover, coil and count cables, adapters, power supplies and borrowed gear.
- [ ] Compare actual count with the private inventory; report loss/damage immediately.
- [ ] Confirm the venue is restored and any public/temporary equipment has been removed.
- [ ] Captain files the final service log and follow-ups.

## Stop conditions

Unsafe power/cables; unauthorized change to shared network; inability to verify the viewer feed; missing critical owner; exposed credentials; unexplained access to sensitive data; untested or unreliable fallback when the event requires one. Escalate before proceeding.

## Service completion evidence

Date/event identifier (no protected attendee data), campus role on duty, checklist revision, streaming status, failover result, incident IDs, packdown custody, and a short debrief with next owner.
