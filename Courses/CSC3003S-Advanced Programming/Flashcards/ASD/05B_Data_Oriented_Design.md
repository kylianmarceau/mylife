---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 05B — Data-Oriented Design"
---

# ASD 05B — Data-Oriented Design

**Source note:** [Data-Oriented Design](../../ASD/05B_Data_Oriented_Design.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Overview|Overview]]
  - [[#Memory And Caches|Memory And Caches]]
  - [[#Objects On The CPU|Objects On The CPU]]
  - [[#The DOD Steps|The DOD Steps]]
  - [[#CPU Code Flow|CPU Code Flow]]

## Core Content

### Overview

<!-- qard-id: ap-6307daf195ee8c0c5ff8 -->
> [!qard]- What is data-oriented design?
> Organising code around how data flows through the CPU, to speed up processing of large amounts of data.

<!-- qard-id: ap-feb5f5411a1708abaa02 -->
> [!qard]- When should you use DOD?
> Only with lots of uniform data and a real bottleneck (games, database engines, simulations, solvers) — otherwise "if it ain't broke…".

<!-- qard-id: ap-3ed44223e29db64070db -->
> [!qard]- Why does traditional OOP mapping run slowly?
> It creates blob objects with lots of indirection, scattered on the heap, mixing hot/cold and read-only/read-write data.

### Memory And Caches

<!-- qard-id: ap-a1e19f0504dc52e27836 -->
> [!qard]- Why can't RAM keep a modern CPU fed?
> A core can consume ~600 GiB/s, but sequential RAM gives ~70 GiB/s (~10× slower) and random access ~400 MiB/s (~1500× slower).

<!-- qard-id: ap-5620fc0057b6622a54fc -->
> [!qard]- What is hot data?
> A small amount of data used over and over (loop data, locals, lookup tables), kept in cache.

<!-- qard-id: ap-44771921bc5dc837785e -->
> [!qard]- Order the cache hierarchy from fastest to slowest.
> Register file/micro-op cache, L1, L2, L3, RAM.

<!-- qard-id: ap-80f28766d64ef09b69cc -->
> [!qard]- What eviction schemes do caches use?
> LRU, LFU, and in modern CPUs a small neural network mixing both, plus speculative prefetching.

<!-- qard-id: ap-9f5b31d90ee7224ebeab -->
> [!qard]- Why does fetching 1 byte evict other data?
> Data loads in fixed-size lines (32 bytes+), so the whole line is fetched and something else is evicted.

<!-- qard-id: ap-8e6fade97d4c0691ef1f -->
> [!qard]- Why is sequential access much faster than random?
> The prefetcher can predict it; random access pays full RAM latency almost every time.

<!-- qard-id: ap-633ffe93f0c208e606f0 -->
> [!qard]- Why is a Java `Integer[]` slower and larger than `int[]`?
> It holds pointers to separate heap objects with headers, so iterating it is effectively random access.

### Objects On The CPU

<!-- qard-id: ap-1f6f635975f6c9c6a145 -->
> [!qard]- Why are heap objects slow?
> They're scattered randomly by allocation and garbage collection, costing up to ~1500 cycles per access.

<!-- qard-id: ap-bc65240cbae506c3df4d -->
> [!qard]- Why are virtual method calls slow?
> Each goes through a VMT pointer chase the CPU can't predict, causing pipeline stalls and data/code cache misses.

<!-- qard-id: ap-01b547a4ea9f5d0c7cbd -->
> [!qard]- Stack versus heap access?
> Stack: direct, local, effectively free. Heap: indirect, polymorphic, up to 1500 cycles.

<!-- qard-id: ap-4845f56dca230241a595 -->
> [!qard]- Run-time versus compile-time polymorphism?
> Run-time (late binding, VMT): flexible but slow and unpredictable. Compile-time (C++ templates): almost as flexible and up to 1000× faster.

### The DOD Steps

<!-- qard-id: ap-c25c3c883f14c2f28587 -->
> [!qard]- State the three steps of data-oriented design.
> 1. Find the hot code (measure with a profiler). 2. Analyse its data flow. 3. Keep data that flows together together.

<!-- qard-id: ap-1cb1223c72cd1a87a26b -->
> [!qard]- Hot code versus cold code?
> Hot: runs in loops many times per second, so more objects means slower. Cold: rarely run, so its cost is negligible.

<!-- qard-id: ap-5f42f2fc6cdfd0a3feaa -->
> [!qard]- How is DOD implemented in Java?
> Arrays of simple types, few objects, static methods taking data as parameters; dynamic data kept in separate objects.

<!-- qard-id: ap-584920258244c4a01aab -->
> [!qard]- How can different object kinds be handled without virtual calls?
> C++ `std::variant` or a type flag; in Java, tag bits in an index.

<!-- qard-id: ap-db7d20627cca040ad021 -->
> [!qard]- What speed-up can DOD and data parallelism give?
> DOD up to ~1 000 000×, data parallelism ~1000×.

### CPU Code Flow

<!-- qard-id: ap-1a21e58fa05fa4d07e30 -->
> [!qard]- What is pipelining, and what breaks it?
> Overlapping instruction stages for one instruction per cycle; an unpredicted jump empties the pipeline.

<!-- qard-id: ap-edab54cd305a094467c3 -->
> [!qard]- What happens when branch prediction is wrong?
> Speculative work is rolled back, the pipeline refilled, and wrongly fetched data may evict useful data.

<!-- qard-id: ap-460cd2f0c4317fbdce0e -->
> [!qard]- Superscalar versus out-of-order execution?
> Superscalar runs independent instructions simultaneously; out-of-order reorders instructions using a dependency graph to keep units busy.

<!-- qard-id: ap-452f47374b0286791241 -->
> [!qard]- What is the stack engine?
> CPU hardware simulating the stack in registers, making local-variable access effectively free.

<!-- qard-id: ap-8f2a2776f5ad5569fa8f -->
> [!qard]- Why can the CPU optimise better than the compiler?
> It sees the actual data at run time and learns predictions; the compiler sees only static code and global dependency analysis is NP-hard.
