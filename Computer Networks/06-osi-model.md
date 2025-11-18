# The OSI Model

The Open Systems Interconnection (OSI) model defines seven abstract layers to help design, implement, and troubleshoot networked systems.

## Layer 1 – Physical
- Moves raw bits over physical media (copper, fiber, wireless, RF).
- Defines voltage levels, modulation, bit rates, connectors, and physical topologies.
- Components: cables, patch panels, repeaters, hubs, antennas.
- Real world: Wi-Fi radios or Ethernet transceivers converting digital signals to electromagnetic waves.

## Layer 2 – Data Link
- Provides node-to-node delivery via framing, MAC addressing, and error detection (CRC).
- Sub-layers: LLC (flow control) and MAC (media access, addressing).
- Protocols: Ethernet, PPP, VLAN tagging (802.1Q), ARP.
- Devices: switches and bridges that learn MAC tables to forward frames.
- Real example: your laptop sends a frame to the router using the router's MAC; the switch forwards it based on its MAC table entry.

## Layer 3 – Network
- Performs logical addressing, routing, and fragmentation.
- Core protocols: IPv4, IPv6, ICMP, routing protocols (OSPF, BGP, RIP).
- Devices: routers and Layer 3 switches.
- TTL prevents endlessly looping packets.

## Layer 4 – Transport
- Ensures end-to-end delivery between processes.
- **TCP:** Reliability, sequencing, flow control, congestion control, three-way handshake (SYN → SYN/ACK → ACK).
- **UDP:** Connectionless datagrams for low-latency services (streaming, DNS, gaming).
- Segment fields include sequence/ack numbers, window sizes, and flags.

## Layer 5 – Session
- Establishes, maintains, and terminates application sessions; may provide checkpoints and authentication hooks.
- Examples: RPC, NetBIOS, SQL session management.

## Layer 6 – Presentation
- Translates data formats, handles compression, and encrypts/decrypts payloads.
- Technologies: TLS/SSL, JSON, XML, JPEG, PNG, ASCII, Unicode.

## Layer 7 – Application
- Closest to the end user, providing networked services such as HTTP/S, DNS, SMTP, IMAP, FTP/SFTP, SSH, DHCP, SNMP, and Telnet.

## Putting It Together
When you open a website, the application layer issues an HTTP GET, the presentation layer encrypts it (TLS), the session layer manages state, TCP segments it, IP routes it, the data link frames it, and the physical layer transmits the bits.

## Troubleshooting Tip
When diagnosing an outage, work from the physical layer upward ("layer 1 first") to systematically isolate the issue.
