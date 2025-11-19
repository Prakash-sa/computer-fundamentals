# Common Interview Diagram

## Layered Walkthrough When Loading `www.google.com`
| OSI Layer | Action |
|-----------|--------|
| Application | Browser constructs an HTTP GET request with headers and cookies. |
| Presentation | TLS encrypts the payload, negotiates cipher suites, and handles compression if enabled. |
| Session | TLS session/SSL context maintains handshake parameters and renegotiation. |
| Transport | TCP establishes the three-way handshake (SYN, SYN-ACK, ACK) and manages sequencing/acknowledgments. |
| Network | IP addresses guide packets through routers across ISPs and backbone networks; TTL decrements each hop. |
| Data Link | Ethernet or Wi-Fi frames encapsulate the packets hop-by-hop using MAC addresses. |
| Physical | Bits traverse copper, fiber, or RF spectrum as electrical/optical signals. |

```
Application  → HTTP
Presentation → TLS
Session      → SSL/TLS session
Transport    → TCP handshake
Network      → IP routing
Data Link    → Ethernet/Wi-Fi frame
Physical     → Bits on the medium
```

## Interview Tips
- Be ready to elaborate on each layer when asked "What happens when you type a URL into your browser?"
- Mention DNS lookup, TCP/TLS handshakes, ARP resolution, routing, and rendering steps for a comprehensive answer.
- Include performance considerations (CDN, caching) or security layers (HSTS, certificate validation) to stand out.
