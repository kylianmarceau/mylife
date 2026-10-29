---
tags:
  - advanced-programming
---

# Haskell 9 — Making Illegal States Unrepresentable

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP 13-Haskell 9-Making illegal states unrepresentable.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%2013-Haskell%209-Making%20illegal%20states%20unrepresentable.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–12  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: wrapper types, modelling state with sum types, non-empty lists, "parse, don't validate", and when to stop.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Idea|The Idea]]
  - [[#Wrapper Types: The Mars Climate Orbiter|Wrapper Types: The Mars Climate Orbiter]]
  - [[#Modelling Message State With Sum Types|Modelling Message State With Sum Types]]
  - [[#Non-Empty Lists|Non-Empty Lists]]
  - [[#Applications: Parse, Don't Validate|Applications: Parse, Don't Validate]]
  - [[#Don't Go Overboard|Don't Go Overboard]]
  - [[#Why Haskell Here|Why Haskell Here]]

---

## Core Content

### The Idea

#### Definitions

> **Making illegal states unrepresentable**: Designing types so that invalid combinations of data cannot be constructed at all, letting the type checker catch errors before the program runs.

> **Wrapper type**: A new type that wraps an existing type to give it a distinct meaning, e.g. `Inches` wrapping `Int`.

### Wrapper Types: The Mars Climate Orbiter

In 1999 NASA lost the **Mars Climate Orbiter** because of a units mix-up. One part of the codebase used inches and another used centimetres. Both were plain `Int`s, so nothing stopped the code from treating 2 inches + 4 cm as 6 inches.

```haskell
data Inches      = In Int
data Centimetres = Cm Int

instance Num Inches      where …
instance Num Centimetres where …
```

`(In 1) + (Cm 2)` is now a **type error**, because `(+) :: Num a => a -> a -> a` needs both operands to have the same type.

### Modelling Message State With Sum Types

A naive WhatsApp message:

```haskell
data WhatsappMessage = Msg {
  content   :: String,
  sender    :: String,
  read      :: Maybe Time,
  delivered :: Maybe Time,
  sent      :: Maybe Time
}
```

This allows a message with a read time but no sent time, which is meaningless. Moving the state into a sum type fixes it:

```haskell
data WhatsappMessage = Msg {
  content :: String,
  sender  :: String,
  state   :: MsgState
}

data MsgState = Draft
  | Sent      { sent :: Time }
  | Delivered { sent :: Time, delivered :: Time }
  | Read      { sent :: Time, delivered :: Time, read :: Time }
```

![Message states](../../../diagrams/CSC3003S-Advanced%20Programming/FP/13_Making_Illegal_States_Unrepresentable/message-states.svg)

*Each constructor carries exactly the timestamps valid in that state, so "read but never sent" cannot be constructed.*

| Design | Can represent "read but not sent"? |
|---|---|
| Three independent `Maybe Time` fields | Yes: $2^3=8$ combinations, most invalid |
| `MsgState` sum type | No: only the 4 valid states exist |

### Non-Empty Lists

```haskell
data NonEmptyList a = NonEmptyList a [a]   -- an obligatory first element
```

A `NonEmptyList` with no elements cannot be built, so `head` can never fail:

```haskell
head :: NonEmptyList a -> a
head (NonEmptyList x _) = x
```

The slide writes `data NonEmptyList = NonEmptyList a [a]`; the type parameter `a` must appear on the left as `NonEmptyList a`.

The lecture exercise: a type holding one or two values, never zero (unlike `(Maybe a, Maybe a)`):

```haskell
data AtLeastOne a = One a | Two a a
```

### Applications: Parse, Don't Validate

#### Definitions

> **Parse, don't validate**: Convert raw input once into a type that enforces the constraints, then work only with that type, rather than repeatedly checking raw data.

> **Shotgun parsing**: Scattering validation checks throughout a program instead of doing it once at the boundary.

1. **Validate once, at parse time.** Afterwards the constrained type guarantees validity, which prevents shotgun parsing.
2. **Eliminate classes of logic errors** before they happen: `Inches + Centimetres` is a type error.
3. **Move checks from run time to compile time**: with `NonEmptyList`, `head` can never crash at run time.

This also closes the `Just ""` loophole from [Advanced Typing And Functions](08_Advanced_Typing_And_Functions.md). Parse emails into an `Email` type that cannot hold an empty string.

### Don't Go Overboard

> [!warning] <span style="color:#ffc778">Don't let perfect be the enemy of good</span>
> Make illegal states unrepresentable as far as is reasonable, but overdoing it is also harmful. It can hurt interoperability: typeclasses implemented for `Int` may not exist for your custom `PrimeInt` type.

### Why Haskell Here

Haskell's type system is more expressive than most, so it can enforce far more constraints. For example, `MsgState` is awkward to define in Java. Sum types alone are a game changer.
