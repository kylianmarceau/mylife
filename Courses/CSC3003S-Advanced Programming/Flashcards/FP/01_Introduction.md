---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 01 — Introduction To Functional Programming"
---

# FP 01 — Introduction To Functional Programming

**Source note:** [Introduction To Functional Programming](../../FP/01_Introduction.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Functional Programming|Functional Programming]]
  - [[#Purity And Immutability|Purity And Immutability]]
  - [[#Haskell And Typing|Haskell And Typing]]
  - [[#Benefits And Costs|Benefits And Costs]]

## Core Content

### Functional Programming

<!-- qard-id: ap-3ef543725b9cf85d20e1 -->
> [!qard]- What is functional programming?
> Declarative programming by composing and applying mathematical functions.

<!-- qard-id: ap-ff7661c022b10fe919ab -->
> [!qard]- What are FP's three core features?
> Immutable data, pure functions, and first-class functions.

<!-- qard-id: ap-17ae49db03a53414cca3 -->
> [!qard]- What are first-class functions?
> Functions that can be passed as arguments, returned as values and stored like any other data.

<!-- qard-id: ap-7a77ead0db7d32bb8fce -->
> [!qard]- Imperative versus declarative programming?
> Imperative says how, step by step. Declarative says what (the logic/goal) and leaves state and control flow to the system.

<!-- qard-id: ap-54238925e9545553b937 -->
> [!qard]- Which paradigms are declarative, with an example language each?
> Functional (Haskell) and logic (Prolog).

### Purity And Immutability

<!-- qard-id: ap-3d9658ac860fdc0fdd75 -->
> [!qard]- What is a side effect?
> Any effect beyond returning a value — changing globals, mutating arguments, I/O, network requests.

<!-- qard-id: ap-3f9ea98872ba2fe00b2b -->
> [!qard]- Why are side effects a problem?
> Same inputs can give different outputs (nondeterminism), making code hard to debug and reason about.

<!-- qard-id: ap-d816c8fa0736bbf91c28 -->
> [!qard]- What is immutable data?
> Data bound to a name at initialisation and never changed; FP creates new values instead of mutating.

<!-- qard-id: ap-1e4a3f950ef21193b207 -->
> [!qard]- What is a pure function?
> A function that always returns the same output for the same input and has no side effects.

<!-- qard-id: ap-40ecbb358b20962f938d -->
> [!qard]- What is referential transparency?
> An expression can be replaced by its value without changing the program's behaviour.

<!-- qard-id: ap-a34f30af1b1a86621543 -->
> [!qard]- Give two kinds of operation that break referential transparency.
> Non-deterministic functions (time, random) and external input/output.

### Haskell And Typing

<!-- qard-id: ap-18ec79b22eae57ee1d36 -->
> [!qard]- Where does Haskell sit among languages?
> Statically typed, functional, lazily evaluated and pure (SML is functional but eager and impure).

<!-- qard-id: ap-b6a70eb834ce88bb0f76 -->
> [!qard]- Static versus dynamic typing?
> Static: types fixed at compile time — fewer bugs, better optimisation, more verbose. Dynamic: types fixed at run time — faster to write, risk of run-time errors.

<!-- qard-id: ap-df0c382cdaaef8aec278 -->
> [!qard]- What replaces loops and mutation in FP style?
> Recursion and new allocations; programs are designed as data flowing through composed functions.

### Benefits And Costs

<!-- qard-id: ap-2118745affaaa58e343f -->
> [!qard]- Why does FP suit parallelism?
> Immutable data and pure functions remove shared mutable state, so there's no "writing while reading".

<!-- qard-id: ap-fb7beb94c473209cc7da -->
> [!qard]- Why does FP improve code clarity?
> It hides low-level details, has high-level operations (map/filter/reduce), and pure functions can be tested in isolation.

<!-- qard-id: ap-afb96df1a35d2c3828a4 -->
> [!qard]- What are FP's costs?
> Less fine-grained performance control, and memory overhead from laziness (thunks) and recursion.

<!-- qard-id: ap-1658e683882ed045b6ba -->
> [!qard]- Why doesn't adding lambdas to an imperative language give the full benefits of FP?
> Imperative languages are mutable by default and need discipline; FP is immutable by default.
