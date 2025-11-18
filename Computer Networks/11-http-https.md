# HTTP and HTTPS

## HTTP Basics
Example request:
```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Chrome
```
Example response:
```
HTTP/1.1 200 OK
Content-Type: text/html
```

## Common Methods
- `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`

## HTTPS
- Wraps HTTP inside TLS/SSL to provide encryption, integrity, and server authentication via digital certificates.
- Modern browsers enforce HTTPS for sensitive data and offer HSTS to require secure transport.

## Additional Notes
- HTTP/2 multiplexes streams over a single TCP connection; HTTP/3 uses QUIC/UDP to reduce latency.
- REST, GraphQL, and gRPC build application semantics on top of HTTP transports.
