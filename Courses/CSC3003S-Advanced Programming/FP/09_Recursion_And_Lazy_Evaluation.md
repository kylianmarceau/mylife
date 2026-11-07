---
tags:
  - advanced-programming
---

# Recursion And Lazy Evaluation In Haskell

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP 9 - Haskell 5 - Recursion and lazy evaluation-1.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%209%20-%20Haskell%205%20-%20Recursion%20and%20lazy%20evaluation-1.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–35
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Recursion as while and for loops, naturally recursive functions (Fibonacci, quicksort), why `foldl` overflows and `foldl'` doesn't, thunks, and three ways to make Fibonacci fast.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Loops, Folds And Recursion|Loops, Folds And Recursion]]
  - [[#Recursion As While Loops|Recursion As While Loops]]
  - [[#Recursion As For Loops|Recursion As For Loops]]
  - [[#Naturally Recursive Functions And Their Structure|Naturally Recursive Functions And Their Structure]]
  - [[#Quicksort|Quicksort]]
  - [[#Recursive Expansion|Recursive Expansion]]
  - [[#Why foldl Overflows|Why foldl Overflows]]
  - [[#foldl' And seq|foldl' And seq]]
  - [[#Think Of The Thunks|Think Of The Thunks]]
  - [[#Memoising Fibonacci: Lazy Dynamic Programming|Memoising Fibonacci: Lazy Dynamic Programming]]
  - [[#Tail Recursion And Constant-Space Fibonacci|Tail Recursion And Constant-Space Fibonacci]]
  - [[#Recursion Or Combinator?|Recursion Or Combinator?]]
  - [[#Guarded Recursion|Guarded Recursion]]

---

## Core Content

### Loops, Folds And Recursion

Recap: `:kind Int` is `*`, and a typeclass encapsulates supported **behaviour** only (no data).

| Imperative construct | Haskell equivalent |
|---|---|
| `for` loop | `foldl` / `foldr` / `foldl'` |
| `while` loop (the "unbounded search operator" $\mu$) | Recursion |

Haskell has no `while` loops, but recursion can compute exactly the same things. Just as any `for` loop can become a fold, any `while` loop can become a recursive function — recursion can implement **any** kind of loop.

### Recursion As While Loops

Recursive functions needn't be complicated. Think of them as `while` loops where the state is passed forward in the arguments.

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

The helper `searchPrime` exists because the loop's state (`x`) starts at `start + 1`, not at `start`. The outer function sets up the initial state, and the helper carries it through the iterations.

**Keeping more state**: find the $k$th prime after `start`.

- `kth_next_prime(2, 4)` passes 3, 5 and 7, returning 11 (2 itself is not counted).
- `kth_next_prime(4, 4)` passes 5, 7 and 11, returning 13.

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

Recursion also neatly expresses `for` loops — and therefore list combinators and comprehensions.

```haskell
sum' :: Num a => [a] -> a
sum' []     = 0
sum' (x:xs) = x + sum' xs

map' :: (a -> b) -> [a] -> [b]
map' _ []     = []
map' f (x:xs) = f x : map' f xs
```

The lecture exercise "implement `foldr` recursively":

```haskell
myfoldr :: (a -> b -> b) -> b -> [a] -> b
myfoldr _ acc []     = acc
myfoldr f acc (x:xs) = f x (myfoldr f acc xs)
```

### Naturally Recursive Functions And Their Structure

#### Definitions

> **Recurrence relation**: The part of a recursive function that calls itself.

> **Base case**: The part that defines the output for the simplest input and stops the recursion. Omit it only if you want an infinite loop.

Some functions are most natural recursively, like Fibonacci:

$$
\text{fib}(0) = 0, \qquad \text{fib}(1) = 1, \qquad \text{fib}(n) = \text{fib}(n-1) + \text{fib}(n-2)
$$

```haskell
fib :: Int -> Int
fib 0 = 0                          -- base case
fib 1 = 1                          -- base case
fib n = fib (n - 1) + fib (n - 2)  -- recurrence relation

fib 10 -- 55
```

### Quicksort

Many sorting algorithms are naturally recursive. Quicksort:

1. `[]` is already sorted.
2. A non-empty list is sorted by picking a pivot (here, simply the first element) and partitioning the rest:
   - elements $\le$ pivot,
   - elements $>$ pivot.
3. Quicksort both parts.
4. Return (sorted smaller part) ++ [pivot] ++ (sorted larger part).

```haskell
qsort :: Ord a => [a] -> [a]
qsort []     = []
qsort (x:xs) = qsort smaller ++ [pivot] ++ qsort larger
  where
    pivot   = x
    smaller = [i | i <- xs, i <= pivot]
    larger  = [i | i <- xs, i >  pivot]

qsort [2, 5, -10, 2]   -- [-10, 2, 2, 5]
```

The `Ord a` constraint is needed because elements are compared. (The source names the parts `tail` and `head`, which shadows the Prelude functions; they are renamed here for clarity.)

The lecture exercise "implement merge sort recursively":

```haskell
msort :: Ord a => [a] -> [a]
msort []  = []
msort [x] = [x]
msort xs  = merge (msort left) (msort right)
  where (left, right) = splitAt (length xs `div` 2) xs

merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
  | x <= y    = x : merge xs (y:ys)
  | otherwise = y : merge (x:xs) ys
```

### Recursive Expansion

Substituting definitions shows how `fib 3` is evaluated:

```text
fib 3 = ( fib (3-1)              +  fib (3-2) )
      = ( fib (3-1)              +  fib 1     )
      = ( fib 2                  +  1         )
      = ( (fib (2-1) + fib (2-2)) + 1         )
      = ( (fib 1 + fib 0)        +  1         )
      = ( (1 + 0)                +  1         )
      = 1 + 1 = 2
```

`fib 1` is evaluated **twice**, and the duplication gets exponentially worse for larger $n$.

![Naive Fibonacci call tree](../../../diagrams/CSC3003S-Advanced%20Programming/FP/09_Recursion_And_Lazy_Evaluation/fib-call-tree.svg)

*The call tree for `fib 4` repeats whole subtrees, which is why naive recursion is exponential.*

### Why foldl Overflows

`foldl` has a trap: stack overflows.

```haskell
ns = [1..300_000_000]
foldl (+) 0 ns
```

This allocates about 14.3 GiB of memory and may end with `*** Exception: stack overflow` — on a mere 300 million items.

#### Definitions

> **Thunk**: An unevaluated expression held in memory until its value is needed.

`foldl (+) 0 ns` computes $((((0 + 1) + 2) + 3) + 4) + \dots$. Because Haskell evaluates lazily and outermost-first, none of the additions happens until the very end. Memory fills with a chain of almost 300 million thunks:

$$
((\dots + 299999998) + 299999999) + 300000000
$$

The expression can't be reduced until memory has already run out. (The lecture's "lazy kitchen with only one bench" analogy: piling up unfinished dishes instead of finishing each as you go.)

`foldr` doesn't help. `foldr (+) 0 ns` computes $1 + (2 + (3 + \dots))$; before resolving $1 + (\dots)$ it must resolve $2 + (\dots)$, and so on. (And `foldr` is only interchangeable with `foldl` for associative operators — not for `-`.)

### foldl' And seq

#### Definitions

> **`seq`**: A built-in ("magic", not user-implementable) function `seq :: a -> b -> b` that strictly evaluates its first argument, then returns its second. It is useful when the second is defined in terms of the first, e.g. `seq arg (function arg)`.

> **`foldl'`**: A left fold that applies the operator strictly at each step.

The fix is to stop Haskell piling up thunks by forcing strict evaluation of the operator, so the accumulator collapses as we go:

```haskell
-- Lazy
foldl f acc []     = acc
foldl f acc (x:xs) = let acc' = f acc x
                     in foldl f acc' xs

-- Strict in the operator f
foldl' f acc []     = acc
foldl' f acc (x:xs) = let acc' = f acc x
                      in seq acc' $ foldl' f acc' xs
```

`foldl' (+) 0 [1..300_000_000]` works.

![foldl versus foldl'](../../../diagrams/CSC3003S-Advanced%20Programming/FP/09_Recursion_And_Lazy_Evaluation/foldl-thunks.svg)

*`foldl` builds a growing chain of thunks; `foldl'` forces each partial sum immediately, keeping one value.*

| Fold | Associativity | Evaluation | Large sums |
|---|---|---|---|
| `foldl` | Left | Lazy — builds thunks | Overflows |
| `foldr` | Right | Lazy — nested pending additions | Overflows |
| `foldl'` | Left | Strict at each step | Constant memory |

### Think Of The Thunks

The most important thing about recursion in Haskell is to **think of the thunks**.

- Because Haskell is lazy, a notional call stack growing large doesn't matter much — Haskell doesn't really have one in the usual sense.
- What matters is keeping the number of **unevaluated thunks** down, by judiciously forcing strict evaluation when necessary, as with `foldl'`.

Technically Haskell is specified as **non-strict**, which is slightly different from lazy. [AR: "Lazy vs. non-strict", Haskell Wiki]

### Memoising Fibonacci: Lazy Dynamic Programming

#### Definitions

> **Memoisation**: Caching previously computed values of a function, conceptually like dynamic programming.

Following Tikhon Jelvis's "Lazy Dynamic Programming": define an array of computed values, as in DP, but build the array **recursively from itself** instead of iteratively.

```haskell
import Data.Array

fib' :: Int -> Integer
fib' n = go n
  where go 0 = 0
        go 1 = 1
        go i = fibs ! (i - 1) + fibs ! (i - 2)
        fibs = listArray (0, n) [go x | x <- [0..n]]
```

| Piece | Role |
|---|---|
| `Data.Array` | Like Java's `ArrayList`: $O(1)$ access; `!` is the index operator |
| `listArray (0, n) [...]` | Builds the array lazily from a range of indices |
| `go` | Conventional name for a recursing helper (like `i` in a `for` loop) |

Each array entry is a thunk that refers to earlier entries. Once forced, it stays computed, so each Fibonacci number is computed once. This is much faster and handles much larger $n$.

It still keeps every previous value, so it uses $O(n)$ space. Only the last two values are needed, so Fibonacci can run in $O(1)$ space. Laziness doesn't make Haskell immune to ordinary algorithmic optimisation.

### Tail Recursion And Constant-Space Fibonacci

#### Definitions

> **Tail recursion**: A function always returns either a simple value or a call to itself (a **tail call**). In many languages this allows $O(1)$ stack space.

In Haskell, tail recursion and tail-call elimination matter less because laziness is implemented with thunks [see "Tail recursion" on the Haskell Wiki], but it helps here.

**Tail-recursive version**:

```haskell
fib :: Int -> Integer
fib n = go 0 1 0
  where
    go n_2 n_1 cur_n
      | n == cur_n = n_2
      | otherwise  = go n_1 (n_2 + n_1) (cur_n + 1)
```

- Only the last two results are kept and passed to the next `go` call, so it uses $O(1)$ space.
- `+` is strict in both arguments, which forces evaluation and avoids a large stack of thunks.
- The source returns `n_1` in the base case, which yields $\text{fib}(n+1)$; returning `n_2` gives $\text{fib}(n)$ with $\text{fib}(0) = 0$.

**Fold version** — fold is the universal list combinator. Fold over $1..n$ carrying the pair $(\text{fib}(i), \text{fib}(i-1))$:

```haskell
import Data.List (foldl')

fib :: Int -> Integer
fib n = fst (foldl' go (0, 1) [1..n])
  where
    go (n_1, n_2) _ = (n_1 + n_2, n_1)
```

| Version | Time | Space |
|---|---|---|
| Naive recursion | Exponential | Large (repeated calls) |
| Lazy DP array | $O(n)$ | $O(n)$ |
| Tail recursion / `foldl'` | $O(n)$ | $O(1)$ — fast enough for `fib 1_000_000` |

### Recursion Or Combinator?

Many things can be written either way:

| Recursive | Combinator |
|---|---|
| `fib` with `go` | `fib` with `foldl'` |
| `transform (x:xs) = (x * 2) : transform xs` | `map (*2) xs` |

It is ultimately a matter of taste.

- Combinators each do one specific thing, so the intent is obvious — the `map` version is much clearer.
- Some say the more Haskell you know, the less recursion you write, because you learn the specific tool for each job.
- Code is read more often than it is written, so keep it clear.

### Guarded Recursion

#### Definitions

> **Guarded recursion**: Placing the recursive call inside a data constructor (such as cons `:`), so the rest of the structure is only computed when demanded.

```haskell
map f (x:xs) = (f x) : (map f xs)
```

Because Haskell is lazy, `map f xs` is only evaluated if and only if the rest of the list is needed. This lets `map` work on infinite lists and avoids building thunk chains. You don't need the theory, just the habit: make recursive calls happen inside a data constructor where possible.

Quiz answers: a base case is the condition for the simplest input, which stops the recursion; `foldl` differs from `foldr` in being left-associative; recursion can implement any kind of loop.

Further reading (only if folds confuse you): "Foldl and foldr" (blog.haskell.org), "Foldr Foldl Foldl'" and "Performance/Strictness" (Haskell Wiki); assigned: LYAH *Recursion*, "Fold" (Haskell Wiki), Jelvis's "Lazy Dynamic Programming", "Fibonacci in Haskell" (Michael Jones).
