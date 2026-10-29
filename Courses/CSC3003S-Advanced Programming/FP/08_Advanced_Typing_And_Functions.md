---
tags:
  - advanced-programming
---

# Haskell 4 — Advanced Typing And Functions

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP 8 - Haskell 4 - advanced typing and functions-3.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%208%20-%20Haskell%204%20-%20advanced%20typing%20and%20functions-3.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–31  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: polymorphism, constraints, typeclasses, deriving `Show`, the `Maybe` type, kinds, and Hoogle.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Rationale For Polymorphism|Rationale For Polymorphism]]
  - [[#Declaring A Generic Function|Declaring A Generic Function]]
  - [[#Constraints And Overloaded Functions|Constraints And Overloaded Functions]]
  - [[#Typeclasses|Typeclasses]]
  - [[#Num As An Example Typeclass|Num As An Example Typeclass]]
  - [[#Implementing Show|Implementing Show]]
  - [[#Deriving Typeclasses|Deriving Typeclasses]]
  - [[#Generic Types: The Problem With Null|Generic Types: The Problem With Null]]
  - [[#The Maybe Type|The Maybe Type]]
  - [[#Type Constructors And Kinds|Type Constructors And Kinds]]
  - [[#Hoogle|Hoogle]]

---

## Core Content

### Rationale For Polymorphism

A function over concrete types works only on those types:

```haskell
add' :: Int -> Int -> Int
add' a b = a + b

add' 1 2      -- 3
add' 1.0 2.0  -- ERROR: this function takes only Ints
```

Floats can be added too, so how do we write one function that accepts both?

### Declaring A Generic Function

#### Definitions

> **Polymorphism**: "Having many forms" (poly = many, morph = form). A polymorphic (generic) function works over many types.

> **Type parameter (type variable)**: A placeholder such as `a` in a type signature, standing for any concrete type.

> **Unconstrained type variable**: A type variable with no constraint. It only forces all occurrences to be the same concrete type.

This is like Java generics such as `ArrayList<T>`. Make `add'` generic by adding a type parameter:

```haskell
add :: Int -> Int -> Int
-- becomes
add :: a -> a -> a
```

Read it as: "`add` has a type parameter `a`, takes two values of type `a`, and returns a value of type `a`."

```haskell
add' :: a -> a -> a
add' x y = x + y
```

```text
error: [GHC-39999]
    * No instance for `Num a' arising from a use of `+'
    * In the expression: x + y
```

The mistake: the signature promises `add'` accepts **any** type, but not every type supports `+`.

### Constraints And Overloaded Functions

#### Definitions

> **Constraint**: A restriction on a type variable, written before `=>`, requiring it to belong to a typeclass.

> **Overloaded function**: A function with one or more constraints on its type parameters.

```haskell
add' :: Num a => a -> a -> a   -- Num a is the constraint
add' x y = x + y

add' 1 2      -- 3
add' 1.0 2.4  -- 3.4
```

### Typeclasses

#### Definitions

> **Typeclass**: A named set of behaviours (functions) that a type can implement. It is like an interface in Java, and almost exactly like a trait in Rust. It is **not** an OOP class.

| Typeclass | OOP class |
|---|---|
| Specifies **behaviours** | Bundles **data and logic** |
| A type can implement as many as you wish | Often only single inheritance |
| The instance can be written with the typeclass **or** with the type, so it can be implemented for **foreign types** | Inheritance is declared at type definition; you cannot inherit "for" a foreign type |

### Num As An Example Typeclass

```haskell
class Num a where                  -- a: the type that will implement Num
    (+), (-), (*)  :: a -> a -> a   -- member functions that must be implemented
    negate         :: a -> a
    abs            :: a -> a
    signum         :: a -> a
    fromInteger    :: Integer -> a
    x - y          = x + negate y   -- member functions that are provided
    negate x       = 0 - x          --   (default implementations)
```

- The type parameter `a` names the implementing type so signatures can mention it.
- Signatures without bodies must be implemented by each instance.
- Definitions with bodies are **defaults** an instance gets for free. `-` and `negate` are defined in terms of each other, so an instance must define at least one of them.

### Implementing Show

#### Definitions

> **`Show`**: A typeclass from `base` that specifies how to convert a value to a `String` for printing. Its only required function is `show :: a -> String`.

> **Instance**: An implementation of a typeclass for a particular type, written `instance Class Type where …`.

`Show` is often implemented for your own types and is useful for debugging with `print :: Show a => a -> IO ()`, which is equivalent to `putStrLn . show`. By tacit contract, `show` output should itself be a valid Haskell expression: it is for debugging, not pretty-printing.

```haskell
-- It's legal to name the constructor something other than the type
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

Every new field (postcode, city, province, …) needs another hand-written line, which quickly becomes tedious.

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

### Generic Types: The Problem With Null

A social-media user profile has these rules:

- A user **must** have a name.
- A user **may** have an age.
- A user **may** have a parent's email (e.g. if under 18).

```sql
CREATE TABLE users (
    name        TEXT NOT NULL,
    age         INTEGER,
    parentEmail TEXT
);
```

Haskell has **no null values**: you cannot assign "null" or "None" to an `Int` or `String`. A tempting workaround is to use sentinel values, `0` for no age and `""` for no email:

```haskell
data User = User
    { name        :: String
    , age         :: Int
    , parentEmail :: String
    }

User "Cael" 24 ""
User "Thabo" 16 "mama.ka.thabo@example.com"
User "Haskell Curry" 0 ""      -- he is dead
```

Now spam every user:

```haskell
sendEmail :: String -> String -> IO ()
-- sends the 1st string to the email address given by the 2nd string

spamAll :: String -> [User] -> IO ()
-- mapM_ is like map for IO functions, discarding the () results
spamAll spam users = mapM_ (\user -> sendEmail spam $ email user) users
```

The slides call the email accessor `email`. With the record above it would be `parentEmail`.

Eventually this runs:

```haskell
(\user -> sendEmail spam $ email user) (User "Cael" 24 "")
= sendEmail "We miss you!" $ email (User "Cael" 24 "")
= sendEmail "We miss you!" ""     -- uh-oh! No email address!
```

This is fundamentally a **type error**: `sendEmail` expects a non-empty address, and the empty case was never handled. You could filter:

```haskell
mapM_ (\user -> sendEmail spam $ email user)
    $ filter (\user -> (email user) /= "") users
```

But you would need that filter everywhere the email is used. If "no email" is introduced late in development, every use must be tracked down. A type system exists to prevent exactly this kind of error. Tony Hoare, the inventor of null, called null references his "billion dollar mistake".

### The Maybe Type

#### Definitions

> **`Maybe a`**: A generic sum type representing an optional value: either `Nothing` or `Just` a value of type `a`.

```haskell
data Maybe a = Nothing | Just a
```

For a type, the type parameter `a` is written **before** the `=`. This differs from function syntax.

```haskell
data User = User
    { name        :: String
    , age         :: Maybe Int
    , parentEmail :: Maybe String
    }
```

The old `spamAll` now fails to compile, so GHC catches the bug before it happens:

```text
error: [GHC-83865]
    * Couldn't match expected type: [Char]
                  with actual type: Maybe String
    * In the second argument of `($)', namely `email user'
```

The fix uses `mapMaybe`:

```haskell
import Data.Maybe

spamAll :: String -> [User] -> IO ()
spamAll spam users = mapM_
    (\usrEmail -> sendEmail spam usrEmail)
    $ mapMaybe email users
```

> **`mapMaybe :: (a -> Maybe b) -> [a] -> [b]`**: A version of `map` that can throw out elements. If the function returns `Nothing`, nothing is added to the result; if it returns `Just b`, `b` is included.

![mapMaybe drops Nothing](../../../diagrams/CSC3003S-Advanced%20Programming/FP/08_Advanced_Typing_And_Functions/mapmaybe.svg)

*Users with no email give `Nothing` and are dropped. Only `Just` addresses reach `sendEmail`.*

> [!warning] <span style="color:#ffc778">Loophole</span>
> You can still build `Just ""`, a `Maybe String` holding an empty string. Ways to close this are covered in [Making Illegal States Unrepresentable](13_Making_Illegal_States_Unrepresentable.md).

The exercise solutions for `sum'` and `mapMaybe'`:

```haskell
sum' :: Num a => [a] -> a
sum' = foldl (+) 0

mapMaybe' :: (a -> Maybe b) -> [a] -> [b]
mapMaybe' _ [] = []
mapMaybe' f (x:xs) = case f x of
    Nothing -> mapMaybe' f xs
    Just y  -> y : mapMaybe' f xs
```

The exercise slide writes the type as `(a -> Maybe a) -> [a] -> [a]`. The general type above includes that case.

### Type Constructors And Kinds

#### Definitions

> **Type constructor**: A generic type such as `Maybe`, viewed as a function from types to types: it maps `Int` to `Maybe Int`.

> **Kind**: The "type of a type". `*` is a concrete type and `* -> *` maps a type to a type. Check it with `:kind` in ghci, the type-level analogue of `:type`.

```text
ghci> :kind Maybe
Maybe :: * -> *
ghci> :kind Maybe Int
Maybe Int :: *
ghci> :kind Int
Int :: *
```

![Maybe as a function on types](../../../diagrams/CSC3003S-Advanced%20Programming/FP/08_Advanced_Typing_And_Functions/type-constructor.svg)

*Just as `show` maps a value to a `String`, the type constructor `Maybe` maps the type `Int` to the type `Maybe Int`.*

### Hoogle

Haskell's type system is so expressive that Haskellers often search for functions by **type signature** rather than name, using Hoogle (`https://hoogle.haskell.org/`).

- Searching `Show a => a -> IO ()` finds `print`.
- An exercise: search for functions mapping `Integer` to `String`.
