---
tags:
  - advanced-programming
---

# Lazy Evaluation

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-2-LazyEvaluation.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-2-LazyEvaluation.pdf), James Gain, University of Cape Town, pages 1–10
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Lazy evaluation as outermost reduction plus sharing: redex selection, termination, thunks and infinite lists.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Lazy Evaluation Means|What Lazy Evaluation Means]]
  - [[#Evaluating Expressions: Innermost Versus Outermost|Evaluating Expressions: Innermost Versus Outermost]]
  - [[#Properties Of Redex Strategies|Properties Of Redex Strategies]]
  - [[#Example: Same Result, More Steps|Example: Same Result, More Steps]]
  - [[#Example: Same Result, Fewer Steps|Example: Same Result, Fewer Steps]]
  - [[#Sharing And Thunks|Sharing And Thunks]]
  - [[#Example: Termination|Example: Termination]]
  - [[#Infinite Lists|Infinite Lists]]
  - [[#Lazy Versus Strict Evaluation|Lazy Versus Strict Evaluation]]

---

## Core Content

### What Lazy Evaluation Means

#### Definitions

> **Lazy evaluation**: "Procrastination as an execution philosophy" — avoid unnecessary evaluation by delaying it as long as possible.

Lazy evaluation follows three rules:

1. Evaluate only **when needed**.
2. Evaluate only **enough** to satisfy the need.
3. Evaluate **at most once** — once a value is computed, it is never re-evaluated.

This allows programming with infinite lists.

### Evaluating Expressions: Innermost Versus Outermost

#### Definitions

> **Reduction (evaluation)**: Simplifying an expression by repeatedly applying definitions until no further simplification is possible.

> **Redex (reducible expression)**: A sub-expression that can be simplified by applying a definition.

> **Innermost reduction**: Always choose the innermost redex of a nested expression.

> **Outermost reduction**: Work from the outermost redex inwards.

In `f(g(h(…)))`, innermost reduction starts with `h`; outermost reduction starts with `f`.

![Innermost versus outermost redex](../../../diagrams/CSC3003S-Advanced%20Programming/FP/02_Lazy_Evaluation/redex-order.svg)

*Innermost evaluates arguments first; outermost applies the outer function first and evaluates arguments only if needed.*

### Properties Of Redex Strategies

Assuming pure functions:

| Property | Statement |
|---|---|
| **Termination** | Outermost reduction has the best termination behaviour. Strictly: if any reduction sequence terminates, outermost reduction also terminates. |
| **Equivalence** | If both orders terminate, they produce the same result (a variant of the **Church–Rosser theorem**). |
| **Cost** | Outermost may need more reduction steps, but it can also skip unnecessary evaluations. |

### Example: Same Result, More Steps

```haskell
square n = n * n
square (3+4)
```

| Innermost | Outermost |
|---|---|
| `square (3+4)` | `square (3+4)` |
| `= square 7` | `= (3+4) * (3+4)` |
| `= 7 * 7` | `= 7 * (3+4)` |
| `= 49` | `= 7 * 7` |
| | `= 49` |

Same result, but plain outermost reduction takes more steps because `(3+4)` is duplicated and evaluated twice.

### Example: Same Result, Fewer Steps

```haskell
square n = n * n
ignore x = "boondoggle"
ignore (square 5)
```

| Innermost | Outermost |
|---|---|
| `ignore (square 5)` | `ignore (square 5)` |
| `= ignore 25` | `= "boondoggle"` |
| `= "boondoggle"` | |

The result of `ignore` does not depend on its argument, so outermost reduction never evaluates `square 5`.

### Sharing And Thunks

#### Definitions

> **Sharing**: Ensuring the same expression is never evaluated more than once.

> **Thunk**: A heap data structure representing an unevaluated expression. Duplicates of the expression hold pointers to the same thunk, and the thunk is replaced with its value when evaluation is forced.

Sharing fixes the "more steps" problem of outermost reduction:

1. Each unique expression gets a matching thunk on the heap.
2. Every copy of the expression points to that thunk.
3. When evaluation is forced, the thunk is overwritten with its value, so all copies see the result.

```text
square (3+4) = (•) * (•)      both point to the thunk for (3+4)
             = (•) * (•)      thunk evaluated once → 7
             = 49
```

![Sharing with a thunk](../../../diagrams/CSC3003S-Advanced%20Programming/FP/02_Lazy_Evaluation/sharing-thunk.svg)

*Both operands point to one thunk; forcing it once updates it to 7 for every reference.*

Sharing is an example of **memoisation**.

### Example: Termination

```haskell
loop = tail loop
fst (1, loop)
```

| Innermost | Outermost |
|---|---|
| `fst (1, loop)` | `fst (1, loop)` |
| `= fst (1, tail loop)` | `= 1` |
| `= fst (1, tail (tail loop))` | |
| `= fst (1, tail (tail (tail loop)))` | |
| … never terminates | Terminates in 1 step |

Innermost reduction tries to evaluate `loop` before applying `fst`, and `loop` never finishes. Outermost applies `fst` first, which only needs the first component.

### Infinite Lists

Haskell supports potentially infinite lists, evaluated only as far as the context requires.

```haskell
ones :: [Int]   -- ones produces a list of integers
ones = 1 : ones -- recursively defined
```

```text
ones = 1 : ones
     = 1 : 1 : ones
     = 1 : 1 : 1 : ones
     = ...
```

A function such as `take 3 ones` forces only the first three cells, giving `[1,1,1]`.

### Lazy Versus Strict Evaluation

#### Definitions

> **Strict (eager) evaluation**: Arguments are evaluated before a function is called. Imperative languages generally use it.

$$
\text{Lazy evaluation} = \text{outermost reduction} + \text{sharing}
$$

| | Lazy evaluation | Strict evaluation |
|---|---|---|
| Order | Outermost, with sharing | Innermost (arguments first) |
| Steps | Never more than innermost, and possibly fewer | Evaluates arguments even when unused |
| Termination | Terminates whenever any order does | May loop on unused non-terminating arguments |
| Memory | Can use significantly more memory (thunks) | Lower memory overhead |
| Used by | Haskell | Most imperative languages |
