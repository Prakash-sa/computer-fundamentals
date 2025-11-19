# Switching

## Core Functions
- Forward frames based on MAC address tables learned dynamically.
- Break collision domains, enabling full-duplex communication on each port.
- Provide VLAN segmentation, QoS classification, and port mirroring for monitoring.
- Run Spanning Tree Protocol (STP/RSTP/MSTP) to prevent loops.

## Advanced Capabilities
- **Link Aggregation (LACP):** Bundles multiple links into a single logical channel for throughput and redundancy.
- **Port Security:** Limits learned MAC addresses per port; useful for preventing rogue devices.
- **Power over Ethernet (PoE):** Supplies DC power to phones, access points, and cameras.
- **Multicast Management:** IGMP/MLD snooping ensures multicast traffic only goes where needed.
- **VXLAN/EVPN:** Modern data center switches support overlays for multi-tenant segmentation.

## Troubleshooting and Best Practices
- Monitor `show mac address-table` for flapping MACs indicating loops.
- Use BPDU Guard, Root Guard, and Loop Guard to protect STP topology.
- Implement storm control to limit broadcast/multicast storms.
- Document VLAN assignments and trunk allowed lists to avoid misconfigurations.

## Interview Questions
- *"How does STP prevent loops?"* — Elects a root bridge, blocks redundant links, re-calculates when topology changes.
- *"Difference between access and trunk ports?"* — Access carries a single VLAN; trunk carries multiple VLANs tagged via 802.1Q.
- *"Why use Layer 3 switching?"* — Provides wire-speed inter-VLAN routing without a separate router.
- *"What is CAM table exhaustion?"* — Attack or misconfiguration causing switches to flood frames, mitigated by port security and monitoring.
