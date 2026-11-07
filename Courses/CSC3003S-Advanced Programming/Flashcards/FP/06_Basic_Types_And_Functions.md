---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 06 — Basic Types And Functions"
---

# FP 06 — Basic Types And Functions

**Source note:** [Basic Types And Functions](../../FP/06_Basic_Types_And_Functions.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Types|Types]]
  - [[#Lists And Tuples|Lists And Tuples]]
  - [[#Functions And Currying|Functions And Currying]]
  - [[#Defining Functions|Defining Functions]]
  - [[#Algebraic Data Types|Algebraic Data Types]]

## Core Content

### Types

<!-- qard-id: ap-bca5d19708949c8766e0 -->
> [!qard]- What is a type?
> A name for a collection of related values; it restricts what a binding can hold.

<!-- qard-id: ap-7210d6961b57c77c76db -->
> [!qard]- What does `e :: T` mean?
> Expression `e` has type `T`.

<!-- qard-id: ap-d2778d76bb7c903e3227 -->
> [!qard]- When are Haskell type errors detected, and why is that good?
> At compile time, eliminating run-time type errors.

<!-- qard-id: ap-c8e926981d260660e259 -->
> [!qard]- What is the unit type `()`?
> A type meaning "no value", used e.g. for IO actions that return nothing.

<!-- qard-id: ap-3f3d81079afe5f58af34 -->
> [!qard]- `Int` versus `Integer`?
> `Int` is fixed-size; `Integer` is arbitrary precision.

### Lists And Tuples

<!-- qard-id: ap-66e1f673f037f27c3ce6 -->
> [!qard]- What is a list in Haskell?
> An ordered, variable-length sequence of values all of the same type, e.g. `[Int]`.

<!-- qard-id: ap-ac397977fe9a8a782705 -->
> [!qard]- How is a list defined recursively?
> `data List a = [] | a : List a` — empty, or an element consed onto a list.

<!-- qard-id: ap-31c40c47c6ec64bf8b4f -->
> [!qard]- What is cons?
> The `:` operator joining an element to the front of a list; `[1,2,3]` is `1:2:3:[]`.

<!-- qard-id: ap-08d5a6eb4fb5b61d52b0 -->
> [!qard]- What is a tuple, and how does it differ from a list?
> A fixed-length sequence of possibly different types; lists are variable-length and homogeneous.

<!-- qard-id: ap-c888e02422909c6f76fd -->
> [!qard]- What do `fst` and `snd` do?
> Return the first and second elements of a pair.

### Functions And Currying

<!-- qard-id: ap-8c0fee46d450a9aaf7c1 -->
> [!qard]- Why is `addVals :: Int -> Int -> Int` written that way?
> It's really `Int -> (Int -> Int)`: it takes an `Int` and returns a function.

<!-- qard-id: ap-41f2d615ebc1b5d9f2a8 -->
> [!qard]- What is currying?
> Treating a multi-argument function as a chain of one-argument functions.

<!-- qard-id: ap-354dc7d3de173899c9ef -->
> [!qard]- What is partial application?
> Supplying fewer arguments than a function takes, giving a function awaiting the rest (e.g. `(2 *)`).

<!-- qard-id: ap-f97b0521d5e838d7e092 -->
> [!qard]- What associativity do `->` and function application have?
> `->` is right-associative; application is left-associative.

### Defining Functions

<!-- qard-id: ap-424f2f4bc5fe4ceedbb5 -->
> [!qard]- What is a guarded equation?
> A definition with conditions after `|`, each giving a result, with `otherwise` as the catch-all.

<!-- qard-id: ap-891965911886ae2bd3a2 -->
> [!qard]- In what order are function patterns tried?
> Top to bottom, in definition order; the first match wins.

<!-- qard-id: ap-443840eb66206775cfb7 -->
> [!qard]- What is a partial function?
> One not defined for every input of its type (e.g. `head` on `[]`).

### Algebraic Data Types

<!-- qard-id: ap-c98f6695cfcfe2fa0a52 -->
> [!qard]- What is an algebraic data type?
> A composite type built from other types using sum and product.

<!-- qard-id: ap-a0b29c671d39ec7ced65 -->
> [!qard]- What is a sum type?
> A value is one of several alternatives, e.g. `data Suit = Hearts | Clubs | Spades | Diamonds`.

<!-- qard-id: ap-0bb3bffc34306138b5ff -->
> [!qard]- What is a product type?
> A value combines one value from each component, e.g. `data IntAndStr = IntAndStr Int String`.

<!-- qard-id: ap-a01c1528a0fbac157473 -->
> [!qard]- How many values do sum and product types have, in terms of their parts?
> Sum: $|A|+|B|$. Product: $|A|\times|B|$.

<!-- qard-id: ap-5467dbd5c527dffadb4c -->
> [!qard]- What does record syntax give you?
> Named fields that double as accessor functions, and update syntax `r { field = v }` that returns a copy.

<!-- qard-id: ap-1cf34cba711f7e86025b -->
> [!qard]- What is type inference?
> The compiler working out an expression's type from context, so most type annotations are optional.
