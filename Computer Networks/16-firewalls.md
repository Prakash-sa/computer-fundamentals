# Firewalls

## Firewall Types
- **Packet Filtering:** Stateless inspection of source/destination IP, port, and protocol; fast but limited context.
- **Stateful Inspection:** Tracks connection state (TCP flags, sessions) to allow return traffic automatically.
- **Application/Proxy:** Terminates connections and understands protocols like HTTP/FTP for granular control.
- **Next-Generation Firewall (NGFW):** Combines stateful inspection with IPS, SSL decryption, user identity, sandboxing, and threat intelligence feeds.
- **Cloud/Host Firewalls:** Security groups, NACLs, and host-based firewalls (iptables, Windows Defender Firewall) protect VMs and containers.

## Core Capabilities
- Segmentation between zones (LAN, DMZ, WAN, OT networks).
- NAT/PAT and VPN termination (IPsec, SSL VPN).
- Policy enforcement based on users, applications, geolocation, or time of day.
- Logging, alerting, and integration with SIEM/SOAR platforms.

## Best Practices
- Default-deny rule at end of policy; explicitly allow required flows.
- Regular policy reviews to remove stale rules and minimize attack surface.
- High availability pairs with state sync to avoid outages.
- Keep firmware up to date and leverage threat feeds for real-time protection.

## Interview-Ready Answers
- *"Difference between stateless and stateful firewall?"* — Stateless inspects each packet independently; stateful tracks sessions.
- *"What is a DMZ?"* — A semi-trusted network segment hosting public-facing services separated from internal LAN.
- *"How do you allow remote workers securely?"* — Implement VPNs or zero-trust access with MFA, split tunneling policies, and endpoint posture checks.
- *"Explain UTM vs NGFW."* — UTM (Unified Threat Management) was the earlier term for multi-function devices; NGFW emphasizes application awareness and advanced features.

## Troubleshooting Tips
- Use packet captures/diagnostic commands (`show session`, `show conn`) to confirm rule hits.
- Check NAT translations when flows fail; asymmetry often indicates NAT or routing issues.
- Monitor CPU/memory to ensure inspection engines are not overloaded, which can cause latency.
