---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 01 — Introduction To Algorithms"
---

# TOA 01 — Introduction To Algorithms

**Source note:** [Introduction To Algorithms](../../TOA/01_Introduction.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Algorithms|Algorithms]]
  - [[#Design Strategies|Design Strategies]]
  - [[#Fibonacci|Fibonacci]]
  - [[#GCD|GCD]]

## Core Content

### Algorithms

<!-- qard-id: ap-7ab263b5824b2ae15d38 -->
> [!qard]- What is an algorithm?
> A sequence of unambiguous instructions for solving a well-defined problem, guaranteed to terminate for valid input.

<!-- qard-id: ap-044bb7ed4dbbc4313010 -->
> [!qard]- What are the five features every algorithm must have?
> Finite, definite, specified input, provably correct output, effective (simple, basic steps).

<!-- qard-id: ap-7727435f0ae553357707 -->
> [!qard]- Can an algorithm decide, for any program and input, whether that program halts?
> No — the halting problem is undecidable, so some well-defined problems have no algorithm.

<!-- qard-id: ap-1aa4e05beccdfec6982b -->
> [!qard]- When is finding the fastest algorithm not worth it?
> When that part isn't the bottleneck, the program runs only a few times, or time isn't an issue (e.g. it can run overnight).

<!-- qard-id: ap-6eb417c4155bfef72146 -->
> [!qard]- What are the three algorithm design principles?
> Simplicity, generality (range of inputs and special cases) and optimality (no algorithm can do better).

### Design Strategies

<!-- qard-id: ap-d6a88d701959ed84e4aa -->
> [!qard]- Name the seven algorithm design strategies covered in TOA.
> Brute force, decrease and conquer, divide and conquer, transform and conquer, space–time trade-off, dynamic programming, greedy.

<!-- qard-id: ap-4e85eee600e17482f380 -->
> [!qard]- How does dynamic programming differ from divide and conquer?
> Divide and conquer splits into distinct subproblems; dynamic programming handles overlapping subproblems and stores their answers.

<!-- qard-id: ap-a5c7364437cc56dd2d71 -->
> [!qard]- What does the greedy strategy do?
> Repeatedly makes the choice that is best right now.

### Fibonacci

<!-- qard-id: ap-5c9ec0e522cd3d6c9ff1 -->
> [!qard]- State the Fibonacci recurrence.
> $F_0=0,\ F_1=1,\ F_n=F_{n-1}+F_{n-2}$ for $n>1$.

<!-- qard-id: ap-9ed84ead1975826d9553 -->
> [!qard]- Why is naive recursive Fibonacci slow?
> It recomputes the same subproblems repeatedly, so the number of calls grows exponentially (about $1.618^n$).

<!-- qard-id: ap-a718c46f445f89b80e5d -->
> [!qard]- What are the time and space costs of iterative table Fibonacci, and of the rolling 3-cell version?
> Both take linear time ($n-1$ additions); the full table uses $\Theta(n)$ space, the rolling version constant space.

<!-- qard-id: ap-a18e46b8528013eef336 -->
> [!qard]- Why is the closed-form formula $F_n=\operatorname{round}(\phi^n/\sqrt5)$ only superficially efficient?
> Computing $\phi^n$ isn't constant time, and floating-point rounding makes it wrong for larger $n$ (Java fails from $F_{43}$).

### GCD

<!-- qard-id: ap-3cccfa1971f2004c19f4 -->
> [!qard]- State Euclid's algorithm.
> $\gcd(m,n)=\gcd(n,\ m \bmod n)$, with $\gcd(m,0)=m$.

<!-- qard-id: ap-e46c839f96ff29dfb2ae -->
> [!qard]- Why is iterative Euclid no faster than the recursive version in C++?
> The recursion is tail recursive, so the compiler turns it into a loop.

<!-- qard-id: ap-3caa4bd5b9fa93e13cb4 -->
> [!qard]- How does consecutive integer checking find the GCD, and what is its weakness?
> Start at $\min(m,n)$ and count down until $t$ divides both; up to $\min(m,n)$ iterations, and it fails if an input is 0.
