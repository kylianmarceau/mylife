---
tags:
  - advanced-programming
---

# Introduction To Haskell

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP 5 - Haskell 1 - Intro.pptx](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP%205%20-%20Haskell%201%20-%20Intro.pptx), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, slides 1–28
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Haskell's four defining characteristics, installing and using GHC/GHCi, basic syntax and list functions, writing functions as pipelines, naming and layout rules, and a prime-search example.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#How To Approach The Haskell Section|How To Approach The Haskell Section]]
  - [[#What Is Haskell?|What Is Haskell?]]
  - [[#Functional Programming Language|Functional Programming Language]]
  - [[#Pure Functions And No Mutability|Pure Functions And No Mutability]]
  - [[#Lazy Evaluation In Practice|Lazy Evaluation In Practice]]
  - [[#Strict, Static, Expressive Type System|Strict, Static, Expressive Type System]]
  - [[#Installing And Using GHC And GHCi|Installing And Using GHC And GHCi]]
  - [[#Basic Haskell: Arithmetic And Defining Functions|Basic Haskell: Arithmetic And Defining Functions]]
  - [[#Basic List Functions|Basic List Functions]]
  - [[#Calling Functions|Calling Functions]]
  - [[#Scripts|Scripts]]
  - [[#Writing Functions As Pipelines|Writing Functions As Pipelines]]
  - [[#Naming Conventions|Naming Conventions]]
  - [[#Layout Rules|Layout Rules]]
  - [[#Example: Prime Number Search|Example: Prime Number Search]]

---

## Core Content

### How To Approach The Haskell Section

- The lectures give an overview, but are **authoritative and complete** about what is examinable.
- The textbook gives detail; Google and the Haskell Wiki (wiki.haskell.org) supplement it.
- Practice builds understanding — exercises come with each lecture.
- Ask questions in class or by email. One resource alone isn't enough.
- Learn to program Haskell yourself rather than having an LLM generate code: closed practicals require writing code unassisted.

Advanced readings are marked **[AR: …]**. They are **not examinable** and never appear in assignments, tests, quizzes or the exam. If you aren't yet confident in FP, read them after the course.

Lecture aims: know Haskell's major characteristics, have GHC and GHCi installed, and be able to define your own function.

### What Is Haskell?

Haskell is unlike most languages you've used — abandon your preconceptions. It has four major characteristics:

| Characteristic | Meaning |
|---|---|
| Functional | Computation is a series of mathematical functions; functions are first-class |
| Pure | Functions have no side effects; nothing is mutable |
| Lazy | Expressions aren't evaluated until used |
| Strongly typed | Strict, static, expressive type system with **type inference** |

### Functional Programming Language

Haskell follows the functional paradigm: computations are treated as a series of mathematical functions.

Functions are **first-class objects** — you can do anything with a function that you could do with any other value, such as a string:

- treat them as values,
- pass them to functions,
- assign them to variables.

### Pure Functions And No Mutability

#### Definitions

> **Side effect**: An effect of a function other than its return value, such as modifying a variable passed to it.

In Haskell, functions can affect the program **only through what they return**. There is no mutability: every variable is constant.

This Python can't be translated directly into Haskell, because `add_name` mutates its argument:

```python
def add_name(name: str, names: list[str]):
    # Modifying 'names' is a side effect: it isn't the main effect
    # of the function (= what it returns, here nothing)
    names.append(name)

our_names = []
add_name("Alice", our_names)
add_name("Bob", our_names)
add_name("Charlie", our_names)
print("Original list", our_names)
# Original ['Alice', 'Bob', 'Charlie']
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

-- Not idiomatic Haskell; written to mirror the Python version
main :: IO ()
main = do
    let our_names :: [String] = []
    let new_names1 = add_name "Alice" our_names
    let new_names2 = add_name "Bob" new_names1
    let new_names3 = add_name "Charlie" new_names2
    putStrLn ("New names " ++ show new_names3)
    putStrLn ("Original our_names " ++ show our_names)
```

The original list is never changed.

### Lazy Evaluation In Practice

Expressions are not evaluated until they are used, so anything unused is skipped. This is safe because expressions have no side effects — skipping them changes nothing else.

```python
def infinite_loop():
    print("Infinite loop")
    infinite_loop()

print("All fine?", (infinite_loop(), ())[1])
# Prints "Infinite loop" forever (until stack overflow)
```

```haskell
infiniteLoop :: IO ()
infiniteLoop = do
    putStrLn "Infinite loop"
    infiniteLoop -- recursive tail call = infinite loop

main :: IO ()
-- snd is equivalent to my_tuple[1] in Python
main = putStrLn ("All fine! " ++ show (snd (infiniteLoop, ())))
-- Prints "All fine! ()"
```

`infiniteLoop` does print, but in Haskell that effect is encapsulated in its return type `IO ()`, so it is no longer a side effect. `snd` throws away the first component, so the prints are never run.

### Strict, Static, Expressive Type System

| Property | Meaning | Comparison |
|---|---|---|
| **Strict** | Values are not coerced between types: an `Int` can't become a `String` | Like Python, unlike JavaScript |
| **Static** | Types don't change at run time; a function declared to return `String` can only return `String` | Like Java, unlike Python |
| **Expressive** | Types can capture — **and enforce** — many more constraints than Python's or Java's | Revisited in [Making Illegal States Unrepresentable](13_Making_Illegal_States_Unrepresentable.md) |

[AR: "Parse, don't validate" by Alexis King] [AR: "Making illegal states unrepresentable"]

### Installing And Using GHC And GHCi

Install through **GHCup** (haskell.org/ghcup), selecting both ghc and ghci; Cabal is also useful. On Linux or WSL, run the installer and follow the wizard:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
```

| Tool | Role | Analogy |
|---|---|---|
| `ghc` | Glasgow Haskell Compiler | `javac` |
| `ghci` | GHC interactive interpreter | Python REPL |
| Cabal | Package manager for GHC | pip/uv (Python), Maven/Gradle (Java) |

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
Leaving GHCi.
```

| GHCi command | Action |
|---|---|
| `:?` | Show all commands |
| `:quit` | Quit GHCi |
| `:load name` | Load the given script |
| `:reload` | Reload the current script |

### Basic Haskell: Arithmetic And Defining Functions

#### Definitions

> **Prelude**: The built-in functions available without any import.

> **Type signature**: A line `name :: Type` declaring a function's argument and result types.

```haskell
1 + 1      -- 2
5 - 2      -- 3
8 / 2      -- 4.0
2 * 5      -- 10
sqrt(144)  -- 12.0
5 ^ 2      -- 25
```

Functions are written much like in mathematics: a type signature, then the body. Here `f` accepts a `Float` and returns a `Float`:

```haskell
f :: Float -> Float
f x = 2 * x
```

![Anatomy of a function definition](../../../diagrams/CSC3003S-Advanced%20Programming/FP/05_Haskell_Introduction/function-anatomy.svg)

*The signature names the argument and result types; the equation names the parameter and gives the body expression.*

### Basic List Functions

The list never changes — each function returns a new value.

```haskell
let list = [1, 2, 3, 4]
```

| Expression | Meaning | Result |
|---|---|---|
| `head list` | First element | `1` |
| `tail list` | Everything after the first element | `[2, 3, 4]` |
| `list !! 2` | Element at index 2 | `3` |
| `take 3 list` | First 3 elements | `[1, 2, 3]` |
| `drop 3 list` | Remove the first 3 elements | `[4]` |
| `length list` | Length | `4` |
| `sum list` | Sum (numeric lists) | `10` |
| `product list` | Product (numeric lists) | `24` |
| `list ++ [5, 6]` | Append two lists | `[1, 2, 3, 4, 5, 6]` |
| `list ++ [5]` | Often used to add one element | `[1, 2, 3, 4, 5]` |
| `reverse list` | Reverse | `[4, 3, 2, 1]` |
| `map (* 2) list` | Apply a function to each element | `[2, 4, 6, 8]` |

The lecture exercise "return only the palindromes from a list of strings" combines these:

```haskell
palindromes :: [String] -> [String]
palindromes ws = filter (\w -> w == reverse w) ws
-- palindromes ["aba", "abb", "hello", "racecar"] == ["aba", "racecar"]
```

### Calling Functions

Functions are called (applied) with a **space**, not brackets: `head [1, 2, 3, 4]`.

Function application binds more tightly than any operator:

| Haskell | Means |
|---|---|
| `f a + b` | $f(a) + b$, not $f(a + b)$ |
| `f (a + b)` | $f(a + b)$ — brackets group |

### Scripts

Haskell scripts use the `.hs` extension.

- Run with `runghc myscript.hs` (needs a `main` function).
- Or load into GHCi as a module: `ghci myscript.hs`, or `:load myscript.hs` at the prompt.

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

### Writing Functions As Pipelines

Write functions as **compositions of other functions**. Instead of a sequence of imperative actions, express the computation as a pipeline of functions applied to the input (similar to map-reduce).

A function body is often a single expression, with a `where` clause for interim steps:

```haskell
-- Quadratic formula: solutions for x in ax^2 + bx + c = 0
intercepts :: Float -> Float -> Float -> (Float, Float)
intercepts a b c = (sol1, sol2)
    where sol1 = (-b + sqrt(discrim)) / denom
          sol2 = (-b - sqrt(discrim)) / denom
          discrim = b ^ 2 - (4 * a * c)
          denom = 2 * a
```

This implements

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### Naming Conventions

| Kind | Convention | Example |
|---|---|---|
| Functions | Start lowercase, camelCase | `sayHello` |
| Types | Start uppercase, PascalCase | `MyPet` |
| List arguments | End in `s` | `xs`, `pets` |

```haskell
-- A type, so PascalCase
data MyPet = Cat | Dog -- like an enum

-- A function, so camelCase
sayHello :: MyPet -> String
sayHello Cat = "Hello, cat!"
sayHello Dog = "Hello, dog!"

sayHelloAll :: [MyPet] -> [String]
-- apply sayHello to each element; pets ends in s because it's a list
sayHelloAll pets = map sayHello pets

main :: IO ()
main = putStrLn (show (sayHelloAll [Dog, Cat, Dog]))
-- Prints ["Hello, dog!","Hello, cat!","Hello, dog!"]
```

### Layout Rules

Whitespace is significant, as in Python. In a sequence of definitions, every definition must start in the **same column**. Braces `{}` and semicolons `;` can be used for explicit grouping instead.

| Code | Valid? |
|---|---|
| `a = 10` / `b = 20` / `c = 30`, all in column 1 | ✅ |
| `a = 10` / `  b = 20` / `c = 30` (b indented) | ❌ |
| `  a = 10` / `  b = 20` / `c = 30` (c out of line) | ❌ |
| `{a = 10;` / `  b = 20;` / `c = 30}` | ✅ (explicit grouping) |

In the `intercepts` example, the `where` definitions `sol1`, `sol2`, `discrim` and `denom` are all in line.

The lecture exercise asks you to fix this code:

```haskell
foo :: String
foo = a ‘div’ length xs
    Where a = 10
  xs = [1, 2, 3, 4, 5]
```

Its errors and the fix:

| Error | Kind | Fix |
|---|---|---|
| `foo :: String` but the result is a number | Type | `foo :: Int` |
| `‘div’` uses curly quotes | Syntax | Backticks: `` `div` `` |
| `Where` is capitalised | Syntax | `where` |
| `xs` is not aligned with `a` | Layout | Line up the `where` definitions |

```haskell
foo :: Int
foo = a `div` length xs
    where a = 10
          xs = [1, 2, 3, 4, 5]
```

### Example: Prime Number Search

Return all primes from 2 to `upperBound`. Think declaratively first:

1. We want all numbers from 2 to `upperBound` that are prime…
2. … $x$ is prime when it has no divisors other than 1 and $x$ …
3. … which means that for every $y \in [2, x-1]$, dividing $x$ by $y$ leaves a remainder.

Then implement top-down. The main function tests each number for primality and keeps only primes:

```haskell
primes :: Int -> [Int]
primes upperBound = filter isPrime [2..upperBound]
```

`isPrime` checks that no number in $[2, x-1]$ divides $x$:

```haskell
isPrime :: Int -> Bool
-- not $ a b c is syntax sugar for not (a b c)
-- Haskellers like to avoid brackets where possible!
isPrime x = not $ any (isDivisor x) [2..(x - 1)]

-- Int -> Int -> Bool = takes two ints, returns a Bool
isDivisor :: Int -> Int -> Bool
-- a `mod` b is syntax sugar for mod a b
isDivisor num divisor = (num `mod` divisor) == 0
```

| Syntax | Meaning |
|---|---|
| `f $ g x` | `f (g x)` — `$` avoids brackets |
| `` a `mod` b `` | `mod a b` — backticks make a function infix |
| `[2..n]` | The list $2, 3, \dots, n$ |
| `any p xs` | True if `p` holds for some element of `xs` |

```text
ghci> :load primeSearch.hs
Ok, one module loaded.
ghci> isPrime 10
False
ghci> isPrime 13
True
```

![Prime search pipeline](../../../diagrams/CSC3003S-Advanced%20Programming/FP/05_Haskell_Introduction/prime-pipeline.svg)

*The range $[2..n]$ flows through `filter isPrime`, which uses `any (isDivisor x)` to reject composites.*

Assigned reading (Learn You a Haskell): *Introduction* ("So, what's Haskell?", "What you need"), *Starting Out* ("Ready, set, go!", "Baby's first functions", "Tuples"), and *Types and Typeclasses* ("Believe the type").
