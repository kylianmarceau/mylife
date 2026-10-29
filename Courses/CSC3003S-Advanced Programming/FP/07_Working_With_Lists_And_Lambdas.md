---
tags:
  - advanced-programming
---

# Haskell 3 — Working With Lists And Lambdas

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-7-Haskell 3-working with lists-2.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-7-Haskell%203-working%20with%20lists-2.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–29  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: map, filter, zip, fold, lambdas, and list/string comprehensions with guards and dependent generators.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Recap Quiz|Recap Quiz]]
  - [[#Map And Filter|Map And Filter]]
  - [[#Batch Processing: Prime Factorisation|Batch Processing: Prime Factorisation]]
  - [[#Lambdas|Lambdas]]
  - [[#Why Have Lambdas?|Why Have Lambdas?]]
  - [[#Zip|Zip]]
  - [[#Quickfire Combinators|Quickfire Combinators]]
  - [[#Fold|Fold]]
  - [[#foldl Versus foldr|foldl Versus foldr]]
  - [[#Fold Is The Universal List Combinator|Fold Is The Universal List Combinator]]
  - [[#Sequence Comprehensions And Generators|Sequence Comprehensions And Generators]]
  - [[#Guards: Comprehensions Versus Combinators|Guards: Comprehensions Versus Combinators]]
  - [[#Multiple Generators (Not Zip)|Multiple Generators (Not Zip)]]
  - [[#Dependent Generators|Dependent Generators]]
  - [[#String Comprehensions|String Comprehensions]]

---

## Core Content

### Recap Quiz

| Question | Answer |
|---|---|
| How do you state that `x` has type `Int -> Int -> Int`? | `x :: Int -> Int -> Int = ...` |
| What is a sum type? | A type whose value must be **one of** the types it is a sum of |

### Map And Filter

#### Definitions

> **Higher-order function**: A function that accepts a function as an argument.

> **`map`**: Applies the given function (the **mapper**) to each element of a sequence.

> **`filter`**: Applies the given function (the **predicate**) to each element and removes elements for which it returns `False`.

> **(List) combinator**: A function like `map` or `filter` that builds sequence processing from other functions.

```haskell
map (* 2) [1, 2, 3, 4]     -- [2, 4, 6, 8]
filter (<= 2) [1, 2, 3, 4] -- [1, 2]
```

They are useful because data processing becomes a pipeline of independent steps, which suits batch and parallel stream processing.

![Map and filter pipeline](../../../diagrams/CSC3003S-Advanced%20Programming/FP/07_Working_With_Lists_And_Lambdas/map-filter-pipeline.svg)

*A stream passes through `map (+1)`, `filter isOdd`, then `map (*2)`. Each stage is independent, so stages can be streamed or parallelised.*

### Batch Processing: Prime Factorisation

Goal: the **unique** prime factors of each number, e.g. $9 \mapsto [3]$, not $[3,3]$. The naive plan:

1. Get each number's factors: all numbers in $1..N$ that divide $N$.
2. Keep only prime factors: $F$ is prime when the only numbers in $1..F$ dividing $F$ are $1$ and $F$.

In combinator terms:

1. **map** each input number to its factors by **filtering** $1..N$ for divisors.
2. **filter** the factors to the primes by checking that the factors of $F$ equal $[1,F]$.

```haskell
primeFactoriseNums :: [Int] -> [[Int]]
primeFactoriseNums ns = map primeFactorise ns

primeFactorise :: Int -> [Int]
primeFactorise n = filter isPrime (factorise n)

factorise :: Int -> [Int]
factorise n = filter (divides n) [1..n]

divides :: Int -> Int -> Bool
divides num denom = num `mod` denom == 0

isPrime :: Int -> Bool
isPrime n = (factorise n) == [1, n]
```

| Question | Answer |
|---|---|
| Q1. What does `divides n` do? | It partially applies `divides`, fixing `num = n`. The result is a predicate `Int -> Bool` testing whether a candidate divides `n`. |
| Q2. What do the backticks do? | They use a prefix function as an infix operator: ``num `mod` denom`` means `mod num denom`. |

`1` is never counted as prime: `factorise 1 = [1]`, which is not `[1, 1]`.

### Lambdas

#### Definitions

> **Lambda**: An anonymous function, named after the Greek letter λ, because Haskell is based on lambda calculus.

`divides` exists only to be passed to `filter`, so replace it with a lambda:

```haskell
factorise :: Int -> [Int]
factorise n = filter (\f -> n `mod` f == 0) [1..n]
```

| Language | Notation |
|---|---|
| Haskell | `\x -> 2 * x` |
| Python | `lambda x: 2 * x` |
| Java | `x -> 2 * x` |
| JavaScript (closures) | `(x) => 2 * x` |
| Rust (closures / `Fn*` family) | `\|x\| 2 * x` |
| Mathematics | $x \mapsto 2x$ |
| Lambda calculus | $(\lambda x.\,2x)$ or $\lambda x \to 2x$ |

### Why Have Lambdas?

1. **Fewer one-off functions** to define.
2. **Notating currying**: "a function returning a function" is easy to write.

$$
\texttt{add x y = x + y} \quad\equiv\quad \texttt{add} = \lambda x \to (\lambda y \to x + y)
$$

3. **Writing functions that return functions**, which can show intent better than currying a two-argument function. For example, a UI button callback receives the press count (`Int`) and returns text to display (`String`):

```haskell
makeCallback :: String -> (Int -> String)
makeCallback name = \n -> "Hello" ++ name ++
                          "! Button has been pressed" ++ show n ++ "times."

makeButton (makeCallback "Cael")
```

This is about ergonomics and expressivity, which FP values highly, not about what is possible.

### Zip

#### Definitions

> **`zip`**: Combines two parallel lists pairwise into a list of tuples.

Task: print the names of everyone under 65. Filtering names alone loses the ages, and filtering ages alone loses the names.

```haskell
names = ["John", "Eliza", "Muhammad", "Velesazi"]
ages  = [ 18,     102,     34,         68       ]

zip names ages
-- [("John", 18), ("Eliza", 102), ("Muhammad", 34), ("Velesazi", 68)]

map fst $ filter (\(name, age) -> age < 65) $ zip names ages
-- ["John", "Muhammad"]
```

- `fst` returns the first element of a pair.
- `foo $ bar baz quux` is sugar for `foo (bar baz quux)`.
- The lambda pattern-matches the tuple directly: `\(name, age) -> …`.

### Quickfire Combinators

| Combinator | Behaviour |
|---|---|
| `all pred list` | `True` if `pred` holds for **all** elements |
| `any pred list` | `True` if `pred` holds for **any** element |
| `take n list` | First $n$ elements |
| `drop n list` | Remove first $n$ elements |
| `takeWhile pred list` | Elements matching `pred` from the front, **stopping at the first non-match** |
| `dropWhile pred list` | Remove elements matching `pred` from the front, stopping at the first non-match |

### Fold

#### Definitions

> **Fold**: The most powerful list combinator. It takes an operation $f$, an **accumulator** (`acc`) and the data, and runs `f acc elt` for each element, using the output as the next accumulator.

$$
acc' = f(acc,\ elt)
$$

Use fold when a task does not fit `zip`, `filter`, `map` or another combinator:

```haskell
names = ["Tshepo", "Tafadzwa", "Tom"]
(foldl (\acc elt -> acc ++ elt ++ ", ") "Hello, " names)
    ++ "and everyone else!"
-- "Hello, Tshepo, Tafadzwa, Tom, and everyone else!"
```

Product:

```haskell
ns = [5, 10, 2, 3]
foldl (*) 1 ns   -- 300
```

### foldl Versus foldr

The product above is $1\times5\times10\times2\times3=300$, but the order of combination differs:

| Fold | Associativity | Product expansion |
|---|---|---|
| `foldl` (left) | Left-associative | $(((1\times5)\times10)\times2)\times3$ |
| `foldr` (right) | Right-associative | $5\times(10\times(2\times(3\times1)))$ |

![foldl versus foldr](../../../diagrams/CSC3003S-Advanced%20Programming/FP/07_Working_With_Lists_And_Lambdas/fold-trees.svg)

*`foldl` nests from the left starting at `z`. `foldr` nests from the right, ending at `z`. In the captions, `f` is written infix.*

The difference matters for operators that are not associative, such as subtraction:

$$
\texttt{foldl (-) 1 ns} = (((1-5)-10)-2)-3 = -19
$$

$$
\texttt{foldr (-) 1 ns} = 5-(10-(2-(3-1))) = 5-(10-0) = -5
$$

The strict variant `foldl'` is covered in the lazy evaluation lecture ([Recursion And Lazy Evaluation](09_Recursion_And_Lazy_Evaluation.md)).

### Fold Is The Universal List Combinator

Fold can implement any other list combinator. It is the FP analogue of a `for` loop with state:

```python
greeting = "Hello, "
for name in names:
    greeting += name + ","
greeting += "and everyone else"
```

The difference: the accumulator is not mutated. A new copy is passed forward for each element.

The lecture exercise reimplements `sum`, `map` and `filter` with `foldl`:

```haskell
sum' :: [Int] -> Int
sum' = foldl (+) 0

map' :: (a -> b) -> [a] -> [b]
map' f xs = foldl (\acc x -> acc ++ [f x]) [] xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' p xs = foldl (\acc x -> if p x then acc ++ [x] else acc) [] xs
```

### Sequence Comprehensions And Generators

#### Definitions

> **Comprehension**: Building a sequence the way a set is defined in mathematics.

> **Generator**: The part `x <- xs` that draws each element from a source sequence.

The even positive integers:

$$
E=\{\,2x \mid x\in\mathbb{N}\,\}
$$

```haskell
e = [2 * x | x <- [1..]]   -- x <- [1..] is a generator
take 3 e                   -- [2, 4, 6]
```

Laziness makes the infinite source `[1..]` safe.

### Guards: Comprehensions Versus Combinators

#### Definitions

> **Guard (in a comprehension)**: A Boolean condition after the generators that filters which elements are kept.

Comprehensions are an alternative to `map` and `filter`:

```haskell
-- type signatures are optional if they can be inferred
factorise  n = filter (\f -> n `mod` f == 0) [1..n]
factorise' n = [f | f <- [1..n], n `mod` f == 0]   -- n `mod` f == 0 is a guard
```

Mapping strings to their lengths: `[length s | s <- strs]`, equivalent to `map length strs`.

### Multiple Generators (Not Zip)

Several generators produce the **Cartesian product**: every combination. They work like nested `for` loops, so order matters. The **later** generator varies fastest.

```haskell
suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
-- deck without jokers, aces, or royalty
regularCards = [(n, suit) | suit <- suits, n <- [2..10]]

take 3 regularCards
-- [(2,"Clubs"), (3,"Clubs"), (4,"Clubs")]
take 3 $ drop 9 regularCards
-- [(2,"Hearts"), (3,"Hearts"), (4,"Hearts")]
```

Swapping the generators, `[(n, suit) | n <- [2..10], suit <- suits]`, cycles suits fastest: `(2,"Clubs"), (2,"Hearts"), (2,"Spades"), …`.

| `zip xs ys` | `[(x, y) \| x <- xs, y <- ys]` |
|---|---|
| Pairs elements position by position | Pairs every element with every element |
| Length = shorter list | Length = product of lengths |

### Dependent Generators

A later generator can depend on variables bound by an **earlier** one. For example, the coordinates of the 1s in a $3\times3$ bottom-left triangular matrix:

```haskell
[(x, y) | x <- [1..3], y <- [1..x]]
-- [(1,1),
--  (2,1), (2,2),
--  (3,1), (3,2), (3,3)]
```

Flattening a list of lists:

```haskell
flatten xss = [x | xs <- xss, x <- xs]
flatten [[1, 2], [3, 4], [5]]   -- [1, 2, 3, 4, 5]
```

### String Comprehensions

A `String` is a list of `Char`, so `map`, `filter`, `fold` and comprehensions all work on it:

```haskell
import Data.Char
[toUpper c | c <- "hello"]   -- "HELLO"
```
