# Lec-11: Normalisation

## Quick Highlights
- Normalization reduces redundancy and anomalies using functional dependencies.
- Trivial vs non-trivial FDs; determinants and dependents.
- Armstrong's axioms: reflexive, augmentation, transitive, decomposition, union, pseudo-transitive.
- Normal forms progression: 1NF -> 2NF -> 3NF -> BCNF, balancing dependency preservation.

## Diagram
```mermaid
flowchart LR
    Raw[Unnormalised relation] --> N1[1NF: remove repeating groups]
    N1 --> N2[2NF: remove partial dependency]
    N2 --> N3[3NF: remove transitive dependency]
    N3 --> BCNF[BCNF: strongest key-based FDs]
```

## Full Notes
Use the highlights for a quick scan; expand below for the verbatim PDF text.
<details>
<summary>Show raw lecture notes</summary>

```text
1. Purpose of normalization
  - Normalization is a process to organize database schemas to reduce redundancy and avoid anomalies (insert/update/delete).

2. Functional dependencies (FD)
  - An FD X -> Y means the value of attribute set X uniquely determines attribute set Y.
  - Terminology: X is the determinant; Y is the dependent.
  - Trivial FD: Y is a subset of X (e.g., A -> A).
  - Non-trivial FD: Y is not a subset of X.

3. Armstrong's axioms (FD inference rules)
  - Reflexivity: If B ⊆ A then A -> B.
  - Augmentation: If A -> B then AX -> BX for any attribute set X.
  - Transitivity: If A -> B and B -> C then A -> C.

4. Why normalize?
  - To eliminate redundancy and prevent anomalies that cause inconsistency or extra storage.

5. Anomalies caused by redundancy
  - Insertion anomaly: cannot insert certain information without other unrelated data.
  - Deletion anomaly: deleting a row removes other needed information.
  - Update anomaly: updating a value requires multiple row updates and may lead to inconsistencies.

6. Normal forms (progression)
  - 1NF: Atomic values only; no repeating or multi-valued attributes.
  - 2NF: In 1NF and no partial dependency — every non-prime attribute must depend fully on the (composite) PK.
  - 3NF: In 2NF and no transitive dependency — non-prime attributes must not depend on other non-prime attributes.
  - BCNF: Stronger than 3NF — for every FD A -> B, A must be a superkey.

7. Benefits
  - Reduced redundancy, improved organization, easier maintenance, and better data consistency.
```

</details>

## Interview Q&A
- **Q:** What problem does normalization solve?
  **A:** It reduces redundancy and anomalies (update/insert/delete) by organizing data based on functional dependencies.
- **Q:** 3NF vs BCNF—when can BCNF be hard to achieve?
  **A:** BCNF requires every determinant to be a super key; in schemas with overlapping candidate keys (e.g., course-teacher-room), 3NF may be chosen to keep dependency preservation.
- **Q:** Give an example of a transitive dependency.
  **A:** Student(id, dept_id, dept_name): id -> dept_id and dept_id -> dept_name, so id transitively determines dept_name.
