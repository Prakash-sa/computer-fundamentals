# DHCP (Dynamic Host Configuration Protocol)

## DORA Process
1. **Discover:** Client broadcasts `DHCPDISCOVER` to UDP/67 seeking available servers.
2. **Offer:** Server responds with `DHCPOFFER` containing proposed IP, lease time, and options.
3. **Request:** Client broadcasts `DHCPREQUEST` accepting the offer (or renewing existing lease).
4. **Acknowledge:** Server sends `DHCPACK`, finalizing the lease and storing the client MAC/IP binding.

## What DHCP Delivers
- IP address, subnet mask, default gateway
- DNS/NTP servers, domain search suffix, MTU, TFTP/PXE boot options, VoIP VLAN IDs
- Lease duration plus renewal timers T1 (50%) and T2 (87.5%)

## Operational Concepts
- **Reservations:** Bind a MAC address to a predictable IP without static configuration on the device.
- **Relay Agent (IP Helper):** Forwards DHCP messages across L3 boundaries to centralized servers.
- **Failover:** Active/standby or load-sharing pairs share lease databases for high availability.
- **Options 82/60:** Provide circuit-ID and vendor class for ISP-managed broadband deployments.

## Troubleshooting Checklist
- Ensure DHCP scope has free addresses; exhaustion is common.
- Verify VLANs and trunking so broadcasts reach the relay/server.
- Capture packets with `tcpdump -i eth0 port 67 or port 68` to observe DORA.
- On clients, `ipconfig /renew` or `dhclient -r` resets leases.

## Interview Prep
- *"How does DHCP know which pool to use?"* — Based on the server interface or helper address receiving the request.
- *"What happens if two DHCP servers respond?"* — Client accepts the first ACK; reason to coordinate scopes carefully.
- *"How do you provide IPs to VoIP phones needing a voice VLAN?"* — Use Option 43/129 or LLDP-MED to signal VLAN assignment.
