---
tags:
  - advanced-programming
---

# Haskell 1 — Introduction To Haskell

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP 5 - Haskell 1 - Intro.pptx](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%205%20-%20Haskell%201%20-%20Intro.pptx), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, slides 1–28  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: Haskell's four characteristics, the GHC toolchain, basic Prelude functions, and writing your first functions.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#How To Approach The Haskell Section|How To Approach The Haskell Section]]
  - [[#What Is Haskell?|What Is Haskell?]]
  - [[#1. A Functional Programming Language|1. A Functional Programming Language]]
  - [[#2. Pure Functions (No Side Effects)|2. Pure Functions (No Side Effects)]]
  - [[#3. Lazy Evaluation|3. Lazy Evaluation]]
  - [[#4. Strict, Static, Expressive Type System|4. Strict, Static, Expressive Type System]]
  - [[#Installation And GHCi|Installation And GHCi]]
  - [[#Basic Haskell: Prelude Maths And Defining Functions|Basic Haskell: Prelude Maths And Defining Functions]]
  - [[#Basic Haskell: List Functions|Basic Haskell: List Functions]]
  - [[#Calling Functions|Calling Functions]]
  - [[#Your First Script|Your First Script]]
  - [[#Writing Functions As Compositions|Writing Functions As Compositions]]
  - [[#Naming Conventions|Naming Conventions]]
  - [[#Layout Rule|Layout Rule]]
  - [[#Worked Example: Prime Number Search|Worked Example: Prime Number Search]]

---

## Core Content

### How To Approach The Haskell Section

- The **lectures are authoritative and complete** about what is examinable. The textbook gives detail; Google and the Haskell Wiki (`https://wiki.haskell.org`) supplement it.
- Practice is essential: exercises come at the end of each lecture. No single resource is enough on its own.
- Write Haskell yourself rather than relying on an LLM: **closed pracs** require writing code unassisted.
- Advanced reading is marked `[AR: …]` and is **not examinable** (not in assignments, tests, quizzes or the exam).

### What Is Haskell?

Haskell has four major characteristics:

1. A functional programming language.
2. Pure functions (no side effects).
3. Lazy evaluation.
4. A strict, static, expressive type system with **type inference**.

Haskell is unlike most languages you will have used, so set aside imperative preconceptions.

### 1. A Functional Programming Language

#### Definitions

> **First-class object**: A value you can do anything with that you could do with any other value.

Computations are treated as a series of mathematical functions. Because functions are first-class, you can:

- treat them as values
- pass them to functions
- assign them to variables

### 2. Pure Functions (No Side Effects)

#### Definitions

> **Side effect**: An effect a function has other than its main effect, which is what it returns.

Functions can affect the program **only through what they return**. There is no mutability: every variable is constant.

This Python mutates the list passed in, so it cannot be translated directly into Haskell:

```python
def add_name(name: str, names: list[str]):
    names.append(name)      # side effect: modifies the caller's list

our_names = []
add_name("Alice", our_names)
add_name("Bob", our_names)
add_name("Charlie", our_names)
print("Original list", our_names)   # ['Alice', 'Bob', 'Charlie']
```

Instead, create a new copy with the change and pass it forward:

```python
def add_name(name: str, names: list[str]) -> list[str]:
    return names + [name]

our_names = []
new_names1 = add_name("Alice", our_names)
new_names2 = add_name("Bob", new_names1)
new_names3 = add_name("Charlie", new_names2)
print("New names", new_names3)          # ["Alice", "Bob", "Charlie"]
print("Original our_names", our_names)  # []
```

```haskell
add_name :: String -> [String] -> [String]
add_name name names = names ++ [name]
-- Not idiomatic Haskell: written to mirror the Python version

main :: IO ()
main = do
    let our_names :: [String] = []
    let new_names1 = add_name "Alice" our_names
    let new_names2 = add_name "Bob" new_names1
    let new_names3 = add_name "Charlie" new_names2
    putStrLn ("New names " ++ show new_names3)
    putStrLn ("Original our_names " ++ show our_names)
```

### 3. Lazy Evaluation

Expressions are not evaluated until they are used, so anything unused can be skipped. This is safe because expressions have no side effects: skipping one changes nothing else.

```python
def infinite_loop():
    print("Infinite loop")
    infinite_loop()

print("All fine?", (infinite_loop(), ())[1])
# Prints "Infinite loop" forever: Python evaluates the tuple eagerly
```

```haskell
infiniteLoop :: IO ()
infiniteLoop = do
    putStrLn "Infinite loop"
    infiniteLoop            -- recursive tail call = infinite loop

main :: IO ()
-- snd is equivalent to my_tuple[1] in Python
main = putStrLn ("All fine! " ++ show (snd (infiniteLoop, ())))
-- Prints "All fine! ()"
```

Printing looks like a side effect, but in Haskell it is encapsulated in the return type `IO ()`, so it is no longer a side effect. Throwing away the returned value throws away the prints too, and the unused `infiniteLoop` is never run.

### 4. Strict, Static, Expressive Type System

| Property | Meaning | Comparison |
|---|---|---|
| **Strict** | No implicit coercion: an `Int` cannot be coerced to a `String` | Like Python; unlike JavaScript |
| **Static** | Types do not change at run time; a function declared to return `String` can only return `String` | Like Java; unlike Python |
| **Expressive** | Can capture **and enforce** many more constraints than Python or Java | Revisited in [Making Illegal States Unrepresentable](13_Making_Illegal_States_Unrepresentable.md) |

### Installation And GHCi

#### Definitions

> **ghc**: The Glasgow Haskell Compiler.

> **ghci**: The GHC interactive interpreter.

> **Cabal**: The package manager for GHC (like pip/uv for Python, or Maven/Gradle for Java).

> **GHCup**: The installer for the Haskell toolchain (`https://www.haskell.org/ghcup/`). Select both ghc and ghci; Cabal may also be useful.

On Linux or WSL:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
```

Run `ghci` and type expressions at the `ghci>` prompt. Wrap multi-line input in `:{` and `:}`:

```text
$ ghci
ghci> 1 + 1
2
ghci> :{
ghci| f :: Int -> Int
ghci| f x = x - 1
ghci| :}
ghci> f 2
1
ghci> :quit
```

| Command | Effect |
|---|---|
| `:?` | Show all commands |
| `:quit` | Quit ghci |
| `:load name` | Load the given script |
| `:reload` | Reload the current script |

### Basic Haskell: Prelude Maths And Defining Functions

#### Definitions

> **Prelude**: The built-in functions available without any import.

> **Type signature**: A declaration of a function's argument and result types, written before its body.

```haskell
1 + 1      -- 2
5 - 2      -- 3
8 / 2      -- 4.0
2 * 5      -- 10
sqrt(144)  -- 12.0
5 ^ 2      -- 25
```

Functions are defined much like mathematical functions:

```haskell
f :: Float -> Float
f x = 2 * x
```

![Anatomy of a Haskell function](../../../diagrams/CSC3003S-Advanced%20Programming/FP/05_Haskell_Introduction/function-anatomy.svg)

*The signature `f :: Float -> Float` says `f` takes a `Float` and returns a `Float`. The equation names the parameter and gives the body.*

### Basic Haskell: List Functions

`list` never changes in the examples below, because Haskell is immutable.

```haskell
let list = [1, 2, 3, 4]
```

| Expression | Meaning | Result |
|---|---|---|
| `head list` | First element | `1` |
| `tail list` | Everything after the first element | `[2, 3, 4]` |
| `list !! 2` | $n$th element (zero-based) | `3` |
| `take 3 list` | First $n$ elements | `[1, 2, 3]` |
| `drop 3 list` | Remove first $n$ elements | `[4]` |
| `length list` | Length | `4` |
| `sum list` | Sum (numeric lists) | `10` |
| `product list` | Product (numeric lists) | `24` |
| `list ++ [5, 6]` | Append two lists | `[1, 2, 3, 4, 5, 6]` |
| `list ++ [5]` | Common way to add one element | `[1, 2, 3, 4, 5]` |
| `reverse list` | Reverse | `[4, 3, 2, 1]` |
| `map (* 2) list` | Apply a function to each element | `[2, 4, 6, 8]` |

### Calling Functions

Functions are called (applied) with a **space**, not brackets: `head [1, 2, 3, 4]`.

- Function application has **higher priority** than other operators: `f a + b` means $f(a)+b$, not $f(a+b)$.
- Brackets may still be used for grouping, e.g. `f (a + b)`.

### Your First Script

Scripts use the `.hs` extension.

- `runghc myscript.hs` runs a script that has a `main` function.
- `ghci myscript.hs`, or `:load myscript.hs` inside ghci, loads it as a module.

```haskell
double :: Int -> Int
double x = x + x

quadruple :: Int -> Int
quadruple x = double (double x)

-- show converts a value to a string for printing
main :: IO ()
main = putStrLn (show (quadruple 4))
```

```text
ghci> :load myscript.hs
[1 of 2] Compiling Main ( myscript.hs, interpreted )
Ok, one module loaded.
ghci> quadruple 4
16
```

### Writing Functions As Compositions

- Write functions as **compositions** of other functions.
- Instead of an imperative sequence of actions, express the computation as a **pipeline** of functions over an input, similar to map-reduce.
- A function body is often a single expression, with **`where` clauses** for interim steps.

```haskell
-- Quadratic formula: solutions for x in ax^2 + bx + c = 0
intercepts :: Float -> Float -> Float -> (Float, Float)
intercepts a b c = (sol1, sol2)
    where sol1 = (-b + sqrt(discrim)) / denom
          sol2 = (-b - sqrt(discrim)) / denom
          discrim = b ^ 2 - (4 * a * c)
          denom = 2 * a
```

This implements:

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

### Naming Conventions

| Thing | Convention | Example |
|---|---|---|
| Functions | Start lowercase, camelCase | `sayHello` |
| Types | Start uppercase, PascalCase | `MyPet` |
| List arguments | `s` suffix | `xs`, `pets` |

```haskell
data MyPet = Cat | Dog            -- a type (like an enum), so PascalCase

sayHello :: MyPet -> String       -- a function, so camelCase
sayHello Cat = "Hello, cat!"
sayHello Dog = "Hello, dog!"

sayHelloAll :: [MyPet] -> [String]
sayHelloAll pets = map sayHello pets   -- pets is a list, so ends in s

main :: IO ()
main = putStrLn (show (sayHelloAll [Dog, Cat, Dog]))
-- Prints ["Hello, dog!","Hello, cat!","Hello, dog!"]
```

### Layout Rule

#### Definitions

> **Layout rule**: Whitespace is significant. In a sequence of definitions, each definition must begin in the same column.

| Code | Valid? |
|---|---|
| `a = 10` / `b = 20` / `c = 30`, all in column 1 | Yes |
| `b = 20` indented, `a` and `c` not | No |
| `a` and `b` indented, `c` not | No |
| `{a = 10;  b = 20; c = 30}` with explicit braces and semicolons | Yes |

In `intercepts` above, all four `where` definitions start in the same column.

In the lecture's fix-the-errors exercise, applying the layout rule, the type rules and the syntax rules gives:

```haskell
-- Broken original:
-- foo :: String
-- foo = a ‘div’ length xs
--     Where a = 10
--   xs = [1, 2, 3, 4, 5]

foo :: Int                      -- div returns an Int, not a String
foo = a `div` length xs         -- backticks, not curly quotes
    where a = 10                -- lowercase where
          xs = [1, 2, 3, 4, 5]  -- aligned with a
```

### Worked Example: Prime Number Search

Think declaratively first:

1. We want all numbers from $2$ to `upperBound` that are prime.
2. $x$ is prime when it has no divisors other than $1$ and $x$.
3. So for every $y\in[2,x-1]$, dividing $x$ by $y$ leaves a remainder.

Then implement top-down:

```haskell
primes :: Int -> [Int]
primes upperBound = filter isPrime [2..upperBound]

isPrime :: Int -> Bool
-- not $ a b c is syntax sugar for not (a b c)
isPrime x = not $ any (isDivisor x) [2..(x - 1)]

isDivisor :: Int -> Int -> Bool
-- a `mod` b is syntax sugar for mod a b
isDivisor num divisor = (num `mod` divisor) == 0
```

- `$` avoids brackets: Haskellers prefer fewer brackets.
- `isDivisor x` is a partial application (see [Basic Types And Functions](06_Basic_Types_And_Functions.md)).

![Prime search pipeline](../../../diagrams/CSC3003S-Advanced%20Programming/FP/05_Haskell_Introduction/prime-pipeline.svg)

*`primes` filters a range with `isPrime`, which is itself built from `any` and `isDivisor`.*

```text
ghci> :load primeSearch.hs
ghci> isPrime 10
False
ghci> isPrime 13
True
```
