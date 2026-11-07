---
tags:
  - advanced-programming
---

# Introduction To Algorithms

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)
**Source**: [1 - TOA Introduction.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/1%20-%20TOA%20Introduction.pdf), Patrick Marais, University of Cape Town, pages 1–25
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Opening TOA lecture: what an algorithm is, design principles, the main design strategies, and three worked comparisons (Fibonacci, GCD).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Is An Algorithm?|What Is An Algorithm?]]
  - [[#Algorithm Features|Algorithm Features]]
  - [[#When A Better Algorithm Is Worth It|When A Better Algorithm Is Worth It]]
  - [[#Algorithm Design Basics|Algorithm Design Basics]]
  - [[#History Of Algorithms|History Of Algorithms]]
  - [[#Typical Problem Domains|Typical Problem Domains]]
  - [[#Types Of Algorithms (Design Strategies)|Types Of Algorithms (Design Strategies)]]
  - [[#Fibonacci: Brute-Force Recursion|Fibonacci: Brute-Force Recursion]]
  - [[#Fibonacci: Iterative Table Versions|Fibonacci: Iterative Table Versions]]
  - [[#Fibonacci: Closed-Form Formula|Fibonacci: Closed-Form Formula]]
  - [[#Greatest Common Divisor|Greatest Common Divisor]]
  - [[#Course Resources, Tests And Practicals|Course Resources, Tests And Practicals]]

---

## Core Content

### What Is An Algorithm?

#### Definitions

> **Algorithm**: A sequence of unambiguous instructions for solving a well-defined problem. An algorithm is guaranteed to terminate if the input is valid.

> **Valid input**: An input that belongs to the clearly specified range of inputs the algorithm is designed for.

An algorithm sits between a problem and a running program. The problem specification says what must be computed; the algorithm says how; the implementation is the algorithm written in a particular language.

![Problem, algorithm and implementation](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/01_Introduction/problem-model.svg)

*An algorithm maps every valid input of the problem to a correct output; the implementation is one concrete realisation of it.*

The lecture opens with a challenge: can you write an algorithm that takes any program as input and decides whether that program stops for every input? This is the **halting problem**, and the answer is no. No algorithm can decide halting for all programs, so some well-defined problems have no algorithm at all.

Key points about the notion of an algorithm:

- Each step must be unambiguous.
- The range of inputs must be specified carefully.
- The same algorithm can be represented in different ways (pseudocode, flowchart, code in several languages).
- Several different algorithms may solve the same problem, each with different properties (speed, memory, simplicity).

### Algorithm Features

Every algorithm must have these five features:

| Feature | Meaning |
|---|---|
| **Finite** | Terminates after a finite number of steps |
| **Definite** | Rigorously and unambiguously specified |
| **Input** | Valid inputs are clearly specified |
| **Output** | Can be proved to produce the correct output given a valid input |
| **Effective** | Steps are sufficiently simple and basic to be carried out (comprehensibility) |

### When A Better Algorithm Is Worth It

Faster algorithms are usually desirable, but there is no point in finding the fastest algorithm if:

- That part of the system is not the **bottleneck**, so speeding it up does not speed up the whole system.
- The program will only be run very few times, e.g. reconciling and merging two databases when two companies merge.
- Time is not an issue, e.g. the job can run overnight.

### Algorithm Design Basics

#### Definitions

> **Pseudocode**: A language-neutral, semi-formal description of an algorithm's steps, used to specify algorithms without committing to a programming language.

> **Generality**: How wide a range of inputs (including special cases) an algorithm handles.

> **Optimality**: The property that no other algorithm for the problem can do better (for the measure being considered).

> **Efficiency**: How much time and space an algorithm uses, determined through formal algorithm analysis.

Designing an algorithm involves:

1. **Specify the algorithm**, typically in pseudocode. The data structures chosen are just as important as the steps.
2. Apply the **design principles**:
   - **Simplicity** — easier to understand, prove and implement.
   - **Generality** — handles the full range of inputs and special cases.
   - **Optimality** — no other algorithm can do better.
3. Perform **formal algorithm analysis** of efficiency in time and space.

![Algorithm design workflow](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/01_Introduction/design-workflow.svg)

*Design is iterative: failing a correctness proof or an efficiency analysis sends you back to revise earlier choices.*

### History Of Algorithms

| When | Who | Contribution |
|---|---|---|
| 1600 BC | Babylonians | Algorithms for factorisation and square roots |
| 300 BC | Euclid | Several algorithms, including the GCD algorithm below |
| 780–850 AD | Muḥammad ibn Mūsā al-Khwārizmī | Contributions to algebra and decimal numbers; the word "algorithm" comes from the Latin form of his name |
| Medieval Italy | Leonardo Fibonacci | Introduced the decimal system to the West and defined the Fibonacci series |

### Typical Problem Domains

| Domain | Examples |
|---|---|
| Sorting and searching | Ordering lists, finding a key |
| String processing | Pattern matching in text |
| Graph problems | GPS: fewest roads or shortest path from A to B |
| Combinatorial problems | Listing all permutations of a set |
| Geometric problems | Closest pair, convex hull |
| Numerical problems | Solving systems of equations, random numbers, matrix multiplication |

### Types Of Algorithms (Design Strategies)

These strategies structure the rest of the TOA section:

| Strategy | Core idea |
|---|---|
| **Brute force** | Follow the definition directly; try all possibilities |
| **Decrease and conquer** | Solve a larger instance in terms of one smaller instance |
| **Divide and conquer** | Break the problem into distinct (non-overlapping) subproblems |
| **Transformation** (transform and conquer) | Convert the problem into another, easier one |
| **Space/time trade-off** | Use additional data structures to save time |
| **Dynamic programming** | Break the problem into *overlapping* subproblems and store their answers |
| **Greedy** | Repeatedly do what is best right now |

### Fibonacci: Brute-Force Recursion

#### Definitions

> **Fibonacci series**: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$, where each term is the sum of the two before it.

The recurrence is:

$$
F_n =
\begin{cases}
0 & n = 0 \\
1 & n = 1 \\
F_{n-1} + F_{n-2} & n > 1
\end{cases}
$$

The brute-force solution translates the definition directly into code. It looks fine:

```java
public long fibo(long n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibo(n-1) + fibo(n-2);
}
```

The problem is that it recomputes the same values again and again. Each call spawns two more calls, so the number of calls grows exponentially in $n$. Computing $F(100)$ this way is hopeless.

![Fibonacci recursion tree for F(6)](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/01_Introduction/fibonacci-tree.svg)

*The call tree for $F(6)$: $F(4)$ is computed twice, $F(3)$ three times, and $F(2)$ five times.*

### Fibonacci: Iterative Table Versions

**Version 1** fills an array bottom-up, so each value is computed exactly once. This takes $n-1$ additions, i.e. linear time and linear space.

```text
Fibo(n):
// Computes nth Fibonacci number
// Input: Non-negative integer n
// Output: nth Fibonacci number
F[0] = 0
F[1] = 1
for i = 2 to n do:
    F[i] = F[i - 1] + F[i - 2]
return F[n]
```

**Version 2** keeps only the last few values in a 3-element rolling table and uses `BigInteger`:

```java
public BigInteger fibo(int n) {
    if (n==0) return 0; if (n==1) return 1;
    BigInteger [] table = new BigInteger[3];
    table[0] = new BigInteger("0");
    table[1] = new BigInteger("1");
    for (int i=2; i<n; i++) {
        table[2] = table[1].add(table[0]);
        table[0] = table[1];
        table[1] = table[2];
    }
    return table[2];
}
```

Comparing v2 with v1:

| Aspect | v1 (full array) | v2 (rolling table) |
|---|---|---|
| Space | $\Theta(n)$ array | Constant: three cells |
| Time | $n-1$ additions | $n-1$ additions |
| Overflow | Overflows if stored in fixed-size integers ($F_{93}$ exceeds a `long`) | `BigInteger` gives exact arbitrary-size results |
| Cost per addition | Constant for fixed-size integers | Grows with the number of digits for `BigInteger` |
| Risk | Simple to get right | Easy to get wrong |

As written, v2 has bugs worth spotting. The loop runs while `i<n`, which stops one step early (for $n=2$ the loop never runs and `table[2]` is still null), so the bound should be `i<=n`. The early `return 0` / `return 1` also need to return `BigInteger` values to compile.

### Fibonacci: Closed-Form Formula

Fibonacci numbers have a closed form (Binet's formula). Because the second term shrinks to zero, rounding the first term gives the answer:

$$
F_n = \operatorname{round}\!\left(\frac{1}{\sqrt{5}}\,\phi^{\,n}\right), \qquad \phi = \frac{1+\sqrt{5}}{2} \approx 1.6180339887
$$

where $\phi$ is the golden ratio.

```java
public long fibo(int n) {
    return Math.round(
        (1.0/Math.sqrt(5.0)) *
        Math.pow(1.6180339887, n));
}
```

Why it is only **superficially** efficient:

- It looks like a single constant-time step, but computing $\phi^n$ is not free: `Math.pow` hides work, and exact power computation needs about $\log n$ multiplications on numbers whose size grows with $n$.
- It has practical implementation problems with **floating-point rounding**. In Java it gives correct results only up to $F_{42}$. For $F_{43}$ it returns $433494436$ instead of the correct $433494437$, and the error grows for larger $n$.

The three Fibonacci solutions are instructive even though you rarely need Fibonacci numbers: the same problem has an exponential solution, a linear one, and a "constant-looking" one that is numerically wrong. Their complexity is analysed in the next lecture.

### Greatest Common Divisor

#### Definitions

> **Greatest common divisor (GCD)**: For two positive integers $m$ and $n$, the largest integer that divides both without remainder.

Example: $\gcd(60, 24) = 12$.

| Number | Divisors |
|---|---|
| 60 | 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 |
| 24 | 1, 2, 3, 4, 6, 8, 12, 24 |

The largest value common to both lists is 12.

#### Euclid's algorithm

Euclid's algorithm (about 2300 years old) repeatedly applies:

$$
\gcd(m, n) = \gcd(n,\; m \bmod n), \qquad \gcd(m, 0) = m
$$

```cpp
int gcd(int m, int n) {
    if (n==0) return m;
    return gcd(n, m % n);
}
```

Trace for $\gcd(14142, 3131)$:

| Step | Call |
|---|---|
| 1 | $\gcd(14142, 3131)$ |
| 2 | $\gcd(3131, 1618)$ |
| 3 | $\gcd(1618, 1513)$ |
| 4 | $\gcd(1513, 105)$ |
| 5 | $\gcd(105, 43)$ |
| 6 | $\gcd(43, 19)$ |
| 7 | $\gcd(19, 5)$ |
| 8 | $\gcd(5, 4)$ |
| 9 | $\gcd(4, 1)$ |
| 10 | $\gcd(1, 0) = 1$ |

The same algorithm without recursion:

```cpp
int gcd(int m, int n) {
    int r;
    while (n != 0) {
        r = m % n;
        m = n;
        n = r;
    }
    return m;
}
```

The iterative version is no more efficient than the recursive one on some compilers. The recursive version is **tail recursive** (the recursive call is the last action), so a C++ compiler will optimise it into a loop and remove the recursion.

#### Consecutive integer checking (GCD v2)

A second method starts at $t = \min(m, n)$ and counts down until $t$ divides both numbers:

```cpp
int gcd(int m, int n) {
    int t = min(m,n);
    while (m % t > 0 || n % t > 0) {
        t--;
    }
    return t;
}
```

For $\gcd(60, 42)$ it tries $42, 41, 40, \dots$ until it reaches $6$.

| Method | Work | Notes |
|---|---|---|
| Euclid | Few steps; the remainders shrink quickly (logarithmic in the smaller number) | Works when $n = 0$ |
| Consecutive integer checking | Up to $\min(m,n)$ iterations | Brute force; fails if either input is 0 (division by zero) |

### Course Resources, Tests And Practicals

| Resource | Notes |
|---|---|
| Levitin, *Introduction to the Design and Analysis of Algorithms* (3rd ed.) | Prescribed textbook |
| Dasgupta, Papadimitriou & Vazirani, *Algorithms* | Free; basis of the Berkeley algorithms course |
| Knuth, *The Art of Computer Programming* | The "bible" of algorithms, in four volumes and counting; expensive |

Studying for the test:

- Go through the slides; if a slide is unclear, read the matching Levitin section.
- When slides point to a Levitin section with no further explanation, read and understand that section.
- Content in the slides but not in Levitin **is examinable** unless explicitly stated otherwise.
- References to other sources (e.g. Dasgupta) are optional unless you cannot understand the slide.

Closed practicals are hard but are a chance to improve your programming, and must be your own work:

| Week | Topic | Difficulty |
|---|---|---|
| 1 | Brute force | Easiest, but not trivial |
| 2 | Divide and conquer / recursion | Hard |
| 3 | Dynamic programming | Very hard |
