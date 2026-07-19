# Process Synchronization

**Subject**: CSC3002F Operating Systems  
**Source**: `CSC3002F_MK_3_ProcessSynchronization_v2.pdf`, Michelle Kuttel, pages 1-68  
**Generated**: 2026-06-03

---

## Core Content

### Concurrency, Races, And Synchronization Constraints

#### Definitions

> **Concurrent Events**: Events where we cannot tell which will happen first.

> **Race Condition**: Correctness depends on timing or interleaving.

> **Data Race**: Unsynchronized concurrent access to the same memory location, with at least one write.

> **Synchronization Constraint**: A requirement about the order of events or access to shared state.

> **Mutual Exclusion**: A constraint that only one thread/process may execute a critical section at a time.

> **Atomic Operation**: An operation that executes indivisibly, with no visible intermediate state.

Operating systems are highly concurrent. Multiple processes/threads may interact with shared memory, run at arbitrary speeds, and suffer unpredictable delays from cache misses, page faults, and scheduler preemption. Maintaining data consistency requires synchronization mechanisms supplied by hardware, the OS, and programming languages.

The programmer is responsible for specifying the needed constraints; the compiler cannot infer which interleavings are allowed.

Synchronization constraints in the source:

| Constraint | Meaning |
|---|---|
| Signaling | Event $a_1$ must happen before event $b_1$ |
| Rendezvous | $a_1$ before $b_2$ and $b_1$ before $a_2$ |
| Barrier | All threads wait until all arrive |
| Reusable barrier | Barrier can be used more than once |
| Mutex | Critical section has one thread at a time |
| Multiplex | Critical section permits at most $n$ threads |




### Liveness Problems

#### Definitions

> **Liveness**: The requirement that processes/threads eventually make progress.

> **Deadlock**: Two or more threads permanently wait for each other, so none progresses.

> **Starvation**: A thread waits indefinitely because others keep getting the resource.

> **Livelock**: Threads keep changing state in response to each other but make no useful progress.

Key distinction:

| Problem | System Activity | Progress? |
|---|---|---|
| Deadlock | Threads stuck/inactive | No one in the cycle progresses |
| Starvation | Other threads may progress | One thread is continually denied |
| Livelock | Threads keep running/changing state | No useful progress |

Synchronization often fixes safety problems but can introduce liveness problems.
### Classic Synchronization Problems

#### Definitions

> **Producer-Consumer / Bounded Buffer Problem**: Producers add items to a buffer and consumers remove them, while respecting empty/full and mutual-exclusion constraints.

> **Readers-Writers Problem**: Many readers may read shared data concurrently, but writers need exclusive access.

> **Dining Philosophers Problem**: Philosophers need two neighboring chopsticks to eat, illustrating deadlock/starvation risks.

Producer-consumer constraints:

1. The shared buffer must be protected with mutual exclusion.
2. Consumers cannot consume from an empty buffer.
3. Producers cannot add to a full bounded buffer.

Readers-writers constraints:

| Requirement | Meaning |
|---|---|
| Concurrent readers allowed | Many readers may be in the critical section |
| Writer exclusion | A writer must be alone |
| Policy variants | Reader preference, writer preference, or fair/no-starvation |

Dining philosophers illustrates how each philosopher can hold one chopstick while waiting for another, creating deadlock. Deadlock freedom alone does not imply starvation freedom.


### Hardware Atomic Instructions

#### Definitions

> **test-and-set()**: Atomic instruction that reads a Boolean and sets it to true in one indivisible action.

> **compare-and-swap() (CAS)**: Atomic instruction that changes a value only if it still equals an expected value.

> **Atomic Variable**: A variable whose updates are guaranteed atomic.

Hardware atomic instructions are the base for locks and other synchronization tools.

Conceptual `test_and_set`:

```c
boolean test_and_set(boolean *target) {
    boolean rv = *target;
    *target = true;
    return rv;
}
```

Spinlock with `test_and_set`:

```c
do {
    while (test_and_set(&lock))
        ; // spin

    // critical section

    lock = false;

    // remainder section
} while (true);
```

Conceptual CAS:

```c
int compare_and_swap(int *value, int expected, int new_value) {
    int temp = *value;
    if (*value == expected)
        *value = new_value;
    return temp;
}
```

CAS spinlock:

```c
while (true) {
    while (compare_and_swap(&lock, 0, 1) != 0)
        ; // spin

    // critical section

    lock = 0;

    // remainder section
}
```

