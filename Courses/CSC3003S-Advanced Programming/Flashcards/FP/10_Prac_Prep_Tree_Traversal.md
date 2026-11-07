---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 10 — Practical Preparation: Tree Traversal"
---

# FP 10 — Practical Preparation: Tree Traversal

**Source note:** [Practical Preparation: Tree Traversal](../../FP/10_Prac_Prep_Tree_Traversal.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Function Composition|Function Composition]]
  - [[#Modelling The Dungeon|Modelling The Dungeon]]
  - [[#Ranking Results|Ranking Results]]
  - [[#Solving The Tree|Solving The Tree]]
  - [[#The Practical|The Practical]]

## Core Content

### Function Composition

<!-- qard-id: ap-823b0bcc7a915320be63 -->
> [!qard]- What is function composition?
> Defining a function as a combination of other functions, without mentioning the data.

<!-- qard-id: ap-6f9380e7e5be682da5b0 -->
> [!qard]- Define the `.` operator.
> $f . g=\lambda x\to f\,(g\,x)$, so $(f . g)\,x=f\,(g\,x)$.

<!-- qard-id: ap-1fea653c8f48582f16f2 -->
> [!qard]- In which direction does data flow through `sqrt . sum . map (^2)`?
> Right to left: `map (^2)` first, then `sum`, then `sqrt`.

### Modelling The Dungeon

<!-- qard-id: ap-1c862e1abfccee2d93b5 -->
> [!qard]- What three properties make the dungeon a tree?
> Each room has 0–2 children, there are no cycles, and every room is reachable from the start.

<!-- qard-id: ap-bf19b3afd373412daf40 -->
> [!qard]- How is an optional child room represented?
> With `Maybe Room`.

<!-- qard-id: ap-9cc9c49546d917cb794f -->
> [!qard]- How is the dungeon problem solved?
> Divide and conquer: solve each subtree, then keep the best result at each room.

<!-- qard-id: ap-5e98fd46497dd655a433 -->
> [!qard]- How does the `fight` function decide the outcome?
> It recurses, both sides dealing damage each round, until the dog's HP ≤ 0 (`Death`) or the monster's HP ≤ 0 (`Continue dog`).

### Ranking Results

<!-- qard-id: ap-2f598315a468ee3cc8cf -->
> [!qard]- Why must implementing `Ord` also implement `Eq`?
> `Ord` is declared as `class Eq a => Ord a`, so `Eq` is a superclass.

<!-- qard-id: ap-6bd30cd4d0c48df93060 -->
> [!qard]- How are `VisitResult`s ranked?
> `Death` worst, `Continue dog` ordered by HP, `Victory` best.

<!-- qard-id: ap-ad9700920845736911ce -->
> [!qard]- What is a pattern guard?
> A guard `| Pat <- expr` that succeeds if `expr` matches `Pat`, binding its variables.

### Solving The Tree

<!-- qard-id: ap-1306804ae28b2fc30692 -->
> [!qard]- What does `visitRoom` do?
> Conquer: works out the result of entering one room's contents (fight, heal, escape or empty).

<!-- qard-id: ap-2432de0e619907cc5491 -->
> [!qard]- What does `fork` do?
> Divide: tries every way of continuing (left then right, right then left, left only, right only, stay) and returns the maximum.

<!-- qard-id: ap-5a9c0731ae30b7d21dfe -->
> [!qard]- What does `catMaybes` do in `fork`?
> Removes `Nothing` entries — paths that can't be taken — keeping the `Just` values.

<!-- qard-id: ap-86f0673636125a21b562 -->
> [!qard]- What do `fmap` and `uncurry` do?
> `fmap` applies a function inside a `Just` (leaving `Nothing` alone); `uncurry` turns a two-argument function into one taking a pair.

<!-- qard-id: ap-22574edd20fd16e41645 -->
> [!qard]- What pattern does `flatmapContinue` capture?
> Continue with the next step only on `Continue dog`, passing `Victory`/`Death` through unchanged — the idea monads generalise.

### The Practical

<!-- qard-id: ap-0c732cb5cb766c8b6c18 -->
> [!qard]- What is the key rule for getting marks in the Haskell practical?
> Your code must compile — partial marks depend on it.

<!-- qard-id: ap-6f77112db22f2ef9cb45 -->
> [!qard]- How should Question 1 and Question 2 be submitted?
> In separate files; Q2 may start from a copy of Q1, never the reverse.
