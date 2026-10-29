---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 13 — Haskell 9 — Making Illegal States Unrepresentable"
---

# FP 13 — Haskell 9 — Making Illegal States Unrepresentable

**Source note:** [Haskell 9 — Making Illegal States Unrepresentable](../../FP/13_Making_Illegal_States_Unrepresentable.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Designing Safer Types|Designing Safer Types]]
  - [[#Applications: Parse, Don't Validate|Applications: Parse, Don't Validate]]
  - [[#Preserving Invariants Through Types|Preserving Invariants Through Types]]

## Core Content

### Designing Safer Types

<!-- qard-id: ap-0f42993d852c2beafbaf -->
> [!qard]- What does making illegal states unrepresentable mean?
> Design types whose values encode valid states and combinations, so invalid ones cannot be constructed through the intended API.

<!-- qard-id: ap-8b757bee35325f59e14b -->
> [!qard]- How do distinct unit wrapper types prevent mistakes?
> A function expecting `Inches` cannot silently receive `Centimetres`; conversions must be explicit, unlike using a plain number for both.

<!-- qard-id: ap-60bd3ab0a857d5bd5e15 -->
> [!qard]- Why use a sum type for Draft, Sent, Delivered and Read message states?
> Each constructor carries exactly the data required by that state, preventing combinations such as a read timestamp with no sent timestamp.

<!-- qard-id: ap-05c907a6fc4ae6fb907b -->
> [!qard]- Does a message-state sum type automatically enforce timestamp order?
> No. It enforces the presence of fields; checks or a stronger abstraction are still needed to guarantee their chronological order.

<!-- qard-id: ap-aa6a89fbffd3ce69734f -->
> [!qard]- How does `data NonEmptyList a = NonEmptyList a [a]` make `head` safe?
> Every value contains a mandatory first element, so extracting it never encounters an empty case.

<!-- qard-id: ap-48318d5753d44d87ca70 -->
> [!qard]- How can a type require exactly one or two values?
> `data AtLeastOne a = One a | Two a a`; neither constructor represents zero values.

<!-- qard-id: ap-d01cc860e4582295bf60 -->
> [!qard]- What does “parse, don't validate” recommend?
> Check raw input at a boundary and convert it to a constrained type. Downstream functions consume that type rather than repeatedly checking the raw representation.

<!-- qard-id: ap-aaeb0dc7255998425093 -->
> [!qard]- What must a validated email type's API prevent?
> Bypassing validation through unrestricted construction; expose a checked constructor and keep invalid raw values out of the type.

<!-- qard-id: ap-889597ea64ef61411c1f -->
> [!qard]- What is the practical limit of encoding constraints in types?
> Balance safety against complexity and interoperability; elaborate wrappers may need extra instances and make ordinary use harder.

### Applications: Parse, Don't Validate

<!-- qard-id: ap-dc27cc7f9efb2450b5a0 -->
> [!qard]- Why can a Boolean validation result be weaker than returning a parsed constrained type?
> The Boolean does not carry the checked value's guarantee into later function signatures; returning a validated value preserves the evidence and prevents repeated scattered checks (“shotgun parsing”).

### Preserving Invariants Through Types

<!-- qard-id: ap-bb0d4baaed2c2467ad32 -->
> [!qard]- Why is a distinct wrapper stronger than a type synonym for preventing unit mix-ups?
> A synonym merely renames the same underlying type; a distinct wrapper requires deliberate conversion and rejects using one unit where another is expected.

<!-- qard-id: ap-13513f38a025f017491b -->
> [!qard]- What must a unit conversion function make explicit?
> The source/target unit types and the numerical conversion rule, so a caller cannot silently mix their representations.

<!-- qard-id: ap-f949b3f7bad11087caac -->
> [!qard]- Why do several independent `Maybe` fields create invalid combinations?
> Each field can be absent/present independently, even when the domain requires them to appear together or in a state-dependent sequence.

<!-- qard-id: ap-7b05f5eeb15545212057 -->
> [!qard]- How does choosing one state constructor encode mutually exclusive alternatives?
> A value can be Draft, Sent, Delivered or Read, with only that constructor's fields. It cannot simultaneously be incompatible alternatives.

<!-- qard-id: ap-cd13bce7ea69f7b68a93 -->
> [!qard]- What guarantee does `NonEmptyList a` provide that `[a]` does not?
> Construction requires a head element; functions requiring one can express that precondition in their input type rather than fail on an empty runtime case.

<!-- qard-id: ap-30dd75319a4902b5ab01 -->
> [!qard]- Does giving a type a meaningful name ensure its invariant is enforced?
> No. If arbitrary invalid payloads can be constructed, the name is documentation only. Restrict construction or validate at a controlled boundary.

<!-- qard-id: ap-262e0cb6e1e420f557cc -->
> [!qard]- Why should downstream functions accept the parsed domain type rather than the raw string again?
> Their signatures preserve and use the already-established guarantee, avoiding repeated checks and accidental use of unchecked input.

<!-- qard-id: ap-95fa6933432f02d4f5bc -->
> [!qard]- What kind of error can remain even after invalid data combinations are removed?
> An incorrect algorithm, wrong conversion formula, invalid transition rule or nontermination. Type modelling prevents targeted classes of errors, not every possible bug.

<!-- qard-id: ap-b70d881385fb2e9face0 -->
> [!qard]- Why can increasingly refined types make ordinary reuse harder?
> Existing operations/instances may be defined for the underlying type rather than the refined wrapper; maintaining the abstraction can require explicit adapters and implementations.
