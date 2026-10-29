---
tags:
  - advanced-programming
---

# Recursion

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-3-Recursion - Copy.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-3-Recursion%20-%20Copy.pdf), James Gain, University of Cape Town, PDF pages 1–11  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes on replacing loops with recursion, higher-order list functions, and tail recursion.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#No Loops In Pure Haskell|No Loops In Pure Haskell]]
  - [[#Recursion Instead Of Loops|Recursion Instead Of Loops]]
  - [[#Higher-Order Functions: map, filter, foldr|Higher-Order Functions: map, filter, foldr]]
  - [[#Memory Issues|Memory Issues]]
  - [[#Example: Factorial And Lazy Evaluation|Example: Factorial And Lazy Evaluation]]
  - [[#Tail Recursion|Tail Recursion]]
  - [[#Limits Of Tail Recursion|Limits Of Tail Recursion]]

---

## Core Content

### No Loops In Pure Haskell

A loop needs a **counter variable** that changes on each iteration. That mutation breaks immutability, so pure Haskell has no loops.

To build $[n, n-1, \ldots, 1]$ in Python:

```python
countdown = []
for i in range(n, 0, -1):    # mutating loop counter
    countdown.append(i)

# Pythonic alternative
countdown = [i for i in range(n, 0, -1)]
```

### Recursion Instead Of Loops

#### Definitions

> **Base case**: The non-recursive case of a recursive definition. It plays the role of the loop exit.

> **Recursive step**: The case that calls the function again on a smaller input. It plays the role of the loop body.

```haskell
buildList :: Int -> [Int]
buildList 0 = []                     -- base case: exit at 0
buildList n = n : buildList (n - 1)  -- recursive step: add n to the front
```

- `:` (cons) adds an element to the front of a list.
- This does not break immutability because lists are built from pointers: each new cell points at the existing, unchanged tail.
- Haskell also has range syntax that does this automatically: `countdown = [5, 4 .. 1]`.

### Higher-Order Functions: map, filter, foldr

#### Definitions

> **Higher-order function**: A function that takes another function as an argument or returns one.

> **`map fn lst`**: Applies function `fn` to every element of list `lst`.

> **`filter prd lst`**: Returns the elements of `lst` that satisfy the predicate function `prd`.

> **`foldr cmb base lst`**: Combines the elements of `lst`, starting from the right, using combining function `cmb` and starting value `base`.

These Prelude functions remove the need to write recursive loops over list elements by hand.

| Function | Example | Output |
|---|---|---|
| `map` | `map square [1,2,3]` | `[1,4,9]` |
| `filter` | `filter even [1,2,3]` (`even` is in the Prelude) | `[2]` |
| `foldr` | `foldr (+) 0 [1,2,3]` | `6` |

`foldr (+) 0 [1,2,3]` works from the right end:

$$
1 + (2 + (3 + 0)) = 6
$$

These higher-order functions "made all the imperative programming languages jealous", which is why many of them later adopted similar functions.

### Memory Issues

- Each function call creates a **stack frame**.
- With enough nested calls, recursion can cause a **stack overflow**.
- Recursion is often forbidden in safety-critical systems for reliability reasons. Lockheed Martin and NASA coding rules state: "Functions shall not call themselves either directly or indirectly."

### Example: Factorial And Lazy Evaluation

```haskell
fac 0 = 1
fac n = n * fac (n-1)
```

```haskell
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

| Approach | Stack space |
|---|---|
| Standard recursion | $O(n)$ |
| Iteration | $O(1)$ |

Under lazy evaluation:

1. During recursion, the expression is built lazily.
2. During reduction, Haskell tries outermost order.
3. But `*` is **strict**: it needs both operands to be values.
4. So evaluation collapses to innermost order, and every pending multiplication stays on the stack.

### Tail Recursion

#### Definitions

> **Tail recursion**: Recursion in which everything is calculated first and the recursive call is the very last action, so no state needs to be saved in the calling frame.

> **Accumulator**: An extra parameter that carries the partial result forward into the next call.

```haskell
facAux 0 r = r
facAux n r = facAux (n-1) (r * n)
fac n = facAux n 1
```

```haskell
fac 5 = facAux 5 1
      = facAux (5-1) (5*1)
      = facAux 4 5
      = facAux 3 20
      = facAux 2 60
      = facAux 1 120
      = facAux 0 120
      = 120
```

- The compiler can optimise away stack frames, using $O(1)$ stack space.
- `n` is always evaluated because of the pattern match against `0`.
- It **requires strict evaluation** of the accumulator. Otherwise `r * n` builds a chain of heap thunks: stack frames are just replaced by thunks, with a risk of **heap overflow**.

![Factorial stack frames](../../../diagrams/CSC3003S-Advanced%20Programming/FP/03_Recursion/factorial-stack.svg)

*Straight recursion keeps six `fac` frames alive until the multiplications unwind. Strict tail recursion reuses one frame for each `facAux` call.*

### Limits Of Tail Recursion

- Haskell uses recursion instead of explicit iteration.
- Tail recursion plus strict evaluation cuts stack cost from $O(n)$ to $O(1)$.
- It needs compiler support and programmer directives (to force strictness).
- It does not apply in every case: some **branching recursion** (several recursive calls per step) cannot be refactored into tail form.
