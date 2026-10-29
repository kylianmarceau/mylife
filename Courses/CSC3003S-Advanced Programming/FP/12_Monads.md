---
tags:
  - advanced-programming
---

# Haskell 8 — Monads

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-12-Haskell 8-Monads-2.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-12-Haskell%208-Monads-2.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–37  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: `Maybe` failure propagation, bind (`>>=`), monads on lists, `pure`/`fmap`/`<*>`, monads as effect systems, the IO monad, `>>`, and `do` notation.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Maybe: Propagating Failure|Maybe: Propagating Failure]]
  - [[#Flat-Map, Bind, >>=|Flat-Map, Bind, >>=]]
  - [[#Bind For Lists|Bind For Lists]]
  - [[#Generalising: The Monad Typeclass|Generalising: The Monad Typeclass]]
  - [[#pure, fmap, <$> And <*>|pure, fmap, <$> And <*>]]
  - [[#Monads As Effect Systems|Monads As Effect Systems]]
  - [[#Tracking Effects: CounterMonad And DummyIO|Tracking Effects: CounterMonad And DummyIO]]
  - [[#The IO Monad|The IO Monad]]
  - [[#>> And *>: Throwing Away Results|>> And *>: Throwing Away Results]]
  - [[#do Notation|do Notation]]
  - [[#Not Examinable Extras|Not Examinable Extras]]

---

## Core Content

### Maybe: Propagating Failure

```haskell
data Maybe a = Nothing | Just a
```

To fetch a cat picture from the internet, every step can fail:

| Step | Fails if… |
|---|---|
| 1. Search Google for "cat" | eduroam is broken |
| 2. Get the first link | No results |
| 3. Load the webpage at that link | Link gives 404 |
| 4. Find the first `<img>` tag | No `<img>` tag |
| 5. Download that image's `src` | `src` gives 404 |
| 6. Save it to disk | No disk space |

"Gracefully" handling failure means not crashing: the final result should simply be `Nothing`. Handling each step by hand is long and inelegant:

```haskell
searchCat :: Maybe String
searchCat = firstResult $ searchGoogle "cat"
    where
  firstResult (Just (link:links)) = Just link
  firstResult (Just [])           = Nothing
  firstResult Nothing             = Nothing
```

`listToMaybe :: [a] -> Maybe a` returns `Just` the first element if there is one, else `Nothing`. It is a safe `head`; plain `head` crashes on `[]`. It removes one pattern:

```haskell
import Data.Maybe
searchCat = firstResult $ searchGoogle "cat"
    where
  firstResult (Just links) = listToMaybe links
  firstResult Nothing      = Nothing
```

There are still two patterns. What we want is like `map`: apply a function to the value inside the structure. But mapping `listToMaybe` over a `Maybe [String]` gives `Maybe (Maybe String)`, so we also want to **flatten** `Just (Just "cats.com")` to `Just "cats.com"`.

### Flat-Map, Bind, >>=

#### Definitions

> **Bind (`>>=`, flat-map)**: Applies a function that returns a wrapped value to the contents of a wrapped value, then flattens the result.

```haskell
(>>=) :: Maybe a -> (a -> Maybe b) -> Maybe b
fmap  :: (a -> b) -> Maybe a -> Maybe b

searchCat :: Maybe String
searchCat = searchGoogle "cat" >>= listToMaybe
```

The mapper passed to `>>=` already returns `Maybe b`, so there is no double wrapping. The whole pipeline becomes:

```haskell
searchGoogle "cat"            -- 1. Search "cat" on Google
  >>= listToMaybe             -- 2. Get first link
  >>= loadWebpage             -- 3. Load webpage at first link
  >>= getImgs >>= listToMaybe -- 4. Get first <img>
  >>= downloadImg             -- 5. Download img at <src>
  >>= saveToDisk              -- 6. Save to disk
```

![Bind chain short-circuits](../../../diagrams/CSC3003S-Advanced%20Programming/FP/12_Monads/bind-chain.svg)

*Each `Just` result feeds the next step. The first `Nothing` stops the whole chain early, with no manual checks.*

### Bind For Lists

For `Maybe`, `>>=` collapses `Just (Just x)` into `Just x`. For lists it maps and then concatenates:

```haskell
[1, 2, 3] >>= (\n -> [1..n])
-- map:     [[1], [1, 2], [1, 2, 3]]
-- flatten: [1, 1, 2, 1, 2, 3]
```

![List bind is map then flatten](../../../diagrams/CSC3003S-Advanced%20Programming/FP/12_Monads/list-bind.svg)

*`>>=` on lists maps each element to a list, then flattens. Unlike `fmap`, it can change the structure.*

### Generalising: The Monad Typeclass

#### Definitions

> **Monad**: The typeclass of types supporting `>>=` (plus `pure`). `List`, `Maybe` and `IO` are all monads.

`>>=` works on both lists and `Maybe`, so from the polymorphism lecture it must be a generic function of a typeclass both types implement. That typeclass is `Monad`. The lecture's joke: a monad is like a burrito, a value wrapped in extra structure.

### pure, fmap, <$> And <*>

| Operation | Meaning | Example |
|---|---|---|
| `pure` | Wrap a value in the monad | `pure x = [x]` (list); `pure x = Just x` (Maybe) |
| `fmap fn mon` | Apply a function to the inside | For lists, exactly `map` |
| `<$>` | Infix `fmap` | `(*2) <$> myList = map (*2) myList` |
| `<*>` | Apply a **wrapped** function to a wrapped value | `(*) <$> Just 1 <*> Just 3 = Just (1 * 3)` |

```haskell
(<*>) :: Applicative f => f (a -> b) -> f a -> f b
```

`<*>` is `fmap` for when the function itself is wrapped. It expresses currying inside monads:

```haskell
(*)                       :: Int -> Int -> Int
(*) <$> Just 1            :: Maybe (Int -> Int)
(*) <$> Just 1 <*> Just 3 :: Maybe Int
```

#### Definitions

> **Functor**: A type supporting `fmap`.

> **Applicative**: A Functor supporting `pure` and `<*>`. Every Monad is an Applicative, but not every Applicative is a Monad.

The slide says "Applicative is a subclass of Monad". The hierarchy is the other way round: Monad is a subclass of Applicative, which matches the slide's own "every Monad is Applicative".

| Typeclass | Key operation | Can do |
|---|---|---|
| Functor | `fmap :: (a -> b) -> f a -> f b` | Change values inside |
| Applicative | `<*> :: f (a -> b) -> f a -> f b` | Combine wrapped values and functions |
| Monad | `>>= :: m a -> (a -> m b) -> m b` | Let a step decide the resulting structure |

### Monads As Effect Systems

#### Definitions

> **Effect**: A change to the structure itself (the wrapper's "higher information") rather than just to the values inside.

Could the cat pipeline be written with only `fmap`? **No.** `fmap :: (a -> b) -> Maybe a -> Maybe b` only changes what is inside. It can never say "something broke, abandon ship".

`>>=` can change the structure because the mapping function returns a monad, which is merged (flattened) with the original:

```haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b
```

The slide prints this signature as `(a -> f b) -> f a -> f b`, mixing up the argument order and type variable. The standard signature is above.

On lists, `fmap :: (Int -> Int) -> [Int] -> [Int]` always returns exactly one `Int` per input, so the length cannot change. `>>=` can add or remove elements:

```haskell
filter f xs = xs >>= (\x -> if f x then [x] else [])
repeat2 xs  = xs >>= (\x -> [x, x])
```

Both affect the structure itself. That is an effect.

### Tracking Effects: CounterMonad And DummyIO

A monad can track effects directly. This one counts calls to `inc`:

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
x  = Count 0 "Hi"                               -- Count 0 "Hi"
x' = (++ " there") <$> x <* inc <* inc <* inc   -- Count 3 "Hi there"
```

- `<*` sequences effects but keeps the **left** value; `*>` keeps the **right**.
- `(++ " there") <$> x` alone gives `Count 0 "Hi there"`.
- The slide says `x *> inc` returns `Count 1 "Hi there"`. Since `*>` keeps the right value, it actually gives `Count 1 ()`; `x' <* inc` would give `Count 1 "Hi there"`.

Because we defined the interfaces (`fmap`, `<*>`, `>>=`), we act as **gatekeeper** and see every `inc`. IO works the same way: GHC uses the IO monad to gatekeep IO actions.

A `DummyIO` monad records instructions instead of performing IO:

```haskell
data Action = Print String
            | Write  { fname :: String, text :: String }
            | Delete { fname :: String } deriving Show

data DummyIO a = Dummy [Action] a deriving Show

instance Monad DummyIO where
    Dummy actions val >>= f = dummy'
      where Dummy actions' val' = f val
            dummy' = Dummy (actions ++ actions') val'
-- Applicative and Functor instances left for the reader

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
--       , Write {fname = "out.txt", text = "Hi there"} ] "Hi there"
```

In summary:

- Monads wrap values but carry **higher information** (like metadata). `Maybe` carries presence or absence; `List` carries "multiple values".
- `fmap` changes only the values.
- `>>=` (bind, flat-map) can also change the structure.
- Whether a function **does I/O** is exactly this kind of higher information.

### The IO Monad

A function to read a terminal line (like Python's `input()`) cannot be typed `getLine :: String`. GHC would treat it as pure and substitute its value. But two calls can return different input, so it must run each time.

```haskell
getLine :: IO String
```

`IO` is a monad whose structure tracks the IO actions performed. The type also tells the compiler the function is not pure and cannot be replaced by its value.

`>>=` in IO maps the value and merges the IO effects:

```haskell
putStrLn "Enter name" >>= \_ -> getLine >>= putStrLn . ("Hello, " ++)
```

The `()` inside `putStrLn`'s `IO ()` is thrown away and replaced by `getLine`'s `IO String`. But the printing effect is merged in: the value was discarded, but the effect on the structure remained.

### >> And *>: Throwing Away Results

#### Definitions

> **`>>`**: Sequences two monadic values, merging structure and replacing the value without using the old one as input. It is the same as `*>`, which is more general (from Applicative).

```haskell
x :: IO () = putStrLn "Hi"
x >>= (\_ -> putStrLn "There")
-- is the same as
x >> putStrLn "There"
```

### do Notation

#### Definitions

> **do notation**: Syntactic sugar for chains of `>>=`. Any `do` block can be written with `>>=`.

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

The rules:

1. Every statement must be a `let`, a `<-` expression, or a value of the monad.
2. `<-` **unwraps** the monad, e.g. takes the `String` out of `IO String`.
3. `let` makes temporary variables.
4. `pure` **wraps** a value into the monad.

Desugared, the block above is roughly:

```haskell
putStrLn "What is your name?" >>
getLine >>= \name ->
let greeting = "Hello, " ++ name ++ "!" in
putStrLn greeting >>
pure name
```

`do` is the closest Haskell gets to imperative code, but it is still different:

- You cannot modify variables with `let`. `let x = x + 2` loops forever, because it defines `x` recursively in terms of itself.
- Rebinding with `<-` works as you might expect: each `<-` introduces a new binding that shadows the old one.

The lecture exercise defines a `Result` monad:

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
```

The slide's `throw` and `orErr` types write the parameters as `Result v e`. They are written here to match `data Result e v`.

### Not Examinable Extras

- **MonadPlus**: monads with default/empty values (`Maybe`, `List`, `IO`) that can be filtered generally.
- **MonadFail**: monads with failure states. A failing pattern in a `do`-block `<-` ends the block early.
- Other operators: `<$`, `$>`, `<*`, `*>`, `&`, `>>>`. `>>>` is different from `>>`.
- The precise differences between Functors, Applicatives and Monads.
