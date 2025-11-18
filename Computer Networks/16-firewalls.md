# Firewalls

## Types of Firewalls
- **Packet filtering:** Examines headers (IP, port, protocol) and applies stateless rules.
- **Stateful inspection:** Tracks connection state to allow legitimate return traffic automatically.
- **Application-level (proxy):** Understands protocols like HTTP/FTP to enforce granular policies.
- **Next-generation firewalls (NGFW):** Combine stateful inspection with intrusion prevention, SSL inspection, and user identity awareness.

## Core Functions
- Enforce segmentation and least privilege between network zones.
- Provide NAT/PAT, VPN termination, and traffic logging.
- Detect anomalies via IDS/IPS signatures or behavioral analytics.

## Best Practices
- Use default-deny policies and explicitly permit required flows.
- Keep firmware updated and monitor logs/SIEM alerts.
- Implement high-availability pairs or cloud firewalls to avoid single points of failure.
