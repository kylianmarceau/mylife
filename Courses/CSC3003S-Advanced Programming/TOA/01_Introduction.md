---
tags:
  - advanced-programming
---

# Introduction To Algorithms

**Subject**: CSC3003S Advanced Programming — Theory of Algorithms (TOA)  
**Source**: [1 - TOA Introduction.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/TOA/1%20-%20TOA%20Introduction.pdf), Patrick Marais, University of Cape Town, PDF pages 1–25  
**Generated**: 2026-10-02

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Examples and corrections appear beside the relevant concept.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Algorithms And Correctness|Algorithms And Correctness]]
  - [[#Design, Analysis And Problem Domains|Design, Analysis And Problem Domains]]
  - [[#Algorithm Design Strategies|Algorithm Design Strategies]]
  - [[#Fibonacci: Recursion, Tables And Rolling Storage|Fibonacci: Recursion, Tables And Rolling Storage]]
  - [[#Fibonacci By Formula And Numerical Accuracy|Fibonacci By Formula And Numerical Accuracy]]
  - [[#Greatest Common Divisor|Greatest Common Divisor]]
  - [[#Course Resources And Study Expectations|Course Resources And Study Expectations]]

---

## Core Content

### Algorithms And Correctness

#### Definitions

> **Algorithm**: A finite sequence of unambiguous, effective instructions that solves a well-defined problem and produces a correct result for every valid input.

> **Valid input**: Input satisfying the algorithm's stated preconditions.

> **Correctness**: The guarantee that an algorithm returns the required output when its input satisfies those preconditions.

An algorithm describes a method; a program implements it in a language. The same algorithm can have several representations, and the same problem can have several algorithms with different costs.

| Feature | Requirement |
|---|---|
| Finite | Terminates after finitely many steps on every valid input |
| Definite | Every instruction has an unambiguous meaning |
| Input | Clearly specifies the allowed input domain |
| Output | Produces the required result, with a correctness argument |
| Effective | Uses elementary steps that can actually be carried out |

A terminating implementation can still return the wrong result. Correctness requires both a suitable result and termination.

The **halting problem** asks whether a program terminates on a specified input. No algorithm decides this for every possible program and input. This limits what algorithms can compute, rather than how fast they compute it.

![Problem, algorithm, input and output](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/01_Introduction/problem-model.svg)

*An algorithm turns a problem specification into executable steps mapping valid inputs to outputs.*

### Design, Analysis And Problem Domains

#### Definitions

> **Pseudocode**: A language-independent description of an algorithm's instructions.

> **Time efficiency**: The amount of computation needed as a function of input size.

> **Space efficiency**: The memory needed as a function of input size, usually counting additional storage separately from the input.

> **Optimal algorithm**: An algorithm whose cost cannot be improved within the stated problem and computational model.

1. Understand the problem, including inputs, outputs and special cases.
2. Choose the computational model, exact or approximate solving, a design technique and data structures.
3. Specify the algorithm, normally using pseudocode.
4. Prove correctness; revisit the design if the argument fails.
5. Analyse time and space; revisit choices if the cost is unsuitable.
6. Implement the algorithm.

![Algorithm design workflow](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/01_Introduction/design-workflow.svg)

*Correctness and efficiency checks can send the design back to earlier choices.*

Design aims include **simplicity**, **generality** across valid inputs, and optimality. Data structures affect both clarity and cost.

Optimisation is useful when this computation is a bottleneck. A faster method may not justify its development effort for a one-off database merge, a rarely used operation, or a task that can run overnight.

| Domain | Typical tasks |
|---|---|
| Sorting and searching | Order records; find a key |
| String processing | Find a pattern in text |
| Graph problems | Find routes or dependencies |
| Combinatorial problems | Generate permutations or subsets |
| Computational geometry | Closest pair; convex hull |
| Numerical problems | Linear systems; matrix multiplication; random numbers |

Babylonian procedures for factorisation and square roots and Euclid's GCD method are early algorithms. The word algorithm derives from the Latinised name of al-Khwārizmī.

### Algorithm Design Strategies

#### Definitions

> **Design strategy**: A reusable way to organise the solution of a class of problems.

| Strategy | Core idea | Example |
|---|---|---|
| **Brute force** | Follow the definition directly; try candidates | Linear search |
| **Decrease and conquer** | Solve one smaller instance, then extend its answer | Insertion sort |
| **Divide and conquer** | Solve multiple smaller instances, then combine answers | Mergesort |
| **Transform and conquer** | Change the instance, representation or problem | Horner's rule |
| **Space–time tradeoff** | Store extra information to reduce later work | String-matching shift tables |
| **Dynamic programming** | Store answers to overlapping subproblems | Coin-row optimisation |
| **Greedy technique** | Commit to a feasible locally best choice at each step | Prim's algorithm |

The distinction depends on the work performed. Binary search solves only one selected half; mergesort solves both halves. Recursive syntax alone does not determine the strategy.

### Fibonacci: Recursion, Tables And Rolling Storage

#### Definitions

> **Fibonacci sequence**: The sequence whose first two values are zero and one, with each later value the sum of its two predecessors.

> **Overlapping subproblems**: Subproblems whose answers are needed repeatedly in the same computation.

$$
F_0=0,\qquad F_1=1,\qquad F_n=F_{n-1}+F_{n-2}\quad(n\ge2).
$$

The sequence begins $0,1,1,2,3,5,8,13,21,34,55$. Direct recursion follows the definition:

```java
Fibonacci(n):
    if n <= 1: return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)
```

![Full Fibonacci recursion tree for six](../../../diagrams/CSC3003S-Advanced%20Programming/TOA/01_Introduction/fibonacci-tree.svg)

*Computing the sixth Fibonacci number repeatedly recomputes the same smaller values.*

For example, $F_4$ occurs in both branches of the $F_6$ computation. Repeated work leads to exponential time.

A table stores each computed answer:

```java
FibonacciTable(n):
    if n == 0: return 0
    F[0] = 0
    F[1] = 1
    for i = 2 to n:
        F[i] = F[i - 1] + F[i - 2]
    return F[n]
```

Only two preceding values are needed if earlier results need not be retained:

```java
FibonacciRolling(n):
    if n <= 1: return n
    previous = 0
    current = 1
    for i = 2 to n:
        next = previous + current
        previous = current
        current = next
    return current
```

| Method | Time, counting arithmetic operations | Extra storage |
|---|---|---|
| Direct recursion | $\Theta(\varphi^n)$, where $\varphi=(1+\sqrt5)/2$ | $\Theta(n)$ stack depth |
| Table | $\Theta(n)$ | $\Theta(n)$ integer values |
| Rolling values | $\Theta(n)$ | $\Theta(1)$ integer values |

> [!warning] <span style="color:#ffc778">Source code correction</span>
> The rolling-storage loop uses `i < n` in the PDF. It must include the final iteration, `i <= n`. Otherwise it returns the previous Fibonacci value and leaves the result uninitialised for the input two. The pseudocode above also handles zero before allocating a table entry for one.

Fixed-size integers eventually overflow. Arbitrary-precision integers avoid that, but additions become more expensive as values grow; the table reports arithmetic-operation counts, not bit-operation costs.

### Fibonacci By Formula And Numerical Accuracy

#### Definitions

> **Floating-point rounding error**: Error caused by storing and computing with finite-precision approximations to real numbers.

The exact closed form is:

$$
F_n=\frac{\varphi^n-\psi^n}{\sqrt5},\qquad
\varphi=\frac{1+\sqrt5}{2},\quad\psi=\frac{1-\sqrt5}{2}.
$$

The approximate implementation rounds $\varphi^n/\sqrt5$, using the truncated constant $1.6180339887$. It looks like a short constant-sized expression, but numerical accuracy and the cost of exponentiation still matter.

The provided implementation gives $433{,}494{,}436$ for $F_{43}$; the correct result is $433{,}494{,}437$. Small relative errors in a large power can exceed half an integer, so rounding cannot recover the exact answer. The failure point depends on the constant and numerical implementation.

### Greatest Common Divisor

#### Definitions

> **Greatest common divisor (GCD)**: The largest positive integer dividing both given positive integers without remainder.

> **Tail recursion**: Recursion in which the recursive call is the final action of the function.

For example, $\gcd(60,24)=12$. A direct method tests possible common divisors from the smaller input downward:

```java
ConsecutiveIntegerGCD(m, n):
    t = min(m, n)
    while m mod t != 0 or n mod t != 0:
        t = t - 1
    return t
```

Euclid uses a remainder to reduce the problem:

$$
\gcd(m,n)=\gcd(n,m\bmod n),\qquad \gcd(m,0)=m.
$$

A divisor of both original numbers divides the remainder, and a divisor of the second number and remainder divides the first. The common-divisor set is preserved.

```java
Euclid(m, n):
    if n == 0: return m
    return Euclid(n, m mod n)

EuclidIterative(m, n):
    while n != 0:
        remainder = m mod n
        m = n
        n = remainder
    return m
```

The source trace is:

$$
(14142,3131)\to(3131,1618)\to(1618,1513)\to(1513,105)
\to(105,43)\to(43,19)\to(19,5)\to(5,4)\to(4,1)\to(1,0).
$$

Thus the GCD is $1$. Euclid needs $O(\log\min(m,n))$ remainder operations; downward testing can try $\Theta(\min(m,n))$ candidates. Recursive Euclid may use a stack; tail-call optimisation is compiler-dependent and is not guaranteed by C++.

### Course Resources And Study Expectations

The prescribed text is Anany Levitin, *Introduction to the Design and Analysis of Algorithms*, third edition. Additional references are Dasgupta, Papadimitriou and Vazirani's *Algorithms* and Knuth's *The Art of Computer Programming*.

- Material in the lectures is examinable unless explicitly excluded, including material outside Levitin.
- Sections delegated to Levitin must also be understood; these notes expand the named algorithms where needed.
- Closed practicals progress through brute force, recursion/divide and conquer, then dynamic programming.
- Practise implementing and tracing algorithms, and submit your own work.
