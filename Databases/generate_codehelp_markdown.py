from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "lecture"


TITLE_OVERRIDES: Dict[int, str] = {
    5: "ER Diagram Workflow & Banking System Case",
    6: "Facebook Mini-Project ERD",
    21: "Master-Slave Database Concept",
}

DIAGRAMS: Dict[int, str] = {
    1: """```mermaid
flowchart LR
    Raw[Raw data] -->|capture| DB[(Database)]
    DB -->|managed by| DBMS[DBMS]
    DBMS -->|processing| Info[Information]
    Info --> Decisions[Decisions/insights]
    Raw -->|context| Info
```""",
    2: """```mermaid
flowchart TB
    subgraph Schema_Levels[Three-Schema Architecture]
        External1[External/View schemas] --> Logical[Logical/Conceptual schema]
        External2[Report view] --> Logical
        Logical --> Physical[Physical/Internal schema]
    end
    subgraph Runtime[Deployment Styles]
        T1[Single tier] --> LocalDB[(Local DB)]
        Client[Rich client] -->|ODBC/JDBC| Server[DB/App Server]
        ThinClient[Browser] --> AppSrv[App Server] --> DBServer[(DB Server)]
    end
```""",
    3: """```mermaid
erDiagram
    STUDENT ||--o{ ENROLLMENT : registers
    COURSE ||--o{ ENROLLMENT : has
    STUDENT {
        int student_id PK
        string name
        string phone
    }
    COURSE {
        int course_id PK
        string title
    }
    ENROLLMENT {
        date enrolled_on
        int grade
    }
```""",
    4: """```mermaid
flowchart TB
    Person -->|is-a| Customer
    Person -->|is-a| Employee
    Vehicle[Vehicle (generalised)] --> Car
    Vehicle --> Bus
    subgraph Aggregation
        Borrow[[Borrow relationship]] --- Customer
        Borrow --- Loan
        Borrow --- Branch
    end
```""",
    5: """```mermaid
erDiagram
    BRANCH ||--o{ ACCOUNT : holds
    BRANCH ||--o{ LOAN : originates
    CUSTOMER ||--o{ ACCOUNT : owns
    CUSTOMER ||--o{ LOAN : borrows
    LOAN ||--o{ PAYMENT : schedules
    EMPLOYEE }o--|| BRANCH : works_at
```""",
    6: """```mermaid
erDiagram
    USER ||--o{ POST : writes
    POST ||--o{ COMMENT : has
    USER ||--o{ COMMENT : authors
    POST ||--o{ LIKE : receives
    USER ||--o{ LIKE : reacts
    USER ||--o{ FRIENDSHIP : connects
    USER ||--o{ FRIENDSHIP : connects
```""",
    7: """```mermaid
flowchart TB
    subgraph Table[Relation]
        direction TB
        Header[Columns/Attributes] --> Rows[Rows/Tuples]
        Rows --> Domains[Domains define legal values]
    end
```""",
    8: """```mermaid
flowchart LR
    ER[ER Diagram] --> Entities[Strong/Weak Entities]
    Entities --> Relations[Tables with PK/FK]
    Attributes[Attributes & multivalued fields] --> Normalised[Flattened columns]
    Relations --> Constraints[PK/FK/Unique/Not null]
```""",
    9: """```mermaid
flowchart LR
    Client --> Parser --> Optimizer --> Executor --> Storage[(Tables/Indexes)]
    Storage --> Executor
    Executor --> Client
```""",
    11: """```mermaid
flowchart LR
    Raw[Unnormalised relation] --> N1[1NF: remove repeating groups]
    N1 --> N2[2NF: remove partial dependency]
    N2 --> N3[3NF: remove transitive dependency]
    N3 --> BCNF[BCNF: strongest key-based FDs]
```""",
    12: """```mermaid
stateDiagram-v2
    [*] --> Active
    Active --> Committed: commit
    Active --> Failed: error/constraint
    Failed --> Aborted: rollback
    Active --> Aborted: rollback request
    Committed --> [*]
    Aborted --> [*]
```""",
    13: """```mermaid
flowchart TB
    DBPointer[db-pointer] --> Shadow[Shadow DB copy]
    DBPointer -.switch.-> NewCopy[New DB copy]
    NewCopy -->|write| Disk[(Disk pages)]
    NewCopy --> Commit[Commit]
    Commit -->|update pointer| DBPointer
```""",
    14: """```mermaid
flowchart TB
    Root[B+ tree root] --> Internal1[Internal node]
    Internal1 --> Leaf1[Leaf node keys + record pointers]
    Internal1 --> Leaf2[Leaf node keys + record pointers]
    Leaf1 --- Leaf2
```""",
    15: """```mermaid
flowchart LR
    KeyValue[Key-Value] --- Doc[Document]
    Doc --- Column[Wide Column]
    Column --- Graph[Graph]
    KeyValue --> Use1[Session/cache]
    Doc --> Use2[Content/catalog]
    Column --> Use3[Analytics/time series]
    Graph --> Use4[Relationships/recommendations]
```""",
    16: """```mermaid
flowchart LR
    Relational --> SQL[SQL + joins]
    Document --> JSON[Flexible schema]
    KeyValue --> Cache[Fast lookups]
    Columnar --> OLAP[Compressed column store]
    Graph --> Traversals[Connected data]
    TimeSeries --> Metrics[Ordered events]
```""",
    17: """```mermaid
flowchart LR
    Client1 & Client2 --> LB[Load balancer]
    LB --> Node1[(DB Node 1)]
    LB --> Node2[(DB Node 2)]
    Node1 --- Node2
    Node1 --> Replica1[Replica set]
    Node2 --> Replica2[Replica set]
```""",
    18: """```mermaid
flowchart TB
    Dataset -->|hash/range key| Shard1[Partition 1]
    Dataset -->|hash/range key| Shard2[Partition 2]
    Dataset -->|hash/range key| Shard3[Partition 3]
    Shard1 & Shard2 & Shard3 --> Queries[Parallel queries]
```""",
    20: """```mermaid
flowchart TB
    Consistency --- Availability
    Availability --- PartitionTolerance
    PartitionTolerance --- Consistency
    note right of PartitionTolerance: Network splits force CP or AP choice
```""",
    21: """```mermaid
flowchart LR
    AppWrites[Writes] --> Master[(Master DB)]
    Master -->|replication| Slave1[(Read replica)]
    Master -->|replication| Slave2[(Read replica)]
    AppReads[Reads] --> Slave1
    AppReads --> Slave2
```""",
}

