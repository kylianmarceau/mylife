---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 02 — Algorithm Efficiency Analysis"
---

# TOA 02 — Algorithm Efficiency Analysis

**Source note:** [Algorithm Efficiency Analysis](../../TOA/02_Efficiency_Analysis.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Input Size, Basic Operations And Cases|Input Size, Basic Operations And Cases]]
  - [[#Growth Orders And Asymptotic Bounds|Growth Orders And Asymptotic Bounds]]
  - [[#Combining Costs And Comparing Classes|Combining Costs And Comparing Classes]]
  - [[#Counting Iterative Algorithms|Counting Iterative Algorithms]]
  - [[#Checking Uniqueness: Three Designs|Checking Uniqueness: Three Designs]]
  - [[#Recurrences And Backward Substitution|Recurrences And Backward Substitution]]
  - [[#Fibonacci Recursion Analysis|Fibonacci Recursion Analysis]]
  - [[#Master Theorem|Master Theorem]]
  - [[#Precise Bounds And Counting|Precise Bounds And Counting]]

## Core Content

### Input Size, Basic Operations And Cases

<!-- qard-id: ap-af18b23ea58b102eb107 -->
> [!qard]- What is input size in algorithm analysis?
> A problem-dependent measure of the amount of input, denoted $n$.

<!-- qard-id: ap-725775f1fa7719ca33b7 -->
> [!qard]- What is an algorithm's basic operation?
> A repeated core operation selected to measure computation cost.

<!-- qard-id: ap-c78f4dfc6ca24e05a257 -->
> [!qard]- What is the best-case cost at a fixed input size?
> The minimum cost over inputs of that size.

<!-- qard-id: ap-e77cc1c43c8a7ddb6a7e -->
> [!qard]- What is the worst-case cost at a fixed input size?
> The maximum cost over inputs of that size.

<!-- qard-id: ap-b79461b7b6954f989285 -->
> [!qard]- What is average-case cost?
> Expected cost over a specified distribution of inputs of the same size.

<!-- qard-id: ap-539e5fe8ec64b2047f34 -->
> [!qard]- What is auxiliary space?
> Storage beyond the original input, including recursion stacks where relevant.

<!-- qard-id: ap-c0f8a72bb5e57e22e77e -->
> [!qard]- Do best-case and worst-case analysis correspond by definition to $\Omega$ and $O$?
> No. The chosen case and the type of asymptotic bound are separate decisions.

<!-- qard-id: ap-87dd0e7f9a5f154bf9bd -->
> [!qard]- What are linear search's best, worst and uniform-success average comparison counts?
> $1$, $n$, and $(n+1)/2$ respectively. The average assumes each matching position is equally likely; unsuccessful searches change the model.

### Growth Orders And Asymptotic Bounds

<!-- qard-id: ap-9cd46fac1f883cdcf5f0 -->
> [!qard]- What does $t(n)\in O(g(n))$ mean formally?
> Big O is an eventual upper bound. There exist $c>0$ and $n_0$ such that $0\le t(n)\le cg(n)$ for every $n\ge n_0$.

<!-- qard-id: ap-bea337df2fe87c6e5425 -->
> [!qard]- What does $t(n)\in\Omega(g(n))$ mean formally?
> Big Omega is an eventual lower bound. There exist $c>0$ and $n_0$ such that $0\le cg(n)\le t(n)$ for every $n\ge n_0$.

<!-- qard-id: ap-b47fb1426924d1edbb80 -->
> [!qard]- What does $t(n)\in\Theta(g(n))$ mean formally?
> Big Theta is a tight two-sided bound. There exist $c_L,c_U>0$ and $n_0$ such that $0\le c_Lg(n)\le t(n)\le c_Ug(n)$ for every $n\ge n_0$.

<!-- qard-id: ap-f7a23ede891f4c093710 -->
> [!qard]- What is the increasing order of the common growth classes in these notes?
> $1\prec\log n\prec n\prec n\log n\prec n^2\prec n^3\prec2^n\prec n!$ for sufficiently large $n$.

<!-- qard-id: ap-e7ff09e89910884a5355 -->
> [!qard]- Can a valid big-O bound be loose, and does Theta give an exact count?
> Yes: $100n+5$ is $O(n^2)$ but tightly $\Theta(n)$. Theta bounds constant-factor growth, not an exact count or a ratio tending to one; constants still matter for practical input sizes.

### Combining Costs And Comparing Classes

<!-- qard-id: ap-df22a9374cca0f99b6f6 -->
> [!qard]- How do you combine asymptotic costs of consecutive stages?
> If $t_1\in O(g)$ and $t_2\in O(h)$, then $t_1+t_2\in O(\max\{g,h\})$; analogous rules hold for $\Theta$ and $\Omega$ on nonnegative costs.

<!-- qard-id: ap-23fd1cec95ba0c271403 -->
> [!qard]- Why do consecutive stages and nested loops need different cost calculations?
> Consecutive costs add; nested repetitions require summing the inner work over outer iterations. Multiplying loop limits is valid only when that inner count is uniform.

<!-- qard-id: ap-29f8ccb04e2ede17d18b -->
> [!qard]- Which logarithm transformations preserve asymptotic growth?
> Changing a fixed base multiplies by a constant, so it preserves Theta. Squaring a logarithm does not: $(\log n)^2/\log n$ grows without bound.

<!-- qard-id: ap-ba974583cf00ba6e8dbc -->
> [!qard]- Does $O(n\log n)$ imply $O(n)$ or $O(n^2)$?
> It implies the larger upper bound $O(n^2)$, but not $O(n)$. A tight $\Theta(n\log n)$ function is not $\Theta(n^2)$.

### Counting Iterative Algorithms

<!-- qard-id: ap-05ee3cf5258a132fe68e -->
> [!qard]- What is the general process for analysing an iterative algorithm?
> Identify the basic operation, specify the case, count executions from loop limits, simplify the sum, then state the asymptotic class.

<!-- qard-id: ap-e4fb9aa3e1fceb20cd2a -->
> [!qard]- What does $\sum_{i=1}^ni$ equal?
> $n(n+1)/2$.

<!-- qard-id: ap-e9d7afcea264e07e5ec1 -->
> [!qard]- Which basic summation rules support loop analysis?
> $\sum_{i=j}^n1=n-j+1$; constants factor out; sums/differences can be separated. Use the actual bounds, including endpoints, before simplifying.

<!-- qard-id: ap-e8253d390d9597a23591 -->
> [!qard]- Why count comparisons rather than only assignments when scanning for a maximum?
> On a nonempty $n$-element input, every later element is compared once: $n-1$ comparisons in every case, even if the maximum never changes.

### Checking Uniqueness: Three Designs

<!-- qard-id: ap-e69ab522dffc073972b6 -->
> [!qard]- What is the worst-case comparison count for unique-pair checking?
> $n(n-1)/2$, still $\Theta(n^2)$.

<!-- qard-id: ap-29a98d48a61c4d184f7d -->
> [!qard]- How do ordered-pair, unique-pair and recursive uniqueness checks compare?
> Ordered pairs compare $n(n-1)$ distinct-index ordered pairs; unique pairs compare $n(n-1)/2$. Recursion obeys $C(n)=C(n-1)+(n-1)$ and may add linear stack space; all are quadratic worst case.

<!-- qard-id: ap-f9702524f5d140175444 -->
> [!qard]- How does presorting test uniqueness, and what qualifications matter?
> Sort, then compare adjacent entries: $\Theta(n\log n)$ total with efficient comparison sorting. It may reorder input; early duplicate exits affect best case; string comparisons need not cost constant time.

### Recurrences And Backward Substitution

<!-- qard-id: ap-7408f5cb5010fce492d2 -->
> [!qard]- What is a recurrence relation in efficiency analysis?
> An equation expressing cost at one size through costs at smaller sizes, together with base cases.

<!-- qard-id: ap-560879bb3d6a3134535e -->
> [!qard]- What is backward substitution?
> Repeatedly expand a recurrence until reaching its base case, then simplify the accumulated work.

<!-- qard-id: ap-e7d01742586e2bdd2d51 -->
> [!qard]- What costs must a recursive algorithm's recurrence include?
> The costs of all recursive calls and the work performed outside them.

<!-- qard-id: ap-c09863128f70cc5d68b1 -->
> [!qard]- How do you determine the expansion depth in backward substitution?
> Solve for the number of expansions that reduces the recursive argument to the base-case input size.

<!-- qard-id: ap-5a19b47cb294c325f02c -->
> [!qard]- What costs result from $T(n)=T(n-1)+1$, $T(n)=T(n/2)+1$ and $T(n)=2T(n/2)+1$?
> With constant base costs, respectively $\Theta(n)$, $\Theta(\log n)$ and $\Theta(n)$. Expansion depths are $n$, $\log_2n$ and $\log_2n$, but branching changes the accumulated work.

<!-- qard-id: ap-5ac30fd8025f9ce7957a -->
> [!qard]- How do recursive bit counting's returned value and operation count differ?
> For positive integer $n$, the bit length is $\lfloor\log_2n\rfloor+1$, while the recurrence uses $\lfloor\log_2n\rfloor$ additions. Analyse work separately from the returned number.

<!-- qard-id: ap-5bd0dd5a035cdb013cca -->
> [!qard]- How can base cases affect exact recurrence solutions without changing the growth class?
> For $M(n)=2M(n/2)+1$, zero base cost gives $n-1$ on powers of two; unit base cost gives $2n-1$. Both are linear.

### Fibonacci Recursion Analysis

<!-- qard-id: ap-8a602907a28c80235a2f -->
> [!qard]- Why does the course's Master Theorem not apply to recursive Fibonacci?
> Its subproblems have different sizes $n-1,n-2$ and shrink by subtraction, not by the same fixed fraction.

<!-- qard-id: ap-edf4e0960092577a8874 -->
> [!qard]- What addition-count recurrence describes direct recursive Fibonacci?
> $A(0)=A(1)=0$ and $A(n)=A(n-1)+A(n-2)+1$, solved by $A(n)=F_{n+1}-1\in\Theta(\varphi^n)$.

### Master Theorem

<!-- qard-id: ap-8051d043f2936f6ed79c -->
> [!qard]- What form of recurrence does the course's Master Theorem handle?
> $T(n)=aT(n/b)+f(n)$ with $f(n)\in\Theta(n^d)$, $a\ge1$, $b>1$, $d\ge0$, and constant-size base cost.

<!-- qard-id: ap-280d7c56cab56fbd30f9 -->
> [!qard]- What result does the Master Theorem give when $a<b^d$?
> $T(n)\in\Theta(n^d)$.

<!-- qard-id: ap-2a2b18acd139d75010eb -->
> [!qard]- What result does the Master Theorem give when $a=b^d$?
> $T(n)\in\Theta(n^d\log n)$.

<!-- qard-id: ap-5b1b441dcd5a98782bec -->
> [!qard]- What result does the Master Theorem give when $a>b^d$?
> $T(n)\in\Theta(n^{\log_ba})$.

### Precise Bounds And Counting

<!-- qard-id: ap-38a3c0223b216ca9bab1 -->
> [!qard]- What do the constants and threshold in an asymptotic bound permit you to ignore?
> A finite initial range and constant factors; the inequality must hold for every sufficiently large input, not merely selected sample points.

<!-- qard-id: ap-dd28ecdd0e3c4650eb5a -->
> [!qard]- Why is an average-case bound incomplete without a distribution?
> “Average” is an expectation weighted by input probabilities; different successful/unsuccessful cases or key distributions can change that expectation.

<!-- qard-id: ap-344727a13614fc61901f -->
> [!qard]- Why must a nonconstant basic operation be costed separately?
> Counting comparisons or arithmetic as one step is a model assumption; long strings or growing integers may make each operation more expensive.

<!-- qard-id: ap-9ee745b3477e9d94b456 -->
> [!qard]- How does an early return affect worst-case loop analysis?
> Identify an input where no earlier return occurs and count the resulting full path. The presence of an early exit does not lower that maximum automatically.

<!-- qard-id: ap-d026bf448c7d0f6d8aa4 -->
> [!qard]- Why does halving pair comparisons not turn quadratic work into linear work?
> $n(n-1)$ and $n(n-1)/2$ differ by a constant factor and share the same quadratic leading growth.

<!-- qard-id: ap-00aa8ba358f6f72c6cd7 -->
> [!qard]- How do you construct a recurrence for several recursive calls of different sizes?
> Add the cost of every call with its actual argument size plus all work outside the calls, then include correct base cases; do not force equal fractions that the algorithm does not have.

<!-- qard-id: ap-187a3d2083723f2ccc24 -->
> [!qard]- Why do floor/ceiling and base-size details matter even when an asymptotic class is unchanged?
> They determine exact counts and correct termination on small or odd sizes; simplified powers-of-two algebra must still correspond to a valid implementation.

<!-- qard-id: ap-31915c45c9ff95f10aba -->
> [!qard]- What do $a$, $b$ and $d$ mean when applying the course's Master Theorem?
> Number of recursive calls, factor reducing each call's input size, and exponent of the nonrecursive polynomial work. Compare $a$ with $b^d$ only after identifying the actual recurrence.
