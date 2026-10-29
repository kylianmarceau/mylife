---
tags:
  - advanced-programming
---

# Algorithm Efficiency Analysis

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [2 - TOA Efficiency.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/2%20-%20TOA%20Efficiency.pdf), Patrick Marais, University of Cape Town, PDF pages 1–44  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

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

---

## Core Content

### Input Size, Basic Operations And Cases

#### Definitions

> **Input size**: A measure of the amount of input, denoted $n$; its meaning depends on the problem.

> **Basic operation**: A repeated core operation used to measure an algorithm's computation cost.

> **Best case**, **worst case** and **average case**: Respectively the minimum cost, maximum cost, and expected cost over a specified distribution of inputs of the same size.

> **Auxiliary space**: Storage used in addition to the original input, including recursion stacks where applicable.

Count comparisons for searching and sorting, and additions or multiplications for numerical algorithms. State what the input size and counted operation mean before deriving a bound.

For linear search in an array of size $n$:

| Case | Key comparisons | Growth |
|---|---:|---|
| First element matches | $1$ | $\Theta(1)$ |
| Last matches, or key is absent | $n$ | $\Theta(n)$ |
| Successful match uniformly distributed among positions | $(n+1)/2$ | $\Theta(n)$ |

The average depends on the input distribution and probability of unsuccessful search. A best-case statement is not a lower-bound notation by definition; case analysis and bound notation are separate choices.

### Growth Orders And Asymptotic Bounds

#### Definitions

> **Big O**: An asymptotic upper bound on a nonnegative cost function.

> **Big Omega**: An asymptotic lower bound on a nonnegative cost function.

> **Big Theta**: Matching asymptotic upper and lower bounds, up to positive constant factors.

$$
\begin{aligned}
t(n)\in O(g(n))&\iff \exists c>0,n_0:\ 0\le t(n)\le cg(n)\quad(n\ge n_0),\\
t(n)\in\Omega(g(n))&\iff \exists c>0,n_0:\ 0\le cg(n)\le t(n)\quad(n\ge n_0),\\
t(n)\in\Theta(g(n))&\iff \exists c_L,c_U>0,n_0:\ 0\le c_Lg(n)\le t(n)\le c_Ug(n)\quad(n\ge n_0).
\end{aligned}
$$

Theta does not mean an exact operation count or a limiting ratio of one. It means that the cost is bounded between constant multiples of the same growth function.

![Theta upper and lower envelopes](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/02_Efficiency_Analysis/theta-bounds.svg)

*After the threshold, the cost stays between positive constant multiples of the reference function.*

For $t(n)=100n+5$, choose $c_U=101$, $n_0=5$ to prove an upper bound, and $c_L=100$ for the lower bound. Thus $t(n)\in\Theta(n)$; it is also in $O(n^2)$, but not $\Theta(n^2)$.

For sufficiently large input, typical classes grow in this order:

$$
1\prec\log n\prec n\prec n\log n\prec n^2\prec n^3\prec2^n\prec n!.
$$

| $n$ | $\log_2n$ | $n\log_2n$ | $n^2$ | $n^3$ | $2^n$ | $n!$ |
|---:|---:|---:|---:|---:|---:|---:|
| $10$ | $3.3$ | $33.2$ | $10^2$ | $10^3$ | $1024$ | $3.63\times10^6$ |
| $100$ | $6.6$ | $664.4$ | $10^4$ | $10^6$ | $1.27\times10^{30}$ | $9.33\times10^{157}$ |
| $1000$ | $10.0$ | $9965.8$ | $10^6$ | $10^9$ | $1.07\times10^{301}$ | Enormous |
| $10^4$ | $13.3$ | $132877.1$ | $10^8$ | $10^{12}$ | Enormous | Enormous |
| $10^5$ | $16.6$ | $1660964.0$ | $10^{10}$ | $10^{15}$ | Enormous | Enormous |
| $10^6$ | $19.9$ | $19931568.6$ | $10^{12}$ | $10^{18}$ | Enormous | Enormous |

Constant factors can matter on small inputs. For large inputs, growth often dominates: at $n=10^8$, quadratic work is about $3.76\times10^6$ times the size of $n\log_2n$. If the latter takes thirty seconds at the same operation rate, the former takes roughly $3.6$ years.

### Combining Costs And Comparing Classes

