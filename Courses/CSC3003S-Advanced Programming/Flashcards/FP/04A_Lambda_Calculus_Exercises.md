---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 04A — Lambda Calculus Exercises"
---

# FP 04A — Lambda Calculus Exercises

**Source note:** [Lambda Calculus Exercises](../../FP/04A_Lambda_Calculus_Exercises.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Reduction Techniques|Reduction Techniques]]
  - [[#Church AND|Church AND]]
  - [[#I M Versus M I|I M Versus M I]]

## Core Content

### Reduction Techniques

<!-- qard-id: ap-78529bf29555d1e66299 -->
> [!qard]- How does application associate in the lambda calculus?
> To the left: $f\,a\,b=(f\,a)\,b$.

<!-- qard-id: ap-ce38ddcba6f4a8715ebf -->
> [!qard]- Why is the second argument dropped when reducing $(\lambda y.\ \lambda x.\,x)\,N$?
> $y$ doesn't occur in the body, so substitution removes $N$.

<!-- qard-id: ap-150ca188bb7081a2d5d1 -->
> [!qard]- What does the identity function do when applied?
> Returns its argument unchanged: $(\lambda x.\,x)\,N\to_\beta N$.

### Church AND

<!-- qard-id: ap-b7f0851a0b930d931287 -->
> [!qard]- Define AND with Church Booleans.
> $\text{AND}=\lambda a.\lambda b.\ a\,b\ \text{FALSE}$.

<!-- qard-id: ap-a2d0ffe6633561ea1f17 -->
> [!qard]- Why does $\text{AND}=\lambda a.\lambda b.\,a\,b\,\text{FALSE}$ work?
> If $a$ is TRUE it returns $b$; if FALSE it returns FALSE.

<!-- qard-id: ap-a67722a3e2d7ccaaf46c -->
> [!qard]- How many cases must be checked to prove AND correct?
> Four: TT, TF, FT, FF.

### I M Versus M I

<!-- qard-id: ap-2df4a76e214b42ac2140 -->
> [!qard]- What do $I\,M$ and $M\,I$ reduce to?
> $I\,M\to M=\lambda z.\,z\,z$; $M\,I\to I\,I\to I=\lambda x.\,x$. Different, so $I\,M\ne M\,I$.

<!-- qard-id: ap-d09ff81d20a53ca76f93 -->
> [!qard]- Why do strict and lazy evaluation agree on $I\,M$?
> With a single application and no nested redexes there is only one possible reduction order.