HIGHLIGHTS: Dict[int, List[str]] = {
    1: [
        "Data vs information with examples; information is processed data used for decisions.",
        "Databases organize data for easy access, updates, and management; DBMS is the software layer.",
        "DBMS solves file-system pain: redundancy, inconsistency, isolation, integrity, atomicity, concurrency, security.",
        "Data measured in bits/bytes; qualitative vs quantitative forms.",
    ],
    2: [
        "Three-schema architecture: external, conceptual, physical; enables data independence.",
        "Physical vs logical vs view schemas; goal is efficient storage plus simple access.",
        "DB languages: DDL for schema/constraints, DML for queries/updates.",
        "DBA responsibilities: schema design, storage, auth, maintenance, backups, patches.",
        "App access via APIs like ODBC/JDBC; 1-tier/2-tier/3-tier client-server patterns.",
    ],
    3: [
        "ER model represents entities, attributes, and relationships as a conceptual blueprint.",
        "Entities have keys; strong vs weak entities (depend on owners).",
        "Attributes can be simple/composite, single/multi-valued, derived; null reasons vary.",
        "Relationships carry cardinality (1:1, 1:N, N:M) and participation (total/partial).",
        "Unary/binary/ternary relationship degrees; mapping impacts schema design.",
    ],
    4: [
        "Specialization (top-down) splits a superclass into subclasses by behavior/attributes.",
        "Generalization (bottom-up) factors common attributes into a new superclass.",
        "Attribute and participation inheritance: children get parent fields and relationships.",
        "Aggregation treats a relationship set as an abstract entity to relate further.",
    ],
    5: [
        "ER diagramming workflow: identify entities, attributes, relationships, mapping, participation.",
        "Banking case: Branch, Customer, Employee, Account (savings/current), Loan, Payment (weak).",
        "Branch originates loans; customers own accounts and loans; payments depend on loans.",
        "Multi-valued attributes (phones, dependents) modeled separately; account generalized.",
    ],
    6: [
        "Facebook mini-ERD: User profiles, Posts, Comments, Likes, Friendships.",
        "Posts have content/media/timestamps; users author posts/comments/likes.",
        "Friendship is an M:N self-relationship; likes/comments are 1:N from posts.",
        "Model supports feed-building via relationships among users and posts.",
    ],
    7: [
        "Relational model stores data in named relations (tables) of tuples and attributes.",
        "Domains define legal values; relation schema = name + attributes + constraints.",
        "Keys (candidate/super) ensure uniqueness; degree = columns, cardinality = rows.",
        "Common RDBMS: Oracle, IBM DB2, MySQL, SQL Server; tuples represent facts.",
    ],
    8: [
        "Goal: convert ER designs into relational schemas while keeping semantics.",
        "Strong entities become tables with PK; weak entities include owner PK in composite key.",
        "M:N relationships become bridge tables with both FKs plus relationship attributes.",
        "Multivalued attributes move to separate tables; specialization handled via PK/FK patterns.",
    ],
    9: [
        "SQL enables CRUD on RDBMS; MySQL uses client-server and SQL dialect.",
        "Data types range from numeric to text/blob; choose sizes carefully (e.g., VARCHAR).",
        "SQL command families: DDL, DML, DQL, DCL, TCL; transactions control atomicity.",
        "Covers selection, filtering, joins, grouping, aggregation, subqueries, views, set ops, functions.",
    ],
    11: [
        "Normalization reduces redundancy and anomalies using functional dependencies.",
        "Trivial vs non-trivial FDs; determinants and dependents.",
        "Armstrong's axioms: reflexive, augmentation, transitive, decomposition, union, pseudo-transitive.",
        "Normal forms progression: 1NF -> 2NF -> 3NF -> BCNF, balancing dependency preservation.",
    ],
    12: [
        "Transaction = logical unit of work; sequence and grouping matter.",
        "ACID: Atomicity, Consistency, Isolation, Durability ensure integrity.",
        "Concurrency control uses schedules (serial, serializable) and isolation levels.",
        "Abort/commit behaviors define outcome visibility and rollback handling.",
    ],
    13: [
        "Recovery mechanisms enforce atomicity/durability after crashes.",
        "Shadow-copy: work on a copy, flip db-pointer on commit; simple, low concurrency.",
        "Log-based recovery (WAL) tracks updates to enable undo/redo; checkpoints trim logs.",
        "Force vs non-force, steal vs no-steal buffer policies shape needed recovery actions.",
    ],
    14: [
        "Indexing is a secondary access path to cut disk I/O for lookups and range scans.",
        "Key + data reference; index files sorted; optional but speeds reads.",
        "Primary/clustered vs secondary/non-clustered; dense vs sparse; multilevel indexes.",
        "B+ tree and hash indexing trade-offs; covering indexes avoid base-table hits.",
    ],
    15: [
        "NoSQL = \"not only SQL\"; non-tabular models: document, key-value, wide-column, graph.",
        "Flexible schemas, horizontal scaling, and handling of big/varied data.",
        "Eventual consistency and CAP trade-offs common in distributed NoSQL stores.",
        "Use cases: caching, content/catalog, analytics/time-series, relationship-heavy workloads.",
    ],
    16: [
        "Database categories: relational, document, key-value, graph, columnar, time-series, cloud/analytic.",
        "Relational uses SQL and joins; document stores JSON-like flexible docs.",
        "Key-value excels at simple lookups/caching; graph optimizes traversals.",
        "Columnar and time-series optimize analytics/ordered events; cloud DBs handle scaling/ops.",
    ],
    17: [
        "Clustering = multiple servers sharing replicated data for availability and scale.",
        "Replica sets improve redundancy; load balancers route requests across nodes.",
        "Failover and replication lag are key operational concerns.",
        "Security and consistency considerations increase with more nodes.",
    ],
    18: [
        "Partitioning/sharding splits large datasets into manageable slices across servers.",
        "Horizontal vs vertical partitioning; range/hash/list/round-robin strategies.",
        "Benefits: performance, manageability, parallelism; costs: cross-shard queries, rebalancing.",
        "Choosing a shard key balances load distribution and query locality.",
    ],
    20: [
        "CAP: consistency, availability, partition tolerance—can pick only two under partitions.",
        "Consistency = all nodes see same data; availability = every request gets a response.",
        "Partitions force systems toward CP (consistent, less available) or AP (available, eventual consistency).",
        "CA only when partitions are impossible (single-node/fully reliable network).",
    ],
    21: [
        "Master-slave (primary-replica) splits writes to master, reads to replicas.",
        "Replication distributes data; replicas reduce read load but can lag.",
        "Failover requires safe promotion and routing updates.",
        "Used to improve throughput, availability, and read latency.",
    ],
}

