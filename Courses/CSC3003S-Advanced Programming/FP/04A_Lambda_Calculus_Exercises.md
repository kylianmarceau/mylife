---
tags:
  - advanced-programming
---

# Lambda Calculus Exercises

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-4A-Lambda Calculus Exercises.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-4A-Lambda%20Calculus%20Exercises.pdf), James Gain, University of Cape Town, PDF pages 1–5  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> The three set exercises and their full solutions. Theory is in [Lambda Calculus](04_Lambda_Calculus.md).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Definitions Used|Definitions Used]]
  - [[#Exercise 1: Lazy Reduction Of K I M M|Exercise 1: Lazy Reduction Of K I M M]]
  - [[#Exercise 2: Church AND|Exercise 2: Church AND]]
  - [[#Exercise 3: I M Versus M I|Exercise 3: I M Versus M I]]

---

## Core Content

### Definitions Used

| Alias | Definition | Behaviour |
|---|---|---|
| $I$ | $\lambda x.\,x$ | Returns its argument unchanged |
| $M$ | $\lambda z.\,z\,z$ | Applies its argument to itself |
| $K$ / TRUE | $\lambda x.\,\lambda y.\,x$ | Returns the first of two inputs |
| FALSE | $\lambda x.\,\lambda y.\,y$ | Returns the second of two inputs |

### Exercise 1: Lazy Reduction Of K I M M

Show that $(\lambda x.\lambda y.\,x)\,(\lambda x.\,x)\,(\lambda z.\,z\,z)\,(\lambda z.\,z\,z)$ reduces to $(\lambda z.\,z\,z)$ by lazy evaluation.

$$
\begin{aligned}
&(\lambda x.\lambda y.\,x)\,(\lambda x.\,x)\,(\lambda z.\,z\,z)\,(\lambda z.\,z\,z) \\
\xrightarrow{\beta}\;& (\lambda y.\,\lambda x.\,x)\,(\lambda z.\,z\,z)\,(\lambda z.\,z\,z) \\
\xrightarrow{\beta}\;& (\lambda x.\,x)\,(\lambda z.\,z\,z) \\
\xrightarrow{\beta}\;& (\lambda z.\,z\,z)
\end{aligned}
$$

1. Substitute $(\lambda x.\,x)$ for $x$ in the outer function.
2. The argument $(\lambda z.\,z\,z)$ is dropped because $y$ does not appear in the body.
3. The identity function returns its argument unchanged.

### Exercise 2: Church AND

Prove that $\mathrm{AND} \equiv \lambda a.\,\lambda b.\;a\;b\;\mathrm{FALSE}$ has the expected behaviour.

There are four cases. The source works the first:

$$
\begin{aligned}
\mathrm{AND}\;\mathrm{TRUE}\;\mathrm{TRUE} &\equiv (\lambda a.\lambda b.\;a\,b\,\mathrm{FALSE})\;\mathrm{TRUE}\;\mathrm{TRUE} \\
&\xrightarrow{\beta} (\lambda b.\;\mathrm{TRUE}\,b\,\mathrm{FALSE})\;\mathrm{TRUE} \\
&\xrightarrow{\beta} \mathrm{TRUE}\;\mathrm{TRUE}\;\mathrm{FALSE} \\
&\equiv (\lambda x.\lambda y.\,x)\;\mathrm{TRUE}\;\mathrm{FALSE} \\
&\xrightarrow{\beta} (\lambda y.\,\mathrm{TRUE})\;\mathrm{FALSE} \\
&\xrightarrow{\beta} \mathrm{TRUE}
\end{aligned}
$$

The other cases follow the same two steps to $a\;b\;\mathrm{FALSE}$:

| Case | After substitution | Result | Why |
|---|---|---|---|
| AND TRUE TRUE | TRUE TRUE FALSE | TRUE | TRUE picks the first input |
| AND TRUE FALSE | TRUE FALSE FALSE | FALSE | TRUE picks the first input |
| AND FALSE TRUE | FALSE TRUE FALSE | FALSE | FALSE picks the second input |
| AND FALSE FALSE | FALSE FALSE FALSE | FALSE | FALSE picks the second input |

The result is TRUE only when both inputs are TRUE, which is the AND truth table. If $a$ is TRUE the answer is $b$; otherwise it is FALSE.

### Exercise 3: I M Versus M I

Show that under both strict and lazy evaluation $I\,M \neq M\,I$.

**$I\,M$:**

$$
I\,M \equiv (\lambda x.\,x)(\lambda z.\,z\,z) \xrightarrow{\beta} (\lambda z.\,z\,z) = M
$$

**$M\,I$:**

$$
M\,I \equiv (\lambda z.\,z\,z)(\lambda x.\,x) \xrightarrow{\beta} (\lambda x.\,x)(\lambda x.\,x) \xrightarrow{\beta} (\lambda x.\,x) = I
$$

$M \neq I$, so $I\,M \neq M\,I$.

- Strict evaluation behaves exactly the same here: a single application with no nested redexes has only one possible order of β-reduction.
- In general, if both orders terminate they give the same final result.
