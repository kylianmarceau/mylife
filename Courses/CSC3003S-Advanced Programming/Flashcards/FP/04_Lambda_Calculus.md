---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 04 — Lambda Calculus"
---

# FP 04 — Lambda Calculus

**Source note:** [Lambda Calculus](../../FP/04_Lambda_Calculus.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Basics|Basics]]
  - [[#Scope|Scope]]
  - [[#Reduction|Reduction]]
  - [[#Combinators And Church Booleans|Combinators And Church Booleans]]

## Core Content

### Basics

<!-- qard-id: ap-0842d77f69c95c80053f -->
> [!qard]- What is the lambda calculus?
> A tiny formal language of anonymous first-class functions (Alonzo Church, 1930s), the "machine code" of functional languages.

<!-- qard-id: ap-beebdf4868082b783018 -->
> [!qard]- How do Turing machines and the lambda calculus compare?
> Turing machines mutate state on a tape; lambda calculus rewrites expressions by reduction. Both are universal and equivalent (Church–Turing thesis).

<!-- qard-id: ap-0d0318ccef98cacec4e2 -->
> [!qard]- What are the three kinds of lambda expression?
> Names (variables), functions (abstractions $\lambda x.\,e$) and applications ($e_1\,e_2$).

<!-- qard-id: ap-78bc2a9a3d323bed3a99 -->
> [!qard]- Name the parts of $\lambda x.\ x\,y$.
> $\lambda$ starts the function, $x$ is the parameter, `.` separates, $x\,y$ is the body.

<!-- qard-id: ap-271463d042d08154a497 -->
> [!qard]- How are multi-argument functions represented?
> By currying: $\lambda x\,y.\ e$ is shorthand for $\lambda x.\,(\lambda y.\ e)$.

### Scope

<!-- qard-id: ap-b759ac318672a101c1f2 -->
> [!qard]- When is a variable occurrence bound, and when free?
> Bound if it lies in the body of a lambda with that parameter name; otherwise free.

<!-- qard-id: ap-46c973146ef8a06c0c80 -->
> [!qard]- What is a closed expression?
> One with no free variables.

<!-- qard-id: ap-a97212d14f4deda0945a -->
> [!qard]- What is alpha equivalence?
> Two expressions are equivalent if they differ only by renaming bound variables (free variables unchanged).

### Reduction

<!-- qard-id: ap-0373455339fbc4304829 -->
> [!qard]- State β-reduction.
> $(\lambda x.\ M)\,N\to_\beta M[x:=N]$ — replace free occurrences of $x$ in $M$ by $N$.

<!-- qard-id: ap-7512fc9067ef66a0b293 -->
> [!qard]- What is β-normal form?
> An expression with no redexes left — equivalent to termination.

<!-- qard-id: ap-bcaf20dfe00f06c21713 -->
> [!qard]- What is divergence?
> An expression that never reaches normal form, e.g. $(\lambda x.\,x\,x)(\lambda x.\,x\,x)$ — an infinite loop.

<!-- qard-id: ap-564e2fb0c93e09c100e7 -->
> [!qard]- Lazy versus strict reduction order in the lambda calculus?
> Lazy reduces the leftmost/outermost redex, avoiding argument evaluation; strict reduces the rightmost/innermost, evaluating arguments first.

<!-- qard-id: ap-3ac46f7d347c0e843107 -->
> [!qard]- Why does $K\,I\,\Omega$ terminate lazily but not strictly?
> Lazy applies $K$ first and discards $\Omega$; strict tries to evaluate $\Omega$ forever.

### Combinators And Church Booleans

<!-- qard-id: ap-30b6c72902116f694b98 -->
> [!qard]- Define $I$, $M$, $K$ and $\Omega$.
> $I=\lambda x.\,x$; $M=\lambda x.\,x\,x$; $K=\lambda x.\lambda y.\,x$; $\Omega=(\lambda z.\,z\,z)(\lambda z.\,z\,z)$.

<!-- qard-id: ap-fd5645190bcbe90dda96 -->
> [!qard]- Define Church TRUE and FALSE.
> $\text{TRUE}=\lambda x.\lambda y.\,x$ (picks the first); $\text{FALSE}=\lambda x.\lambda y.\,y$ (picks the second).

<!-- qard-id: ap-f74cae00703af4463456 -->
> [!qard]- Define IFTHEN in the lambda calculus.
> $\lambda b.\lambda t.\lambda e.\ b\,t\,e$ — the Boolean selects the branch.

<!-- qard-id: ap-f6b36870e37dccecebc6 -->
> [!qard]- Define NOT with Church Booleans.
> $\lambda b.\ b\ \text{FALSE}\ \text{TRUE}$.

<!-- qard-id: ap-18bb08d0e38a336e3746 -->
> [!qard]- What is a Church numeral?
> A number $N$ represented as applying a function $N$ times.

<!-- qard-id: ap-9cd2de790bec6af42e38 -->
> [!qard]- What is alpha conversion?
> Renaming bound variables (e.g. to avoid name clashes), which preserves meaning.