INTERVIEW_QA: Dict[int, List[Tuple[str, str]]] = {
    1: [
        ("Differentiate data vs information with a real example you have seen in production systems.",
         "Data are raw observations (e.g., clickstream logs), information is processed data that informs action (e.g., session conversion rate derived from those logs)."),
        ("Why do teams move from file-based storage to a DBMS as scale grows?",
         "To reduce redundancy/inconsistency, enforce integrity/security, support concurrency control, indexing, backups, and standardized access through a query language."),
        ("Name two ways to improve data quality at ingestion time.",
         "Validate schemas/types at the edge, normalize controlled vocabularies, reject duplicates with keys, and add metadata (timestamps/source) for traceability."),
    ],
    2: [
        ("Explain physical vs logical data independence and why it matters.",
         "Physical independence means changing storage structures shouldn't break logical schemas; logical independence means view changes shouldn't break apps. This decoupling keeps apps stable as DBs evolve."),
        ("Compare 2-tier and 3-tier DB application architectures.",
         "2-tier has client directly talk to DB server, simpler but harder to scale and secure; 3-tier inserts an app server for business logic, pooling, and security, which scales better on the web."),
        ("How would you expose different user-specific views without duplicating data?",
         "Use the external schema/view layer: create SQL views or APIs that project/secure subsets of the logical schema while the physical data stays single-sourced."),
    ],
    3: [
        ("When do you model something as a weak entity?",
         "Use a weak entity when it lacks a full primary key on its own (e.g., Payment depends on Loan) and must include the owner's key plus a partial discriminator."),
        ("How do cardinality and participation constraints influence schema design?",
         "They drive key/FK placement and uniqueness/nullability (e.g., total participation often means NOT NULL FK; one-to-one may suggest merging tables)."),
        ("Give an example where a ternary relationship is preferable to three binaries.",
         "Assigning an employee to a job at a branch; ternary preserves the joint constraint that involves all three rather than three looser binary links."),
    ],
    4: [
        ("Specialization vs generalization—how do you decide which direction to model?",
         "Top-down specialization when starting from a broad entity and splitting by behavior; bottom-up generalization when multiple entities share attributes/relationships that should be factored out."),
        ("What is aggregation used for?",
         "Aggregation treats a relationship set as an abstract entity so it can participate in other relationships, reducing redundancy (e.g., Loan-Payment relationship linked to Auditor)."),
        ("How would you enforce inherited participation constraints in SQL?",
         "Use shared PK/FK patterns and declarative constraints or triggers so child tables inherit parent's relationships; in ORMs, use table-per-subclass with FK references."),
    ],
    5: [
        ("Walk me through building a banking ERD under 5 minutes.",
         "Identify entities (Branch, Customer, Account, Loan, Employee, Payment), set keys, map relationships (customer-accounts many-to-many via ownership, branch-originates-loan), and note weak entities like Payment."),
        ("How do you capture multi-valued attributes such as customer phone numbers?",
         "Model them as separate related tables (CustomerPhone) or JSON arrays when supported, instead of repeating columns."),
        ("What is the right PK for a payment schedule table tied to loans?",
         "Use a composite key of loan_id + installment_number or a surrogate with a unique constraint on that pair to preserve order and uniqueness."),
    ],
    6: [
        ("Design a minimal schema for news-feed posts.",
         "User table, Post table (id, author_id, content, media, timestamps), Like and Comment tables linked to both post and user, plus Friendship edges for visibility."),
        ("How would you scale the like counter on hot posts?",
         "Use write sharding or counters in cache with periodic aggregation, avoiding per-like row locks on the base post record."),
        ("What edge cases appear in friendship modeling?",
         "Bidirectionality/confirmation, blocking, and ensuring uniqueness per user pair, often via canonical ordering of user_ids with a unique constraint."),
    ],
    7: [
        ("Difference between candidate key, primary key, and super key?",
         "Super key: any set of attributes uniquely identifying tuples; candidate key: minimal super key; primary key: the chosen candidate key used for PK/FK references."),
        ("What are integrity constraints in the relational model?",
         "Domain, entity integrity (PK not null/unique), and referential integrity (FK must match or be null), enforced via constraints and indexes."),
        ("Why is relation degree and cardinality useful?",
         "They describe width (attributes) and size (rows), guiding indexing, normalization, and query cost expectations."),
    ],
    8: [
        ("How do you map a multi-valued attribute from ER to relational schema?",
         "Create a separate table with FK to the owning entity and the multi-valued attribute, turning the multi-valued field into multiple rows."),
        ("What happens to weak entities during transformation?",
         "They become tables whose PK includes the owner’s PK (as FK) plus their partial key, preserving total participation and dependency."),
        ("How do you map M:N relationships?",
         "Introduce a junction/bridge table containing FKs to both entities and any relationship attributes, with a composite PK or unique constraint."),
    ],
    9: [
        ("INNER JOIN vs WHERE old-style joins—why prefer the former?",
         "Explicit JOINs clarify intent, support different join types (LEFT/RIGHT/FULL), and separate join predicates from filters, improving readability and optimizer hints."),
        ("When would you choose EXISTS over IN?",
         "EXISTS short-circuits and handles correlated checks efficiently; IN is fine for small static lists. EXISTS also avoids null/duplicate pitfalls in subqueries."),
        ("Explain GROUP BY vs DISTINCT.",
         "DISTINCT removes duplicates from the projection; GROUP BY aggregates rows by grouping columns and pairs with aggregate functions."),
        ("How do UNION and UNION ALL differ?",
         "UNION removes duplicates and sorts/hashed results; UNION ALL appends without deduping, so it is faster when duplicates are acceptable."),
        ("What is a window function and why is it useful?",
         "It performs calculations across related rows without collapsing them (e.g., running totals, row_number over partitions), enabling advanced analytics in SQL."),
    ],
    11: [
        ("What problem does normalization solve?",
         "It reduces redundancy and anomalies (update/insert/delete) by organizing data based on functional dependencies."),
        ("3NF vs BCNF—when can BCNF be hard to achieve?",
         "BCNF requires every determinant to be a super key; in schemas with overlapping candidate keys (e.g., course-teacher-room), 3NF may be chosen to keep dependency preservation."),
        ("Give an example of a transitive dependency.",
         "Student(id, dept_id, dept_name): id -> dept_id and dept_id -> dept_name, so id transitively determines dept_name."),
    ],
    12: [
        ("Define ACID with a concrete scenario.",
         "Atomicity (all-or-nothing transfer), Consistency (constraints hold), Isolation (concurrent transfers don't interfere), Durability (committed transfer survives crash)."),
        ("Which isolation level prevents phantom reads?",
         "Serializable prevents phantoms; Repeatable Read may still allow them unless using predicate locking or index range locks (varies by DB)."),
        ("How do you group SQL statements into a transaction in application code?",
         "Begin/commit boundaries (START TRANSACTION ... COMMIT) or session autocommit off, with explicit rollback on failures."),
    ],
    13: [
        ("Contrast write-ahead logging with shadow paging.",
         "WAL appends log records before data writes, supporting concurrency; shadow paging copies pages and flips pointers, simpler but less concurrent and copy-heavy."),
        ("What does 'force' vs 'steal' buffer policy mean?",
         "Force writes dirty pages at commit; steal allows flushing uncommitted pages. Steal/no-force is common and requires UNDO/REDO logging."),
        ("How would you test crash recovery?",
         "Simulate crashes mid-transaction, restart the DB, and verify committed data persists while uncommitted changes roll back according to the log."),
    ],
    14: [
        ("Clustered vs non-clustered index?",
         "Clustered index orders the table data physically; non-clustered stores separate index pages pointing to data. Most engines allow one clustered index."),
        ("Hash vs B+ tree index trade-offs?",
         "Hash excels at equality lookups but not range scans/orderings; B+ tree supports range queries, ordering, and partial matches."),
        ("What is a covering index?",
         "An index that contains all columns needed for a query (key + included columns), allowing index-only scans without touching the base table."),
    ],
    15: [
        ("When would you pick a document DB over relational?",
         "When schemas are dynamic, data is hierarchical, and you want to avoid expensive joins—e.g., product catalogs or content metadata."),
        ("Explain eventual consistency in NoSQL stores.",
         "Writes propagate asynchronously; replicas converge over time. Clients may read stale data unless using stronger consistency options."),
        ("How do key design and partitioning interact in NoSQL?",
         "A good partition/shard key evenly distributes load while preserving query patterns (avoid hot partitions; sometimes add random suffixes or time bucketing)."),
    ],
    16: [
        ("Why are columnar stores faster for analytics?",
         "They read only needed columns, compress well, and support vectorized scans; row stores are better for OLTP writes and point lookups."),
        ("Give a use case for graph databases.",
         "Fraud detection or recommendations where traversing multi-hop relationships efficiently is key."),
        ("How do time-series databases optimize for append-heavy workloads?",
         "They use time-ordered partitions, compression, and downsampling/retention policies tuned for sequential writes and range queries."),
    ],
    17: [
        ("How does replication improve availability?",
         "Multiple copies allow failover when one node dies, maintaining reads; synchronous vs asynchronous replication trades latency vs durability."),
        ("What is replication lag and why does it matter?",
         "Delay between master and replicas applying changes; it can cause stale reads or inconsistency in read-after-write workloads."),
        ("How would you avoid split-brain in a DB cluster?",
         "Use consensus/quorum protocols, fencing, or managed failover with single writer election to ensure only one primary at a time."),
    ],
    18: [
        ("Range vs hash partitioning—when to use each?",
         "Range suits ordered queries/time-series; hash balances load uniformly for random access. Composite schemes mix both."),
        ("How do you choose a good shard key?",
         "Pick a high-cardinality field used in filters that avoids hotspots and supports data locality for common queries."),
        ("How to run queries that span shards?",
         "Use scatter-gather with coordinators, or maintain global indexes/aggregations; design queries to minimize cross-shard joins."),
    ],
    20: [
        ("Give a CP and an AP system example.",
         "CP: HBase/Zookeeper (prefer consistency on partition); AP: Dynamo/Cassandra (remain available with eventual consistency)."),
        ("How would you handle network partitions in a payments system?",
         "Favor consistency (CP): reject or queue writes until quorum is restored to avoid double spending."),
        ("Can a system be fully CA in the CAP sense?",
         "No in distributed environments where partitions can occur; CA is achievable only when partitions are ruled out (single-node or fully reliable network)."),
    ],
    21: [
        ("How do applications route reads and writes in master-slave setups?",
         "Writes go to master; reads go to replicas via connection pools or proxies that understand role metadata, with fallbacks on failover."),
        ("What risks come with read replicas?",
         "Replica lag causing stale reads, potential inconsistency for read-after-write flows, and added complexity in promotion/failover."),
        ("How do you promote a replica to master safely?",
         "Ensure it has all WAL/relay logs, stop writes to old master, elect/promote the replica, redirect traffic, and rebuild other replicas from the new master."),
    ],
}


