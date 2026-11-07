---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 17 — Clean Code And The Visitor Pattern"
---

# ASD 17 — Clean Code And The Visitor Pattern

**Source note:** [Design Patterns II: Clean Code And The Visitor Pattern](../../ASD/17_Clean_Code_And_Visitor.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Clean Code|Clean Code]]
  - [[#Visitor|Visitor]]

## Core Content

### Clean Code

<!-- qard-id: ap-7a9e70f806b4a65a5037 -->
> [!qard]- Name the six clean-coding principles.
> DRY, one task per function, meaningful names, no littering, no magic constants, const correctness.

<!-- qard-id: ap-c92f7004a0b975a09f0c -->
> [!qard]- What is DRY?
> Don't repeat yourself — extract shared steps into functions.

<!-- qard-id: ap-a67edb5b4914cce43852 -->
> [!qard]- What naming rules make code readable?
> `verbNoun` functions, multi-noun variables with units, name length matching scope, consistent names, no Hungarian notation.

<!-- qard-id: ap-8e5520aab78b144f5365 -->
> [!qard]- What does "no littering" mean?
> Remove commented-out code (use git); comments explain why, code explains how/what.

<!-- qard-id: ap-7d7aa94e1c0cbfbe74e8 -->
> [!qard]- What is a magic constant, and why name it?
> A naked number or string; naming clarifies intent, keeps it in one place and lets you document it.

<!-- qard-id: ap-05036ac8b4de959b9f01 -->
> [!qard]- What does const correctness enable?
> Pure functions, easier reasoning and debugging, and compiler optimisation.

### Visitor

<!-- qard-id: ap-7b82fabed195f110f03d -->
> [!qard]- What problem does the Visitor pattern solve?
> Adding operations to a type hierarchy without changing the types (OOP makes types easy but operations hard).

<!-- qard-id: ap-86004077c9f2f3d3e895 -->
> [!qard]- How does the classic visitor work?
> Each type's `accept(v)` calls `v.visit(this)`; each operation is a visitor class with a `visit` per type (double dispatch).

<!-- qard-id: ap-dfde406478af7c940fed -->
> [!qard]- Give the visitor's pros and cons.
> Pros: easy to add operations (OCP), hides implementation (SRP). Cons: hard to add types, public interface only, needs heap/virtuals, cyclic dependency.

<!-- qard-id: ap-adbc0e525edb8a38ba31 -->
> [!qard]- Why is the procedural switch alternative bad?
> Every new type means editing every switch — unmaintainable.

<!-- qard-id: ap-649e20dcd8104dc56c9a -->
> [!qard]- How do `std::variant` and `std::visit` replace the visitor?
> The variant holds one of several types by value; `std::visit` calls the matching overload of an operation object.

<!-- qard-id: ap-4ee8cd2ce04cef848e57 -->
> [!qard]- Give three advantages of `std::variant` + `std::visit`.
> No cycles, easy to add both types and operations, no heap or virtual calls — and faster.

<!-- qard-id: ap-554af829fbc28c038901 -->
> [!qard]- What are the drawbacks of `std::variant`?
> Mixing big and small types wastes space (fix with Proxy), and it hides implementation details poorly.

<!-- qard-id: ap-0e6151787c42fa312fc0 -->
> [!qard]- What is the acyclic visitor?
> Splits the visitor into an empty base plus one `Visitor<T>` per type, breaking the cycle via run-time casts.

<!-- qard-id: ap-6a5fd8eda0c7fdec4247 -->
> [!qard]- Why is the acyclic visitor slow?
> `dynamic_cast` walks the inheritance tree on every visit.

<!-- qard-id: ap-c1a52c498997cf4e5108 -->
> [!qard]- Which visitor approach should you prefer?
> `std::variant` + `std::visit` in most cases; acyclic if overhead doesn't matter (and in Java there's no other choice).

<!-- qard-id: ap-ec0818b819b253cdd23c -->
> [!qard]- What does the OneTask principle say?
> A function or class should do one thing, taking only the parameters that task needs — SRP at function level.
