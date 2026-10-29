---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 11 — Software Architecture And Architectural Patterns"
---

# ASD 11 — Software Architecture And Architectural Patterns

**Source note:** [Software Architecture And Architectural Patterns](../../ASD/11_Architecture.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Architectural Decisions|Architectural Decisions]]
  - [[#Choosing A Pattern|Choosing A Pattern]]
  - [[#Requirements And Trade-offs|Requirements And Trade-offs]]
  - [[#From Analysis To Design|From Analysis To Design]]
  - [[#Layered Architectures In Depth|Layered Architectures In Depth]]
  - [[#Layered Examples: Internet Stack And Web 2.0|Layered Examples: Internet Stack And Web 2.0]]
  - [[#Realising Non-Functional Requirements|Realising Non-Functional Requirements]]
  - [[#Purpose Of Architecture|Purpose Of Architecture]]
  - [[#Generic Application Architectures|Generic Application Architectures]]
  - [[#Boundaries And Dependencies|Boundaries And Dependencies]]
  - [[#MVC And Quality Tactics|MVC And Quality Tactics]]
  - [[#Model–View–Controller (MVC)|Model–View–Controller (MVC)]]

## Core Content

### Architectural Decisions

<!-- qard-id: ap-4f367ac59de1bdce5dfe -->
> [!qard]- What is software architecture concerned with?
> System-wide organisation, responsibilities, interfaces, constraints and major trade-offs, especially those affecting non-functional requirements.

<!-- qard-id: ap-16594c4209414cc487f2 -->
> [!qard]- How do architectural decisions differ from tactical design decisions?
> Architecture sets strategic system-wide structure; tactical choices concern local implementation, patterns and refactoring within it.

<!-- qard-id: ap-c38262d4c1a4c68e8324 -->
> [!qard]- Why reuse an architectural pattern?
> It captures proven structure and trade-offs, provides a shared vocabulary and helps teams understand, document and adapt a design.

<!-- qard-id: ap-bc8f14935efeb51498df -->
> [!qard]- What are cohesion and coupling, and what direction is desirable?
> Cohesion is how strongly a module's contents belong together; coupling is dependence between modules. Aim for high cohesion and low coupling.

### Choosing A Pattern

<!-- qard-id: ap-b9c255be8a8041ae2aa9 -->
> [!qard]- When is layered architecture useful, and what is its cost?
> When separating responsibilities behind service interfaces permits substitution and team ownership. Layer boundaries can be difficult and repeated crossings can add overhead.

<!-- qard-id: ap-ffd8a8569339717d9e1a -->
> [!qard]- How do strict and relaxed layering differ?
> Strict layers call only the next lower layer; relaxed layers may call deeper layers directly, trading separation for convenience/performance.

<!-- qard-id: ap-595336d483a23881b018 -->
> [!qard]- When is repository architecture useful, and what is its risk?
> Components share substantial persistent data through a central store. It centralises data management but can become a bottleneck or single point of failure.

<!-- qard-id: ap-9478a111550e1b77a81e -->
> [!qard]- When is client–server architecture useful, and what dependencies does it introduce?
> Many clients need shared services across locations; it introduces network, service availability and distributed management dependencies.

<!-- qard-id: ap-1bea932e4ca15473ddd8 -->
> [!qard]- When does pipe-and-filter architecture fit?
> Data passes through reusable transformation stages with agreed formats. Conversion overhead and incompatible formats can limit its benefits.

<!-- qard-id: ap-aa4dab8bc793000836b2 -->
> [!qard]- What are the responsibilities of MVC's Model, View and Controller?
> Model: domain state and operations. View: presentation. Controller: interpret user interactions and coordinate the appropriate operations.

<!-- qard-id: ap-fec895480ef7f340cae4 -->
> [!qard]- Why keep domain logic independent of the UI?
> It can be tested and reused with different interfaces, and display changes need not rewrite business rules.

### Requirements And Trade-offs

<!-- qard-id: ap-624778bdb42de6e714d9 -->
> [!qard]- Why can performance and maintainability pull architecture in different directions?
> Larger/localised components reduce communication overhead; smaller replaceable components can improve isolation and maintenance but add boundaries.

<!-- qard-id: ap-0759f79d15eca5ea8646 -->
> [!qard]- How can architecture improve availability?
> Use redundancy, fault-tolerance and replaceable components to reduce the effect and duration of a failure.

<!-- qard-id: ap-8b307a84780d1088a003 -->
> [!qard]- How do batch, transaction and event processing differ?
> Batch processes groups of data without interactive requests; transaction processing handles coherent user/database operations; event processing reacts to environmental or UI events.

<!-- qard-id: ap-42f1b5878c21ec93f8a2 -->
> [!qard]- How does language-processing architecture often form a pipeline?
> Lexical analysis, parsing, semantic analysis and code generation transform a formal-language input, sharing structures such as a syntax tree and symbol table.

### From Analysis To Design

<!-- qard-id: ap-5e3343ac5ceea57f7d22 -->
> [!qard]- How do analysis and design artefacts answer different questions?
> Use cases, system sequence diagrams and a domain model investigate the problem; architecture and interaction/class diagrams describe a solution. Findings feed back between the two activities.

### Layered Architectures In Depth

<!-- qard-id: ap-a8655e7b7c926c1d8122 -->
> [!qard]- Where does an application-coordination/use-case layer sit?
> Between presentation and domain logic, coordinating a user task and possibly session state while leaving UI rendering and core domain responsibilities separate.

### Layered Examples: Internet Stack And Web 2.0

<!-- qard-id: ap-49e7d3332d4640e64920 -->
> [!qard]- What do the Internet stack and the note's Web reference architecture illustrate about layering?
> Separate responsibilities behind interfaces: link/network/transport/application services in the network; client, connectivity, service and resource roles in the Web example. Upper layers depend on services below rather than every implementation detail.

### Realising Non-Functional Requirements

<!-- qard-id: ap-9aa80e072018f778c829 -->
> [!qard]- Which architectural tactics support security, safety and performance in the lecture?
> Protect critical assets behind controlled layers; isolate safety-critical functions into a manageable set of subsystems; localise critical operations, reduce communication and exploit concurrency for performance. Evaluate conflicts with maintainability and other goals.

### Purpose Of Architecture

<!-- qard-id: ap-3f5cec2792102a5146e2 -->
> [!qard]- Why is an architecture useful before all implementation details are known?
> It exposes constraints and trade-offs for stakeholder negotiation and lets the team reason about key abstractions while hiding unnecessary detail; it guides rather than replaces later design.

### Generic Application Architectures

<!-- qard-id: ap-c55c06f565e2666500fd -->
> [!qard]- What are the stages of an input–process–output batch application?
> Read/validate input into a queue, process items into results, then format and persist/display output. Each stage has a focused data transformation responsibility.

<!-- qard-id: ap-3ae1ffd1ca5bac8eccb3 -->
> [!qard]- How does event-processing architecture separate an editor's work?
> Detect events, interpret commands, update editor/ancillary data, access files as required and redraw the display; those responsibilities need not all live in one object.

<!-- qard-id: ap-32b896364448dea46292 -->
> [!qard]- How does an interpreter differ from a compiler within language processing?
> A compiler translates source into another representation/language; an interpreter executes the described instructions. Both may perform lexical, syntactic and semantic analysis.

### Boundaries And Dependencies

<!-- qard-id: ap-8f6a0901333bb9e29442 -->
> [!qard]- Why do architecture decisions often need to precede low-level coding?
> They constrain components' interfaces, deployment, data ownership and crosscutting qualities, making uncoordinated local choices expensive to reconcile later.

<!-- qard-id: ap-e48019493eaccbf2ca16 -->
> [!qard]- What distinguishes an architectural pattern from one local design-pattern instance?
> Its scope is the organisation/interactions of major system parts rather than one class/object collaboration, though the ideas can work together.

<!-- qard-id: ap-f0e40862e8b8fa455aa3 -->
> [!qard]- Why must a swappable layer preserve its interface contract?
> Callers rely on that contract rather than the old implementation; matching method names alone is insufficient if behaviour/assumptions change.

<!-- qard-id: ap-e25e1ad4e2a3244f6cca -->
> [!qard]- What trade-off motivates relaxed rather than strict layering?
> Skipping layers can reduce wrapping/overhead or expose needed services, but increases dependency paths and weakens isolation.

<!-- qard-id: ap-8f426e89abe2584b8fcb -->
> [!qard]- Why can repository architecture make component changes independent while centralising risk?
> Components share data through the repository contract rather than calling each other, but they all rely on that store's availability, capacity and schema.

<!-- qard-id: ap-408f45d67f246bb15eb7 -->
> [!qard]- How does client–server organisation differ from every client implementing the shared service locally?
> The service owns common functionality centrally/remotely, supporting shared access and independent upgrades while adding network/service dependencies.

<!-- qard-id: ap-e0d39e82c1c408bee55c -->
> [!qard]- Why is a common data format essential between pipe-and-filter stages?
> Each stage must interpret the preceding stage's output; incompatible representations force adapters or prevent reuse and add conversion work.

### MVC And Quality Tactics

<!-- qard-id: ap-17e35d57bc1fc5784d57 -->
> [!qard]- Why should a Model not contain concrete View presentation responsibilities?
> It would couple domain behaviour to one interface and complicate reuse/testing; the presentation layer should interpret domain state for its users.

<!-- qard-id: ap-64b0594f251dbc4fecff -->
> [!qard]- How can multiple views stay consistent with one Model?
> They query the same domain state and receive change notifications through suitable abstractions, rather than each maintaining an independent authoritative copy.

<!-- qard-id: ap-49920c31d180632aa9d8 -->
> [!qard]- What is the Controller's role when a user presses a button?
> Translate the interaction into the appropriate application/domain operation; domain results then drive presentation updates rather than embedding all business rules in the button.

<!-- qard-id: ap-fd300ef72ef0613ce3a2 -->
> [!qard]- How can finer-grained components help maintenance but hurt performance?
> Smaller boundaries isolate changes and substitution, but more interactions/communication can increase overhead in a critical path.

<!-- qard-id: ap-7d50ff00ef00bffdbbe5 -->
> [!qard]- Why localise safety-critical operations into a manageable part of an architecture?
> It narrows the area needing strong hazard analysis, review and protection, while integration assumptions must still be assessed.

<!-- qard-id: ap-8c186fb3710c4d2d0406 -->
> [!qard]- Why can one application combine batch, transaction, event and language-processing patterns?
> Different workflows have different triggers and data/control needs; a reference architecture need not force every subsystem into one exclusive category.

### Model–View–Controller (MVC)

<!-- qard-id: ap-2f1ea8971ca7504e77bd -->
> [!qard]- How does a Model query differ from a Model mutator?
> A query observes domain state without changing it; a mutator intentionally changes domain state under its rules. Views query for presentation; Controllers route intended user changes through the appropriate operations.
