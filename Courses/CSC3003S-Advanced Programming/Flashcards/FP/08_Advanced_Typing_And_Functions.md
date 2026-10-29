---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 08 — Haskell 4 — Advanced Typing And Functions"
---

# FP 08 — Haskell 4 — Advanced Typing And Functions

**Source note:** [Haskell 4 — Advanced Typing And Functions](../../FP/08_Advanced_Typing_And_Functions.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Polymorphism And Typeclasses|Polymorphism And Typeclasses]]
  - [[#Optional Values|Optional Values]]
  - [[#Type Constructors|Type Constructors]]
  - [[#Num As An Example Typeclass|Num As An Example Typeclass]]
  - [[#Implementing Show|Implementing Show]]
  - [[#The Maybe Type|The Maybe Type]]
  - [[#Hoogle|Hoogle]]
  - [[#Polymorphism And Constraints|Polymorphism And Constraints]]
  - [[#Optional Data And Kinds|Optional Data And Kinds]]

## Core Content

### Polymorphism And Typeclasses

<!-- qard-id: ap-cf6315e777a1d79fcc73 -->
> [!qard]- What does a repeated type variable require in `a -> a -> a`?
> Both arguments and the result have the same chosen type. Without constraints, the implementation must work uniformly for any type `a`.

<!-- qard-id: ap-e8381f542f35638b3ac6 -->
> [!qard]- Why does `add x y = x + y` need `Num a => a -> a -> a`?
> `(+)` requires numeric operations. The `Num a` constraint limits `a` to types implementing them.

<!-- qard-id: ap-db2f670b092eefbf13ea -->
> [!qard]- What is a typeclass, and what is an instance?
> A typeclass specifies supported operations; an instance implements them for a particular type. It describes behaviour rather than an OOP object's stored fields.

<!-- qard-id: ap-c86cd45e9fff8ec34fd7 -->
> [!qard]- What does `Show a => a -> String` express?
> The function accepts values of a type implementing `Show` and returns a string; `show` is the standard example.

<!-- qard-id: ap-fc140d014d6c88854667 -->
> [!qard]- What does `deriving Show` request?
> Compiler generation of a `Show` instance for the declared data type, when its fields support the required instances.

### Optional Values

<!-- qard-id: ap-926ce211ae957c386323 -->
> [!qard]- How does `Maybe a` represent optional data?
> `data Maybe a = Nothing | Just a`: absence is explicit and distinct from a present value.

<!-- qard-id: ap-bdd2a284551c1c5c0b9e -->
> [!qard]- Why is `Maybe Int` safer than using `0` for a missing age?
> The type separates missing data from a legitimate value, so consuming code must account for absence rather than silently treating it as an age.

<!-- qard-id: ap-4a886e388b6e5968b478 -->
> [!qard]- What does `mapMaybe :: (a -> Maybe b) -> [a] -> [b]` do?
> Apply the function, discard `Nothing` results and unwrap the `Just` results, preserving order.

<!-- qard-id: ap-11d9f02374d4a30863a8 -->
> [!qard]- Does `Maybe String` guarantee a nonempty valid email?
> No. `Just ""` is still allowed; a separately validated email type is needed to enforce that constraint.

### Type Constructors

<!-- qard-id: ap-dd445f87b851dbaab1b8 -->
> [!qard]- How do `Maybe` and `Maybe Int` differ?
> `Maybe` needs a type argument and has kind `* -> *`; `Maybe Int` is a fully applied type with kind `*`.

<!-- qard-id: ap-2a7359666204a76790d2 -->
> [!qard]- How do `:type` and `:kind` differ in GHCi?
> `:type` asks for an expression's type; `:kind` asks for a type expression's kind.

### Num As An Example Typeclass

<!-- qard-id: ap-374a3781d42768e92a32 -->
> [!qard]- How can mutually defined typeclass defaults fail if neither primitive is implemented?
> In `Num`, subtraction and `negate` may be defined via each other; an instance needs at least one concrete implementation to avoid infinite recursion, alongside the other required numeric operations.

### Implementing Show

<!-- qard-id: ap-a85b21a93bd601d68cb8 -->
> [!qard]- How does a custom `Show` instance differ from `deriving Show`?
> A hand-written `instance Show T where show ... = ...` chooses the representation explicitly. Deriving generates the ordinary constructor/field representation automatically; `print` uses `show` then outputs the text.

### The Maybe Type

<!-- qard-id: ap-9fee52d877989c7f1fa9 -->
> [!qard]- How can `mapMaybe` be implemented recursively?
> On `[]`, return `[]`. For `(x:xs)`, evaluate `f x`: discard `Nothing`, or cons the payload of `Just y` onto `mapMaybe f xs`.

### Hoogle

<!-- qard-id: ap-d15fe4dd393a66d9e990 -->
> [!qard]- Why search Hoogle using a type signature?
> A desired mapping often specifies the operation more precisely than a guessed name; searching a type such as `Show a => a -> IO ()` can locate `print`.

### Polymorphism And Constraints

<!-- qard-id: ap-617701a2f854e41d428c -->
> [!qard]- How does parametric polymorphism differ from typeclass overloading?
> An unconstrained parameter supports uniform code without assuming type-specific operations; a class constraint permits the operations implemented by that type's instance.

<!-- qard-id: ap-21b885c6a3675b2e8cb9 -->
> [!qard]- Why can `a -> a -> a` not by itself promise addition?
> It promises to work for every `a`, including types with no numeric operation. `(+)` requires an additional `Num a` capability.

<!-- qard-id: ap-f052d42f0acc03987041 -->
> [!qard]- What does a constraint before `=>` contribute to the rest of a signature?
> It lists assumptions the implementation may use, such as `Eq a` for equality or `Num a` for numeric operations.

<!-- qard-id: ap-ba0da4b4bd832dc69408 -->
> [!qard]- Can one type implement more than one typeclass?
> Yes. A type may support behaviours such as `Show`, `Eq` and `Ord` independently when suitable instances are provided.

<!-- qard-id: ap-d031a3b46edaf79720b5 -->
> [!qard]- Why is a typeclass not an OO object holding fields?
> It specifies a family of operations for implementing types rather than defining each object's stored state and identity.

<!-- qard-id: ap-164692bce67b3805b983 -->
> [!qard]- What is a default method in a typeclass?
> An implementation supplied by the class that an instance may inherit or override; mutually recursive defaults still need enough concrete operations to terminate.

<!-- qard-id: ap-7b187af6be89bf8ffdbd -->
> [!qard]- Why can an instance be useful for a type defined elsewhere?
> It supplies a supported behaviour without changing the type's original data declaration, subject to the language's instance rules.

### Optional Data And Kinds

<!-- qard-id: ap-e43b33cfd60021344015 -->
> [!qard]- Why does changing an email field from `String` to `Maybe String` reveal unsafe callers?
> Code expecting a bare string no longer typechecks until it explicitly accounts for the absent/present alternatives.

<!-- qard-id: ap-af7ee3ee2407bb54de06 -->
> [!qard]- How does `mapMaybe` differ from applying `map` to an optional-producing function?
> `map` gives one `Maybe b` per input, including Nothings; `mapMaybe` drops absence and extracts present payloads into `[b]`.

<!-- qard-id: ap-156332cd88b832a965db -->
> [!qard]- Why is `Just ""` different from `Nothing`?
> The former is a present empty string; the latter is absence. Optionality does not enforce the payload's semantic validity.

<!-- qard-id: ap-fc6cee7573fa7c6a400f -->
> [!qard]- Why must `data Maybe a = ...` put `a` on the left of the definition?
> The data type is parameterised by `a`; its constructors use that same parameter when specifying payloads.

<!-- qard-id: ap-f8a58af7f55db907f0a7 -->
> [!qard]- What does kind `* -> *` describe compared with kind `*`?
> A type constructor still needing one ordinary type argument versus a fully applied ordinary type. For example `Maybe` versus `Maybe Int`.

<!-- qard-id: ap-5f08e96acafb03c2bf96 -->
> [!qard]- What constraints can prevent a derived `Show` instance?
> The generated representation must be able to show the fields it includes; required field instances must be available. Automatic derivation is not a universal pretty-printer.

<!-- qard-id: ap-f641214d66cec88c0c06 -->
> [!qard]- What is the type-level analogy between applying `Maybe` and applying a function?
> `Maybe` maps a type such as `Int` to `Maybe Int`; an ordinary function maps values. Kinds classify the former application's inputs/outputs, types classify the latter.
