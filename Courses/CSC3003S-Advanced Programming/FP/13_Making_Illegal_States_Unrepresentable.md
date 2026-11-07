---
tags:
  - advanced-programming
---

# Making Illegal States Unrepresentable

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP 13-Haskell 9-Making illegal states unrepresentable.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%2013-Haskell%209-Making%20illegal%20states%20unrepresentable.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–12
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> "Parse, don't validate": wrapper types for units, sum types for message states, a non-empty list, when to stop, and why Haskell's type system suits this.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Idea|The Idea]]
  - [[#Wrapper Types: The Mars Climate Orbiter|Wrapper Types: The Mars Climate Orbiter]]
  - [[#Modelling Message State With A Sum Type|Modelling Message State With A Sum Type]]
  - [[#A Non-Empty List|A Non-Empty List]]
  - [[#Don't Go Overboard|Don't Go Overboard]]
  - [[#Applications: Parse, Don't Validate|Applications: Parse, Don't Validate]]
  - [[#Why Haskell Suits This|Why Haskell Suits This]]

---

## Core Content

### The Idea

#### Definitions

> **Illegal state**: A combination of values a type allows but that makes no sense in the domain (e.g. a message read before it was sent).

> **Making illegal states unrepresentable**: Designing types so that such combinations cannot be constructed at all, so the compiler rejects them.

> **Wrapper type**: A new type that wraps an existing one (e.g. an `Int`) to give it a distinct meaning the type checker can enforce.

Goals of the lecture: know why we define types that wrap other types, and use the type system to catch errors **before** they happen.

### Wrapper Types: The Mars Climate Orbiter

In 1999 NASA lost the Mars Climate Orbiter because of a units mix-up: one part of the code used inches and another centimetres. Both were plain `Int`s, so nothing stopped the code from treating $2\text{ in} + 4\text{ cm}$ as $6\text{ in}$.

Wrapper types fix this:

```haskell
data Inches      = In Int
data Centimetres = Cm Int

instance Num Inches where ...
instance Num Centimetres where ...
```

Now `(In 1) + (Cm 2)` is a **type error**. The type of `+` requires both operands to be the same type:

```haskell
(+) :: Num a => a -> a -> a
```

### Modelling Message State With A Sum Type

A first attempt at modelling WhatsApp messages:

```haskell
data WhatsappMessage = Msg {
  content   :: String,
  sender    :: String,
  read      :: Maybe Time,
  delivered :: Maybe Time,
  sent      :: Maybe Time
}
```

This allows nonsense, such as a message with a `read` time but no `sent` time. What would that even mean?

Replace the independent `Maybe` fields with a sum type of the legal states:

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

![Message states as a sum type](../../../diagrams/CSC3003S-Advanced%20Programming/FP/13_Making_Illegal_States_Unrepresentable/message-states.svg)

*Each state carries exactly the timestamps that must exist by then; later states include all earlier ones.*

Can you now build a message with a read time but no send time? **No** — the only constructor with a `read` field also requires `sent` and `delivered`.

| Design | Read-but-never-sent message |
|---|---|
| Three `Maybe Time` fields | Representable — a bug waiting to happen |
| `MsgState` sum type | Unrepresentable — won't compile |

### A Non-Empty List

```haskell
data NonEmptyList a = NonEmptyList a [a]
```

This is just a list with an obligatory first element. It is impossible to construct a `NonEmptyList` with no elements.

So `head` becomes **total** — it can never crash:

```haskell
head :: NonEmptyList a -> a
head (NonEmptyList x _) = x
```

Compare the ordinary `head :: [a] -> a`, which is partial and crashes on `[]` (see [Basic Types And Functions](06_Basic_Types_And_Functions.md#Pattern%20Matching)).

The same trick handles "one or two values, never zero" (a lecture exercise), which `(Maybe a, Maybe a)` gets wrong because it allows `(Nothing, Nothing)`:

```haskell
data AtLeastOne a = One a | Two a a
```

### Don't Go Overboard

Don't let perfect be the enemy of good. Go as far as is useful in making illegal states unrepresentable, but going overboard can also hurt.

- It can harm **interoperability**: typeclasses implemented for `Int` may not be implemented for your custom `PrimeInt` type.

[AR: "Fast and Loose Reasoning is Morally Correct", Danielsson et al.]

### Applications: Parse, Don't Validate

#### Definitions

> **Parse, don't validate**: Convert raw input once, at the boundary, into a type that enforces the constraints; afterwards, work only with the constrained type.

> **Shotgun parsing**: Scattering validation checks throughout the code, mixed in with processing logic.

| Benefit | Example |
|---|---|
| **Validate once**, at parse time, then rely on the type — prevents shotgun parsing | Parse input into `NonEmptyList` once; later code never checks for emptiness |
| **Eliminate whole classes of logic errors** before they happen | `Inches + Centimetres` is now a type error |
| **Move checks from run time to compile time** | With `NonEmptyList`, `head` can never crash at run time |

This also closes the loophole left in [Advanced Typing And Functions](08_Advanced_Typing_And_Functions.md#The%20Maybe%20Type), where `Just ""` was still a possible "email".

### Why Haskell Suits This

Haskell's type system is more expressive than most, letting you enforce far more constraints. For example, `MsgState` is awkward to define in Java. Sum types alone are a game changer.

Reading: "Parse, don't validate" (Alexis King, lexi-lambda.github.io) and "Make illegal states unrepresentable" (functional-architecture.org).
