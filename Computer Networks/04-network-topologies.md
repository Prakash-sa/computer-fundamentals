# Network Topologies

## Star
- Nodes connect to a central switch/hub; easy to manage and expand.
- Failure of the central device impacts all nodes, so redundancy (stacked switches) is recommended.
- Interview Q: *"Why is star preferred for modern Ethernet?"* — isolates collisions and simplifies troubleshooting.

## Bus
- Single backbone cable shared by multiple hosts; collisions and terminator issues made it unreliable.
- Mainly historic but still referenced in exams; remind interviewers you understand CSMA/CD roots.

## Ring
- Each device connects to two neighbors, forming a loop. Token passing ensures deterministic access.
- Modern SONET/SDH and some metro Ethernet deployments use dual counter-rotating rings for resiliency.

## Mesh
- Every node has multiple paths to others; scales well for backbone/ISP networks and wireless mesh.
- Full mesh is expensive; partial mesh balances cost and redundancy.

## Hybrid
- Real-world networks combine stars, rings, and meshes (e.g., star access with dual-homed core).

## Logical vs Physical Topology
- Logical describes data flow (VLANs, overlay tunnels), whereas physical describes cabling layout.
- Interview Q: *"Can a network be physically star but logically ring?"* — yes, protocols like Token Ring over star wiring.

## Design Considerations
- **Redundancy:** Dual uplinks, link aggregation, and chassis pairs prevent single points of failure.
- **Performance:** Avoid bottlenecks by sizing uplinks higher than access links (3:1 ratio rule of thumb).
- **Spanning Tree & Routing:** Loops require protocols (STP, RSTP, MSTP) or layer-3 designs (leaf-spine) to stay stable.

## Common Interview Prompts
- *"Explain leaf-spine architecture."* — Two-layer fabric where every leaf switch connects to every spine, delivering predictable latency.
- *"How would you connect two data centers for high availability?"* — discuss redundant dark fiber, DWDM, EVPN/VXLAN overlays forming a hybrid topology.
