# Internet equipment and tool requirements

**Status:** portable capacity-planning guide. Models, prices, quantities and layout require site survey and owner approval; do not guess required bandwidth from attendance alone.

## Equipment categories

| Category | Required capability | What to verify |
| --- | --- | --- |
| Connectivity | Approved primary WAN; fallback when a critical ministry function depends on it | Provider availability, expected capacity, latency/jitter under load, restrictions, support route |
| Routing/firewall | Segregate approved traffic classes and manage failover | Config custody, update policy, recovery and backup access |
| Distribution | Safe switching and cabling to critical stations | Cable lengths, labels, spares, physical redundancy where appropriate |
| Wireless | Coverage and client support matching the floor plan | Site survey, interference, client limits, safe visitor access |
| Stream transport | Approved path for encoder/distribution and remote-viewer verification | End-to-end test, monitoring, dependency map |
| Power | Proper adapters, protected cable runs, approved backup power where needed | Venue safety, load budget, safe shutdown |
| Operations | Labeled cases, cable testers, adapters, basic monitoring, accessible checklists | Count at setup and packdown; maintenance ownership |
| Accessibility / special streams | Additional gear when captioning, interpreting, recording or auxiliary feeds are required | Agreement with Production, privacy and reliability |

## Sizing questions

1. Which services absolutely require live Internet? Which can work offline?
2. Is the venue permanently installed or rapidly deployed/packed down?
3. What is the expected number of concurrent wired/wireless users, and what traffic types dominate?
4. How many critical streaming endpoints and independent destinations exist?
5. What is the acceptable degraded mode and who may declare it?
6. What hazards, venue limitations, provider outages and climate/transport constraints exist?
7. Who owns asset custody, purchase approvals, spares and replacements?

## Standard equipment acceptance

- [ ] Equipment is approved, inventoried, labeled, physically safe and serviceable.
- [ ] Owner knows warranty/support and replacement process.
- [ ] Power and cable paths pass venue safety review.
- [ ] Compatibility tested with the actual stream/critical workflow.
- [ ] Configuration backed up in authorized private tooling.
- [ ] Backup plan is rehearsed for any service-critical single point of failure.

## Asset management

Use the [inventory CSV](../../templates/ASSET-INVENTORY.csv) for a blank example. Keep the completed inventory private if it includes precise locations, serial numbers, network interfaces, management details or contact information. A public bill of materials should list **equipment classes**, not exploitable asset details.

## Budgeting principles

List one-time purchase, transport/storage, consumables, subscriptions/data, warranty, power safety, lifecycle replacement and emergency spares separately. Obtain current, campus-specific quotes. Never publish a claimed universal purchase price or carrier service level without evidence.

## Retiring or transferring equipment

Confirm data/configuration sanitization, ownership sign-off, inventory change, and safe disposal. Remove confidential labels and stored secrets before donation or return.
