---
tags:
  - advanced-programming
---

# Haskell 6 — Practical Prep: Tree Traversal

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-10-Haskell 6 - Prac prep (tree traversal)-1.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-10-Haskell%206%20-%20Prac%20prep%20%28tree%20traversal%29-1.pdf), Cael Marquard (adapted from Dr Sabre Didi), University of Cape Town, PDF pages 1–39  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: function composition, then the dungeon-crawl prac base game (tree data types, divide and conquer, custom `Eq`/`Ord`, `fmap`, `uncurry`) and the prac format.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Function Composition|Function Composition]]
  - [[#The Dungeon Problem|The Dungeon Problem]]
  - [[#Modelling The Dungeon In Haskell|Modelling The Dungeon In Haskell]]
  - [[#Divide And Conquer Walkthrough|Divide And Conquer Walkthrough]]
  - [[#Fighting A Monster|Fighting A Monster]]
  - [[#Comparing Results: Eq And Ord Instances|Comparing Results: Eq And Ord Instances]]
  - [[#Solving One Room (Conquer)|Solving One Room (Conquer)]]
  - [[#Solving The Children (Divide)|Solving The Children (Divide)]]
  - [[#fmap And uncurry|fmap And uncurry]]
  - [[#Putting It Together: crawl|Putting It Together: crawl]]
  - [[#Prac Format And Sample Questions|Prac Format And Sample Questions]]

---

## Core Content

### Function Composition

#### Definitions

> **Function composition**: Defining a function purely as a combination of other functions, without mentioning the data.

> **`.` (compose)**: The function composition operator: `f . g = \x -> f (g x)`.

Functions are first-class, and Haskell is expressive in its types and in how functions are defined. Composition lets you think about the **mapping you want**, not how the data is shuffled around. Rather than picturing values passing through little machines one after another, think of the composed machine itself.

$$
(f \circ g)(x) = f(g(x))
$$

![Function composition](../../../diagrams/CSC3003S-Advanced%20Programming/FP/10_Prac_Prep_Tree_Traversal/composition.svg)

*Feeding $3$ through $f(x)=x^2$ then $g(x)=x+1$ gives $10$. The composed function `g . f` does the same in one step, applying the rightmost function first.*

The magnitude of a vector, e.g. the distance from $(1,2)$ to $(0,0)$:

$$
\lVert \mathbf{x}\rVert=\sqrt{\textstyle\sum_i x_i^2}
$$

```haskell
magnitude :: [Float] -> Float
magnitude xs = sqrt $ sum $ map (^2) xs   -- applied to data
magnitude    = sqrt . sum . map (^2)      -- as a composition
```

Composing multi-argument functions with `.` is not trivial. The lecturer's own example, `flip flip 2 . ((^) .) . (-)`, defeated him.

Quiz: a valid type for `sum . (map (+2))` is `Num a => [a] -> a`. A lambda is an anonymous function.

### The Dungeon Problem

An evil (but fair) wizard has locked the class dog in a dungeon maze. Send a Haskell program to guide her out within a week.

| Wizard's promise | Consequence |
|---|---|
| Each room connects to 0–2 **child rooms** | It is a graph |
| No cycles: each room is reachable by only one path | It is an acyclic graph |
| Every room is reachable from the start room | It is a **tree** (binary) |

Each room contains one of: nothing (empty), a monster, a health potion, or the exit.

**Goal**: compute the best possible outcome for the dog by taking the best route. You do not record which turns were taken; you track only where the dog is, where it has been, and its current attributes.

### Modelling The Dungeon In Haskell

```haskell
-- A room has contents and might branch into 0, 1, or 2 rooms.
-- No cycles, so Room is a tree data structure.
data Room = Room RoomContents
                 (Maybe Room) (Maybe Room)
                 deriving Show

data RoomContents = Fight Monster
                  | Heal Int
                  | Empty
                  | Escape
                  deriving Show

data Dog = Dog
  { dhp  :: Int   -- health
  , ddmg :: Int   -- damage dealt
  } deriving Show

data Monster = Monster
  { mhp  :: Int
  , mdmg :: Int
  } deriving Show

-- Result of the dog entering a room
data VisitResult = Victory        -- escaped
                 | Death          -- died
                 | Continue Dog   -- alive, not yet free
                 deriving Show

-- The solution: result of visiting a room AND its child rooms
crawl :: Dog -> Room -> VisitResult
```

- `Maybe Room` encodes "a child room may or may not exist".
- `RoomContents` is a sum type. `Dog` and `Monster` are product types with record syntax.

### Divide And Conquer Walkthrough

#### Definitions

> **Divide and conquer**: Solve independent subproblems and combine their solutions into the optimal overall solution (see [TOA Divide And Conquer](../TOA/05_Divide_And_Conquer.md)).

Here each **subtree** is a subproblem. Subtrees are combined by checking which rooms to visit and keeping only the best result. The dog starts as `Dog { dhp = 10, ddmg = 5 }`.

![Dungeon tree with D&C results](../../../diagrams/CSC3003S-Advanced%20Programming/FP/10_Prac_Prep_Tree_Traversal/dungeon-tree.svg)

*Each subtree is solved recursively. At the root, the best of staying, going left and going right is chosen.*

1. **Root → left**: the dog fights a skeleton, giving `Continue (Dog 5 5)`.
2. **Root → left → right**: an empty room, so nothing changes.
3. **Back at the root (left solved)**: going left leaves the dog with lower health than staying. So far the best options are going right or staying in the root room ("slowly starving to death").
4. **Root → right** (potion `Heal 10`, then an empty room and the exit): the answer to the slide's quiz is **Victory**. The dog can reach the exit.
5. **Root (both solved)**: stay = `Continue (Dog 10 5)`, left = `Continue (Dog 5 5)`, right = `Victory`. The overall result is **Victory**.

### Fighting A Monster

```haskell
fight :: Dog -> Monster -> VisitResult
fight dog mon
  | dhp dog <= 0 = Death
  | mhp mon <= 0 = Continue dog
  | otherwise    = fight dog' mon'
    where
  dog' = (dog { dhp = (dhp dog) - (mdmg mon) })
  mon' = (mon { mhp = (mhp mon) - (ddmg dog) })
```

The dog and monster trade blows each round, each losing health equal to the other's damage. This repeats until one reaches $\le 0$ health. The dog's death is checked first.

### Comparing Results: Eq And Ord Instances

Ranking the candidate `VisitResult`s needs `Ord`, which requires `Eq`:

```haskell
class Eq a => Ord a   -- Eq is a superclass of Ord
```

```haskell
-- ddmg never changes, and dogs from different dungeons are never compared,
-- so only HP is compared
instance Eq VisitResult where
    Victory      == Victory      = True
    Death        == Death        = True
    (Continue a) == (Continue b) = (dhp a) == (dhp b)
    _ == _                       = False
```

```haskell
-- x <= y means x is a WORSE result than y for the dog
instance Ord VisitResult where
    a <= b
      | a == b = True
      -- Both continue: more health is better
      | (Continue dog) <- a, (Continue dog') <- b = (dhp dog) <= (dhp dog')
      -- Death is worse than anything
      | Death <- a = True
      | Death <- b = False
      -- Victory is better than anything
      | Victory <- b = True
      | Victory <- a = False
```

- `| (Continue dog) <- a` is a **pattern guard**: it succeeds if `a` matches `Continue dog`, binding `dog`.
- The resulting order is $\text{Death} < \text{Continue (by HP)} < \text{Victory}$.

### Solving One Room (Conquer)

```haskell
-- The CONQUER part: result of the dog visiting a room's contents
visitRoom :: Dog -> RoomContents -> VisitResult
visitRoom dog room = go room
    where
  go (Fight monster) = fight dog monster
  go (Heal hp)       = Continue dog { dhp = (dhp dog) + hp }
  go Escape          = Victory
  go Empty           = Continue dog
```

Children are left out here and handled separately, which keeps the code neat.

### Solving The Children (Divide)

```haskell
-- The DIVIDE part
fork :: Dog -> Maybe Room -> Maybe Room -> VisitResult
fork dog leftRoom rightRoom = bestPath
    where
  bestPath   = maximum validPaths          -- highest-scoring valid path
  -- Invalid paths (e.g. going left when there is no left room) are Nothing;
  -- catMaybes removes them
  validPaths = catMaybes
                 [leftFirst, rightFirst, leftOnly, rightOnly, Just $ Continue dog]
  leftFirst  = fmap (uncurry $ crawlBoth dog) (both leftRoom rightRoom)
  rightFirst = fmap (uncurry $ crawlBoth dog) (both rightRoom leftRoom)
  leftOnly   = fmap (crawl dog) leftRoom
  rightOnly  = fmap (crawl dog) rightRoom
```

The five candidates are: left then right, right then left, left only, right only, or stay (`Continue dog`).

```haskell
-- Just a pair only when both are Just
both :: Maybe a -> Maybe b -> Maybe (a, b)
both (Just a) (Just b) = Just (a, b)
both _        _        = Nothing

-- Visit the first room's subtree and THEN the second's
crawlBoth :: Dog -> Room -> Room -> VisitResult
crawlBoth dog first second = sequenced
    where
  sequenced = case (crawl dog first) of
                Continue dog' -> crawl dog' second
                Victory       -> Victory
                Death         -> Death
```

### fmap And uncurry

#### Definitions

> **`fmap`**: A more general `map`. On `Maybe`, it applies a function to the value inside if present.

> **`uncurry`**: Converts a curried two-argument function into a function on a pair.

```haskell
fmap f (Just x) = Just (f x)
fmap _ _        = Nothing

uncurry f = \(a, b) -> f a b
(uncurry (+)) (1, 2) == (+) 1 2
```

In `fork`, `both` gives `Maybe (Room, Room)`. `uncurry $ crawlBoth dog` turns `crawlBoth dog :: Room -> Room -> VisitResult` into a function on the pair, and `fmap` applies it only if both rooms exist.

### Putting It Together: crawl

```haskell
-- Solves the subtree rooted at the given room; called on the root,
-- it solves the whole dungeon
crawl :: Dog -> Room -> VisitResult
crawl dog (Room this left right) = soln
    where
  soln = case (visitRoom dog this) of
              Continue dog' -> fork dog' left right
              Victory       -> Victory
              Death         -> Death
```

`crawl` and `fork` are **mutually recursive**: `crawl` conquers one room, then `fork` divides into the children, which calls `crawl` again.

The exercise removes the repeated `case` in `crawl` and `crawlBoth`:

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

The slide's signature says `VictoryResult`; the type is `VisitResult`.

### Prac Format And Sample Questions

The full base-game solution (`BaseGame.hs`) is provided on Amathuba. Each prac session has different but equally difficult questions.

| Question | Format | Advice |
|---|---|---|
| Q1 | Heavily scaffolded, incremental (1.2 builds on 1.1, …) | Partial marks **only if code compiles**. Start from a blank `Q1Ans.hs` and slowly copy and modify the skeleton. |
| Q2 | Not scaffolded; usually builds on Q1 | Code that merely compiles earns little. Marks grow with harder inputs handled. Submit in a **separate file**; you may copy Q1 into Q2, not the other way. |

**Sample prac: the stolen rat.** Also fetch your pet rat if possible, but leave it if fetching it would hurt the dog at all. The best path with the rat must have net health $\ge$ the best path without it.

- 1.1 A `Rat` type with member `ratName :: String`.
- 1.2 Add `rat :: Maybe Rat` to `Dog`.
- 1.3 Add a `Cage Rat` variant to `RoomContents`.
- 1.4 Modify `Eq` for `Dog` so dogs are unequal unless both have rats.
- 1.5 Modify `Ord` so that, at equal health, a dog without a rat is less than one with a rat. Health still dominates: `Dog 4 2 (Just (Rat "Jeremy")) <= Dog 10 2 Nothing`.
- Q2 (multiple rats, at most one per room): `Dog` holds `rats`, add `ratCount :: Dog -> Int`, make `Victory` hold a `Dog`, make `visitRoom` pick up rats, and rank so one rat is worth 2 HP. For example, 10 HP with 5 rats beats 19 HP with none, while still avoiding death.
