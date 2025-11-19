# Networking Troubleshooting Flow

## Stepwise Methodology
1. **Physical Layer:** Verify power, cabling, link LEDs, and port status. Replace suspect cables or optics.
2. **Interface Configuration:** Check IP addressing, subnet mask, gateway, and duplex/speed settings (`ipconfig`, `ip addr`, `show interface`).
3. **Local Connectivity:** Ping loopback and default gateway; inspect ARP cache for expected MAC addresses.
4. **External Reachability:** Ping known public IPs (8.8.8.8) and run `traceroute` to locate failures.
5. **Name Resolution:** Test DNS lookups (`nslookup`, `dig`). If IP ping works but DNS fails, focus on resolver settings.
6. **Firewall/ACL Review:** Ensure security policies permit desired traffic; examine logs for drops.
7. **Application Layer:** Check service status, logs, and metrics; confirm ports are listening (`netstat`, `ss`).
8. **Performance Analysis:** Capture packets (Wireshark/tcpdump) to analyze latency, retransmissions, or drops.
9. **Escalation & Documentation:** Record findings, timestamps, and remediation steps for team hand-offs.

## Interview Talking Points
- Describe the OSI-layered approach to troubleshooting; start at Layer 1 and move upward.
- Mention tools: `ping`, `traceroute`, `mtr`, `pathping`, `iperf`, SNMP, and flow telemetry.
- Explain how to diagnose intermittent issues using monitoring systems and packet captures.
- Discuss war stories (e.g., duplex mismatch, DNS misconfiguration) to demonstrate practical experience.

## Tips & Tricks
- Automate health checks with scripts or network monitoring systems (Nagios, Zabbix, NetBox webhook automations).
- Maintain runbooks for recurring incidents; update after every postmortem.
- Use change management to correlate outages with recent deployments.
