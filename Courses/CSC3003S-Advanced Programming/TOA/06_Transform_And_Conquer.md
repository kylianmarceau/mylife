---
tags:
  - advanced-programming
---

# Transform And Conquer

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [6 - TOA Transform and Conquer.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/6%20-%20TOA%20Transform%20and%20Conquer.pdf), Patrick Marais, University of Cape Town, pages 1–27
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Instance simplification (Gaussian elimination, presorting), representation change (Horner's rule, binary exponentiation) and problem reduction (LCM, optimisation, state-space graphs).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Transform-And-Conquer Strategy|The Transform-And-Conquer Strategy]]
  - [[#Gaussian Elimination|Gaussian Elimination]]
  - [[#Presorting|Presorting]]
  - [[#Is Presorting Better?|Is Presorting Better?]]
  - [[#Presorted Selection|Presorted Selection]]
  - [[#Evaluating Polynomials By Brute Force|Evaluating Polynomials By Brute Force]]
  - [[#Horner's Rule|Horner's Rule]]
  - [[#Binary Exponentiation|Binary Exponentiation]]
  - [[#Problem Reduction: LCM And Optimisation|Problem Reduction: LCM And Optimisation]]
  - [[#Reduction To Graph Problems: River Crossing|Reduction To Graph Problems: River Crossing]]
  - [[#Strengths And Weaknesses|Strengths And Weaknesses]]

---

## Core Content

### The Transform-And-Conquer Strategy

#### Definitions

> **Transform and conquer**: Transform the problem in some way, then solve the transformed problem. ("The secret of life… to replace one worry with another" — Charles M. Schulz.)

> **Instance simplification**: Transform to a simpler or more convenient instance of the same problem.

> **Representation change**: Transform to a different representation of the same instance.

> **Problem reduction**: Transform to an instance of a different problem for which an algorithm is already available.

![Three kinds of transformation](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/06_Transform_And_Conquer/transform-types.svg)

*The instance is transformed into a simpler instance, another representation, or another problem's instance, which is then solved.*

| Approach | Examples |
|---|---|
| Instance simplification | Presorting; Gaussian elimination |
| Representation change | Balanced search trees (CS2); heaps and heapsort (CS2); polynomial evaluation by Horner's rule; binary exponentiation |
| Problem reduction | Lowest common multiple; reductions to graph problems |

### Gaussian Elimination

Gaussian elimination solves a fully determined system of $n$ linear equations in $n$ unknowns, $A\mathbf{x} = \mathbf{b}$.

1. **Transform (simplify)**: forward elimination turns $A$ into an upper-triangular matrix, applying the same row operations to $\mathbf{b}$.
2. **Conquer**: solve the triangular system by backward substitution, from the last unknown upwards.

$$
\begin{pmatrix}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44}
\end{pmatrix}
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix}
=
\begin{pmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{pmatrix}
\;\Longrightarrow\;
\begin{pmatrix}
b_{11} & b_{12} & b_{13} & b_{14} \\
0 & b_{22} & b_{23} & b_{24} \\
0 & 0 & b_{33} & b_{34} \\
0 & 0 & 0 & b_{44}
\end{pmatrix}
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix}
=
\begin{pmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \end{pmatrix}
$$

| Phase | Efficiency |
|---|---|
| Forward elimination | $\Theta(n^3)$ |
| Backward substitution | $\Theta(n^2)$ |

### Presorting

#### Definitions

> **Presorting**: Preprocessing a problem by sorting its list, transforming it into a simpler instance of the same problem.

Many list problems are easier once the list is sorted:

- Searching
- Computing the median (the selection problem)
- Finding repeated elements
- Convex hull and closest pair

Presorting adds a $\Theta(n\log n)$ preprocessing overhead. In exchange, the sorted problem often improves by at least one efficiency class over the unsorted problem (e.g. $\Theta(n^2) \to \Theta(n)$).

### Is Presorting Better?

Sorting costs $\Theta(n\log n)$, so presorting only pays off when the alternative algorithm is less efficient than that.

| Problem | Brute force | Presort? |
|---|---|---|
| Closest pair | $\Theta(n^2)$ → $\Theta(n\log n)$ with presorting | Yes |
| Checking uniqueness | $\Theta(n^2)$ | Yes |
| Finding min and max | $\Theta(n)$ | No |
| Finding the median | $\Theta(n^2)$ | Yes |
| Searching an unordered array (once) | $\Theta(n)$ | No |

### Presorted Selection

Find the $k$th smallest element of $A[1], \dots, A[n]$. Special cases: minimum ($k = 1$), maximum ($k = n$), median ($k = \lceil n/2 \rceil$).

| Presorting-based | Partition-based (variable decrease and conquer) |
|---|---|
| 1. Sort the list. | 1. Partition around a pivot using quicksort's partitioning; the pivot lands at $A[s]$. |
| 2. Return $A[k]$. | 2. If $s = k$, return $A[s]$. |
| | 3. If $s < k$, repeat with $A[s+1..n]$. |
| | 4. If $s > k$, repeat with $A[1..s-1]$. |

| Algorithm | Efficiency | Notes |
|---|---|---|
| Presorting | $\Theta(n\log n) + \Theta(1) = \Theta(n\log n)$ | Also identifies the $k$ smallest elements, not just the $k$th |
| Partition-based | Worst $\Theta(n^2)$; best $\Theta(n)$; average $\Theta(n)$ | |
| Simple linear scan | $\Theta(n)$ | Better for max and min |

### Evaluating Polynomials By Brute Force

A polynomial of degree $n$ has the form:

$$
p(x) = a_n x^n + \dots + a_i x^i + \dots + a_0
$$

Example: evaluate $p(x) = 2x^4 - x^3 + 3x^2 + x - 5$ at $x = 3$. The obvious brute-force approach computes each power separately:

$$
p(3) = 2(3)^4 - 3^3 + 3(3)^2 + 3 - 5
$$

For a polynomial of degree $n$, just the first term $a_n x^n$ needs $n$ multiplications. Computing every term this way needs

$$
n + (n-1) + \dots + 1 \in \Theta(n^2)
$$

multiplications. Computing $x^n$ more efficiently helps, but Horner's rule does even better for large polynomials and is very easy.

### Horner's Rule

#### Definitions

> **Horner's rule**: A representation change that factors $x$ out of a polynomial as far as possible, so it can be evaluated with one multiplication and one addition per coefficient.

Factor $x$ out repeatedly:

$$
\begin{aligned}
p(x) &= 2x^4 - x^3 + 3x^2 + x - 5 \\
&= (2x^3 - x^2 + 3x + 1)\,x - 5 \\
&= ((2x^2 - x + 3)\,x + 1)\,x - 5 \\
&= (((2x - 1)\,x + 3)\,x + 1)\,x - 5
\end{aligned}
$$

Evaluate from the innermost bracket outwards.

**Example**: $p(x) = 2x^3 - x^2 - 6x + 5$ at $x = 3$, i.e. $p(x) = ((2x - 1)x - 6)x + 5$.

| Coefficient $C[i]$ | 2 | $-1$ | $-6$ | 5 |
|---|---|---|---|---|
| $p$ | 2 | $2 \cdot 3 - 1 = 5$ | $5 \cdot 3 - 6 = 9$ | $9 \cdot 3 + 5 = 32$ |

| Method | Work for this example |
|---|---|
| Brute force: $2\cdot3\cdot3\cdot3 - 3\cdot3 - 6\cdot3 + 5 = 32$ | 5 multiplications, 3 additions/subtractions |
| Horner's rule | 3 multiplications, 3 additions/subtractions |

```text
double horner(coefficients[0..n], x):
    p = coefficients[n]
    for i = n - 1 downto 0:
        p = x * p + coefficients[i]
    return p
```

**Efficiency**: multiplications $M(n)$ and additions $A(n)$ are equal:

$$
M(n) = A(n) = \sum_{i=0}^{n-1} 1 = n
$$

Horner's rule evaluates the whole polynomial with as many multiplications as brute force spends on the first term alone.

Horner's rule is no help for a polynomial with a single non-zero term, such as $p(x) = x^n$: it still needs $n$ multiplications, the same as computing $x^n$ directly.

### Binary Exponentiation

Binary exponentiation computes $a^n$ efficiently using the binary representation of $n$. Represent $n$ as a polynomial evaluated at $x = 2$:

$$
n = p(2) = b_k 2^k + \dots + b_i 2^i + \dots + b_0
$$

The coefficients $b_k \dots b_0$ are the binary digits of $n$. Example: $13 = 1\cdot2^3 + 1\cdot2^2 + 0\cdot2 + 1$, i.e. $1101_2$.

Horner's rule computes $p(2)$, starting from the leading digit (always 1):

```text
p = 1                     // leading digit is always 1
for i = k-1 downto 0:
    p = 2 * p + C[i]
```

Each step changes the exponent from $p$ to $2p + C[i]$, and

$$
a^{2p + C[i]} = a^{2p} \cdot a^{C[i]} = (a^p)^2 \cdot a^{C[i]} =
\begin{cases}
(a^p)^2 & \text{if } C[i] = 0 \\
(a^p)^2 \cdot a & \text{if } C[i] = 1
\end{cases}
$$

So the exponent loop becomes "square, then multiply by $a$ if the bit is 1":

| Horner's rule for $p(x)$ | Horner's rule for $a^n$ |
|---|---|
| `p = C[n]` | `p = a` |
| `for i = n-1 downto 0:` | `for i = k-1 downto 0:` |
| `    p = x*p + C[i]` | `    p = p*p` |
| | `    if C[i] == 1: p = p*a` |
| `return p` | `return p` |

**Example**: $a^{13}$, with $p(x) = ((x + 1)x + 0)x + 1$ at $x = 2$:

| Binary digit $C[i]$ | 1 | 1 | 0 | 1 |
|---|---|---|---|---|
| Exponent $p$ | 1 | $1\cdot2 + 1 = 3$ | $3\cdot2 + 0 = 6$ | $6\cdot2 + 1 = 13$ |
| Power $a^p$ | $a^1$ | $(a^1)^2 \cdot a = a^3$ | $(a^3)^2 = a^6$ | $(a^6)^2 \cdot a = a^{13}$ |

**Efficiency** (basic operation: multiplication):

| Method | Multiplications |
|---|---|
| Brute force $a \cdot a \cdots a$ | $M(n) = n - 1 \in \Theta(n)$ |
| Horner (binary) exponentiation | At most 2 per loop iteration |

With $k$ the length of the bit representation, $k - 1 = \lfloor \log_2 n \rfloor$, so:

$$
k - 1 \le M(n) \le 2(k-1) \;\Rightarrow\; M(n) \le 2\lfloor\log_2 n\rfloor \in \Theta(\log n)
$$

### Problem Reduction: LCM And Optimisation

Problem reduction is also used in complexity theory to classify problems.

#### Definitions

> **Least common multiple (LCM)**: The smallest integer divisible by both positive integers $m$ and $n$.

**LCM via GCD**: rather than factorising, reduce LCM to GCD, which Euclid's algorithm solves efficiently:

$$
\operatorname{lcm}(m, n) = \frac{m \cdot n}{\gcd(m, n)}
$$

Example: $\operatorname{lcm}(24, 60) = 1440 / 12 = 120$.

**Optimisation problems**: maximisation seeks a function's maximum and minimisation its minimum. Either reduces to the other:

$$
\min f(x) = -\max\,[-f(x)]
$$

### Reduction To Graph Problems: River Crossing

#### Definitions

> **State-space graph**: A graph whose vertices represent states of a problem and whose edges represent valid transitions between states. It has start and goal vertices and is widely used in AI.

Reduce a problem to a graph, then find a path from the start node to the goal node.

**River crossing puzzle**: a peasant (P), wolf (w), goat (g) and cabbage (c) must cross a river.

- The boat carries the peasant plus at most one item.
- The goat and wolf cannot be left alone together; nor can the goat and cabbage.
- Find a path from the initial state to the goal state, ideally of minimal length.

States are written `left bank || right bank`. The safe states are `Pwgc||`, `wc||Pg`, `Pwc||g`, `w||Pgc`, `c||Pwg`, `Pwg||c`, `Pgc||w`, `g||Pwc`, `Pg||wc`, `||Pwgc`.

![River crossing state graph](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/06_Transform_And_Conquer/river-crossing.svg)

*Every safe state is a vertex and every legal boat trip an edge; any shortest start-to-goal path solves the puzzle.*

A shortest solution (7 crossings):

1. `Pwgc||` → `wc||Pg` (take the goat across)
2. → `Pwc||g` (return alone)
3. → `c||Pwg` (take the wolf across)
4. → `Pgc||w` (bring the goat back)
5. → `g||Pwc` (take the cabbage across)
6. → `Pg||wc` (return alone)
7. → `||Pwgc` (take the goat across)

A symmetric solution takes the cabbage at step 3 (via `w||Pgc` and `Pwg||c`).

### Strengths And Weaknesses

| Strengths | Weaknesses |
|---|---|
| Allows powerful data structures to be applied via representation change (e.g. trees) | Can be difficult to derive, especially reductions |
| Effective in complexity theory | |
