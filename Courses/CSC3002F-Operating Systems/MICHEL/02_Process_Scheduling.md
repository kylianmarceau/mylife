# Process Scheduling

**Subject**: CSC3002F Operating Systems  
**Source**: `CSC3002F_MK_2_ProcessScheduling_v3.pdf`, Michelle Kuttel, pages 1-52  
**Generated**: 2026-06-03

---

## Core Content

### Scheduling Basics, Bursts, And Preemption

#### Definitions

> **Processor Scheduling Policy**: The rule deciding which runnable thread/process runs next.

> **Ready Queue**: The collection of schedulable tasks/threads ready to execute.

> **CPU Burst**: A period during which a process/thread uses the CPU before blocking or yielding.

> **I/O-Bound Process**: A process with many short CPU bursts and frequent I/O waits.

> **CPU-Bound Process**: A process with few long CPU bursts.

> **Preemptive Scheduling**: Scheduling where the OS can take the CPU away from a running process.

> **Non-Preemptive / Cooperative Scheduling**: Scheduling where a process keeps the CPU until it blocks, yields, or terminates.

Modern OSes schedule kernel-level threads, but the slides use "process scheduling" and "thread scheduling" interchangeably.

The ready queue can be implemented as:

| Ready Queue Structure | Example Use |
|---|---|
| FIFO queue | FCFS/RR style algorithms |
| Priority queue | Windows-style priority scheduling |
| Tree | Linux CFS uses red-black trees |
| Unordered linked list | Simple conceptual queue |

Scheduling may occur when a process changes:

1. Running $\rightarrow$ waiting, such as I/O start.
2. Running $\rightarrow$ ready, such as timer interrupt/preemption.
3. Waiting $\rightarrow$ ready, such as I/O completion.
4. Running $\rightarrow$ terminated.

If scheduling happens only in cases 1 and 4, it is non-preemptive. Modern OS scheduling is preemptive, which improves responsiveness but introduces concurrency hazards because shared data can be interrupted mid-update.



### Context Switches And Scheduling Criteria

#### Definitions

> **Voluntary Context Switch**: A switch where a process gives up the CPU because it needs an unavailable resource.

> **Nonvoluntary Context Switch**: A switch where the CPU is taken from a process, such as time-slice expiry or higher-priority preemption.

> **CPU Utilization**: Fraction of time the CPU is busy.

> **Throughput**: Number of processes completed per unit time.

> **Turnaround Time**: Time from process submission to completion.

> **Waiting Time**: Total time a process spends waiting in the ready queue.

> **Response Time**: Time from request submission until first response.

> **Starvation**: Indefinite waiting because a process is continually denied CPU/resource access.

Linux reports context switches through tools such as `vmstat` and `/proc/<pid>/status`. The `/proc` status file can include `voluntary_ctxt_switches` and `nonvoluntary_ctxt_switches`.

Scheduling criteria:

| Criterion | Goal |
|---|---|
| CPU utilization | Maximize |
| Throughput | Maximize |
| Turnaround time | Minimize |
| Waiting time | Minimize |
| Response time | Minimize, especially for interactive systems |
| Fairness | Give runnable tasks reasonable CPU share |
| Starvation freedom / bounded waiting | No task waits forever |
| Predictability / low jitter | Keep response-time variation low |
| Scheduler overhead | Keep scheduling/context-switch cost low |

Interactive systems may prefer predictable response time over the absolute lowest average response time.
### Evaluating Scheduling Algorithms

#### Definitions

> **Deterministic Evaluation**: Comparing algorithms on a fixed scenario with exact numbers.

> **Queueing Model**: Probabilistic performance model based on arrival and service rates.

> **Simulation**: Programmed model generating arrivals, bursts, and departures to measure an algorithm.

> **Little's Law**: In steady state, average queue length equals arrival rate times average waiting time.

Little's Law:

$$
L=\lambda W
$$

where:

| Symbol | Meaning |
|---|---|
| $L$ | Average queue length |
| $\lambda$ | Average arrival rate |
| $W$ | Average waiting time in queue/system |

Example:

$$
\lambda=2\ \text{customers/minute},\quad W=5\ \text{minutes}
$$

$$
L=2\times5=10
$$
### First-Come, First-Served (FCFS)

#### Definitions

> **First-Come, First-Served (FCFS)**: Non-preemptive scheduling where the process at the head of the FIFO ready queue runs next.

> **Convoy Effect**: Short processes wait behind a long process, hurting response and utilization.

FCFS uses a FIFO queue. Arriving process PCBs are added to the end; the process at the head gets the CPU.

| Property | FCFS |
|---|---|
| Preemptive? | No |
| Strength | Simple and fair by arrival order |
| Weakness | Long average waiting/response time; convoy effect |

