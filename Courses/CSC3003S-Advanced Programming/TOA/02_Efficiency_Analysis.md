---
tags:
  - advanced-programming
---

# Algorithm Efficiency Analysis

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [2 - TOA Efficiency.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/2%20-%20TOA%20Efficiency.pdf), Patrick Marais, University of Cape Town, pages 1–44
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Asymptotic notation ($O$, $\Omega$, $\Theta$), counting basic operations with summations, and solving recurrences by backward substitution and the Master Theorem.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Measuring Algorithm Efficiency|Measuring Algorithm Efficiency]]
  - [[#Best, Worst And Average Case: Linear Search|Best, Worst And Average Case: Linear Search]]
  - [[#Typical Efficiency Classes|Typical Efficiency Classes]]
  - [[#Big O|Big O]]
  - [[#Big Omega|Big Omega]]
  - [[#Big Theta|Big Theta]]
  - [[#Sum Rule For Sequential Parts|Sum Rule For Sequential Parts]]
  - [[#Comparing O, Ω And Θ|Comparing O, Ω And Θ]]
  - [[#Checkpoint: Asymptotic Equalities|Checkpoint: Asymptotic Equalities]]
  - [[#Analysing Non-Recursive Algorithms|Analysing Non-Recursive Algorithms]]
  - [[#Summation Rules|Summation Rules]]
  - [[#Example: Maximum Element|Example: Maximum Element]]
  - [[#Example: Is The Array A Set?|Example: Is The Array A Set?]]
  - [[#Analysing Recursive Algorithms|Analysing Recursive Algorithms]]
  - [[#Backward Substitution Examples|Backward Substitution Examples]]
  - [[#Fibonacci Recurrence|Fibonacci Recurrence]]
  - [[#The Master Theorem|The Master Theorem]]

---

## Core Content

### Measuring Algorithm Efficiency

#### Definitions

> **Input size**: The measure of how big an instance is, typically written $n$.

> **Basic operation**: The operation executed repeatedly at the core of the algorithm; its count is the unit used to measure time.

> **Order of growth**: How the operation count grows as $n$ grows, ignoring constant factors and lower-order terms.

> **Time efficiency**: The number of basic operations performed, as a function of $n$.

> **Space efficiency**: The number of extra memory units required, as a function of $n$.

To analyse efficiency you need two things: a measure of input size $n$ and a unit of time (the basic operation).

- We care about **growth order**. The difference between $O(n^2)$ and $O(n^3)$ matters far more than the difference between $1412n^2$ and $4n^3$.
- We distinguish **best**, **average** and **worst** case performance.
- Both time and memory efficiency are expressed as functions of $n$.

### Best, Worst And Average Case: Linear Search

Linear search scans an array of length $n$ for a key.

| Case | Elements examined | Efficiency |
|---|---|---|
| Worst | All $n$ | $\Theta(n)$ |
| Best | 1 (key is first) | $\Theta(1)$ |
| Average | About $n/2$ | $\Theta(n/2) = \Theta(n)$, since $\tfrac12$ is a constant |

You could also say the worst case is $O(n)$, or even $O(n^2)$, but we want the **tightest bound**.

### Typical Efficiency Classes

Values of common growth functions:

| $n$ | $\log_2 n$ | $n$ | $n\log_2 n$ | $n^2$ | $n^3$ | $2^n$ | $n!$ |
|---|---|---|---|---|---|---|---|
| 10 | 3.3 | $10$ | 33.2 | $10^2$ | $10^3$ | $10^3$ | $3.6\times10^6$ |
| 100 | 6.6 | $10^2$ | 664.4 | $10^4$ | $10^6$ | $1.3\times10^{30}$ | $9.3\times10^{157}$ |
| 1,000 | 10.0 | $10^3$ | 9,965.8 | $10^6$ | $10^9$ | $1.1\times10^{301}$ | — |
| 10,000 | 13.3 | $10^4$ | 132,877.1 | $10^8$ | $10^{12}$ | — | — |
| 100,000 | 16.6 | $10^5$ | 1,660,964.0 | $10^{10}$ | $10^{15}$ | — | — |
| 1,000,000 | 19.9 | $10^6$ | 19,931,568.6 | $10^{12}$ | $10^{18}$ | — | — |

Exponential and factorial functions become astronomically large even for small $n$.

#### How long to sort 100 million items?

Suppose an $n\log_2 n$ sort of $n = 10^8$ items takes 30 seconds:

$$
n\log_2 n = 10^8 \log_2 10^8 \approx 2{,}657{,}542{,}476 \text{ operations in } 30\text{ s}
$$

A quadratic sort needs $n^2 = 10^{16}$ operations:

$$
\frac{10^{16}}{2{,}657{,}542{,}476} \approx 3{,}762{,}875, \qquad 3{,}762{,}875 \times 30\text{ s} = 112{,}886{,}248\text{ s} \approx 3.6 \text{ years}
$$

Insertion sort and bubble sort ($\Theta(n^2)$) are therefore impractical for large data sets.

### Big O

#### Definitions

> **Big O**: $t(n) \in O(g(n))$ if and only if there exist a constant $c$ and an $n_0$ such that $t(n) \le c\,g(n)$ for all $n \ge n_0$.

Intuitively, Big O drops constant factors and lower-order terms:

| Operation count | Class | Ignored parts |
|---|---|---|
| $2n + 10$ | $O(n)$ | the 2 and the 10 |
| $3n^2 + 9n + 5$ | $O(n^2)$ | the 3, the $9n$ and the 5 |

**Example 1**: $100n + 5 \in O(n)$. Choose $c = 101$ and $n_0 = 5$. Then $100n + 5 \le 101n$ for all $n \ge 5$.

**Example 2**: $100n + 5 \in O(n^2)$. Choose $c = 21$, $n_0 = 5$ and check $100n + 5 \le 21n^2$. More formally:

$$
100n + 5 \le 100n + n = 101n \le 101n^2 \quad (n \ge 5) \;\Rightarrow\; 100n+5 \in O(n^2)
$$

### Big Omega

#### Definitions

> **Big Omega**: $t(n) \in \Omega(g(n))$ if and only if there exist a positive constant $c$ and a non-negative integer $n_0$ such that $t(n) \ge c\,g(n)$ for all $n \ge n_0$.

This is the same as Big O with the inequality reversed. It gives a **lower bound** on growth and is not widely used.

### Big Theta

#### Definitions

> **Big Theta**: $t(n) \in \Theta(g(n))$ if and only if there exist constants $c_1$, $c_2$ and $n_0$ such that $c_2\,g(n) \le t(n) \le c_1\,g(n)$ for all $n \ge n_0$.

Big O only gives an upper bound. Summing an array is $O(n)$, but by the definition it is also $O(n^2)$, $O(2^n)$ and $O(n\log n)$. (It is not $O(\log n)$.) $O(n^2)$ means "proportional to $n^2$ **or better**".

To say an algorithm's basic operation executes *exactly* in proportion to $n$, use Big Theta. Summing an array is $\Theta(n)$; it is not $\Theta(n^2)$ or $\Theta(n\log n)$.

Functions in a $\Theta$ class cannot also be in a more efficient class:

- $100n + 5 \in \Theta(n)$
- $100n + 5 \in O(n^2)$
- $100n + 5 \notin \Theta(n^2)$

$\Theta$ is the notation used most in this course.

![Theta bounds graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/02_Efficiency_Analysis/theta-bounds.svg)

*Beyond $n_0$, $t(n)$ is sandwiched between $c_2 g(n)$ and $c_1 g(n)$.*

### Sum Rule For Sequential Parts

> **Theorem**: If $t_1(n) \in O(g(n))$ and $t_2(n) \in O(h(n))$, then $t_1(n) + t_2(n) \in O(\max\{g(n), h(n)\})$. The same holds for $\Theta$ and $\Omega$.

This lets you estimate the complexity of an algorithm made of sequential parts. The slowest-growing part dominates.

Example: bubble sort an array, then search it.

| Part | Complexity |
|---|---|
| Bubble sort | $O(n^2)$ |
| Search | $O(n)$ |
| Combined | $O(\max\{n^2, n\}) = O(n^2)$ |

### Comparing O, Ω And Θ

| Notation | Meaning as $n$ grows | Bound type |
|---|---|---|
| Big O | Running time at most proportional to $g(n)$ | Upper bound |
| Big Ω | Running time at least proportional to $g(n)$ | Lower bound |
| Big Θ | Running time exactly proportional to $g(n)$ | Exact (tight) bound |

Bounds can be stated for any case:

| Statement | Meaning | Example |
|---|---|---|
| Average case $O(n^2)$ | Grows at most as fast as $n^2$ on average input | Bubble sort |
| Worst case $O(n^3)$ | Grows at most as fast as $n^3$ in the worst case | Brute-force matrix multiplication (also $\Theta(n^3)$) |
| Best case $\Theta(n)$ | Grows linearly in the best case | Summing an array |
| Worst case $\Omega(2^n)$ | Grows at least exponentially in the worst case | Creating the power set |

### Checkpoint: Asymptotic Equalities

| Statement | Answer | Reason |
|---|---|---|
| $\Theta(n + \log n) = \Theta(n)$ | True | Discard added terms that grow more slowly |
| $O(n + \log n) = O(n)$ | True | Same reason |
| $\Theta(n\log_2 n) = \Theta(n\log_{10} n)$ | True | $\log_2 n / \log_{10} n \approx 3.32$, a constant (change of base) |
| $\Theta(\log^2 n) = \Theta(\log n)$ | False | $\log^2 n$ grows more than a constant factor faster than $\log n$ |
| $O(n\log n) = O(n)$ | False | Different sets; $O(n)$ is a subset of $O(n\log n)$ |
| If $x \in O(n\log n)$ then $x \in O(n^2)$ | True | Mergesort is $O(n\log n)$, so by definition also $O(n^2)$ |
| If $x \in \Theta(n\log n)$ then $x \in \Theta(n^2)$ | False | Mergesort is strictly $\Theta(n\log n)$ |
| If $x \in O(n\log n)$ then $x \in O(n)$ | False | $x$ might be in $O(n)$, but might not be (e.g. mergesort) |

#### Proof that $\Theta(n + \log n) = \Theta(n)$

1. Constants do not matter, so $\Theta(2n) = \Theta(n)$.
2. Since $\log n < n$: $n + \log n < n + n = 2n$.
3. Also $n + \log n \ge n$.
4. So $n \le n + \log n < 2n$, which matches the $\Theta$ definition with $c_2 = 1$, $c_1 = 2$.
5. Therefore $t(n) = n + \log n \in \Theta(n)$, and the two sets are equivalent in asymptotic efficiency.

### Analysing Non-Recursive Algorithms

Steps for calculating efficiency:

1. **Identify the basic operations** — those executed repeatedly at the core of the algorithm.
   - Sorting: comparisons and swaps.
   - Matrix multiplication: multiplications and additions.
2. **Set up an equation** $C(n) = \dots$ that counts the basic operations for an input of size $n$.
3. **Solve the equation** and state the efficiency class.

### Summation Rules

| Rule | Statement |
|---|---|
| R1 (constant factor) | $\displaystyle\sum_{i=l}^{u} c\,a_i = c\sum_{i=l}^{u} a_i$ |
| R2 (sum/difference) | $\displaystyle\sum_{i=l}^{u} (a_i \pm b_i) = \sum_{i=l}^{u} a_i \pm \sum_{i=l}^{u} b_i$ |
| S1 (counting ones) | $\displaystyle\sum_{i=l}^{u} 1 = u - l + 1$ |
| S2 (arithmetic series) | $\displaystyle\sum_{i=0}^{n} i = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \approx \frac{n^2}{2} \in \Theta(n^2)$ |

S2 is the familiar $1 + 2 + 3 + \dots + n = n(n+1)/2$.

### Example: Maximum Element

```text
int MysteryFunction( A[0 .. n-1] )
    MysteryVal = A[0]
    for i = 1 to n - 1:
        if A[i] > MysteryVal:
            MysteryVal = A[i]
    return MysteryVal
```

1. **What it does**: finds the largest element in the array (rename it `maxElement`, with `maxVal`).
2. **Basic operation**: the comparison `A[i] > maxVal`.
3. **Count**: one comparison per loop iteration:

$$
C(n) = \sum_{i=1}^{n-1} 1 = n - 1 \in \Theta(n)
$$

4. **Class**: $\Theta(n)$ (and therefore also $O(n)$). Every case is the same because the loop always runs to completion.

### Example: Is The Array A Set?

You have loaded a file of strings into an array $A$ and want to check for duplicates, i.e. whether each element appears at most once.

#### Brute force

```java
boolean isset(A) {
  for (i=0; i<A.length; i++)
    for (j=0; j<A.length; j++)
      if (i != j and A[i] == A[j])
         return false;
  return true;
}
```

- **Worst case**: no duplicates, so both loops run to completion.
- **Basic operation**: comparison.
- **Count**: every ordered pair is examined; about $(n-1)^2$ to $n^2$ comparisons, i.e. $\Theta(n^2)$. Each unordered pair is checked twice.

#### Decrease and conquer (iterative)

Compare each element only with the elements after it:

```java
boolean isset(A) {
  for (i=0; i<A.length-1; i++)
    for (j=i+1; j<A.length; j++)
      if (A[i] == A[j]) return false;
  return true;
}
```

The inner loop runs $(n-1) + (n-2) + \dots + 1 = n(n-1)/2$ times in the worst case (no early exit). Full derivation:

$$
\begin{aligned}
C_{worst}(n) &= \sum_{i=0}^{n-2}\sum_{j=i+1}^{n-1} 1 \\
&= \sum_{i=0}^{n-2} (n-1-i) && \text{S1 on the inner sum} \\
&= \sum_{i=0}^{n-2} (n-1) - \sum_{i=0}^{n-2} i && \text{R2} \\
&= (n-1)\sum_{i=0}^{n-2} 1 - \frac{(n-2)(n-1)}{2} && \text{R1 and S2} \\
&= (n-1)^2 - \frac{(n-2)(n-1)}{2} && \text{S1} \\
&= \frac{(n-1)n}{2} \approx \frac12 n^2 \in \Theta(n^2)
\end{aligned}
$$

Worst case $\Theta(n^2)$; the average case is also $\Theta(n^2)$.

#### Decrease and conquer (recursive)

```java
Boolean isset(Array A, int index=0) {
  if (index >= A.length-1) return true;
  for (i=index+1; i<A.length; i++) {
    if (A[index]==A[i]) return false;
  }
  return isset(A, index+1);
}
```

The recursion should not scare you: this is materially identical to the iterative version. Worst and average case are both $\Theta(n^2)$.

#### Transform and conquer

Sort the array, then any duplicates are adjacent, so a single linear scan finds them:

```java
boolean isset(A) {
  sort(A);
  for (int i=0; i<A.length-1; i++)
    if (A[i] == A[i+1]) return false;
  return true;
}
```

| Step | Efficiency |
|---|---|
| Sort (best algorithms) | $\Theta(n\log n)$ |
| Linear scan (worst case) | $\Theta(n)$ |
| Sequence of both | $\Theta(\max\{n\log n, n\}) = \Theta(n\log n)$ |

| Algorithm | Worst case |
|---|---|
| Brute force / decrease and conquer | $\Theta(n^2)$ |
| Transform and conquer (presort) | $\Theta(n\log n)$ — faster |

### Analysing Recursive Algorithms

#### Definitions

> **Recurrence relation**: A recursive mathematical function with a recursive case and a base case, used to count operations of a recursive algorithm.

Recursive analysis follows the same pattern as sequential analysis:

1. Determine the core operation.
2. Create an equation for the number of repetitions — now a **recurrence relation**, not a summation.
3. Solve it, by **backward substitution** or the **Master Theorem**. (Closed-form recurrence solutions are not covered; see Levitin's appendices.)
4. Derive the efficiency class.

Example recurrence:

$$
M(n) =
\begin{cases}
0 & \text{if } n = 0 \\
M(n-1) + 1 & \text{otherwise}
\end{cases}
$$

The two recurrence shapes in this course are:

$$
T(n) = aT(n-k) + f(n) \qquad\text{(decrease by a constant, like } M(n)\text{)}
$$

$$
T(n) = aT(n/b) + f(n) \qquad\text{(divide by a constant factor)}
$$

### Backward Substitution Examples

#### Factorial

```text
int F(n) {
    if n == 0 return 1;
    return F(n-1) * n;
}
```

The basic operation is multiplication, performed once per recursive call. Let $M(n)$ be the number of multiplications:

$$
M(0) = 0, \qquad M(n) = M(n-1) + 1
$$

Substitute backwards:

$$
\begin{aligned}
M(n) &= M(n-1) + 1 \\
&= [M(n-2) + 1] + 1 = M(n-2) + 2 \\
&= [M(n-3) + 1] + 2 = M(n-3) + 3 \\
&\;\;\vdots \\
&= M(n-k) + k
\end{aligned}
$$

When $k = n$: $M(n) = M(0) + n = n$. So $M(n) \in \Theta(n)$ — exactly $n$ in this case.

#### Counting bits

```text
int CountBits(int n such that n > 0):
    if n == 1 return 1
    else return 1 + CountBits(n / 2)
```

The basic operation is the addition of 1 on each call. Let $A(n)$ count additions:

$$
A(1) = 0, \qquad A(n) = A(\lfloor n/2 \rfloor) + 1 \quad (n > 1)
$$

The floor is needed for an integer argument, which makes substitution awkward. The trick is to assume $n$ is a power of 2: let $n = 2^k$, i.e. $k = \log_2 n$, so $n/2 = 2^{k-1}$.

$$
\begin{aligned}
A(2^k) &= A(2^{k-1}) + 1 \\
&= [A(2^{k-2}) + 1] + 1 = A(2^{k-2}) + 2 \\
&\;\;\vdots \\
&= A(2^{k-k}) + k = A(2^0) + k = k
\end{aligned}
$$

So $A(n) = \log_2 n \in \Theta(\log n)$. The **smoothness theorem** extends the result to all positive $n$.

#### A more complicated case

Solve $M(n) = 2M(n/2) + 1$ with $M(1) = 0$. Let $n = 2^k$:

$$
\begin{aligned}
M(2^k) &= 2M(2^{k-1}) + 1 \\
&= 2\,[2M(2^{k-2}) + 1] + 1 = 2^2 M(2^{k-2}) + 2 + 1 \\
&= 2^2\,[2M(2^{k-3}) + 1] + 2 + 1 = 2^3 M(2^{k-3}) + 2^2 + 2 + 1
\end{aligned}
$$

After $i$ substitutions:

$$
M(2^k) = 2^i M(2^{k-i}) + 2^{i-1} + 2^{i-2} + \dots + 2 + 1 = 2^i M(2^{k-i}) + 2^i - 1
$$

using $1 + 2 + 4 + \dots + 2^{i-1} = 2^i - 1$ (e.g. $1 + 2 + 4 = 7 = 2^3 - 1$). When $i = k$, the base case $M(1) = 0$ gives:

$$
M(n) = 2^k M(1) + 2^k - 1 = n - 1 \in \Theta(n)
$$

### Fibonacci Recurrence

```text
int F(n):
    if n <= 1 return n
    else return F(n-1) + F(n-2)
```

The basic operation is an addition:

$$
A(n) = A(n-1) + A(n-2) + 1
$$

This needs a different solution method (the **characteristic equation**), giving:

$$
A(n) \in \Theta(1.61803^n)
$$

The brute-force Fibonacci algorithm is exponential, with base equal to the golden ratio.

### The Master Theorem

There is no general solution to every recurrence. The **Master Theorem** gives the asymptotic class of divide-style recurrences directly, as a shortcut that replaces backward substitution. You must know how to apply it; you do not need to prove or derive it (see Levitin, Appendix B).

> **Master Theorem**: If $T(n) = aT(n/b) + f(n)$ with $f(n) \in \Theta(n^d)$ and $T(1) = c$, then
>
> $$
> T(n) \in
> \begin{cases}
> \Theta(n^d) & \text{if } a < b^d \\
> \Theta(n^d \log n) & \text{if } a = b^d \\
> \Theta(n^{\log_b a}) & \text{if } a > b^d
> \end{cases}
> $$
>
> Analogous results hold for $O$ and $\Omega$.

| Symbol | Meaning |
|---|---|
| $a$ | Number of subproblems solved recursively |
| $b$ | Factor by which the input size shrinks |
| $f(n) \in \Theta(n^d)$ | Work done outside the recursive calls (divide + combine) |

Steps to apply it:

1. Match the recurrence to $T(n) = aT(n/b) + f(n)$ and read off $a$, $b$.
2. Find $d$ from $f(n) \in \Theta(n^d)$.
3. Compare $a$ with $b^d$ and pick the case.

**Example 1**: $A(n) = A(n/2) + 1$, $A(1) = 0$.

- $a = 1$, $b = 2$, $c = 0$, $f(n) \in \Theta(1) = \Theta(n^0)$, so $d = 0$.
- $b^d = 2^0 = 1 = a$, so case 2.
- $T(n) \in \Theta(n^0 \log n) = \Theta(\log n)$.

**Example 2**: $A(n) = 2A(n/2) + 1$, $A(1) = 1$.

- $a = 2$, $b = 2$, $c = 1$, $f(n) \in \Theta(n^0)$, so $d = 0$.
- $2 > 2^0$, so $a > b^d$, case 3.
- $A(n) \in \Theta(n^{\log_2 2}) = \Theta(n)$.
