# ARP (Address Resolution Protocol)

## Purpose
Maps IP addresses to MAC addresses on a local network segment so Layer 3 packets can be encapsulated into Layer 2 frames.

## Process
1. Host broadcasts: "Who has 192.168.1.5? Tell 192.168.1.10."
2. Owner of 192.168.1.5 replies with its MAC address.
3. Sender caches the result in its ARP table for a limited time.

## Operational Notes
- Gratuitous ARP announces a device’s own MAC/IP mapping, useful for failover.
- ARP tables can be viewed with `arp -a`, `ip neigh`, or switch CLI equivalents.
- ARP spoofing/poisoning attacks impersonate MAC addresses; mitigations include dynamic ARP inspection and static entries on critical hosts.
