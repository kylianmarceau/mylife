---
tags:
  - advanced-programming
---

# Lambda Calculus

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-4-Lambda Calculus - Copy (3).pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-4-Lambda%20Calculus%20-%20Copy%20%283%29.pdf), James Gain, University of Cape Town, PDF pages 1–22  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes on lambda calculus syntax, scope, β-reduction, reduction order, and Church Booleans. Practice solutions are in [Lambda Calculus Exercises](04A_Lambda_Calculus_Exercises.md).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is The Lambda Calculus?|What Is The Lambda Calculus?]]
  - [[#Turing Machines Versus Lambda Calculus|Turing Machines Versus Lambda Calculus]]
  - [[#Core Notation|Core Notation]]
  - [[#Function Components|Function Components]]
  - [[#Multi-Argument Functions And Currying|Multi-Argument Functions And Currying]]
  - [[#Scope: Bound And Free Variables|Scope: Bound And Free Variables]]
  - [[#Alpha Equivalence|Alpha Equivalence]]
  - [[#Application And β-Reduction|Application And β-Reduction]]
  - [[#Normal Form And Divergence|Normal Form And Divergence]]
  - [[#Order Of Reductions|Order Of Reductions]]
  - [[#Shorthand Combinators And Termination|Shorthand Combinators And Termination]]
  - [[#Church Booleans And Conditionals|Church Booleans And Conditionals]]
  - [[#Bootstrapping Further Computation|Bootstrapping Further Computation]]

---

## Core Content

### What Is The Lambda Calculus?

#### Definitions

> **Lambda calculus**: A very small, precisely defined programming language based on first-class anonymous mathematical functions, developed by Alonzo Church in the 1930s.

- It is the "machine code" basis of functional languages.
- Its small size makes properties easier to prove.
- It must be heavily **bootstrapped** (building richer constructs out of its few primitives) to be practical.

### Turing Machines Versus Lambda Calculus

| | Turing machines | Lambda calculus |
|---|---|---|
| Components | Infinite tape, read/write head, state register, transition rules | Variables, function abstraction, function application |
| Operation | Imperatively mutate state step by step | Functionally rewrite expressions by reduction |

- Both are **universal** theoretical models of computation and are strictly equivalent.
- By the **Church–Turing thesis**, both can solve any real-world problem that has a step-by-step algorithm.

### Core Notation

The grammar in EBNF (`|` means OR, `{ }` means repetition):

```ebnf
lcletter    ::= a | b | c | ... | z
name        ::= lcletter {lcletter}
expression  ::= name | function | application
function    ::= λ name . expression
application ::= expression expression
```

#### Definitions

> **Name (variable)**: A sequence of one or more letters.

> **Function (abstraction)**: A one-to-one mapping from an argument to an expression.

> **Application**: Function invocation: calling a function (the first expression) with an argument (the second expression).

> **Expression**: The overarching concept. Functions are expressions, so functions are first-class.

### Function Components

![Parts of a lambda abstraction](../../../diagrams/CSC3003S-Advanced%20Programming/FP/04_Lambda_Calculus/function-components.svg)

*In $\lambda x.\,x\,y$, the λ introduces an anonymous function, $x$ is its single parameter, and $x\,y$ is the body.*

| Part | Role |
|---|---|
| **Lambda** $\lambda$ | Indicates that an anonymous function follows |
| **Name** | The *single* parameter; binds identical names in the body |
| **Body** | The expression returned when the lambda is applied; `.` separates parameter from body |

### Multi-Argument Functions And Currying

#### Definitions

> **Currying**: Representing a multi-argument function as nested single-argument functions, each taking the next parameter.

Core lambda calculus does not support parameter lists. Instead, nest functions and use shorthand:

$$
\lambda x\,y.\;x\,y \quad\text{is shorthand for}\quad \lambda x.\,(\lambda y.\;x\,y)
$$

Brackets are not core syntax but help interpretation. Curried version of $\lambda x\,y\,z.\;y\,x\,z$:

$$
\lambda x.\,(\lambda y.\,(\lambda z.\;y\,x\,z))
$$

### Scope: Bound And Free Variables

#### Definitions

> **Scope**: In $\lambda x.\,t$, the scope of $x$ is $t$. All names are local to function definitions.

> **Bound occurrence**: An occurrence of $x$ is bound if it occurs in the body $t$ of a function $\lambda x.\,t$ with parameter $x$.

> **Free occurrence**: An occurrence that is not bound.

> **Closed expression**: An expression with no free variables.

| Expression | Analysis |
|---|---|
| $(\lambda x.\;y\,x)(\lambda y.\;x\,y)$ | In the first function, $y$ is free and $x$ is bound. In the second, $x$ is free and $y$ is bound. |
| $\lambda x.\,(\lambda y.\;x\,y)$ | Both $x$ and $y$ are bound, so the expression is closed. |

An occurrence binds to the **nearest enclosing** parameter with the same name. Quiz: label the names in $\lambda x.\;y\,(\lambda y.\,(\lambda x.\;x\,y\,z))$ as $1$–$7$ from left to right.

![Binding in the quiz expression](../../../diagrams/CSC3003S-Advanced%20Programming/FP/04_Lambda_Calculus/scope-binding.svg)

*Answer: $2$ and $7$ are free, $6$ is bound to $3$, and $5$ is bound to $4$. The inner $\lambda x$ shadows the outer one.*

### Alpha Equivalence

#### Definitions

> **Alpha equivalence** ($=_\alpha$): Two expressions are equivalent if they differ only in the names of bound variables, provided free variables are unchanged.

> **Alpha conversion**: Renaming bound variables, for example to make names unique and avoid confusion between scopes.

$$
\lambda x.\,(\lambda y.\;x\,y\,z) \;=_\alpha\; \lambda b.\,(\lambda a.\;b\,a\,z)
$$

$z$ is free, so it must stay $z$.

Quiz: which expression is alpha-equivalent to $\lambda x\,y\,z.\;z\,x$?

| Option | Equivalent? | Reason |
|---|---|---|
| $\lambda x.\,(\lambda y.\,(\lambda z.\;z))$ | No | Body drops $x$ |
| $\lambda m\,n\,p.\;m\,n$ | No | Body uses the first and second parameters |
| $\lambda t\,o\,s.\;s\,t$ | **Yes** | Third parameter applied to the first |
| $\lambda z\,y\,x.\;z\,x$ | No | First parameter applied to the third (reversed) |

### Application And β-Reduction

#### Definitions

> **β-reduction**: Carrying out an application by replacing every free occurrence of the bound variable in the function body with the argument.

$$
(\lambda x.\,M)\,N \;\xrightarrow{\beta}\; M[x := N]
$$

$M[x:=N]$ means "$M$ with every free $x$ replaced by $N$". For example:

$$
(\lambda x.\,x)\,y \;\xrightarrow{\beta}\; x[x:=y] \;\to\; y
$$

β-reduction replaces a redex with its evaluated form. It may not actually shorten the expression.

The method has three steps:

1. Separate out the function body.
2. Substitute the argument into the **free** occurrences of the parameter.
3. The result is the new expression.

$$
(\lambda x.\,x\,(\lambda x.\,x))\,(a\,b) \;\xrightarrow{\beta}\; (a\,b)\,(\lambda x.\,x)
$$

The innermost $x$ is bound by the inner $\lambda x$, so it is not free in the outer body and is not replaced. Writing $(a\,b)\,(\lambda (a\,b).\,(a\,b))$ is wrong.

$$
(\lambda x.\,x\,x)(\lambda x.\,x\,x) \;\xrightarrow{\beta}\; (\lambda x.\,x\,x)(\lambda x.\,x\,x) \;\xrightarrow{\beta}\; \cdots
$$

This expression reduces to itself forever.

### Normal Form And Divergence

#### Definitions

> **β-normal form**: An expression with no more redexes, so β-reduction cannot continue. This corresponds to program termination.

> **Divergence**: When an expression cannot be reduced to normal form. This corresponds to an infinite loop.

### Order Of Reductions

| Lazy | Strict |
|---|---|
| Always choose the **leftmost / outermost** redex | Always choose the **rightmost / innermost** redex |
| Do not evaluate the argument if it can be avoided | Evaluate the argument before passing it to the function |

![Lazy versus strict reduction order](../../../diagrams/CSC3003S-Advanced%20Programming/FP/04_Lambda_Calculus/reduction-orders.svg)

*Both orders reach `a` for this expression, but they reduce different redexes at each step.*

Quiz: the normal form of $(\lambda x.\lambda y.\,x)\,(\lambda x.\,x)\,(\lambda z.\,z\,z)\,(\lambda z.\,z\,z)$ under lazy evaluation is $(\lambda z.\,z\,z)$. The full working is in [Lambda Calculus Exercises](04A_Lambda_Calculus_Exercises.md).

> [!warning] <span style="color:#ffc778">Strict version and bracketing</span>
> Application is left-associative. Read exactly as written, the last two terms are separate arguments, and strict evaluation also reaches $(\lambda z.\,z\,z)$. If the last two terms are grouped as $\Omega=((\lambda z.\,z\,z)(\lambda z.\,z\,z))$, as in $K\,I\,\Omega$ below, strict evaluation diverges.

### Shorthand Combinators And Termination

Named aliases are a convenience only; they are not part of formal lambda calculus.

| Alias | Name | Definition |
|---|---|---|
| $I$ | Identity | $\lambda x.\,x$ |
| $M$ | Mockingbird (self-application) | $\lambda x.\,x\,x$ |
| $K$ | Discarding | $\lambda x.\,\lambda y.\,x$ |
| $\Omega$ | Infinite loop | $(\lambda z.\,z\,z)(\lambda z.\,z\,z)$ |

Reduce $K\,I\,\Omega \equiv (\lambda x.\lambda y.\,x)\,(\lambda x.\,x)\,((\lambda z.\,z\,z)(\lambda z.\,z\,z))$:

**Lazy** discards $\Omega$:

$$
\begin{aligned}
K\,I\,\Omega &\xrightarrow{\beta} (\lambda y.\,\lambda x.\,x)\,((\lambda z.\,z\,z)(\lambda z.\,z\,z)) \\
&\xrightarrow{\beta} \lambda x.\,x \;\equiv\; I
\end{aligned}
$$

**Strict** reduces the innermost redex, $\Omega$ itself, which reduces to $\Omega$ again:

$$
K\,I\,\Omega \xrightarrow{\beta} K\,I\,\Omega \xrightarrow{\beta} \cdots \quad\text{(repeats }\Omega\text{ infinitely)}
$$

Lazy evaluation is more likely to terminate. Functional programming took this property from lambda calculus.

### Church Booleans And Conditionals

#### Definitions

> **Church Booleans**: Booleans encoded as functions that choose between two inputs. A Boolean is just a switch.

$$
\mathrm{TRUE} \equiv \lambda x.\,\lambda y.\,x \qquad \mathrm{FALSE} \equiv \lambda x.\,\lambda y.\,y
$$

- TRUE takes two inputs and returns the first.
- FALSE takes two inputs and returns the second.

$$
\mathrm{IFTHEN} \equiv \lambda b.\,\lambda t.\,\lambda e.\;b\,t\,e
$$

Here $b$ is a Boolean, $t$ the then-branch and $e$ the else-branch.

$$
\begin{aligned}
\mathrm{IFTHEN}\;\mathrm{TRUE}\;a\;b &\equiv (\lambda b.\lambda t.\lambda e.\;b\,t\,e)\;\mathrm{TRUE}\;a\;b \\
&\xrightarrow{\beta} (\lambda t.\lambda e.\;\mathrm{TRUE}\,t\,e)\;a\;b \\
&\xrightarrow{\beta} (\lambda e.\;\mathrm{TRUE}\,a\,e)\;b \\
&\xrightarrow{\beta} \mathrm{TRUE}\;a\;b \equiv (\lambda x.\lambda y.\,x)\;a\;b \xrightarrow{\beta\beta} a
\end{aligned}
$$

With FALSE the same steps give $\mathrm{FALSE}\;a\;b \equiv (\lambda x.\lambda y.\,y)\;a\;b \xrightarrow{\beta\beta} b$.

$$
\mathrm{NOT} \equiv \lambda b.\;b\;\mathrm{FALSE}\;\mathrm{TRUE}
$$

$$
\begin{aligned}
\mathrm{NOT}\;\mathrm{TRUE} &\xrightarrow{\beta} \mathrm{TRUE}\;\mathrm{FALSE}\;\mathrm{TRUE} \xrightarrow{\beta} \mathrm{FALSE} \\
\mathrm{NOT}\;\mathrm{FALSE} &\xrightarrow{\beta} \mathrm{FALSE}\;\mathrm{FALSE}\;\mathrm{TRUE} \xrightarrow{\beta} \mathrm{TRUE}
\end{aligned}
$$

### Bootstrapping Further Computation

- Other computation is built the same way as Church Booleans.
- **Church numerals**: a number $N$ is a function applied $N$ times.
- **Loops** come from recursion, with Church Booleans deciding termination.
- Once defined, the aliases are used in further computation.

> [!tip] <span style="color:#5ad4b5">Takeaway</span>
> In FP, functions rule everything. Lazy evaluation is more likely to terminate and skips unnecessary work. Recursion replaces loops, with tail recursion avoiding stack overflow. Lambda calculus is the theory underneath all of it.
