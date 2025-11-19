# The OSI Model

The Open Systems Interconnection (OSI) model defines seven layers that provide a common language for designing, deploying, and troubleshooting networked systems.

## Layer 1 – Physical
- Transmits raw bits over copper, fiber, or wireless media.
- Specifies voltages, modulation schemes, connectors, pinouts, and physical topologies.
- Devices: cables, patch panels, hubs, repeaters, wireless radios.
- Interview Q: *"What layer fixes a broken cable?"* — Physical; check link lights and transceivers first.

## Layer 2 – Data Link
- Handles node-to-node delivery via frames, MAC addressing, and CRC error detection.
- LLC manages flow control; MAC defines media access (CSMA/CD, CSMA/CA).
- Protocols: Ethernet, PPP, HDLC, VLAN tagging (802.1Q), ARP (straddles L2/L3).
- Devices: switches, bridges, wireless controllers.
- Real example: your laptop frames traffic with the router's MAC, and the switch forwards based on its MAC table.

## Layer 3 – Network
- Provides logical addressing and routing; fragments packets when necessary.
- Protocols: IPv4/IPv6, ICMP, IPSec, routing protocols (RIP, OSPF, EIGRP, BGP).
- Interview Q: *"Difference between routing and switching?"* — routing uses IP addresses and routing tables; switching uses MAC addresses within a LAN.

## Layer 4 – Transport
- Ensures end-to-end communication between processes.
- **TCP:** Reliable, connection-oriented; uses sequence/ack numbers, windows, and the three-way handshake.
- **UDP:** Connectionless, low overhead; preferred for DNS, VoIP, streaming, QUIC (built on UDP).
- Concepts: flow control, congestion control, retransmissions, multiplexing via ports.

## Layer 5 – Session
- Establishes, manages, and terminates sessions; coordinates checkpoints and recovery.
- Examples: RPC, NetBIOS, SQL sessions, gRPC channels.
- Often abstracted into application frameworks today.

## Layer 6 – Presentation
- Translates data formats, encryption, and compression.
- Technologies: TLS/SSL, TLS 1.3, ASN.1, JSON, XML, JPEG, ASCII, Unicode.
- Interview Q: *"Where does TLS live in the OSI model?"* — commonly mapped to the presentation layer.

## Layer 7 – Application
- Interfaces with end-user applications and defines protocol semantics.
- Protocols: HTTP/S, DNS, SMTP/IMAP/POP, FTP/SFTP, SSH, DHCP, SNMP, Telnet, MQTT.

## Putting It Together
When you browse a website: the application layer issues HTTP GET, presentation encrypts it (TLS), session tracks the connection, transport (TCP) segments it, network (IP) routes it, data link frames it, and physical transmits the bits across the medium.

## Interview Rapid Fire
- *"At which layer do you troubleshoot MTU issues?"* — primarily Layer 3/4 (fragmentation, Path MTU Discovery).
- *"Which layers do switches and routers operate on?"* — switches L2 (some L3), routers L3 and above.
- *"Why is OSI still relevant?"* — aids troubleshooting and exam prep even though TCP/IP stack is implemented in practice.
