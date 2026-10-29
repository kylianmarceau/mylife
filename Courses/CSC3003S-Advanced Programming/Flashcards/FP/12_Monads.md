---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 12 — Haskell 8 — Monads"
---

# FP 12 — Haskell 8 — Monads

**Source note:** [Haskell 8 — Monads](../../FP/12_Monads.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Bind And Wrapped Computations|Bind And Wrapped Computations]]
  - [[#IO And do Notation|IO And do Notation]]
  - [[#Generalising: The Monad Typeclass|Generalising: The Monad Typeclass]]
  - [[#Tracking Effects: CounterMonad And DummyIO|Tracking Effects: CounterMonad And DummyIO]]
  - [[#do Notation|do Notation]]
  - [[#Context And Sequencing|Context And Sequencing]]
  - [[#Effects And IO|Effects And IO]]
  - [[#do Translation|do Translation]]

## Core Content

### Bind And Wrapped Computations

<!-- qard-id: ap-44cb5dd74382d0463aab -->
> [!qard]- What is the general type of bind, `(>>=)`?
> `(>>=) :: Monad m => m a -> (a -> m b) -> m b`: feed a result into a computation that returns the same kind of context.

<!-- qard-id: ap-4f985af92e7af817607e -->
> [!qard]- How does bind work for `Maybe`?
> `Just x >>= f = f x`; `Nothing >>= f = Nothing`. The first absence short-circuits the chain.

<!-- qard-id: ap-f7a9b8553514df35bd5d -->
> [!qard]- Why use bind instead of `fmap` for a function `a -> Maybe b`?
> Mapping it over `Maybe a` gives `Maybe (Maybe b)`. Bind combines the contexts and returns `Maybe b`.

<!-- qard-id: ap-99132781e6512add1185 -->
> [!qard]- How does bind work for lists?
> Apply the function to each element and concatenate the resulting lists: `xs >>= f = concat (map f xs)`.

<!-- qard-id: ap-5851678e249ad719efc0 -->
> [!qard]- What is `[1,2] >>= (\n -> [n,n+10])`?
> `[1,11,2,12]`: each input may produce several results, then the lists are concatenated in order.

<!-- qard-id: ap-3e2bb1664b9e0a1a7e6d -->
> [!qard]- What does `pure` do for `Maybe` and lists?
> It embeds one ordinary value in the context: `pure x = Just x` for `Maybe`, and `pure x = [x]` for lists.

<!-- qard-id: ap-fad07a42f022d930251f -->
> [!qard]- What do `<$>` and `<*>` do in `(*) <$> Just 2 <*> Just 3`?
> `<$>` maps multiplication into `Maybe`, producing a wrapped function; `<*>` applies it to the second wrapped value, yielding `Just 6`.

<!-- qard-id: ap-4ec4de69993f6f3310ea -->
> [!qard]- How can a monadic computation carry information beyond its returned value?
> Its context may represent failure, multiple possibilities, accumulated metadata or IO sequencing; bind combines that information while passing results forward.

### IO And do Notation

<!-- qard-id: ap-2d807c82f763c8cf6347 -->
> [!qard]- Why is `getLine :: IO String` rather than `String`?
> It is an action that reads external input when executed; its result depends on that interaction, which its type records.

<!-- qard-id: ap-bf1cad2f8074c602b306 -->
> [!qard]- Can a pure function generally extract an `a` from `IO a`?
> No. Use bind or `do` to work with the result within IO; a value of type `IO a` is an action, not an ordinary `a`.

<!-- qard-id: ap-0714e1e858ef01f43a19 -->
> [!qard]- How does `>>` differ from `>>=`?
> `action >> next` sequences actions but discards the first result; `>>=` passes that result to a function that determines the next action.

<!-- qard-id: ap-09bd72a36b620ac5bfd5 -->
> [!qard]- What does `x <- action` mean in a `do` block?
> Bind the action's result to `x` for the following computation; it corresponds to `action >>= \x -> ...`.

<!-- qard-id: ap-0b534f42446c9e522707 -->
> [!qard]- How does `let x = expression` differ from `x <- action` in `do`?
> `let` introduces a pure local binding; `<-` binds the result of a computation in the surrounding context.

<!-- qard-id: ap-617bc1861259ef812cb1 -->
> [!qard]- Does `pure x` immediately exit a `do` block?
> No. It constructs a contextual value. Only when used as the final action does its result become the block's result.

<!-- qard-id: ap-5bc086ec606b31dda8d8 -->
> [!qard]- How does a `Result e a = Ok a | Err e` bind propagate errors?
> `Ok x >>= f = f x`; `Err e >>= _ = Err e`, preserving the error and skipping later computations.

### Generalising: The Monad Typeclass

<!-- qard-id: ap-f543d15a651dfb798a60 -->
> [!qard]- What makes a type constructor such as `Maybe` usable with generic monadic code?
> It supplies the contextual embedding and bind operations with the expected consistent behaviour; the same generic sequencing syntax then works for optional results, lists and IO with different meanings.

<!-- qard-id: ap-4db9c40f56954958c147 -->
> [!qard]- What does the lecture mean by the Monad typeclass?
> A shared interface for contextual computation using operations such as `pure` and bind. Maybe, lists and IO support the same sequencing form with different context-specific behaviour.

<!-- qard-id: ap-7526901656067181cc33 -->
> [!qard]- What does the Functor name identify in the lecture's use of `fmap`?
> A type constructor supporting mapping an ordinary function over its contents while respecting the context. This names the interface used by `fmap`; the precise hierarchy distinctions are marked extra reading.

<!-- qard-id: ap-7c93ba6be70b91c5376b -->
> [!qard]- What does Applicative application add when the function is already contextual?
> `<*>` applies a wrapped function to a wrapped argument, while `pure` embeds an ordinary value. This supports examples such as a two-argument operation applied to two Maybe inputs without unwrapping them manually.

### Tracking Effects: CounterMonad And DummyIO

<!-- qard-id: ap-a6e826438cbc832cee13 -->
> [!qard]- How do the Counter and DummyIO examples accumulate effects through bind?
> `Count n x >>= f` combines `n` with the count returned by `f x`; DummyIO concatenates the previous and next action lists. `fmap` changes the payload while preserving this metadata.

<!-- qard-id: ap-da47c945a8a76e5535ef -->
> [!qard]- How do `<*` and `*>` differ when sequencing the Counter example's effects?
> Both combine effects, but `<*` keeps the left payload and `*>` the right. Discarding a payload does not discard the count/effect contributed by its computation.

### do Notation

<!-- qard-id: ap-f6b4577247c71d1e0d3f -->
> [!qard]- Why is `let x = x + 2` inside `do` not an increment?
> A `let` binding is recursive and immutable: the new `x` refers to itself, so demanding it diverges. Give the new result a different name or use an explicit state-passing computation.

<!-- qard-id: ap-ef422adc3fe867816d19 -->
> [!qard]- How do `throw` and `orErr` use `data Result e v = Ok v | Err e`?
> `throw :: e -> Result e v` constructs `Err`; `orErr :: Maybe v -> e -> Result e v` converts `Just v` to `Ok v` and `Nothing` to the supplied `Err e`.

### Context And Sequencing

<!-- qard-id: ap-c98c618aabf29eb1bd63 -->
> [!qard]- What is the type of `fmap` specialised to `Maybe`?
> `(a -> b) -> Maybe a -> Maybe b`: apply an ordinary function to a present payload while preserving Nothing.

<!-- qard-id: ap-7fcc310b9fa51750cd85 -->
> [!qard]- Why can bind's next computation depend on the previous result?
> Its second argument is a function `a -> m b`, so the retrieved `a` determines which contextual computation is returned.

<!-- qard-id: ap-4672e841b8be7a936eff -->
> [!qard]- How does list bind support both filtering and duplication?
> Return `[]` to contribute no result, `[x]` for one result, or several elements for multiple results; concatenation combines each input's alternatives.

<!-- qard-id: ap-ea70c3e2bafc055adb96 -->
> [!qard]- Why does `fmap` alone preserve a list's outer length?
> Its function returns one ordinary output per input element. Bind's function returns a list per element, allowing the outer structure to expand or shrink.

<!-- qard-id: ap-99ce5c2e6f279bee170f -->
> [!qard]- What does `pure` choose for an ordinary value in the Counter or Result examples?
> A neutral context: zero accumulated count for Counter, or `Ok value` for Result, rather than inventing extra effects/failure.

<!-- qard-id: ap-95928a7963293ab4644a -->
> [!qard]- What is the type of a partially mapped two-argument operation such as `(+) <$> Just x`?
> `Maybe (a -> a)` for an appropriate numeric `a`: the context contains a function waiting for its second operand.

<!-- qard-id: ap-de0831596a88f843a182 -->
> [!qard]- How does applicative application propagate absence for `Maybe`?
> `Just f <*> Just x` gives `Just (f x)`; absence in either required input gives Nothing.

### Effects And IO

<!-- qard-id: ap-72efc2e132e2ededc142 -->
> [!qard]- Why can discarding an IO result still preserve the action's effect?
> `>>` sequences the action and ignores its returned payload, rather than throwing away the action itself. Printing can run even though its unit result is unused.

<!-- qard-id: ap-950a3dab88ab1ddcfad1 -->
> [!qard]- What does `IO ()` say about a computation's return value?
> The action returns unit, not an informative payload. It may still perform meaningful external work such as printing or writing.

<!-- qard-id: ap-f942729c7565fcd9b7da -->
> [!qard]- What changes when a pure value is lifted using `pure` inside IO?
> It becomes an IO action returning that value without additional external interaction; it does not execute unrelated actions or mutate the value.

<!-- qard-id: ap-2d79b4611c72404c4956 -->
> [!qard]- How does DummyIO demonstrate separating a description of work from its interpretation?
> Its value records a list of intended actions; constructing/combining that description is distinct from an interpreter actually performing the operations.

### do Translation

<!-- qard-id: ap-a9a4a86db90d8e58f381 -->
> [!qard]- How does a `do` statement with no `<-` become monadic sequencing?
> Sequence it with the following computation using `>>`, discarding its result while retaining the context's effects.

<!-- qard-id: ap-b12601815ac32f834ebf -->
> [!qard]- What determines a `do` block's result type?
> Its final expression/action supplies the contextual result; a local `let` declaration alone is not the final returned action.

<!-- qard-id: ap-09e2861a13e8550c3f21 -->
> [!qard]- Why does a local binding introduced by `<-` not provide a global escape from IO?
> The bound value is available only within the continuation, whose result remains in the IO context.

<!-- qard-id: ap-6aef987e09265a682953 -->
> [!qard]- How does the Result example preserve the original error through a long chain?
> Each `Err e >>= f` returns that same Err without invoking `f`; success alone invokes the next potentially failing computation.
