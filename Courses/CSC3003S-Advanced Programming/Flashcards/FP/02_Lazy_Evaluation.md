---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 02 — Lazy Evaluation"
---

# FP 02 — Lazy Evaluation

**Source note:** [Lazy Evaluation](../../FP/02_Lazy_Evaluation.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Evaluation And Sharing|Evaluation And Sharing]]
  - [[#Demand And Memory|Demand And Memory]]
  - [[#Redex Examples|Redex Examples]]
  - [[#Sharing With Thunks|Sharing With Thunks]]
  - [[#Demand And Reduction|Demand And Reduction]]

## Core Content

### Evaluation And Sharing

<!-- qard-id: ap-749dc98031fa91d3929d -->
> [!qard]- What three rules define lazy evaluation in these notes?
> Evaluate only when needed, evaluate only as much as needed, and share an evaluated result so the same thunk is not evaluated again.

<!-- qard-id: ap-823c7db011835b0e954e -->
> [!qard]- What is a redex?
> A reducible expression: a subexpression to which a reduction rule or function definition can be applied.

<!-- qard-id: ap-7c7b7e3b806f4bbe8bb1 -->
> [!qard]- How do strict and lazy evaluation differ?
> Strict evaluation evaluates arguments before applying a function. Lazy evaluation delays them until demanded and shares the results.

<!-- qard-id: ap-d64d346e5d34941f3949 -->
> [!qard]- Why can outermost reduction terminate when innermost reduction diverges?
> It may discard an unused non-terminating argument. In pure lambda calculus, leftmost-outermost reduction finds a normal form if one exists.

<!-- qard-id: ap-c14ff434ed155fac5979 -->
> [!qard]- If two reduction orders reach a normal form, can they disagree?
> In pure lambda calculus, no: the normal forms are the same up to renaming bound variables.

<!-- qard-id: ap-aaaa5d18f401e4d6dec8 -->
> [!qard]- What is a thunk, and how does sharing work?
> A thunk stores a delayed computation. References share it; once forced, its result is stored and reused by those references.

<!-- qard-id: ap-c1374c27008b7e06c00e -->
> [!qard]- Why does sharing matter in `square (3+4)` with `square x = x*x`?
> Both uses of `x` can reference one thunk for `3+4`, so the addition is performed once rather than duplicated.

### Demand And Memory

<!-- qard-id: ap-f23a743096c99da2aeab -->
> [!qard]- Why does `fst (1, undefined)` return `1`?
> Only the pair's first component is demanded; its undefined second component is never evaluated.

<!-- qard-id: ap-82968dd05c48394e369b -->
> [!qard]- How can Haskell use an infinite list without looping forever?
> A consumer such as `take 3` demands only a finite prefix, provided producing that prefix itself terminates.

<!-- qard-id: ap-0109b5c7986a3a7ebfc5 -->
> [!qard]- What is the main memory risk of laziness?
> Unevaluated thunks and retained references can accumulate, causing a space leak even when delayed work eventually terminates.

### Redex Examples

<!-- qard-id: ap-e09fd471152cc762d172 -->
> [!qard]- Why can outermost rewriting use more steps than innermost reduction before sharing is introduced?
> Substitution may duplicate an unevaluated argument, as in `square (3+4)`. Lazy implementations share the argument thunk; unused arguments, as in `ignore (square 5)`, can instead be skipped entirely.

### Sharing With Thunks

<!-- qard-id: ap-7cf408f72f7a63c35603 -->
> [!qard]- Does lazy sharing automatically memoise every separately written call with equal inputs?
> No. Reuse follows shared references to a thunk or data structure, rather than a universal cache for all equal function arguments; explicit shared tables can provide that wider memoisation.

### Demand And Reduction

<!-- qard-id: ap-fddb8bbb3e0b525936d5 -->
> [!qard]- Does a function argument containing a non-terminating computation always make the whole expression diverge?
> No. A non-strict function may return without demanding that argument; a strict context that needs it will diverge.

<!-- qard-id: ap-21a23fa96b5b972d43f5 -->
> [!qard]- What does “evaluate only enough” mean for a structured value?
> Expose just the constructor, component or prefix needed by the consumer. Demanding a pair's first field need not evaluate its second field or every nested value.

<!-- qard-id: ap-a67897e0b4d74b4303ea -->
> [!qard]- How does call-by-need sharing differ from repeatedly substituting an argument expression?
> All uses of the bound argument can reference one shared thunk. Repeated textual substitution can duplicate its computation, even when it denotes the same pure expression.

<!-- qard-id: ap-f96e161f642126286741 -->
> [!qard]- Why are strict arithmetic operators relevant even inside a lazy language?
> Producing a numeric result for operations such as multiplication demands the numeric operands, which in turn can force further delayed work.

<!-- qard-id: ap-9a92d7bed406256508f4 -->
> [!qard]- Does the existence of a normal form mean every reduction sequence terminates?
> No. Leftmost-outermost reduction reaches a normal form when one exists; a different strategy can keep reducing an unnecessary divergent subexpression.

<!-- qard-id: ap-fb681b89385fa8aa4a70 -->
> [!qard]- How is memoisation related to sharing without being identical to a universal function cache?
> Sharing retains the result attached to a particular thunk. A deliberately memoised function/table organises reuse across requested states; equal calls need not automatically share.

<!-- qard-id: ap-62f3f1b7a0faf26da27d -->
> [!qard]- When does a finite consumer still fail on an infinite list?
> If the demanded prefix cannot be produced, or the consumer needs the entire structure—for example, `length` cannot finish on an infinite list.

<!-- qard-id: ap-5394e8eec00cfc6dd625 -->
> [!qard]- Why can `take n` on a generated stream save intermediate storage?
> A lazy producer and consumer can interleave, producing only demanded cells instead of materialising every potential element before processing begins.
