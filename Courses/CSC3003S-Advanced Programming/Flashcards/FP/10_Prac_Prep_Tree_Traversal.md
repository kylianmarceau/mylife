---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 10 — Haskell 6 — Practical Prep: Tree Traversal"
---

# FP 10 — Haskell 6 — Practical Prep: Tree Traversal

**Source note:** [Haskell 6 — Practical Prep: Tree Traversal](../../FP/10_Prac_Prep_Tree_Traversal.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Tree Modelling|Tree Modelling]]
  - [[#Comparing And Combining Results|Comparing And Combining Results]]
  - [[#Function Composition|Function Composition]]
  - [[#Fighting A Monster|Fighting A Monster]]
  - [[#Solving One Room (Conquer)|Solving One Room (Conquer)]]
  - [[#Solving The Children (Divide)|Solving The Children (Divide)]]
  - [[#Putting It Together: crawl|Putting It Together: crawl]]
  - [[#Prac Format And Sample Questions|Prac Format And Sample Questions]]
  - [[#Data Model And Local Operations|Data Model And Local Operations]]
  - [[#Traversal And Outcome Ordering|Traversal And Outcome Ordering]]
  - [[#Higher-Order Helpers And Extensions|Higher-Order Helpers And Extensions]]

## Core Content

### Tree Modelling

<!-- qard-id: ap-a6616bc9662451b7c255 -->
> [!qard]- How does `Room RoomContents (Maybe Room) (Maybe Room)` represent a dungeon?
> Each room holds contents and zero, one or two child rooms. `Nothing` marks an absent child; recursive `Room` values form a binary tree.

<!-- qard-id: ap-c266e329052851b7a931 -->
> [!qard]- Why is `VisitResult = Victory | Death | Continue Dog` a useful sum type?
> It distinguishes terminal outcomes from an ongoing run; only `Continue` carries the updated dog state needed by the next step.

<!-- qard-id: ap-ca8326e5051f1822428f -->
> [!qard]- How does tree traversal use divide and conquer in the dungeon problem?
> Solve child subtrees recursively, compare their outcomes, and combine them with the result of visiting the current room.

<!-- qard-id: ap-53e2ad10ca6b5b72a68a -->
> [!qard]- Why pass the updated dog to the next subtree?
> Earlier fights or healing affect later possibilities. Traversing with the original dog would lose those state changes.

<!-- qard-id: ap-d60835f420e06ecfd4fb -->
> [!qard]- How should `Victory` and `Death` propagate through sequential traversal?
> Return them unchanged without continuing; only `Continue dog` proceeds to the next computation.

### Comparing And Combining Results

<!-- qard-id: ap-8b85b0b35a23a1305cb3 -->
> [!qard]- Why does a custom `Ord VisitResult` also need `Eq`?
> `Eq` is a superclass of `Ord`; equality and ordering should describe a consistent interpretation of results.

<!-- qard-id: ap-7eff03c26133af222bb2 -->
> [!qard]- How are results ranked in the base dungeon?
> `Death` is worst, `Victory` is best, and `Continue` results are ranked by remaining health, under the base game's fixed-damage assumption.

<!-- qard-id: ap-ca590eb7c362b7cb15b4 -->
> [!qard]- What does `fmap f` do to a `Maybe` value?
> `fmap f (Just x) = Just (f x)`; `fmap f Nothing = Nothing`.

<!-- qard-id: ap-a5a6ef1f47372515cce7 -->
> [!qard]- What is `uncurry`'s type and purpose?
> `uncurry :: (a -> b -> c) -> (a,b) -> c`: adapt a curried two-argument function to consume a pair.

<!-- qard-id: ap-3a68d32339a64b8b20e2 -->
> [!qard]- What does `catMaybes` do when assembling candidate paths?
> It removes absent paths (`Nothing`) and extracts present results (`Just result`) before selecting the best.

### Function Composition

<!-- qard-id: ap-1bcc7c6d33b55b7b30ca -->
> [!qard]- How does `sqrt . sum . map (^2)` transform a vector?
> Square each component, add them and take the square root; composition applies rightmost first. For `[3,4]`, the result is `5`.

### Fighting A Monster

<!-- qard-id: ap-7acae30989d1b89ca966 -->
> [!qard]- How does the base game's fight update state and resolve simultaneous death?
> Subtract monster damage from dog health and dog damage from monster health each round, producing new records. The dog's nonpositive-health check comes first, so simultaneous death is `Death`.

### Solving One Room (Conquer)

<!-- qard-id: ap-d2a7104ecdb6a8846d40 -->
> [!qard]- How does `visitRoom` handle Fight, Heal, Empty and Escape?
> Fight runs combat; Heal returns `Continue` with increased health; Empty returns `Continue` unchanged; Escape returns `Victory`. Child rooms are handled by traversal rather than this local operation.

### Solving The Children (Divide)

<!-- qard-id: ap-bd76a1ee9671b1e9ffdb -->
> [!qard]- What five choices does the dungeon's `fork` compare?
> Left then right, right then left, left only, right only, and stay. Missing child combinations give `Nothing`, removed by `catMaybes`; choose the maximum of valid results.

### Putting It Together: crawl

<!-- qard-id: ap-b50aeb0ffb92f306ea03 -->
> [!qard]- How do `crawl`, `fork` and `flatmapContinue` divide their responsibilities?
> `crawl` visits the current room; on `Continue`, `fork` explores children and may call `crawl` again. `flatmapContinue` centralises “continue with this dog, but preserve terminal Victory/Death”.

### Prac Format And Sample Questions

<!-- qard-id: ap-8f42db3a8545ebff4646 -->
> [!qard]- Why must a new result-ordering rule update both `Eq` and `Ord` consistently?
> “Equal” must mean indistinguishable for that ordering. If health and rat possession/count affect ranking, the comparison instances must agree on those relevant fields.

### Data Model And Local Operations

<!-- qard-id: ap-c6571aaf309b1bfc3c74 -->
> [!qard]- What guarantees distinguish the dungeon tree from a general directed graph?
> Every room is reachable from the root by a unique route, with no cycles and at most two child links. Traversal therefore does not require general cycle handling for this model.

<!-- qard-id: ap-9ff7abd0c8fa33aebdba -->
> [!qard]- Why represent each optional child as `Maybe Room` rather than a special dummy room?
> Absence is explicit in the type; real contents such as Empty remain meaningful room values rather than overloaded sentinels.

<!-- qard-id: ap-cc7fd40c5a771111cd13 -->
> [!qard]- Which dungeon types are sums and which are products?
> `RoomContents` and `VisitResult` choose alternatives; Room, Dog and Monster combine fields. A sum alternative such as `Fight Monster` also carries a payload.

<!-- qard-id: ap-c6e038948a6297bf08a9 -->
> [!qard]- Why separate `visitRoom` from exploring the room's children?
> One handles the local contents; traversal handles structural choices. This keeps responsibilities small and allows each behaviour to be reasoned about independently.

<!-- qard-id: ap-1b732d5f4422c5c22aab -->
> [!qard]- How does a heal operation preserve immutability?
> Construct an updated Dog record with increased health and return it in `Continue`; the previous record remains unchanged.

<!-- qard-id: ap-17a2292dfc0a4c85a284 -->
> [!qard]- What does `fight` return when the monster is already defeated and the dog is alive?
> `Continue dog`, allowing traversal to proceed. Terminal tests must be ordered consistently with the specified simultaneous-death rule.

### Traversal And Outcome Ordering

<!-- qard-id: ap-cd2659af8ce9fd284a1d -->
> [!qard]- Why can choosing a child by its immediate room effect be wrong?
> A worse immediate health result may lead to a later exit/heal. Compare completed subtree outcomes, using the updated state, rather than greedily judging one room.

<!-- qard-id: ap-831e139ac895a5b7741d -->
> [!qard]- What does `both :: Maybe a -> Maybe b -> Maybe (a,b)` require to produce a pair?
> Both arguments must be `Just`; otherwise it returns `Nothing`. It expresses that a two-child traversal option needs both children.

<!-- qard-id: ap-62ed0d865483c2d63b34 -->
> [!qard]- Why include the “stay” result among `fork`'s candidates?
> It represents taking neither child and guarantees a valid candidate even when no child exists, under the base game's outcome definition.

<!-- qard-id: ap-c1d4b3a93d71cb3381c1 -->
> [!qard]- How does `crawlBoth` preserve state between child traversals?
> If the first returns `Continue dog'`, call the second with `dog'`; preserve Victory or Death without exploring further.

<!-- qard-id: ap-dc6a88b6f725f8ddb470 -->
> [!qard]- What is a pattern guard such as `(Continue dog) <- result`?
> A guard that succeeds only when the value matches that constructor, binding its payload for the guarded expression.

<!-- qard-id: ap-386488952e29f248430d -->
> [!qard]- Why must `maximum` use the intended semantic ordering of outcomes?
> Constructor order alone would not necessarily mean “best for the dog”; the custom order encodes death, continuing health and victory priorities.

### Higher-Order Helpers And Extensions

<!-- qard-id: ap-f44c7e699067c62a7551 -->
> [!qard]- What is the type of `fmap (uncurry f)` when `f :: a -> b -> c` and the input is `Maybe (a,b)`?
> It maps the present pair to `Maybe c`, applying the two components to the curried function; absence stays Nothing.

<!-- qard-id: ap-975390fdc613bea6710a -->
> [!qard]- Why is `flatmapContinue` more than mapping a function over every constructor?
> It invokes the next computation only for an ongoing Dog and flattens the returned VisitResult; terminal constructors short-circuit rather than gaining nested results.

<!-- qard-id: ap-aca7fd301a48eca32ff5 -->
> [!qard]- When adding a new room-content alternative, what code locations need semantic review?
> Its type declaration, exhaustive visit handling, any associated state updates, result representation and comparisons, plus tests of traversal interactions. Compilation alone does not settle the new rule.