Example from the source:

| Process | Burst |
|---|---:|
| $P_1$ | $24$ |
| $P_2$ | $3$ |
| $P_3$ | $3$ |

If arrival order is $P_1,P_2,P_3$, waiting times are:

$$
W_{P_1}=0,\quad W_{P_2}=24,\quad W_{P_3}=27
$$

$$
\text{average waiting time}=\frac{0+24+27}{3}=17
$$

If arrival order is $P_2,P_3,P_1$:

$$
W_{P_2}=0,\quad W_{P_3}=3,\quad W_{P_1}=6
$$

$$
\text{average waiting time}=\frac{0+3+6}{3}=3
$$

Same burst times, different arrival order, very different waiting time.
### Shortest-Job-First (SJF) And Shortest-Remaining-Time-First

#### Definitions

> **Shortest-Job-First (SJF)**: Scheduling that chooses the process with the shortest next CPU burst.

> **Shortest-Remaining-Time-First (SRTF)**: Preemptive SJF where a newly arrived shorter remaining burst can preempt the current process.

> **Exponential Averaging**: Predicting the next CPU burst from the previous actual burst and previous prediction.

SJF is provably optimal for minimum average waiting time for a fixed set of processes if exact next CPU bursts are known. Exact implementation is impossible because the OS cannot know the future burst length. It predicts.

Prediction formula:

$$
\tau_{n+1}=\alpha t_n+(1-\alpha)\tau_n
$$

where:

| Symbol | Meaning |
|---|---|
| $\tau_{n+1}$ | Predicted next CPU burst |
| $t_n$ | Actual most recent CPU burst |
| $\tau_n$ | Previous prediction |
| $\alpha$ | Weighting factor, often $0.5$ |

Expanded:

$$
\tau_{n+1}=\alpha t_n+(1-\alpha)\alpha t_{n-1}+\cdots+(1-\alpha)^{n+1}\tau_0
$$

If $\alpha=0$, recent bursts are ignored. If $\alpha=1$, only the most recent actual burst counts.

Source SJF example:

| Process | Burst |
|---|---:|
| $P_1$ | $6$ |
| $P_2$ | $8$ |
| $P_3$ | $7$ |
| $P_4$ | $3$ |

SJF order: $P_4,P_1,P_3,P_2$. Waiting times:

$$
W_{P_4}=0,\quad W_{P_1}=3,\quad W_{P_3}=9,\quad W_{P_2}=16
$$

$$
\text{average waiting time}=\frac{0+3+9+16}{4}=7
$$

SJF can be preemptive or non-preemptive. With arrivals:

| Process | Arrival | Burst |
|---|---:|---:|
| $P_1$ | $0$ | $8$ |
| $P_2$ | $1$ | $4$ |
| $P_3$ | $2$ | $9$ |
| $P_4$ | $3$ | $5$ |

The source gives preemptive SJF average waiting time:

$$
\frac{(10-1)+(1-1)+(17-2)+(5-3)}{4}=6.5
$$

and compares non-preemptive SJF at $7.75$ and FCFS at $8.75$.



### Round-Robin (RR)

#### Definitions

> **Round-Robin (RR)**: Preemptive scheduling where each process receives up to one time quantum, then returns to the end of the ready queue if unfinished.

> **Time Quantum**: The maximum CPU time slice a process receives before preemption.

RR is like FCFS with preemption. The ready queue is treated as circular. A timer interrupt fires every quantum. If a CPU burst finishes before the quantum, the process voluntarily releases the CPU.

For $N$ ready processes and time quantum $q$, each process gets approximately:

$$
\frac{1}{N}
$$

of CPU time in chunks of at most $q$ time units.

Quantum trade-off:

| Quantum Size | Effect |
|---|---|
| Very large | RR approaches FCFS |
| Very small | Too many context switches; overhead high |
| Good practical value | Large relative to context-switch time and often larger than most CPU bursts |

Rule of thumb from the source: about $80\%$ of CPU bursts should be shorter than the time quantum.

Source RR example with $q=4$:

| Process | Burst |
|---|---:|
| $P_1$ | $24$ |
| $P_2$ | $3$ |
| $P_3$ | $3$ |

Waiting times from the source visualization:

$$
W_{P_1}=6,\quad W_{P_2}=4,\quad W_{P_3}=7
$$

$$
\text{average waiting time}=\frac{6+4+7}{3}=\frac{17}{3}=5.66
$$

RR often improves response time but may have higher waiting/turnaround time than SJF.



### Priority, Multilevel Queue, And Multilevel Feedback Queue

#### Definitions

> **Priority Scheduling**: Scheduling where each process has a priority and the highest-priority process runs next.

> **Aging**: Gradually increasing a waiting process's priority to prevent starvation.

