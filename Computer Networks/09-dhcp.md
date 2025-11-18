# DHCP (Dynamic Host Configuration Protocol)

## DORA Exchange
1. **Discover:** Client broadcasts to locate a DHCP server.
2. **Offer:** Server proposes an IP configuration (address, lease time, options).
3. **Request:** Client requests the offered configuration.
4. **Acknowledge:** Server finalizes the lease and records the assignment.

## What DHCP Provides
- IP address and subnet mask
- Default gateway and DNS servers
- Optional settings: NTP servers, domain search suffixes, PXE boot info, VoIP VLAN IDs

## Operational Notes
- Clients renew leases at T1 (50% of lease time) and T2 (87.5%) to avoid address conflicts.
- DHCP relay (IP helper) forwards client broadcasts across networks to centralized servers.
- Reservations can guarantee the same IP for a MAC address, useful for printers or appliances.