Atomic variables solve atomic updates of a single variable, but do not automatically protect compound invariants across multiple variables.
### Mutex Locks And Spinlocks

#### Definitions

> **Mutex Lock**: A lock that enforces mutual exclusion with `acquire()` and `release()`.

> **Spinlock**: A lock where waiting threads busy-wait until the lock is available.

> **Busy Waiting**: Repeatedly checking a condition until it changes.

> **Contended Lock**: A lock where at least one thread blocks or waits trying to acquire it.

Conceptual mutex:

```c
acquire() {
    while (!available)
        ; // busy wait
    available = false;
}

release() {
    available = true;
}
```

Real `acquire()` and `release()` must be atomic, usually implemented with hardware atomic instructions.

Busy waiting trade-off:

| Disadvantage | Advantage |
|---|---|
| Wastes CPU cycles | Avoids context-switch overhead |

Spinlocks are useful on multiprocessor systems when a lock is held for less than about two context switches. One core can spin while another core quickly exits the critical section. High lock contention reduces overall concurrent performance.
### Semaphores

#### Definitions

> **Semaphore**: An integer synchronization variable accessed only through atomic `wait()` and `signal()` operations.

> **wait() / P() / acquire()**: Semaphore operation that decrements or waits for a permit.

> **signal() / V() / release()**: Semaphore operation that increments and may wake a waiter.

> **Binary Semaphore**: Semaphore restricted to values $0$ and $1$.

> **Counting Semaphore**: Semaphore with an unrestricted integer value.

Naive semaphore concept:

```c
wait(S) {
    while (S <= 0)
        ; // busy wait
    S = S - 1;
}

signal(S) {
    S = S + 1;
}
```

Practical OS/Java semaphores usually block waiting threads rather than spin. The original semaphore definition does not allow reading the current value, although Java exposes some introspection.

Semaphore meanings:

| Value | Meaning |
|---:|---|
| Positive | Number of permits available |
| Zero | No permits; waiters block |

For a multiplex allowing at most $n$ threads, initialize the semaphore to $n$.

Implementation without busy waiting uses:

| Operation | Meaning |
|---|---|
| `block()` | Place invoking process on semaphore waiting queue |
| `wakeup(P)` | Remove a process from waiting queue and place it in ready queue |
### Semaphores For Signaling, Rendezvous, Barriers, And Producer-Consumer

#### Definitions

> **Circular Buffer**: Buffer with logical pointers `in` and `out` that wrap around modulo the buffer size.

> **Full Slot Semaphore**: Semaphore counting occupied buffer slots.

> **Empty Slot Semaphore**: Semaphore counting free buffer slots.

Signaling with semaphore initialized to $0$:

```text
Thread A:           Thread B:
a1                  wait(sem)
signal(sem)         b1
```

This forces $a_1$ before $b_1$.

Producer-consumer semaphore solution:

```c
// Shared:
// mutex = 1, full = 0, empty = n

producer:
while (true) {
    produce item;
    wait(empty);
    wait(mutex);
    add item to buffer;
    signal(mutex);
    signal(full);
}

consumer:
while (true) {
    wait(full);
    wait(mutex);
    remove item from buffer;
    signal(mutex);
    signal(empty);
    consume item;
}
```

| Semaphore | Initial Value | Purpose |
|---|---:|---|
| `mutex` | $1$ | Mutual exclusion on buffer structure |
| `full` | $0$ | Number of full slots |
| `empty` | $n$ | Number of empty slots |

Order matters. A producer must wait for an empty slot before entering the buffer update, then signal full after insertion. A consumer must wait for full before entering the buffer update, then signal empty after removal.


### Readers-Writers And Starvation

#### Definitions

> **Reader Preference**: Readers are not kept waiting unless a writer already has permission to write.

> **Writer Preference**: Once a writer is ready, it writes as soon as possible.

> **Lightswitch Pattern**: A pattern where the first entrant locks a shared resource and the last leaver unlocks it.

Reader-preference semaphore solution:

```c
// shared:
// rw_mutex = 1
// mutex = 1
// read_count = 0

writer:
while (true) {
    wait(rw_mutex);
    write;
    signal(rw_mutex);
}

reader:
while (true) {
    wait(mutex);
    read_count++;
    if (read_count == 1)
        wait(rw_mutex);
    signal(mutex);

    read;

    wait(mutex);
    read_count--;
    if (read_count == 0)
        signal(rw_mutex);
    signal(mutex);
}
```

