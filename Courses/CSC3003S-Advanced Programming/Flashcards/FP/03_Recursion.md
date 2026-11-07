---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 03 — Recursion"
---

# FP 03 — Recursion

**Source note:** [Recursion](../../FP/03_Recursion.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Recursion Instead Of Loops|Recursion Instead Of Loops]]
  - [[#Higher-Order Functions|Higher-Order Functions]]
  - [[#Stack Usage|Stack Usage]]
  - [[#Tail Recursion|Tail Recursion]]

## Core Content

### Recursion Instead Of Loops

<!-- qard-id: ap-ef4e0ca6116dd506d4ce -->
> [!qard]- Why does pure Haskell have no loops?
> A loop needs a mutable counter, which breaks immutability.

<!-- qard-id: ap-9d05871bd230f98ca21a -->
> [!qard]- How does recursion map onto a loop?
> The base case is the loop exit; the recursive step is the loop body.

<!-- qard-id: ap-dad9a70cb592c5848ac4 -->
> [!qard]- Why doesn't building a list with `n : buildList (n-1)` break immutability?
> Cons creates a new cell pointing at the existing list; nothing is modified.

### Higher-Order Functions

<!-- qard-id: ap-1a268a3c5159479ebba0 -->
> [!qard]- What is a higher-order function?
> A function that takes a function as an argument or returns one.

<!-- qard-id: ap-1eb1641879da6af7be3e -->
> [!qard]- What do `map`, `filter` and `foldr` do?
> `map` applies a function to each element; `filter` keeps elements satisfying a predicate; `foldr` combines elements from the right with a function and starting value.

<!-- qard-id: ap-ddb5d7449aee919db853 -->
> [!qard]- What does `foldr (+) 0 [1,2,3]` compute and how is it bracketed?
> 6, as $1+(2+(3+0))$.

### Stack Usage

<!-- qard-id: ap-8c29dede30f99971026e -->
> [!qard]- Why can recursion be memory-intensive?
> Each call creates a stack frame; deep recursion can overflow the stack.

<!-- qard-id: ap-0bc23d1fd6a82feb432a -->
> [!qard]- Why is recursion often banned in safety-critical code?
> Reliability concerns over unbounded stack use (e.g. NASA/Lockheed Martin rules).

<!-- qard-id: ap-f8bd821601eafd4afe22 -->
> [!qard]- What stack space does straight-recursive factorial use, and why?
> $O(n)$ — each call waits to multiply by `n` after the recursive call returns.

<!-- qard-id: ap-8d2eea1de1c506e56294 -->
> [!qard]- Why does lazy evaluation of `n * fac (n-1)` collapse to innermost order?
> `*` is strict and needs both operands as values.

### Tail Recursion

<!-- qard-id: ap-879519cd8cebf4ef5553 -->
> [!qard]- What is tail recursion?
> Recursion where the recursive call is the last action, with all work done beforehand.

<!-- qard-id: ap-244580f15d7f358e415f -->
> [!qard]- What is an accumulator?
> An extra parameter carrying the partial result through recursive calls.

<!-- qard-id: ap-496690803beb74b82468 -->
> [!qard]- Why does tail recursion allow $O(1)$ stack space?
> No work remains after the call, so the compiler can reuse the frame.

<!-- qard-id: ap-61f486c5709c7d0732e6 -->
> [!qard]- Why does tail recursion in Haskell need strict evaluation?
> Otherwise the accumulator becomes a growing chain of heap thunks, risking heap overflow instead.

<!-- qard-id: ap-eaae742acd52bec63df5 -->
> [!qard]- Can every recursive function be made tail recursive?
> No — some branching recursion (like doubly recursive Fibonacci) can't be refactored this way.
