# Load Balancers

## Types
- **Layer 4 (Transport):** Distributes TCP/UDP connections using IP/port information.
- **Layer 7 (Application):** Makes decisions based on HTTP headers, cookies, URLs, or content.

## Common Algorithms
- **Round robin:** Rotate through backend pool.
- **Least connections:** Send traffic to servers handling the fewest active sessions.
- **IP hash/sticky sessions:** Always map a client IP or cookie to the same backend.

## Use Cases
- Improve availability and scalability for microservices, APIs, and web apps.
- Offload TLS termination, compression, or caching.
- Provide health checks to remove failed instances automatically.

## Additional Considerations
- Global server load balancing (GSLB) uses DNS or Anycast to steer users to the nearest region.
- Modern platforms (Envoy, Nginx, AWS ALB/ELB) integrate observability, WAF, and autoscaling triggers.
