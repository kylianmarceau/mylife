---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 04A — Lambda Calculus Exercises"
---

# FP 04A — Lambda Calculus Exercises

**Source note:** [Lambda Calculus Exercises](../../FP/04A_Lambda_Calculus_Exercises.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Applying Reduction Rules|Applying Reduction Rules]]

## Core Content

### Applying Reduction Rules

<!-- qard-id: ap-b19639feeca115dfbb6b -->
> [!qard]- How does Church AND implement conjunction?
> $\mathrm{AND}=\lambda a.\lambda b.a\ b\ \mathrm{FALSE}$. If $a$ is TRUE it returns $b$; otherwise it returns FALSE.

<!-- qard-id: ap-52d3299055c3d5a61f4c -->
> [!qard]- Why is lambda application not commutative?
> $I\,M\to M$, but $M\,I\to I\,I\to I$. Swapping function and argument changes the result.

<!-- qard-id: ap-2e55ec9e231493c24037 -->
> [!qard]- How should you approach a lambda-reduction exercise?
> Make application grouping explicit, identify the selected redex, alpha-rename if needed, substitute without capture, and repeat until normal form or evident divergence.