> **Multilevel Queue Scheduling**: Scheduling with separate queues for classes or priorities, where a process stays in its assigned queue.

> **Multilevel Feedback Queue Scheduling**: Scheduling where processes can move between queues based on behavior.

Priority scheduling can be preemptive or non-preemptive. Priorities may be internal, such as predicted burst, memory needs, I/O behavior, or job type; or external, such as user importance. SJF is a form of priority scheduling where priority is inverse predicted next CPU burst length.

Problem: starvation. Solution: aging.

Multilevel queues can partition by priority or process type, such as foreground and background. Each queue may have its own algorithm, e.g. foreground RR and background FCFS. Scheduling between queues can be fixed-priority or time-sliced, e.g. $80\%$ CPU to foreground and $20\%$ to background.

Multilevel feedback queues allow upgrading and demoting:

| Parameter | Meaning |
|---|---|
| Number of queues | How many levels exist |
| Algorithm per queue | RR, FCFS, etc. |
| Upgrade rule | When long-waiting lower-priority tasks move up |
| Demotion rule | When CPU-heavy tasks move down |
| Entry rule | Which queue a new task enters |

Summary comparison from the source:

| Algorithm | Preemptive? | Strength | Weakness |
|---|---|---|---|
| FCFS | No | Simple, fair by arrival | Poor response time |
| SJF | Either | Best average waiting time | Needs burst prediction |
| RR | Yes | Good responsiveness | More overhead |
| Priority | Either | Expresses importance | Starvation |
| Multilevel queue | Usually mixed | Supports workload classes | Starvation |



### Linux Completely Fair Scheduler (CFS)

#### Definitions

> **Completely Fair Scheduler (CFS)**: Linux scheduler that allocates CPU proportionally using virtual runtime rather than a fixed time quantum.

> **Scheduling Class**: A category of tasks with a priority ordering.

> **Nice Value**: Linux user-visible priority adjustment from $-20$ to $+19$, where lower is higher priority.

> **Targeted Latency**: Time interval in which every runnable task should run at least once.

> **Virtual Runtime (`vruntime`)**: Runtime scaled by task weight/nice value.

> **Red-Black Tree**: A self-balancing binary search tree.

Standard Linux kernels have a default scheduling class and a higher-priority real-time scheduling class. The scheduler picks a task from the highest-priority class first.

CFS does not use a traditional fixed time quantum. It computes a share of CPU time from targeted latency and each task's nice-derived weight. For nice $0$:

$$
\text{vruntime}=\text{actual runtime}
$$

Higher-priority tasks accumulate `vruntime` more slowly; lower-priority tasks accumulate it faster. CFS stores runnable tasks in a red-black tree keyed by `vruntime` and picks the leftmost node, the task with smallest virtual runtime.



### Multicore Scheduling, SMT, Load Balancing, And Affinity

#### Definitions

> **Multicore Processor**: A chip with multiple computing cores.

> **Asymmetric Multiprocessing**: One processor handles scheduling/I/O/system activities while others run user code.

> **Symmetric Multiprocessing (SMP)**: Each processor is self-scheduling.

> **Memory Stall**: Time a processor waits for memory data.

> **Chip Multithreading (CMT)**: Hardware supports multiple hardware threads per core so another can run during stalls.

> **Simultaneous Multithreading (SMT)**: A form of CMT where one core can run multiple hardware threads at once, such as Intel Hyper-Threading.

> **Load Balancing**: Moving work so processors have approximately equal load.

> **Processor Affinity**: Keeping a thread on the same processor/core to preserve cache locality.

> **Non-Uniform Memory Access (NUMA)**: Architecture where memory access time depends on which processor/socket owns the memory.

SMP may use one global ready queue or per-core run queues. A global queue is simpler but risks lock contention and races: two CPUs must not choose the same thread or lose a queued thread. Per-core queues scale better and preserve cache locality, but require load balancing.

Load-balancing approaches:

| Approach | Meaning |
|---|---|
| Push migration | A supervisor moves tasks from overloaded CPUs to idle/less-busy CPUs |
| Pull migration | An idle CPU takes work from a busy CPU |

Linux CFS uses both and is NUMA-aware. It defines scheduling domains and NUMA nodes, balancing within domains first and migrating across NUMA nodes mainly under severe imbalance.

Thread load combines priority and average CPU utilization. A high-priority I/O-bound thread can have low load; a low-priority CPU-bound thread can have similar load. Queue load is the sum of thread loads in the queue.


## Worked Examples

### Example 1: FCFS Waiting Time

**Problem**: Processes arrive as $P_1,P_2,P_3$ with bursts $24,3,3$. Compute average waiting time.

**Step 1**: Gantt order:

