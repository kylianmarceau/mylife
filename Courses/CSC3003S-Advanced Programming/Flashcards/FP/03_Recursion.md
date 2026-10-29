---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 03 — Recursion"
---

# FP 03 — Recursion

**Source note:** [Recursion](../../FP/03_Recursion.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Recursive Structure|Recursive Structure]]
  - [[#Tail Recursion|Tail Recursion]]
  - [[#Higher-Order Functions: map, filter, foldr|Higher-Order Functions: map, filter, foldr]]
  - [[#Memory Issues|Memory Issues]]
  - [[#Limits Of Tail Recursion|Limits Of Tail Recursion]]
  - [[#Recursion Mechanics|Recursion Mechanics]]

## Core Content

### Recursive Structure

<!-- qard-id: ap-3ca59c09839047891d26 -->
> [!qard]- What makes a recursive function terminate on its intended inputs?
> A reachable base case and recursive steps that make progress toward it, such as a smaller number or shorter list.

<!-- qard-id: ap-91a343b15bd67ffdf0d0 -->
> [!qard]- How does recursion replace an imperative loop's changing variables?
> Pass the current state as arguments and pass updated values to the next call; the base case replaces the loop's stopping condition.

<!-- qard-id: ap-e357cb6db11369b25979 -->
> [!qard]- Why does `x : xs` preserve immutability?
> It creates a new list cell pointing to the existing unchanged tail `xs`.

<!-- qard-id: ap-8c972a453f291e0dbef4 -->
> [!qard]- When should you prefer `map`, `filter` or a fold to explicit list recursion?
> When the task matches their standard traversal: transform each element, retain selected elements, or combine elements into a result. This usually makes intent clearer.

### Tail Recursion

<!-- qard-id: ap-90509ed40b21d3ab95e5 -->
> [!qard]- What makes a recursive call a tail call?
> The call's result is returned directly; no further work remains after it returns.

<!-- qard-id: ap-42684ed0fec1b085c479 -->
> [!qard]- How does an accumulator turn factorial into tail recursion?
> Carry the partial product: `go 0 acc = acc`; `go n acc = go (n-1) (acc*n)`, starting with `acc = 1` for nonnegative `n`.

<!-- qard-id: ap-7c8db72b45110459138f -->
> [!qard]- Why does tail recursion alone not guarantee constant memory in Haskell?
> The accumulator may remain a growing chain of thunks. Constant stack behaviour also needs compiler support, and bounded thunk growth needs appropriate strictness.

<!-- qard-id: ap-555110bc268874a8e030 -->
> [!qard]- Why is `fac n = n * fac (n-1)` not tail recursive?
> The multiplication by `n` still has to happen after the recursive result is obtained.

### Higher-Order Functions: map, filter, foldr

<!-- qard-id: ap-cb8a224416915a33a6c3 -->
> [!qard]- How do `map`, `filter` and `foldr` act on $[1,2,3]$?
> `map (\x -> x*x)` gives `[1,4,9]`; `filter even` gives `[2]`; `foldr (+) 0` expands to `1+(2+(3+0)) = 6`.

### Memory Issues

<!-- qard-id: ap-7670783d7edbcb1f0a00 -->
> [!qard]- Why can ordinary recursive factorial keep linear pending work despite lazy evaluation?
> Each call leaves a multiplication awaiting the recursive result, and multiplication demands its numeric operands. Laziness does not remove the dependency chain or its memory pressure.

### Limits Of Tail Recursion

<!-- qard-id: ap-684528e58fa566e6abd3 -->
> [!qard]- What limits the benefit of tail recursion?
> It needs suitable optimisation and strict treatment of accumulators for bounded memory; branching recursion is not always conveniently refactored into a single tail call. Allocation and large values may still use substantial heap space.

### Recursion Mechanics

<!-- qard-id: ap-16b2b219b53746aec390 -->
> [!qard]- Why do ordinary mutable loop counters conflict with the pure immutable model?
> Reassigning a counter changes a binding's state. A recursive call instead receives a new counter/state value while the previous binding keeps its meaning.

<!-- qard-id: ap-b9ed3aa5386f78f6762d -->
> [!qard]- Is a base case alone sufficient to prove recursive termination?
> No. Recursive branches must reach it for the intended domain. A decreasing nonnegative measure is a common termination argument.

<!-- qard-id: ap-8c6dac044a660a0ed58b -->
> [!qard]- What is the empty-list base case for a recursive list builder or transformer?
> Return `[]` when there is no remaining input; on a nonempty input, construct the next cell and recurse on the tail or a smaller argument.

<!-- qard-id: ap-57c668cf20a8aaf8de80 -->
> [!qard]- What is an accumulator's invariant?
> A statement connecting the accumulated partial result and remaining input to the original problem, maintained by each recursive update. It explains why the base case returns the intended result.

<!-- qard-id: ap-4e81deceb52840bf3620 -->
> [!qard]- Why start a factorial accumulator at one rather than zero?
> One is multiplication's identity and correctly represents the empty product. Starting at zero would keep every later product zero.

<!-- qard-id: ap-8c1eb6d07ee2a2dcd915 -->
> [!qard]- What pending operation prevents ordinary factorial from being a tail call?
> The caller must multiply the recursive result by its current argument, retaining work until the deeper call returns.

<!-- qard-id: ap-01744a35e732dec8f5eb -->
> [!qard]- How does forcing an accumulator address a lazy tail-recursion space leak?
> It computes the next partial value before passing it onward, rather than retaining an ever-longer expression referring to earlier work.

<!-- qard-id: ap-c71440ebf663295c27d6 -->
> [!qard]- Why does recursion over two branches need more care than a single state-update loop?
> The caller may need both results and a combination step, so one recursive call cannot simply replace the whole current computation.
