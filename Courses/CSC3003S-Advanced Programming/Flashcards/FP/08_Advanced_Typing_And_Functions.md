---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 08 — Advanced Typing And Functions"
---

# FP 08 — Advanced Typing And Functions

**Source note:** [Advanced Typing And Functions](../../FP/08_Advanced_Typing_And_Functions.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Polymorphism|Polymorphism]]
  - [[#Typeclasses|Typeclasses]]
  - [[#Maybe|Maybe]]
  - [[#Kinds And Hoogle|Kinds And Hoogle]]

## Core Content

### Polymorphism

<!-- qard-id: ap-276cc7469c176bb80c87 -->
> [!qard]- What is polymorphism?
> "Having many forms": a function or type that works for many types.

<!-- qard-id: ap-6f6b3596ba9cff476baa -->
> [!qard]- What is a type variable?
> A type parameter such as `a` in `a -> a -> a`, standing for any type.

<!-- qard-id: ap-ef08059d67667ead9805 -->
> [!qard]- Why does `add :: a -> a -> a; add x y = x + y` fail to compile?
> `a` is unconstrained, but not every type supports `+`.

<!-- qard-id: ap-1c84e0fff9d2bc018a06 -->
> [!qard]- What is a type constraint?
> A restriction like `Num a =>` limiting a type variable to instances of a typeclass.

<!-- qard-id: ap-93c63c8116ab596fa0d6 -->
> [!qard]- What is an overloaded function?
> A function with one or more constraints on its type parameters.

### Typeclasses

<!-- qard-id: ap-12b62d75b65f4d6e7b79 -->
> [!qard]- What is a typeclass?
> A named set of behaviours a type can implement — like an interface or Rust trait, not an OOP class.

<!-- qard-id: ap-9b63cb8d7e2103901e92 -->
> [!qard]- Typeclass versus OOP class?
> A typeclass specifies behaviour only, a type can implement many, and instances can be written for foreign types. An OOP class bundles data and logic, usually with single inheritance.

<!-- qard-id: ap-369073dc2ac8f90803db -->
> [!qard]- What does a typeclass definition contain?
> Member signatures that instances must implement, plus optional default implementations.

<!-- qard-id: ap-61d108919f82600ec621 -->
> [!qard]- What does `Show` require, and what is its convention?
> `show :: a -> String`; the output should be valid Haskell, for debugging rather than pretty-printing.

<!-- qard-id: ap-6c1ccc4b504395e24837 -->
> [!qard]- What does `deriving Show` do?
> Makes the compiler generate the `Show` instance automatically.

### Maybe

<!-- qard-id: ap-55eea8c9f9550575d5e0 -->
> [!qard]- Why does Haskell have no null?
> Null causes run-time errors; optional values are made explicit in the type instead.

<!-- qard-id: ap-c8222c00211ef7b538d7 -->
> [!qard]- Define `Maybe`.
> `data Maybe a = Nothing | Just a`.

<!-- qard-id: ap-4d02647c393ece9b9e62 -->
> [!qard]- Why is using `""` or `0` for "no value" a problem?
> It's a type error the compiler can't catch — every use site must remember to check.

<!-- qard-id: ap-90538512ba124c41fd95 -->
> [!qard]- How does `Maybe` prevent missing-value bugs?
> Code can't use a `Maybe String` as a `String`; the compiler forces you to handle `Nothing`.

<!-- qard-id: ap-eab71e30608b64da8f64 -->
> [!qard]- What does `mapMaybe` do?
> Applies a function returning `Maybe`, keeping the `Just` values and dropping `Nothing`s.

### Kinds And Hoogle

<!-- qard-id: ap-9bfddb2f51c81b2d4a0f -->
> [!qard]- What is a type constructor?
> A generic type like `Maybe`, viewed as a function from types to types (`Int` to `Maybe Int`).

<!-- qard-id: ap-a1cc8eff13e46fa0f26d -->
> [!qard]- What is a kind, and what is the kind of `Maybe`?
> The type of a type; `*` is a concrete type, so `Maybe :: * -> *`.

<!-- qard-id: ap-40066bce2caf369a7f2c -->
> [!qard]- What is Hoogle?
> A Haskell search engine that finds functions by type signature.
