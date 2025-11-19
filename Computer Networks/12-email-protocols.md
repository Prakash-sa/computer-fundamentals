# Email Protocols

## Core Protocol Roles
- **SMTP (Simple Mail Transfer Protocol):** Push protocol for sending mail between clients (MUAs) and servers (MTAs). Ports 25, 465 (SMTPS), 587 (submission).
- **IMAP (Internet Message Access Protocol):** Synchronizes mailboxes while keeping messages on the server; supports multiple folders, flags, and partial fetches. Ports 143/993.
- **POP3 (Post Office Protocol):** Downloads messages to the client, optionally deleting server copies. Ports 110/995.

## End-to-End Flow
```
Client (MUA) → SMTP submission → Sender MTA → DNS MX lookup → Recipient MTA → Recipient mailbox → IMAP/POP3 access
```
- MX records determine which server receives inbound mail.
- MTAs queue and retry if the recipient server is temporarily unreachable.

## Security and Trust
- **Authentication:** SMTP AUTH, OAuth for cloud services.
- **Encryption:** STARTTLS upgrades plaintext SMTP/IMAP/POP3; or implicit TLS on ports 465/993/995.
- **Anti-spoofing:** SPF (allows sender IP ranges), DKIM (signs headers), DMARC (policy/monitoring) combine to reduce phishing.

## Interview Questions
- *"Difference between IMAP and POP3?"* — IMAP leaves mail on server with multi-device sync; POP3 typically downloads and removes messages.
- *"How do you ensure reliable mail delivery?"* — Use redundant MX records, queue monitoring, spam filtering, and TLS enforcement.
- *"What is an open relay?"* — SMTP server that allows unauthenticated relaying; major security risk.

## Troubleshooting Tips
- Use `telnet`/`openssl s_client` to manually converse with SMTP/IMAP servers and verify responses.
- Check message headers for `Received` lines to trace path.
- Monitor mail queues (`postqueue -p`, `mailq`) and logs (`/var/log/maillog`) for deferred/bounced mail.