If consecutive stages cost $t_1(n)\in O(g(n))$ and $t_2(n)\in O(h(n))$, then:

$$
t_1(n)+t_2(n)\in O(\max\{g(n),h(n)\}).
$$

The corresponding statement also holds for Theta and Omega bounds on nonnegative costs. Thus a quadratic sort followed by linear search remains quadratic. Nested repetition requires multiplication or summation, not this sequential-stage rule.

Since $n\le n+\log n\le2n$ eventually, $\Theta(n+\log n)=\Theta(n)$. Also:

$$
\log_a n=\frac{\log_b n}{\log_b a}\qquad(a,b>1).
$$

Changing a fixed logarithm base only changes a constant. Squaring a logarithm changes its growth.

| Checkpoint | Result | Reason |
|---|---|---|
| $\Theta(n+\log n)=\Theta(n)$ | True | Linear term dominates |
| $O(n+\log n)=O(n)$ | True | Constant-factor equivalence |
| $\Theta(n\log_2n)=\Theta(n\log_{10}n)$ | True | Base change is constant |
| $\Theta((\log n)^2)=\Theta(\log n)$ | False | Ratio grows without bound |
| $O(n\log n)=O(n)$ | False | $O(n)$ is a proper subset |
| $t\in O(n\log n)\Rightarrow t\in O(n^2)$ | True | Larger upper bound |
| $t\in\Theta(n\log n)\Rightarrow t\in\Theta(n^2)$ | False | Different tight classes |
| $t\in O(n\log n)\Rightarrow t\in O(n)$ | False | Counterexample: $t=n\log n$ |

### Counting Iterative Algorithms

#### Definitions

> **Summation**: A compact representation of repeated additions used to count loop work.

1. Identify the basic operation.
2. State the case being analysed.
3. Count executions using the loop limits.
4. Simplify the sum and give an asymptotic class.

Useful identities are:

$$
\sum_{i=j}^{n}1=n-j+1,\qquad
\sum_{i=1}^{n}i=\frac{n(n+1)}2,
$$
$$
\sum_i ca_i=c\sum_i a_i,\qquad
\sum_i(a_i\pm b_i)=\sum_i a_i\pm\sum_i b_i.
$$

Finding an array maximum:

```pseudo
Maximum(A):
    maximum = A[0]       // requires nonempty input
    for i = 1 to length(A) - 1:
        if A[i] > maximum:
            maximum = A[i]
    return maximum
```

The comparison executes $C(n)=\sum_{i=1}^{n-1}1=n-1\in\Theta(n)$ in every case. Updating the maximum happens a variable number of times; counting only updates would miss the comparisons that always occur.

### Checking Uniqueness: Three Designs

#### Definitions

> **Set**: A collection with no duplicate elements; here the question is whether all array entries are distinct.

The direct method compares each entry with every other entry:

```pseudo
IsSetOrderedPairs(A):
    for i = 0 to length(A) - 1:
        for j = 0 to length(A) - 1:
            if i != j and A[i] == A[j]: return false
    return true
```

For distinct entries, the inner loop executes $n^2$ times and the element-equality comparison executes $n(n-1)$ times under short-circuit evaluation. The PDF's count $(n-1)^2$ is incorrect; the quadratic class is unchanged.

Avoid checking each unordered pair twice:

```pseudo
IsSetPairs(A):
    for i = 0 to length(A) - 2:
        for j = i + 1 to length(A) - 1:
            if A[i] == A[j]: return false
    return true
```

$$
\begin{aligned}
C(n)&=\sum_{i=0}^{n-2}\sum_{j=i+1}^{n-1}1
=\sum_{i=0}^{n-2}(n-1-i)\\
&=(n-1)^2-\frac{(n-2)(n-1)}2
=\frac{n(n-1)}2\in\Theta(n^2).
\end{aligned}
$$

The recursive version checks one entry against the suffix, then recurses on that suffix:

```pseudo
IsSetRecursive(A, index):
    if index >= length(A) - 1: return true
    for j = index + 1 to length(A) - 1:
        if A[index] == A[j]: return false
    return IsSetRecursive(A, index + 1)
```

Its worst-case recurrence is $C(n)=C(n-1)+(n-1)$ with $C(1)=0$, giving the same pair count. Explicit recursion can add linear stack storage.

A transformation sorts first, then checks neighbours:

```pseudo
IsSetPresorted(A):
    EfficientSort(A)
    for i = 0 to length(A) - 2:
        if A[i] == A[i + 1]: return false
    return true
```

