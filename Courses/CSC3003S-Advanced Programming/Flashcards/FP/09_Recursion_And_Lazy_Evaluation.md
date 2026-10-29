---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 09 — Haskell 5 — Recursion And Lazy Evaluation"
---

# FP 09 — Haskell 5 — Recursion And Lazy Evaluation

**Source note:** [Haskell 5 — Recursion And Lazy Evaluation](../../FP/09_Recursion_And_Lazy_Evaluation.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#State And Delayed Work|State And Delayed Work]]
  - [[#Sharing And Productive Recursion|Sharing And Productive Recursion]]
  - [[#Recursion As For Loops|Recursion As For Loops]]
  - [[#Naturally Recursive Functions: Fibonacci And Quicksort|Naturally Recursive Functions: Fibonacci And Quicksort]]
  - [[#Tail-Recursive And Fold-Based Fibonacci|Tail-Recursive And Fold-Based Fibonacci]]
  - [[#Loop Translation And Recursive Structure|Loop Translation And Recursive Structure]]
  - [[#Space And Memoisation|Space And Memoisation]]
  - [[#Choosing An Expression Of The Algorithm|Choosing An Expression Of The Algorithm]]

## Core Content

### State And Delayed Work

<!-- qard-id: ap-397f7ad83ac2909c47df -->
> [!qard]- How can recursion implement a `while` loop with several state variables?
> Give the helper one parameter per state value; return at the stopping condition and otherwise recurse with updated arguments.

<!-- qard-id: ap-a5b9fddbc43ab35dc2d7 -->
> [!qard]- Why does naive recursive Fibonacci remain inefficient in a lazy language?
> Separate calls need not share a cached result just because their arguments are equal. The branching recurrence repeatedly solves the same subproblems.

<!-- qard-id: ap-0ee51a6b8a4ec114c311 -->
> [!qard]- Why can `foldl (+) 0 xs` consume excessive memory?
> The accumulator may become a nested chain of unevaluated additions rather than a running numeric value.

<!-- qard-id: ap-bcc6d638e82e0c7783c1 -->
> [!qard]- How does `foldl'` address this problem?
> It forces each new accumulator to weak head normal form before proceeding, preventing a growing thunk chain for a simple numeric accumulator.

<!-- qard-id: ap-ab78295219b1c08177bc -->
> [!qard]- What does `seq :: a -> b -> b` force?
> Its first argument to weak head normal form, then it returns the second. It does not recursively evaluate every field of a structure.

<!-- qard-id: ap-14bf0416a8f7e0a9d91a -->
> [!qard]- Why might `foldl'` still retain thunks inside a pair accumulator?
> Forcing a pair exposes only its outer constructor; its fields may remain lazy. Force the fields too when bounded memory depends on them.

<!-- qard-id: ap-643adc7f76e12595797a -->
> [!qard]- Why does changing a numeric sum from `foldl` to `foldr` not automatically fix its space use?
> `(+)` needs both numeric operands, so it must still evaluate the nested tail computation. Association alone does not remove pending work.

### Sharing And Productive Recursion

<!-- qard-id: ap-c5048779433036302181 -->
> [!qard]- How does a lazy array memoise Fibonacci states?
> Array entries are shared thunks referring to earlier entries; forcing a needed state stores its result for later reuse.

<!-- qard-id: ap-724ebae616c398b1054f -->
> [!qard]- When can Fibonacci avoid a full table?
> For the final value alone, carry only the previous two values, forcing them as needed. This uses constant many stored integers, whose bit sizes still grow.

<!-- qard-id: ap-470e96c470976cc1246f -->
> [!qard]- What is guarded recursion on a list?
> Put the recursive call beneath a constructor, e.g. `map f (x:xs) = f x : map f xs`, so the next cell can be produced before the tail is demanded.

<!-- qard-id: ap-2c4b016a140beba9a0f9 -->
> [!qard]- When can `foldr` consume an infinite list productively?
> When its combining function can produce a result without demanding the entire folded tail, such as short-circuiting `any` or constructing a list prefix.

### Recursion As For Loops

<!-- qard-id: ap-1f8e6727320d41bee347 -->
> [!qard]- What recursive equations implement `map` and `foldr`?
> `map f [] = []`; `map f (x:xs) = f x : map f xs`. `foldr f z [] = z`; `foldr f z (x:xs) = f x (foldr f z xs)`.

### Naturally Recursive Functions: Fibonacci And Quicksort

<!-- qard-id: ap-feeb0a121e03a8dba800 -->
> [!qard]- How does the functional-list quicksort in the notes partition and recombine?
> For `(pivot:xs)`, recursively sort `[x | x <- xs, x <= pivot]` and `[x | x <- xs, x > pivot]`, then concatenate smaller, `[pivot]`, larger. Base case is `[]`; comparisons require `Ord a`.

### Tail-Recursive And Fold-Based Fibonacci

<!-- qard-id: ap-dd113ea185596fa6485f -->
> [!qard]- What state update computes Fibonacci with only two running values?
> Start `(a,b)=(0,1)` and repeat `(a,b) <- (b,a+b)` exactly `n` times, then return `a`. Force numeric fields when needed to avoid retained thunks; the returned component and iteration count determine off-by-one behaviour.

### Loop Translation And Recursive Structure

<!-- qard-id: ap-d19cc4d342dc27d31e3d -->
> [!qard]- Why might a loop translation need a helper with more parameters than the public function?
> Its changing internal state includes counters, partial results or flags not supplied by the original caller; initialise them once and pass updated values recursively.

<!-- qard-id: ap-aa3c455249723120cdce -->
> [!qard]- How does a recursive search model an unbounded `while` loop?
> It models the unbounded search operator ($\mu$). Test the stopping condition, otherwise update the state and recurse. Termination depends on eventually finding the condition, not a predetermined iteration count.

<!-- qard-id: ap-13108c99b46a20f8581a -->
> [!qard]- What must a “kth next” search track besides its current candidate?
> The number of qualifying results still required; decrease it only when the candidate qualifies, and define whether the initial candidate is included.

<!-- qard-id: ap-ac27c2e4d4efdd3149d7 -->
> [!qard]- Why should base cases precede a catch-all recursive equation in Haskell?
> Equations are tried in order; a general pattern first can recursively match even the intended stopping inputs.

<!-- qard-id: ap-2989ac6eab3eab305a9b -->
> [!qard]- How does a recursive `sum` split a list problem?
> `sum [] = 0`; `sum (x:xs) = x + sum xs`. The head contributes once and the tail is the smaller subproblem.

### Space And Memoisation

<!-- qard-id: ap-51e930baf7328f6e472b -->
> [!qard]- Why does the mathematical tail-call shape not prove a lazy numeric accumulator stays small?
> The argument may be a delayed expression containing references to earlier arguments; force the relevant values or rely on justified strictness analysis.

<!-- qard-id: ap-20a1589f6c0b51b6aefa -->
> [!qard]- How does `seq` differ from fully evaluating a nested structure?
> It forces only the outer value/constructor to weak head normal form, so inner fields or list tails can remain unevaluated.

<!-- qard-id: ap-f654ef73076432a4ebfd -->
> [!qard]- Why can `foldl'` be the suitable default for a finite strict numeric reduction?
> It forces each numeric accumulator as the traversal progresses, avoiding a chain of pending arithmetic while preserving the left-fold operand order.

<!-- qard-id: ap-5c8e15938070261ba239 -->
> [!qard]- What does a memoisation table need for recursive dependencies to work?
> Shared indexed cells, correct base states and dependencies that can be computed without an unproductive cycle; laziness alone cannot repair a cyclic invalid recurrence.

<!-- qard-id: ap-efc555303ec0423d8f31 -->
> [!qard]- Why does a Fibonacci array use more retained state than a two-value recurrence?
> It keeps every prior result for arbitrary reuse/indexing; only the previous two are necessary for computing one final Fibonacci value.

### Choosing An Expression Of The Algorithm

<!-- qard-id: ap-080209d500d3a4efe94d -->
> [!qard]- Why might `map` express intent more clearly than a hand-written recursive transformer?
> Its standard contract says “one mapped output per input”; readers need not reconstruct that invariant from the recursion.

<!-- qard-id: ap-16fb80cc94792194f394 -->
> [!qard]- How does guarded recursion support streaming output?
> Producing a constructor exposes the next cell before demanding the recursive tail, so consumers can request only the needed prefix.

<!-- qard-id: ap-caa4bf4477bdb8249f2a -->
> [!qard]- What could make a recursively generated list unproductive despite an infinite-looking definition?
> It recurses again before exposing the next constructor/value, so no finite prefix can be obtained.

<!-- qard-id: ap-7586637fbe29d330d6db -->
> [!qard]- Why does choosing a good algorithm still matter in a lazy language?
> Laziness can skip unused work and share deliberately linked computations, but it does not automatically remove an exponential recurrence or excessive state space.
