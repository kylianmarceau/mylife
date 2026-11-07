---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 05 — Introduction To Haskell"
---

# FP 05 — Introduction To Haskell

**Source note:** [Introduction To Haskell](../../FP/05_Haskell_Introduction.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#What Haskell Is|What Haskell Is]]
  - [[#Tools|Tools]]
  - [[#Syntax|Syntax]]
  - [[#Conventions|Conventions]]

## Core Content

### What Haskell Is

<!-- qard-id: ap-cc970157b0e5fb0cb337 -->
> [!qard]- What are Haskell's four defining characteristics?
> Functional, pure (no side effects), lazy, and a strict, static, expressive type system with type inference.

<!-- qard-id: ap-b9fc86c9c5b85cd8c0f6 -->
> [!qard]- What does "strict" mean for Haskell's type system?
> Values are never implicitly coerced between types (an `Int` can't become a `String`).

<!-- qard-id: ap-781b5309fdc7de7594e3 -->
> [!qard]- What does "static" mean for Haskell's type system?
> Types are fixed at compile time and can't change at run time.

<!-- qard-id: ap-217ee6cf1db46cd164ef -->
> [!qard]- How does Haskell handle an operation that needs to modify a list?
> It returns a new list with the change; the original is never mutated.

<!-- qard-id: ap-208270fe5f1b82130263 -->
> [!qard]- How can Haskell print without side effects?
> The effect is encoded in the return type `IO ()`, so it's an explicit value, not a hidden side effect.

### Tools

<!-- qard-id: ap-53b402c56f59d1a8082c -->
> [!qard]- What are `ghc`, `ghci` and Cabal?
> The Glasgow Haskell Compiler, its interactive interpreter, and the Haskell package manager.

<!-- qard-id: ap-543fad1a43dafd792a6d -->
> [!qard]- Name four useful GHCi commands.
> `:?` help, `:load file`, `:reload`, `:quit` (and `:{ … :}` for multi-line input).

<!-- qard-id: ap-6a856cad0e74c8c050a7 -->
> [!qard]- How do you run a Haskell script?
> `runghc file.hs` (needs `main`), or load it in GHCi with `ghci file.hs` / `:load`.

### Syntax

<!-- qard-id: ap-0dba3ef1fa8e723dba57 -->
> [!qard]- What does a type signature look like?
> `name :: Type`, e.g. `f :: Float -> Float`.

<!-- qard-id: ap-fb92a0c78dc290e122ab -->
> [!qard]- How are functions applied in Haskell, and how does `f a + b` parse?
> By juxtaposition (a space). Application binds tightest, so `f a + b` is $f(a)+b$.

<!-- qard-id: ap-ec9181c1a783247e3ff4 -->
> [!qard]- What do `head`, `tail`, `!!`, `take` and `drop` do?
> First element; all but the first; index; first $n$ elements; all but the first $n$.

<!-- qard-id: ap-c1f114e4adff50e1c18a -->
> [!qard]- What is a `where` clause for?
> Defining local helper values used in a function's body.

<!-- qard-id: ap-4a898ec1854d7913a2d6 -->
> [!qard]- What do `$` and backticks do?
> `f $ g x` means `f (g x)`; `` a `mod` b `` makes a prefix function infix.

### Conventions

<!-- qard-id: ap-6d337253683b56bf746d -->
> [!qard]- What are Haskell's naming conventions?
> Functions/variables camelCase starting lowercase; types PascalCase; list arguments end in `s` (`xs`).

<!-- qard-id: ap-44c116b7a6a351bab003 -->
> [!qard]- What is the layout rule?
> Whitespace is significant: definitions in a block must start in the same column (or use `{ ; }`).

<!-- qard-id: ap-283c12c4389ac925b502 -->
> [!qard]- What style does Haskell encourage for writing functions?
> Compositions of smaller functions — a pipeline of transformations, not a sequence of actions.

<!-- qard-id: ap-ff502aa452e9bdceac05 -->
> [!qard]- What is the Prelude?
> The standard functions available in every Haskell program without an import.
