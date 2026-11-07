---
tags:
  - advanced-programming
---

# Working With Lists And Lambdas

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-7-Haskell 3-working with lists-2.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-7-Haskell%203-working%20with%20lists-2.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–29
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> List combinators (map, filter, zip, fold and friends), lambdas, and list, set and string comprehensions with multiple and dependent generators.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Map And Filter|Map And Filter]]
  - [[#Batch Processing: Prime Factorisation|Batch Processing: Prime Factorisation]]
  - [[#Lambdas|Lambdas]]
  - [[#Why Have Lambdas?|Why Have Lambdas?]]
  - [[#Zip|Zip]]
  - [[#Quickfire Combinators|Quickfire Combinators]]
  - [[#Fold|Fold]]
  - [[#Left Versus Right Folds|Left Versus Right Folds]]
  - [[#Fold Is The Universal List Combinator|Fold Is The Universal List Combinator]]
  - [[#Sequence Comprehensions|Sequence Comprehensions]]
  - [[#Multiple Generators|Multiple Generators]]
  - [[#Dependent Generators|Dependent Generators]]
  - [[#String Comprehensions|String Comprehensions]]

---

## Core Content

### Map And Filter

#### Definitions

> **Higher-order function**: A function that accepts a function as an argument.

> **Map**: Applies a given function (the **mapper**) to each element of a sequence.

> **Filter**: Applies a given function (the **predicate**) to each element of a sequence and removes the element if the predicate returns `False`.

> **(List) combinator**: A name for `map`, `filter` and similar functions that build list computations from smaller functions.

```haskell
map (* 2) [1, 2, 3, 4]     -- [2, 4, 6, 8]
filter (<= 2) [1, 2, 3, 4] -- [1, 2]
```

They work on sequences such as lists and strings. They are practically useful because they make batch and streaming data processing simple — and parallelisable (e.g. Channable's parallel streaming in Haskell).

Recap: `x :: Int -> Int -> Int = ...` declares that `x` has that type, and a **sum type** must hold a value of exactly **one** of the types it is a sum of.

### Batch Processing: Prime Factorisation

Task: get the unique prime factors of each number (for 9, return just `[3]`, not `[3, 3]`).

A naive approach:

1. Get every factor of each number $N$: all numbers in $1..N$ that divide $N$.
2. Keep only the prime factors: $F$ is prime if, among $1..F$, only $1$ and $F$ divide $F$.

In terms of maps and filters:

1. **Map** the input list to each number's factors (filter $1..N$ to those dividing $N$).
2. **Filter** the factors to the primes (filter $1..F$ to the divisors of $F$ and check the result equals $[1, F]$).

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

Two details:

- `divides n` is a **partial application**: `divides` takes two `Int`s, so giving it `n` produces a predicate `Int -> Bool` that tests whether its argument divides `n`. That is exactly what `filter` needs.
- The backticks in `` num `mod` denom `` turn the prefix function `mod` into an infix operator: it means `mod num denom`.

![Map and filter pipeline](../../../diagrams/CSC3003S-Advanced%20Programming/FP/07_Working_With_Lists_And_Lambdas/map-filter-pipeline.svg)

*Each number is mapped to its factor list, which is then filtered down to the primes.*

### Lambdas

#### Definitions

> **Lambda**: An anonymous function — that is all. Named after the Greek letter λ, because Haskell is based on the lambda calculus.

`divides` exists only to be passed to `filter`. A lambda replaces it:

```haskell
factorise :: Int -> [Int]
factorise n = filter (\f -> n `mod` f == 0) [1..n]
```

| Language | Lambda for "double x" |
|---|---|
| Haskell | `\x -> 2 * x` |
| Python | `lambda x: 2 * x` |
| Java | `x -> 2 * x` |
| JavaScript (closures) | `(x) => 2 * x` |
| Rust (closures / `Fn*` family) | `\|x\| 2 * x` |
| Mathematics | $x \mapsto 2x$ |
| Lambda calculus | $\lambda x.\ 2x$ or $\lambda x \to 2x$ |

### Why Have Lambdas?

1. **Fewer one-off functions**: no need to name helpers like `divides`.
2. **Notating currying**: "a function returning a function" is easy to write:
$$
\texttt{add } x\ y = x + y \quad\equiv\quad \texttt{add} = \lambda x \to (\lambda y \to x + y)
$$
3. **Functions that return functions**, for clearer intent. A UI framework might call a button callback with the press count (`Int`) and display the returned `String`:

```haskell
makeCallback :: String -> (Int -> String)
makeCallback name = \n -> "Hello " ++ name ++
                          "! Button has been pressed " ++ show n ++ " times."

makeButton (makeCallback "Cael")
```

This could also be a two-argument function that is then curried. The lambda isn't about what is possible but about **ergonomics and expressivity**, which FP values highly.

### Zip

#### Definitions

> **Zip**: Combines two lists pairwise into a list of tuples.

Suppose you have parallel lists of names and ages and want the names of everyone under 65. Filtering `names` fails (the predicate doesn't see ages), and filtering `ages` fails (you lose the names). Zip them first:

```haskell
names = ["John", "Eliza", "Muhammad", "Velesazi"]
ages  = [ 18,     102,     34,         68       ]

zip names ages
-- [("John",18), ("Eliza",102), ("Muhammad",34), ("Velesazi",68)]

map fst $ filter (\(name, age) -> age < 65) $ zip names ages
-- ["John", "Muhammad"]
```

Recall that `fst` returns the first element of a pair, and `foo $ bar baz quux` means `foo (bar baz quux)`.

### Quickfire Combinators

| Combinator | Result |
|---|---|
| `all pred list` | `True` if `pred` holds for **all** elements |
| `any pred list` | `True` if `pred` holds for **any** element |
| `take n list` | The first `n` elements |
| `drop n list` | The list without its first `n` elements |
| `takeWhile pred list` | Elements from the front while `pred` holds; stops at the first non-matching element |
| `dropWhile pred list` | Removes elements from the front while `pred` holds; stops at the first non-matching element |

### Fold

#### Definitions

> **Fold**: The most general list combinator. It walks a list, combining each element into an accumulator with a given function.

> **Accumulator (`acc`)**: The running result carried from one step to the next.

Some tasks don't fit `zip`, `filter`, `map` or the other combinators. For example, greet everyone in a list in one paragraph:

```haskell
names = ["Tshepo", "Tafadzwa", "Tom"]
-- want "Hello, Tshepo, Tafadzwa, Tom, and everyone else!"
```

Fold takes three arguments:

1. the operation `f`,
2. the initial accumulator `acc`,
3. the data to fold over.

For each element it computes `f acc elt` and uses the result as the next accumulator — the recurrence $acc' = f(acc, elt)$.

```haskell
(foldl (\acc elt -> acc ++ elt ++ ", ") "Hello, " names)
    ++ "and everyone else!"
-- "Hello, Tshepo, Tafadzwa, Tom, and everyone else!"
```

Product of a list:

```haskell
ns = [5, 10, 2, 3]
foldl (*) 1 ns   -- 300
```

### Left Versus Right Folds

`foldl (*) 1 ns` computes $1 \times 5 \times 10 \times 2 \times 3 = 300$, but in what order?

| Fold | Associativity | Product example |
|---|---|---|
| `foldl` ("L" = left) | Left-associative | $(((1 \times 5) \times 10) \times 2) \times 3$ |
| `foldr` | Right-associative | $5 \times (10 \times (2 \times (3 \times 1)))$ |

![foldl versus foldr](../../../diagrams/CSC3003S-Advanced%20Programming/FP/07_Working_With_Lists_And_Lambdas/fold-trees.svg)

*`foldl` nests to the left starting from the accumulator; `foldr` nests to the right, ending with the accumulator.*

The order matters for operators that are not associative and commutative, such as subtraction:

$$
\texttt{foldl (-) 1 [5,10,2,3]} = (((1 - 5) - 10) - 2) - 3 = -19
$$

$$
\texttt{foldr (-) 1 [5,10,2,3]} = 5 - (10 - (2 - (3 - 1))) = 5 - (10 - 0) = -5
$$

`foldl'` (the strict left fold) is covered in [Recursion And Lazy Evaluation](09_Recursion_And_Lazy_Evaluation.md).

### Fold Is The Universal List Combinator

Fold can implement every other list combinator because it is so general. It is FP's analogue of a `for` loop with state:

```python
greeting = "Hello, "
for name in names:
    greeting += name + ", "
greeting += "and everyone else"
```

The difference: instead of mutating the accumulator (`greeting`), fold creates a new copy and passes it forward for each element.

The lecture exercise proves this by re-implementing `sum`, `map` and `filter` with `foldl`:

```haskell
sum' :: [Int] -> Int
sum' xs = foldl (+) 0 xs

map' :: (a -> b) -> [a] -> [b]
map' f xs = foldl (\acc x -> acc ++ [f x]) [] xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' p xs = foldl (\acc x -> if p x then acc ++ [x] else acc) [] xs
```

### Sequence Comprehensions

#### Definitions

> **Comprehension**: An expression that builds a sequence from generators and guards, like set-builder notation in maths.

> **Generator**: The `x <- list` part of a comprehension, which draws values from a list.

> **Guard**: A Boolean condition in a comprehension; only values satisfying it are kept.

The set of positive even integers in maths:

$$
E = \{\, 2x \mid x \in \mathbb{N} \,\}
$$

"Take every positive integer $x$ and double it." In Haskell:

```haskell
e = [2 * x | x <- [1..]]   -- x <- [1..] is a generator
take 3 e                   -- [2, 4, 6]
```

Comprehensions are an alternative to `map` and `filter`:

```haskell
-- type signatures are optional if they can be inferred
factorise  n = filter (\f -> n `mod` f == 0) [1..n]
factorise' n = [f | f <- [1..n], n `mod` f == 0]   -- n `mod` f == 0 is a guard
```

Mapping a list of strings to their lengths: `[length s | s <- strings]`, which equals `map length strings`.

### Multiple Generators

Several generators give the **Cartesian product** of the inputs — every combination, like a nested `for` loop. This is **not** the same as `zip`, which pairs elements position by position.

```haskell
suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

-- deck without jokers, aces or royalty
regularCards = [(n, suit) | suit <- suits, n <- [2..10]]

take 3 regularCards
-- [(2,"Clubs"), (3,"Clubs"), (4,"Clubs")]
take 3 $ drop 9 regularCards
-- [(2,"Hearts"), (3,"Hearts"), (4,"Hearts")]
```

Order matters: the **later** generator varies fastest, like an inner loop. Swapping them (`n <- [2..10], suit <- suits`) gives `(2,"Clubs"), (2,"Hearts"), (2,"Spades"), (2,"Diamonds"), (3,"Clubs"), …`.

### Dependent Generators

A generator can depend on an earlier generator's variable (only earlier ones, since it must already be bound).

Coordinates of the 1s in a $3 \times 3$ lower-triangular matrix:

```haskell
[(x, y) | x <- [1..3], y <- [1..x]]
-- [(1,1),
--  (2,1), (2,2),
--  (3,1), (3,2), (3,3)]
```

Flattening a list of lists uses the same idea:

```haskell
flatten :: [[a]] -> [a]
flatten xss = [x | xs <- xss, x <- xs]
-- flatten [[1, 2], [3, 4], [5]] == [1, 2, 3, 4, 5]
```

### String Comprehensions

A string is just a list of characters, so `map`, `filter`, `fold` and comprehensions all work on it:

```haskell
import Data.Char

[toUpper c | c <- "hello"]   -- "HELLO"
```

Assigned reading (LYAH): "I'm a list comprehension", "An intro to lists"; in preparation: the whole *Types and Typeclasses* and *Syntax in Functions* chapters.
