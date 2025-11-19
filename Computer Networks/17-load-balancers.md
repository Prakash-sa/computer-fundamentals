# Load Balancers

## Purpose
Distribute client requests across multiple backend servers to increase availability, scalability, and performance.

## Types of Load Balancing
- **Layer 4 (Transport):** Decisions based on IP/port; TCP/UDP proxy or DNAT. Examples: AWS NLB, HAProxy in TCP mode.
- **Layer 7 (Application):** Inspects HTTP headers, URIs, cookies to route intelligently. Examples: Nginx, Envoy, AWS ALB, F5 BIG-IP LTM.
- **Global Server Load Balancing (GSLB):** Uses DNS or Anycast to steer users to the nearest/healthiest region.

## Common Algorithms
- **Round Robin:** Rotate through backend list.
- **Least Connections:** Prefer servers handling fewer active sessions.
- **Weighted Round Robin/Least Connections:** Prioritize more powerful nodes.
- **IP Hash / Sticky Sessions:** Persist clients to the same server (important for stateful apps without shared storage).

## Additional Features
- Health checks (HTTP/S, TCP, custom scripts) to remove unhealthy instances.
- TLS termination/offload, HTTP compression, caching.
- Web Application Firewall (WAF) integration and rate limiting.
- Service discovery integration with Kubernetes/Consul for dynamic backends.

## Interview Questions
- *"Why terminate TLS at a load balancer?"* — Centralized certificate management, reduced CPU load on application servers, ability to inspect traffic.
- *"Difference between reverse proxy and load balancer?"* — Reverse proxy forwards client requests to a server; load balancer usually distributes across multiple servers (often implemented as a reverse proxy).
- *"How do you maintain session stickiness?"* — Cookies, source IP hashing, or consistent hashing algorithms.
- *"What is Anycast?"* — Multiple load balancers share the same IP; routing sends clients to the closest instance, improving latency and resiliency.

## Troubleshooting
- Inspect health check logs to see why nodes are marked down.
- Capture traffic to verify TLS negotiation and header rewriting.
- Monitor metrics (requests/sec, latency, errors) to scale pools proactively.
