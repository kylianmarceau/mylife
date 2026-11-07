---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 06 — Transform And Conquer"
---

# TOA 06 — Transform And Conquer

**Source note:** [Transform And Conquer](../../TOA/06_Transform_And_Conquer.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Strategy|Strategy]]
  - [[#Instance Simplification|Instance Simplification]]
  - [[#Horner's Rule|Horner's Rule]]
  - [[#Binary Exponentiation|Binary Exponentiation]]
  - [[#Problem Reduction|Problem Reduction]]

## Core Content

### Strategy

<!-- qard-id: ap-bd5526cbc4ec500c6de6 -->
> [!qard]- What is transform and conquer?
> Transform the problem into something easier, then solve the transformed problem.

<!-- qard-id: ap-f3a584aa1e5745513388 -->
> [!qard]- Name the three kinds of transformation with an example of each.
> Instance simplification (presorting, Gaussian elimination), representation change (heaps, Horner's rule, binary exponentiation), problem reduction (LCM via GCD, graph reductions).

<!-- qard-id: ap-b231f3010b1f11a3ef3e -->
> [!qard]- What are transform and conquer's strength and weakness?
> Strength: lets powerful data structures be used; useful in complexity theory. Weakness: can be hard to derive, especially reductions.

### Instance Simplification

<!-- qard-id: ap-ba7170989d806d866f00 -->
> [!qard]- How does Gaussian elimination use transform and conquer?
> Forward elimination transforms the system to upper-triangular form ($\Theta(n^3)$), then backward substitution solves it ($\Theta(n^2)$).

<!-- qard-id: ap-2b622f9204dcb842923f -->
> [!qard]- When is presorting worth it?
> When the unsorted algorithm is slower than $\Theta(n\log n)$ — e.g. uniqueness, median, closest pair.

<!-- qard-id: ap-9577f8ff148913b3221c -->
> [!qard]- Should you presort to find the min and max or to search an unsorted array once?
> No — both are already $\Theta(n)$ by brute force.

<!-- qard-id: ap-041c50fd01ce79b92826 -->
> [!qard]- Compare presorted selection with partition-based selection.
> Presorting: $\Theta(n\log n)$, but gives the $k$ smallest too. Partition-based (quickselect): average $\Theta(n)$, worst $\Theta(n^2)$.

### Horner's Rule

<!-- qard-id: ap-02d768f907f5e682f1f3 -->
> [!qard]- What is Horner's rule?
> Factor $x$ out repeatedly: $p(x)=(\dots(a_nx+a_{n-1})x+\dots)x+a_0$, evaluated innermost first.

<!-- qard-id: ap-a0a678023729b4d8721a -->
> [!qard]- Give Horner's rule as pseudocode.
> `p = c[n]; for i = n-1 downto 0: p = x*p + c[i]`

<!-- qard-id: ap-9e7983e1dc21013727b6 -->
> [!qard]- How many multiplications does Horner's rule need, compared with brute force?
> $n$ multiplications and $n$ additions — as many as brute force spends on the first term alone; brute force needs $\Theta(n^2)$.

<!-- qard-id: ap-1df0303c131f9a63dfcc -->
> [!qard]- For which polynomial does Horner's rule not help?
> One with a single non-zero term, such as $x^n$.

### Binary Exponentiation

<!-- qard-id: ap-322ed5b782384be8b5f6 -->
> [!qard]- How does binary exponentiation compute $a^n$?
> Scan $n$'s bits from the most significant: start with $a$, then for each further bit square the result and multiply by $a$ if the bit is 1.

<!-- qard-id: ap-0cc87f1b99d6cb322e03 -->
> [!qard]- Why does squaring work in binary exponentiation?
> Each step changes the exponent $p\to2p+b$, and $a^{2p+b}=(a^p)^2\cdot a^b$.

<!-- qard-id: ap-d89e87f6aa5bafe92541 -->
> [!qard]- How many multiplications does binary exponentiation need?
> Between $k-1$ and $2(k-1)$ where $k-1=\lfloor\log_2 n\rfloor$, so $\Theta(\log n)$ versus $n-1$ for brute force.

### Problem Reduction

<!-- qard-id: ap-fcfa2cb39c08a580ea55 -->
> [!qard]- How is LCM reduced to GCD?
> $\operatorname{lcm}(m,n)=\dfrac{mn}{\gcd(m,n)}$.

<!-- qard-id: ap-6e5d30db3da64f16622d -->
> [!qard]- How is minimisation reduced to maximisation?
> $\min f(x)=-\max[-f(x)]$.

<!-- qard-id: ap-2fd5f3ac9d4caeea7acb -->
> [!qard]- What is a state-space graph?
> A graph whose vertices are problem states and edges are legal transitions; solving means finding a (shortest) path from start to goal.

<!-- qard-id: ap-e7b5f4de79b1d953db69 -->
> [!qard]- What is the minimum number of crossings for the peasant–wolf–goat–cabbage puzzle?
> 7 — take the goat first, swap the goat back midway, and finish by taking the goat again.