This allows concurrent readers and writer exclusion, but writers may starve if readers keep arriving. A fair solution needs queueing or fair semaphore behavior so a hungry writer or reader cannot be postponed forever.


### Dining Philosophers

#### Definitions

> **Deadlock Freedom**: Guarantee that the system cannot reach a state where all relevant threads are permanently stuck.

> **Starvation Freedom**: Guarantee that every waiting/hungry thread eventually gets a turn.

Naive dining philosophers:

```c
do {
    wait(chopstick[i]);
    wait(chopstick[(i + 1) % 5]);

    eat;

    signal(chopstick[i]);
    signal(chopstick[(i + 1) % 5]);

    think;
} while (true);
```

Problem: if every philosopher picks up one chopstick and waits for the next, the system deadlocks.

Standard deadlock-avoidance solutions:

1. Allow at most $4$ philosophers at the table simultaneously.
2. Allow a philosopher to pick up chopsticks only if both are available, with pickup inside a critical section.
3. Use an asymmetric ordering: odd philosophers pick left then right; even philosophers pick right then left.

However, many deadlock-free solutions can still starve a philosopher. Starvation freedom requires fairness, such as queueing philosophers or fair semaphores.
### Common Semaphore Errors

Incorrect semaphore use can cause subtle timing bugs:

| Error | Result |
|---|---|
| Inverting `wait(mutex)` and `signal(mutex)` | Critical-section violation |
| Replacing `signal(mutex)` with `wait(mutex)` | Deadlock |
| Omitting `wait(mutex)` | Mutual-exclusion violation |
| Omitting `signal(mutex)` | Deadlock or permanent blocking |

Semaphores are powerful but low-level, so higher-level constructs such as monitors were created to reduce misuse.
### Monitors, Condition Variables, And Java Synchronization

#### Definitions

> **Monitor**: A high-level synchronization abstraction where internal variables are accessed only through monitor procedures and only one process is active in the monitor at a time.

> **Condition Variable**: A synchronization variable supporting `wait()` and `signal()`/notification for condition-based waiting.

> **Entry Set**: Java object set of threads waiting to acquire the object's lock.

> **Wait Set**: Java object set of threads that called `wait()` on the object.

Monitor structure:

```text
monitor monitor-name {
    shared variable declarations

    procedure P1(...) { ... }
    ...
    procedure Pn(...) { ... }

    initialization code(...) { ... }
}
```

Condition variable operations:

| Operation | Meaning |
|---|---|
| `x.wait()` | Suspend until signalled |
| `x.signal()` | Resume one waiting process, if any |

In Java:

- Every object has an intrinsic lock.
- A `synchronized` method requires the caller to own that object's lock.
- A thread calling `wait()` releases the lock, becomes blocked, and enters the object's wait set.
- A thread calling `notify()` moves an arbitrary waiting thread from wait set to entry set and marks it runnable.
- The awakened thread must reacquire the lock before continuing.

When using `wait()`, always check the condition in a loop:

```java
while (counter == 0) {
    this.wait();
}
```

Reasons:

1. Spurious wakeups can occur.
2. Another thread may change the state before the awakened thread reacquires the lock.

Java also provides atomic variables, semaphores, reentrant locks, condition variables, monitors, and concurrent collections. In practice, use well-tested concurrent data structures such as `BlockingQueue` when they match the problem.



### Linux Synchronization

#### Definitions

> **Fully Preemptive Kernel**: A kernel that can be preempted, creating potential kernel-level race conditions.

> **Reader-Writer Lock**: A lock allowing multiple readers or one writer.

Linux provides semaphores, atomic integers (`atomic_t`), mutex locks, spinlocks, and reader-writer versions of locks. Since Linux is fully preemptive, synchronization is required inside the kernel as well as in user programs.

## Worked Examples

### Example 1: Lost Update Race

**Problem**: Two threads both execute `counter = counter + 1` when `counter` is initially $0$. How can the final value be $1$?

**Step 1**: Thread A reads $0$.  
**Step 2**: Thread B reads $0$.  
**Step 3**: Thread A computes and writes $1$.  
**Step 4**: Thread B computes and writes $1$.  
**Answer**: Final value is $1$, not $2$, because the read-modify-write sequence was not atomic.

