# Network Topologies

## Star
- Every node connects to a central switch or hub.
- Simplifies adds/moves/changes and isolates link failures.
- Single point of failure at the core switch—if it fails, all attached nodes lose connectivity.

## Bus
- Devices share a single backbone cable (coaxial in early Ethernet).
- Inexpensive but prone to collisions and difficult troubleshooting.
- Mostly legacy; replaced by switched Ethernet topologies.

## Ring
- Each device connects to exactly two neighbors, forming a loop.
- Token Ring and SONET/SDH use deterministic access; a break anywhere can disrupt the ring without protection mechanisms.

## Mesh
- Every node has links to many or all other nodes.
- Provides high fault tolerance and multiple redundant paths, common in WAN backbones and wireless mesh deployments.

## Hybrid
- Combines multiple topologies (e.g., star-of-stars, ringed core with spoke access) to balance cost and resiliency.

## Design Considerations
- **Redundancy vs. budget:** Dense meshes improve uptime but cost more cabling and ports.
- **Management:** Topology affects how easy it is to monitor, configure, and secure the environment.
- **Scalability:** Plan for growth so additional nodes can be added without major redesign.
