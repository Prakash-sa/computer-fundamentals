# Lec-20: CAP Theorem

## Quick Highlights
- CAP: consistency, availability, partition tolerance—can pick only two under partitions.
- Consistency = all nodes see same data; availability = every request gets a response.
- Partitions force systems toward CP (consistent, less available) or AP (available, eventual consistency).
- CA only when partitions are impossible (single-node/fully reliable network).

## Diagram
```mermaid
flowchart TB
    Consistency --- Availability
    Availability --- PartitionTolerance
    PartitionTolerance --- Consistency
    note right of PartitionTolerance: Network splits force CP or AP choice
```

## Full Notes
Use the highlights for a quick scan; expand below for the verbatim PDF text.
<details>
<summary>Show raw lecture notes</summary>

```text
1. CAP theorem — overview
  - CAP is a fundamental principle for distributed systems: under network partitions, a system must trade between consistency and availability.

2. Definitions
  - Consistency: every read receives the most recent write (all nodes appear to have the same data at the same time).
  - Availability: every request receives a response (the system remains operational) even if some nodes are down.
  - Partition tolerance: the system continues to operate despite arbitrary message loss or network partitioning between nodes.

3. The trade-off
  - The CAP theorem states that in the presence of a network partition, a distributed system can provide either consistency or availability, but not both.
  - When there is no partition, a system can be both consistent and available (CA), but partitions are realistic in distributed environments.

4. Examples and choices
  - CP systems: prioritize consistency and tolerate partitions by sacrificing availability during the split (e.g., some MongoDB configurations, Zookeeper).
  - AP systems: prioritize availability and tolerate partitions by allowing temporary inconsistency (eventual consistency) such as Cassandra or Dynamo-style systems.
  - CA systems: provide consistency and availability only when partitions are impossible (single-node or perfectly reliable networks).

5. Practical implications
  - Choose CP when correctness is critical (banking/payments) and temporary unavailability is acceptable.
  - Choose AP when low-latency availability is critical and eventual convergence is acceptable (social feeds, caching).
  - Design for the expected failure modes and pick data models/replication strategies to match application requirements.
```

</details>

## Interview Q&A
- **Q:** Give a CP and an AP system example.
  **A:** CP: HBase/Zookeeper (prefer consistency on partition); AP: Dynamo/Cassandra (remain available with eventual consistency).
- **Q:** How would you handle network partitions in a payments system?
  **A:** Favor consistency (CP): reject or queue writes until quorum is restored to avoid double spending.
- **Q:** Can a system be fully CA in the CAP sense?
  **A:** No in distributed environments where partitions can occur; CA is achievable only when partitions are ruled out (single-node or fully reliable network).