### Example 2: Producer-Consumer Semaphore Values

**Problem**: A bounded buffer has size $5$. What should `mutex`, `full`, and `empty` be initialized to?

**Step 1**: `mutex` protects buffer structure and starts available:

$$
\text{mutex}=1
$$

**Step 2**: No slots are full initially:

$$
\text{full}=0
$$

**Step 3**: All $5$ slots are empty:

$$
\text{empty}=5
$$

**Answer**: `mutex = 1`, `full = 0`, `empty = 5`.

### Example 3: Readers-Writers First And Last Reader

**Problem**: Why does only the first reader wait on `rw_mutex`, and only the last reader signal it?

**Step 1**: First reader changes `read_count` from $0$ to $1$ and locks `rw_mutex`, blocking writers.  
**Step 2**: Later readers increment `read_count` but do not need to lock `rw_mutex`; writer exclusion is already active.  
**Step 3**: Each reader decrements on exit.  
**Step 4**: The last reader changes `read_count` from $1$ to $0$ and releases `rw_mutex`.  
**Answer**: This allows reader concurrency while writers remain excluded whenever at least one reader is active.

### Example 4: Dining Philosophers Deadlock

**Problem**: Why can the naive algorithm deadlock?

**Step 1**: Each philosopher executes `wait(chopstick[i])` and succeeds.  
**Step 2**: Each philosopher then tries `wait(chopstick[(i+1)%5])`.  
**Step 3**: That second chopstick is held by the neighbor.  
**Step 4**: Nobody releases their first chopstick because each waits for the second.  
**Answer**: The philosophers form a circular wait, so all are deadlocked.

---

## Common Mistakes / Gotchas

- Assuming atomic variables solve every concurrency problem. They protect single-variable updates, not multi-variable invariants.
- Using `if` instead of `while` around Java `wait()`.
- Treating deadlock freedom as starvation freedom. They are different liveness guarantees.
- Forgetting to release a mutex/semaphore on all code paths.
- Acquiring resources in inconsistent orders.
- Using a spinlock for a long critical section on a single-core system, wasting CPU.
- Reading a semaphore's value for correctness decisions when the abstract semaphore model does not provide that operation.

---

## Summary / Cheat Sheet

| Term | Meaning |
|---|---|
| Race condition | Correctness depends on timing/interleaving |
| Data race | Unsynchronized same-location access with a write |
| Critical section | Code accessing shared state needing protection |
| Atomic | Indivisible operation |
| Mutex | One-at-a-time lock |
| Spinlock | Busy-waiting lock |
| Semaphore | Atomic permit counter with wait/signal |
| Binary semaphore | Semaphore with values $0$ or $1$ |
| Counting semaphore | Semaphore for multiple permits |
| Monitor | High-level synchronized abstraction |
| Condition variable | Wait/signal for condition-based waiting |
| BlockingQueue | Library data structure handling producer-consumer safely |

**Key Formulas**:

$$
\text{Multiplex initial permits}=n
$$

$$
\text{producer-consumer initial values: mutex}=1,\quad \text{full}=0,\quad \text{empty}=n
$$

$$
\text{buffer full when }(\text{in}+1)\bmod \text{BUFFER\_SIZE}=\text{out}
$$

**Key Takeaways**:

- Synchronization is about controlling interleavings and shared access.
- Hardware atomic instructions build locks, but application programmers usually use higher-level tools.
- Semaphores can express many patterns but are easy to misuse.
- Monitors and condition variables make shared-state synchronization more structured.
- Fairness matters: a solution can avoid deadlock yet still starve a thread.

---

## Practice Questions

**Q1**: Distinguish race condition and data race.  
> Answer: A race condition is any correctness dependence on timing/interleaving. A data race is a specific unsynchronized concurrent access to the same memory location with at least one write.

**Q2**: Why does producer-consumer need three semaphores in the standard solution?  
> Answer: `mutex` protects buffer updates, `full` counts items available to consume, and `empty` counts free spaces available to produce into.

**Q3**: Why should Java `wait()` be inside a `while` loop?  
> Answer: Because of spurious wakeups and because another thread may change the condition before the awakened thread reacquires the lock.

**Q4**: Give one deadlock-free dining philosophers strategy and explain why it works.  
> Answer: Allow at most four philosophers at the table. With five chopsticks and only four philosophers competing, at least one philosopher can acquire two chopsticks and eventually release them, preventing a full circular wait.
