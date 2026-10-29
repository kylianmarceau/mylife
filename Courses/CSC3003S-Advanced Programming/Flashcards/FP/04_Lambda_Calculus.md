---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 04 — Lambda Calculus"
---

# FP 04 — Lambda Calculus

**Source note:** [Lambda Calculus](../../FP/04_Lambda_Calculus.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Syntax And Binding|Syntax And Binding]]
  - [[#Reduction|Reduction]]
  - [[#Encoding Values|Encoding Values]]
  - [[#Turing Machines Versus Lambda Calculus|Turing Machines Versus Lambda Calculus]]
  - [[#Shorthand Combinators And Termination|Shorthand Combinators And Termination]]
  - [[#Bootstrapping Further Computation|Bootstrapping Further Computation]]
  - [[#Binding And Substitution In Detail|Binding And Substitution In Detail]]

## Core Content

### Syntax And Binding

<!-- qard-id: ap-4bfa1ba50f56c654e906 -->
> [!qard]- What are the three basic lambda-calculus expression forms?
> A variable, an abstraction $\lambda x.M$, or an application $M\,N$.

<!-- qard-id: ap-209f5039749a688176a2 -->
> [!qard]- How are application and abstraction grouped?
> Application associates left: $f\,x\,y=(f\,x)\,y$. An abstraction's body extends as far right as its enclosing parentheses allow.

<!-- qard-id: ap-4a4f1948e58a5701d99e -->
> [!qard]- How does currying represent a function of two arguments?
> As nested unary functions: $\lambda x\,y.M$ abbreviates $\lambda x.(\lambda y.M)$.

<!-- qard-id: ap-a351868c7aed58136795 -->
> [!qard]- What distinguishes a free variable occurrence from a bound one?
> A bound occurrence refers to the nearest enclosing abstraction with that name. An occurrence with no such binder is free.

<!-- qard-id: ap-87fd4d517df542f08447 -->
> [!qard]- What is a closed lambda expression?
> One with no free variables.

<!-- qard-id: ap-8e76242591f944fbb4ee -->
> [!qard]- What is alpha equivalence?
> Equality up to consistent renaming of bound variables while preserving their bindings and leaving free variables unchanged.

### Reduction

<!-- qard-id: ap-a13963ec8a7b3df9c892 -->
> [!qard]- What is beta reduction?
> $(\lambda x.M)\,N\to M[x:=N]$: substitute $N$ for the free occurrences of $x$ in $M$, avoiding capture.

<!-- qard-id: ap-fa73e6db4ef9b2c68ad2 -->
> [!qard]- Why might alpha-renaming be necessary before beta reduction?
> To stop a free variable in the argument from becoming bound by an abstraction in the body. For example, $(\lambda x.\lambda y.x)\,y\to\lambda z.y$, not $\lambda y.y$.

<!-- qard-id: ap-ebcaee742ab7987c9d63 -->
> [!qard]- Why does $(\lambda x.x\,(\lambda x.x))\,a$ become $a\,(\lambda x.x)$?
> Only occurrences bound by the outer lambda are replaced; the inner lambda introduces its own `x`.

<!-- qard-id: ap-eb0bd2e3283be8e8018e -->
> [!qard]- What is beta-normal form?
> An expression containing no beta redexes. An expression may have no normal form, or a poor reduction strategy may fail to reach one that exists.

<!-- qard-id: ap-ddf6077879444cdfb8d0 -->
> [!qard]- Why does $\Omega=(\lambda x.x\,x)(\lambda x.x\,x)$ diverge?
> A beta step reproduces the same expression, so reduction repeats forever.

<!-- qard-id: ap-906645d310b9135b6da7 -->
> [!qard]- Why does $K\,I\,\Omega$ terminate under normal order but not strict evaluation?
> $K=\lambda x.\lambda y.x$ discards its second argument, leaving $I$. Strict evaluation attempts to evaluate the divergent $\Omega$ first.

### Encoding Values

<!-- qard-id: ap-694fdb93bbd7432b8dd0 -->
> [!qard]- How do Church Booleans represent TRUE and FALSE?
> $\mathrm{TRUE}=\lambda x.\lambda y.x$ chooses the first argument; $\mathrm{FALSE}=\lambda x.\lambda y.y$ chooses the second.

<!-- qard-id: ap-0e2e80972c25feaa59e9 -->
> [!qard]- How do Church conditionals and NOT work?
> $\mathrm{IF}\ b\ t\ e=b\ t\ e$; $\mathrm{NOT}\ b=b\ \mathrm{FALSE}\ \mathrm{TRUE}$. The Boolean acts as a selector.

### Turing Machines Versus Lambda Calculus

<!-- qard-id: ap-d3fedb7c1d3171d96db9 -->
> [!qard]- How do lambda calculus and Turing machines differ as computation models?
> Lambda calculus rewrites variables, abstractions and applications; a Turing machine updates tape and machine state. They have equivalent computational expressive power; the Church–Turing thesis connects such formal models to effective algorithmic computation.

### Shorthand Combinators And Termination

<!-- qard-id: ap-a08fb1972960589cb56e -->
> [!qard]- What do the standard combinators $I$, $M$ and $K$ do?
> $I=\lambda x.x$ returns its argument; $M=\lambda x.x\,x$ self-applies; $K=\lambda x.\lambda y.x$ returns the first of two arguments. Their names are shorthand, not extra core syntax.

### Bootstrapping Further Computation

<!-- qard-id: ap-8d53bd26a373a8be61e5 -->
> [!qard]- How are numbers and iteration built from lambda calculus's small core?
> A Church numeral $n$ applies a supplied function $n$ times to a starting value. Function encodings and recursion build arithmetic, repeated computation and control from the core forms.

### Binding And Substitution In Detail

<!-- qard-id: ap-d3304f77a6a8c0243729 -->
> [!qard]- Can one variable name have both free and bound occurrences in the same expression?
> Yes. Classify occurrences by their own enclosing binders rather than labelling the name globally; a binder's scope does not extend into a separate argument outside it.

<!-- qard-id: ap-0df2ae690fb90ed02e9a -->
> [!qard]- What does shadowing mean in a nested lambda?
> An inner binder with the same name captures occurrences within its own body; those occurrences no longer refer to the outer binder.

<!-- qard-id: ap-40798608fa88969bde85 -->
> [!qard]- What must a valid alpha conversion preserve?
> Which binder each occurrence refers to, all free variable identities, and the structure of the expression. Pick a fresh name to avoid capture or collisions.

<!-- qard-id: ap-8751f396235aa64f1729 -->
> [!qard]- Does beta reduction substitute inside a nested lambda that rebinds the same parameter name?
> No. Those inner occurrences belong to the inner binder, so substitution for the outer parameter stops at that binding boundary.

<!-- qard-id: ap-e56ca1cc520f9bfb57b7 -->
> [!qard]- Must beta reduction make an expression textually shorter?
> No. An argument can be duplicated, discarded or inserted into a larger body. Reduction is a semantic rewrite, not a promise of shorter notation.

<!-- qard-id: ap-07245507732807e9b593 -->
> [!qard]- How does a beta redex differ from an application already in normal form?
> A beta redex has an abstraction in function position, such as $(\lambda x.M)N$. An application like $x\,y$ cannot beta-reduce unless its subexpressions themselves contain redexes.

<!-- qard-id: ap-95dd5f275d4a86ed1ee4 -->
> [!qard]- Can an abstraction be in beta-normal form?
> Yes. For example $\lambda x.x$ contains no beta redex. Being a function does not itself mean an expression needs another reduction.

<!-- qard-id: ap-243ffb9029f6484fcc0d -->
> [!qard]- Why do Church Booleans work as control flow without a built-in conditional primitive?
> Each Boolean is already a function selecting one of two arguments; applying it to branch expressions chooses the result.

<!-- qard-id: ap-b4073072f4ed670eb1ba -->
> [!qard]- How does $\mathrm{NOT}\ b=b\ \mathrm{FALSE}\ \mathrm{TRUE}$ reverse a Church Boolean?
> TRUE selects the FALSE argument and FALSE selects the TRUE argument, so selection itself implements negation.
