---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 12 — Monads"
---

# FP 12 — Monads

**Source note:** [Monads](../../FP/12_Monads.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Bind|Bind]]
  - [[#The Monad Family|The Monad Family]]
  - [[#Effects|Effects]]
  - [[#IO And do Notation|IO And do Notation]]

## Core Content

### Bind

<!-- qard-id: ap-e0a923535492afef8be2 -->
> [!qard]- What does `>>=` (bind / flat-map) do?
> Applies a function returning a wrapped value to the value inside a wrapper, then flattens the result to one layer.

<!-- qard-id: ap-f323f1d2a6ef0e29db74 -->
> [!qard]- Give the type of `>>=`.
> `(>>=) :: Monad m => m a -> (a -> m b) -> m b`.

<!-- qard-id: ap-987fda4f5580e684ed62 -->
> [!qard]- How does `>>=` let a `Maybe` pipeline fail gracefully?
> A `Just` value passes to the next step; the first `Nothing` short-circuits all remaining steps.

<!-- qard-id: ap-1d3f43020d592a280090 -->
> [!qard]- What does `>>=` do on lists?
> Maps a list-returning function over the list, then concatenates: `[1,2,3] >>= \n -> [1..n]` is `[1,1,2,1,2,3]`.

<!-- qard-id: ap-19aed526791d68868a33 -->
> [!qard]- What is `listToMaybe`?
> A safe `head`: `Just` the first element, or `Nothing` for an empty list.

### The Monad Family

<!-- qard-id: ap-c157b222459045264331 -->
> [!qard]- What is a monad?
> A typeclass of wrapper types supporting `pure` and `>>=` — e.g. `Maybe`, lists and `IO`.

<!-- qard-id: ap-c6b0524dc801fd857536 -->
> [!qard]- What does `pure` do?
> Wraps a value in the monad (`Just x`, `[x]`).

<!-- qard-id: ap-1200b7c8d30d86973cad -->
> [!qard]- What are `fmap` and `<$>`?
> Apply a function to the value inside a structure; `<$>` is infix `fmap`.

<!-- qard-id: ap-b9c12d5bf29d737c0417 -->
> [!qard]- What does `<*>` do?
> Applies a wrapped function to a wrapped value: `(*) <$> Just 1 <*> Just 3 = Just 3`.

<!-- qard-id: ap-21da0392c2dcc5243763 -->
> [!qard]- How are Functor, Applicative and Monad related?
> Every Monad is an Applicative, and every Applicative is a Functor — not the other way round.

<!-- qard-id: ap-27cb9c1fccc987935918 -->
> [!qard]- What do `>>` and `*>` do?
> Sequence two actions, combining their structure but discarding the first value; `>>` is the Monad version of the more general `*>`.

### Effects

<!-- qard-id: ap-4255c577cb0d089f20d5 -->
> [!qard]- Why can't `fmap` alone express the failing pipeline?
> `fmap` can only change the values inside, never the structure (it can't abort or change length).

<!-- qard-id: ap-a09e7fdcacfd04dc825a -->
> [!qard]- What is an effect, in monad terms?
> A change to the structure around a value — failing, producing many values, doing I/O.

<!-- qard-id: ap-04879b3bf6340dc2db91 -->
> [!qard]- What higher information do `Maybe`, lists and `IO` carry?
> Presence/absence; multiple values; whether and what I/O is performed.

<!-- qard-id: ap-5ad3bd3e4aee86b936fd -->
> [!qard]- How can `filter` be written with bind?
> `xs >>= \x -> if f x then [x] else []`.

<!-- qard-id: ap-0fda9ea96e1ff61bbb74 -->
> [!qard]- How can a monad act as a gatekeeper?
> All operations pass through its `>>=`/`<*>`, so it can track or record effects (e.g. counting calls, logging I/O).

### IO And do Notation

<!-- qard-id: ap-f521598db502b935d050 -->
> [!qard]- Why is `getLine` typed `IO String` and not `String`?
> Each call can return different input; `IO` tells the compiler it's impure and can't be replaced by a value.

<!-- qard-id: ap-ca700fa72e558fad6bb1 -->
> [!qard]- What does `>>=` do in the `IO` monad?
> Passes the result value on and merges the I/O effects, even when the value is discarded.

<!-- qard-id: ap-d580f90c1fa0736717a7 -->
> [!qard]- What is `do` notation?
> Syntactic sugar for chains of `>>=` and `>>`.

<!-- qard-id: ap-f34a47b070519c091f53 -->
> [!qard]- What may each statement in a `do` block be?
> A `let`, a `name <- action`, or a monadic value.

<!-- qard-id: ap-3d34a6c352f7438f1534 -->
> [!qard]- What do `<-`, `let` and `pure` do inside `do`?
> `<-` unwraps a monadic result; `let` binds a temporary value; `pure` wraps a value.

<!-- qard-id: ap-5d6e7d8a26efb3b67e62 -->
> [!qard]- Why does `let x = x + 2` in a `do` block loop forever?
> It defines `x` recursively in terms of itself rather than updating it.
