---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 11 — Haskell 7 — Point-Free Programming"
---

# FP 11 — Haskell 7 — Point-Free Programming

**Source note:** [Haskell 7 — Point-Free Programming](../../FP/11_Point_Free_Programming.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Composition|Composition]]
  - [[#Many Styles, One Output|Many Styles, One Output]]
  - [[#Rewriting isPrime As A Composition|Rewriting isPrime As A Composition]]
  - [[#Eliminating Arguments Carefully|Eliminating Arguments Carefully]]

## Core Content

### Composition

<!-- qard-id: ap-a48aadd5d0c23c009622 -->
> [!qard]- What does point-free programming omit?
> Explicit names for a function's arguments, expressing the function through composition and partial application instead.

<!-- qard-id: ap-20d7266ea1a9be372140 -->
> [!qard]- What is the definition and type of `(.)`?
> `(f . g) x = f (g x)`; `(.) :: (b -> c) -> (a -> b) -> a -> c`. The rightmost function acts first.

<!-- qard-id: ap-f139da688b385d448f90 -->
> [!qard]- When can `h x = f (g x)` become `h = f . g`?
> When the types align and `x` is only passed through that pipeline, so removing the explicit argument preserves the same mapping.

<!-- qard-id: ap-edc514afab6868e58015 -->
> [!qard]- What is the difference between `f . g` and `f $ g x`?
> The first constructs a composed function; the second applies `f` to the value `g x`.

<!-- qard-id: ap-c8882df90b83cc8c8bc8 -->
> [!qard]- How is vector magnitude expressed point-free?
> `magnitude = sqrt . sum . map (^2)`: square components, sum them, then take the square root.

<!-- qard-id: ap-b671edac395d21a04c51 -->
> [!qard]- What is the main trade-off of point-free code?
> Simple pipelines can be clearer, but complex composition can hide data dependencies and make types harder to follow; prefer the more readable form.

<!-- qard-id: ap-2621ee99929afdebf9f3 -->
> [!qard]- Why check boundary and indexing conventions when rewriting a search as a pipeline?
> `[start..]` may include the starting value, and `!!` is zero-based; a recursive version may search strictly after `start` and count from one.

### Many Styles, One Output

<!-- qard-id: ap-c2c2508a67051c34df0a -->
> [!qard]- How do `where` and `let ... in ...` differ syntactically?
> `where` attaches local definitions to an equation; `let ... in ...` is itself an expression that can appear wherever an expression is needed. Neither implies mutable assignment.

### Rewriting isPrime As A Composition

<!-- qard-id: ap-51843992c50d1106fce9 -->
> [!qard]- How does `all ((/= 0) . mod n) [2..n-1]` replace the prime-testing lambda?
> `mod n` fixes the dividend; composition tests whether each resulting remainder differs from zero. It equals ``all (\d -> n `mod` d /= 0) [2..n-1]`` for the intended candidate range.

### Eliminating Arguments Carefully

<!-- qard-id: ap-90d274549260a8beaf68 -->
> [!qard]- Why does `(f . g)` require `g`'s result type to match `f`'s input type?
> The composed function passes that result directly as the next argument; type mismatches expose an invalid pipeline.

<!-- qard-id: ap-c29b197e4c978d95dbad -->
> [!qard]- How does partial application help turn a multi-argument expression into a composition?
> Fix known arguments so each pipeline stage accepts the one value supplied by the preceding stage; the result can itself be a function awaiting later arguments.

<!-- qard-id: ap-15e5a2d6aac710d2982e -->
> [!qard]- Is point-free style defined by using the dot operator?
> No. It is defined by omitting explicit argument names. `add = (+)` is point-free without any dot.

<!-- qard-id: ap-be7336973374f83db20b -->
> [!qard]- When is `f x = g x` safely shortened to `f = g` in ordinary code refactoring?
> When the explicit parameter is just passed to that same function and the intended types/behaviour remain the same; do not remove parameters used for additional computation or branching.

<!-- qard-id: ap-ac19f10442e1abac4a23 -->
> [!qard]- Why does using one input in several positions make point-free conversion harder?
> A simple linear pipeline no longer expresses the data dependency; extra combinators can conceal the relationship and reduce readability.

<!-- qard-id: ap-11a47c1788a68a4987ee -->
> [!qard]- How do operator sections affect operand order?
> `(/2)` divides its later argument by two, while `(2/)` divides two by its later argument. Removing named arguments must preserve which operand is fixed.

<!-- qard-id: ap-884c2376dee1bef23d64 -->
> [!qard]- How can you check a dense point-free expression without guessing from its appearance?
> Expand composition and sections to explicit applications/lambdas, infer the intermediate types, and verify boundary/indexing conventions.

<!-- qard-id: ap-aaca6ce4b945448c0769 -->
> [!qard]- What makes a point-free rewrite worthwhile?
> It clarifies the composition of meaningful operations and reduces unnecessary plumbing without hiding the relation between inputs and results.
