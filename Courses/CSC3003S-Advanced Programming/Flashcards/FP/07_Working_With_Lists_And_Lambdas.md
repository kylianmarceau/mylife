---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 07 — Working With Lists And Lambdas"
---

# FP 07 — Working With Lists And Lambdas

**Source note:** [Working With Lists And Lambdas](../../FP/07_Working_With_Lists_And_Lambdas.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Combinators|Combinators]]
  - [[#Lambdas|Lambdas]]
  - [[#Folds|Folds]]
  - [[#Comprehensions|Comprehensions]]

## Core Content

### Combinators

<!-- qard-id: ap-b6c6325502ebefe0fd20 -->
> [!qard]- What is a list combinator?
> A higher-order function such as `map` or `filter` that builds list computations from smaller functions.

<!-- qard-id: ap-e5511010929cd400b1dc -->
> [!qard]- What are a mapper and a predicate?
> The function `map` applies to each element; the Boolean function `filter` uses to keep elements.

<!-- qard-id: ap-4ce1d63cc417732774b1 -->
> [!qard]- What does `zip` do?
> Pairs up two lists element by element into a list of tuples.

<!-- qard-id: ap-25b9ae980894480ad6fb -->
> [!qard]- `takeWhile` versus `dropWhile`?
> `takeWhile p` keeps elements from the front while `p` holds; `dropWhile p` removes them; both stop at the first failure.

<!-- qard-id: ap-18ebe2238f7aef3dc0e6 -->
> [!qard]- What do `all` and `any` return?
> `True` if the predicate holds for every element / for at least one element.

### Lambdas

<!-- qard-id: ap-2b17fc3ef046966e2ba2 -->
> [!qard]- What is a lambda?
> An anonymous function, written `\x -> …` in Haskell.

<!-- qard-id: ap-8954398f57effa9be75f -->
> [!qard]- Give three reasons to use lambdas.
> Avoid one-off named helpers, express currying clearly, and write functions that return functions.

### Folds

<!-- qard-id: ap-93834ea04e3540d1cecf -->
> [!qard]- What three arguments does a fold take?
> A combining function, an initial accumulator, and the list.

<!-- qard-id: ap-2c14d41caae1fff90f22 -->
> [!qard]- What recurrence describes a fold step?
> $acc' = f(acc, elt)$.

<!-- qard-id: ap-2c08d070f1a9e9a8442c -->
> [!qard]- How does `foldl` differ from `foldr`?
> `foldl` is left-associative: $((z\oplus a)\oplus b)\oplus c$. `foldr` is right-associative: $a\oplus(b\oplus(c\oplus z))$.

<!-- qard-id: ap-e656928c3f35e0fcf4a1 -->
> [!qard]- When do `foldl` and `foldr` give different results?
> For non-associative operators like subtraction.

<!-- qard-id: ap-29e2d22da1d1a3274599 -->
> [!qard]- Why is fold the universal list combinator?
> It can implement every other combinator (sum, map, filter) — it's FP's version of a stateful loop.

### Comprehensions

<!-- qard-id: ap-09fee8aaf450eff238fe -->
> [!qard]- What are the generator and guard in `[f | f <- [1..n], n mod f == 0]`?
> Generator: `f <- [1..n]` draws values. Guard: the Boolean condition filtering them.

<!-- qard-id: ap-0a94bad950c4c6620b72 -->
> [!qard]- How do multiple generators behave?
> They produce the Cartesian product like nested loops; the last generator varies fastest.

<!-- qard-id: ap-32dc6aae744e7286009d -->
> [!qard]- How do multiple generators differ from `zip`?
> Generators give every combination; `zip` pairs elements position by position.

<!-- qard-id: ap-00963db419bdbbbb9f44 -->
> [!qard]- What is a dependent generator?
> A later generator that uses an earlier variable, e.g. `[(x,y) | x <- [1..3], y <- [1..x]]`.

<!-- qard-id: ap-52c65e0929ce6bea9b39 -->
> [!qard]- How do you flatten a list of lists with a comprehension?
> `[x | xs <- xss, x <- xs]`.
