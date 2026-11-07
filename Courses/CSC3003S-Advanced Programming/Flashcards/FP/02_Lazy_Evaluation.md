---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 02 — Lazy Evaluation"
---

# FP 02 — Lazy Evaluation

**Source note:** [Lazy Evaluation](../../FP/02_Lazy_Evaluation.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Lazy Evaluation|Lazy Evaluation]]
  - [[#Redexes And Reduction Order|Redexes And Reduction Order]]
  - [[#Sharing And Thunks|Sharing And Thunks]]

## Core Content

### Lazy Evaluation

<!-- qard-id: ap-e3ef38ddfedbd1195286 -->
> [!qard]- What are the three rules of lazy evaluation?
> Evaluate only when needed, only as much as needed, and at most once.

<!-- qard-id: ap-b3f912fcdbf15dd880bd -->
> [!qard]- State lazy evaluation as an equation.
> Lazy evaluation = outermost reduction + sharing.

<!-- qard-id: ap-9fe0eb2ca5ab75d63d5a -->
> [!qard]- What is strict (eager) evaluation?
> Evaluating arguments before calling a function — used by most imperative languages.

<!-- qard-id: ap-d3ffae90a1bf051ffaee -->
> [!qard]- What capability does laziness enable that strict evaluation can't?
> Working with infinite data structures, evaluated only as far as needed.

### Redexes And Reduction Order

<!-- qard-id: ap-28b485de4b1f28c2327c -->
> [!qard]- What is a redex?
> A reducible expression — a sub-expression that can be simplified by applying a definition.

<!-- qard-id: ap-335c2d2d54cf31a0625c -->
> [!qard]- Innermost versus outermost reduction?
> Innermost reduces the innermost redex first (arguments before functions); outermost applies the outer function first.

<!-- qard-id: ap-2db8f63f48c33d46e3ad -->
> [!qard]- Which reduction order has the best termination behaviour?
> Outermost: if any order terminates, outermost does too.

<!-- qard-id: ap-f2e37b4219db0f28ed68 -->
> [!qard]- If innermost and outermost both terminate, do they give the same result?
> Yes (a variant of the Church–Rosser theorem), for pure functions.

<!-- qard-id: ap-e556146e938230a98e72 -->
> [!qard]- Why can plain outermost reduction take more steps?
> It can duplicate an unevaluated argument (e.g. `(3+4)*(3+4)`) and evaluate it more than once.

<!-- qard-id: ap-f563751c0318fa159030 -->
> [!qard]- Why does outermost reduction sometimes take fewer steps?
> It never evaluates arguments the function doesn't use.

<!-- qard-id: ap-36409b6cd84175e45cf0 -->
> [!qard]- Why does `fst (1, loop)` terminate lazily but not strictly?
> Outermost applies `fst` first and never needs `loop`; innermost tries to evaluate `loop` forever.

### Sharing And Thunks

<!-- qard-id: ap-b53d9795982cab152bd1 -->
> [!qard]- What is a thunk?
> A heap structure for an unevaluated expression; all copies point to it and it is overwritten with its value once forced.

<!-- qard-id: ap-8d59d1f1fccd54da571f -->
> [!qard]- What does sharing achieve?
> Each expression is evaluated at most once — a form of memoisation.

<!-- qard-id: ap-e58547def3760761e6a0 -->
> [!qard]- What is the main cost of lazy evaluation?
> Significantly more memory, because of thunks.

<!-- qard-id: ap-3ca3743b2e8f3607182f -->
> [!qard]- How is the infinite list `ones` defined, and why is it usable?
> `ones = 1 : ones`; only the cells demanded (e.g. by `take 3`) are ever built.
