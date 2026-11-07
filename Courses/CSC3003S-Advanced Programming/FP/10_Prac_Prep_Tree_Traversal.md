---
tags:
  - advanced-programming
---

# Practical Preparation: Tree Traversal

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-10-Haskell 6 - Prac prep (tree traversal)-1.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-10-Haskell%206%20-%20Prac%20prep%20%28tree%20traversal%29-1.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, pages 1–39
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Function composition, then the "dog in the wizard's dungeon" problem: modelling a tree in Haskell, solving it by divide and conquer, ranking results with custom `Eq`/`Ord` instances, and the format of the practical.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Engagement Warning|Engagement Warning]]
  - [[#Function Composition|Function Composition]]
  - [[#The Dungeon Problem|The Dungeon Problem]]
  - [[#Modelling The Dungeon In Haskell|Modelling The Dungeon In Haskell]]
  - [[#Divide-And-Conquer Strategy|Divide-And-Conquer Strategy]]
  - [[#Fighting A Monster|Fighting A Monster]]
  - [[#Worked Example On A Small Dungeon|Worked Example On A Small Dungeon]]
  - [[#Ranking Results With Eq And Ord|Ranking Results With Eq And Ord]]
  - [[#Visiting One Room (Conquer)|Visiting One Room (Conquer)]]
  - [[#Choosing Among Child Rooms (Divide)|Choosing Among Child Rooms (Divide)]]
  - [[#fmap And uncurry|fmap And uncurry]]
  - [[#Putting It Together: crawl|Putting It Together: crawl]]
  - [[#Practical Format And Sample Test|Practical Format And Sample Test]]

---

## Core Content

### Engagement Warning

The test and practical are set at a fair level and won't be hard **if you engage and practise** — but you will certainly fail if you don't practise Haskell. Most students weren't doing the daily exercises or attending, and fewer than 300 of 429 had opened the first lecture PDF.

### Function Composition

#### Definitions

> **Function composition**: Defining a function as a combination of other functions, without mentioning the data it acts on.

> **Compose operator (`.`)**: $f . g = \lambda x \to f\,(g\,x)$, so $(f . g)\,x = f\,(g\,x)$.

Haskell's functions are first-class and its function definitions are expressive. Composition lets you think about the **mapping** you want rather than how data is shuffled around — about the functions themselves, not the values going in and out.

**Example**: the magnitude (length) of a vector, e.g. the distance from $(1, 2)$ to $(0, 0)$:

$$
\lVert \mathbf{x} \rVert = \sqrt{\sum_i x_i^2}
$$

```haskell
magnitude :: [Float] -> Float

-- applying functions to the data
magnitude xs = sqrt $ sum $ map (^2) xs

-- as a composition of functions
magnitude = sqrt . sum . map (^2)
```

![Function composition](../../../diagrams/CSC3003S-Advanced%20Programming/FP/10_Prac_Prep_Tree_Traversal/composition.svg)

*`sqrt . sum . map (^2)` is one function built by chaining three; data flows right to left.*

Composing functions with several arguments with `.` is possible but far from trivial. (The lecturer's example `flip flip 2 . ((^) .) . (-)` is famously hard to read.)

Quiz: a valid inferred type for `sum . (map (+2))` is `Num a => [a] -> a`, and a lambda is an anonymous function.

### The Dungeon Problem

An evil (but fair) wizard has locked the class dog in his dungeon maze. Send him a Haskell program that guides the dog through, and she'll be returned.

A dungeon is like a maze whose rooms contain hazards (as in tabletop role-playing games such as D&D, Pathfinder or Dungeon Crawl Classics). The wizard promises:

| Promise | Consequence |
|---|---|
| Each room connects to 0–2 **child rooms** | The dungeon is a graph |
| There are no cycles; each room is reachable by only one path | It is an acyclic graph |
| Every room is reachable from the start room (no hidden rooms) | It is a **tree** |

Each room contains one of:

- nothing (empty),
- a monster,
- a health potion that helps the dog recover from fights,
- the exit, which the dog must reach.

**Goal**: calculate the best possible outcome for the dog by taking the best route. You don't need to record which turns were taken — only where the dog is, where it has been, and its current attributes.

### Modelling The Dungeon In Haskell

```haskell
-- A room has contents and may branch into 0, 1 or 2 rooms.
-- No cycles, so Room is a tree data structure.
data Room = Room RoomContents
                 (Maybe Room) (Maybe Room)
                 deriving Show

data RoomContents = Fight Monster
                  | Heal Int
                  | Empty
                  | Escape
                  deriving Show

-- Our dog :)
data Dog = Dog
  { dhp  :: Int   -- health points
  , ddmg :: Int   -- damage per hit
  } deriving Show

-- A monster! :o
data Monster = Monster
  { mhp  :: Int
  , mdmg :: Int
  } deriving Show

-- The result of the dog entering a room:
-- 1. Victory: escape
-- 2. Death: die
-- 3. Continue: alive, but not free yet
data VisitResult = Victory
                 | Death
                 | Continue Dog
                 deriving Show

-- The solution: the result of the dog visiting a room AND its child rooms
crawl :: Dog -> Room -> VisitResult
```

`Maybe Room` encodes "there may or may not be a child here", and `RoomContents` and `VisitResult` are sum types.

### Divide-And-Conquer Strategy

This is divide and conquer, as in TOA ([Divide And Conquer](../TOA/05_Divide_And_Conquer.md)):

- **Subproblem**: each subtree.
- **Combine**: decide which child rooms to visit and keep only the best results.

![Dungeon tree and results](../../../diagrams/CSC3003S-Advanced%20Programming/FP/10_Prac_Prep_Tree_Traversal/dungeon-tree.svg)

*Each subtree is solved independently; at every room the best of the possible routes is passed up to its parent.*

### Fighting A Monster

```haskell
-- The result of our dog fighting a monster
fight :: Dog -> Monster -> VisitResult
fight dog mon
  | dhp dog <= 0 = Death
  | mhp mon <= 0 = Continue dog
  | otherwise    = fight dog' mon'
  where
    dog' = dog { dhp = (dhp dog) - (mdmg mon) }
    mon' = mon { mhp = (mhp mon) - (ddmg dog) }
```

Each round, both sides deal damage at the same time. The fight recurses until one side's HP drops to 0 or below; the dog's death is checked first.

### Worked Example On A Small Dungeon

The dog starts as `Dog { dhp = 10, ddmg = 5 }`. The root has a left child (a skeleton, whose own right child is empty) and a right child (a healing room `Heal 10` leading to the exit).

1. **Root → left**: the dog fights the skeleton and survives as `Continue (Dog 5 5)`.
2. **Root → left → right**: an empty room; nothing changes, so the result is still `Continue (Dog 5 5)`.
3. Propagating up: the best of the left side is `Continue (Dog 5 5)`, which has less health than the starting dog. So the real choice is between going right or staying in the root room (slowly starving).
4. **Root → right**: the healing room gives `Dog 20 5`, then the exit gives `Victory`. (The quiz answer for this subtree is **Victory**.)
5. **At the root**, the options are:

| Option | Result |
|---|---|
| Stay | `Continue (Dog 10 5)` |
| Go left | `Continue (Dog 5 5)` |
| Go right | `Victory` |

The overall result is **Victory**. To pick it in code, we need a way to compare and rank `VisitResult`s.

### Ranking Results With Eq And Ord

#### Definitions

> **`Eq`**: The typeclass for equality (`==`).

> **`Ord`**: The typeclass for ordering (`<=`, `max`, …). It requires `Eq`: `class Eq a => Ord a`.

> **Pattern guard**: A guard of the form `| Pattern <- expr`, which succeeds if `expr` matches `Pattern` and binds its variables.

Implementing `Ord` therefore also requires `Eq`. The dog's damage never changes, and dogs from different dungeons are never compared, so only HP matters:

```haskell
instance Eq VisitResult where
    Victory      == Victory      = True
    Death        == Death        = True
    (Continue a) == (Continue b) = (dhp a) == (dhp b)
    _            == _            = False
```

`x <= y` is defined to mean "x is a **worse** result than y for the dog":

```haskell
instance Ord VisitResult where
    a <= b
      -- == implies <=, since <= means < or ==
      | a == b = True
      -- If both continue, the better one has more health
      | (Continue dog) <- a, (Continue dog') <- b = (dhp dog) <= (dhp dog')
      -- Death is worse than anything
      | Death <- a = True     -- Death <= anything
      | Death <- b = False    -- anything <= Death fails
      -- Victory is better than anything
      | Victory <- b = True   -- anything <= Victory
      | Victory <- a = False  -- Victory <= anything fails
```

| Ranking | Result |
|---|---|
| Worst | `Death` |
| Middle | `Continue dog`, ordered by `dhp` |
| Best | `Victory` |

### Visiting One Room (Conquer)

`visitRoom` handles every kind of room, ignoring the children for now (they're dealt with in `fork`, which keeps the code neat). This is the **conquer** part.

```haskell
visitRoom :: Dog -> RoomContents -> VisitResult
visitRoom dog room = go room
  where
    go (Fight monster) = fight dog monster
    go (Heal hp)       = Continue dog { dhp = (dhp dog) + hp }
    go Escape          = Victory
    go Empty           = Continue dog
```

### Choosing Among Child Rooms (Divide)

`fork` is the **divide** part: it tries every way of continuing from a room and returns the best.

```haskell
fork :: Dog -> Maybe Room -> Maybe Room -> VisitResult
fork dog leftRoom rightRoom = bestPath
  where
    -- The best path is the highest-scoring valid path
    bestPath   = maximum validPaths
    -- Nothing = an invalid path (e.g. going left when there is no left room);
    -- catMaybes keeps only the paths that can actually be taken
    validPaths = catMaybes
                   [leftFirst, rightFirst, leftOnly, rightOnly, Just $ Continue dog]
    leftFirst  = fmap (uncurry $ crawlBoth dog) (both leftRoom rightRoom)
    rightFirst = fmap (uncurry $ crawlBoth dog) (both rightRoom leftRoom)
    leftOnly   = fmap (crawl dog) leftRoom
    rightOnly  = fmap (crawl dog) rightRoom

-- Combine two Maybes: Just only when both are Just
both :: Maybe a -> Maybe b -> Maybe (a, b)
both (Just a) (Just b) = Just (a, b)
both _        _        = Nothing

-- Visit the first room (and its subtree) and THEN the second
crawlBoth :: Dog -> Room -> Room -> VisitResult
crawlBoth dog first second = case (crawl dog first) of
    Continue dog' -> crawl dog' second
    Victory       -> Victory
    Death         -> Death
```

The five candidate paths:

| Path | Meaning |
|---|---|
| `leftFirst` | Do the whole left subtree, then the right subtree |
| `rightFirst` | Do the right subtree, then the left |
| `leftOnly` | Only the left subtree |
| `rightOnly` | Only the right subtree |
| `Just $ Continue dog` | Stay put |

`maximum` uses the `Ord` instance to pick the best.

### fmap And uncurry

#### Definitions

> **`fmap`**: A generalisation of `map`. On `Maybe` it applies a function to the value inside a `Just` and leaves `Nothing` alone.

> **`uncurry`**: Turns a curried two-argument function into one that takes a pair.

```haskell
fmap f (Just x) = Just (f x)
fmap _ Nothing  = Nothing

uncurry f = \(a, b) -> f a b
(uncurry (+)) (1, 2) == (+) 1 2
```

So `fmap (uncurry $ crawlBoth dog) (both leftRoom rightRoom)` calls `crawlBoth dog left right` only if both rooms exist.

### Putting It Together: crawl

```haskell
-- The result of the dog visiting a room AND its children.
-- This solves the subtree rooted at the room, so calling it
-- on the root solves the whole dungeon.
crawl :: Dog -> Room -> VisitResult
crawl dog (Room this left right) = case (visitRoom dog this) of
    Continue dog' -> fork dog' left right
    Victory       -> Victory
    Death         -> Death
```

`crawl` and `crawlBoth` repeat the same `case` pattern. The lecture exercise factors it out:

```haskell
flatmapContinue :: (Dog -> VisitResult) -> VisitResult -> VisitResult
flatmapContinue f (Continue dog) = f dog
flatmapContinue _ Victory        = Victory
flatmapContinue _ Death          = Death

crawlBoth dog first second =
    flatmapContinue (\dog' -> crawl dog' second) $ crawl dog first

crawl dog (Room this left right) =
    flatmapContinue (\dog' -> fork dog' left right) $ visitRoom dog this
```

This "continue only on success" pattern is exactly what monads generalise (see [Monads](12_Monads.md)).

### Practical Format And Sample Test

The full base solution is provided (Amathuba: `Haskell - BaseGame.hs`). Each prac session has a different but equally difficult set of questions.

| Question | Format | Advice |
|---|---|---|
| 1 | Heavily scaffolded and incremental (1.2 builds on 1.1, …) | Lots of partial marks **as long as your code compiles**. Start from a blank `Q1Ans.hs` and slowly copy and modify code from the skeleton |
| 2 | Not scaffolded; usually builds on Question 1 | Partial marks for a basic solution, more for handling harder inputs; a perfect answer compiles and handles all cases. Submit in a **separate file** — copy Q1 forward, never the other way |

**Sample test**: the wizard also stole a pet rat. Fetch it if possible, but only if it costs the dog nothing: the net health of the best path that gets the rat must be $\ge$ the best path that doesn't.

Question 1 (scaffolded):

1. Implement a `Rat` type with a member `ratName :: String` (accessor `ratName :: Rat -> String`).
2. Add a member `rat :: Maybe Rat` to `Dog`.
3. Add a `RoomContents` variant `Cage` holding a `Rat`.
4. Change `Eq` for `Dog` so two dogs are equal only if both have rats.
5. Change `Ord` for `Dog` so that, at equal health, a dog without a rat is less than one with a rat: `(Dog 10 2 Nothing) <= (Dog 10 2 (Just (Rat "Jeremy")))`, but `(Dog 4 2 (Just (Rat "Jeremy"))) <= (Dog 10 2 Nothing)`.

Question 2 (unscaffolded): **all** your rats have been taken, at most one per room.

1. Change `Dog` to hold multiple rats (member `rats`).
2. Write `ratCount :: Dog -> Int`.
3. Change `Victory` to hold a `Dog`, to show how many rats were fetched.
4. Change `visitRoom` to pick up a rat in a rat room.
5. Change `Eq` and `Ord` so the best solution picks up the most rats, where one rat is worth 2 HP (10 HP with 5 rats beats 19 HP with none). Still avoid death.
