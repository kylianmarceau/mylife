---
tags:
  - operating-systems
---

# Process Synchronization

**Subject**: CSC3002F Operating Systems  
**Source**: `CSC3002F_MK_3_ProcessSynchronization_v2.pdf`, Michelle Kuttel, pages 1-68  
**Generated**: 2026-06-03

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Concurrency, Races, And Synchronization Constraints|Concurrency, Races, And Synchronization Constraints]]
  - [[#Liveness Problems|Liveness Problems]]
  - [[#Classic Synchronization Problems|Classic Synchronization Problems]]
  - [[#Hardware Atomic Instructions|Hardware Atomic Instructions]]
  - [[#Mutex Locks And Spinlocks|Mutex Locks And Spinlocks]]
  - [[#Semaphores|Semaphores]]
  - [[#Semaphores For Signaling, Rendezvous, Barriers, And Producer-Consumer|Semaphores For Signaling, Rendezvous, Barriers, And Producer-Consumer]]
  - [[#Readers-Writers And Starvation|Readers-Writers And Starvation]]
  - [[#Dining Philosophers|Dining Philosophers]]
  - [[#Common Semaphore Errors|Common Semaphore Errors]]
  - [[#Monitors, Condition Variables, And Java Synchronization|Monitors, Condition Variables, And Java Synchronization]]
  - [[#Linux Synchronization|Linux Synchronization]]

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
