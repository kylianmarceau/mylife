---
tags:
  - advanced-programming
---

# Point-Free Programming

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP 11 (Haskell 7)_ Point-free programming.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%2011%20%28Haskell%207%29_%20Point-free%20programming.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–14
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Many equivalent ways to write one function, rewriting functions as compositions, the point-free style, and its advantages and disadvantages.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Many Styles, One Output|Many Styles, One Output]]
  - [[#Thinking In Function Composition|Thinking In Function Composition]]
  - [[#Rewriting isPrime As A Composition|Rewriting isPrime As A Composition]]
  - [[#Deriving A Point-Free kthNextPrime|Deriving A Point-Free kthNextPrime]]
  - [[#What Point-Free Programming Is|What Point-Free Programming Is]]
  - [[#Advantages And Disadvantages|Advantages And Disadvantages]]

---

## Core Content

### Many Styles, One Output

Haskell often has several ways of writing the same thing. All of these define the same `add'`:

```haskell
add' :: Num a => a -> a -> a
add' a b = a + b

-- Same, with the type signature left to inference
add' a b = a + b

-- As a function returning a lambda
add' a = \b -> a + b

-- Using a where clause
add' a b = res
  where
    res = a + b

-- Using let-in (an expression, so it can be used anywhere)
add' a b = let res = a + b
           in res

-- In Polish (prefix) notation
add' a b = (+) a b

-- With no arguments named at all
add' = (+)
```

Likewise, `add' 1 (2 - 3)` can be written `add' 1 $ 2 - 3`, using `$` to remove the grouping brackets.

Which to use is often a matter of taste and context — some ways are more natural for a given function.

### Thinking In Function Composition

Functions are often pictured (especially in maths) as little machines that transform input values into output values. Haskell encourages you to think about the **functions themselves** instead of the values flowing through them, using function composition:

$$
(f . g)\,x = f\,(g\,x)
$$

See [Practical Preparation: Tree Traversal](10_Prac_Prep_Tree_Traversal.md#Function%20Composition) for the `.` operator.

### Rewriting isPrime As A Composition

A sensible definition of `isPrime` uses a lambda that tests each potential factor `f`:

```haskell
isPrime n = all (\f -> (n `mod` f) /= 0) [2..(n - 1)]
```

The lambda "take `f`, compute `mod n f`, check it is not 0" is a composition of two functions:

```haskell
isPrime n = all ((/= 0) . mod n) [2..(n - 1)]
```

| Piece | Type | Meaning |
|---|---|---|
| `mod n` | `Int -> Int` | Partially applied: `\f -> mod n f` |
| `(/= 0)` | `Int -> Bool` | Operator section: `\r -> r /= 0` |
| `(/= 0) . mod n` | `Int -> Bool` | "is not a factor of `n`" |

### Deriving A Point-Free kthNextPrime

The recursive version from [Recursion And Lazy Evaluation](09_Recursion_And_Lazy_Evaluation.md):

```haskell
kthNextPrime :: Int -> Int -> Int
kthNextPrime start k = searchPrime (start + 1) (k - 1)
  where
    searchPrime start k
      | isPrime start && k == 0 = start
      | isPrime start           = searchPrime (start + 1) (k - 1)
      | otherwise               = searchPrime (start + 1) k
```

Instead, think of it as generating and manipulating a sequence of primes.

1. **Generate** an infinite list of primes from `start`. Laziness means only as much as needed is evaluated:
```haskell
filter isPrime [start..]
```
2. **Index** it to get the $k$th one:
```haskell
kthNextPrime start k = filter isPrime [start..] !! k
```
3. **Drop `k`** using an operator section:
```haskell
kthNextPrime start = (filter isPrime [start..] !!)
```
4. **Rewrite `!!` in prefix (Polish) notation**:
```haskell
kthNextPrime start = (!!) (filter isPrime [start..])
```
5. **Replace the range literal with `enumFrom`**, since `[start..] = enumFrom start`:
```haskell
kthNextPrime start = (!!) (filter isPrime (enumFrom start))
```
6. **Drop `start`**: the right side is now `(!!)` applied to `filter isPrime` applied to `enumFrom` applied to `start`, which is a composition:
```haskell
kthNextPrime = (!!) . filter isPrime . enumFrom
```

The function no longer mentions its arguments at all.

![Point-free kthNextPrime pipeline](../../../diagrams/CSC3003S-Advanced%20Programming/FP/11_Point_Free_Programming/kthnextprime-pipeline.svg)

*`enumFrom` builds the infinite range, `filter isPrime` keeps primes, and `(!!)` returns the indexing function waiting for `k`.*

### What Point-Free Programming Is

#### Definitions

> **Point-free programming**: Writing functions that do not name their arguments — the "points" the style is free from. It does not mean there are no dots, or that the programming is pointless.

> **Pointful**: The ordinary style, which names arguments.

| Style | Definition |
|---|---|
| Pointful | `kthNextPrime start k = filter isPrime [start..] !! k` |
| Point-free | `kthNextPrime = (!!) . filter isPrime . enumFrom` |

The lecture exercises, in point-free style:

```haskell
sum' :: Num a => [a] -> a
sum' = foldl' (+) 0

isEven :: Int -> Bool
isEven = (== 0) . (`mod` 2)
```

### Advantages And Disadvantages

| Advantages | Disadvantages |
|---|---|
| **1. Clearer when variables only get passed straight on.** `foldl' (+) 0 xs` ("fold `xs` with `+`") states the intent better than `foldl' (\acc x -> acc + x) 0 xs` ("add `acc` and `x` for each element") | **1. Sometimes less clear.** The lecturer prefers the pointful `kthNextPrime`; it depends on context and taste |
| **2. Thinking at a higher, declarative level** — about what the program is, by composing functions, not how data is shuffled: `vectorMagnitude = sqrt . sum . map (^2)` | **2. Hard to follow when an argument is used in several places.** Compare `isPrime n = all ((/= 0) . mod n) [2..(n - 1)]` with `isPrime = ap (all . ((0 /=) .) . mod) (enumFromTo 2 . subtract 1)` |
| **3. Considered the purest expression of FP** — functions all the way down | **3. Types are hard to follow** in long chains, with fewer clues from variable names |

For disadvantage 3, consider:

```haskell
example = (. (7.0 +)) . (/) . fromIntegral . (10 +)
```

What are its argument types? It's `Int -> Float -> Float`: it computes $\dfrac{10 + n}{7.0 + x}$ for an `Int` $n$ and a `Float` $x$, but that is far from obvious.
