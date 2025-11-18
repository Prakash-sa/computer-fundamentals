# Switching

## Switch Functions
- Forward frames based on MAC address tables learned dynamically.
- Break collision domains per port, enabling full-duplex communication.
- Provide VLAN segmentation to isolate traffic logically.
- Run Spanning Tree Protocol (STP/RSTP/MSTP) to prevent switching loops.

## Additional Capabilities
- **Quality of Service:** Prioritize voice/video traffic via IEEE 802.1p or DSCP re-marking.
- **Link aggregation:** IEEE 802.3ad/LACP bundles links for additional throughput and resiliency.
- **Port security:** Limits MAC addresses per port to mitigate rogue device insertion.
- **Power over Ethernet:** Supplies power to IP phones, access points, and cameras over copper cabling.

## Operational Tips
- Regularly verify STP root roles to avoid accidental topology changes.
- Monitor MAC table usage; overflowing tables cause flooding and degraded performance.
