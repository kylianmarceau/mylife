---
tags:
  - advanced-programming
---

# Haskell 5 — Recursion And Lazy Evaluation

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP 9 - Haskell 5 - Recursion and lazy evaluation-1.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%209%20-%20Haskell%205%20-%20Recursion%20and%20lazy%20evaluation-1.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–35  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: recursion as loops, recursive structure, thunks, `foldl` versus `foldl'`, `seq`, and making Fibonacci efficient.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Recap Quiz|Recap Quiz]]
  - [[#Recursion Replaces Loops|Recursion Replaces Loops]]
  - [[#Recursion As While Loops|Recursion As While Loops]]
  - [[#Recursion As For Loops|Recursion As For Loops]]
  - [[#Structure Of A Recursive Function|Structure Of A Recursive Function]]
  - [[#Naturally Recursive Functions: Fibonacci And Quicksort|Naturally Recursive Functions: Fibonacci And Quicksort]]
  - [[#Recursive Expansion|Recursive Expansion]]
  - [[#The foldl Trap: Thunks And Stack Overflow|The foldl Trap: Thunks And Stack Overflow]]
  - [[#foldl' And seq|foldl' And seq]]
  - [[#Think Of The Thunks|Think Of The Thunks]]
  - [[#Memoising Fibonacci: Lazy Dynamic Programming|Memoising Fibonacci: Lazy Dynamic Programming]]
  - [[#Tail-Recursive And Fold-Based Fibonacci|Tail-Recursive And Fold-Based Fibonacci]]
  - [[#Recursion Or Combinator?|Recursion Or Combinator?]]
  - [[#Guarded Recursion|Guarded Recursion]]

---

## Core Content

### Recap Quiz

| Question | Answer |
|---|---|
| What is the `:kind` of `Int`? | `*` |
| A typeclass is… | Encapsulation of supported behaviour only, for a type |
| What is a base case? | The condition for the simplest input, which stops the recursion |
| Difference between `foldl` and `foldr`? | `foldl` is left-associative |
| Which statement is most correct? | Recursion can implement any kind of loop |

### Recursion Replaces Loops

#### Definitions

> **Unbounded search operator (μ)**: The theoretical operation behind a `while` loop: keep searching until a condition holds.

| Imperative construct | Haskell equivalent |
|---|---|
| `for` loop | `foldl` / `foldr` / `foldl'` |
| `while` loop | Recursion |

Haskell has no `while` loops, but recursion can compute exactly the same things. Any `for` loop can become a fold, and any `while` loop can become a recursive function.

### Recursion As While Loops

Think of a recursive function as a `while` loop whose state is passed forward in its arguments.

```python
def next_prime(start):
    x = start + 1
    while not isPrime(x):
        x += 1
    return x
```

```haskell
nextPrime :: Int -> Int
nextPrime start = searchPrime $ start + 1
  where
    searchPrime start
      | isPrime start = start
      | otherwise     = searchPrime (start + 1)
```

The helper `searchPrime` exists because the loop's starting state (`start + 1`) differs from the function's input. It plays the role of the loop body, with the loop variable as its parameter.

Keeping more state means adding more parameters. `kth_next_prime(2, 4)` skips 3, 5 and 7 and returns 11; `kth_next_prime(4, 4)` returns 13. The start itself is not counted.

```python
def kth_next_prime(start, k):
    x = start
    while k > 0:
        x += 1
        if isPrime(x):
            k -= 1
    return x
```

```haskell
kthNextPrime :: Int -> Int -> Int
kthNextPrime start k = searchPrime (start + 1) (k - 1)
  where
    searchPrime start k
      | isPrime start && k == 0 = start
      | isPrime start           = searchPrime (start + 1) (k - 1)
      | otherwise               = searchPrime (start + 1) k
```

### Recursion As For Loops

Recursion also expresses `for` loops, and therefore list combinators and comprehensions:

```haskell
sum' :: Num a => [a] -> a
sum' []     = 0
sum' (x:xs) = x + sum' xs

map' :: (a -> b) -> [a] -> [b]
map' _ []     = []
map' f (x:xs) = f x : map' f xs
```

### Structure Of A Recursive Function

#### Definitions

> **Recurrence relation**: The part of the function that calls itself.

> **Base case**: The part that defines the output for the simplest input and stops the recursion. Omitting it is fine only if you want an infinite loop.

```haskell
fib n = fib (n - 1) + fib (n - 2)   -- recurrence relation
fib 0 = 0                           -- base cases
fib 1 = 1
```

### Naturally Recursive Functions: Fibonacci And Quicksort

$$
\mathrm{fib}(0)=0,\qquad \mathrm{fib}(1)=1,\qquad \mathrm{fib}(n)=\mathrm{fib}(n-1)+\mathrm{fib}(n-2)
$$

```haskell
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

fib 10   -- 55
```

**Quicksort**:

1. `[]` is already sorted.
2. For a non-empty list, pick a pivot (here the first element, for simplicity) and partition the rest.
3. Recursively sort elements $\le$ the pivot and elements $>$ the pivot.
4. Return sorted-smaller ++ `[pivot]` ++ sorted-larger.

```haskell
qsort :: Ord a => [a] -> [a]
qsort []     = []
qsort (x:xs) = qsort tail ++ [pivot] ++ qsort head
  where
    pivot = x
    tail = [i | i <- xs, i <= pivot]
    head = [i | i <- xs, i >  pivot]

qsort [2, 5, -10, 2]   -- [-10, 2, 2, 5]
```

The `Ord a` constraint is needed because elements are compared. The local names `tail` and `head` shadow the Prelude functions.

### Recursive Expansion

Substituting definitions shows how `fib 3` evaluates:

```haskell
fib 3 = ( fib (3 - 1)             +  fib (3 - 2) )
      = ( fib (3 - 1)             +  fib 1       )
      = ( fib 2                   +  1           )
      = ( (fib (2-1) + fib (2-2)) +  1           )
      = ( (fib 1 + fib 0)         +  1           )
      = ( (1 + 0)                 +  1           )
      = 1 + 1 = 2
```

`fib 1` is evaluated twice. The duplication gets exponentially worse as $n$ grows.

> [!warning] <span style="color:#ffc778">Source slip</span>
> Two later slides repeat this trace with swapped base cases (`fib 0 = 1`, `fib 1 = 0`) and a final value of `3`. With the standard definition above, `fib 3 = 2`.

![Naive Fibonacci call tree](../../../diagrams/CSC3003S-Advanced%20Programming/FP/09_Recursion_And_Lazy_Evaluation/fib-call-tree.svg)

*In `fib 4`, `fib 2` is computed twice and `fib 1` three times. Memoisation removes this repeated work.*

### The foldl Trap: Thunks And Stack Overflow

#### Definitions

> **Thunk**: An unevaluated expression held in memory until its value is needed.

```haskell
ns = [1..300_000_000]
foldl (+) 0 ns
-- allocates ~14.3 GiB and may end with *** Exception: stack overflow
```

`foldl (+) 0 ns` computes $((((0+1)+2)+3)+4)+\cdots$. Haskell evaluates lazily and outermost-first, so nothing reduces until the very end:

$$
((\cdots + 299999998) + 299999999) + 300000000
$$

That is a stack of almost 300 million thunks; memory runs out before anything is reduced. The lecture's "lazy kitchen with only one bench" analogy describes the same thing: work piles up instead of being finished as you go.

`foldr (+) 0 ns` computes $1+(2+(3+(4+\cdots)))$. It doesn't help: resolving $1+(\ldots)$ first needs $2+(\ldots)$, and so on. Swapping to `foldr` is also only valid for associative operators, not `-`.

### foldl' And seq

#### Definitions

> **`seq :: a -> b -> b`**: A built-in (not user-implementable) function that strictly evaluates its first argument, then returns its second. It is usually used with `b` defined in terms of `a`, e.g. `seq arg (function arg)`.

> **`foldl'`**: A version of `foldl` that is strict in applying the operator. It forces the accumulator at each step, so it collapses as it goes.

```haskell
-- Lazy
foldl  f acc []     = acc
foldl  f acc (x:xs) = let acc' = f acc x
                      in foldl f acc' xs

-- Strict in the operator f
foldl' f acc []     = acc
foldl' f acc (x:xs) = let acc' = f acc x
                      in seq acc' $ foldl' f acc' xs
```

![foldl versus foldl'](../../../diagrams/CSC3003S-Advanced%20Programming/FP/09_Recursion_And_Lazy_Evaluation/foldl-thunks.svg)

*`foldl` grows a nested thunk proportional to the list. `foldl'` forces the accumulator each step, so it stays a single number.*

With `foldl'`, the 300-million-element sum completes.

### Think Of The Thunks

The most important rule for recursion in Haskell is **think of the thunks**.

- Because Haskell is lazy, a notional "call stack" growing large is not really the problem; Haskell doesn't have a conventional call stack.
- What matters is keeping the number of **unevaluated thunks** down by judiciously forcing strict evaluation, as `foldl'` does.
- Technically Haskell is specified as **non-strict**, which is slightly different from lazy.

### Memoising Fibonacci: Lazy Dynamic Programming

#### Definitions

> **Memoisation**: Caching previously computed values of a function, as in dynamic programming.

> **`go`**: A conventional name for a recursing helper subfunction (like `i` in a `for` loop).

Following Tikhon Jelvis's "Lazy Dynamic Programming": define an array of computed values, as in DP, but build it **recursively from the array itself** rather than iteratively.

```haskell
import Data.Array

fib' n = go n
  where go 0 = 0
        go 1 = 1
        go n = fibs ! (n - 1) + fibs ! (n - 2)
        fibs = listArray (0, n) [go x | x <- [0..n]]
```

- `Array` gives $O(1)$ access, like Java's `ArrayList`; `!` is the index operator.
- `listArray` builds the array lazily from a range of indices. Each element is a thunk `go x`, evaluated at most once and then shared.

This is much faster, but it keeps all previous values, so it uses $O(n)$ space. Only the last two values are needed, so Fibonacci can run in $O(1)$ space. Laziness does not exempt you from ordinary algorithmic optimisation.

### Tail-Recursive And Fold-Based Fibonacci

#### Definitions

> **Tail recursion**: A function that always returns either a simple value or a call to itself (a **tail call**). In many languages this allows $O(1)$ stack space.

In Haskell, tail-call elimination matters less because of how thunks implement laziness, but it helps here:

```haskell
fib :: Int -> Integer
fib n = go 0 1 0
  where
    go n_2 n_1 cur_n
      | n == cur_n = n_2
      | otherwise  = go n_1 (n_2 + n_1) (cur_n + 1)
```

- Only the last two results are kept and passed to the next `go` call.
- The source returns `n_1` in the base case, which gives $\mathrm{fib}(n+1)$; returning `n_2` gives $\mathrm{fib}(n)$.
- `+` is strict in both arguments. The source credits this with forcing evaluation and avoiding a large stack of thunks, but `n_2 + n_1` itself stays an unevaluated thunk until something demands it. In practice, GHC's strictness analysis (with optimisation) or `seq`/bang patterns guarantee the accumulators are forced.

As a fold, writing `n_1` for $\mathrm{fib}(n-1)$ and `n_2` for $\mathrm{fib}(n-2)$:

```haskell
fib :: Int -> Integer
fib n = fst (foldl' go (0, 1) [1..n])
  where
    go (n_1, n_2) _ = (n_1 + n_2, n_1)
```

| Step | Tuple | `fst` |
|---|---|---|
| start | $(0,1)$ | $\mathrm{fib}(0)=0$ |
| 1 | $(1,0)$ | $1$ |
| 2 | $(1,1)$ | $1$ |
| 3 | $(2,1)$ | $2$ |
| 4 | $(3,2)$ | $3$ |

`Integer` avoids overflow for large inputs such as `fib 1_000_000`.

### Recursion Or Combinator?

Many things can be written either way:

| Recursion | Combinator |
|---|---|
| Recursive `fib` | `foldl'` |
| `transform (x:xs) = (x * 2) : transform xs` | `map (*2) xs` |

- It is ultimately a matter of taste.
- Combinators each do one specific thing, so intent is often clearer; the `map` version is much clearer.
- "The more Haskell you know, the less recursion you write": you learn the specific tool for each job.
- Code is read more often than it is written, so prefer clarity.

### Guarded Recursion

#### Definitions

> **Guarded recursion**: Placing the recursive call inside a data constructor where possible, so laziness evaluates the rest only on demand.

```haskell
map f (x:xs) = (f x) : (map f xs)
```

The recursive call sits inside `:`. The rest of the list (`map f xs`) is evaluated only if it is demanded, which also lets this `map` work on infinite lists.

The exercise implements `foldr` recursively:

```haskell
myfoldr :: (a -> b -> b) -> b -> [a] -> b
myfoldr _ z []     = z
myfoldr f z (x:xs) = f x (myfoldr f z xs)
```
