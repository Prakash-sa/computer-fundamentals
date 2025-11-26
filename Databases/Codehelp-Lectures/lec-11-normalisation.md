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
1. Normalisation is a step towards DB optimisation.
2. Functional Dependency (FD)
1. It's a relationship between the primary key a ttribute (usually) of the relation to that of the other attribute of the
relation.
2. X -> Y, the left side of FD is known as a Determinant, the right side of the production is known as a Dependent.
3. Types of FD
1. Trivial FD
1. A  B has trivial functional dependency if B is a subset of A. A->A, B->B are also Trivial FD.
2. Non-trivial FD
1. A  B has a non-trivial functional dependency if B is not a subset of A. [A intersection B is NULL].
4. Rules of FD (Armstrongs axioms)
1. Reflexive
1. If A is a set of attributes and B is a subset of A. Then, A B holds.
2. If A  B then A  B.
2. Augmentation
1. If B can be determined from A, then adding an attribute to this functional dependency wont change
anything.
2. If A B holds, then AX BX holds too. X being a set of attributes.
3. Transitivity
1. If A determines B and B determines C, we can say that A determines C.
2. if A B and B C then A C.
3. Why Normalisation?
1. To avoid redundancy in the DB, not to store redundant data.
4. What happen if we have redundant data?
1. Insertion, deletion and updation anomalies arises.
5. Anomalies
1. Anomalies means abnormalities, there are three types of anomalies introduced by data redundancy.
2. Insertion anomaly
1. When certain data (attribute) can not be inserted into the DB without the presence of other data.
3. Deletion anomaly
1. The delete anomaly refers to the situation where the deletion of data results in the unintended loss of some
other important data.
4. Updation anomaly (or modification anomaly)
1. The update anomaly is when an update of a single data value requires multiple rows of data to be updated.
2. Due to updation to many places, may be Data inconsistency arises, if one forgets to update the data at all the
intended places.
5. Due to these anomalies, DB size increases and DB performance become very slow.
6. To rectify these anomalies and the eect of these of DB, we use Database optimisation technique called
NORMALISATION.
6. What is Normalisation?
1. Normalisation is used to minimise the redundancy from a relations. It is also used to eliminate undesirable
characteristics like Insertion, Update, and Deletion Anomalies.
2. Normalisation divides the composite attributes into individual attributes OR larger table into smaller and links them
using relationships.
3. The normal form is used to reduce redundancy from the database table.
7. Types of Normal forms
1. 1NF
1. Every relation cell must have atomic value.
2. Relation must not have multi-valued attributes.
2. 2NF
1. Relation must be in 1NF.
2. There should not be any partial dependency.
1. All non-prime attributes must be fully dependent on PK.
2. Non prime attribute can not depend on the part of the PK.
3. 3NF
1. Relation must be in 2NF.
2. No transitivity dependency exists.
1. Non-prime attribute should not find a non-prime attribute.
4. BCNF (Boyce-Codd normal form)
1. Relation must be in 3NF.
2. FD: A -> B, A must be a super key.
1. We must not derive prime attribute from any prime or non-prime attribute.
8. Advantages of Normalisation
1. Normalisation helps to minimise data redundancy.
2. Greater overall database organisation.
3. Data consistency is maintained in DB.
```

</details>

## Interview Q&A
- **Q:** What problem does normalization solve?
  **A:** It reduces redundancy and anomalies (update/insert/delete) by organizing data based on functional dependencies.
- **Q:** 3NF vs BCNF—when can BCNF be hard to achieve?
  **A:** BCNF requires every determinant to be a super key; in schemas with overlapping candidate keys (e.g., course-teacher-room), 3NF may be chosen to keep dependency preservation.
- **Q:** Give an example of a transitive dependency.
  **A:** Student(id, dept_id, dept_name): id -> dept_id and dept_id -> dept_name, so id transitively determines dept_name.
