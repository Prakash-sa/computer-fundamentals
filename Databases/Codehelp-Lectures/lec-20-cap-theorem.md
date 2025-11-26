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
1. Basic and one of the most important concept in Distributed Databases.
2. Useful to know this to design efcient distributed system for your given business logic.
3. Lets rst breakdown CAP
1. Consistency: In a consistent system, all nodes see the same data simultaneously. If we perform a read operation on a consistent system, it
should return the value of the most recent write operation. The read should cause all nodes to return the same data. All users see the same data
at the same time, regardless of the node they connect to. When data is written to a single node, it is then replicated across the other nodes in
the system.
2. Availability: When availability is present in a distributed system, it means that the system remains operational all of the time. Every request
will get a response regardless of the individual state of the nodes. This means that the system will operate even if there are multiple nodes
down. Unlike a consistent system, theres no guarantee that the response will be the most recent write operation.
3. Partition Tolerance: When a distributed system encounters a partition, it means that theres a break in communication between nodes. If a
system is partition-tolerant, the system does not fail, regardless of whether messages are dropped or delayed between nodes within the
system. To have partition tolerance, the system must replicate records across combinations of nodes and networks.
4. What does the CAP Theorem says,
1. The CAP theorem states that a distributed system can only provide two of three properties simultaneously: consistency, availability, and
partition tolerance. The theorem formalises the tradeoff between consistency and availability when theres a partition.
5. CAP Theorem NoSQL Databases: NoSQL databases are great for distributed networks. They allow for horizontal scaling, and they can quickly scale
across multiple nodes. When deciding which NoSQL database to use, its important to keep the CAP theorem in mind.
1. CA Databases: CA databases enable consistency and availability across all nodes. Unfortunately, CA databases cant deliver fault tolerance. In
any distributed system, partitions are bound to happen, which means this type of database isnt a very practical choice. That being said, you still
can nd a CA database if you need one. Some relational databases, such as MySQL or PostgreSQL, allow for consistency and availability. You can
deploy them to nodes using replication.
2. CP Databases: CP databases enable consistency and partition tolerance, but not availability. When a partition occurs, the system has to turn
off inconsistent nodes until the partition can be xed. MongoDB is an example of a CP database. Its a NoSQL database management system
(DBMS) that uses documents for data storage. Its considered schema-less, which means that it doesnt require a dened database schema. Its
commonly used in big data and applications running in different locations. The CP system is structured so that theres only one primary
node that receives all of the write requests in a given replica set. Secondary nodes replicate the data in the primary nodes, so if the
primary node fails, a secondary node can stand-in. In banking system Availability is not as important as consistency, so we can opt it
(MongoDB).
3. AP Databases: AP databases enable availability and partition tolerance, but not consistency. In the event of a partition, all nodes are available,
but theyre not all updated. For example, if a user tries to access data from a bad node, they wont receive the most up-to-date version of the
data. When the partition is eventually resolved, most AP databases will sync the nodes to ensure consistency across them. Apache Cassandra is
an example of an AP database. Its a NoSQL database with no primary node, meaning that all of the nodes remain available. Cassandra allows
for eventual consistency because users can re-sync their data right after a partition is resolved. For apps like Facebook, we value availability
more than consistency, wed opt for AP Databases like Cassandra or Amazon DynamoDB.
```

</details>

## Interview Q&A
- **Q:** Give a CP and an AP system example.
  **A:** CP: HBase/Zookeeper (prefer consistency on partition); AP: Dynamo/Cassandra (remain available with eventual consistency).
- **Q:** How would you handle network partitions in a payments system?
  **A:** Favor consistency (CP): reject or queue writes until quorum is restored to avoid double spending.
- **Q:** Can a system be fully CA in the CAP sense?
  **A:** No in distributed environments where partitions can occur; CA is achievable only when partitions are ruled out (single-node or fully reliable network).
