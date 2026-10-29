---
tags:
  - advanced-programming
---

# Lazy Evaluation

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-2-LazyEvaluation.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-2-LazyEvaluation.pdf), James Gain, University of Cape Town, PDF pages 1–10  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes on reduction order, sharing, and infinite lists.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Lazy Evaluation Defined|Lazy Evaluation Defined]]
  - [[#Evaluating Expressions: Innermost And Outermost|Evaluating Expressions: Innermost And Outermost]]
  - [[#Redex Features: Termination, Equivalence, Cost|Redex Features: Termination, Equivalence, Cost]]
  - [[#Redex Examples|Redex Examples]]
  - [[#Sharing With Thunks|Sharing With Thunks]]
  - [[#Infinite Lists|Infinite Lists]]
  - [[#Lazy Versus Strict Evaluation|Lazy Versus Strict Evaluation]]

---

## Core Content

### Lazy Evaluation Defined

#### Definitions

> **Lazy evaluation**: An execution strategy that avoids unnecessary evaluation by delaying it as long as possible. It is "procrastination as an execution philosophy."

Lazy evaluation follows three rules:

1. **Evaluate only when needed**: an expression is evaluated only when its value is demanded.
2. **Evaluate only enough**: evaluate only as much of a structure as the context requires.
3. **Evaluate at most once**: never re-evaluate an expression that has already been evaluated.

Together these rules let you program with **infinite lists**.

### Evaluating Expressions: Innermost And Outermost

#### Definitions

> **Evaluation (reduction)**: Applying definitions to an expression until no further simplification is possible.

> **Redex (reducible expression)**: A sub-expression that can be reduced by applying a definition.

> **Innermost reduction**: Always choose the innermost redex of a nested expression.

> **Outermost reduction**: Work from the outermost redex inwards.

![Innermost versus outermost redex](../../../diagrams/CSC3003S-Advanced%20Programming/FP/02_Lazy_Evaluation/redex-order.svg)

*In `f(g(h(x)))`, innermost reduction starts with `h(x)`. Outermost reduction starts by applying `f`.*

### Redex Features: Termination, Equivalence, Cost

These properties assume pure functions.

| Property | Statement |
|---|---|
| **Termination** | Outermost reduction has the best termination behaviour. Strictly: if *any* reduction sequence terminates, outermost reduction also terminates. |
| **Equivalence** | If both orders terminate, they give the same result (a variant of the **Church–Rosser theorem**). |
| **Cost** | Outermost may need more reduction steps, but it can also skip evaluations that are never needed. |

### Redex Examples

Each example uses these definitions:

```haskell
square n = n * n
ignore x = "boondoggle"
loop     = tail loop
```

**Same result, more steps.** Outermost duplicates the unevaluated argument:

| Innermost | Outermost |
|---|---|
| `square (3+4)` | `square (3+4)` |
| `= square 7` | `= (3+4) * (3+4)` |
| `= 7 * 7` | `= 7 * (3+4)` |
| `= 49` | `= 7 * 7` |
| | `= 49` |

**Same result, fewer steps.** `ignore` does not depend on its argument, so outermost never evaluates `square 5`:

| Innermost | Outermost |
|---|---|
| `ignore (square 5)` | `ignore (square 5)` |
| `= ignore 25` | `= "boondoggle"` |
| `= "boondoggle"` | |

**Termination.** `fst` returns the first element of a pair. Innermost keeps expanding `loop` forever:

| Innermost | Outermost |
|---|---|
| `fst (1, loop)` | `fst (1, loop)` |
| `= fst (1, tail loop)` | `= 1` |
| `= fst (1, tail (tail loop))` | |
| `= …` (never terminates) | (terminates in 1 step) |

### Sharing With Thunks

#### Definitions

> **Sharing**: Avoiding repeated evaluation of the same expression by letting all copies refer to one shared representation.

> **Thunk**: A heap data structure representing a not-yet-evaluated expression. When evaluation is forced, it is replaced by its value.

> **Memoisation**: Storing a computed result so later requests reuse it instead of recomputing.

Sharing fixes the extra steps outermost reduction takes in the `square (3+4)` example.

1. Each unique expression gets a matching thunk on the heap.
2. Duplicates of the expression hold pointers to that thunk instead of copies.
3. When evaluation is forced, the thunk is overwritten with its value.
4. Every other pointer then sees the value without re-evaluating it.

![Sharing a thunk](../../../diagrams/CSC3003S-Advanced%20Programming/FP/02_Lazy_Evaluation/sharing-thunk.svg)

*Both operands of `*` point to one thunk for `3+4`. It is evaluated once to `7`, giving `49` without the duplicated work.*

Sharing is an example of memoisation.

### Infinite Lists

Haskell supports potentially infinite lists. They are evaluated only as far as the context requires.

```haskell
ones :: [Int]   -- ones produces a list of integers
ones = 1 : ones -- recursively defined
```

```haskell
ones = 1 : ones
     = 1 : 1 : ones
     = 1 : 1 : 1 : ones
     = ...
```

Taking a finite prefix, such as `take 3 ones`, forces only three cells.

### Lazy Versus Strict Evaluation

#### Definitions

> **Strict (eager) evaluation**: Arguments are evaluated before a function is called. Imperative languages generally use this.

$$
\text{Lazy evaluation} = \text{outermost reduction} + \text{sharing}
$$

| | Lazy | Strict |
|---|---|---|
| Reduction order | Outermost + sharing | Innermost |
| Steps | Never more than innermost; possibly fewer | Evaluates every argument, even unused ones |
| Termination | Terminates whenever any order does | May loop on unused non-terminating arguments |
| Memory | Can use significantly more (thunks) | No thunk overhead |
| Typical languages | Haskell | Most imperative languages |
