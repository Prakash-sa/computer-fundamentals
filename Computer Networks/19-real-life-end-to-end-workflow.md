# Real-Life End-to-End Workflow

## Step-by-Step Walkthrough
1. **URL Entry:** User types a URL or clicks a link; browser parses the scheme, host, and path.
2. **DNS Resolution:** Browser/OS cache lookup → router cache → ISP recursive resolver → root/TLD/authoritative servers if needed.
3. **TCP Handshake:** Browser opens a TCP connection to the resolved IP (typically port 443) using the three-way handshake.
4. **TLS Handshake:** Negotiates cipher suites, exchanges certificates, validates chain, and establishes symmetric keys.
5. **HTTP Request:** Browser sends `GET /` with headers (Host, User-Agent, cookies) and possibly H2 multiplexed streams.
6. **Server Processing:** Web server or CDN retrieves content, applies business logic, queries databases/cache, and prepares response.
7. **HTTP Response:** Server sends status code, headers, and HTML body; content may be chunked or compressed (Gzip/Brotli).
8. **Asset Fetching:** Browser parses HTML, issues concurrent requests for CSS, JS, images, fonts; may reuse TCP connections (keep-alive) or HTTP/2 streams.
9. **Rendering:** DOM + CSSOM combined into render tree; JavaScript executes, layout/paint/composite occurs.
10. **Persistent Connections:** Keep-alive or HTTP/2 prevents repeat handshakes; WebSockets or SSE maintain bidirectional streams when needed.

## Optimization Touchpoints
- DNS prefetch, preconnect, and CDN edge caching reduce latency.
- Compression, minification, and lazy loading improve render time.
- QUIC/HTTP3 shortens connection setup and improves loss recovery.

## Interview Notes
- Highlight caches at multiple layers (browser, CDN, reverse proxy, database) when asked about performance.
- Discuss security: HSTS, certificate pinning, CSP, and SameSite cookies.
- Mention observability: use HAR files, `lighthouse`, and tracing headers to troubleshoot slow page loads.
