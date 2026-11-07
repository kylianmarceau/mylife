---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 13 — Making Illegal States Unrepresentable"
---

# FP 13 — Making Illegal States Unrepresentable

**Source note:** [Making Illegal States Unrepresentable](../../FP/13_Making_Illegal_States_Unrepresentable.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Core Idea|Core Idea]]
  - [[#Sum Types And Non-Empty Lists|Sum Types And Non-Empty Lists]]
  - [[#Parse, Don't Validate|Parse, Don't Validate]]

## Core Content

### Core Idea

<!-- qard-id: ap-8599ed72ee7c2597f4a5 -->
> [!qard]- What does "make illegal states unrepresentable" mean?
> Design types so that meaningless combinations of values can't be constructed, so the compiler rejects them.

<!-- qard-id: ap-329f0eece9572982e2b8 -->
> [!qard]- What is a wrapper type?
> A new type wrapping an existing one (e.g. `data Inches = In Int`) to give it a distinct, checked meaning.

<!-- qard-id: ap-4f67bb21bc313730bdf8 -->
> [!qard]- How do wrapper types prevent unit mix-ups?
> `(+) :: Num a => a -> a -> a` needs both operands to be the same type, so `Inches + Centimetres` is a type error.

### Sum Types And Non-Empty Lists

<!-- qard-id: ap-8a3c9d54298840bcd54d -->
> [!qard]- Why are three independent `Maybe Time` fields a poor model for message status?
> They allow nonsense such as a read time without a sent time.

<!-- qard-id: ap-bf84e76d979eccc86a3b -->
> [!qard]- How does a sum type like `MsgState` fix message status?
> Each constructor (`Draft`, `Sent`, `Delivered`, `Read`) carries exactly the timestamps that must exist, so illegal combinations can't be built.

<!-- qard-id: ap-9da0b6b5284820f66a5d -->
> [!qard]- How is a non-empty list defined?
> `data NonEmptyList a = NonEmptyList a [a]` — an obligatory first element plus the rest.

<!-- qard-id: ap-5c6cf8c4176b4a0070dc -->
> [!qard]- Why is `head` on a `NonEmptyList` safe?
> There is always a first element, so `head` is total and can't crash.

<!-- qard-id: ap-5962b41e13b5f28e551d -->
> [!qard]- How do you model "one or two values, never zero"?
> `data AtLeastOne a = One a | Two a a` (not `(Maybe a, Maybe a)`, which allows two `Nothing`s).

### Parse, Don't Validate

<!-- qard-id: ap-98b44e4b6a6e03fde669 -->
> [!qard]- What is "parse, don't validate"?
> Convert raw input once, at the boundary, into a type that enforces the constraints, then work only with that type.

<!-- qard-id: ap-cb89edee138b531ce847 -->
> [!qard]- What is shotgun parsing?
> Validation checks scattered throughout the code, mixed with processing logic.

<!-- qard-id: ap-59a908e1d72a1173dbed -->
> [!qard]- Give three benefits of these techniques.
> Validate only once; eliminate whole classes of logic errors; move checks from run time to compile time.

<!-- qard-id: ap-a29830e880f5d13c3d43 -->
> [!qard]- Why not make every constraint a type?
> Going overboard hurts interoperability — e.g. typeclasses for `Int` may not exist for a custom `PrimeInt`.

<!-- qard-id: ap-474f6197eb820800ff38 -->
> [!qard]- Why is Haskell especially suited to this?
> Its expressive type system — particularly sum types — enforces far more constraints than most languages.
