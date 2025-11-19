# Introduction to Networking

## What Is a Network?
A network is a collection of interconnected nodes—endpoints, servers, sensors, printers, or appliances—that communicate through shared media using standardized protocols. Links can be physical (Ethernet, fiber) or wireless (Wi-Fi, 5G, Bluetooth) yet appear seamless to applications.

## Why Do We Need Networking?
- **Resource sharing:** Pool expensive printers, storage arrays, GPU farms, and licensed software for multiple consumers.
- **Communication:** Email, instant messaging, VoIP, video conferencing, and IoT telemetry all rely on IP connectivity.
- **Distributed computing:** Microservices and clustered workloads scale horizontally instead of depending on a single machine.
- **Internet access:** Users consume SaaS apps, APIs, and cloud resources via ISPs and backbone providers.
- **Centralized management:** IT can push patches, monitor devices, and enforce policies from a single location.

## Real-World Flow Example
```
Laptop → Wi-Fi Router → ISP Edge → Internet Backbone → CDN/DC → App Server → reverse path response
```
Each hop may be controlled by a different entity, yet standardized protocols keep traffic interoperable and secure.

## Key Metrics and Design Goals
- **Bandwidth vs. throughput:** Theoretical link speed vs. effective data transfer rate.
- **Latency & jitter:** Round-trip delay and variation; critical for real-time apps.
- **Availability:** Redundant hardware and paths reduce downtime.
- **Security:** Encryption, segmentation, and access control guard sensitive data.
- **Scalability:** Modular architectures accommodate new devices, sites, or users without redesign.

## Common Interview Prompts
- *"Explain the difference between a switch and a router in a home network."* — Highlight that switches keep traffic within a LAN using MAC addresses, while routers connect distinct networks and make IP-based forwarding decisions.
- *"Describe what happens after you hit Enter on a URL."* — Reference DNS lookups, TCP/TLS handshakes, HTTP requests, and rendering pipeline.
- *"How would you design a small office network for 50 users?"* — Mention segmented VLANs, redundant switches, firewall/UTM, Wi-Fi controllers, and monitoring.

## Quick Answers to Expect
- **What is bandwidth?** Maximum rate a link can carry, measured in bits per second.
- **What is latency?** Time required for a packet to travel from source to destination.
- **What is QoS?** Policies that prioritize critical traffic when contention occurs.
