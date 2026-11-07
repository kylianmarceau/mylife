---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 09 — Recursion And Lazy Evaluation In Haskell"
---

# FP 09 — Recursion And Lazy Evaluation In Haskell

**Source note:** [Recursion And Lazy Evaluation In Haskell](../../FP/09_Recursion_And_Lazy_Evaluation.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Recursion As Loops|Recursion As Loops]]
  - [[#foldl, foldr And foldl'|foldl, foldr And foldl']]
  - [[#Fast Fibonacci|Fast Fibonacci]]
  - [[#Style|Style]]

## Core Content

### Recursion As Loops

<!-- qard-id: ap-f2980e0b7bfd3133ebca -->
> [!qard]- What are Haskell's equivalents of `for` and `while` loops?
> `for`: folds. `while`: recursion — which can implement any kind of loop.

<!-- qard-id: ap-683b38d396421a86d18e -->
> [!qard]- How do you translate a `while` loop into recursion?
> Pass the loop state forward as arguments to a recursive helper; the condition becomes a guard or base case.

<!-- qard-id: ap-f3a163729f3b86730c35 -->
> [!qard]- Why define a helper like `go`/`searchPrime` inside a recursive function?
> It carries the loop state (and initial value) without exposing extra parameters to callers.

<!-- qard-id: ap-19c5d3f86b2fadad13d5 -->
> [!qard]- What two parts must a terminating recursive function have?
> A recurrence relation (the self-call) and a base case (the simplest input, which stops recursion).

<!-- qard-id: ap-6d7ec03668d7675293c1 -->
> [!qard]- Why does `qsort` need an `Ord a` constraint?
> It compares elements with `<=` and `>`.

### foldl, foldr And foldl'

<!-- qard-id: ap-eaf4bfadb47565cc7dcb -->
> [!qard]- Why can `foldl (+) 0 [1..300_000_000]` overflow?
> Laziness defers every addition, building ~300 million nested thunks before anything is evaluated.

<!-- qard-id: ap-338fb001e23c37ece398 -->
> [!qard]- Why doesn't `foldr` fix the large-sum overflow?
> $1+(2+(3+\dots))$ must resolve the inner sums first, so it also nests pending work.

<!-- qard-id: ap-40c0caf217bff4bebf6b -->
> [!qard]- What does `foldl'` do differently?
> It forces the accumulator at every step (with `seq`), so the sum collapses as it goes.

<!-- qard-id: ap-2d608e4a487717bfdf1f -->
> [!qard]- What does `seq a b` do?
> Strictly evaluates `a`, then returns `b`.

<!-- qard-id: ap-783d3cabe8b4216766dc -->
> [!qard]- What is the key rule for recursion in Haskell?
> Think of the thunks — keep unevaluated thunks down by forcing strictness where needed.

### Fast Fibonacci

<!-- qard-id: ap-b6097f0e302754650e45 -->
> [!qard]- What is memoisation?
> Caching previously computed function results.

<!-- qard-id: ap-6266e7fc2da87b4841d3 -->
> [!qard]- How does lazy dynamic programming memoise Fibonacci?
> Build an array whose entries are defined in terms of earlier entries; laziness computes each once on demand.

<!-- qard-id: ap-93a02c9a54515c6964e6 -->
> [!qard]- What is the space cost of the lazy-DP Fibonacci, and how can it improve?
> $O(n)$; keeping only the last two values gives $O(1)$.

<!-- qard-id: ap-08b65ce81b7f976a9151 -->
> [!qard]- How does tail-recursive Fibonacci achieve $O(1)$ space?
> It passes the last two values as accumulators, and strict `+` prevents thunk build-up.

<!-- qard-id: ap-8541fe86800abce0aaed -->
> [!qard]- How can Fibonacci be written with a fold?
> `foldl'` over `[1..n]` carrying the pair $(\text{fib}(i),\text{fib}(i-1))$.

<!-- qard-id: ap-82aab6a95d781c636f47 -->
> [!qard]- Is tail recursion as important in Haskell as in strict languages?
> Less so — laziness means thunks matter more than the call stack.

### Style

<!-- qard-id: ap-5110a8631c3f15842323 -->
> [!qard]- Recursion or combinator — which should you prefer?
> A matter of taste, but combinators state intent more clearly; keep code readable.

<!-- qard-id: ap-46e170783c8926bc50c9 -->
> [!qard]- What is guarded recursion?
> Putting the recursive call inside a data constructor, e.g. `f x : map f xs`, so later parts are computed only on demand.

<!-- qard-id: ap-feae5d6647776967e2e5 -->
> [!qard]- How is quicksort written in Haskell?
> `qsort [] = []`; `qsort (x:xs) = qsort [a | a <- xs, a <= x] ++ [x] ++ qsort [a | a <- xs, a > x]`.
