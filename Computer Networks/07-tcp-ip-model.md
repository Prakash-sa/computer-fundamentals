# The TCP/IP Model

## Four-Layer Stack Overview
1. **Application:** Protocols such as HTTP/S, DNS, SMTP, SSH, NTP, DHCP. Combines OSI layers 5–7.
2. **Transport:** TCP, UDP, SCTP, QUIC; responsible for reliable delivery, ordered segments, or lightweight datagrams.
3. **Internet:** IP addressing and routing (IPv4/IPv6, ICMP, ARP, IPSec) similar to OSI Layer 3.
4. **Link:** Network access layer combining OSI Layers 1–2 (Ethernet, Wi-Fi, PPP, Frame Relay, LTE).

## OSI Mapping Reference
| OSI Layer(s) | TCP/IP Layer | Key Protocols |
|--------------|--------------|---------------|
| 7, 6, 5 | Application | HTTP/S, DNS, SMTP, SNMP, FTP |
| 4 | Transport | TCP, UDP, QUIC |
| 3 | Internet | IPv4, IPv6, ICMP, IPSec |
| 2, 1 | Link | Ethernet, Wi-Fi, PPP |

## Why TCP/IP Prevails
- Directly maps to the stack implemented in operating systems and routers.
- Built-in flexibility to add new protocols (e.g., QUIC over UDP, HTTP/3) without redefining the stack.
- Interoperability: RFCs from the IETF define behavior and promote open standards.

## Interview-Oriented Notes
- *"Difference between TCP and UDP?"* — Mention connection-oriented reliability vs stateless, low-latency datagrams, plus use cases.
- *"Where does TLS fit?"* — Typically between application and transport; interacts with both stacks.
- *"Explain the encapsulation process."* — Data (Layer 7) → segment (Layer 4) → packet (Layer 3) → frame (Layer 2) → bits (Layer 1).
- *"Why is QUIC significant?"* — Runs over UDP to reduce handshake latency, supports multiplexing without head-of-line blocking.

## Practical Tip
When capturing packets, use filters aligned with stack layers (`tcp.port == 443`, `ip.addr == 8.8.8.8`, `eth.addr == 00:11:22:33:44:55`) to isolate issues quickly.
