# IP Addressing & Subnetting

## IPv4 Review
- 32-bit addresses written as dotted decimal; CIDR notation (`192.168.1.23/24`) indicates network mask length.
- Divided logically into network ID and host ID determined by subnet mask.

## Address Classes (Legacy)
- **Class A:** 0.0.0.0–127.255.255.255, /8 default mask.
- **Class B:** 128.0.0.0–191.255.255.255, /16.
- **Class C:** 192.0.0.0–223.255.255.255, /24.
- **Class D:** 224.0.0.0–239.255.255.255 for multicast.
- **Class E:** 240.0.0.0–255.255.255.255 reserved.
- Interview note: Modern networks use CIDR supernetting/subnetting rather than classful assumptions, but classes still appear in exams.

## Private Ranges (RFC1918)
- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`
- Must be translated (NAT/PAT) for Internet access.

## Subnet Masks & Calculations
- Mask identifies how many bits belong to the network. Example: `/26` → 255.255.255.192 → 62 usable hosts.
- Wildcard mask (inverse mask) used in ACLs: `/24` → 0.0.0.255.
- Interview Q: *"How many hosts in /27?"* — 2^(32-27) - 2 = 30 usable.

## NAT Variants
- **Static NAT:** One-to-one mapping; used for public-facing servers.
- **Dynamic NAT:** Pool of public IPs shared among private hosts.
- **PAT (Port Address Translation):** Many-to-one mapping using unique source ports.
- **CGNAT:** Carrier-grade NAT for ISPs to conserve IPv4, but complicates end-to-end connectivity.

## IPv6 Highlights
- 128-bit addresses written in hexadecimal (e.g., `2001:db8::1`).
- Vast address space removes need for NAT; uses Neighbor Discovery and SLAAC.
- Interview Q: *"How do IPv6 and IPv4 differ in header structure?"* — IPv6 has fixed 40-byte header, no checksum, optional extension headers.

## Troubleshooting Tips
- Use `ipconfig`, `ifconfig`, or `ip addr` to verify addressing; `ip route` for default gateway checks.
- `ping`, `traceroute`, and `arp -a` confirm reachability and layer-2 resolution.
- Subnet calculators and mental math (powers of two) are frequently asked in interviews.
