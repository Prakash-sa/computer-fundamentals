# ARP (Address Resolution Protocol)

## Purpose
ARP maps IPv4 addresses to MAC addresses within a local broadcast domain, enabling Layer 3 packets to be encapsulated into Layer 2 frames.

## Resolution Workflow
1. Host checks its ARP cache for the destination IP.
2. If absent, it broadcasts `Who has 192.168.1.5? Tell 192.168.1.10`.
3. Owner of the IP replies with its MAC address.
4. The sender updates its ARP table and transmits the packet using that MAC as the destination in the Ethernet frame.

## Variants and Features
- **Gratuitous ARP:** Host announces its IP/MAC mapping without being asked; used during failover (VRRP/HSRP) to update switches.
- **Proxy ARP:** Router answers ARP requests on behalf of another device, enabling connectivity across subnets without reconfiguring hosts.
- **Reverse ARP (RARP):** Legacy protocol where a device with known MAC requests its IP; replaced by BOOTP/DHCP.

## Security Concerns
- ARP spoofing/poisoning can redirect traffic or perform man-in-the-middle attacks by responding with malicious MAC addresses.
- Mitigations: Dynamic ARP Inspection (DAI), DHCP snooping, static ARP entries on critical servers, port security.

## Interview Questions
- *"Is ARP used in IPv6?"* — No; IPv6 uses Neighbor Discovery (ND) and Neighbor Solicitation/Advertisement messages.
- *"How do you clear the ARP cache?"* — `arp -d` on Windows, `ip neigh flush` on Linux, or device-specific commands.
- *"What happens if ARP fails?"* — Packets cannot be delivered on the LAN; ping shows unresolved ARP entries or timeouts.
