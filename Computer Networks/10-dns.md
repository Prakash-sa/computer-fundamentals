# DNS (Domain Name System)

## Purpose
DNS translates human-readable names (e.g., `www.example.com`) into IP addresses so applications can connect to services.

## Hierarchy
1. **Root servers** know where each top-level domain (TLD) is hosted.
2. **TLD servers** handle domains like `.com`, `.net`, `.org`.
3. **Authoritative servers** store records for specific domains such as `google.com`.
4. **Subdomains** (e.g., `mail.google.com`) can delegate to additional authoritative servers.

## Record Types
- `A`: IPv4 address
- `AAAA`: IPv6 address
- `CNAME`: Alias pointing to another canonical name
- `MX`: Mail exchange records for SMTP routing
- `NS`: Authoritative name servers
- `TXT`, `SRV`, `CAA`: Additional metadata and service records

## Query Process
1. Browser checks its local cache.
2. Operating system cache.
3. Router or home gateway cache.
4. ISP recursive resolver.
5. Root → TLD → authoritative lookup if cache misses occur.

## Operational Considerations
- **TTL (time to live):** Controls caching duration; low TTLs speed up record changes but increase query volume.
- **Forward vs. reverse DNS:** Reverse lookups map IPs to names using PTR records.
- **Security:** DNSSEC adds authenticity, while DoH/DoT encrypts queries to prevent snooping.
