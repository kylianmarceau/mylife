---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 17 — Design Patterns II: Clean Code And The Visitor"
---

# ASD 17 — Design Patterns II: Clean Code And The Visitor

**Source note:** [Design Patterns II: Clean Code And The Visitor](../../ASD/17_Clean_Code_And_Visitor.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Readable And Maintainable Code|Readable And Maintainable Code]]
  - [[#Visitor Choices|Visitor Choices]]
  - [[#Const Correctness|Const Correctness]]
  - [[#Procedural Alternative|Procedural Alternative]]
  - [[#Performance And Recap|Performance And Recap]]
  - [[#Clean Code Principles|Clean Code Principles]]
  - [[#Classic Visitor|Classic Visitor]]
  - [[#Alternatives|Alternatives]]

## Core Content

### Readable And Maintainable Code

<!-- qard-id: ap-534a0e53e0943ffb650a -->
> [!qard]- How do DRY and OneTask improve maintenance?
> Shared logic lives in one place, and each unit has a focused purpose, reducing inconsistent edits and unrelated reasons for change.

<!-- qard-id: ap-f0070b8c8ab5ad258a9a -->
> [!qard]- What makes a useful name for a function or long-lived variable?
> It expresses purpose and, where relevant, units; function names commonly use verb–object form, and wider scope warrants more descriptive names.

<!-- qard-id: ap-6c9ac864f006af0abea0 -->
> [!qard]- What should comments explain, and why remove commented-out code?
> Explain intent, constraints and reasons that the code cannot express clearly. Version control retains old code without leaving stale clutter in the current implementation.

<!-- qard-id: ap-74caf2984868c17c1642 -->
> [!qard]- Why replace a magic constant with a meaningful named constant?
> It documents meaning and units and centralises changes, avoiding unexplained repeated literals.

### Visitor Choices

<!-- qard-id: ap-52e24e556eed3b2c1639 -->
> [!qard]- What problem does classic Visitor solve?
> Add operations over a relatively stable type hierarchy without putting each operation's implementation into every type's class.

<!-- qard-id: ap-555a90401c3ab9ff595a -->
> [!qard]- How does Visitor use double dispatch?
> Call `element.accept(visitor)`; the concrete element then calls `visitor.visit(this)`, selecting behaviour for both the element kind and operation.

<!-- qard-id: ap-48fe91c05acc39a1bbf2 -->
> [!qard]- What is classic Visitor's main extension trade-off?
> Adding a new operation/visitor is easy, but adding an element type requires extending the visitor interface and relevant visitors.

<!-- qard-id: ap-2057fa37314061f8c399 -->
> [!qard]- Why does classic Visitor create cyclic dependencies?
> Elements know the visitor interface, while that interface names concrete element types, linking the two hierarchies in both directions.

<!-- qard-id: ap-34b218583d01279e1d53 -->
> [!qard]- What do `std::variant` and `std::visit` provide?
> A type-safe value holding one of a fixed set of alternatives, plus application of a callable matching the current alternative, without requiring a shared virtual base hierarchy.

<!-- qard-id: ap-17f4162597ecf7b489f7 -->
> [!qard]- Does adding an alternative to a variant automatically update every operation?
> No. Each operation must still handle the relevant alternatives, but the types need not themselves depend on the operations.

<!-- qard-id: ap-8788f46f8b5a44989c9c -->
> [!qard]- What is a memory trade-off of storing alternatives directly in a variant?
> Each value must accommodate its largest alternative plus a tag/alignment; combining very large and small alternatives can waste space.

<!-- qard-id: ap-4fcc8cc397292c1bc703 -->
> [!qard]- How does an acyclic Visitor break the dependency cycle, and at what cost?
> Separate per-type visitor interfaces and runtime casts decouple the base element from concrete visitors, but add runtime checking/dispatch overhead.

### Const Correctness

<!-- qard-id: ap-dc29f2e0465f1b9fe273 -->
> [!qard]- How does restricting mutation improve reasoning without alone guaranteeing purity?
> It reduces state changes through a given interface and helps isolate accidental writes. A fixed binding can still refer to mutable data, and a function may still perform external effects.

### Procedural Alternative

<!-- qard-id: ap-78e303cdf06cb7db8d6a -->
> [!qard]- Why does the lecture criticise a growing type-tag switch as a replacement for Visitor?
> Each new element kind forces edits across operations, increasing scattered knowledge and maintenance risk. A small closed choice may still be manageable; the concern is uncontrolled growth and coupling.

### Performance And Recap

<!-- qard-id: ap-76d1eaef00fc860392bb -->
> [!qard]- How should the Visitor/variant performance examples influence a design choice?
> Compare indirection, casts, representation size and actual measured workload. The lecture favours variants in many C++ scenarios, but chart results are implementation-specific rather than universal guarantees.

### Clean Code Principles

<!-- qard-id: ap-44b08f0362d631fd11d0 -->
> [!qard]- Why can reducing variable scope improve clarity and correctness?
> It limits where the binding can be used/changed and reduces the state readers must track at each point.

<!-- qard-id: ap-420d3ac51e0a5e53f03b -->
> [!qard]- Why include units in a measurement's name or type?
> It exposes meaning and helps prevent incompatible quantities being combined or passed to the wrong operation.

<!-- qard-id: ap-91adb539e316f7213f55 -->
> [!qard]- Why can naming a constant improve DRY as well as readability?
> It gives the meaning one authoritative definition so repeated uses do not drift when the value changes.

<!-- qard-id: ap-03cf31518f2ebbbad403 -->
> [!qard]- What is the risk of a comment merely restating complicated code?
> It can become stale while leaving the implementation difficult to understand; clarify the code and reserve comments for reasons/constraints not evident from it.

<!-- qard-id: ap-5c9f8dbcda0424ee2e5e -->
> [!qard]- How does OneTask apply below the class level?
> A routine should perform one coherent operation, taking only the data it needs rather than mixing unrelated actions and parameters.

### Classic Visitor

<!-- qard-id: ap-959ce9a11f1ea3433b11 -->
> [!qard]- Why can OO hierarchies make adding a new operation awkward?
> The operation's implementation may need edits in each existing type, while ordinary subclass extension mainly makes adding another type convenient.

<!-- qard-id: ap-1d66b1ccbfeee7000459 -->
> [!qard]- Where does a classic Visitor place the varying operation's implementation?
> In the visitor class's type-specific visit methods, while elements expose an `accept` entry point to dispatch to the appropriate method.

<!-- qard-id: ap-f505401d24ab85efd702 -->
> [!qard]- Why is a new element type expensive for an exhaustive Visitor interface?
> The interface and existing concrete visitors may need a method/implementation for the new kind, propagating changes across the operation dimension.

<!-- qard-id: ap-e19b05f4a515e972aeaf -->
> [!qard]- What limits a visitor that can use only each element's public interface?
> An operation needing hidden representation details may require new exposed operations or another design, balancing extensibility against information hiding.

### Alternatives

<!-- qard-id: ap-89b2492bc6b6e2a74ac4 -->
> [!qard]- How does a tagged union express a closed set of element alternatives?
> The value has exactly one active tagged alternative from the declared list; operations dispatch over that set rather than through a shared virtual class hierarchy.

<!-- qard-id: ap-a189464ae0f0e006c9be -->
> [!qard]- Why can a variant remove the element-to-operation dependency?
> Plain element data need not mention each visitor/operation; the variant and external callables depend on the data types instead.

<!-- qard-id: ap-40fd69398338b5c968d7 -->
> [!qard]- Why does adding a new operation with `std::visit` not require changing every element type?
> Define another callable handling the variants; the existing data representations need no new virtual method or `accept` overload.

<!-- qard-id: ap-8d70c87dc0390d2163b3 -->
> [!qard]- What does an acyclic visitor do if a visitor does not implement the interface for an element type?
> Its runtime cast does not find that supported visitor interface; the implementation must define the intended no-op/failure behaviour rather than assume every operation supports every type.

<!-- qard-id: ap-bbb935fa56d112b7ff73 -->
> [!qard]- Why can runtime casts be a cost of acyclic Visitor's added flexibility?
> Each accepted operation may need runtime interface/type discovery rather than a direct known call; measure whether that matters for the workload.

<!-- qard-id: ap-6570f1516ea661d6edc7 -->
> [!qard]- How does Memento differ from Visitor's purpose?
> Memento preserves/restores state without exposing private details; Visitor organises new operations across element types. They solve different extension/state problems even when used together.
