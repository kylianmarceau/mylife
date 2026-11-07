---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 18 — Aspect-Oriented Programming And Patterns Recap"
---

# ASD 18 — Aspect-Oriented Programming And Patterns Recap

**Source note:** [Aspect-Oriented Programming And Design Patterns Recap](../../ASD/18_Aspect_Oriented_Programming.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#AOP|AOP]]
  - [[#Patterns Recap|Patterns Recap]]

## Core Content

### AOP

<!-- qard-id: ap-7c9150872a2fba15d3c6 -->
> [!qard]- Why does aspect-oriented programming exist?
> To add operations (e.g. security checks) to an existing system that grew without the right design patterns.

<!-- qard-id: ap-ccea3e1cd3018bc7b97f -->
> [!qard]- What is a crosscutting concern?
> A requirement that applies across many unrelated classes and methods.

<!-- qard-id: ap-659e7e158cb39658faf6 -->
> [!qard]- Define advice, pointcut and aspect.
> Advice: code injected into methods. Pointcut: where it's injected. Aspect: advice + pointcut.

<!-- qard-id: ap-71bfd9820c12b7803f7a -->
> [!qard]- How are pointcuts specified?
> With patterns matching class names and method signatures, combined with AND/OR.

<!-- qard-id: ap-203e24f988afccdbcb26 -->
> [!qard]- Name the five kinds of advice.
> Before, after, around, after exception, after return.

<!-- qard-id: ap-ce1c6f80bb83abc264aa -->
> [!qard]- Dynamic versus static reflection for AOP?
> Dynamic: at run time using RTTI (injection). Static: compile-time search-and-replace on code (instrumentation).

<!-- qard-id: ap-bae10785c5c97da0f33f -->
> [!qard]- What is weaving, and how does AspectJ do it?
> Inserting aspects at their pointcuts; AspectJ uses a weaving compiler as an extra compile step.

<!-- qard-id: ap-4d3f9af5b4e523a43533 -->
> [!qard]- Give three pros of AOP.
> Modular crosscutting additions, DRY reuse, easy patching of existing code (plus SOLID, testability).

<!-- qard-id: ap-71a1b0621cf9aa58e2e1 -->
> [!qard]- Give three cons of AOP.
> Harder debugging, potentially very complex crosscuts, poor tooling visibility and portability (best in Java).

### Patterns Recap

<!-- qard-id: ap-2606d6090aa2385ab289 -->
> [!qard]- Why do the creational patterns exist?
> They work around object-creation limits (no virtual constructors, shallow copies, global access).

<!-- qard-id: ap-ff2d9302870b977ba1d6 -->
> [!qard]- Builder versus abstract factory?
> Builder constructs one complex object in stages; abstract factory creates families of related objects.

<!-- qard-id: ap-10b9e9c0276a58e1d051 -->
> [!qard]- Which design pattern is now obsolete, and what replaces it?
> Flyweight — replaced by data-oriented design.

<!-- qard-id: ap-086d98c38efa3ccae47e -->
> [!qard]- Rank the four visitor variants.
> Variant visitor (best), classic cyclic visitor (pure OOP), acyclic visitor (slow), procedural visitor (don't use).

<!-- qard-id: ap-39bd425b98105e50695c -->
> [!qard]- How do lambdas simplify Command, Strategy and Observer?
> Command: a lambda per action. Strategy: a lambda steers the algorithm. Observer: a lambda per subscription.

<!-- qard-id: ap-ee3223d3ffed4a5f93c0 -->
> [!qard]- How do lambdas simplify Template Method and Chain of Responsibility?
> Template: a lambda per step. Chain: a lambda per message handler.

<!-- qard-id: ap-5290b14acfca1a1e32c9 -->
> [!qard]- How much does a mediator reduce communication links?
> From $\frac{n^2-n}{2}$ to $n+1$.

<!-- qard-id: ap-cd1886c60ba484b19d03 -->
> [!qard]- What is a join point?
> A specific point in program execution (such as a method call) where advice can run; a pointcut selects a set of join points.
