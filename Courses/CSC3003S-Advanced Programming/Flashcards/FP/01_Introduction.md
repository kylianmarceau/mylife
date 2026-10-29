---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 01 — Functional Programming — Introduction"
---

# FP 01 — Functional Programming — Introduction

**Source note:** [Functional Programming — Introduction](../../FP/01_Introduction.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Functional Programming Foundations|Functional Programming Foundations]]
  - [[#Benefits And Costs|Benefits And Costs]]
  - [[#Functional Programming Style|Functional Programming Style]]
  - [[#Industry Use And Mixing Paradigms|Industry Use And Mixing Paradigms]]
  - [[#Example: The Countdown Problem|Example: The Countdown Problem]]
  - [[#Course Structure, Evaluation And Readings|Course Structure, Evaluation And Readings]]
  - [[#Purity, State And Types|Purity, State And Types]]

## Core Content

### Functional Programming Foundations

<!-- qard-id: ap-0f4fad8dadffc3dd152e -->
> [!qard]- What defines functional programming?
> Declarative computation through applying and composing functions, emphasising pure functions, immutable data and first-class functions.

<!-- qard-id: ap-b89e0bd29624a575ff21 -->
> [!qard]- How does declarative programming differ from imperative programming?
> Declarative code states the desired result or relationships; imperative code explicitly controls the sequence of state-changing steps.

<!-- qard-id: ap-b75818e66b0bcbf965ae -->
> [!qard]- What makes a function pure?
> It returns the same result for the same inputs and has no externally observable side effects.

<!-- qard-id: ap-8f9411178f9d2c7047aa -->
> [!qard]- What is referential transparency, and why does purity enable it?
> An expression can be replaced by its value without changing program behaviour, because evaluating it has no hidden effects or dependencies.

<!-- qard-id: ap-89f0d800587475554fae -->
> [!qard]- What are examples of impurity?
> Reading changing external state, mutating shared data, performing I/O, or obtaining the current time; the computation has dependencies or effects beyond its explicit result.

<!-- qard-id: ap-b793fffd8366f4b478eb -->
> [!qard]- What does immutability require when updating a collection?
> Construct a new value and pass it forward; the original collection remains unchanged. Unchanged parts can be shared.

<!-- qard-id: ap-0760ba1988362af81fb1 -->
> [!qard]- What does it mean for functions to be first-class?
> They can be stored, passed as arguments and returned as results, like other values.

### Benefits And Costs

<!-- qard-id: ap-b825d5313348bb778fd8 -->
> [!qard]- Why do purity and immutability help parallel programming?
> Independent computations can share data without one changing what another reads, reducing shared-state coordination and making behaviour easier to reason about.

<!-- qard-id: ap-7fc2b4f415a069ca47cb -->
> [!qard]- Why are pure functions easier to test?
> Their behaviour depends on explicit inputs, so they can be tested in isolation without reconstructing hidden mutable state.

<!-- qard-id: ap-64a09605708c76141bfc -->
> [!qard]- What are the main potential costs of a functional style?
> Allocation, recursion and delayed computations can add memory or runtime overhead; high abstraction can reduce control over execution.

<!-- qard-id: ap-40752da1485120f745b2 -->
> [!qard]- What are Haskell's main characteristics?
> It is a pure functional language with non-strict evaluation (usually implemented lazily), static typing and type inference.

<!-- qard-id: ap-bceed7228a8b85140493 -->
> [!qard]- Does type inference make Haskell dynamically typed?
> No. Inference discovers types automatically, but Haskell checks them at compile time.

<!-- qard-id: ap-087ab68d37d7b497d58b -->
> [!qard]- How do computational and memory overhead differ in functional code?
> Computational overhead is extra execution work from abstraction/indirection; memory overhead includes allocations, retained thunks and pending recursive work. A technique may improve one while worsening the other.

<!-- qard-id: ap-74c00b46ba5e1fc0293e -->
> [!qard]- Why can eliminating shared mutation reduce the need for locks?
> Independent readers cannot race with writes to the same immutable data. External resources and explicitly stateful coordination can still require synchronisation.

<!-- qard-id: ap-08306fd1f610cf825c9f -->
> [!qard]- Why do lambdas in a mutable language not automatically provide all the benefits of pure FP?
> The lambda can capture and change external state, and its inputs can still be mutated. Passing functions is only one part of the purity/immutability discipline.

### Functional Programming Style

<!-- qard-id: ap-a119c40cf14c18feff57 -->
> [!qard]- What replaces mutation, loops and explicit control flow in a typical functional solution?
> New immutable values, recursion/list combinators, and composition of transformations into a data-flow pipeline.

### Industry Use And Mixing Paradigms

<!-- qard-id: ap-5357ce0af176a2252146 -->
> [!qard]- Why might finance, messaging or language-processing systems use functional techniques?
> Type-safe/predictable transformations, concurrent processing of shared immutable data and natural composition. Adding lambdas to an imperative language supplies useful tools but does not itself enforce purity.

### Example: The Countdown Problem

<!-- qard-id: ap-7e7946321312b610f048 -->
> [!qard]- What constraints and optimisations define the Countdown example?
> Build a target expression from given numbers, each used at most once, using $+,-,\times,\div$ with positive-integer intermediate values. Generate candidates, reject invalid partial expressions early, and exploit laziness to stop when only one solution is needed.

### Course Structure, Evaluation And Readings

<!-- qard-id: ap-95107cf627383d0cc070 -->
> [!qard]- What does the FP course expect beyond remembering definitions?
> Understand FP foundations, lazy evaluation/lambda calculus, practical Haskell and comparison with other paradigms; practise writing and explaining code unaided, because controlled assessments test that understanding.

### Purity, State And Types

<!-- qard-id: ap-d3a44eadb5a1df9db496 -->
> [!qard]- Can a function return the same output each time and still be impure?
> Yes. It might always return the same value while also writing a file, printing or mutating shared state. Determinism alone is insufficient for purity.

<!-- qard-id: ap-7e519244faa1acf17f38 -->
> [!qard]- What is a hidden input or “side cause” of a function?
> External state read during evaluation, such as a global variable or clock, that affects behaviour without appearing among the explicit arguments.

<!-- qard-id: ap-02cfb363539120e14eb9 -->
> [!qard]- Why does purity permit changing evaluation order for independent expressions?
> With no hidden state changes, evaluating one cannot change the other's value. Data dependencies and termination/demand requirements still constrain useful evaluation.

<!-- qard-id: ap-59d5330f64d0dbe7cfa9 -->
> [!qard]- How does static typing differ from dynamic typing without relying on explicit annotations?
> Static systems check compatible types before execution; dynamic systems check values/types during execution. Either may infer information automatically, so annotation syntax is not the defining distinction.

<!-- qard-id: ap-c7f3edb8260b2fb25d33 -->
> [!qard]- Why can immutable data be shared without copying every element?
> A new structure can point to unchanged portions of the old one. Since neither may mutate them, sharing preserves both values' meaning.

<!-- qard-id: ap-d875df793c42c428ceb2 -->
> [!qard]- What is a higher-order function compared with a first-class function?
> First-class describes functions being usable as values; higher-order describes a function that accepts or returns a function. The first capability enables the second pattern.
