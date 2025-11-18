# Email Protocols

## Core Roles
- **SMTP:** Sends mail from clients to servers and between MTAs.
- **IMAP:** Retrieves and synchronizes mail while keeping messages on the server.
- **POP3:** Downloads mail to the client, optionally deleting the server copy.

## Typical Flow
```
Client (MUA) → SMTP submission → Mail server → DNS MX lookup → Recipient mail server → IMAP/POP3 access
```

## Additional Concepts
- **Authentication:** SMTP AUTH prevents open relays; SPF, DKIM, and DMARC fight spoofing.
- **Security:** STARTTLS or SMTPS encrypts SMTP, while IMAPS/POP3S secure retrieval.
- **Queueing:** MTAs retry delivery with exponential backoff when recipients are temporarily unavailable.
