# The TCP/IP Model

## Four-Layer Stack
1. **Application:** Maps to OSI layers 5–7; includes protocols such as HTTP/S, DNS, SMTP, and SSH.
2. **Transport:** Equivalent to OSI Layer 4; implements TCP, UDP, QUIC.
3. **Internet:** OSI Layer 3; provides IP addressing and routing (IPv4/IPv6, ICMP, ARP at the boundary).
4. **Link:** Combines OSI Layers 1–2; includes Ethernet, Wi-Fi, PPP, Fiber Channel.

## OSI vs TCP/IP Mapping
| OSI Layers | TCP/IP Layer |
|------------|--------------|
| 7, 6, 5    | Application  |
| 4          | Transport    |
| 3          | Internet     |
| 2, 1       | Link         |

## Why It Matters
- TCP/IP is the de facto model implemented in real networks, while OSI is more conceptual.
- Understanding both views aids in interviews, certification exams, and troubleshooting because tools and documentation often reference either model.
- Newer protocols (e.g., QUIC, HTTP/3) still fit into the TCP/IP layering even when they blur traditional OSI boundaries.
