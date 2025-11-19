# HTTP and HTTPS

## HTTP Basics
- Application-layer protocol using request/response semantics over TCP (default port 80).
- Example request:
```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Chrome
Accept: text/html
```
- Response includes status line, headers, and optional body.
- Methods: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`.

## HTTP Versions
- **HTTP/1.1:** Persistent connections with pipelining (rarely used due to HOL blocking).
- **HTTP/2:** Binary framing, multiplexed streams, header compression (HPACK), requires TLS in browsers.
- **HTTP/3:** Runs over QUIC/UDP to reduce handshake latency and mitigate head-of-line blocking.

## HTTPS (HTTP over TLS)
- Encrypts HTTP using TLS (default port 443), providing confidentiality, integrity, and authentication.
- Involves certificate verification via public key infrastructure (Certificate Authorities, OCSP, stapling).
- Modern best practices: TLS 1.2+, strong cipher suites, HSTS, certificate transparency monitoring.

## Interview Q&A
- *"What happens during an HTTPS handshake?"* — ClientHello/ServerHello negotiate cipher suites, exchange certificates, establish shared secrets via Diffie-Hellman, then derive session keys.
- *"Difference between idempotent and safe methods?"* — `GET` is safe (no modification), `PUT` is idempotent (same effect on repeated calls), `POST` is neither.
- *"How do REST and SOAP differ?"* — REST leverages resources and HTTP verbs; SOAP uses XML envelopes and can run over multiple transports.

## Troubleshooting Tips
- Use `curl -v` or browser dev tools to inspect headers, response codes, and TLS versions.
- Check server logs for 4xx/5xx errors; correlate with load balancer metrics.
- Tools like `openssl s_client`, `ssllabs.com`, or `testssl.sh` verify certificates and cipher support.
