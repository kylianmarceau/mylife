---
tags:
  - advanced-programming
---

# Haskell 2 — Basic Types And Functions

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP 6 - Haskell 2 - Basic types & functions-1.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%206%20-%20Haskell%202%20-%20Basic%20types%20%26%20functions-1.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–25  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: types, lists, tuples, currying, guards, pattern matching, and algebraic data types.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is A Type?|What Is A Type?]]
  - [[#Type Inference And Typechecking|Type Inference And Typechecking]]
  - [[#Basic Types|Basic Types]]
  - [[#Lists And Cons|Lists And Cons]]
  - [[#Tuples|Tuples]]
  - [[#Function Types|Function Types]]
  - [[#Multiple Arguments And Currying|Multiple Arguments And Currying]]
  - [[#Conditionals And Guards|Conditionals And Guards]]
  - [[#Pattern Matching|Pattern Matching]]
  - [[#Algebraic Data Types|Algebraic Data Types]]
  - [[#Sum Types|Sum Types]]
  - [[#Product Types And Record Syntax|Product Types And Record Syntax]]

---

## Core Content

### What Is A Type?

#### Definitions

> **Type**: A name for a collection of related values. For example, `Bool` contains `True` and `False`.

A type restricts a **binding** (a variable, function argument, or return value) to certain kinds of values.

- `isEven :: Int -> Bool` accepts an `Int` and returns a `Bool`. It cannot accept `2.5` or `"dog"`.
- `Int` is "a fixed-precision integer type with at least the range $[-2^{29}, 2^{29}-1]$".
- `myDiv :: Int -> Int -> Float` takes two `Int`s and returns a `Float`.

### Type Inference And Typechecking

If evaluating expression $e$ would produce a value of type $T$, then $e$ has type $T$:

$$
e :: T
$$

Every well-formed expression has a type, which can often be **inferred** at compile time from context:

```haskell
x :: Int = 1
y = x   -- y is inferred to be Int
```

All type errors are found at **compile time**. That makes programs safer, by removing run-time type errors, and faster. This will not compile:

```haskell
addNumbers :: Int -> Int -> Int
addNumbers x y = x + y

addNumbers "Hello" 1   -- type error: String is not Int
```

In Python, a similar bug buried deep in a codebase could run fine for a long time and then fail in production. An example is `add_numbers(customerBalance, transaction)` where `transaction` is the transaction ID rather than the amount.

### Basic Types

| Type | Values |
|---|---|
| `()` | The **unit type**: "no value". Used for functions that do IO but return nothing, e.g. `print` |
| `Bool` | `True` or `False` |
| `Char` | A single character: one Unicode code point |
| `String` | A string of characters |
| `Int` | Fixed-size integers |
| `Integer` | Arbitrary-size integers (like BigInt) |
| `Float` / `Double` | Floating-point numbers |
| List | Values all of the same type |

Recap quiz answers: `map` applies a function to every element of a list. A **pure** function has no side effects: it purely computes its return value.

### Lists And Cons

#### Definitions

> **List**: An ordered sequence of values, all of the same type, with unrestricted length. A list of `Int` is written `[Int]`.

> **Cons (`:`)**: The operator that joins an element to the front of a list.

The element type is unrestricted (even lists or functions), but every element must have the same type.

| Expression | Type | Valid? |
|---|---|---|
| `[False, True, False]` | `[Bool]` | Yes |
| `[1, 2, 3, 4, 5]` | `[Int]` | Yes |
| `[1.0, 1.2, 1.4, 5.0]` | `[Float]` | Yes |
| `[[1], [1, 2], [1, 2, 3]]` | `[[Int]]` | Yes |
| `[]` | `[Int]` | Yes |
| `[1.0, False]` | — | No: mixed types |

Lists are like linked lists. A list is either the empty list `[]`, or an element consed onto the rest of the list:

```haskell
-- | means "or": a List is [] OR  a : List a
data List a = [] | a : List a

-- These are all equivalent:
[1, 2, 3, 4]
1:2:3:4:[]
1:(2:(3:(4:[])))
```

![A list as cons cells](../../../diagrams/CSC3003S-Advanced%20Programming/FP/06_Basic_Types_And_Functions/cons-list.svg)

*`[1,2,3,4]` is sugar for a chain of cons cells, each holding an element and a pointer to the rest, ending in `[]`.*

### Tuples

#### Definitions

> **Tuple**: A fixed-length, ordered sequence of values, possibly of different types, written `(Type1, Type2, …)`.

> **Pair**: A two-element tuple. `fst` and `snd` are defined on pairs.

Tuples group values without defining a new type, for example to return a name (`String`) and age (`Int`) from one function.

```haskell
(False, True, False) :: (Bool, Bool, Bool)
(False, 1, "Hello")  :: (Bool, Int, String)

(3, False) :: (Int, Bool)
fst (3, False) = 3
snd (3, False) = False
```

| | List | Tuple |
|---|---|---|
| Length | Variable | Fixed (part of the type) |
| Element types | Homogeneous | Possibly heterogeneous |

Quiz answers: a tuple is a *fixed-length collection of possibly heterogeneous types*. The list definition is `data List a = [] | a : List a`.

### Function Types

#### Definitions

> **Function**: A mapping from values of one type to values of another. The type of a function from $T_1$ to $T_2$ is written `T1 -> T2`.

```haskell
not  :: Bool -> Bool
even :: Int -> Bool
```

### Multiple Arguments And Currying

#### Definitions

> **Partial application**: Supplying a function with only some of its arguments, giving a function that waits for the rest.

> **Currying**: Treating a function of several arguments as a chain of one-argument functions, each returning the next function. Named after Haskell Curry.

```haskell
addVals :: Int -> Int -> Int
addVals a b = a + b
```

Why `Int -> Int -> Int` and not something like `Int, Int -> Int`? Consider doubling every element of a list:

```haskell
double :: Int -> Int
double x = x * 2
map double list

-- Or partially apply (*) :: Int -> Int -> Int
map (2 *) list
```

`(2 *)` gives `*` one argument, so it has type `Int -> Int` and waits for the second argument, which `map` supplies.

Under the hood, `addVals` is not a two-argument function. It takes an `Int` and **returns a function** `Int -> Int`:

```haskell
addVals :: Int -> (Int -> Int)
```

| Equivalent forms | |
|---|---|
| `addVals :: Int -> Int -> Int` | `addVals :: Int -> (Int -> Int)` |
| `addVals 1 2` | `((addVals 1) 2)` |

This works because `->` is **right-associative** and function application is **left-associative**.

![Currying addVals](../../../diagrams/CSC3003S-Advanced%20Programming/FP/06_Basic_Types_And_Functions/currying.svg)

*Applying `addVals` to `1` returns a function `Int -> Int`; applying that to `2` gives `3`.*

### Conditionals And Guards

#### Definitions

> **Guarded equations**: A function definition split into cases by Boolean guards (`|`), like a piecewise mathematical function or a switch/match statement.

```haskell
abs :: Int -> Int
abs n = if n >= 0 then n else -n

signum :: Int -> Int
signum n = if n < 0 then -1
           else if n == 0 then 0
           else 1
```

In Haskell `if` is an expression, so it always needs an `else`.

```haskell
f :: Float -> Float
f x | x < 0     = -1
    | x > 1     = 1
    | otherwise = x
```

$$
f(x)=\begin{cases}-1 & x<0\\ 1 & x>1\\ x & \text{otherwise}\end{cases}
$$

### Pattern Matching

#### Definitions

> **Pattern matching**: Defining a function by separate equations for different argument shapes or values, tried in definition order.

> **Partial function**: A function that is not defined for every input of its type.

```haskell
isPet :: String -> Bool
isPet "dog" = True
isPet "cat" = True
isPet var   = False   -- a variable (or _) matches any value
```

- Patterns are matched **in definition order**. `"dog"` would also match `isPet var`, but the earlier `isPet "dog" = True` wins.
- Each variable name in a pattern must be unique, except `_`.

Cons notation works in patterns. Wrap it in brackets because of operator precedence:

```haskell
head :: [Int] -> Int
head (x:_) = x

tail :: [Int] -> [Int]
tail (_:xs) = xs
```

Neither defines a case for `[]`, so GHC warns that they are **partial functions**. The course returns to this in later lectures.

### Algebraic Data Types

#### Definitions

> **Algebraic data type (ADT)**: A composite data type made up of other data types. ADTs include sum types and product types.

ADTs are similar to Python classes (without inheritance) or C/C++/Rust structs. They are "algebraic" because they are built with the operators **sum** and **product**, treating a type as a set of possible values.

![Sum versus product](../../../diagrams/CSC3003S-Advanced%20Programming/FP/06_Basic_Types_And_Functions/sum-product.svg)

*With $A=\{1,2\}$ and $B=\{foo,bar\}$, the sum has $2+2$ values (one of either set). The product has $2\times 2$ values (one from each set).*

### Sum Types

#### Definitions

> **Sum type**: A type whose values can be **one of** many alternatives. Its value set is the union of the alternatives: $A+B=\{1,2,foo,bar\}$.

```haskell
-- Values of Suit can only be Hearts, Clubs, Spades, or Diamonds
data Suit = Hearts | Clubs | Spades | Diamonds
x :: Suit = Hearts

-- Values of IntOrStr can be anything from Int or String
data IntOrStr = AnInteger Int | AString String
y :: IntOrStr = AnInteger 1
z :: IntOrStr = AString "Hello there"
```

`AnInteger` and `AString` are **constructors** that tag which alternative a value is.

### Product Types And Record Syntax

#### Definitions

> **Product type**: A type whose values contain **each of** several components. Its value set is the Cartesian product: $A\times B=\{(1,foo),(2,foo),(1,bar),(2,bar)\}$.

> **Record syntax**: Naming the fields of a product type, which also generates accessor functions.

```haskell
-- Unnamed members, extracted by pattern matching
data IntAndStr = IntAndStr Int String
x :: IntAndStr = IntAndStr 1 "hello there"
```

```haskell
data Address = Address
    { number :: Int
    , street :: String
    }            -- Haskell's indentation convention

addr = Address { number = 1, street = "a" }   -- record construction
addr = Address 1 "a"                          -- positional construction

number addr          -- field access: 1
addr { number = 2 }  -- a NEW Address with number changed (values are immutable)
```

The lecture exercise defines a `Person` type and filters adults:

```haskell
data Person = Person { name :: String, age :: Int }

isAdult :: Person -> Bool
isAdult p = age p >= 18                 -- Boolean expression
-- isAdult p | age p >= 18 = True       -- guards
--           | otherwise   = False
-- isAdult p = if age p >= 18 then True else False

adults :: [Person] -> [Person]
adults = filter isAdult

-- Recursive version with cons patterns
adultsRec :: [Person] -> [Person]
adultsRec [] = []
adultsRec (p:ps)
    | isAdult p = p : adultsRec ps
    | otherwise = adultsRec ps
```
