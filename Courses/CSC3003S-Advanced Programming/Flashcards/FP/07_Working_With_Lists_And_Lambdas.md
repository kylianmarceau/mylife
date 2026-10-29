---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 07 — Haskell 3 — Working With Lists And Lambdas"
---

# FP 07 — Haskell 3 — Working With Lists And Lambdas

**Source note:** [Haskell 3 — Working With Lists And Lambdas](../../FP/07_Working_With_Lists_And_Lambdas.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#List Combinators|List Combinators]]
  - [[#Folds|Folds]]
  - [[#Comprehensions|Comprehensions]]
  - [[#Batch Processing: Prime Factorisation|Batch Processing: Prime Factorisation]]
  - [[#Why Have Lambdas?|Why Have Lambdas?]]
  - [[#Quickfire Combinators|Quickfire Combinators]]
  - [[#Fold Is The Universal List Combinator|Fold Is The Universal List Combinator]]
  - [[#String Comprehensions|String Comprehensions]]
  - [[#Combinator Contracts|Combinator Contracts]]
  - [[#Fold Mechanics|Fold Mechanics]]
  - [[#Comprehensions And Function Values|Comprehensions And Function Values]]

## Core Content

### List Combinators

<!-- qard-id: ap-30830b88c78adfaca34f -->
> [!qard]- What is `map`'s type and effect?
> `map :: (a -> b) -> [a] -> [b]`: transform each element, preserving list order and one output element per input.

<!-- qard-id: ap-69ec4a4f7dde21187d5b -->
> [!qard]- What is `filter`'s type and effect?
> `filter :: (a -> Bool) -> [a] -> [a]`: retain elements satisfying the predicate, in their original order.

<!-- qard-id: ap-52a6e80c8c1491119097 -->
> [!qard]- How is a Haskell lambda written?
> `\x -> expression`; multiple arguments or patterns are allowed, such as `\(name, age) -> age < 65`.

<!-- qard-id: ap-6f4052c6dfd71e0b1c2b -->
> [!qard]- What does `zip` do with lists of different lengths?
> It pairs corresponding elements and stops at the shorter list; its type is `[a] -> [b] -> [(a,b)]`.

<!-- qard-id: ap-9f04792de6bfb3e63dcc -->
> [!qard]- How do `all` and `any` differ?
> `all p xs` requires every element to satisfy `p`; `any p xs` needs one. On `[]`, `all` is `True` and `any` is `False`.

<!-- qard-id: ap-4f4bf6e00d1767425130 -->
> [!qard]- How does `takeWhile p` differ from `filter p`?
> `takeWhile` stops at the first failing element; `filter` continues checking later elements.

### Folds

<!-- qard-id: ap-6633f10121e3cf5f42a1 -->
> [!qard]- How do `foldl f z [x,y]` and `foldr f z [x,y]` expand?
> `foldl`: `f (f z x) y`; `foldr`: `f x (f y z)`. The accumulator's position differs.

<!-- qard-id: ap-6b3c55e9774205c5acdc -->
> [!qard]- What are the general types of `foldl` and `foldr`?
> `foldl :: (b -> a -> b) -> b -> [a] -> b`; `foldr :: (a -> b -> b) -> b -> [a] -> b`.

<!-- qard-id: ap-5d254626a624ecc9514e -->
> [!qard]- Why can swapping `foldl` and `foldr` change a result?
> They parenthesise and pass operands differently. For subtraction, `foldl (-) 0 [1,2,3] = -6`, while `foldr (-) 0 [1,2,3] = 2`.

<!-- qard-id: ap-6281763f81f2a911e73e -->
> [!qard]- How can `foldr` implement `map`?
> `map f = foldr (\x acc -> f x : acc) []`: transform the head and cons it onto the folded tail.

<!-- qard-id: ap-648435b4b86526bc58c8 -->
> [!qard]- How can `foldr` implement `filter`?
> `filter p = foldr (\x acc -> if p x then x : acc else acc) []`.

### Comprehensions

<!-- qard-id: ap-cd64cf312bde401301c3 -->
> [!qard]- What do the generator and guard mean in `[f x | x <- xs, p x]`?
> The generator draws values from `xs`; the guard retains those satisfying `p`; `f` transforms the retained values.

<!-- qard-id: ap-a2417ad2f48874ae78fe -->
> [!qard]- Do multiple list-comprehension generators behave like `zip`?
> No. They produce nested-loop combinations, with the later generator varying fastest. `zip` pairs corresponding positions.

<!-- qard-id: ap-0f041bde1452f2f93d4f -->
> [!qard]- How do dependent generators work?
> A later generator may use earlier bindings, e.g. `[(x,y) | x <- [1..3], y <- [1..x]]` includes only `y <= x`.

<!-- qard-id: ap-0708fb04177b9baf2026 -->
> [!qard]- How does a comprehension flatten a list of lists?
> `[x | xs <- xss, x <- xs]`: draw each inner list, then each of its elements.

### Batch Processing: Prime Factorisation

<!-- qard-id: ap-cd5299304e4a0c699061 -->
> [!qard]- How does the notes' unique-prime-factor pipeline avoid repeated prime factors?
> For each positive `n`, filter candidates `[1..n]` for divisibility, then filter those factors for primality; each candidate occurs once, so nine gives `[3]`, not `[3,3]`.

### Why Have Lambdas?

<!-- qard-id: ap-93a69cacb39622ef63e5 -->
> [!qard]- Why can returning a lambda make a callback clearer than naming a one-off helper?
> The returned function captures fixed context, such as a user's name, and waits for event-specific input such as a button count; its purpose stays beside its use.

### Quickfire Combinators

<!-- qard-id: ap-c1d5c4e0a96e86df36a5 -->
> [!qard]- How do `dropWhile` and `drop` differ?
> `dropWhile p` removes only the leading run satisfying `p`, stopping at the first failure; `drop n` removes a specified number of leading elements.

### Fold Is The Universal List Combinator

<!-- qard-id: ap-fb087c29d88c57182cdf -->
> [!qard]- How do folds express sums and products without mutation?
> `foldl (+) 0` and `foldl (*) 1` carry a newly computed accumulator each step; the neutral starting value matters, especially for the empty list.

### String Comprehensions

<!-- qard-id: ap-659f7d092d999c5f5fc6 -->
> [!qard]- Why do list combinators and comprehensions also work on a Haskell `String`?
> `String` is `[Char]`; for example `[toUpper c | c <- text]` maps each character, using `toUpper` from `Data.Char`.

### Combinator Contracts

<!-- qard-id: ap-31c22177df28ef7886d3 -->
> [!qard]- Why must `filter`'s predicate return `Bool` while `map`'s mapper may return another type?
> Filter decides retention without changing element type; map constructs a new element for every input and may change its type.

<!-- qard-id: ap-430395eb34999a5db09b -->
> [!qard]- What is the type of `zip`'s output when names and ages are paired?
> `[(String, Int)]` for `[String]` and `[Int]`, keeping the relationship between parallel data while later filters operate on each pair.

<!-- qard-id: ap-7393c00e7b5c46ae531b -->
> [!qard]- How do `takeWhile` and `dropWhile` divide a list at a predicate boundary?
> They respectively retain and discard its longest leading prefix satisfying the predicate. They stop at the first failure, regardless of later matches.

<!-- qard-id: ap-bbe681281646df73fcf8 -->
> [!qard]- Why can an infinite input be usable for `any` but not for every `all` query?
> A finite successful witness makes `any` return True; a finite counterexample makes `all` return False. Proving the opposite result may require examining the whole infinite input.

### Fold Mechanics

<!-- qard-id: ap-2ec498753e88aedcf477 -->
> [!qard]- What is the neutral starting accumulator for a sum, product and collected list?
> Zero, one and the empty list respectively. It determines the empty-input result as well as the first combination.

<!-- qard-id: ap-5421f882471a5c6141a7 -->
> [!qard]- Why does `foldr (:) [] xs` reconstruct `xs`?
> Replace the empty-list case with `[]` and every cons with cons again, preserving element order and list structure.

<!-- qard-id: ap-34c9702a10d834b080cc -->
> [!qard]- How can a fold accumulate a result of a different type from the input element type?
> Its accumulator type is independent: e.g. fold `String` elements into an `Int` total length or a list into one summary record.

<!-- qard-id: ap-e2ce6128b2fec1089c6d -->
> [!qard]- What must be checked before treating two fold formulations as equivalent?
> Operand order, association, the starting value, and strictness/demand behaviour; equal results for addition do not prove equivalence for subtraction or infinite structures.

### Comprehensions And Function Values

<!-- qard-id: ap-a4b7ef2b22feba6bfe86 -->
> [!qard]- How do you translate a map/filter pipeline into one comprehension?
> `map f (filter p xs)` becomes `[f x | x <- xs, p x]`, preserving the predicate's input and the output order.

<!-- qard-id: ap-011fea0cdf1f24b92f82 -->
> [!qard]- How does generator order determine the order of a Cartesian-product comprehension?
> Earlier generators form outer loops, so the last generator varies fastest. Swapping generators changes result order even if it produces the same set of pairs.

<!-- qard-id: ap-45798f34081a0479641a -->
> [!qard]- Why can a dependent generator use only variables already bound to its left?
> Its source expression is evaluated within the scope created by earlier generators; a later binding is not yet available.

<!-- qard-id: ap-733460b001eaa46c772c -->
> [!qard]- What does a closure capture when `makeCallback name` returns a lambda taking a press count?
> The fixed `name` from its enclosing call; the count remains the returned function's parameter. Each call can produce a callback with different captured context.
