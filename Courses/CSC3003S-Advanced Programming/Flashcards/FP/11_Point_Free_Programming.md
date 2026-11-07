---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 11 — Point-Free Programming"
---

# FP 11 — Point-Free Programming

**Source note:** [Point-Free Programming](../../FP/11_Point_Free_Programming.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Point-Free Style|Point-Free Style]]
  - [[#Trade-offs|Trade-offs]]

## Core Content

### Point-Free Style

<!-- qard-id: ap-d3fc5e2f8d1938b8be6e -->
> [!qard]- What is point-free programming?
> Writing functions that don't name their arguments (the "points"), using composition instead.

<!-- qard-id: ap-cb9fe71ab65c367ed0dc -->
> [!qard]- What is "pointful" style?
> The ordinary style that names a function's arguments.

<!-- qard-id: ap-077dbb8f24ed686307fb -->
> [!qard]- Write `add' a b = a + b` with no arguments named.
> `add' = (+)`.

<!-- qard-id: ap-75bf0e01d2be73c9cc94 -->
> [!qard]- Rewrite `\f -> (n mod f) /= 0` as a composition.
> `(/= 0) . mod n`.

<!-- qard-id: ap-9cd84a61212b08ac6e0a -->
> [!qard]- Give the point-free form of `kthNextPrime start k = filter isPrime [start..] !! k`.
> `kthNextPrime = (!!) . filter isPrime . enumFrom`.

<!-- qard-id: ap-64b86d53dec232c43373 -->
> [!qard]- Why does `filter isPrime [start..]` not loop forever?
> Laziness: only the primes needed by `!!` are computed.

<!-- qard-id: ap-c5d8ee1bc46f10d284c0 -->
> [!qard]- Write `sum` in point-free style.
> `sum' = foldl' (+) 0`.

<!-- qard-id: ap-0865b9b6d66aecab9964 -->
> [!qard]- Write `isEven` in point-free style.
> ``isEven = (== 0) . (`mod` 2)``.

### Trade-offs

<!-- qard-id: ap-c8be25624c359297f1ee -->
> [!qard]- Give three advantages of point-free style.
> Clearer when arguments are only passed through; encourages higher-level, declarative thinking; the "purest" expression of FP.

<!-- qard-id: ap-fdb34a6bd77f7c650028 -->
> [!qard]- Give three disadvantages of point-free style.
> Sometimes less clear; hard to follow when an argument is used in several places; types are hard to read in long chains.
