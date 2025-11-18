# Networking Troubleshooting Flow

1. **Check physical connections:** Verify power, cabling, Wi-Fi status, and link lights.
2. **Inspect IP configuration:** Use `ipconfig`, `ifconfig`, or `ip addr` to confirm addresses, masks, and gateways.
3. **Ping the default gateway:** Ensures local subnet connectivity.
4. **Ping a known external IP (e.g., 8.8.8.8):** Confirms upstream routing and ISP reachability.
5. **Ping a domain name:** Differentiates DNS issues from general connectivity problems.
6. **Traceroute:** Identifies where along the path packets drop or latency spikes.
7. **Review ARP tables:** Detect incorrect MAC entries or duplicate IPs.
8. **Check firewall rules/logs:** Ensure traffic isn’t blocked intentionally.
9. **Examine application logs:** Determine whether the issue is network-related or specific to the service.

## Tips
- Document findings at each step to speed handoffs.
- Automate recurring diagnostics with scripts or observability tools.
- For intermittent issues, capture packets with Wireshark/tcpdump to correlate with timestamps.
