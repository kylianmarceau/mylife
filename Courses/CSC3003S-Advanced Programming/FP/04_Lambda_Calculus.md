---
tags:
  - advanced-programming
---

# Lambda Calculus

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-4-Lambda Calculus - Copy (3).pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-4-Lambda%20Calculus%20-%20Copy%20%283%29.pdf), James Gain, University of Cape Town, pages 1–22
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Church's lambda calculus: notation, currying, scope, alpha equivalence, beta reduction, normal form, lazy versus strict reduction order, named combinators and Church Booleans.

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
  - [[#Beta Reduction|Beta Reduction]]
  - [[#Normal Form And Divergence|Normal Form And Divergence]]
  - [[#Order Of Reductions|Order Of Reductions]]
  - [[#Shorthand Combinators And Termination|Shorthand Combinators And Termination]]
  - [[#Church Booleans And Conditionals|Church Booleans And Conditionals]]
  - [[#Logical NOT And Bootstrapping|Logical NOT And Bootstrapping]]

---

## Core Content

### What Is The Lambda Calculus?

#### Definitions

> **Lambda calculus**: A very small, precisely defined programming language based on first-class anonymous mathematical functions, developed by Alonzo Church in the 1930s. It is the "machine code" basis of functional languages.

- Its small size makes it easier to prove properties about programs.
- It must be bootstrapped significantly (Booleans, numbers, recursion) to be practical.

### Turing Machines Versus Lambda Calculus

| | Turing machine | Lambda calculus |
|---|---|---|
| Components | Infinite tape, read/write head, state register, transition rules | Variables, function abstraction, function application |
| Operation | Imperatively mutates state step by step | Functionally rewrites expressions via reduction |

Both are universal theoretical models of computation and are strictly equivalent. By the **Church–Turing thesis**, both can solve any real-world problem that has a step-by-step algorithm.

### Core Notation

The grammar in EBNF (`|` means OR, `{ }` means repetition):

```text
lcletter    ⇐  a | b | c | ... | z
name        ⇐  lcletter {lcletter}
expression  ⇐  name | function | application
function    ⇐  λ name . expression
application ⇐  expression expression
```

#### Definitions

> **Name (variable)**: A collection of one or more letters.

> **Function (abstraction)**: Defines a one-to-one mapping from an argument to an expression.

> **Application**: Function invocation — calling the first expression (the function) with the second expression (the argument).

> **Expression**: The overarching concept; names, functions and applications are all expressions, so functions are first-class.

### Function Components

![Parts of a lambda function](../../../diagrams/CSC3003S-Advanced%20Programming/FP/04_Lambda_Calculus/function-components.svg)

*In $\lambda x.\ x\,y$, the lambda introduces the function, $x$ is the parameter, and $x\,y$ is the body.*

| Part | Role |
|---|---|
| Lambda ($\lambda$) | Indicates that an anonymous function follows |
| Name | The single parameter; it binds to identical names in the body |
| `.` | Separates the parameter from the body |
| Body | The expression returned when the lambda is applied to an argument |

### Multi-Argument Functions And Currying

#### Definitions

> **Currying**: Representing a function of several arguments as nested single-argument functions, each taking the next parameter.

Core lambda calculus does not support parameter lists. Instead, nest functions and use a shorthand:

$$
\lambda x\,y.\ x\,y \quad \text{is shorthand for} \quad \lambda x.\ (\lambda y.\ x\,y)
$$

Brackets are not part of the core notation, but they help interpretation.

Example: the curried form of $\lambda x\,y\,z.\ y\,x\,z$ is $\lambda x.\ (\lambda y.\ (\lambda z.\ y\,x\,z))$.

### Scope: Bound And Free Variables

#### Definitions

> **Scope**: In $\lambda x.\ t$, the scope of $x$ is the body $t$. All names are local to their function definitions.

> **Bound variable**: An occurrence of $x$ inside the body $t$ of a function $\lambda x.\ t$.

> **Free variable**: A variable occurrence that is not bound by any enclosing lambda.

> **Closed expression**: An expression with no free variables.

Examples:

| Expression | Bound | Free |
|---|---|---|
| $(\lambda x.\ y\,x)(\lambda y.\ x\,y)$ | $x$ in the first function; $y$ in the second | $y$ in the first function; $x$ in the second |
| $\lambda x.\ (\lambda y.\ x\,y)$ | both $x$ and $y$ | none (closed) |

**Quiz**: in $\lambda x.\ y\,(\lambda y.\ (\lambda x.\ x\,y\,z))$, number the occurrences 1–7 left to right ($x_1$ parameter, $y_2$, $y_3$ parameter, $x_4$ parameter, $x_5$, $y_6$, $z_7$).

| Occurrence | Status |
|---|---|
| $y_2$ | Free (it is outside $\lambda y$) |
| $x_5$ | Bound to the inner parameter $x_4$, not the outer $x_1$ |
| $y_6$ | Bound to $y_3$ |
| $z_7$ | Free |

Answer: 2 free, 7 free, 6 bound to 3, 5 bound to 4.

![Binding in a nested expression](../../../diagrams/CSC3003S-Advanced%20Programming/FP/04_Lambda_Calculus/scope-binding.svg)

*Each occurrence binds to the nearest enclosing lambda with the same name; the inner $\lambda x$ shadows the outer one.*

### Alpha Equivalence

#### Definitions

> **Alpha equivalence**: Two expressions are equivalent if they differ only by renaming bound variables, as long as free variables are unchanged.

> **Alpha conversion**: The act of renaming bound variables.

The same name can be bound in different scopes, which is confusing. Bound names are arbitrary, so they can be renamed to be unique:

$$
\lambda x.\ (\lambda y.\ x\,y\,z) \;=_\alpha\; \lambda b.\ (\lambda a.\ b\,a\,z)
$$

$z$ is free and must stay $z$.

**Quiz**: which is alpha-equivalent to $\lambda x\,y\,z.\ z\,x$ (third argument applied to the first)?

| Candidate | Equivalent? | Reason |
|---|---|---|
| $\lambda x.\ (\lambda y.\ \lambda z.\ z)$ | No | Body is just $z$ |
| $\lambda t\,o\,s.\ s\,t$ | **Yes** | Third applied to first |
| $\lambda m\,n\,p.\ m\,n$ | No | First applied to second |
| $\lambda z\,y\,x.\ z\,x$ | No | First applied to third |

### Beta Reduction

#### Definitions

> **β-reduction**: Carrying out an application by replacing every free occurrence of the bound variable in the function body with the argument.

$$
(\lambda x.\ M)\,N \;\to_\beta\; M[x := N]
$$

$M[x := N]$ means "$M$ with every free $x$ replaced by $N$". β-reduction replaces a redex with its evaluated form. Paradoxically, it may not make the expression shorter.

Example: $(\lambda x.\ x)\,y \to_\beta x[x := y] = y$.

Steps:

1. Separate out the function body.
2. Substitute the argument for the free occurrences of the parameter.
3. The result is the new expression.

More examples:

| Expression | Result | Note |
|---|---|---|
| $(\lambda x.\ x\,(\lambda x.\ x))\,(a\,b)$ | $(a\,b)\,(\lambda x.\ x)$ | The inner $x$ is bound by the inner lambda, so it is not free in the outer body and is not replaced |
| $(\lambda x.\ x\,x)(\lambda x.\ x\,x)$ | $(\lambda x.\ x\,x)(\lambda x.\ x\,x)$ | Reduces to itself forever |

### Normal Form And Divergence

#### Definitions

> **β-normal form**: An expression containing no more redexes, so β-reduction cannot continue. Reaching it is equivalent to program termination.

> **Divergence**: When a lambda expression cannot be reduced to normal form — the equivalent of an infinite loop.

$(\lambda x.\ x\,x)(\lambda x.\ x\,x)$ diverges.

### Order Of Reductions

| Order | Rule | Argument handling |
|---|---|---|
| **Lazy** | Always choose the leftmost / outermost redex | Don't evaluate the argument if it can be avoided |
| **Strict** | Always choose the rightmost / innermost redex | Evaluate the argument before passing it to the function |

Example: $(\lambda z.\ z\,a)\,((\lambda x.\ x\,x)\,\lambda y.\ y)$

| Lazy | Strict |
|---|---|
| $\to_\beta ((\lambda x.\ x\,x)(\lambda y.\ y))\,a$ | $\to_\beta (\lambda z.\ z\,a)\,((\lambda y.\ y)(\lambda y.\ y))$ |
| $\to_\beta ((\lambda y.\ y)(\lambda y.\ y))\,a$ | $\to_\beta (\lambda z.\ z\,a)(\lambda y.\ y)$ |
| $\to_\beta (\lambda y.\ y)\,a$ | $\to_\beta (\lambda y.\ y)\,a$ |
| $\to_\beta a$ | $\to_\beta a$ |

![Lazy versus strict reduction](../../../diagrams/CSC3003S-Advanced%20Programming/FP/04_Lambda_Calculus/reduction-orders.svg)

*Lazy substitutes the unevaluated argument first; strict evaluates the argument first. Both reach $a$.*

**Quiz**: the normal form of $(\lambda x.\ \lambda y.\ x)(\lambda x.\ x)(\lambda z.\ z\,z)(\lambda z.\ z\,z)$ under lazy evaluation is $(\lambda z.\ z\,z)$ (see [Lambda Calculus Exercises](04A_Lambda_Calculus_Exercises.md)). Application associates left, so the two $(\lambda z.\ z\,z)$ terms are separate arguments rather than an $\Omega$; strict evaluation gives the same result here.

### Shorthand Combinators And Termination

For sanity, lambda functions can be named with aliases. These are a convenience, not part of the formal calculus.

| Name | Definition | Behaviour |
|---|---|---|
| Identity $I$ | $\lambda x.\ x$ | Returns its argument |
| Mockingbird $M$ | $\lambda x.\ x\,x$ | Self-application |
| Discarding $K$ | $\lambda x.\ \lambda y.\ x$ | Returns the first of two arguments |
| Infinite loop $\Omega$ | $(\lambda z.\ z\,z)(\lambda z.\ z\,z)$ | Reduces to itself forever |

**Reduce $K\,I\,\Omega \equiv (\lambda x.\ \lambda y.\ x)(\lambda x.\ x)((\lambda z.\ z\,z)(\lambda z.\ z\,z))$:**

| Lazy | Strict |
|---|---|
| $\to_\beta (\lambda y.\ \lambda x.\ x)\,((\lambda z.\ z\,z)(\lambda z.\ z\,z))$ | Must first evaluate the argument $\Omega$ |
| $\to_\beta \lambda x.\ x \equiv I$ | $\Omega \to_\beta \Omega \to_\beta \dots$ |
| Discards $\Omega$ and terminates | Repeats $\Omega$ forever |

Lazy evaluation has the properties seen earlier (it is likelier to terminate). In fact, this is where functional programming learnt it from.

### Church Booleans And Conditionals

To compute anything useful we need Boolean logic, arithmetic, loops and selection, all built from functions. A Boolean is just a switch:

| Name | Definition | Behaviour |
|---|---|---|
| $\text{TRUE}$ | $\lambda x.\ \lambda y.\ x$ | Takes two inputs, returns the first |
| $\text{FALSE}$ | $\lambda x.\ \lambda y.\ y$ | Takes two inputs, returns the second |
| $\text{IFTHEN}$ | $\lambda b.\ \lambda t.\ \lambda e.\ b\,t\,e$ | $b$ is a Boolean, $t$ the then-branch, $e$ the else-branch |

$$
\begin{aligned}
\text{IFTHEN}\ \text{TRUE}\ a\ b &\equiv (\lambda b.\ \lambda t.\ \lambda e.\ b\,t\,e)\ \text{TRUE}\ a\ b \\
&\to_\beta (\lambda t.\ \lambda e.\ \text{TRUE}\,t\,e)\ a\ b \\
&\to_\beta (\lambda e.\ \text{TRUE}\,a\,e)\ b \\
&\to_\beta \text{TRUE}\ a\ b \equiv (\lambda x.\ \lambda y.\ x)\ a\ b \to_\beta^* a
\end{aligned}
$$

$$
\text{IFTHEN}\ \text{FALSE}\ a\ b \to_\beta^* \text{FALSE}\ a\ b \equiv (\lambda x.\ \lambda y.\ y)\ a\ b \to_\beta^* b
$$

### Logical NOT And Bootstrapping

$$
\text{NOT} \equiv \lambda b.\ b\ \text{FALSE}\ \text{TRUE}
$$

| Input | Reduction | Result |
|---|---|---|
| $\text{NOT TRUE}$ | $\to_\beta \text{TRUE FALSE TRUE} \to_\beta$ | $\text{FALSE}$ |
| $\text{NOT FALSE}$ | $\to_\beta \text{FALSE FALSE TRUE} \to_\beta$ | $\text{TRUE}$ |

Other computation is bootstrapped the same way:

- **Church numerals**: a number $N$ is a function applied $N$ times.
- **Loops** come from recursion, with Church Booleans for termination.
- The aliases are then used in further computation.

**Summary of the theory lectures**: functions rule everything; lazy evaluation is more likely to terminate and avoids unnecessary computation; recursion is how FP realises loops (use tail recursion to avoid stack overflow); lambda calculus is FP's theoretical foundation.
