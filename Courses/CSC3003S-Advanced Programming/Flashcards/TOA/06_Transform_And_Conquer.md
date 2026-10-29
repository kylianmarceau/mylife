---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 06 — Transform And Conquer"
---

# TOA 06 — Transform And Conquer

**Source note:** [Transform And Conquer](../../TOA/06_Transform_And_Conquer.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Transformation Types|Transformation Types]]
  - [[#Gaussian Elimination|Gaussian Elimination]]
  - [[#Presorting And Selection|Presorting And Selection]]
  - [[#Balanced Trees And Heaps|Balanced Trees And Heaps]]
  - [[#Horner's Rule For Polynomial Evaluation|Horner's Rule For Polynomial Evaluation]]
  - [[#Binary Exponentiation Through Representation Change|Binary Exponentiation Through Representation Change]]
  - [[#LCM And Optimisation Reductions|LCM And Optimisation Reductions]]
  - [[#Reducing River Crossing To A Graph|Reducing River Crossing To A Graph]]
  - [[#Transformation Correctness And Cost|Transformation Correctness And Cost]]

## Core Content

### Transformation Types

<!-- qard-id: ap-9f27cf840322f29574c8 -->
> [!qard]- What are the three transform-and-conquer types, with examples?
> Instance simplification (presorting); representation change (Horner's nested polynomial); problem reduction (LCM via GCD or a puzzle via graph search).

<!-- qard-id: ap-234bcaf1dec0c29c5972 -->
> [!qard]- Which transformation cost must be included in efficiency analysis?
> The preprocessing or conversion overhead, as well as solving and recovering the answer.

### Gaussian Elimination

<!-- qard-id: ap-93e700514ce6c8c80fe5 -->
> [!qard]- What are the forward-elimination steps?
> Choose a nonzero pivot, swapping rows if needed; subtract multiples of the pivot row from lower rows; apply the same changes to the right-hand side.

<!-- qard-id: ap-5950b091c4099660d3cd -->
> [!qard]- How does back substitution solve an upper-triangular system?
> Work from the last row upward: $x_i=(y_i-\sum_{j=i+1}^n u_{ij}x_j)/u_{ii}$. Each pivot $u_{ii}$ must be nonzero for a unique solution.

<!-- qard-id: ap-2b9849005924f11fcb15 -->
> [!qard]- What additional benefit does partial pivoting provide?
> It helps reduce numerical instability.

<!-- qard-id: ap-d38559ed64ed2ea30ffc -->
> [!qard]- What are Gaussian elimination's forward, backward, and total costs?
> Forward elimination $\Theta(n^3)$, back substitution $\Theta(n^2)$, total $\Theta(n^3)$.

<!-- qard-id: ap-c5fd453a2bc5b63d2686 -->
> [!qard]- Why do Gaussian-elimination row operations also modify the right-hand side?
> They must preserve an equivalent system $A\mathbf x=\mathbf b$. Changing only coefficients changes the equations. The result is upper triangular; singular or missing-pivot cases require separate handling.

### Presorting And Selection

<!-- qard-id: ap-a363dececa1a602d0dc1 -->
> [!qard]- Why is sorting before one binary search often worse than linear search?
> The sort dominates, producing $\Theta(n\log n)$ total work instead of a $\Theta(n)$ scan.

<!-- qard-id: ap-658351358412004a4b1c -->
> [!qard]- When can sorting before binary searches be worthwhile?
> For repeated queries, the initial sorting cost is reused and each later search is logarithmic.

<!-- qard-id: ap-c4a1ff764c4cbb405cf2 -->
> [!qard]- When do sorting, quickselect and a simple scan suit selection tasks?
> Sort for reusable ordering or many rank/search queries; quickselect for one general rank in expected linear time; scan for one minimum/maximum. Include sorting's $\Theta(n\log n)$ preprocessing cost.

### Balanced Trees And Heaps

<!-- qard-id: ap-548d6090bf2bb5a41ee8 -->
> [!qard]- What operations do balanced search trees support in logarithmic time?
> Search, insertion, and deletion, under their balancing guarantees.

<!-- qard-id: ap-7bdae7778712a7178c46 -->
> [!qard]- What is a heap?
> A tree-shaped priority structure whose parent-child key relationships expose an extreme key at the root.

<!-- qard-id: ap-3bb0e4db7472472a3838 -->
> [!qard]- What costs and ordering does a binary heap provide?
> Parent-child heap order exposes an extreme at the root: lookup $\Theta(1)$, insertion/extraction $O(\log n)$. It does not provide general search-tree ordering.

<!-- qard-id: ap-8d882dadcbeb36195319 -->
> [!qard]- What is the cost of building a heap from all entries?
> Linear time is possible.

<!-- qard-id: ap-dc7b9c6d9b0c4ac3a0bf -->
> [!qard]- Does a heap provide general binary-search-tree ordering?
> No. Its ordering is designed for extreme-key access, not arbitrary ordered key search.

<!-- qard-id: ap-4cf3c08069610edcc946 -->
> [!qard]- How does bottom-up heap building lead to heapsort's cost?
> Build in $\Theta(n)$ time, then perform $n$ logarithmic extractions for $\Theta(n\log n)$ total. A balanced search tree instead supports arbitrary search/insertion/deletion while maintaining logarithmic height.

### Horner's Rule For Polynomial Evaluation

<!-- qard-id: ap-28d8eb99db9610d97cfd -->
> [!qard]- How does Horner's algorithm update its accumulator?
> Initialise $p=a_n$, then for $i=n-1$ down to $0$, set $p\leftarrow xp+a_i$.

<!-- qard-id: ap-77e28c88083d62a5dbb4 -->
> [!qard]- How many multiplications and additions does Horner use for degree $n$?
> Exactly $n$ multiplications and $n$ additions/subtractions, giving $\Theta(n)$ arithmetic work.

<!-- qard-id: ap-d515189e797a6c21ae73 -->
> [!qard]- When can Horner's dense-polynomial loop be a poor choice?
> For a sparse expression such as $x^n$, scanning every zero coefficient wastes work; binary exponentiation uses logarithmically many multiplications. Reusing consecutive powers is another linear dense method.

### Binary Exponentiation Through Representation Change

<!-- qard-id: ap-96f6086f6160b3f62b79 -->
> [!qard]- How does left-to-right binary exponentiation process a positive exponent?
> Initialise the accumulator to $a$ for the leading $1$ bit. For each remaining bit, square it and, if the bit is $1$, multiply by $a$.

<!-- qard-id: ap-2e6bc7c4bfec1fa1f7d1 -->
> [!qard]- What is binary exponentiation's arithmetic-operation class?
> $\Theta(\log n)$ for growing positive exponents.

<!-- qard-id: ap-b084099b140841416679 -->
> [!qard]- Why does reading exponent bits correspond to squaring and optional multiplication?
> A partial exponent updates by $q\leftarrow2q+b$, so $a^{2q+b}=(a^q)^2a^b$. For $13=(1101)_2$, exponents become $1,3,6,13$ using three squarings and two extra multiplies.

<!-- qard-id: ap-418e3c71c9cf21dd6056 -->
> [!qard]- What bounds the left-to-right binary multiplication count for positive $n$?
> There are $\lfloor\log_2n\rfloor$ bits after the leading one, each needing one squaring and at most one extra multiply: between that many and twice that many multiplications. Handle $n=0$ separately with result one.

### LCM And Optimisation Reductions

<!-- qard-id: ap-2aa017365c6d5e828a71 -->
> [!qard]- How is LCM reduced to GCD?
> $\operatorname{lcm}(m,n)=mn/\gcd(m,n)$.

<!-- qard-id: ap-5956202f5ab34480679f -->
> [!qard]- How is minimisation converted into maximisation by a sign change?
> $\min_xf(x)=-\max_x(-f(x))$ over the same feasible domain.

<!-- qard-id: ap-89031bdd50b0f8a182a2 -->
> [!qard]- Why divide before multiplying in fixed-width LCM computation?
> $(m/\gcd(m,n))n$ avoids some intermediate overflow compared with forming $mn$ first. For $24,60$, the GCD is $12$ and LCM $120$; the final result must still fit.

### Reducing River Crossing To A Graph

<!-- qard-id: ap-d2d904cf47d62791f04c -->
> [!qard]- How do you reduce a constrained crossing puzzle to graph search?
> Encode participant locations as states, retain safe states, and connect legal crossings. Search from start to goal; BFS finds the fewest crossings when every move has equal cost.

<!-- qard-id: ap-de66c5b87ea7d260c21d -->
> [!qard]- What must a state-space reduction preserve?
> Legal moves and the correspondence between graph paths and solutions of the original problem.

<!-- qard-id: ap-82384985df127c179804 -->
> [!qard]- What state constraints and crossing sequence solve the wolf–goat–cabbage example?
> The peasant carries at most one item; wolf/goat and goat/cabbage cannot be unattended together. Take goat, return alone, take wolf, return with goat, take cabbage, return alone, take goat: seven crossings. Swapping wolf/cabbage gives another shortest route.

### Transformation Correctness And Cost

<!-- qard-id: ap-e8e91866930dbe1a394a -->
> [!qard]- What three costs belong in the total analysis of a reduction?
> Convert the original instance, solve the transformed problem, and recover the original answer; a fast middle stage alone does not establish a fast overall algorithm.

<!-- qard-id: ap-badeafd879fbee1974f6 -->
> [!qard]- Why do equivalent row operations preserve a linear system's solutions?
> Apply an invertible equation operation, such as a row swap or adding a multiple of another equation, to both sides; this changes the form without changing which variable assignments satisfy it.

<!-- qard-id: ap-0f1eed236e231e93d326 -->
> [!qard]- Why does a zero pivot require checking row swaps or singularity rather than simply dividing?
> Division by zero is invalid; a usable lower row may supply a pivot, while lack of the necessary pivots can mean no unique solution in the assumed procedure.

<!-- qard-id: ap-a230fe54d7f28741fe7d -->
> [!qard]- How does back substitution exploit upper-triangular structure?
> The last equation contains only the final variable; each earlier equation then has one new unknown after later values are substituted.

<!-- qard-id: ap-eaa7f42f624cfee65b4b -->
> [!qard]- How do repeated-query costs explain when presorting can repay itself?
> Sorting plus $q$ binary searches costs about $n\log n+q\log n$, versus $qn$ for repeated scans; enough reused queries can offset the initial sort.

<!-- qard-id: ap-863d407115c0b4033be4 -->
> [!qard]- How does Horner handle a constant polynomial or a missing coefficient?
> A degree-zero polynomial returns its constant without loop multiplications; an absent power has coefficient zero, which still participates if using a dense representation.

<!-- qard-id: ap-ac424394fc80acfc2319 -->
> [!qard]- What must a minimisation-to-maximisation sign reduction preserve?
> The feasible domain and the correspondence of optimal choices; negate the objective and negate the resulting optimal value back, without changing constraints.
