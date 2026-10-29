---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 12 — Antipatterns"
---

# ASD 12 — Antipatterns

**Source note:** [Antipatterns](../../ASD/12_Antipatterns.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Recognising Harmful Structures|Recognising Harmful Structures]]
  - [[#Fragile Interfaces And Changes|Fragile Interfaces And Changes]]
  - [[#Misguided Development Habits|Misguided Development Habits]]
  - [[#Generic Software Antipatterns|Generic Software Antipatterns]]
  - [[#Object-Oriented Antipatterns|Object-Oriented Antipatterns]]
  - [[#Programming Antipatterns|Programming Antipatterns]]
  - [[#Diagnosing And Repairing Antipatterns|Diagnosing And Repairing Antipatterns]]

## Core Content

### Recognising Harmful Structures

<!-- qard-id: ap-f5007cf889bfdf2ae6d5 -->
> [!qard]- What makes a recurring solution an antipattern?
> It is tempting or common but repeatedly produces harmful consequences; understanding it includes the problem, bad response, resulting harm and remedy.

<!-- qard-id: ap-a665ca84d3c4b57212e4 -->
> [!qard]- What is a big ball of mud, and how is it improved?
> A system understandable only as one tangled unit. Decompose responsibilities and introduce clear architecture and interfaces.

<!-- qard-id: ap-b60205fb850701748483 -->
> [!qard]- What is a god object, and which design problem does it expose?
> One object accumulates many responsibilities and dependencies. Separate things that change for different reasons and give them focused interfaces.

<!-- qard-id: ap-5b13ca6db035c087e1bc -->
> [!qard]- Why are circular module dependencies difficult to maintain?
> Each part needs knowledge of the other, so changes ripple and independent reuse/testing becomes harder. Introduce abstractions or notification boundaries to break cycles.

<!-- qard-id: ap-f32025f075183e6ed93b -->
> [!qard]- What is abstraction inversion?
> Lower-level functionality is forced to depend on higher-level constructs. Redesign the dependency structure so foundational operations sit at the appropriate level.

<!-- qard-id: ap-68df698a876789cef431 -->
> [!qard]- What is the inner-platform effect?
> An application grows its own general programming platform to support customisation, creating unnecessary complexity and a difficult security boundary.

### Fragile Interfaces And Changes

<!-- qard-id: ap-d0b4070dc09797d19c63 -->
> [!qard]- What is temporal coupling, and how can it be reduced?
> Correctness requires callers to invoke methods in a hidden order. Enforce construction/initialisation or the algorithm sequence internally instead.

<!-- qard-id: ap-f4dd38d0159cc5943b32 -->
> [!qard]- How does Template Method address the “call super” problem?
> The base algorithm owns the required sequence and calls overridable hooks, so clients cannot omit essential parent work by forgetting a call.

<!-- qard-id: ap-011b1b7df5b295bb039f -->
> [!qard]- Why is making every field public a poor fix for access difficulties?
> It destroys information hiding, spreads dependencies and makes invariants hard to preserve; provide a focused interface instead.

<!-- qard-id: ap-80bfe0f37c2fa3911dbd -->
> [!qard]- What is shotgun surgery, and what does it suggest?
> One logical change requires scattered edits. Centralise the responsibility through refactoring or, for suitable crosscutting concerns, AOP.

<!-- qard-id: ap-1af5590d9b866214043b -->
> [!qard]- Why is silent exception swallowing dangerous?
> Failures become hidden, state may be invalid and diagnosis is difficult. Handle understood cases and make unresolved failures visible appropriately.

### Misguided Development Habits

<!-- qard-id: ap-b62d6553ad096726815f -->
> [!qard]- Why is cargo-cult or unexplained copy-paste code risky?
> Its assumptions may not hold in the new context, and duplication spreads defects. Understand, adapt and test a solution before reusing it.

<!-- qard-id: ap-6ef6389779c96ee4e9e1 -->
> [!qard]- What distinguishes premature optimisation from useful optimisation?
> Premature optimisation adds complexity without measured benefit. Choose a sound algorithm, profile real workloads and optimise demonstrated bottlenecks.

<!-- qard-id: ap-d9321f8f30db9a351437 -->
> [!qard]- Why use a known good component rather than reinventing a solved problem?
> It can reduce development and validation effort, provided its quality, assumptions and suitability are checked.

### Generic Software Antipatterns

<!-- qard-id: ap-9c4078cbfbe44801d58f -->
> [!qard]- What is a stovepipe system, and how do standard components help?
> A one-off narrowly integrated system accumulates custom features with little reusable/shared infrastructure. Standard storage/interfaces/components reduce duplicated work and make integration and testing easier.

<!-- qard-id: ap-39bb76056d723eb486bd -->
> [!qard]- What is a data race, and what response does the lecture recommend?
> Concurrent conflicting access to shared data without required synchronisation, with at least one write. Simplify the concurrency model and use proven coordination/components rather than ad hoc timing assumptions; language consequences can be severe.

### Object-Oriented Antipatterns

<!-- qard-id: ap-f374b80a5f4927efc6be -->
> [!qard]- What does the circle–ellipse antipattern reveal about inheritance?
> A subtype may need different mutation invariants even when its mathematical set is a special case. Shared interfaces/composition can avoid pretending that incompatible behavioural contracts are substitutable.

### Programming Antipatterns

<!-- qard-id: ap-9430f12f7bf2ec2173e0 -->
> [!qard]- Why is using exceptions for ordinary branching called “coding by exception”?
> It turns expected control flow into hidden jumps and risks inappropriate handlers, overhead and obscured errors. Express normal choices through structured branches/functions and reserve failure mechanisms for the intended error policy.

### Diagnosing And Repairing Antipatterns

<!-- qard-id: ap-3c8a0a855dadbe46804f -->
> [!qard]- What distinguishes a useful pattern from cargo-cult application of its structure?
> A pattern responds to an actual problem/trade-off; cargo cult copies a named structure without understanding why its assumptions fit.

<!-- qard-id: ap-fee78042ba2dffec8303 -->
> [!qard]- Why does adding still more patterns not necessarily repair a big ball of mud?
> Without understood boundaries and decomposition, extra indirection merely obscures the same tangled responsibilities.

<!-- qard-id: ap-e910a261dc14cec5895b -->
> [!qard]- How does a shared database or standard interface address a stovepipe's data-sharing problem?
> It supplies a common representation/access boundary instead of another proprietary one-off path, enabling interoperability and reuse.

<!-- qard-id: ap-fcc1fd2e68568ad1d0e7 -->
> [!qard]- Why can a custom scripting “inner platform” become a security problem?
> It adds a programmable interpreter/execution surface requiring its own capability controls, sandboxing and validation, beyond the original application's simple options.

<!-- qard-id: ap-01c9ea3c84f91ed50a56 -->
> [!qard]- What is the key difference between a data race and a merely slow concurrent program?
> A race violates required coordination for conflicting shared accesses, threatening correctness; execution can be fast and still wrong.

<!-- qard-id: ap-c3928b045e5a1f0f2601 -->
> [!qard]- How can Observer help break direct circular dependencies?
> Depend on notification/subscription abstractions rather than having concrete peers call into each other's internals; review ownership and remaining dependency direction too.

<!-- qard-id: ap-27ebb1bfd91c1626436e -->
> [!qard]- Why does moving every responsibility into a god object not eliminate communication complexity?
> It hides the dependencies inside one large unit, increasing coupling and reducing cohesion/testability rather than removing the interactions.

<!-- qard-id: ap-f15beeaf369772c511c9 -->
> [!qard]- How can construction or an enforced algorithm sequence reduce temporal coupling?
> Make valid initialisation/ordering an internal guarantee rather than a hidden list of steps every external caller must remember.

<!-- qard-id: ap-a487d2837d2ea7511be1 -->
> [!qard]- Why is a “must call super” comment a weak correctness mechanism?
> An overriding method can omit the call without structural prevention; a fixed template sequence can invoke the required work automatically.

<!-- qard-id: ap-60244db1c42cb27f5ef1 -->
> [!qard]- How does unrestricted field access make invariants fragile?
> Every caller can create states the owning abstraction was supposed to forbid, and future representation changes affect all those callers.

<!-- qard-id: ap-d27d8397b62371aa310f -->
> [!qard]- Why is copy-paste with small variations difficult to maintain?
> Shared fixes must be repeated consistently, while differences are easy to miss. Extract the stable operation and make legitimate variation explicit.

<!-- qard-id: ap-162e41c7a61bb0d57bd5 -->
> [!qard]- What should replace a broad catch block that silently ignores every exception?
> Handle only understood recoverable cases, preserve appropriate diagnostics and propagate or report unresolved failures through the intended error policy.

<!-- qard-id: ap-93bb5512bdc02e5fc7c3 -->
> [!qard]- How does profiling distinguish an actual bottleneck from clever-looking optimisation?
> It measures cost under representative workloads, testing whether the proposed target contributes meaningfully to runtime.

<!-- qard-id: ap-de1cec9e9d59a16a2cfd -->
> [!qard]- What should be checked before reusing an existing solution rather than rebuilding it?
> Its assumptions, correctness, integration fit, maintenance and other applicable constraints; “already exists” is not evidence of quality by itself.
