---
tags:
  - operating-systems
---

# Deadlock

**Subject**: CSC3002F Operating Systems  
**Source**: `CSC3002F_MK_4_Deadlock_v2.pdf`, Michelle Kuttel, pages 1-71  
**Generated**: 2026-06-03

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Correctness Properties And Deadlock Definition|Correctness Properties And Deadlock Definition]]
  - [[#Four Necessary Conditions|Four Necessary Conditions]]
  - [[#Resource-Allocation Graphs|Resource-Allocation Graphs]]
  - [[#Handling Deadlocks|Handling Deadlocks]]
  - [[#Deadlock Prevention|Deadlock Prevention]]
  - [[#Deadlock Avoidance And Safe States|Deadlock Avoidance And Safe States]]
  - [[#Resource-Allocation Graph Avoidance|Resource-Allocation Graph Avoidance]]
  - [[#Banker's Algorithm: Data Structures|Banker's Algorithm: Data Structures]]
  - [[#Banker's Algorithm: Safety Check|Banker's Algorithm: Safety Check]]
  - [[#Banker's Algorithm: Resource-Request Check|Banker's Algorithm: Resource-Request Check]]
  - [[#Detection And Recovery|Detection And Recovery]]

---

## Core Content

### Correctness Properties And Deadlock Definition

#### Definitions

> **Safety Property**: A property that must always be true.

> **Liveness Property**: A property that must eventually become true.

> **Deadlock**: A set of threads/processes is deadlocked when every member waits for an event that can be caused only by another member of the set.

> **Resource**: A finite system item used by processes/threads, such as CPU cycles, files, I/O devices, locks, semaphores, memory, disk blocks, or buffer space.

Deadlock is broader than locks and condition variables. It can happen anywhere a thread waits for an event that cannot happen because of a cycle of waiting for resources. Resources include locks, memory, processing time, disk blocks, buffer slots, files, and I/O devices.

A process/thread uses a resource in this sequence:

1. Request.
2. Use.
3. Release.

Testing may not discover deadlock because deadlock can depend on unlucky interleavings or particular workloads. Systems should be designed to be deadlock-free or to handle deadlock deliberately.



### Four Necessary Conditions

#### Definitions

> **Mutual Exclusion**: At least one resource can be used by only one process at a time.

> **Hold And Wait**: A process holds at least one resource while waiting to acquire additional resources held by others.

> **No Preemption**: A resource can be released only voluntarily by the process holding it.

> **Circular Wait**: A cycle of processes exists where each waits for a resource held by the next process in the cycle.

All four conditions must hold simultaneously for deadlock:

| Condition | Why It Matters |
|---|---|
| Mutual exclusion | If every resource were shareable, waiting for exclusive access would not arise |
| Hold and wait | If processes never held while waiting, cycles are harder to form |
| No preemption | If resources could be forcibly taken, a wait could be broken |
| Circular wait | The actual cycle that prevents progress |

Formal circular wait:

$$
P_0\rightarrow P_1\rightarrow \cdots \rightarrow P_n\rightarrow P_0
$$

where $P_i$ waits for a resource held by the next process.
### Resource-Allocation Graphs

#### Definitions

> **Resource-Allocation Graph (RAG)**: Directed graph with process nodes, resource-type nodes, request edges, and assignment edges.

> **Request Edge**: Edge $P_i \rightarrow R_j$ showing process $P_i$ is waiting for resource $R_j$.

> **Assignment Edge**: Edge $R_j \rightarrow P_i$ showing an instance of resource $R_j$ is allocated to process $P_i$.

<svg width="100%" viewBox="0 0 520 420" role="img">
<title>Resource-Allocation Graph</title>
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<rect x="120" y="20" width="44" height="36" rx="3" fill="none" stroke="#888" stroke-width="1.4"/>
<circle cx="132" cy="36" r="4" fill="#888"/>
<circle cx="152" cy="36" r="4" fill="#888"/>
<text x="142" y="68" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">R₁</text>
<text x="142" y="82" text-anchor="middle" font-size="10" fill="#4a90d9" font-family="sans-serif">(resource type)</text>
<rect x="310" y="20" width="44" height="36" rx="3" fill="none" stroke="#888" stroke-width="1.4"/>
<circle cx="322" cy="36" r="4" fill="#888"/>
<circle cx="342" cy="36" r="4" fill="#888"/>
<text x="332" y="68" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">R₃</text>
<circle cx="142" cy="170" r="22" fill="none" stroke="#4a90d9" stroke-width="1.4"/>
<text x="142" y="175" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">P₁</text>
<text x="80" y="175" text-anchor="middle" font-size="10" fill="#4a90d9" font-family="sans-serif">(process)</text>
<circle cx="262" cy="170" r="22" fill="none" stroke="#4a90d9" stroke-width="1.4"/>
<text x="262" y="175" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">P₂</text>
<circle cx="370" cy="170" r="22" fill="none" stroke="#4a90d9" stroke-width="1.4"/>
<text x="370" y="175" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">P₃</text>
<rect x="218" y="270" width="44" height="44" rx="3" fill="none" stroke="#888" stroke-width="1.4"/>
<circle cx="230" cy="285" r="4" fill="#888"/>
<circle cx="250" cy="285" r="4" fill="#888"/>
<circle cx="230" cy="303" r="4" fill="#888"/>
<circle cx="250" cy="303" r="4" fill="#888"/>
<text x="240" y="328" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">R₂</text>
<text x="240" y="342" text-anchor="middle" font-size="10" fill="#4a90d9" font-family="sans-serif">(multiple instances)</text>
<rect x="350" y="270" width="44" height="44" rx="3" fill="none" stroke="#888" stroke-width="1.4"/>
<circle cx="372" cy="292" r="4" fill="#888"/>
<circle cx="372" cy="308" r="4" fill="#888"/>
<text x="372" y="328" text-anchor="middle" font-size="12" fill="#888" font-family="sans-serif">R₄</text>
<line x1="136" y1="56" x2="142" y2="146" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="155" y1="56" x2="248" y2="152" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="338" y1="56" x2="374" y2="148" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="152" y1="188" x2="222" y2="268" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="256" y1="192" x2="248" y2="268" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="262" y1="270" x2="268" y2="194" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="378" y1="192" x2="378" y2="268" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="278" y1="155" x2="308" y2="48" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<line x1="30" y1="375" x2="70" y2="375" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<text x="78" y="379" font-size="10" fill="#888" font-family="sans-serif">request edge  (P to R)</text>
<line x1="270" y1="375" x2="310" y2="375" stroke="#888" stroke-width="1.2" marker-end="url(#arr)"/>
<text x="318" y="379" font-size="10" fill="#888" font-family="sans-serif">assignment edge  (R to P)</text>
<circle cx="41" cy="395" r="8" fill="none" stroke="#4a90d9" stroke-width="1.2"/>
<text x="78" y="399" font-size="10" fill="#888" font-family="sans-serif">process (circle)</text>
<rect x="262" y="387" width="16" height="16" rx="2" fill="none" stroke="#888" stroke-width="1.2"/>
<circle cx="267" cy="392" r="2.5" fill="#888"/>
<circle cx="273" cy="392" r="2.5" fill="#888"/>
<circle cx="267" cy="398" r="2.5" fill="#888"/>
<circle cx="273" cy="398" r="2.5" fill="#888"/>
<text x="286" y="399" font-size="10" fill="#888" font-family="sans-serif">resource type (dots = instances)</text>
</svg>

The graph has vertices:

$$
V=P\cup R
$$

where:

$$
P=\{P_1,P_2,\ldots,P_n\}
$$

is the set of processes and:

$$
R=\{R_1,R_2,\ldots,R_m\}
$$

is the set of resource types.

Rules:

1. When a process requests a resource, insert request edge $P_i\rightarrow R_j$.
2. When request is fulfilled, transform it into assignment edge $R_j\rightarrow P_i$.
3. When process releases the resource, delete the assignment edge.

Cycle interpretation:

| Graph State | Meaning |
|---|---|
| No cycle | No deadlock |
| Cycle and one instance per resource type | Deadlock exists |
| Cycle and multiple instances per resource type | Deadlock is possible but not guaranteed |

For multiple instances, a cycle may be broken if another instance becomes available from outside the cycle.




### Handling Deadlocks

#### Definitions

> **Deadlock Prevention**: Structuring the system so at least one necessary deadlock condition cannot hold.

> **Deadlock Avoidance**: Dynamically deciding whether resource requests are safe before granting them.

> **Deadlock Detection**: Allowing deadlock to occur, then finding it.

> **Deadlock Recovery**: Breaking a detected deadlock.

Possible strategies:

| Strategy | Idea | Example |
|---|---|---|
| Ignore | Pretend deadlocks never occur | Common in Windows/Linux for many user-level deadlocks |
| Prevent | Ensure one necessary condition cannot hold | Resource ordering to break circular wait |
| Avoid | Stay out of unsafe states | Banker's Algorithm |
| Detect and recover | Allow, detect, then recover | Databases and transaction systems |

Undetected deadlock is bad because resources remain held by processes that cannot run, more processes block behind them, and eventually the system may stop functioning until manual restart.

Many general-purpose OSes do not solve all deadlocks globally because complete prevention/avoidance can reduce utilization, require advance information, and add overhead. They rely heavily on kernel/application developers to design correctly.
### Deadlock Prevention

#### Definitions

> **Resource Ordering**: Assigning a global order to resources and requiring all processes acquire resources in increasing order.

To prevent deadlock, break at least one necessary condition:

| Condition | Can We Remove It? | Notes |
|---|---|---|
| Mutual exclusion | Generally no | Safety often requires exclusive access |
| Hold and wait | Sometimes, but impractical | Low resource utilization and starvation risk |
| No preemption | Impractical for many resources | Some resources cannot safely be taken away |
| Circular wait | Often practical | Use global resource ordering |

Resource ordering example from the source: if a hash table has per-bucket locks and an operation moves an item from bucket $k_1$ to bucket $k_2$, always acquire the lower-numbered bucket lock before the higher-numbered one. Then no circular wait can form because all waits move in the same global direction.



### Deadlock Avoidance And Safe States

#### Definitions

> **Deadlock Avoidance**: Ensuring the system never enters an unsafe state by using advance resource-request information.

> **Safe State**: A state where there exists an order in which all processes can finish.

> **Unsafe State**: A state where no safe sequence is guaranteed.

> **Safe Sequence**: An ordering of all processes such that each can obtain needed resources from currently available resources plus resources released by earlier processes.

A state is safe if there exists:

$$
\langle P_1,P_2,\ldots,P_n\rangle
$$

such that for each $P_i$, its remaining resource needs can be satisfied by:

$$
\text{Available}+\sum_{j<i}\text{Allocation}_{P_j}
$$

If $P_i$ cannot be satisfied immediately, it can wait until all earlier $P_j$ finish and release resources. If the system is safe, no deadlock occurs. If unsafe, deadlock is possible.

Avoidance rule:

1. A process requests a currently available resource.
2. The system pretends to grant it.
3. The system checks whether the resulting state is safe.
4. If safe, grant; if unsafe, make the process wait and restore old state.

This can lower resource utilization because an available resource may still be withheld.


### Resource-Allocation Graph Avoidance

#### Definitions

> **Claim Edge**: Dashed edge $P_i\rightarrow R_j$ showing that process $P_i$ may request resource $R_j$ in the future.

For a single instance of each resource type, avoidance can use a RAG variant with claim edges:

1. Each process declares maximum resource use in advance.
2. Claim edge converts to request edge when the process requests the resource.
3. Request edge converts to assignment edge when resource is allocated.
4. Assignment edge reconverts to claim edge on release.

Granting rule:

$$
\text{grant request only if converting request edge to assignment edge creates no cycle}
$$

Cycle detection costs about:

$$
O(n^2)
$$

where $n$ is the number of threads/processes.
### Banker's Algorithm: Data Structures

#### Definitions

> **Banker's Algorithm**: Deadlock-avoidance algorithm for multiple instances of resource types using declared maximum demands.

> **Available Vector**: Vector of currently available instances for each resource type.

> **Max Matrix**: Matrix of each process's maximum declared demand for each resource type.

> **Allocation Matrix**: Matrix of current allocation to each process.

> **Need Matrix**: Matrix of remaining possible need for each process.

For $n$ threads/processes and $m$ resource types:

| Structure | Size | Meaning |
|---|---:|---|
| `Available` | $m$ | `Available[j] = k` means $k$ instances of $R_j$ are free |
| `Max` | $n\times m$ | `Max[i,j] = k` means $P_i$ may request at most $k$ of $R_j$ |
| `Allocation` | $n\times m$ | `Allocation[i,j] = k` means $P_i$ currently holds $k$ of $R_j$ |
| `Need` | $n\times m$ | `Need[i,j] = k` means $P_i$ may need $k$ more of $R_j$ |

Core formula:

$$
\text{Need}[i,j]=\text{Max}[i,j]-\text{Allocation}[i,j]
$$

The algorithm assumes each process declares maximum resource needs in advance and returns resources in finite time after receiving what it needs.
### Banker's Algorithm: Safety Check

To determine whether a state is safe:

1. Initialize:

$$
\text{Work}=\text{Available}
$$

$$
\text{Finish}[i]=\text{false}\quad\text{for all }i
$$

2. Find an $i$ such that:

$$
\text{Finish}[i]=\text{false}
$$

and:

$$
\text{Need}_i\le \text{Work}
$$

where comparison is componentwise.

3. If found, pretend $P_i$ finishes:

$$
\text{Work}=\text{Work}+\text{Allocation}_i
$$

$$
\text{Finish}[i]=\text{true}
$$

Then go back to step 2.

4. If all `Finish[i]` are true, the system is safe. Otherwise it is unsafe.

Time complexity is on the order of:

$$
O(mn^2)
$$
### Banker's Algorithm: Resource-Request Check

#### Definitions

> **Request Vector**: Vector `Request_i` where `Request_i[j] = k` means process $P_i$ asks for $k$ instances of $R_j$.

For a request by process $P_i$:

1. Check that the process did not exceed its declared maximum:

$$
\text{Request}_i\le \text{Need}_i
$$

If false, raise an error.

2. Check that resources are currently available:

$$
\text{Request}_i\le \text{Available}
$$

If false, $P_i$ must wait.

3. Pretend to allocate:

$$
\text{Available}=\text{Available}-\text{Request}_i
$$

$$
\text{Allocation}_i=\text{Allocation}_i+\text{Request}_i
$$

$$
\text{Need}_i=\text{Need}_i-\text{Request}_i
$$

4. Run the safety check.

5. If safe, grant. If unsafe, restore old state and make $P_i$ wait.
### Detection And Recovery

#### Definitions

> **Wait-For Graph**: Graph containing process nodes only, with $P_i\rightarrow P_j$ if $P_i$ waits for $P_j$.

> **Victim**: Process selected to abort or roll back during recovery.

> **Rollback**: Returning a process/system to a previous safe state.

> **Transaction**: Operation sequence that either commits completely or aborts as if it did not happen.

For single-instance resources, detection can maintain a wait-for graph and periodically search for cycles. A cycle means deadlock. Cycle search is about:

$$
O(n^2)
$$

For multiple-instance resources, detection uses an algorithm similar to Banker's Algorithm, costing about:

$$
O(mn^2)
$$

Recovery options:

| Option | Description |
|---|---|
| Abort all deadlocked processes | Fast but expensive/disruptive |
| Abort one at a time | Repeat until cycle eliminated |
| Rollback | Return selected victims to a safe checkpoint |
| Restart | Restart victim process after rollback/abort |

Victim selection should minimize cost. Cost may include priority, work done, resources held, resources still needed, and number of previous rollbacks. If the same process is always selected, recovery itself can cause starvation.

Transactions in file systems and databases support recovery because they can abort/roll back cleanly. The source's Amazon-style example illustrates timeout-based design: if inventory server is unavailable, the frontend can complete/queue the order and send an apology later rather than hang indefinitely.

Java does not provide explicit deadlock detection support, but a thread dump can help analyze a running program. Command:

```sh
jstack -l <pid>
```

shows thread states and locking information, including which locks blocked threads are waiting to acquire.
