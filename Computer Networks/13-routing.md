# Routing

## Definition
Routing is the process of selecting the best path for packets to travel from source to destination across interconnected networks.

## Types of Routing
- **Static routing:** Administrator manually configures next-hop entries; simple but not scalable.
- **Dynamic routing:** Routers exchange information to adapt to topology changes.

## Dynamic Protocol Families
- **RIP (Routing Information Protocol):** Distance-vector, hop-count metric, suitable for small networks.
- **OSPF (Open Shortest Path First):** Link-state, uses Dijkstra’s algorithm and areas for scalability.
- **BGP (Border Gateway Protocol):** Path-vector protocol that powers Internet-wide routing between autonomous systems.

## Router Responsibilities
- Maintain and update routing tables.
- Forward packets based on destination IP.
- Perform NAT/PAT, QoS marking, and policy-based routing when configured.
- Apply access control lists (ACLs) or firewall rules to enforce security policies.

## Additional Considerations
- **Convergence time:** How quickly the network responds to failures.
- **Metrics:** Cost, bandwidth, delay, reliability determine path selection.
- **Redundancy:** Dual routers, VRRP/HSRP, and ECMP keep traffic flowing during outages.
