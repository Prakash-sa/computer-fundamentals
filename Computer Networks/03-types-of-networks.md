# Types of Networks

## LAN (Local Area Network)
- Limited to a building, floor, or campus; owned and managed by a single organization.
- Technologies: Ethernet switching (100 Mbps–400 Gbps), Wi-Fi, PoE for devices.
- Interview Q: *"How would you isolate departments on a LAN?"* — Use VLANs, ACLs, or microsegmentation.

## WAN (Wide Area Network)
- Spans regions/countries, typically leased from service providers; includes MPLS, leased fiber, satellite, and SD-WAN overlays.
- Lower speeds and higher latency than LAN due to propagation distance.
- Interview Q: *"Why choose SD-WAN over traditional MPLS?"* — cost savings, dynamic path selection, centralized policy.

## MAN (Metropolitan Area Network)
- Bridges multiple LANs within a city; carriers offer metro Ethernet or dark fiber rings.
- Often acts as a distribution layer feeding into WAN/Internet gateways.

## Additional Categories
- **PAN (Personal Area Network):** Bluetooth, NFC, Zigbee for wearables and sensors; range of a few meters.
- **CAN (Campus Area Network):** Aggregates multiple LAN buildings with high-speed fiber cores.
- **SAN (Storage Area Network):** Dedicated network (Fibre Channel, iSCSI) for block storage traffic.
- **SD-WAN:** Policy-driven overlay leveraging broadband, LTE, and MPLS simultaneously.

## Comparison Cheat Sheet
| Feature | LAN | MAN | WAN |
|--------|-----|-----|-----|
| Area | Room/Campus | City | Country/Global |
| Speed | 100 Mbps–400 Gbps | 1–100 Gbps | 1 Mbps–100 Gbps |
| Ownership | Private | Carrier/Shared | Carrier/Multiple |
| Protocols | Ethernet, Wi-Fi | Metro Ethernet, DWDM | MPLS, IPsec, BGP |

## Interview Rapid Fire
- *"Which network type is best for IoT sensors spread across a farm?"* — LPWAN (LoRaWAN, NB-IoT) combining WAN reach with low power.
- *"How do you secure branch offices over the Internet?"* — VPN tunnels, ZTNA, and SD-WAN with integrated firewalls.
