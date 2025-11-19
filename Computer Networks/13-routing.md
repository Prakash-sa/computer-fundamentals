# Routing

## Definition
Routing selects the optimal path for packets to traverse interconnected networks by consulting routing tables and metrics.

## Routing Types
- **Static Routing:** Admin-defined next hops; simple and predictable but does not adapt automatically.
- **Dynamic Routing:** Protocols exchange topology information to converge on the best paths.

## Dynamic Protocol Families
- **Distance Vector:** RIP, RIPv2—routers share entire routing tables periodically; metric = hop count.
- **Link State:** OSPF, IS-IS—routers flood link states, build a topology map, and run Dijkstra's SPF algorithm.
- **Path Vector:** BGP—routers exchange AS paths, policies, and attributes (MED, LocalPref) suited for Internet-scale routing.
- **Hybrid:** EIGRP blends distance vector and link-state concepts.

## Router Responsibilities
- Maintain routing tables/FIBs, forward packets, apply ACLs, NAT/PAT, QoS, and policy-based routing.
- Participate in redundancy protocols (HSRP, VRRP, GLBP) for gateway resilience.
- Support features like NetFlow/IPFIX for telemetry.

## Interview Hot Topics
- *"Explain the difference between OSPF areas and BGP autonomous systems."* — OSPF hierarchical design within one organization vs BGP between autonomous systems.
- *"What is convergence time?"* — Duration for routers to agree on routes after a change; critical for uptime.
- *"How does ECMP work?"* — Equal-cost multipath load balances traffic across multiple links with the same metric.
- *"Describe route redistribution."* — Injecting routes from one protocol into another with care to avoid loops.

## Troubleshooting Tips
- Verify interface status and neighbor adjacencies (`show ip ospf neighbor`, `show ip bgp summary`).
- Use `traceroute` to observe path changes; compare with routing tables.
- Monitor for route flapping or dampening triggers in BGP environments.
