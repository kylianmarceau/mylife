---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 05B — Data-Oriented Design"
---

# ASD 05B — Data-Oriented Design

**Source note:** [Data-Oriented Design](../../ASD/05B_Data_Oriented_Design.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Finding The Bottleneck|Finding The Bottleneck]]
  - [[#Locality And Layout|Locality And Layout]]
  - [[#CPU Execution|CPU Execution]]
  - [[#How A CPU Works: Feeding The Beast|How A CPU Works: Feeding The Beast]]
  - [[#The Cache Hierarchy And Hot Data|The Cache Hierarchy And Hot Data]]
  - [[#Cache Movement, Eviction And Load Size|Cache Movement, Eviction And Load Size]]
  - [[#Anatomy Of An Object And The Heap|Anatomy Of An Object And The Heap]]
  - [[#Stack Versus Heap, And Polymorphism|Stack Versus Heap, And Polymorphism]]
  - [[#DOD Step 3: Data That Flows Together Stays Together|DOD Step 3: Data That Flows Together Stays Together]]
  - [[#DOD Speed-Up And Other Benefits|DOD Speed-Up And Other Benefits]]
  - [[#Stack Engine And What The Compiler Can't Do|Stack Engine And What The Compiler Can't Do]]
  - [[#DOD Step 2: Analyse The Data Flow|DOD Step 2: Analyse The Data Flow]]
  - [[#Data Layout And Access|Data Layout And Access]]
  - [[#CPU Code Flow|CPU Code Flow]]

## Core Content

### Finding The Bottleneck

<!-- qard-id: ap-cd3215e2f4cd42abd92e -->
> [!qard]- What does data-oriented design organise a program around?
> The data processed by important operations and how it moves through memory and the CPU, especially for large uniform workloads.

<!-- qard-id: ap-eef31eb67392d7c7d19b -->
> [!qard]- When is DOD worth considering?
> When profiling shows a significant bulk-data bottleneck whose layout/access costs matter; avoid redesigning cold code without evidence.

<!-- qard-id: ap-265ca27a8ffe79305ab6 -->
> [!qard]- What are the three main DOD steps?
> Measure and locate hot code; analyse its data flow; organise together the data used together by that flow.

<!-- qard-id: ap-4aa8fb0d0ff5ac81349f -->
> [!qard]- What is hot data, and why separate it from cold data?
> Hot data is accessed frequently in important operations. Separating rarely used fields lets cache capacity serve useful work rather than unrelated data.

### Locality And Layout

<!-- qard-id: ap-cc1114179e4ee2861df7 -->
> [!qard]- Why does sequential access often outperform scattered pointer chasing?
> Nearby accesses reuse fetched blocks and are easier to prefetch; dependent unpredictable loads can stall while waiting for memory.

<!-- qard-id: ap-5915d56f496c9dacdf8f -->
> [!qard]- What are temporal and spatial locality?
> Temporal locality reuses recently accessed data; spatial locality accesses data near other recently accessed data. Both help caches satisfy requests.

<!-- qard-id: ap-948ec84aee19153c314f -->
> [!qard]- Why can an array of object references still have poor data locality?
> The references are contiguous, but the referenced objects may be scattered, so iteration still requires indirect loads.

<!-- qard-id: ap-a12fb75ad40a2fa16cf6 -->
> [!qard]- How do array-of-structures and structure-of-arrays layouts differ?
> AoS stores complete records together; SoA stores each field in its own array. A loop over one or a few fields can avoid fetching unused fields with SoA.

<!-- qard-id: ap-72762fbd6a05e2f70ce9 -->
> [!qard]- Why can virtual dispatch add cost in a hot loop?
> Indirect call targets may be harder to predict and inline, and may need extra code/data loads. The actual cost depends on runtime/compiler optimisation and access patterns.

<!-- qard-id: ap-f3bbfa14b0a9535784f3 -->
> [!qard]- How can static dispatch or templates help a measured hot path?
> Known call targets can enable inlining and optimisation and avoid some indirect dispatch, while preserving suitable abstraction.

<!-- qard-id: ap-681ccaeb300cdc157b53 -->
> [!qard]- How can DOD coexist with an object-oriented program?
> Reorganise the measured hot data and loops while leaving cold user interfaces, coordination and other code in their existing abstractions.

### CPU Execution

<!-- qard-id: ap-936e59d227e7f5887486 -->
> [!qard]- What does instruction pipelining overlap?
> Fetching, decoding and executing different instructions, improving throughput when the pipeline stays supplied.

<!-- qard-id: ap-ea9d1d8929515396729c -->
> [!qard]- Why can a branch misprediction be expensive?
> Speculative work on the wrong path is discarded and execution resumes on the correct path, wasting cycles and possibly cache work.

<!-- qard-id: ap-2e9e1fb8e8a63be9d261 -->
> [!qard]- How do superscalar and out-of-order execution use independent instructions?
> Superscalar hardware issues multiple instructions; out-of-order scheduling runs ready instructions while respecting data dependencies and observable behaviour.

<!-- qard-id: ap-78509cfaeb617be953db -->
> [!qard]- Why do data dependencies limit parallel instruction execution?
> An instruction cannot use a result that has not been produced; a long dependent chain restricts how much work can overlap.

### How A CPU Works: Feeding The Beast

<!-- qard-id: ap-e7e78ff7fe6fe491bab3 -->
> [!qard]- Why can memory movement dominate a computation with little arithmetic?
> CPU execution throughput can far exceed the rate of obtaining required data, especially scattered dependent loads. A cache miss may leave execution units waiting despite a fast processor.

### The Cache Hierarchy And Hot Data

<!-- qard-id: ap-3ad7fd880be69b8d6c21 -->
> [!qard]- How does the memory hierarchy trade speed against capacity?
> Registers and nearby caches are small/fast; farther caches and RAM are larger/slower. Keeping repeatedly accessed useful data near the core reduces costly transfers; exact sizes/latencies are hardware-dependent.

### Cache Movement, Eviction And Load Size

<!-- qard-id: ap-870ebcdc3c7288ce175e -->
> [!qard]- Why does fetching one small field potentially evict unrelated useful data?
> Memory is transferred and cached in blocks rather than just that field. Loading cold data consumes cache capacity and may displace hot data, making layout and access predictability matter.

### Anatomy Of An Object And The Heap

<!-- qard-id: ap-ea8227d7cd2fd3fb1b8d -->
> [!qard]- How can object headers, pointers and allocation affect bulk-data cost?
> Headers/padding enlarge storage, references add indirection, and separate allocations can scatter data. A contiguous array of primitive values avoids many of those costs; actual layouts and optimisation depend on the runtime.

### Stack Versus Heap, And Polymorphism

<!-- qard-id: ap-7c8a07f4d3da73090925 -->
> [!qard]- How do storage placement and dispatch choices differ conceptually?
> Stack/heap describe lifetime/allocation organisation; static/virtual dispatch describe when a target is selected. They influence optimisation and locality but neither alone proves an access is free or slow.

### DOD Step 3: Data That Flows Together Stays Together

<!-- qard-id: ap-d4376dda545776352e3b -->
> [!qard]- How can a data-oriented loop represent varying object kinds without a large virtual hierarchy?
> Keep compact kind tags alongside arrays and use controlled dispatch, or a suitable tagged union such as `std::variant`; retain only the variation the hot loop actually needs.

### DOD Speed-Up And Other Benefits

<!-- qard-id: ap-7256227fb1a92e6f28a4 -->
> [!qard]- Why should large example DOD speed-up factors not be treated as universal predictions?
> They depend on baseline algorithms, representation, hardware and workload scale. Re-measure the actual bottleneck and preserve code clarity; algorithmic and parallel improvements may contribute separately.

### Stack Engine And What The Compiler Can't Do

<!-- qard-id: ap-a64594540d66b4a50a52 -->
> [!qard]- Why can a compiler fail to infer the best data-oriented design automatically?
> It must preserve semantics despite aliases, dynamic input and externally visible behaviour; a domain-level data reorganisation may require facts or design changes unavailable in the local source analysis.

<!-- qard-id: ap-73cb72318d6180b78a08 -->
> [!qard]- What is the point of the lecture's stack-engine discussion?
> Hardware and compiler mechanisms can track stack-related operations and keep local values close to execution, reducing bookkeeping/access overhead. This is not a guarantee that every local variable has zero physical cost; measure actual generated behaviour and locality.

### DOD Step 2: Analyse The Data Flow

<!-- qard-id: ap-6965a422bcc994d90c55 -->
> [!qard]- In the Pacman example, which data belongs in the hot update/draw flow?
> Sprite positions, collision/grid information, animation state and bitmaps. A small cold timer/input/AI component need not be redesigned unless measurement shows it matters; reorganise the repeated data flow rather than every class.

### Data Layout And Access

<!-- qard-id: ap-8db372cce4bc6f95d86a -->
> [!qard]- Why can grouping fields by real-world entity be inefficient for a particular hot operation?
> The operation may use the same small subset from many entities, so complete objects bring in unused fields and require scattered loads.

<!-- qard-id: ap-ceb0055679f17a7e6804 -->
> [!qard]- Why separate frequently read data from rarely changed or frequently written data?
> Their access patterns differ; unnecessary writes/loads and sharing can disturb cache use. Arrange the layout around the actual operation's needs.

<!-- qard-id: ap-a6f92a8e25e27a97bcde -->
> [!qard]- How does a cache miss differ from a slow arithmetic operation?
> The core waits for required data/instructions from a slower level, so reducing arithmetic alone may leave the dominant bottleneck untouched.

<!-- qard-id: ap-042b225aae5635b2c3b5 -->
> [!qard]- What does hardware prefetching try to exploit?
> Predictable future addresses, often sequential patterns, so useful blocks arrive before execution demands them.

<!-- qard-id: ap-c96108529f822bad0769 -->
> [!qard]- Why do dependent pointer loads limit the benefit of executing many instructions in parallel?
> The next address is unknown until the previous load returns, creating a dependency chain the CPU cannot freely overlap.

<!-- qard-id: ap-63917e7b8099d663bd30 -->
> [!qard]- What is a virtual method table used for?
> It maps an object's runtime type/interface operations to method targets, allowing dynamic dispatch at the cost of an indirect lookup when not optimised away.

<!-- qard-id: ap-9cb5eb48f5fe5e4a4eb6 -->
> [!qard]- How does early/static binding differ from late/dynamic binding?
> Static binding resolves the relevant operation from compile-time information; dynamic binding selects according to runtime type/state. This affects flexibility and optimisation opportunities.

<!-- qard-id: ap-ceb340b20ec9b706e84d -->
> [!qard]- Why is an array of primitive values not equivalent in layout to an array of boxed objects?
> Primitive values can be stored directly contiguously; boxed arrays store references to separately represented values with possible headers/indirection.

<!-- qard-id: ap-e968576a029fa53edec6 -->
> [!qard]- When might a structure-of-arrays transformation not improve the measured operation?
> If it actually needs whole records together, has little data or is limited elsewhere, the new layout may offer little benefit or hurt another access pattern.

### CPU Code Flow

<!-- qard-id: ap-f98180dd1df31c112394 -->
> [!qard]- What does instruction pipelining improve: latency of one instruction or throughput of many?
> Primarily throughput by overlapping stages of different instructions; it does not imply each individual instruction completes instantaneously.

<!-- qard-id: ap-cdd7aa99d024ccd1bcde -->
> [!qard]- What happens to speculative work after a wrong branch prediction?
> Incorrect-path effects are not committed; the CPU discards that work and resumes the correct path, incurring recovery and possible cache costs.

<!-- qard-id: ap-bfbe13258bbbef7f5c4a -->
> [!qard]- How does out-of-order execution preserve the intended program behaviour?
> It schedules ready independent operations while respecting dependencies and committing results consistently with the architecture's observable rules.

<!-- qard-id: ap-78b8b7d6e89886cd05d3 -->
> [!qard]- Why should a profiler precede a broad object-to-array rewrite?
> It identifies which operations/data dominate the workload, allowing a targeted change whose benefit and regressions can be measured.

<!-- qard-id: ap-e6a1df799868acfbd1be -->
> [!qard]- How should an optimisation be evaluated when data size or number of entities changes?
> Re-measure representative scales; an overhead negligible for a few objects may dominate at large scale, while a large redesign may be unwarranted for the small case.
