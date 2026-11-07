---
tags:
  - advanced-programming
---

# Decrease And Conquer

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [4 - TOA Decrease and Conquer.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/4%20-%20TOA%20Decrease%20and%20Conquer.pdf), Patrick Marais, University of Cape Town, pages 1–27
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> The three decrease-and-conquer variants: decrease by a constant (insertion sort, topological sort, subsets, permutations), by a constant factor (exponentiation, fake coin, Russian multiplication) and by a variable amount (Euclid, quickselect, interpolation search).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Decrease-And-Conquer Strategy|The Decrease-And-Conquer Strategy]]
  - [[#Decrease And Conquer Versus Divide And Conquer|Decrease And Conquer Versus Divide And Conquer]]
  - [[#Map Of Algorithms, Strengths And Weaknesses|Map Of Algorithms, Strengths And Weaknesses]]
  - [[#Insertion Sort|Insertion Sort]]
  - [[#Topological Sort|Topological Sort]]
  - [[#Generating The Power Set|Generating The Power Set]]
  - [[#Generating Permutations By Insertion|Generating Permutations By Insertion]]
  - [[#Johnson-Trotter Algorithm|Johnson-Trotter Algorithm]]
  - [[#Exponentiation|Exponentiation]]
  - [[#Fake-Coin Problem|Fake-Coin Problem]]
  - [[#Multiplication À La Russe|Multiplication À La Russe]]
  - [[#Euclid's GCD (Variable-Size Decrease)|Euclid's GCD (Variable-Size Decrease)]]
  - [[#Kth Order Statistic And Quickselect|Kth Order Statistic And Quickselect]]
  - [[#Interpolation Search|Interpolation Search]]

---

## Core Content

### The Decrease-And-Conquer Strategy

#### Definitions

> **Decrease and conquer**: Solve a smaller instance of the problem, then extend that solution to obtain a solution to the original problem. Also called the **inductive** or **incremental** approach.

> **Decrease by a constant**: The instance shrinks by the same constant (often 1) at each step: size $n \to n - c$.

> **Decrease by a constant factor**: The instance shrinks by the same factor (usually 2) at each step: size $n \to n/c$.

> **Variable-size decrease**: The amount by which the instance shrinks changes from one step to the next.

![Decrease variants](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/decrease-variants.svg)

*All three variants reduce a problem of size $n$ to one smaller subproblem; they differ only in how much smaller it is.*

### Decrease And Conquer Versus Divide And Conquer

| Strategy | Subproblems solved | What happens to the rest |
|---|---|---|
| Decrease by a constant factor | One subproblem of size $n/2$ | The other half (or constant fraction) of the work is **thrown away** |
| Divide and conquer | Two subproblems of size $n/2$ | **Both** halves are solved, then the solutions are combined |

Binary search is decrease and conquer (it discards half the array). Mergesort is divide and conquer (it sorts both halves).

### Map Of Algorithms, Strengths And Weaknesses

| Variant | Algorithms |
|---|---|
| Decrease by a constant (often 1) | Insertion sort; graph searching (DFS, BFS); generating permutations and subsets; topological sort |
| Decrease by a constant factor (usually 2) | Binary search (see Levitin for the formal analysis); fake-coin problem; multiplication à la russe |
| Variable-size decrease | Euclid's algorithm; interpolation search; finding the $k$th order statistic (e.g. the median) |

| Strengths | Weaknesses |
|---|---|
| Can be implemented top-down (recursively) or bottom-up (without recursion) | Less widely applicable, especially decrease by a constant factor |
| Often very efficient — possibly $\Theta(\log n)$ | |

### Insertion Sort

Insertion sort is decrease by 1 and conquer:

1. Assume the first $n-1$ elements are already sorted (by recursively insertion-sorting them).
2. Insert the remaining element into its correct position in the sorted part.

The idea is recursive, but it is better performed iteratively, bottom-up.

```text
insertionSort(Array arr, int n)
    if (n <= 1) return;            // base case
    insertionSort(arr, n-1);
    // insert last element
    ins = arr[n-1];  j = n-2;
    while (j >= 0 and arr[j] > ins)
        arr[j+1] = arr[j];
        j = j - 1;
    arr[j+1] = ins;
```

Trace on `6 5 0 2 8 7 4` (the bar separates the sorted prefix from the rest):

| Step | Array |
|---|---|
| Start | `6 | 5 0 2 8 7 4` |
| Insert 5 | `5 6 | 0 2 8 7 4` |
| Insert 0 | `0 5 6 | 2 8 7 4` |
| Insert 2 | `0 2 5 6 | 8 7 4` |
| Insert 8 | `0 2 5 6 8 | 7 4` |
| Insert 7 | `0 2 5 6 7 8 | 4` |
| Insert 4 | `0 2 4 5 6 7 8` |

The recursive view on `6 5 0 2 8 7 9`: `sort(1); insert(2nd)`, then `sort(2); insert(3rd)`, … up to `sort(7)`. Each call sorts a prefix one element longer.

| Case | Efficiency |
|---|---|
| Worst (reverse-sorted input) | $\Theta(n^2)$ |
| Partially sorted input | Works well — few shifts are needed |

### Topological Sort

#### Definitions

> **Directed acyclic graph (DAG)**: A directed graph with no directed cycles.

> **Topological sort**: A listing of a DAG's vertices such that for every directed edge, the source vertex appears before the destination vertex.

> **Source vertex**: A vertex with no incoming edges.

Properties:

- There may be several valid orderings.
- The problem is not solvable if the graph has a cycle.
- It can also be solved with depth-first search (see Levitin).

Applications:

- Ordering courses that have prerequisites.
- Evaluating spreadsheet formulas with dependencies.
- Ordering tasks in a complex project.

**Source-removal algorithm** (decrease by 1):

1. Find a source vertex (in-degree 0).
2. Remove it and all its outgoing edges, and append it to the sorted list.
3. Repeat. If no source exists, either all vertices are listed (finished) or the remaining graph has a cycle.

Example with edges $a \to b$, $a \to c$, $b \to c$, $b \to d$, $c \to d$:

| Step | Removed | Edges removed | List |
|---|---|---|---|
| 1 | $a$ | $a \to b$, $a \to c$ | $\{a\}$ |
| 2 | $b$ | $b \to c$, $b \to d$ | $\{a, b\}$ |
| 3 | $c$ | $c \to d$ | $\{a, b, c\}$ |
| 4 | $d$ | — | $\{a, b, c, d\}$ |

![Topological sort by source removal](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/topological-sort.svg)

*Each step removes the current source; in-degree counts show which vertex becomes a source next.*

### Generating The Power Set

#### Definitions

> **Power set**: The set of all $2^n$ subsets of $\{a_1, a_2, \dots, a_n\}$. Element order does not matter and there are no duplicates.

Example:

$$
\mathcal{P}(\{a,b,c\}) = [\,\{\},\ \{a\},\ \{b\},\ \{a,b\},\ \{c\},\ \{a,c\},\ \{b,c\},\ \{a,b,c\}\,]
$$

| Method | How it works |
|---|---|
| Decrease by 1 and conquer | Recursively generate all subsets of $\{a_1, \dots, a_{n-1}\}$ (base case: $\{\}$). Keep them, and also add $a_n$ to each of them. |
| Bit strings (brute force) | Enumerate all values $0 \dots 2^n - 1$. Assign each element a bit position (LSB to MSB works best). A 1 bit means the element is present. |
| Binary reflected Gray code | Gives a **minimal-change** power set: consecutive subsets differ by a single bit flip (one element added or removed). See Levitin. |

With LSB = $a$, the bit-string order $000, 001, 010, 011, \dots$ produces exactly the list above.

### Generating Permutations By Insertion

Permutations are needed as a component of exhaustive search. Generate all orderings of $\{1, \dots, n\}$; these can be used as indices for any other objects.

Decrease by 1 and conquer:

1. Generate all $(n-1)!$ permutations of $\{1, \dots, n-1\}$.
2. Insert $n$ into every possible position of each one.
3. Insert alternately from right to left and from left to right. This satisfies the **minimal-change requirement**: each permutation is obtained from the previous one by swapping two adjacent elements.

| Stage | Permutations |
|---|---|
| Start | 1 |
| Insert 2 (right to left) | 12, 21 |
| Insert 3 into 12 (right to left) | 123, 132, 312 |
| Insert 3 into 21 (left to right) | 321, 231, 213 |

![Permutation generation tree](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/permutation-tree.svg)

*Alternating the insertion direction makes neighbouring permutations differ by one adjacent swap.*

### Johnson-Trotter Algorithm

#### Definitions

> **Mobile element**: An element $k$ whose arrow points to an adjacent element smaller than $k$.

Johnson–Trotter generates permutations without first generating permutations of smaller lists. Each element carries a direction arrow.

Example: in $\overrightarrow{3}\ \overleftarrow{2}\ \overrightarrow{4}\ \overleftarrow{1}$, 3 and 4 are mobile (3 points at 2, 4 points at 1). 2 and 1 are not (2 points at 3, which is larger; 1 points at 4).

Algorithm:

1. Initialise the first permutation $\overleftarrow{1}\ \overleftarrow{2} \cdots \overleftarrow{n}$ (all arrows left).
2. While the last permutation has a mobile element:
   1. Find its largest mobile element $k$.
   2. Swap $k$ with the neighbour its arrow points to.
   3. Reverse the direction of all elements larger than $k$.
   4. Add the new permutation to the list.
3. Return the list.

Trace for $n = 3$:

| Permutation | Largest mobile | Action |
|---|---|---|
| $\overleftarrow{1}\,\overleftarrow{2}\,\overleftarrow{3}$ | 3 | swap with 2 |
| $\overleftarrow{1}\,\overleftarrow{3}\,\overleftarrow{2}$ | 3 | swap with 1 |
| $\overleftarrow{3}\,\overleftarrow{1}\,\overleftarrow{2}$ | 2 | swap with 1, reverse 3 |
| $\overrightarrow{3}\,\overleftarrow{2}\,\overleftarrow{1}$ | 3 | swap with 2 |
| $\overleftarrow{2}\,\overrightarrow{3}\,\overleftarrow{1}$ | 3 | swap with 1 |
| $\overleftarrow{2}\,\overleftarrow{1}\,\overrightarrow{3}$ | none | stop |

![Johnson-Trotter steps](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/johnson-trotter.svg)

*At each step the largest mobile element moves one place in its arrow's direction.*

### Exponentiation

Computing $a^n$ can be done two ways.

**Bottom-up iteration (decrease by a constant)**: $1 \cdot a \cdots a$ ($n$ times).

```c
expv = 1;
for (i = 0; i < n; i++)
    expv *= a;
```

This is clearly $\Theta(n)$.

**Top-down recursion (decrease by a constant factor)**: use

$$
a^n =
\begin{cases}
\left(a^{n/2}\right)^2 & n \text{ even} \\
\left(a^{(n-1)/2}\right)^2 \cdot a & n \text{ odd} \\
1 & n = 0
\end{cases}
$$

Odd exponents need one extra multiply, which does not change the asymptotic complexity. Each step needs 1 or 2 multiplications:

$$
M(n) = M(n/2) + \Theta(1)
$$

By the Master Theorem ($a = 1$, $b = 2$, $d = 0$, so $a = b^d$, case 2): $M(n) \in \Theta(n^0\log n) = \Theta(\log n)$.

### Fake-Coin Problem

Among $n$ coins, one is fake and weighs less. A balance scale can compare any two sets of coins.

**Two-pile version**:

1. Divide the coins into two piles of $\lfloor n/2 \rfloor$, keeping one coin aside if $n$ is odd.
2. Weigh the piles. If they weigh the same, the coin set aside is fake.
3. Otherwise, continue recursively with the lighter pile.

$$
W(n) = W(\lfloor n/2 \rfloor) + 1 \ (n > 1), \quad W(1) = 0 \;\Rightarrow\; W(n) = \lfloor \log_2 n \rfloor \in \Theta(\log_2 n)
$$

**Three-pile version** (better):

1. Divide into three piles of sizes $\lfloor n/3 \rfloor$, $\lfloor n/3 \rfloor$ and $n - 2\lfloor n/3 \rfloor$.
2. Weigh the first two. If they balance, discard both and continue with the third pile.
3. Otherwise continue recursively with the lighter pile.

$$
W(n) = W(\lceil n/3 \rceil) + 1 \ (n > 1), \quad W(1) = 0 \;\Rightarrow\; W(n) \in \Theta(\log_3 n)
$$

This is better by a factor of about $\log_2 3 \approx 1.6$ than the two-pile solution.

### Multiplication À La Russe

This method multiplies two numbers using only halving, doubling and addition, avoiding multiplication tables:

$$
n \cdot m =
\begin{cases}
\dfrac{n}{2} \cdot 2m & n \text{ even} \\[6pt]
\dfrac{n-1}{2} \cdot 2m + m & n \text{ odd}
\end{cases}
$$

Stop when $n = 1$. Halving and doubling are just bit shifts, so this is efficient in hardware. It is decrease by a constant factor of 2.

Example $50 \times 20$:

$$
\begin{aligned}
50 \times 20 &= 25 \times 40 \\
&= (12 \times 80) + 40 \\
&= (6 \times 160) + 40 \\
&= (3 \times 320) + 40 \\
&= (1 \times 640) + 320 + 40 = 1000
\end{aligned}
$$

### Euclid's GCD (Variable-Size Decrease)

$$
\gcd(m, n) = \gcd(n,\ m \bmod n), \qquad \gcd(m, 0) = m
$$

The right-hand arguments are smaller, but by neither a constant amount nor a constant factor — the decrease varies. Example:

$$
\gcd(60, 24) = \gcd(24, 12) = \gcd(12, 0) = 12
$$

### Kth Order Statistic And Quickselect

#### Definitions

> **$k$th order statistic**: The $k$th smallest element in a list. The **median** is the case $k = \lceil n/2 \rceil$.

Sorting the whole list first ($\Theta(n\log n)$) may be inefficient. Quickselect uses partitioning instead:

1. Choose a pivot $p$ and partition the array around it, as in quicksort.
2. If the pivot lands at position $k-1$ (0-based), it is the answer.
3. Otherwise continue with only one partition: the left one if $k-1$ is before the pivot, the right one if after.

![Quickselect](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/quickselect.svg)

*Quickselect discards the partition that cannot contain the target rank.*

| Case | Efficiency |
|---|---|
| Average | $\Theta(n)$ |
| Worst (bad pivots every time) | $\Theta(n^2)$ |

### Interpolation Search

Interpolation search is an alternative to binary search's even split for a sorted array. It mimics how people search a phone book: to find "Bloggs", look near the beginning.

It assumes the array values between the leftmost $A[l]$ and rightmost $A[r]$ elements increase linearly.

Algorithm (search key $v$):

1. Draw a straight line through $(l, A[l])$ and $(r, A[r])$.
2. Find the point on the line at height $v$; its x-coordinate is the proposed index:

$$
x = l + \left\lfloor \frac{(v - A[l])(r - l)}{A[r] - A[l]} \right\rfloor
$$

3. If $A[x] = v$, stop. Otherwise split at $x$ like binary search and continue in the part that can contain $v$.

![Interpolation search](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/04_Decrease_And_Conquer/interpolation.svg)

*The key's value, not the midpoint, chooses where to probe.*

| Case | Key comparisons |
|---|---|
| Average | $O(\log\log n)$ — better than binary search |
| Worst | $O(n)$ |

It may beat binary search for:

- large files, and
- cases where accesses or comparisons are very expensive, such as some database applications.
