# Networking Devices

## Modem
- Converts digital signals to analog (and back) for DSL, cable, or fiber services.
- Can be standalone or integrated with routers/firewalls provided by ISPs.

## Router
- Operates at Layer 3, selecting next hops using routing tables and protocols.
- Performs NAT/PAT, firewalling, VPN termination, DHCP, and QoS in branch deployments.
- Interview Q: *"Difference between router and default gateway?"* — the gateway is the router IP configured on hosts.

## Switch
- Layer 2 device building MAC address tables to forward frames per port.
- Supports VLANs, trunking (802.1Q), PoE, STP/RSTP, QoS, port mirroring, and sometimes Layer 3 routing.
- Interview Q: *"How does a switch learn MAC addresses?"* — inspects source MAC of incoming frames and associates it with the ingress port.

## Hub
- Multiport repeater broadcasting every bit to all ports; creates one collision domain.
- Rare today but still referenced in CCNA/ITF+ fundamentals.

## Access Point
- Bridges wireless clients to the wired network; handles authentication (802.1X), roaming, and RF optimization.

## Firewall/UTM
- Filters traffic based on rules; modern appliances incorporate IDS/IPS, anti-malware, and SSL decryption.

## Load Balancer / ADC
- Distributes traffic across multiple servers at L4/L7, offloading TLS and providing health checks.

## Interview Cheat Sheet
- *"What is the function of a Layer 3 switch?"* — Combines switching and routing, often used for inter-VLAN routing.
- *"Why use a gateway instead of connecting directly to the Internet?"* — Enforces security, NATs private IPs, and provides policy control.