```text
0        24   27   30
|   P1   | P2 | P3 |
```

**Step 2**: Waiting times:

$$
W_{P_1}=0,\quad W_{P_2}=24,\quad W_{P_3}=27
$$

**Step 3**:

$$
\bar{W}=\frac{0+24+27}{3}=17
$$

**Answer**: Average waiting time is $17$ time units.

### Example 2: SJF Waiting Time

**Problem**: Bursts are $P_1=6$, $P_2=8$, $P_3=7$, $P_4=3$. Compute SJF waiting time.

**Step 1**: Sort by burst: $P_4,P_1,P_3,P_2$.  
**Step 2**: Waiting times:

$$
W_{P_4}=0,\quad W_{P_1}=3,\quad W_{P_3}=9,\quad W_{P_2}=16
$$

**Step 3**:

$$
\bar{W}=\frac{0+3+9+16}{4}=7
$$

**Answer**: Average waiting time is $7$.

### Example 3: Exponential Burst Prediction

**Problem**: Let $\alpha=0.5$, previous prediction $\tau_n=6$, and actual burst $t_n=10$. Predict the next burst.

**Step 1**:

$$
\tau_{n+1}=0.5(10)+(1-0.5)(6)
$$

**Step 2**:

$$
\tau_{n+1}=5+3=8
$$

**Answer**: Predicted next burst is $8$.

### Example 4: RR Turnaround Time

**Problem**: Source example with $q=3$: $P_1$ arrives $0$ burst $7$, $P_2$ arrives $2$ burst $4$, $P_3$ arrives $4$ burst $3$. Completion times from the source are $P_1=14$, $P_2=13$, $P_3=9$. Compute average turnaround time.

**Step 1**: Turnaround time:

$$
T_i=C_i-A_i
$$

**Step 2**:

$$
T_{P_1}=14-0=14
$$

$$
T_{P_2}=13-2=11
$$

$$
T_{P_3}=9-4=5
$$

**Step 3**:

$$
\bar{T}=\frac{14+11+5}{3}=10
$$

**Answer**: Average turnaround time is $10$.

---

## Common Mistakes / Gotchas

- Calculating turnaround time when the question asks for waiting time.
- Forgetting arrival times in SRTF/RR examples.
- Treating SJF as implementable exactly; actual systems need prediction.
- Choosing an RR quantum smaller than context-switch overhead.
- Assuming FCFS is always fair in user experience; arrival-order fairness can still produce convoy effects.
- Thinking Linux CFS is just RR with a different quantum. It uses virtual runtime and proportional fairness.
- Ignoring cache affinity when moving threads between cores.

---

## Summary / Cheat Sheet

| Term | Meaning |
|---|---|
| CPU burst | CPU execution interval before block/yield |
| FCFS | FIFO, non-preemptive |
| SJF | Shortest next CPU burst; optimal average waiting if exact bursts known |
| SRTF | Preemptive SJF |
| RR | Preemptive fixed time-slice scheduling |
| Priority | Run highest priority |
| Aging | Increase priority over time to avoid starvation |
| Multilevel queue | Fixed queues/classes |
| Feedback queue | Processes move between queues |
| CFS | Linux virtual-runtime fair scheduler |
| NUMA | Memory access depends on processor location |

**Key Formulas**:

$$
L=\lambda W
$$

$$
\text{turnaround time}=C_i-A_i
$$

$$
\tau_{n+1}=\alpha t_n+(1-\alpha)\tau_n
$$

$$
\bar{W}=\frac{\sum_i W_i}{n},\quad \bar{T}=\frac{\sum_i T_i}{n}
$$

**Key Takeaways**:

- Scheduling criteria conflict: better response time may cost more overhead or worse turnaround.
- FCFS is simple but vulnerable to convoy effects.
- SJF minimizes average waiting time in ideal deterministic settings but requires burst prediction.
- RR supports interactivity through preemption and a time quantum.
- Real systems combine ideas; Linux CFS uses proportional fairness and `vruntime`.
- Multicore scheduling adds load balance, cache affinity, SMT, and NUMA complexity.

---

## Practice Questions

**Q1**: Why are I/O-bound processes often favored by interactive schedulers?  
> Answer: They have short CPU bursts and block quickly, so giving them prompt CPU access improves responsiveness while they spend much time waiting for I/O.

**Q2**: What happens to RR as the quantum becomes very large?  
> Answer: It approaches FCFS because processes rarely get preempted before finishing their CPU burst.

**Q3**: How does aging prevent starvation?  
> Answer: It gradually increases the priority of waiting processes so a low-priority process eventually becomes high enough to run.

**Q4**: In CFS, which task is selected next?  
> Answer: The runnable task with the smallest `vruntime`, stored as the leftmost node in the red-black tree.
