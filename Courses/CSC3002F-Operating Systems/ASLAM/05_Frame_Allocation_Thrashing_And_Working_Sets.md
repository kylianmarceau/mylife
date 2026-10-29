---
tags:
  - operating-systems
---

# Frame Allocation, Thrashing, And Working Sets

**Subject**: CSC3002F Operating Systems  
**Source**: `Frame Allocation.pdf`, Aslam Safla, pages 1-66  
**Generated**: 2026-06-03

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Frame Allocation Problem|The Frame Allocation Problem]]
  - [[#Local And Global Replacement|Local And Global Replacement]]
  - [[#Frame Allocation Methods|Frame Allocation Methods]]
  - [[#Reclaiming Pages And Free Frame Lists|Reclaiming Pages And Free Frame Lists]]
  - [[#What Causes Page Replacement Pressure|What Causes Page Replacement Pressure]]
  - [[#Thrashing|Thrashing]]
  - [[#Preventing Thrashing|Preventing Thrashing]]
  - [[#Locality And Program Structure|Locality And Program Structure]]
  - [[#Working Set Model|Working Set Model]]
  - [[#Page-Fault Frequency And Working Set Updates|Page-Fault Frequency And Working Set Updates]]
  - [[#Choosing The Working Set Window|Choosing The Working Set Window]]

---

## Core Content

### The Frame Allocation Problem

#### Definitions

> **Physical Frame Allocation**: The OS decision of how many physical memory frames each process should receive.

> **Virtual Memory**: A memory abstraction where processes use virtual address spaces that may be larger than physical memory.

> **Load Control**: OS control over how many processes are allowed to compete for memory at one time.

Demand paging answers when to load a page: only when a page fault occurs. Page replacement answers what to evict when memory is full. Frame allocation answers a different question:

$$
\text{How many frames should each process get?}
$$

The OS must decide whether:

1. Every process gets the same number of frames.
2. Larger or more important processes get more frames.
3. Some processes should be swapped out completely.
4. Frames should stay fixed per process or move dynamically between processes.

The allocation decision affects page-fault rate, fairness, throughput, and whether the system starts thrashing.
### Local And Global Replacement

#### Definitions

> **Local Replacement**: Page replacement where a process can evict only its own pages.

> **Global Replacement**: Page replacement where a victim page may be selected from all frames in the system.

> **Resident Set**: The set of pages from a process currently held in physical memory.

All page replacement algorithms can be applied locally or globally.

| Replacement Scope | Victim Chosen From | Strength | Weakness |
|---|---|---|---|
| Local | Only the faulting process's frames | More predictable per-process behavior | A process may be stuck with too few frames even if freeable frames exist elsewhere |
| Global | Any process's frames | Better overall memory utilization | Process runtime can vary because other processes can steal frames |

Local replacement limits damage: if one process starts faulting badly, it mostly hurts itself. Global replacement can improve total throughput, but memory-hungry processes may keep stealing frames from each other and destabilize performance.




### Frame Allocation Methods

#### Definitions

> **Fixed Allocation**: An allocation policy where each process receives a fixed number of frames.

> **Equal Allocation**: A fixed allocation policy where every process receives the same number of frames.

> **Proportional Allocation**: A fixed allocation policy where processes receive frames proportional to process size.

> **Priority Allocation**: An allocation policy where frame assignment depends on process priority.

With equal allocation, if there are $m$ frames and $n$ processes, each process receives:

$$
\frac{m}{n}
$$

Example from the source:

$$
m=100,\quad n=5
$$

$$
\frac{100}{5}=20\ \text{frames per process}
$$

With proportional allocation:

$$
s_i=\text{size of process }p_i
$$

$$
S=\sum_i s_i
$$

$$
m=\text{total number of frames}
$$

$$
a_i=\frac{s_i}{S}\times m
$$

where $a_i$ is the allocation for process $p_i$.

| Method | Allocation Rule | Useful When |
|---|---|---|
| Equal | Same frames per process | Processes are similar or fairness is prioritized |
| Proportional | Frames proportional to process size | Process sizes differ substantially |
| Priority | Frames based on OS/user/process priority | Some work is more important than other work |
| Dynamic global | Frames grow/shrink with demand | System wants high utilization and can tolerate variability |

Priority allocation can select a victim frame from a lower-priority process when a higher-priority process faults. Priority may depend on kernel importance, time limits, memory requirements, I/O behavior, and policy decisions.
### Reclaiming Pages And Free Frame Lists

#### Definitions

> **Free Frame List**: A list of physical frames currently available for allocation.

> **Page-Out**: The act of moving pages from memory to backing storage to free frames.

> **Threshold**: A configured minimum level that triggers action when crossed.

Reclaiming pages is a global replacement strategy designed to keep free frames available.

The source's reclaiming strategy:

1. Maintain a free frame list.
2. Satisfy memory requests from that list.
3. When the number of free frames falls below a threshold, trigger page replacement.
4. Reclaim pages so future faults can be handled without waiting for emergency eviction.

This attempts to ensure the system has enough free memory for incoming requests.

The source's Linux/Ubuntu example:

| Mechanism | Description |
|---|---|
| Free frame list | Linux maintains free frames for faulting processes |
| Low-free threshold | If free frames fall below `lots-free`, page-out begins |
| `lots-free` | About $1/64$ of main memory in the source example |
| Replacement algorithm | Clock-style page replacement |
| Last resort | If page-out cannot keep enough free pages, whole processes may be swapped out |




### What Causes Page Replacement Pressure

#### Definitions

> **Compulsory Fault**: A fault because a page has not yet been loaded into main memory.

> **Capacity Fault**: A fault because physical memory cannot hold the active pages.

> **Policy Fault**: A fault because the replacement algorithm evicted a page that is needed again.

Page replacement pressure appears when page faults require frames. The same three fault causes from demand paging matter here:

| Fault Type | Allocation Connection |
|---|---|
| Compulsory | Allocation cannot avoid first references, but enough free frames make them easier to satisfy |
| Capacity | More frames or fewer active processes may be needed |
| Policy | Better local/global replacement or better load control may reduce faults |

When allocation is too tight, page faults become frequent. If too many processes are active, every process may have too few frames to hold its active pages.
### Thrashing

#### Definitions

> **Thrashing**: A condition where a process or system spends most of its time swapping pages instead of doing useful computation.

> **CPU Utilization**: The fraction of time the CPU is doing useful work.

> **Over-Commitment**: A state where active processes collectively demand more memory than physical memory can support.

<svg width="100%" viewBox="0 0 680 380" role="img">
<title>CPU utilization vs degree of multiprogramming</title>
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<line x1="80" y1="30" x2="80" y2="310" stroke="#ffffff" stroke-width="1.5" marker-end="url(#arrow)"/>
<line x1="80" y1="310" x2="640" y2="310" stroke="#ffffff" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="68" y="180" text-anchor="middle" font-size="13" fill="#ffffff" font-family="sans-serif" transform="rotate(-90,68,180)">CPU utilization</text>
<text x="360" y="350" text-anchor="middle" font-size="13" fill="#ffffff" font-family="sans-serif">degree of multiprogramming</text>
<path d="M 90 308 C 130 295, 170 265, 220 230 C 270 195, 320 158, 370 130 C 400 114, 430 103, 455 99 C 470 97, 480 97, 490 99 C 500 102, 508 110, 514 124 C 522 145, 524 175, 522 205 C 519 235, 514 262, 507 280 C 500 296, 492 305, 483 308" fill="none" stroke="#4a90d9" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="510" y1="148" x2="510" y2="158" stroke="#ffffff" stroke-width="1.2"/>
<line x1="510" y1="158" x2="600" y2="158" stroke="#ffffff" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="605" y="163" font-size="13" fill="#ffffff" font-family="sans-serif">thrashing</text>
</svg>

Thrashing occurs when page-fault handling dominates useful work. A process that does not have enough frames has a high page-fault rate, so:

1. The process faults.
2. The OS spends time doing disk I/O.
3. CPU utilization drops because processes are waiting for pages.
4. The OS may mistakenly add more processes because the CPU looks underused.
5. More active processes reduce frames per process even further.
6. Page-fault rate gets worse.

Thrashing can be caused by:

| Cause | Explanation |
|---|---|
| Bad replacement policy | The algorithm conflicts with program locality |
| Too many active processes | Memory is over-committed |
| Too few frames per process | Processes cannot hold their active pages |
| Global frame stealing | Processes repeatedly take frames from each other |




### Preventing Thrashing

#### Definitions

> **Working Set**: The set of pages a process has used recently and is likely to need again.

> **Working Set Algorithm**: A load-control and replacement approach that keeps recently referenced pages in memory and runs only processes whose working sets fit.

Main thrashing controls:

| Option | Method | Effect |
|---|---|---|
| Local or priority replacement | Limit replacement to a process or lower-priority victims | One thrashing process cannot easily make all processes thrash |
| Working set model | Run only processes whose working sets fit into available frames | Prevents over-commitment by suspending processes that do not fit |

Local replacement can isolate damage but may make the affected process slow. Working set load control attacks the system-level cause: too many active pages competing for too few frames.
### Locality And Program Structure

#### Definitions

> **Locality Of Reference**: The tendency of memory references to cluster around a small set of pages for a period of time.

> **Temporal Locality**: Reuse of the same memory locations over time.

> **Spatial Locality**: Use of memory locations near other recently used locations.

Virtual memory works because of locality. During a short time period, a program usually uses only a subset of its pages. If that subset fits in memory, compulsory misses happen early and then performance becomes good.

Examples:

| Source Example | Locality Type |
|---|---|
| Accessing array elements in sequence | Spatial locality |
| Executing instructions in sequence | Spatial locality |
| Repeatedly cycling through a loop | Temporal locality |

The source's array example assumes a $128\times128$ integer array where each row is stored in one page and only one page-table entry/frame is effectively available for the array access pattern.

Row-oriented traversal:
```python
for (i = 0; i < 128; i++){
	for(j = 0; j < 128; j++){
		data[i,j] = 0;
	}
}
```

This accesses one row at a time. Since each row fits in one page:

$$
\text{page faults}=128
$$

Column-oriented traversal:

```python
for (j = 0; j < 128; j++){
	for(i = 0; i < 128; i++){
		data[i,j] = 0;
	}
}
```

This jumps across rows. With one row page available at a time:

$$
\text{page faults}=128\times128=16{,}384
$$

The program's access pattern can therefore change page faults dramatically without changing the data size.




### Working Set Model

#### Definitions

> **Working Set Window ($w$)**: The time interval or number of page references used to decide which pages count as recent.

> **Working Set Size ($|WS(t,w)|$)**: The number of distinct pages in the working set at time $t$ using window $w$.

> **Total Frame Demand ($D$)**: The total number of frames demanded by active working sets.

At time $t$, the working set is:

$$
WS(t,w)=\{p\mid p\text{ was referenced during the last }w\text{ references or time units}\}
$$

The working set size is:

$$
|WS(t,w)|
$$

For multiple active processes:

$$
D=\sum_i |WS_i(t,w)|
$$

Let:

$$
m=\text{available physical frames}
$$

Then:

$$
D>m\Rightarrow \text{the active working sets do not fit}
$$

If a process's own demand does not fit in the frames allocated to it, the process behaves badly:

| Condition | Global Replacement Result | Local Replacement Result |
|---|---|---|
| Working set fits | Good performance after compulsory faults | Good performance after compulsory faults |
| Working set does not fit | Thrashing can spread through frame stealing | The process is slow but damage is more contained |

The working set algorithm:

1. Estimate each process's working set size $|WS_i(t,w)|$.
2. Start or continue a process only if enough frames can be allocated to its working set.
3. Use local page replacement inside the process.
4. Track working set size over time.
5. Dynamically reallocate frames as locality changes.
6. Suspend or swap out a process if its working set cannot fit.

**Working set example:**

<svg width="100%" viewBox="0 0 680 280" role="img">
<title>Working Set Example</title>
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<text x="30" y="30" font-size="12" fill="#ffffff" font-family="sans-serif">page reference string</text>
<text x="30" y="60" font-size="13" fill="#ffffff" font-family="monospace" letter-spacing="2">. . . 2 6 1 5 7 7 7 7 5 1 6 2 3 4 1 2 3 4 4 4 3 4 3 4 4 4 1 3 2 3 4 4 4 3 4 4 4 . . .</text>
<line x1="258" y1="65" x2="258" y2="175" stroke="#ffffff" stroke-width="1.5" marker-end="url(#arr)"/>
<line x1="490" y1="65" x2="490" y2="175" stroke="#ffffff" stroke-width="1.5" marker-end="url(#arr)"/>
<line x1="130" y1="115" x2="255" y2="115" stroke="#ffffff" stroke-width="1.2" marker-start="url(#arr)" marker-end="url(#arr)"/>
<text x="185" y="105" text-anchor="middle" font-size="14" fill="#ffffff" font-family="serif" font-style="italic">Δ</text>
<line x1="362" y1="115" x2="487" y2="115" stroke="#ffffff" stroke-width="1.2" marker-start="url(#arr)" marker-end="url(#arr)"/>
<text x="422" y="105" text-anchor="middle" font-size="14" fill="#ffffff" font-family="serif" font-style="italic">Δ</text>
<text x="258" y="195" text-anchor="middle" font-size="13" fill="#ffffff" font-family="serif" font-style="italic">t</text>
<text x="265" y="198" font-size="10" fill="#ffffff" font-family="serif">1</text>
<text x="490" y="195" text-anchor="middle" font-size="13" fill="#ffffff" font-family="serif" font-style="italic">t</text>
<text x="497" y="198" font-size="10" fill="#ffffff" font-family="serif">2</text>
<text x="150" y="245" text-anchor="middle" font-size="13" fill="#ffffff" font-family="sans-serif">WS(t1)</text>
<text x="183" y="248" font-size="10" fill="#ffffff" font-family="sans-serif"></text>
<text x="188" y="245" font-size="13" fill="#ffffff" font-family="sans-serif">) = {1,2,5,6,7}</text>
<text x="420" y="245" text-anchor="middle" font-size="13" fill="#ffffff" font-family="sans-serif">WS(t</text>
<text x="453" y="248" font-size="10" fill="#ffffff" font-family="sans-serif">2</text>
<text x="458" y="245" font-size="13" fill="#ffffff" font-family="sans-serif">) = {3,4}</text>
</svg>

### Page-Fault Frequency And Working Set Updates

#### Definitions

> **Page-Fault Frequency (PFF)**: A measure based on how often a process faults.

> **Faulting Page**: The page whose reference caused the current page fault.

The source connects page-fault frequency with the working set window. Track:

$$
t_{\text{last-PF}}=\text{time or reference count of the previous page fault}
$$

$$
t_{\text{current}}=\text{current time or reference count}
$$

If:

$$
t_{\text{current}}-t_{\text{last-PF}}>w
$$

then remove pages not referenced in the interval:

$$
[t_{\text{last-PF}},t_{\text{current}}]
$$

If:

$$
t_{\text{current}}-t_{\text{last-PF}}\le w
$$

then add the faulting page to memory.

In pseudocode:

```text
if page_refs_since_last_fault > w:
    remove pages not referenced since the last page fault
else:
    add the faulting page to memory
```

This adapts the resident set to the process's current locality.
### Choosing The Working Set Window

#### Definitions

> **Locality**: A phase of execution where a process repeatedly uses a related group of pages.

Choosing $w$ is critical.

The source notes that one page fault can take about:

$$
10\ \text{ms}
$$

and that this can correspond to roughly:

$$
2{,}000{,}000\ \text{instructions}
$$

So $w$ must usually be much larger than a single page-fault service time.

| Window Choice | Effect |
|---|---|
| $w$ too small | The working set misses part of the current locality, causing excessive page faults |
| $w$ too large | The working set includes several localities, wasting memory and slowing other processes |
| $w\rightarrow\infty$ | The working set approaches the entire program |

The goal is to choose a window large enough to capture the current locality but not so large that old localities stay resident unnecessarily.
