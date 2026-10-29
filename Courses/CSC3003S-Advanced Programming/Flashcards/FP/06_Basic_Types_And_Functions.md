---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 06 — Haskell 2 — Basic Types And Functions"
---

# FP 06 — Haskell 2 — Basic Types And Functions

**Source note:** [Haskell 2 — Basic Types And Functions](../../FP/06_Basic_Types_And_Functions.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Types And Data|Types And Data]]
  - [[#Functions And Cases|Functions And Cases]]
  - [[#Algebraic Data Types|Algebraic Data Types]]
  - [[#Type Inference And Typechecking|Type Inference And Typechecking]]
  - [[#Pattern Matching|Pattern Matching]]
  - [[#Sum Types|Sum Types]]
  - [[#Multiple Arguments And Currying|Multiple Arguments And Currying]]
  - [[#Basic Type Distinctions|Basic Type Distinctions]]
  - [[#Constructors And Records|Constructors And Records]]

## Core Content

### Types And Data

<!-- qard-id: ap-97400f96d0d2355b4e5f -->
> [!qard]- How do lists and tuples differ in their types?
> Lists have variable length and homogeneous elements. A tuple has fixed arity, part of its type, and may contain different element types.

<!-- qard-id: ap-c98826864ded7fd6b701 -->
> [!qard]- What is the type of cons, `(:)`?
> `(:) :: a -> [a] -> [a]`: it takes an element and a list of that element type and constructs a new list.

<!-- qard-id: ap-0101a66da176ed75bf52 -->
> [!qard]- How does `(x:xs)` pattern matching decompose a list?
> It matches a nonempty list, binding its first element to `x` and its remaining list to `xs`. It does not match `[]`.

### Functions And Cases

<!-- qard-id: ap-75cf1401b9027159d40d -->
> [!qard]- How are `Int -> Int -> Int` and `add 1 2` grouped?
> The type is `Int -> (Int -> Int)`; the application is `(add 1) 2`. Arrows associate right; application associates left.

<!-- qard-id: ap-a5e1f99c35a52aa222d5 -->
> [!qard]- What is partial application?
> Supplying some arguments to obtain a function expecting the rest; `add 1` has type `Int -> Int` when `add :: Int -> Int -> Int`.

<!-- qard-id: ap-22bf98adc4f81b7ee7ca -->
> [!qard]- Why must an `if` expression include `else` in Haskell?
> It must produce a result on either path, and both branches must have the same type.

<!-- qard-id: ap-a6e0ff738c313eae5e93 -->
> [!qard]- How do guards choose a function result?
> Boolean guards are tested in order; the first true guard selects its expression. `otherwise` is `True`, used as a final fallback.

<!-- qard-id: ap-7182d01e8545ebb472d6 -->
> [!qard]- Why does pattern order matter?
> The first matching equation wins. A catch-all variable or `_` before specific patterns makes those later patterns unreachable.

<!-- qard-id: ap-df160d7daec69d2fe21d -->
> [!qard]- What makes a Haskell function partial?
> Some inputs in its declared type have no defined result, for example `head []`. The type alone does not guarantee totality or termination.

<!-- qard-id: ap-fab40654f77dedca98ef -->
> [!qard]- How does a pair's `fst`/`snd` interface differ from indexing a list?
> It selects a fixed typed position in a two-component product; list indexing selects a runtime position that may be out of range.

<!-- qard-id: ap-3d158ae30642e6c468e9 -->
> [!qard]- What does `otherwise` mean in a guard sequence?
> It is the Boolean value `True`, so it catches remaining inputs only because earlier guards were tried first.

<!-- qard-id: ap-4769ba21b3c8aaa43bd3 -->
> [!qard]- What goes wrong if the catch-all pattern precedes the specific cases?
> It matches every input first, making later special cases unreachable and changing the intended result.

<!-- qard-id: ap-20e8c644e2e501106c3a -->
> [!qard]- Why does `head (x:_) = x` have no result for `[]`?
> The cons pattern requires a cell with a head and tail; the empty constructor does not match. Add an explicit safe result type or require nonempty input.

<!-- qard-id: ap-524e04504bf92b7c2be5 -->
> [!qard]- What type does a partially applied function return?
> Remove the supplied arguments from its curried signature; for `f :: a -> b -> c`, `f x :: b -> c` when `x :: a`.

### Algebraic Data Types

<!-- qard-id: ap-d460aaf1e3b000ffd830 -->
> [!qard]- How do sum and product types differ?
> A sum selects one tagged alternative; a product contains all components together. For finite types, their value counts add and multiply respectively.

<!-- qard-id: ap-ce08223b2c789ef4b778 -->
> [!qard]- In `data IntOrStr = AnInteger Int | AString String`, what do the constructors do?
> They tag which alternative the value contains and carry its payload. Pattern matching recovers that payload.

<!-- qard-id: ap-5b39ac352ce2efec9922 -->
> [!qard]- What does record syntax add to a product type?
> Named fields, accessor functions and record-update notation, while still supporting positional construction and pattern matching.

<!-- qard-id: ap-41b9361a142f4d70a6fc -->
> [!qard]- Does `addr { number = 2 }` mutate `addr`?
> No. It produces a new record with that field changed; the original value is unchanged.

### Type Inference And Typechecking

<!-- qard-id: ap-cd678eb598101b1634fe -->
> [!qard]- What does compile-time typechecking prevent, and what does it not prevent?
> It rejects incompatible uses such as passing a `String` to an `Int` parameter. A well-typed program can still have logical bugs, overflow, partial patterns or divergence.

### Pattern Matching

<!-- qard-id: ap-e489dd7f0c6a3ef2ae60 -->
> [!qard]- What are `_` and variable patterns allowed to match?
> Both match any value; a variable binds it and `_` discards it. Variables must not be repeated in the same pattern; equality relationships require a separate check/guard.

### Sum Types

<!-- qard-id: ap-68c6175c3d790e54fda0 -->
> [!qard]- How many values do a sum and product of finite types with $m$ and $n$ values have?
> A tagged sum has $m+n$ alternatives; a product has $mn$ combinations. The tags keep identically represented payloads in different alternatives distinct.

### Multiple Arguments And Currying

<!-- qard-id: ap-038e1b9d6d1ca1680316 -->
> [!qard]- How does a function taking `(Int, Int)` differ from `Int -> Int -> Int`?
> It receives one pair and must be supplied that pair; the curried function receives one integer and returns a function for the second. `curry`/`uncurry` adapt the calling forms.

### Basic Type Distinctions

<!-- qard-id: ap-b184b3857af694232476 -->
> [!qard]- What does a type restrict about a binding or expression?
> The kinds of values and operations that are valid at that use. A function's signature constrains both what it accepts and what it promises to return.

<!-- qard-id: ap-838e6bb9743d6684a06c -->
> [!qard]- When should `Integer` be preferred over `Int`?
> When results may exceed the fixed-size integer range and arbitrary precision is needed; operations/storage then depend on the integer's growing bit length.

<!-- qard-id: ap-3602b18e0e084ae82b24 -->
> [!qard]- How does `Char` differ from `String`?
> `Char` is one character value, normally written with single quotes; `String` is a list of characters, normally written with double quotes.

<!-- qard-id: ap-87184b445cc2a510a8e5 -->
> [!qard]- Is unit `()` the same as absence represented by `Nothing`?
> No. Unit is a type with one ordinary value; `Nothing` is one constructor of `Maybe a`, representing absence of an optional payload.

<!-- qard-id: ap-d986774235e95bbdd09e -->
> [!qard]- Why does `[]` need no fixed element type written in its syntax?
> It contains no element contradicting a candidate type, so context or a polymorphic signature can determine its list element type.

<!-- qard-id: ap-8db6886f2e17039cc042 -->
> [!qard]- Why is list length absent from a normal list type but tuple arity present in a tuple type?
> `[a]` describes lists of any finite or potentially infinite length; `(a,b)` and `(a,b,c)` are distinct product types with different numbers of positions.

### Constructors And Records

<!-- qard-id: ap-caa6ab1144d8520b24fe -->
> [!qard]- How does a data constructor differ from a type constructor?
> A data constructor builds values, such as `Just x`; a type constructor builds types, such as `Maybe Int`. Their roles occupy different levels of the language.

<!-- qard-id: ap-f24d9b8bf1af967d15c5 -->
> [!qard]- What is the type of `Just`, viewed as a value constructor?
> `Just :: a -> Maybe a`: it wraps one payload in the optional-value type. `Nothing` has type `Maybe a` without a payload.

<!-- qard-id: ap-0c65249785ccab51ea94 -->
> [!qard]- How does pattern matching recover data stored by a constructor?
> Match the constructor and bind its fields, e.g. `AString s` selects that sum alternative and exposes the string `s`.

<!-- qard-id: ap-038536b0e926773ec004 -->
> [!qard]- How can one ADT combine sums and products?
> Alternatives are joined by `|`, and each alternative can carry several fields; e.g. `Shape = Circle Radius | Rectangle Width Height` selects a case with its associated product data.

<!-- qard-id: ap-35efe44aefb238385479 -->
> [!qard]- What does a record field accessor do?
> It is a function extracting that named field from the corresponding record value; named syntax does not change immutability.
