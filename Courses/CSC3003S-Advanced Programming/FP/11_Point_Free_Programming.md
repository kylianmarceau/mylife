---
tags:
  - advanced-programming
---

# Haskell 7 — Point-Free Programming

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP 11 (Haskell 7)_ Point-free programming.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%2011%20%28Haskell%207%29_%20Point-free%20programming.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–14  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: equivalent definition styles, composition, eliminating arguments, and the trade-offs of point-free code.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Many Styles, One Output|Many Styles, One Output]]
  - [[#Function Composition Recap|Function Composition Recap]]
  - [[#Rewriting isPrime As A Composition|Rewriting isPrime As A Composition]]
  - [[#Deriving A Point-Free kthNextPrime|Deriving A Point-Free kthNextPrime]]
  - [[#What Point-Free Means|What Point-Free Means]]
  - [[#Advantages And Disadvantages|Advantages And Disadvantages]]

---

## Core Content

### Many Styles, One Output

Haskell often offers many ways to write the same function:

```haskell
add' :: Num a => a -> a -> a
add' a b = a + b              -- standard (signature may be elided)

add' a = \b -> a + b          -- function returning a lambda

add' a b = res                -- where clause
    where
  res = a + b

add' a b = let res = a + b    -- let-in: an expression, usable anywhere
           in res

add' a b = (+) a b            -- Polish (prefix) notation

add' = (+)                    -- no arguments named
```

The slide writes `add' a + b = a + b`, which is a typo for `add' a b = a + b`.

Expressions also have several forms: `add' 1 (2 - 3)` is the same as `add' 1 $ 2 - 3`, where `$` removes the brackets. Which style is best depends on taste and context.

### Function Composition Recap

#### Definitions

> **Function composition (`.`)**: `(f . g) x = f (g x)`. It builds functions from other functions, so you think about the functions rather than the values flowing through them.

See [Practical Prep: Tree Traversal](10_Prac_Prep_Tree_Traversal.md) for the full introduction.

### Rewriting isPrime As A Composition

```haskell
isPrime n = all (\f -> (n `mod` f) /= 0) [2..(n - 1)]
-- the lambda becomes a composition:
isPrime n = all ((/= 0) . mod n) [2..(n - 1)]
```

`mod n` is a partial application, `\f -> mod n f`. Composing it with the section `(/= 0)` gives `\f -> (mod n f) /= 0`.

### Deriving A Point-Free kthNextPrime

Start from the recursive version:

```haskell
kthNextPrime :: Int -> Int -> Int
kthNextPrime start k = searchPrime (start + 1) (k - 1)
  where
    searchPrime start k
      | isPrime start && k == 0 = start
      | isPrime start           = searchPrime (start + 1) (k - 1)
      | otherwise               = searchPrime (start + 1) k
```

Instead, generate and manipulate a sequence of primes:

1. Generate an infinite sequence of primes from `start`. Laziness means only what is needed gets evaluated: `filter isPrime [start..]`.
2. Index it with `!!`: `kthNextPrime start k = filter isPrime [start..] !! k`.
3. Drop `k` using an operator section: `kthNextPrime start = (filter isPrime [start..] !!)`.
4. Rewrite `!!` in prefix form: `kthNextPrime start = (!!) (filter isPrime [start..])`.
5. Replace the generator literal with `enumFrom`: `kthNextPrime start = (!!) (filter isPrime (enumFrom start))`.
6. This is now $f(g(h(x)))$, so compose and drop `start`: `kthNextPrime = (!!) . filter isPrime . enumFrom`.

![Point-free kthNextPrime pipeline](../../../diagrams/CSC3003S-Advanced%20Programming/FP/11_Point_Free_Programming/kthnextprime-pipeline.svg)

*`enumFrom` produces `[start..]`, `filter isPrime` keeps the primes, and `(!!)` waits for `k`. Laziness computes only the primes that are needed.*

Note on step 2: `filter isPrime [start..]` includes `start` itself if it is prime, and `!!` is zero-based. So this version is not exactly the same as the recursive one, which looks strictly after `start` and counts from 1.

### What Point-Free Means

#### Definitions

> **Point-free programming**: Writing functions that do **not name their arguments**, the "points" this style is free from.

> **Pointful**: The ordinary style, where arguments are named.

"Point-free" does not mean there are no dots (`.`), nor that the program is pointless.

| Pointful | Point-free |
|---|---|
| `kthNextPrime start k = filter isPrime [start..] !! k` | `kthNextPrime = (!!) . filter isPrime . enumFrom` |

### Advantages And Disadvantages

| Advantage | Disadvantage |
|---|---|
| **Clearer when variables only pass data along.** `foldl' (+) 0 xs` ("fold `xs` with `+`") expresses intent better than `foldl' (\acc x -> acc + x) 0 xs`. | **Sometimes less clear.** The lecturer prefers the pointful `kthNextPrime`. It depends on context and taste. |
| **Higher, declarative thinking** about what the program *is*, e.g. `vectorMagnitude = sqrt . sum . map (^2)`. | **Hard to follow when an argument is used in several places.** Compare `isPrime n = all ((/= 0) . mod n) [2..(n - 1)]` with `isPrime = ap (all . ((0 /=) .) . mod) (enumFromTo 2 . subtract 1)`. |
| **Considered the purest FP**: functions all the way down. | **Types are hard to track** with no variable bindings as clues. |

The type puzzle:

```haskell
example = (. (7.0 +)) . (/) . fromIntegral . (10 +)
-- example :: Int -> Float -> Float
```

Working it out: `example n` gives `(/) (fromIntegral (10 + n)) . (7.0 +)`. That is a function of `x` returning $\dfrac{10+n}{7.0+x}$.

The lecture exercises in point-free style:

```haskell
sum' :: Num a => [a] -> a
sum' = foldl' (+) 0

isEven :: Int -> Bool
isEven = (== 0) . (`mod` 2)
```
