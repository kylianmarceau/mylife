---
tags:
  - advanced-programming
---

# Advanced Typing And Functions

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP 8 - Haskell 4 - advanced typing and functions-3.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%208%20-%20Haskell%204%20-%20advanced%20typing%20and%20functions-3.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–31
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Polymorphism and generic functions, type constraints and typeclasses, implementing and deriving `Show`, generic data types and `Maybe` instead of null, type constructors as functions on types, and Hoogle.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Why Polymorphism?|Why Polymorphism?]]
  - [[#Declaring A Generic Function|Declaring A Generic Function]]
  - [[#Type Constraints And Overloaded Functions|Type Constraints And Overloaded Functions]]
  - [[#Typeclasses|Typeclasses]]
  - [[#The Num Typeclass|The Num Typeclass]]
  - [[#Implementing Show|Implementing Show]]
  - [[#Deriving Typeclasses|Deriving Typeclasses]]
  - [[#The Problem With Null-Like Values|The Problem With Null-Like Values]]
  - [[#The Maybe Type|The Maybe Type]]
  - [[#Type Constructors Are Functions On Types|Type Constructors Are Functions On Types]]
  - [[#Hoogle|Hoogle]]

---

## Core Content

### Why Polymorphism?

So far, functions have taken and returned **concrete types**. `add' :: Int -> Int -> Int` works only on `Int`s — not even on `Float`s:

```haskell
add' :: Int -> Int -> Int
add' a b = a + b

add' 1 2      -- 3
add' 1.0 2.0  -- ERROR: this function only takes Ints
```

Floats can be added perfectly well, so how do we write one function that accepts both?

#### Definitions

> **Polymorphism**: "Having many forms" (poly = many, morph = form). A polymorphic function or type works for many types.

> **Generic function**: A function that is parameterised over a type, like Java's `ArrayList<T>`, which is generic over type `T`.

### Declaring A Generic Function

Add a **type parameter** (type variable) to the signature:

```haskell
add :: Int -> Int -> Int
-- becomes
add :: a -> a -> a
```

Read it as: "`add` is a function with a type parameter `a` that takes two values of type `a` and returns a value of type `a`."

Writing the body fails:

```haskell
add' :: a -> a -> a
add' x y = x + y
```

```text
error: [GHC-39999]
  * No instance for `Num a' arising from a use of `+'
  * In the expression: x + y
```

The signature claims `add'` accepts **any** type, but not every type can be added with `+`.

### Type Constraints And Overloaded Functions

#### Definitions

> **Unconstrained type variable**: A type variable such as `a` in `a -> a -> a` that only enforces that all uses are the same concrete type; it says nothing about what operations that type supports.

> **Type constraint**: A restriction such as `Num a =>` limiting a type variable to types that belong to a typeclass.

> **Overloaded function**: A function with one or more constraints on its type parameters.

Restrict `a` to numbers:

```haskell
add' :: Num a => a -> a -> a   -- "Num a =>" is the constraint
add' x y = x + y

add' 1 2      -- 3
add' 1.0 2.4  -- 3.4
```

[AR: "Ad-hoc Polymorphism" on HaskellWiki]

The lecture exercise — a generic `sum` — uses the same idea:

```haskell
sum' :: Num a => [a] -> a
sum' xs = foldl (+) 0 xs
```

### Typeclasses

#### Definitions

> **Typeclass**: A named set of behaviours (functions) that a type can implement. It is not a Java/Python class; it is more like an **interface**, and almost exactly a Rust **trait**.

`Num` in `Num a =>` is a typeclass.

| Typeclass | OOP class |
|---|---|
| Specifies **behaviours** | Bundles data **and** logic |
| A type can implement as many as you like | Often you can inherit from only one |
| The instance can be defined with the typeclass **or** with the type, so you can implement it for foreign types | Inheritance is fixed at the type's definition; you can't inherit "for" a foreign type |

[AR: haskell.org tutorial, "Type Classes and Overloading"]

### The Num Typeclass

```haskell
class Num a where              -- a: the type that will implement Num
    (+), (-), (*)  :: a -> a -> a
    negate         :: a -> a
    abs            :: a -> a
    signum         :: a -> a
    fromInteger    :: Integer -> a
    x - y          = x + negate y   -- provided (default) definitions
    negate x       = 0 - x
```

| Part | Role |
|---|---|
| `class Num a where` | Declares the typeclass; `a` stands for the implementing type, so the signatures can mention it |
| Signatures (`(+)`, `negate`, …) | Member functions an instance must implement |
| Equations (`x - y = …`, `negate x = …`) | Member functions provided by default in terms of others |

### Implementing Show

One advantage of typeclasses is implementing them for **foreign types**: a typeclass defined in one package (e.g. `base`, the standard library) can be implemented in another.

`Show` (from `base`) is a common example. It specifies how to convert a type to a `String`, which is useful for debugging with `print :: Show a => a -> IO ()` (equivalent to `putStrLn . show`).

`Show` requires one function, `show :: a -> String`. There is a tacit contract that the output is itself a valid Haskell expression, so `show` is for debugging, not pretty-printing.

```haskell
-- The constructor may be named differently from the type
data StreetAddress = Addr {
    number :: Int,
    street :: String
}

instance Show StreetAddress where
    show addr =
        "Addr { number = " ++ (show $ number addr)
        ++ ", street = " ++ (show $ street addr)
        ++ "}"

x = Addr { number = 1, street = "Main Rd" }
show x   -- Addr { number = 1, street = "Main Rd" }
```

Adding more fields (`postcode`, `city`, `province`, …) makes the hand-written instance grow line by line — tedious, fast.

### Deriving Typeclasses

#### Definitions

> **Deriving**: Asking the compiler to generate a typeclass instance automatically with `deriving`.

```haskell
data StreetAddress = Addr
  { number   :: Int
  , street   :: String
  , postcode :: Int
  , province :: String
  , city     :: String
  , country  :: String
  } deriving Show

show $ Addr 1 "Main Rd" 7700 "Western Cape" "Cape Town" "South Africa"
-- "Addr {number = 1, street = \"Main Rd\", postcode = 7700,
--  province = \"Western Cape\", city = \"Cape Town\", country = \"South Africa\"}"
```

Deriving `Show` also works for generic types, e.g. `data Pair a = Pair a a deriving Show`.

### The Problem With Null-Like Values

Generic **data types** are useful too. Example: a social-media user profile where

- a user must always have a name,
- a user may have an age,
- a user may have a parent's email (e.g. for under-18s).

In SQL:

```sql
CREATE TABLE users (
    name        TEXT NOT NULL,
    age         INTEGER,
    parentEmail TEXT
);
```

**Haskell has no null values.** You can't assign "null" or "None" to an `Int` or `String`. [AR: "Null References: The Billion Dollar Mistake", Tony Hoare, the inventor of null]

A tempting workaround uses 0 for "no age" and `""` for "no email":

```haskell
data User = User
    { name        :: String
    , age         :: Int
    , parentEmail :: String
    }

users = [ User "Cael" 24 ""
        , User "Thabo" 16 "mama.ka.thabo@example.com"
        , User "Haskell Curry" 0 ""   -- he is dead
        ]
```

Now spam every user:

```haskell
sendEmail :: String -> String -> IO ()
-- sends the 1st string to the email address in the 2nd string

spamAll :: String -> [User] -> IO ()
-- mapM_ is like map for IO functions, discarding the () results
spamAll spam users = mapM_ (\user -> sendEmail spam $ email user) users

spamAll "We miss you!" users
```

Eventually this evaluates:

```haskell
(\user -> sendEmail spam $ email user) (User "Cael" 24 "")
= sendEmail "We miss you!" $ email (User "Cael" 24 "")
= sendEmail "We miss you!" ""   -- uh-oh! No email address!
```

This is fundamentally a **type error**: `sendEmail` expected a non-empty string, and we forgot to handle the empty case. Filtering fixes this one call site:

```haskell
mapM_ (\user -> sendEmail spam $ email user)
    $ filter (\user -> (email user) /= "") users
```

But you would need that filter everywhere the email is used — and if empty emails are introduced late in development, how do you find every place? A type system exists precisely to prevent this kind of error.

### The Maybe Type

#### Definitions

> **`Maybe a`**: A generic sum type representing an optional value: either `Nothing` or `Just` a value of type `a`.

```haskell
data Maybe a = Nothing | Just a
```

The type parameter `a` goes before the `=`; this is different syntax from functions.

```haskell
data User = User
    { name        :: String
    , age         :: Maybe Int
    , parentEmail :: Maybe String
    }
```

Now the buggy `spamAll` doesn't compile:

```text
error: [GHC-83865]
  * Couldn't match expected type: [Char]
                with actual type: Maybe String
  * In the second argument of `($)', namely `email user'
```

GHC catches the bug before it can happen. The fix uses `mapMaybe` from `Data.Maybe`, which applies a function returning `Maybe` and keeps only the `Just` results:

```haskell
import Data.Maybe

spamAll :: String -> [User] -> IO ()
spamAll spam users = mapM_
    (\usrEmail -> sendEmail spam usrEmail)
    $ mapMaybe email users
```

![mapMaybe](../../../diagrams/CSC3003S-Advanced%20Programming/FP/08_Advanced_Typing_And_Functions/mapmaybe.svg)

*`mapMaybe` unwraps every `Just` value and drops every `Nothing`.*

The lecture exercise re-implements it:

```haskell
mapMaybe' :: (a -> Maybe b) -> [a] -> [b]
mapMaybe' _ [] = []
mapMaybe' f (x:xs) = case f x of
    Nothing -> mapMaybe' f xs
    Just y  -> y : mapMaybe' f xs
```

A loophole remains: you can still construct `Just ""`. Closing it is covered in [Making Illegal States Unrepresentable](13_Making_Illegal_States_Unrepresentable.md). [AR: "Make illegal states unrepresentable"] [AR: "Parse, don't validate", Alexis King]

### Type Constructors Are Functions On Types

#### Definitions

> **Type constructor**: A generic type such as `Maybe`, seen as a function that maps a type to another type: `Maybe` maps `Int` to `Maybe Int`.

> **Kind**: The "type of a type". `*` means a concrete type, so `* -> *` means "maps a type to a type".

Functions map between values: `show :: Show a => a -> String` maps a `Show` instance to a string. Generic types map between **types**.

In GHCi, `:kind` shows a type's kind, just as `:type` shows a value's type:

```text
ghci> :kind Int
Int :: *
ghci> :kind Maybe
Maybe :: * -> *
ghci> :kind Maybe Int
Maybe Int :: *
```

![Type constructors as functions on types](../../../diagrams/CSC3003S-Advanced%20Programming/FP/08_Advanced_Typing_And_Functions/type-constructor.svg)

*`Maybe` takes the concrete type `Int` and produces the concrete type `Maybe Int`.*

[AR: "Type constructor" on HaskellWiki] [AR: "Kinds and Higher-Kinded Types in Haskell", Gints Dreimanis]

### Hoogle

Haskell's type system is expressive enough that Haskellers often search for functions by **type signature** rather than by name, using **Hoogle** (hoogle.haskell.org). For example, searching `Integer -> String` finds `show` and related functions.

Assigned reading (LYAH): *Types and Typeclasses*, *Syntax in Functions*, *Making Our Own Types and Typeclasses*; in preparation: "Foldl and foldr" (Alexis King) and the Stack Overflow question "Why does foldl seem to be harmful despite being tail recursive?".
