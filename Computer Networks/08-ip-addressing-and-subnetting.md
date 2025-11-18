# IP Addressing & Subnetting

## IPv4 Basics
- IPv4 uses a 32-bit address split into four octets (`A.B.C.D`).
- Addresses are often written in CIDR notation (e.g., `192.168.1.23/24`).

## Address Classes
- **Class A:** 0.0.0.0 – 127.255.255.255
- **Class B:** 128.0.0.0 – 191.255.255.255
- **Class C:** 192.0.0.0 – 223.255.255.255
- **Class D:** 224.0.0.0 – 239.255.255.255 (multicast)
- **Class E:** Reserved for experimentation

## Private Address Ranges
- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`
These ranges are non-routable on the public Internet and require NAT to reach external services.

## Subnet Masks
- Define how many bits represent the network vs the host portion.
- Example: `192.168.1.23/24` has a mask of `255.255.255.0`, meaning 24 bits for the network and 8 bits for hosts.
- Subnetting enables segmentation for security, performance, and address conservation.

## NAT (Network Address Translation)
- **Static NAT:** One-to-one mapping between private and public addresses.
- **Dynamic NAT:** Uses a pool of public addresses shared among private clients.
- **PAT (Port Address Translation):** Maps multiple internal clients to a single public IP by translating ports (a.k.a. NAT overload).

## Additional Considerations
- IPv6 (128-bit) eliminates exhaustion concerns and simplifies routing via huge address spaces.
- Supernetting and CIDR allow more flexible allocations than classful addressing.
- Tools such as `ipcalc` or `cidr.xyz` help calculate host counts, masks, and wildcard bits quickly.