| Method | Worst-case comparisons or time | Qualification |
|---|---|---|
| All ordered pairs | $\Theta(n^2)$ | Checks each distinct pair twice |
| Unique pairs, iterative or recursive | $\Theta(n^2)$ | Half as many element comparisons |
| Efficient sort then scan | $\Theta(n\log n)$ | Sorting cost included; may reorder input |

Early duplicates can produce a constant-time best case for pair checking. Average-case claims need an input model; quadratic average behaviour is not automatic. Comparing arbitrary strings can also cost more than a constant per comparison.

### Recurrences And Backward Substitution

#### Definitions

> **Recurrence relation**: An equation expressing a cost at one input size in terms of costs at smaller sizes, together with base cases.

> **Backward substitution**: Repeated expansion of a recurrence until its base case is reached.

Typical forms are $T(n)=aT(n-k)+f(n)$ and $T(n)=aT(n/b)+f(n)$. Include the recursive calls and the work outside them.

For recursive factorial, count multiplications:

```java
Factorial(n):
    if n == 0: return 1
    return Factorial(n - 1) * n
```

$$
M(0)=0,\quad M(n)=M(n-1)+1=M(n-k)+k.
$$

Set $k=n$: $M(n)=n\in\Theta(n)$.

For counting the bits of a positive integer:

```pseudo
CountBits(n):
    if n == 1: return 1
    return 1 + CountBits(floor(n / 2))
```

The return value is $\lfloor\log_2n\rfloor+1$, but the number of additions is $\lfloor\log_2n\rfloor$. If $n=2^k$:

$$
A(1)=0,\qquad A(2^k)=A(2^{k-1})+1=A(1)+k=\log_2n.
$$

For two recursive half-size calls with one operation outside them:

$$
M(n)=2M(n/2)+1,\quad M(1)=0.
$$

After $i$ expansions:

$$
M(n)=2^iM(n/2^i)+\sum_{j=0}^{i-1}2^j
=2^iM(n/2^i)+2^i-1.
$$

At $i=\log_2n$, $M(n)=n-1\in\Theta(n)$. Powers of two simplify exact algebra; floor and ceiling divisions give the same asymptotic result for ordinary positive sizes.

### Fibonacci Recursion Analysis

The basic operation is addition:

$$
A(0)=A(1)=0,\qquad A(n)=A(n-1)+A(n-2)+1.
$$

Using the Fibonacci recurrence, $A(n)=F_{n+1}-1$, hence $A(n)\in\Theta(\varphi^n)$ with $\varphi=(1+\sqrt5)/2$. This is exponential despite the very short code.

The two subproblem sizes differ and are obtained by subtraction. The course's Master Theorem does not apply to this recurrence.

### Master Theorem

#### Definitions

> **Master Theorem**: A rule giving asymptotic costs for equal-fraction recursive subproblems with a specified nonrecursive cost.

For the course version, let:

$$
T(n)=aT(n/b)+f(n),\qquad f(n)\in\Theta(n^d),\quad a\ge1,\ b>1,\ d\ge0,
$$

with constant-size base cost. Identify the number of recursive calls $a$, shrink factor $b$, and polynomial degree $d$.

| Condition | Cost |
|---|---|
| $a<b^d$ | $\Theta(n^d)$ |
| $a=b^d$ | $\Theta(n^d\log n)$ |
| $a>b^d$ | $\Theta(n^{\log_ba})$ |

| Recurrence | Parameters | Case | Result |
|---|---|---|---|
| $A(n)=A(n/2)+1$ | $a=1,b=2,d=0$ | Equal | $\Theta(\log n)$ |
| $A(n)=2A(n/2)+1$ | $a=2,b=2,d=0$ | Greater | $\Theta(n)$ |
| $T(n)=2T(n/2)+n$ | $a=2,b=2,d=1$ | Equal | $\Theta(n\log n)$ |
| $T(n)=T(n/2)+n$ | $a=1,b=2,d=1$ | Less | $\Theta(n)$ |

The base cost changes exact counts but usually not the class. For $A(1)=1$, the second recurrence yields $2n-1$, rather than $n-1$ for a zero base.

Know how to apply this theorem; its proof is outside the course scope. Do not force it onto decrement recurrences, Fibonacci, or unequal quicksort subproblem sizes.
