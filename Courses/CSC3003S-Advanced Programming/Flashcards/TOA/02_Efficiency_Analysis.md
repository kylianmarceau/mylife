---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 02 — Algorithm Efficiency Analysis"
---

# TOA 02 — Algorithm Efficiency Analysis

**Source note:** [Algorithm Efficiency Analysis](../../TOA/02_Efficiency_Analysis.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Measuring Efficiency|Measuring Efficiency]]
  - [[#Asymptotic Notation|Asymptotic Notation]]
  - [[#Non-Recursive Analysis|Non-Recursive Analysis]]
  - [[#Recursive Analysis|Recursive Analysis]]

## Core Content

### Measuring Efficiency

<!-- qard-id: ap-19b527112a41ac7fb55b -->
> [!qard]- What two things must you define to analyse an algorithm's time efficiency?
> A measure of input size $n$ and the basic operation (the operation repeated at the algorithm's core).

<!-- qard-id: ap-748021a83a08603b1092 -->
> [!qard]- Why do we care about order of growth rather than constants?
> For large $n$ the growth class dominates: $O(n^2)$ vs $O(n^3)$ matters far more than $1412n^2$ vs $4n^3$.

<!-- qard-id: ap-b5815f04773482fced4e -->
> [!qard]- Give the best, worst and average cases of linear search.
> Best $\Theta(1)$, worst $\Theta(n)$, average about $n/2$ comparisons $=\Theta(n)$.

<!-- qard-id: ap-e419ab4ad7f90c4d3297 -->
> [!qard]- Order these classes from slowest to fastest growing: $n!$, $n\log n$, $2^n$, $\log n$, $n^3$, $n$, $n^2$.
> $\log n < n < n\log n < n^2 < n^3 < 2^n < n!$

### Asymptotic Notation

<!-- qard-id: ap-2a7f06c7d92f4deb0010 -->
> [!qard]- Define $t(n)\in O(g(n))$.
> There exist $c>0$ and $n_0$ such that $t(n)\le c\,g(n)$ for all $n\ge n_0$ — an upper bound.

<!-- qard-id: ap-45c16dab239a50bd4fb0 -->
> [!qard]- Define $t(n)\in\Omega(g(n))$.
> There exist $c>0$ and $n_0$ such that $t(n)\ge c\,g(n)$ for all $n\ge n_0$ — a lower bound.

<!-- qard-id: ap-e224398ec088363f4258 -->
> [!qard]- Define $t(n)\in\Theta(g(n))$.
> There exist $c_1,c_2>0$ and $n_0$ such that $c_2g(n)\le t(n)\le c_1g(n)$ for all $n\ge n_0$ — a tight bound.

<!-- qard-id: ap-a07850987bd5aa976e3d -->
> [!qard]- Is $100n+5$ in $O(n^2)$? In $\Theta(n^2)$?
> In $O(n^2)$ yes (upper bounds needn't be tight); in $\Theta(n^2)$ no — it is $\Theta(n)$.

<!-- qard-id: ap-4b694c6200b1d790c5a0 -->
> [!qard]- State the sum rule for sequential parts of an algorithm.
> If $t_1\in O(g)$ and $t_2\in O(h)$ then $t_1+t_2\in O(\max\{g,h\})$; the same holds for $\Theta$ and $\Omega$.

<!-- qard-id: ap-8f8011aaafa7852db03d -->
> [!qard]- Is $\Theta(n\log_2 n)=\Theta(n\log_{10} n)$? Why?
> Yes — logs of different bases differ only by a constant factor.

<!-- qard-id: ap-1225ebe2d8f64df2de2a -->
> [!qard]- Is $\Theta(\log^2 n)=\Theta(\log n)$?
> No — $\log^2 n$ grows more than a constant factor faster.

### Non-Recursive Analysis

<!-- qard-id: ap-73c24c50f00301356fd8 -->
> [!qard]- What are the steps for analysing a non-recursive algorithm?
> 1. Identify the basic operation. 2. Set up a sum $C(n)$ counting it. 3. Solve the sum for the efficiency class.

<!-- qard-id: ap-57a67b087a54d820fd87 -->
> [!qard]- What is $\sum_{i=l}^{u} 1$ and $\sum_{i=1}^{n} i$?
> $u-l+1$, and $\dfrac{n(n+1)}{2}\in\Theta(n^2)$.

<!-- qard-id: ap-22c1865f7402d9322f8b -->
> [!qard]- How many comparisons does the "compare each element with all later ones" uniqueness check make in the worst case?
> $\dfrac{n(n-1)}{2}\in\Theta(n^2)$.

<!-- qard-id: ap-7522239834b48f35470a -->
> [!qard]- Why is presort-then-scan faster for checking uniqueness?
> Sorting is $\Theta(n\log n)$ and the adjacent scan $\Theta(n)$, so the total is $\Theta(n\log n)$, beating $\Theta(n^2)$.

### Recursive Analysis

<!-- qard-id: ap-fa41a705087499a497a5 -->
> [!qard]- How does recursive-algorithm analysis differ from non-recursive?
> The count is a recurrence relation, solved by backward substitution or the Master Theorem.

<!-- qard-id: ap-a55b19a4556d26376c33 -->
> [!qard]- Solve $M(n)=M(n-1)+1$, $M(0)=0$.
> Backward substitution gives $M(n)=M(n-k)+k$, so $M(n)=n\in\Theta(n)$.

<!-- qard-id: ap-5b1ddaf4234ea39e53ff -->
> [!qard]- Why assume $n=2^k$ when solving $A(n)=A(n/2)+1$?
> It keeps arguments integral; the smoothness theorem extends the result ($\Theta(\log n)$) to all $n$.

<!-- qard-id: ap-ec5ec0cdf84aa9c5de3d -->
> [!qard]- State the Master Theorem.
> For $T(n)=aT(n/b)+f(n)$, $f\in\Theta(n^d)$: $\Theta(n^d)$ if $a<b^d$; $\Theta(n^d\log n)$ if $a=b^d$; $\Theta(n^{\log_b a})$ if $a>b^d$.

<!-- qard-id: ap-b2f3715752654bcdf563 -->
> [!qard]- Apply the Master Theorem to $T(n)=2T(n/2)+1$.
> $a=2,b=2,d=0$; $a>b^d$, so $\Theta(n^{\log_2 2})=\Theta(n)$.

<!-- qard-id: ap-4ff8264701e678c1a917 -->
> [!qard]- What is the efficiency class of naive recursive Fibonacci?
> $A(n)=A(n-1)+A(n-2)+1$ gives $\Theta(1.618^n)$ — exponential.

<!-- qard-id: ap-f98bd3ff086154435737 -->
> [!qard]- Time efficiency versus space efficiency?
> Time: how many basic operations run. Space: how much extra memory is needed. Both are functions of $n$.
