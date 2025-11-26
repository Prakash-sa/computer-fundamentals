# Lec-08: Transform - ER Model to Relational Model

## Quick Highlights
1. Overview
  - ER and relational models both provide abstract logical representations of real-world enterprises. Because they
    follow similar design principles, ER designs can be systematically transformed into relational schemas.

2. Convert ER to relational: high-level rules
  - The conversion maps ER constructs (entities, relationships, attributes, generalization, aggregation) to tables,
    primary keys (PK), and foreign keys (FK) while preserving semantics.

3. Strong entities
  - Create a table named for the entity; attributes become columns.
  - Use the entity's primary key as the table's PK.
  - Add FKs to represent relationships to other tables when needed.

4. Weak entities
  - Create a table containing the weak entity's attributes.
  - Include the PK of the owner (strong entity) as an FK in the weak-entity table.
  - The weak-entity table's PK is typically a composite: {owner_PK + partial_key} to preserve dependency.

5. Single-valued attributes
  - Represent as columns directly in the owning table.

6. Composite attributes
  - Expand composite attributes into multiple columns in the same table (e.g., Address -> address_street, address_house_no).

7. Multivalued attributes
  - Create a separate table for the multivalued attribute.
  - Include the owning entity's PK as an FK column in that table.
  - The new table's PK is typically {owner_PK, multivalue}.
  - Example: Employee dependents -> DEPENDENT(emp_id FK, dependent_name, PK(emp_id, dependent_name)).

8. Derived attributes
  - Do not store derived attributes as persistent columns unless there is a strong performance reason; derive them at query time.

9. Generalization / Specialization (mapping strategies)
  Method 1 — Superclass table + subclass tables (store PK in subclasses):
    - Create a table for the superclass with common attributes.
    - For each subclass, create a table containing subclass attributes plus the superclass PK as FK/PK.
    - Example: ACCOUNT(account_no PK, balance)
     - SAVINGS(account_no PK/FK, interest_rate, daily_withdrawal_limit)
     - CURRENT(account_no PK/FK, overdraft_amount, per_transaction_charges)

  Method 2 — One table per subclass (only when specialization is disjoint and total):
    - Do not create a superclass table; include superclass attributes in each subclass table.
    - Example: SAVINGS(account_no PK, balance, interest_rate, daily_withdrawal_limit)
           CURRENT(account_no PK, balance, overdraft_amount, per_transaction_charges)

  Drawbacks of Method 2:
    - Overlap or non-total specializations cause duplication or missing representations (e.g., balance duplicated or accounts that belong to neither subclass cannot be represented).

10. Relationships
  - 1:1 and 1:N: implement by adding a FK in the relation on the "many" side (or choose side based on optionality and access patterns).
  - M:N: create a junction table containing FKs to both participating tables and any relationship attributes; set a composite PK or unique constraint on the pair of FKs.

11. Aggregation
  - Represent aggregation (a relationship treated as an entity) by creating a table for the relationship set.
  - Include PKs of participating entities as columns (FKs) and add any descriptive attributes on the relationship.

12. Practical notes
  - Preserve total participation by enforcing NOT NULL and FK constraints where applicable.
  - Choose surrogate vs natural PKs intentionally; use composite keys when necessary to preserve semantics (e.g., weak entities, ordered installments).
  - Normalize tables to avoid redundancy, but denormalize carefully for performance (e.g., caching counters).
For e.g., Banking System generalisation of Account - saving & current.
1. Table 1: account (account-number, balance)
2. Table 2: savings-account (account-number, interest-rate, daily-withdrawal-limit)
3. Table 3: current-account (account-number, overdraft-amount, per-transaction-charges)
2. Method-2: An alternative representation is possible, if the generalisation is disjoint and completethat is, if no
entity is a member of two lower-level entity sets directly below a higher-level entity set, and if every entity in
the higher level entity set is also a member of one of the lower-level entity sets. Here, do not create a table for
the higher-level entity set. Instead, for each lower-level entity set, create a table that includes a column for each
of the attributes of that entity set plus a column for each a ttribute of the higher-level entity sets.
Tables would be:
1. Table 1: savings-account (account-number, balance, interest-rate, daily-withdrawal-limit)
2. Table 2: current-account (account-number, balance, overdraft-amount, per-transaction-charges)
3. Drawbacks of Method-2: If the second method were used for an overlapping generalisation, some values such
as balance would be stored twice unnecessarily. Similarly, if the generalisation were not completethat is, if
some accounts were neither savings nor current accountsthen such accounts could not be represented with
the second method.
8. Aggregation
1. Table of the relationship set is made.
2. Attributes includes primary keys of entity set and aggregation sets entities.
3. Also, add descriptive attribute if any on the relationship.
```

</details>

## Interview Q&A
- **Q:** How do you map a multi-valued attribute from ER to relational schema?
  **A:** Create a separate table with FK to the owning entity and the multi-valued attribute, turning the multi-valued field into multiple rows.
- **Q:** What happens to weak entities during transformation?
  **A:** They become tables whose PK includes the owner’s PK (as FK) plus their partial key, preserving total participation and dependency.
- **Q:** How do you map M:N relationships?
  **A:** Introduce a junction/bridge table containing FKs to both entities and any relationship attributes, with a composite PK or unique constraint.
