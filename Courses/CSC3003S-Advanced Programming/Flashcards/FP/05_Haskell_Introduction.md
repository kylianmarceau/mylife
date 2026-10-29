---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 05 — Haskell 1 — Introduction To Haskell"
---

# FP 05 — Haskell 1 — Introduction To Haskell

**Source note:** [Haskell 1 — Introduction To Haskell](../../FP/05_Haskell_Introduction.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Reading And Writing Haskell|Reading And Writing Haskell]]
  - [[#Lists And Scripts|Lists And Scripts]]
  - [[#How To Approach The Haskell Section|How To Approach The Haskell Section]]
  - [[#What Is Haskell?|What Is Haskell?]]
  - [[#Installation And GHCi|Installation And GHCi]]
  - [[#Your First Script|Your First Script]]
  - [[#Writing Functions As Compositions|Writing Functions As Compositions]]
  - [[#Worked Example: Prime Number Search|Worked Example: Prime Number Search]]
  - [[#Reading Haskell Expressions|Reading Haskell Expressions]]

## Core Content

### Reading And Writing Haskell

<!-- qard-id: ap-1a7b859156211c839ce3 -->
> [!qard]- What does `f :: Float -> Float` declare?
> A type signature: `f` takes a `Float` and returns a `Float`.

<!-- qard-id: ap-3bd4d1dfe360726b0d82 -->
> [!qard]- How does function application group relative to operators?
> Application binds more tightly and associates left: `f x + y` means `(f x) + y`, and `f x y` means `(f x) y`.

<!-- qard-id: ap-108467ee876912020703 -->
> [!qard]- What does `$` do in `f $ g x`?
> It applies the left function to the whole expression on its right: `f (g x)`. It has low precedence and associates right.

<!-- qard-id: ap-50945316f2bf8c9d39cf -->
> [!qard]- How does Haskell use a normally prefix function as an infix operator?
> Surround its name with backticks: ``a `div` b`` is `div a b`.

<!-- qard-id: ap-74e336aa9cbfb2ca7fff -->
> [!qard]- What does a `where` clause provide?
> Local names for intermediate expressions or helper functions used by the preceding definition.

<!-- qard-id: ap-ef482ef05354b322bc95 -->
> [!qard]- What is Haskell's layout rule?
> Definitions in the same layout block start in the same column; indentation determines the block's structure.

<!-- qard-id: ap-e869f9db6b1d4a519ba6 -->
> [!qard]- How are functions, types and constructors named?
> Functions and ordinary variables begin lowercase; types and data constructors begin uppercase.

### Lists And Scripts

<!-- qard-id: ap-aab07bfe1353a7bd2e44 -->
> [!qard]- What do `head`, `tail` and `!!` return, and when can they fail?
> The first element, the remaining list, and a zero-based indexed element. `head`/`tail` fail on `[]`; `!!` fails for negative or out-of-range indexes.

<!-- qard-id: ap-76026dc14ba1509ef5e4 -->
> [!qard]- How do `take n xs`, `drop n xs` and `xs ++ ys` differ?
> They return a prefix, the suffix after a prefix, and concatenation of two lists. They do not mutate `xs`.

<!-- qard-id: ap-7236323d5c1e6445a9f5 -->
> [!qard]- What distinguishes constructing an IO action from running it?
> A value such as `putStrLn "Hi"` describes an action. Effects occur when the runtime executes it as part of `main`; merely storing it in an unused expression does not run it.

### How To Approach The Haskell Section

<!-- qard-id: ap-81ba063029bc3d07cc38 -->
> [!qard]- What distinguishes examinable Haskell material from advanced reading in these notes?
> The lectures define examinable scope, while `[AR: ...]` marks advanced material outside assignments/tests/quizzes/exam. Practise implementing code yourself, rather than only reading completed solutions.

### What Is Haskell?

<!-- qard-id: ap-6d886e2539477c914b3e -->
> [!qard]- How do Haskell's purity, lazy evaluation and static type system interact?
> Expressions are immutable/pure, so unused computations may be skipped without hidden changes; types are inferred/checked before execution. Strong type constraints do not mean evaluation is eager or that every runtime error is impossible.

### Installation And GHCi

<!-- qard-id: ap-ae2bfee536927f740415 -->
> [!qard]- What roles do GHC, GHCi, Cabal and GHCup serve?
> Compiler, interactive evaluator, package/build tool, and toolchain installer respectively.

<!-- qard-id: ap-9e662b1b407e448af708 -->
> [!qard]- Which GHCi commands load/reload a script, show an expression's type and leave the interpreter?
> `:load file`, `:reload`, `:type expression`, and `:quit`; use `:{` and `:}` around multiline interactive input.

### Your First Script

<!-- qard-id: ap-0afc52327562377dff64 -->
> [!qard]- How does running an `.hs` script differ from loading it into GHCi?
> `runghc file.hs` executes its `main` action; GHCi loads definitions for interactive evaluation. `show` converts a supported value to text, and `putStrLn` describes a line-output action.

### Writing Functions As Compositions

<!-- qard-id: ap-9d397c0731cbb60bdb2f -->
> [!qard]- How does a `where` block support the quadratic-formula example?
> Name reusable expressions such as discriminant and denominator, then define both solutions using them; align the local definitions in one layout block.

### Worked Example: Prime Number Search

<!-- qard-id: ap-a41dbbf0239a6d5c2e8d -->
> [!qard]- How does the introductory Haskell prime-search pipeline work?
> `filter isPrime [2..upperBound]`; for candidate `n`, check that no `d` in `[2..n-1]` divides it, e.g. ``not (any (\d -> n `mod` d == 0) [2..n-1])``. Starting at two avoids treating one as prime.

### Reading Haskell Expressions

<!-- qard-id: ap-02e06c23aedb8d1aa53f -->
> [!qard]- What is the Prelude?
> The standard collection of common types and functions available without explicitly importing a module, including basic numeric and list operations.

<!-- qard-id: ap-f454944199b0d0c74734 -->
> [!qard]- What does the expression `f (g x)` differ from `f g x`?
> The first passes the result of `g x` to `f`; the second groups as `(f g) x`, first passing the function `g` itself to `f`.

<!-- qard-id: ap-cca9a00e2073d7fafe53 -->
> [!qard]- How can a numeric operator be used as an ordinary function?
> Put it in parentheses, such as `(+) x y`; an operator section such as `(2 *)` fixes one operand and returns a function.

<!-- qard-id: ap-9a6dd4476b09b084c426 -->
> [!qard]- Why does `x = expression` not mean repeatedly assigning to a mutable variable?
> It defines an immutable binding. Later expressions use that value; changed data is represented by a new binding/value.

<!-- qard-id: ap-6507159f32875cb68d20 -->
> [!qard]- What does `map (*2) xs` describe without an explicit loop?
> Apply the partially supplied multiplication function to each element of `xs`, producing a new list while preserving the original.

<!-- qard-id: ap-9fdc042a0d190a1e74f6 -->
> [!qard]- How do `sum`, `product`, `reverse` and `length` consume a finite list?
> Sum/product combine numeric elements using additive/multiplicative identities; reverse changes their order; length counts elements. These computations generally require reaching the list's end.

<!-- qard-id: ap-aa4af9f03cc88d26bbd9 -->
> [!qard]- Why is `xs ++ [x]` different in structure from `x : xs`?
> Append places `x` at the end and must traverse/copy the left list spine; cons adds one new front cell and shares the existing tail.

<!-- qard-id: ap-39ad4cfcaa63785d4134 -->
> [!qard]- What does `show` require that plain string concatenation does not provide?
> A `Show` instance converts a non-string value into a `String`; `++` concatenates lists/strings and does not automatically convert arbitrary values.

<!-- qard-id: ap-7d8acbb9718277af118f -->
> [!qard]- Why must local definitions under `where` align with one another?
> The layout block uses a shared indentation column to distinguish sibling definitions from nested continuations.

<!-- qard-id: ap-98a1fcdd7076396d5b9e -->
> [!qard]- How can type signatures help find a mistaken function composition?
> They state expected argument/result types, letting the typechecker identify a stage whose output cannot feed the next stage.

<!-- qard-id: ap-9730f8afe1a71feac384 -->
> [!qard]- What does a function such as `quadruple = double . double` demonstrate?
> Larger transformations can be built by composing reusable smaller functions; the inner/rightmost `double` runs first.

<!-- qard-id: ap-8eb3b1a8d9b576e83668 -->
> [!qard]- Why can a function signature mention `IO ()` without making every surrounding expression effectful?
> It describes an action with a unit result. Pure expressions can construct or contain that action value; execution and sequencing remain within IO.

<!-- qard-id: ap-56986e741f33695506c8 -->
> [!qard]- What does the lecture's “strict/strong type system” description mean, as distinct from strict evaluation?
> Incompatible types are rejected rather than freely coerced, for example an Int is not automatically a String. This is a typing property; Haskell's expression evaluation remains non-strict/lazy.