def clean_body(raw: str) -> str:
    lines = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("===") or stripped == "CodeHelp":
            continue
        lines.append(stripped)
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"[^\x00-\x7F]+", "", cleaned)
    return cleaned


def parse_sections(text: str) -> List[Tuple[int, str, str]]:
    matches = list(re.finditer(r"(?im)^lec-\s*\d+[^\n]*", text))
    sections: List[Tuple[int, str, str]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        header = match.group(0).strip()
        number_match = re.search(r"\d+", header)
        if not number_match:
            continue
        number = int(number_match.group(0))
        title_fragment = header.split(":", 1)[1].strip() if ":" in header else TITLE_OVERRIDES.get(number, f"Lecture {number}")
        title = TITLE_OVERRIDES.get(number, title_fragment)
        body = text[start:end]
        body = body.split("\n", 1)[1] if "\n" in body else ""
        sections.append((number, title, clean_body(body)))
    return sections


def build_markdown(number: int, title: str, notes: str) -> str:
    diagram = DIAGRAMS.get(number, "_Add a diagram for this lecture_")
    highlights = HIGHLIGHTS.get(number, ["Add quick highlights here."])
    highlights_block = "\n".join(f"- {item}" for item in highlights)
    qas = INTERVIEW_QA.get(number, [])
    qa_lines = []
    for q, a in qas:
        qa_lines.append(f"- **Q:** {q}\n  **A:** {a}")
    qa_block = "\n".join(qa_lines) if qa_lines else "- Add interview questions here."
    md = (
        f"# Lec-{number:02d}: {title}\n\n"
        f"## Quick Highlights\n{highlights_block}\n\n"
        f"## Diagram\n{diagram}\n\n"
        f"## Full Notes (verbatim)\n"
        f"<details>\n<summary>Expand to read the original lecture notes</summary>\n\n"
        f"{notes}\n\n"
        f"</details>\n\n"
        f"## Interview Q&A\n{qa_block}\n"
    )
    return md


def main() -> None:
    base_dir = Path("Databases/Codehelp-Lectures")
    base_dir.mkdir(parents=True, exist_ok=True)
    text = Path("Databases/Codehelp.txt").read_text()
    sections = parse_sections(text)
    for number, title, notes in sections:
        filename = base_dir / f"lec-{number:02d}-{slugify(title)}.md"
        content = build_markdown(number, title, notes)
        filename.write_text(content)
        print(f"Wrote {filename}")


if __name__ == "__main__":
    main()
