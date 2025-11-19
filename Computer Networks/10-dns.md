# DNS (Domain Name System)

## Purpose
DNS translates human-friendly hostnames into IP addresses so clients can locate services.

## Hierarchy Recap
1. **Root servers** direct queries to TLD servers.
2. **TLD servers** know authoritative name servers for domains like `.com`, `.org`, `.io`.
3. **Authoritative servers** hold zone files for `example.com` and subdomains.
4. **Recursive resolvers** (ISP, corporate, public) cache answers for clients.

## Common Record Types
- `A` / `AAAA`: IPv4 / IPv6 address mappings.
- `CNAME`: Alias pointing to another canonical name.
- `MX`: Mail exchange records prioritized by preference values.
- `NS`: Authoritative name servers for a zone.
- `TXT`: Arbitrary text; used for SPF, DKIM, ownership verification.
- `SRV`: Service location (e.g., `_sip._tcp`).
- `PTR`: Reverse DNS mapping IP → name.

## Query Flow
1. Browser/OS cache lookup.
2. Local resolver query (router, ISP).
3. If miss, recursive resolver contacts root → TLD → authoritative server.
4. Response cached per record TTL to reduce latency.

## Security Enhancements
- **DNSSEC:** Adds digital signatures to prove authenticity, preventing cache poisoning.
- **DoH/DoT:** Encrypts DNS queries over HTTPS/TLS to prevent eavesdropping.
- **Split-horizon DNS:** Provides different answers internally vs externally.

## Troubleshooting Tools
- `nslookup`, `dig`, `host` for manual queries.
- `whois` for registration info.
- Packet captures to inspect recursion or verify EDNS(0) behavior.

## Sample Interview Questions
- *"Difference between iterative and recursive queries?"* — Recursive resolver handles the full lookup; iterative returns referrals for the client to query next server.
- *"How do CDNs use DNS?"* — Provide geolocated answers (Anycast, GeoDNS) to direct users to the closest edge cache.
- *"Why might a DNS change not take effect immediately?"* — Cached responses respect previous TTL values, requiring propagation time.
