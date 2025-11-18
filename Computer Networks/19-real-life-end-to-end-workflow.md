# Real-Life End-to-End Workflow

1. User enters a URL in the browser address bar.
2. Browser checks its DNS cache, then OS cache, router, and finally recursive DNS if needed.
3. Recursive DNS performs root → TLD → authoritative lookups and returns the IP.
4. Browser establishes a TCP three-way handshake with the server IP and port 443/80.
5. TLS handshake negotiates ciphers, verifies certificates, and creates session keys.
6. Browser sends an HTTP GET request for the page.
7. Web server responds with HTML; browser streams in the response body.
8. Browser parses HTML, discovers CSS/JS/image assets, and issues additional HTTP(S) requests.
9. TCP keep-alive or HTTP/2 multiplexing reuses connections to reduce latency.
10. Rendering engine builds the DOM/CSSOM, runs JavaScript, and paints pixels on screen.

## Additional Insights
- Modern browsers leverage prefetch, preconnect, and DNS over HTTPS to reduce page load time.
- Content Delivery Networks (CDNs) may terminate TLS closer to the user while fetching from the origin server.
