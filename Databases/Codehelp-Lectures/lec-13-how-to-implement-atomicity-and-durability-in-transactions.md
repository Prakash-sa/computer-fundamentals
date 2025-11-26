# Lec-13: How to implement Atomicity and Durability in Transactions

## Quick Highlights
- Recovery mechanisms enforce atomicity/durability after crashes.
- Shadow-copy: work on a copy, flip db-pointer on commit; simple, low concurrency.
- Log-based recovery (WAL) tracks updates to enable undo/redo; checkpoints trim logs.
- Force vs non-force, steal vs no-steal buffer policies shape needed recovery actions.

## Diagram
```mermaid
flowchart TB
    DBPointer[db-pointer] --> Shadow[Shadow DB copy]
    DBPointer -.switch.-> NewCopy[New DB copy]
    NewCopy -->|write| Disk[(Disk pages)]
    NewCopy --> Commit[Commit]
    Commit -->|update pointer| DBPointer
```

## Full Notes
Use the highlights for a quick scan; expand below for the verbatim PDF text.
<details>
<summary>Show raw lecture notes</summary>

```text
1. Recovery Mechanism Component of DBMS supports atomicity and durability.
2. Shadow-copy scheme
1. Based on making copies of DB (aka, shadow copies).
2. Assumption only one Transaction (T) is active at a time.
3. A pointer called db-pointer is maintained on the disk; which at any instant points to current copy of DB.
4. T, that wants to update DB first creates a complete copy of DB.
5. All further updates are done on new DB copy leaving the original copy (shadow copy) untouched.
6. If at any point the T has to be aborted the system deletes the new copy. And the old copy is not aected.
7. If T success, it is committed as,
1. OS makes sure all the pages of the new copy of DB written on the disk.
2. DB system updates the db-pointer to point to the new copy of DB.
3. New copy is now the current copy of DB.
4. The old copy is deleted.
5. The T is said to have been COMMITTED at the point where the updated db-pointer is wri tten to disk.
8. Atomicity
1. If T fails at any time before db-pointer is updated, the old content of DB are not aected.
2. T abort can be done by just deleting the new copy of DB.
3. Hence, either all updates are reflected or none.
9. Durability
1. Suppose, system fails are any time before the updated db-pointer is wri tten to disk.
2. When the system restarts, it will read db-pointer & will thus, see the original content of DB and none of the e ects of T will
be visible.
3. T is assumed to be successful only when db-pointer is updated.
4. If system fails after db-pointer has been updated. Before that all the pages of the new copy were wri tten to disk. Hence,
when system restarts, it will read new DB copy.
10. The implementation is dependent on write to the db-pointer being atomic. Luckily, disk system provide atomic updates to entire
block or at least a disk sector. So, we make sure db-pointer lies entirely in a single sector. By storing db-pointer at the beginning
of a block.
11. Inecient, as entire DB is copied for every Transaction.
3. Log-based recovery methods
1. The log is a sequence of records. Log of each transaction is maintained in some stable storage so that if any failure occurs, then
it can be recovered from there.
2. If any operation is performed on the database, then it will be recorded in the log.
3. But the process of storing the logs should be done before the actual transaction is applied in the database.
4. Stable storage is a classification of computer data storage technology that guarantees atomicity for any given write operation
and allows software to be written that is robust against some hardware and power failures.
5. Deferred DB Modifications
1. Ensuring atomicity by recording all the DB modifications in the log but deferring the execution of all the write operations
until the final action of the T has been executed.
2. Log information is used to execute deferred writes when T is completed.
3. If system crashed before the T completes, or if T is aborted, the information in the logs are ignored.
4. If T completes, the records associated to it in the log file are used in executing the deferred writes.
5. If failure occur while this updating is taking place, we preform redo.
6. Immediate DB Modifications
1. DB modifications to be output to the DB while the T is still in active state.
2. DB modifications written by active T are called uncommitted modifications.
3. In the event of crash or T failure, system uses old value field of the log records to restore modi fied values.
4. Update takes place only after log records in a stable storage.
5. Failure handling
1. System failure before T completes, or if T aborted, then old value field is used to undo the T.
2. If T completes and system crashes, then new value field is used to redo T having commit logs in the logs.
```

</details>

## Interview Q&A
- **Q:** Contrast write-ahead logging with shadow paging.
  **A:** WAL appends log records before data writes, supporting concurrency; shadow paging copies pages and flips pointers, simpler but less concurrent and copy-heavy.
- **Q:** What does 'force' vs 'steal' buffer policy mean?
  **A:** Force writes dirty pages at commit; steal allows flushing uncommitted pages. Steal/no-force is common and requires UNDO/REDO logging.
- **Q:** How would you test crash recovery?
  **A:** Simulate crashes mid-transaction, restart the DB, and verify committed data persists while uncommitted changes roll back according to the log.
