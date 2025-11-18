# Common Interview Diagram

When a user loads `www.google.com`, each OSI layer plays a part:

| Layer | Role in the Request |
|-------|---------------------|
| Application | Browser issues an HTTP GET request. |
| Presentation | TLS encrypts the HTTP payload before transmission. |
| Session | SSL/TLS session maintains state and renegotiation. |
| Transport | TCP performs a three-way handshake and provides reliable delivery. |
| Network | IP addresses route the packet across ISPs and backbone routers. |
| Data Link | Ethernet/Wi-Fi frames deliver packets hop-by-hop. |
| Physical | Bits traverse copper, fiber, or wireless spectrum. |

## Visualization
```
Application  → HTTP
Presentation → TLS
Session      → SSL session
Transport    → TCP (3-way handshake)
Network      → IP routing
Data Link    → Ethernet frame
Physical     → Bits on cable/wireless
```

Remembering this "stack walk" helps answer interview questions such as “What happens when you type a URL into a browser?”
