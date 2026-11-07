---
tags:
  - advanced-programming
---

# Monads

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-12-Haskell 8-Monads-2.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-12-Haskell%208-Monads-2.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–37
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> What `Maybe`, lists and `IO` have in common: bind (`>>=`) as flat-map, the monad operations (`pure`, `fmap`/`<$>`, `<*>`, `>>`), monads as effect systems, the `IO` monad, and `do` notation.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Maybe: Propagating Failure|Maybe: Propagating Failure]]
  - [[#Flat-Map, Bind And >>=|Flat-Map, Bind And >>=]]
  - [[#Bind On Lists|Bind On Lists]]
  - [[#The Monad Typeclass And Its Operations|The Monad Typeclass And Its Operations]]
  - [[#A Closer Look At <*>|A Closer Look At <*>]]
  - [[#Monads As Effect Systems|Monads As Effect Systems]]
  - [[#Tracking Effects: CounterMonad And DummyIO|Tracking Effects: CounterMonad And DummyIO]]
  - [[#The IO Monad|The IO Monad]]
  - [[#>> And *>: Discarding Results|>> And *>: Discarding Results]]
  - [[#do Notation|do Notation]]
  - [[#Beyond The Course And A Result Monad|Beyond The Course And A Result Monad]]

---

## Core Content

### Maybe: Propagating Failure

Recall:

```haskell
data Maybe a = Nothing | Just a
```

`Maybe` represents something that may or may not be there. Suppose you want to fetch a cat picture from the internet. Every step can fail:

| Step | Fails if |
|---|---|
| 1. Search Google for "cat" | eduroam is broken |
| 2. Get the first link | There are no results |
| 3. Load the page at that link | The link gives a 404 |
| 4. Find the first `<img>` tag | There is no `<img>` |
| 5. Download the image's `src` | The `src` gives a 404 |
| 6. Save it to disk | There is no disk space |

We want to express the whole process while handling failure **gracefully** at every point: no crash, just a final result of `Nothing`.

Handling it by hand is long and annoying:

```haskell
searchCat :: Maybe String
searchCat = firstResult $ searchGoogle "cat"
  where
    firstResult (Just (link:links)) = Just link
    firstResult (Just [])           = Nothing
    firstResult Nothing             = Nothing
```

`listToMaybe :: [a] -> Maybe a` (from `Data.Maybe`) returns `Just` the first element of a list, or `Nothing` if it is empty — a **safe `head`**. It merges two patterns:

```haskell
import Data.Maybe

searchCat :: Maybe String
searchCat = firstResult $ searchGoogle "cat"
  where
    firstResult (Just links) = listToMaybe links
    firstResult Nothing      = Nothing
```

Better, but still a pattern per step. What we want is like `map` — apply a function to the value inside the structure — plus a **flatten**. Mapping `listToMaybe` over a `Maybe [String]` would give `Maybe (Maybe String)`; we want to collapse `Just (Just "cats.com")` into `Just "cats.com"`.

### Flat-Map, Bind And >>=

#### Definitions

> **Bind (`>>=`, flat-map)**: Applies a function that returns a wrapped value to the value inside a wrapper, then flattens the result into a single layer.

```haskell
searchCat :: Maybe String
searchCat = searchGoogle "cat" >>= listToMaybe
```

Compare the signatures:

```haskell
(>>=) :: Maybe a -> (a -> Maybe b) -> Maybe b
fmap  :: (a -> b) -> Maybe a -> Maybe b
```

With `fmap` the function returns a plain `b`. With `>>=` the function itself returns a `Maybe b`, and bind merges the two layers — that is the "flattening".

The whole pipeline now reads cleanly. If any step fails, everything stops early with `Nothing`, with no manual handling:

```haskell
searchGoogle "cat"            -- 1. Search "cat" on Google
  >>= listToMaybe             -- 2. Get first link
  >>= loadWebpage             -- 3. Load webpage at first link
  >>= getImgs >>= listToMaybe -- 4. Get first <img>
  >>= downloadImg             -- 5. Download img at src
  >>= saveToDisk              -- 6. Save to disk
```

![Bind chain short-circuits](../../../diagrams/CSC3003S-Advanced%20Programming/FP/12_Monads/bind-chain.svg)

*Each `>>=` passes a `Just` value to the next step; the first `Nothing` skips every remaining step.*

### Bind On Lists

`>>=` flat-maps `Maybe` by collapsing `Just (Just x)` into `Just x`. On lists, it maps a list-returning function over the list, then concatenates:

```haskell
[1, 2, 3] >>= (\n -> [1..n])
```

1. Map: `[[1], [1, 2], [1, 2, 3]]`
2. Flatten: `[1, 1, 2, 1, 2, 3]`

![Bind on lists](../../../diagrams/CSC3003S-Advanced%20Programming/FP/12_Monads/list-bind.svg)

*List bind is map followed by flatten (concatenation).*

### The Monad Typeclass And Its Operations

#### Definitions

> **Monad**: The typeclass of types that support `>>=` (and `pure`). Lists, `Maybe` and `IO` are all monads.

Because `>>=` works for both lists and `Maybe`, it must be a generic function, and both types must implement a common typeclass: `Monad`. Monads offer much more than flat-map:

| Operation | Meaning | Example |
|---|---|---|
| `pure x` | Wrap a value in the monad | `pure x = [x]` (list), `pure x = Just x` (`Maybe`) |
| `fmap fn mon` | Apply a function to the inside of the monad; for lists it is exactly `map` | `fmap (*2) [1,2] = [2,4]` |
| `<$>` | Infix `fmap` | `(*2) <$> myList = map (*2) myList` |
| `<*>` | Apply a **wrapped** function to a wrapped value; sequences computations and curries functions in monads | `(*) <$> Just 1 <*> Just 3 = Just (1 * 3)` |
| `>>=` | Bind / flat-map | see above |

The lecture also promises to explain why "a monad is like a burrito": a value wrapped up with extra structure around it.

### A Closer Look At <*>

```haskell
(<*>) :: Applicative f => f (a -> b) -> f a -> f b
```

`<*>` takes the function inside the wrapper and applies it to the value in another wrapper, giving a new wrapped value. It is like `fmap`/`<$>` for when the function is itself wrapped in `Maybe` or a list.

It expresses currying inside monads:

```haskell
(*)                       :: Int -> Int -> Int
(*) <$> Just 1            :: Maybe (Int -> Int)
(*) <$> Just 1 <*> Just 3 :: Maybe Int        -- Just 3
```

#### Definitions

> **Functor**: A type supporting `fmap`.

> **Applicative**: A functor that also supports `pure` and `<*>`.

| Class | Adds | Relationship |
|---|---|---|
| Functor | `fmap` / `<$>` | — |
| Applicative | `pure`, `<*>`, `*>` | Every Applicative is a Functor |
| Monad | `>>=`, `>>` | Every Monad is an Applicative, but not every Applicative is a Monad |

### Monads As Effect Systems

#### Definitions

> **Effect**: A change to the **structure** around a value (failing, producing several values, doing IO), as opposed to a change to the value itself.

Could the cat pipeline be written with just `fmap`? **No.** Its signature only lets you change what is **inside** the structure:

```haskell
fmap :: Functor f => (a -> b) -> f a -> f b
fmap :: (a -> b) -> Maybe a -> Maybe b      -- specialised to Maybe
```

At no point can `fmap` say "something broke — abandon ship!". Bind can, because the mapping function itself returns a monad, which is then combined (flattened) with the original:

```haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b
```

The same holds for lists. Can `fmap` add or remove elements?

```haskell
fmap :: (Int -> Int) -> [Int] -> [Int]
```

No: each element maps to exactly one element, so the length is fixed. With bind, the function can return zero, one or many elements, so it can change the structure:

```haskell
filter f xs = xs >>= (\x -> if f x then [x] else [])
repeat2 xs  = xs >>= (\x -> [x, x])
```

In both cases we affect the structure itself — that is an **effect**.

| Monad | Higher information ("metadata") it carries |
|---|---|
| `Maybe` | Whether a value is present |
| List | That there are multiple values |
| `IO` | Whether (and what) I/O is performed |

- Values change only with `fmap`.
- The monad's structure can change with `>>=` (bind / flat-map).

### Tracking Effects: CounterMonad And DummyIO

Monads can track effects directly. This one counts how many times `inc` has been called:

```haskell
data CounterMonad a = Count Int a deriving Show

instance Monad CounterMonad where
    Count times val >>= f = Count (times + times') val'
      where Count times' val' = f val

instance Applicative CounterMonad where
    pure = Count 0
    Count times f <*> Count times' val = Count (times + times') (f val)

instance Functor CounterMonad where
    fmap f (Count times val) = Count times (f val)

inc = Count 1 ()

x   = Count 0 "Hi"                              -- Count 0 "Hi"
x'  = (++ " there") <$> x                       -- Count 0 "Hi there"
x'' = x' *> inc                                 -- Count 1 ()
y   = (++ " there") <$> x <* inc <* inc <* inc  -- Count 3 "Hi there"
```

`<*` and `*>` sequence two computations and keep the value on the arrow's side, while combining both structures (here, adding the counts).

Because we define the monad and its interface (`<$>`/`fmap`, `<*>`, `>>=`), we act as **gatekeeper**: every call to `inc` passes through us and can be logged. This is how `IO` works — the compiler uses the `IO` monad to gatekeep IO actions. Imagine replacing `inc` with something that tells GHC to actually perform IO.

A `DummyIO` monad that records IO instructions instead of performing them:

```haskell
data Action = Print String
            | Write  { fname :: String, text :: String }
            | Delete { fname :: String } deriving Show

data DummyIO a = Dummy [Action] a deriving Show

instance Monad DummyIO where
    Dummy actions val >>= f = Dummy (actions ++ actions') val'
      where Dummy actions' val' = f val
-- Applicative and Functor instances left as an exercise

x = Dummy [] "Hi"

done = do
    x' <- x
    let out = x' ++ " there"
    print' out
    delete "somefile.txt"
    write "out.txt" out
    pure out
-- Dummy [ Print "Hi there"
--       , Delete {fname = "somefile.txt"}
--       , Write {fname = "out.txt", text = "Hi there"}
--       ] "Hi there"
```

### The IO Monad

Suppose `getLine` reads a line from the terminal (like Python's `input()`):

```haskell
getLine :: String   -- wrong!
```

With this type, Haskell would assume `getLine` is pure and could replace any call with its value. That breaks: two calls may return different input, so each call **must** run again.

The fix is to wrap the result in the `IO` monad:

```haskell
getLine :: IO String
```

- `IO`'s higher structure tracks the IO actions performed, just as `Maybe` tracks presence and lists track multiplicity.
- It tells the compiler the function is **not** pure and can't be replaced by its value.

In `IO`, `>>=` does the same as elsewhere: it maps the value and **merges the structure** — here, it merges the IO the next function performs into the same `IO` value.

```haskell
putStrLn "Enter name" >>= \_ -> getLine >>= putStrLn . ("Hello, " ++)
```

The `()` inside `putStrLn`'s `IO ()` is thrown away and replaced by `getLine`'s `IO String`, but the printing effect is **merged in**. The value was discarded, yet its effect on the structure remained.

### >> And *>: Discarding Results

#### Definitions

> **`>>`**: Sequences two monadic actions, merging their structure but discarding the first's value. `m >> k = m >>= \_ -> k`.

```haskell
x :: IO () = putStrLn "Hi"

x >>= (\_ -> putStrLn "There")
-- is the same as
x >> putStrLn "There"
```

`>>` is the same as `*>`, but `*>` is more general: it comes from Applicative, and every Monad is an Applicative.

### do Notation

#### Definitions

> **`do` notation**: Syntactic sugar for chains of `>>=` and `>>`. Any `do` block can be rewritten with `>>=`.

```haskell
greet :: IO String
greet = do
    putStrLn "What is your name?"
    name <- getLine
    let greeting = "Hello, " ++ name ++ "!"
    putStrLn greeting
    pure name

greet >>= putStrLn . ("Return value was " ++)
```

Rules:

1. Every statement must be one of:
   - a `let`,
   - a `name <- expr`,
   - a monadic value (an instance of the monad).
2. `<-` **unwraps** the monad (e.g. gets the `String` out of `IO String`).
3. `let` makes temporary variables.
4. `pure` **wraps** a value into the monad.

The same function desugared:

```haskell
greet = putStrLn "What is your name?" >>
        getLine >>= \name ->
        let greeting = "Hello, " ++ name ++ "!"
        in putStrLn greeting >> pure name
```

`do` notation is the closest Haskell gets to imperative code, but it differs:

| Statement | Behaviour |
|---|---|
| `let x = x + 2` | Does **not** modify `x`; it defines `x` recursively in terms of itself and loops forever |
| `x <- action` | Binds a new `x` (shadowing the old one), which behaves as you'd expect |
| Any other line | Must be a monadic value |

### Beyond The Course And A Result Monad

Useful but **not examinable**:

- **MonadPlus**: monads with a default empty value (`Maybe`, list, `IO`); they can be filtered with a general function.
- **MonadFail**: monads with failure states. Fallible patterns can appear on the left of `<-` in a `do` block; when a match fails the block ends early, with the failure combined into the monad's structure.
- More Applicative/Monad operators: `<$`, `$>`, `<*`, `*>`, `&`, `>>>` (`>>` is in scope; `>>>` is something else).
- The precise differences between Functors, Applicatives and Monads.

The lecture's longer exercise builds a monad for computations that might fail with an error value, like `Maybe` but keeping the error:

```haskell
data Result e v = Ok v | Err e

instance Functor (Result e) where
    fmap f (Ok v)  = Ok (f v)
    fmap _ (Err e) = Err e

instance Applicative (Result e) where
    pure = Ok
    Ok f  <*> r = fmap f r
    Err e <*> _ = Err e

instance Monad (Result e) where
    Ok v  >>= f = f v
    Err e >>= _ = Err e

throw :: e -> Result e v
throw = Err

orErr :: Maybe v -> e -> Result e v
orErr (Just v) _ = Ok v
orErr Nothing  e = Err e

-- Validate a name (at least 5 characters) and parse an age
register :: String -> String -> Result String (String, Int)
register name ageStr = do
    if length name < 5 then throw "name too short" else pure ()
    age <- readMaybe ageStr `orErr` "age is not a number"
    pure (name, age)
```

`readMaybe` comes from `Text.Read`. Readings: haskell.org's "A Gentle Introduction to Haskell: Monads" and HaskellWiki's "Merely monadic".
