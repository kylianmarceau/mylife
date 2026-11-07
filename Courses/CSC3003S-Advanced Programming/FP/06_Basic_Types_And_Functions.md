---
tags:
  - advanced-programming
---

# Basic Types And Functions

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP 6 - Haskell 2 - Basic types & functions-1.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%206%20-%20Haskell%202%20-%20Basic%20types%20%26%20functions-1.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–25
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Types and type checking, Haskell's basic types, lists and cons, tuples, function types and currying, conditionals, guards and pattern matching, and algebraic data types (sum and product types, record syntax).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is A Type?|What Is A Type?]]
  - [[#Type Inference And Type Checking|Type Inference And Type Checking]]
  - [[#Basic Types|Basic Types]]
  - [[#Lists|Lists]]
  - [[#Lists As Cons Cells|Lists As Cons Cells]]
  - [[#Tuples|Tuples]]
  - [[#Function Types|Function Types]]
  - [[#Currying And Partial Application|Currying And Partial Application]]
  - [[#Conditionals And Guards|Conditionals And Guards]]
  - [[#Pattern Matching|Pattern Matching]]
  - [[#Algebraic Data Types|Algebraic Data Types]]
  - [[#Sum Types|Sum Types]]
  - [[#Product Types And Record Syntax|Product Types And Record Syntax]]
  - [[#Worked Exercise: A Person Type|Worked Exercise: A Person Type]]

---

## Core Content

### What Is A Type?

#### Definitions

> **Type**: A name for a collection of related values. For example, the basic type `Bool` contains the values `True` and `False`.

A type restricts a binding (a variable, function argument or return value) to contain only certain kinds of things.

- `isEven :: Int -> Bool` accepts an `Int` and returns a `Bool`.
- `Int` is "a fixed-precision integer type with at least the range $[-2^{29} .. 2^{29}-1]$".
- So `isEven` cannot accept `2.5` (not an integer) or `"dog"` (not a number).
- `myDiv :: Int -> Int -> Float` takes two `Int`s and returns a `Float` — the type alone tells you a lot about the function.

### Type Inference And Type Checking

If evaluating an expression `e` would produce a value of type `T`, then `e` has type `T`, written `e :: T`.

- Every well-formed expression has a type.
- The type can often be **inferred** at compile time from context.

```haskell
x :: Int = 1
y = x   -- y is inferred to have type Int
```

All type errors are found at **compile time**. This makes programs safer and faster by removing run-time type errors. This does not compile:

```haskell
addNumbers :: Int -> Int -> Int
addNumbers x y = x + y

addNumbers "Hello" 1   -- type error: "Hello" is not an Int
```

In a dynamically typed Python codebase, a call like `add_numbers(customerBalance, transaction)` — where `transaction` is accidentally the transaction **ID**, not the amount — could run fine for a while and then blow up when that code path finally executes.

### Basic Types

| Type | Values |
|---|---|
| `()` | The **unit** type: "no value". Useful for functions that do IO but return nothing, e.g. `print` |
| `Bool` | `True` or `False` |
| `Char` | A single character — one Unicode code point |
| `String` | A string of characters |
| `Int` | Fixed-size integers |
| `Integer` | Arbitrary-size integers (like BigNum / BigInt) |
| `Float` / `Double` | Floating-point numbers |
| List | A list of values of the same type |

[AR: "Let's stop ascribing meaning to code-points", Manish Goregaokar] [AR: "Text Rendering Hates You", @Gankra]

Recap: `map` applies a function to every element of a list, mapping each element to a new value. A **pure** function has no side effects — it purely computes its return value.

### Lists

#### Definitions

> **List**: An ordered sequence of values, all of the same type, of unrestricted length (like Python's `list` or Java's `ArrayList`). A list of `Int` has type `[Int]`.

The element type is unrestricted — lists of lists or of functions are fine — but every element must have the same type.

| Expression | Valid? |
|---|---|
| `[False, True, False] :: [Bool]` | ✅ |
| `[1, 2, 3, 4, 5] :: [Int]` | ✅ |
| `[1.0, 1.2, 1.4, 5.0] :: [Float]` | ✅ |
| `[[1], [1, 2], [1, 2, 3]] :: [[Int]]` | ✅ |
| `[] :: [Int]` | ✅ |
| `[1.0, False]` | ❌ — elements must all be the same type |

### Lists As Cons Cells

#### Definitions

> **Cons (`:`)**: The operator that joins an element to the front of a list.

Lists are represented like linked lists. A list is either:

1. the empty list `[]`, **or**
2. an element joined, by cons, to the rest of the list.

```haskell
-- | means "or": a List is either [] or (a : List a)
data List a = [] | a : List a

-- These are all equivalent
[1, 2, 3, 4]
1:2:3:4:[]
1:(2:(3:(4:[])))
```

![Cons list](../../../diagrams/CSC3003S-Advanced%20Programming/FP/06_Basic_Types_And_Functions/cons-list.svg)

*`[1,2,3,4]` is a chain of cons cells, each holding an element and a pointer to the rest, ending in `[]`.*

### Tuples

#### Definitions

> **Tuple**: A fixed-length, ordered sequence of values of possibly different types, written `(Type1, Type2, …)`.

> **Pair**: A two-element tuple. `fst` and `snd` return its first and second elements.

Tuples group values without defining a new type, e.g. to return a person's name (`String`) and age (`Int`) from one function.

```haskell
(False, True, False) :: (Bool, Bool, Bool)
(False, 1, "Hello")  :: (Bool, Int, String)

(3, False) :: (Int, Bool)
fst (3, False) = 3
snd (3, False) = False
```

| | List | Tuple |
|---|---|---|
| Length | Variable | Fixed |
| Element types | All the same (homogeneous) | Possibly different (heterogeneous) |

### Function Types

A function maps values of one type to another. The type of a function from `T1` to `T2` is written `T1 -> T2`.

```haskell
not  :: Bool -> Bool
even :: Int -> Bool
```

Functions can take multiple arguments:

```haskell
addVals :: Int -> Int -> Int
addVals a b = a + b
```

Why `Int -> Int -> Int` and not something like `Int, Int -> Int`? Currying explains it.

### Currying And Partial Application

#### Definitions

> **Partial application**: Calling a function with fewer arguments than it takes, giving a new function that waits for the rest.

> **Currying**: Treating a function of several arguments as a chain of one-argument functions, each returning the next. Named after the mathematician Haskell Curry.

**Rationale**: to double every element of a list, you could define `double` and map it:

```haskell
double :: Int -> Int
double x = x * 2

map double list
```

Or you could partially apply `(*) :: Int -> Int -> Int`:

```haskell
map (2 *) list
```

`(2 *)` gives `*` one of its two arguments. The result has type `Int -> Int` and waits for the second argument, which `map` supplies.

The real reason `addVals` has type `Int -> Int -> Int` is that, under the hood, it is **not** a two-argument function. It takes an `Int` and returns a function from `Int` to `Int`:

```haskell
addVals :: Int -> (Int -> Int)
```

These are equivalent:

| Curried shorthand | Explicit form |
|---|---|
| `addVals :: Int -> Int -> Int` | `addVals :: Int -> (Int -> Int)` |
| `addVals 1 2` | `((addVals 1) 2)` |

This works because:

- the `->` arrow is **right-associative**, and
- function application is **left-associative**.

![Currying addVals](../../../diagrams/CSC3003S-Advanced%20Programming/FP/06_Basic_Types_And_Functions/currying.svg)

*`addVals 1` returns a new function `Int -> Int`, which is then applied to 2.*

### Conditionals And Guards

#### Definitions

> **Guarded equation**: A definition with several conditions (guards, after `|`), each with its own result, like a piecewise function in maths or a switch/match statement. `otherwise` catches every remaining case.

`if`/`else` works as in other languages (the `else` is required):

```haskell
abs :: Int -> Int
abs n = if n >= 0 then n else -n

signum :: Int -> Int
signum n = if n < 0 then -1
           else if n == 0 then 0
           else 1
```

Guards express the same choices more cleanly:

```haskell
f :: Float -> Float
f x | x < 0     = -1
    | x > 1     = 1
    | otherwise = x
```

### Pattern Matching

#### Definitions

> **Pattern matching**: Defining a function by several equations, each matching a particular shape or value of the arguments.

> **Partial function**: A function not defined for every input of its type.

```haskell
isPet :: String -> Bool
isPet "dog" = True
isPet "cat" = True
-- a variable name (or _ if the value isn't used) matches any value
-- with several arguments, each name must be unique (except _)
isPet var = False
```

Patterns are tried **in definition order**. `"dog"` would also match `isPet var = False`, but the earlier equation `isPet "dog" = True` takes precedence, so the function returns `True`.

**Pattern matching on lists** uses cons notation (wrapped in brackets because of operator precedence):

```haskell
head :: [Int] -> Int
head (x:_) = x

tail :: [Int] -> [Int]
tail (_:xs) = xs
```

- `head` returns the first element; `tail` returns everything except it.
- Neither defines a case for the empty list `[]`, so GHC warns that they are **partial functions**. This comes back later (see [Advanced Typing And Functions](08_Advanced_Typing_And_Functions.md)).

### Algebraic Data Types

#### Definitions

> **Algebraic data type (ADT)**: A data type made up of other data types — a composite data type. ADTs include sum types and product types.

ADTs are similar to Python classes (without inheritance) or C/C++/Rust structs. This course covers defining your own ADTs and making them polymorphic.

They are called *algebraic* because they are built with an algebra of two operators, **sum** and **product**. Think of a type as a set of possible values.

![Sum versus product types](../../../diagrams/CSC3003S-Advanced%20Programming/FP/06_Basic_Types_And_Functions/sum-product.svg)

*A sum type's values come from one of its alternatives; a product type's values combine one value from each component.*

| | Sum type | Product type |
|---|---|---|
| A value is | **One of** several things | **Each of** several things together |
| Set view, $A = \{1,2\}$, $B = \{\text{foo},\text{bar}\}$ | $A + B = \{1, 2, \text{foo}, \text{bar}\}$ | $A \times B = \{(1,\text{foo}), (2,\text{foo}), (1,\text{bar}), (2,\text{bar})\}$ |
| Number of values | $\lvert A\rvert + \lvert B\rvert$ | $\lvert A\rvert \times \lvert B\rvert$ |
| Analogy | Enum / tagged union | Struct / record |

### Sum Types

```haskell
-- Values of Suit can only be hearts, clubs, spades or diamonds
data Suit = Hearts | Clubs | Spades | Diamonds
x :: Suit = Hearts            -- instantiating a value of Suit

-- Values of IntOrStr can be anything from Int or from String
data IntOrStr = AnInteger Int | AString String
y :: IntOrStr = AnInteger 1
z :: IntOrStr = AString "Hello there"
```

Each alternative is introduced by a **constructor** (`Hearts`, `AnInteger`, …), which may carry data.

### Product Types And Record Syntax

```haskell
-- The Int and String are unnamed members,
-- extracted by pattern matching
data IntAndStr = IntAndStr Int String
x :: IntAndStr = IntAndStr 1 "hello there"
```

#### Definitions

> **Record syntax**: A way to name the members of a product type; each name also becomes an accessor function.

```haskell
-- number and street are named members
data Address = Address
    { number :: Int
    , street :: String
    } -- this is the Haskell indentation convention

-- Create a value with names, or positionally
addr = Address { number = 1, street = "a" }
addr = Address 1 "a"

-- Access a member
number addr

-- A new Address with number changed (values are immutable, so it's a copy)
addr { number = 2 }
```

### Worked Exercise: A Person Type

The lecture exercise asks for a `Person` type with an integer age and string name, an `isAdult` test written three ways, and filtering a list of people.

```haskell
data Person = Person { name :: String, age :: Int }

-- 1. Boolean expression
isAdult :: Person -> Bool
isAdult p = age p >= 18

-- 2. Guarded equation
isAdult' :: Person -> Bool
isAdult' p | age p >= 18 = True
           | otherwise   = False

-- 3. if/else expression
isAdult'' :: Person -> Bool
isAdult'' p = if age p >= 18 then True else False

people = [Person "Ann" 20, Person "Bo" 12, Person "Cy" 18]
adults = filter isAdult people          -- Ann and Cy

-- Extension: recursive filter with list patterns and cons
adultsRec :: [Person] -> [Person]
adultsRec [] = []
adultsRec (p:ps)
    | isAdult p = p : adultsRec ps
    | otherwise = adultsRec ps
```

Quiz answers from the lecture: a tuple is a **fixed-length collection of possibly heterogeneous types**, and a list is defined as `data List a = [] | a : List a`.

Assigned reading (LYAH): "Baby's first functions", "Texas ranges", "Curried functions"; in preparation: "I'm a list comprehension", "An intro to lists".
