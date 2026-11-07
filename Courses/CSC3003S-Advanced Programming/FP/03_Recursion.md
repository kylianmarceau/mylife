---
tags:
  - advanced-programming
---

# Recursion

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-3-Recursion - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-3-Recursion%20-%20Copy.pdf), James Gain, University of Cape Town, pages 1–11
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Why pure Haskell has no loops, recursion as the replacement, higher-order list functions, and cutting stack use with tail recursion and strict evaluation.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#No Loops In Pure Haskell|No Loops In Pure Haskell]]
  - [[#Recursion Instead Of Loops|Recursion Instead Of Loops]]
  - [[#Higher-Order List Functions|Higher-Order List Functions]]
  - [[#Memory Issues With Recursion|Memory Issues With Recursion]]
  - [[#Example: Factorial With Straight Recursion|Example: Factorial With Straight Recursion]]
  - [[#Tail Recursion|Tail Recursion]]
  - [[#Recursion Summary|Recursion Summary]]

---

## Core Content

### No Loops In Pure Haskell

A loop needs a counter variable that changes on each iteration, which breaks immutability.

Example: build the list $[n, n-1, \dots, 1]$ in Python.

```python
countdown = []
for i in range(n, 0, -1):     # mutating loop counter
    countdown.append(i)

# Pythonic alternative
countdown = [i for i in range(n, 0, -1)]
```

Both the loop counter `i` and the list `countdown` are mutated.

### Recursion Instead Of Loops

#### Definitions

> **Base case**: The case that stops the recursion — the equivalent of a loop's exit condition.

> **Recursive step**: The case that calls the function on a smaller input — the equivalent of the loop body.

```haskell
buildList :: Int -> [Int]
buildList 0 = []                     -- base case: exit at 0
buildList n = n : buildList (n - 1)  -- recursive step: add n to the front
```

This doesn't break immutability: lists are built from pointers, so `n : rest` creates a new cell pointing at the existing list instead of changing anything.

For illustration only — Haskell has syntax to do this directly:

```haskell
countdown :: [Int]
countdown = [5, 4 .. 1]
```

### Higher-Order List Functions

#### Definitions

> **Higher-order function**: A function that takes a function as an argument or returns one.

Haskell provides higher-order functions that operate on lists, so you rarely need to write recursive loops over list elements yourself. They made all the imperative languages jealous.

| Function | Meaning | Example | Output |
|---|---|---|---|
| `map fn lst` | Apply `fn` to every element of `lst` | `map square [1,2,3]` | `[1,4,9]` |
| `filter prd lst` | Keep the elements of `lst` that satisfy predicate `prd` | `filter even [1,2,3]` | `[2]` |
| `foldr cmb base lst` | Combine the elements of `lst` from the right with `cmb`, starting from `base` | `foldr (+) 0 [1,2,3]` | `6` |

`even` is built into the Haskell Prelude. `foldr (+) 0 [1,2,3]` computes $1 + (2 + (3 + 0))$.

### Memory Issues With Recursion

- Each function call creates a **stack frame**.
- With enough calls, recursion causes a **stack overflow**.
- Recursion is often forbidden in safety-critical systems for reliability reasons. Lockheed Martin and NASA coding standards say: "Functions shall not call themselves either directly or indirectly."

### Example: Factorial With Straight Recursion

```haskell
fac 0 = 1
fac n = n * fac (n-1)
```

```text
fac 5 = 5 * (fac 4)
      = 5 * (4 * (fac 3))
      = 5 * (4 * (3 * (fac 2)))
      = 5 * (4 * (3 * (2 * (fac 1))))
      = 5 * (4 * (3 * (2 * (1 * fac 0))))
      = 5 * (4 * (3 * (2 * (1 * 1))))
      = 5 * (4 * (3 * (2 * 1)))
      = 5 * (4 * (3 * 2))
      = 5 * (4 * 6)
      = 5 * 24
      = 120
```

How lazy evaluation handles it:

1. During recursion, the expression is built up lazily.
2. During reduction, Haskell tries outermost order.
3. But `*` is **strict** — it needs both operands as values — so evaluation collapses to innermost order.

| Approach | Stack space |
|---|---|
| Standard recursion | $O(n)$ |
| Iteration | $O(1)$ |

### Tail Recursion

#### Definitions

> **Tail recursion**: Recursion where the recursive call is the very last action; everything else is calculated before the call.

> **Accumulator**: An extra parameter that carries the partial result through the recursive calls.

Because nothing remains to be done after the recursive call, no state needs saving in the current frame, and the compiler can optimise away the stack frames. The stack space drops to $O(1)$.

```haskell
facAux 0 r = r
facAux n r = facAux (n-1) (r * n)
fac n = facAux n 1
```

```text
fac 5 = facAux 5 1
      = facAux (5-1) (5*1)
      = facAux 4 5
      = facAux 3 20
      = facAux 2 60
      = facAux 1 120
      = facAux 0 120
      = 120
```

Tail recursion **requires strict evaluation** of the accumulator:

- Under pure lazy evaluation, `r * n` would not be computed; it would pile up as a chain of heap thunks `(((1*5)*4)*3)…`.
- That just replaces stack frames with heap thunks, risking **heap overflow** instead.
- The counter `n` is always evaluated because of the pattern-match check against 0; the accumulator needs forcing explicitly (e.g. a strictness annotation).

![Factorial stack frames](../../../diagrams/CSC3003S-Advanced%20Programming/FP/03_Recursion/factorial-stack.svg)

*Straight recursion stacks a frame per call (`fac 5` … `fac 0`); tail recursion reuses one frame as the accumulator carries the result.*

| | Straight recursion | Tail recursion (strict) |
|---|---|---|
| Work after the recursive call | Multiply by `n` | None |
| Stack space | $O(n)$ | $O(1)$ |
| Shape of evaluation | Expression grows then shrinks | Constant-size calls |

### Recursion Summary

- Haskell uses recursion instead of explicit iteration.
- Stack frame cost can be cut from $O(n)$ to $O(1)$ using tail recursion plus strict evaluation.
- This requires compiler support and programmer directives.
- It is not applicable in all cases: some branching recursion (e.g. the doubly recursive Fibonacci) cannot be refactored into tail recursion.
