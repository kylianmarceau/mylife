---
tags:
  - advanced-programming
---

# Lambda Calculus Exercises

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-4A-Lambda Calculus Exercises.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-4A-Lambda%20Calculus%20Exercises.pdf), James Gain, University of Cape Town, pages 1–5
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Three worked lambda calculus exercises: lazy reduction with a discarding function, proving Church AND correct, and showing $I\,M \neq M\,I$. Theory is in [Lambda Calculus](04_Lambda_Calculus.md).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Reference Definitions|Reference Definitions]]
  - [[#Exercise 1: Lazy Reduction|Exercise 1: Lazy Reduction]]
  - [[#Exercise 2: Church AND|Exercise 2: Church AND]]
  - [[#Exercise 3: I M Versus M I|Exercise 3: I M Versus M I]]

---

## Core Content

### Reference Definitions

| Name | Definition |
|---|---|
| $I$ (identity) | $\lambda x.\ x$ |
| $M$ (mockingbird) | $\lambda x.\ x\,x$ (written $\lambda z.\ z\,z$ below) |
| $\text{TRUE}$ | $\lambda x.\ \lambda y.\ x$ |
| $\text{FALSE}$ | $\lambda x.\ \lambda y.\ y$ |
| $\text{AND}$ | $\lambda a.\ \lambda b.\ a\,b\,\text{FALSE}$ |

Application associates to the left: $f\,a\,b$ means $(f\,a)\,b$.

### Exercise 1: Lazy Reduction

**Task**: show that $(\lambda x.\ \lambda y.\ x)(\lambda x.\ x)(\lambda z.\ z\,z)(\lambda z.\ z\,z)$ reduces to $(\lambda z.\ z\,z)$ by lazy evaluation.

$$
\begin{aligned}
&(\lambda x.\ \lambda y.\ x)(\lambda x.\ x)(\lambda z.\ z\,z)(\lambda z.\ z\,z) \\
\to_\beta\ &(\lambda y.\ \lambda x.\ x)(\lambda z.\ z\,z)(\lambda z.\ z\,z) \\
\to_\beta\ &(\lambda x.\ x)(\lambda z.\ z\,z) \\
\to_\beta\ &(\lambda z.\ z\,z)
\end{aligned}
$$

1. Substitute $(\lambda x.\ x)$ for $x$ in $\lambda y.\ x$.
2. The next argument $(\lambda z.\ z\,z)$ is dropped, because $y$ does not appear in the body $\lambda x.\ x$.
3. The identity function returns its argument $(\lambda z.\ z\,z)$ unchanged. This contains no redex, so it is the normal form.

### Exercise 2: Church AND

**Task**: prove that $\text{AND} \equiv \lambda a.\ \lambda b.\ a\,b\,\text{FALSE}$ behaves as expected.

Idea: if $a$ is TRUE it returns its first argument, $b$; if $a$ is FALSE it returns its second argument, FALSE. There are four cases.

**AND TRUE TRUE**:

$$
\begin{aligned}
(\lambda a.\ \lambda b.\ a\,b\,\text{FALSE})\ \text{TRUE}\ \text{TRUE}
&\to_\beta (\lambda b.\ \text{TRUE}\,b\,\text{FALSE})\ \text{TRUE} \\
&\to_\beta \text{TRUE}\ \text{TRUE}\ \text{FALSE} \\
&\equiv (\lambda x.\ \lambda y.\ x)\ \text{TRUE}\ \text{FALSE} \\
&\to_\beta (\lambda y.\ \text{TRUE})\ \text{FALSE} \\
&\to_\beta \text{TRUE}
\end{aligned}
$$

The other cases follow the same way:

| Case | After substituting $a, b$ | Result |
|---|---|---|
| AND TRUE TRUE | $\text{TRUE}\ \text{TRUE}\ \text{FALSE}$ | TRUE (first argument) |
| AND TRUE FALSE | $\text{TRUE}\ \text{FALSE}\ \text{FALSE}$ | FALSE (first argument) |
| AND FALSE TRUE | $\text{FALSE}\ \text{TRUE}\ \text{FALSE}$ | FALSE (second argument) |
| AND FALSE FALSE | $\text{FALSE}\ \text{FALSE}\ \text{FALSE}$ | FALSE (second argument) |

### Exercise 3: I M Versus M I

**Task**: show that under both strict and lazy evaluation $I\,M \neq M\,I$.

**$I\,M$**:

$$
I\,M \equiv (\lambda x.\ x)(\lambda z.\ z\,z) \to_\beta (\lambda z.\ z\,z)
$$

**$M\,I$**:

$$
M\,I \equiv (\lambda z.\ z\,z)(\lambda x.\ x) \to_\beta (\lambda x.\ x)(\lambda x.\ x) \to_\beta (\lambda x.\ x)
$$

| Expression | Normal form |
|---|---|
| $I\,M$ | $\lambda z.\ z\,z$ ($= M$) |
| $M\,I$ | $\lambda x.\ x$ ($= I$) |

The normal forms differ, so $I\,M \neq M\,I$.

Strict evaluation behaves exactly the same here. With a single application and no nested redexes in the argument, there is only one possible order of β-reduction. In general, if both orders terminate, they give the same final result.
