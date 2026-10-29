---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "TOA 01 — Introduction To Algorithms"
---

# TOA 01 — Introduction To Algorithms

**Source note:** [Introduction To Algorithms](../../TOA/01_Introduction.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Algorithms And Correctness|Algorithms And Correctness]]
  - [[#Design, Analysis And Problem Domains|Design, Analysis And Problem Domains]]
  - [[#Algorithm Design Strategies|Algorithm Design Strategies]]
  - [[#Fibonacci: Recursion, Tables And Rolling Storage|Fibonacci: Recursion, Tables And Rolling Storage]]
  - [[#Fibonacci By Formula And Numerical Accuracy|Fibonacci By Formula And Numerical Accuracy]]
  - [[#Greatest Common Divisor|Greatest Common Divisor]]
  - [[#Course Resources And Study Expectations|Course Resources And Study Expectations]]
  - [[#Specification And Models|Specification And Models]]
  - [[#Numerical And Implementation Qualifications|Numerical And Implementation Qualifications]]

## Core Content

### Algorithms And Correctness

<!-- qard-id: ap-71c6e70811a265ad2785 -->
> [!qard]- What is an algorithm?
> A finite sequence of unambiguous, effective instructions solving a well-defined problem and producing the required result for every valid input.

<!-- qard-id: ap-4938af920f4e696e9c52 -->
> [!qard]- What does algorithm correctness require?
> Termination and the required output for every input satisfying the preconditions.

<!-- qard-id: ap-5204c92c699aa9edbd3a -->
> [!qard]- What fundamental limit does the halting problem establish?
> No algorithm can decide termination for every possible program and input; this is a limit on computability.

<!-- qard-id: ap-a3ffef8e142db08f30d6 -->
> [!qard]- What do an algorithm's preconditions specify, and how is an algorithm different from a program?
> Preconditions define valid inputs. An algorithm is the underlying method; a program is one language-specific implementation of that method.

### Design, Analysis And Problem Domains

<!-- qard-id: ap-251667fe784787371d2e -->
> [!qard]- What are the main stages of algorithm development?
> Understand the problem; choose model, solving approach, strategy, and data structures; specify the algorithm; prove correctness; analyse time and space; implement it.

<!-- qard-id: ap-a6b7a7d4e90468b1f204 -->
> [!qard]- What do time efficiency, space efficiency and algorithmic optimality measure?
> Computation and memory as functions of input size; optimality means no better cost is possible within the specified problem and computational model.

<!-- qard-id: ap-4799f792f92209d5cc8b -->
> [!qard]- What roles do pseudocode and data structures play in algorithm design?
> Pseudocode expresses the method independently of a language; data structures determine how operations are organised and what they cost. Seek simplicity and generality as well as efficiency.

<!-- qard-id: ap-fa653ef5cbe5c0dae89c -->
> [!qard]- Which major problem domains does the introduction identify?
> Sorting/searching, strings, graphs, combinatorics, computational geometry and numerical computation—for example ordering records, matching text, routing, enumerating subsets, finding hulls and solving linear systems.

<!-- qard-id: ap-8bb7369ecd20e557a5ef -->
> [!qard]- When is an algorithmic optimisation worth its development effort?
> When the operation is a significant bottleneck or repeated enough that the saved work matters; rarely used or already acceptable computations may not justify extra complexity.

### Algorithm Design Strategies

<!-- qard-id: ap-3b69951f28e73dd1c5aa -->
> [!qard]- Why is binary search decrease and conquer while mergesort is divide and conquer?
> Binary search solves only one selected half; mergesort solves both halves and combines their results.

<!-- qard-id: ap-b1a38f6598b7d2ab8e19 -->
> [!qard]- How do the seven design strategies differ at a glance?
> Brute force follows the definition; decrease solves one smaller instance; divide solves multiple instances; transform changes the problem/representation; space–time stores helpful information; DP caches overlapping states; greedy commits to local choices.

### Fibonacci: Recursion, Tables And Rolling Storage

<!-- qard-id: ap-cee1dbc40ea3940c2ac2 -->
> [!qard]- Why is direct recursive Fibonacci inefficient?
> The two branches repeatedly recompute many of the same smaller Fibonacci values.

<!-- qard-id: ap-ede3ab872961d0617dae -->
> [!qard]- What are the time and auxiliary-space costs of direct recursive Fibonacci?
> $\Theta(\varphi^n)$ arithmetic-operation time, where $\varphi=(1+\sqrt5)/2$, and $\Theta(n)$ recursion-stack depth.

<!-- qard-id: ap-c78115bea8f347cbeb31 -->
> [!qard]- How does table-based Fibonacci avoid repeated work, and at what cost?
> Store $F_0=0,F_1=1$, then compute each later value once from the preceding two. This takes $\Theta(n)$ arithmetic operations and $\Theta(n)$ stored values.

<!-- qard-id: ap-e44ac65b7a66d0d844da -->
> [!qard]- How does rolling-storage Fibonacci reduce memory?
> Retain only the previous and current values; compute the next value, then advance both stored values.

<!-- qard-id: ap-0b4d04232e51e257e14f -->
> [!qard]- What are the time and storage costs of rolling Fibonacci?
> $\Theta(n)$ arithmetic operations and $\Theta(1)$ stored integer values.

<!-- qard-id: ap-be1afbb34ab1ee1c48b3 -->
> [!qard]- What recurrence and boundary cases define Fibonacci, and what loop endpoint is needed?
> $F_0=0,F_1=1,F_n=F_{n-1}+F_{n-2}$. An iterative computation must include $i=n$ and handle $n=0,1$ before assuming both table entries exist.

<!-- qard-id: ap-ebfa2b58b590151e573c -->
> [!qard]- Why distinguish Fibonacci arithmetic-operation counts from bit costs and overflow?
> The integers grow with $n$: fixed-width values eventually overflow, while arbitrary-precision addition costs grow with the number of bits. Constant many stored integers is not constant many bits.

### Fibonacci By Formula And Numerical Accuracy

<!-- qard-id: ap-3af82176b93ceb4fd5c2 -->
> [!qard]- Why does a short closed-form expression not guarantee constant cost and exact output?
> Exponentiation has a cost, and finite precision can make the result inaccurate.

<!-- qard-id: ap-1fe4d832cd61205b22e3 -->
> [!qard]- What is Fibonacci's exact closed form, and why can floating-point rounding fail?
> $F_n=(\varphi^n-\psi^n)/\sqrt5$, with $\varphi=(1+\sqrt5)/2,\psi=(1-\sqrt5)/2$. Approximation errors in large powers can exceed half an integer, defeating final rounding.

### Greatest Common Divisor

<!-- qard-id: ap-3ada269828650ac231d3 -->
> [!qard]- What identities underpin Euclid's GCD algorithm?
> $\gcd(m,n)=\gcd(n,m\bmod n)$ and $\gcd(m,0)=m$ for the nonnegative inputs considered.

<!-- qard-id: ap-38f61b6a26c3b32728bd -->
> [!qard]- Why does Euclid's remainder step preserve the GCD?
> A common divisor of $m,n$ divides $m\bmod n$; a common divisor of $n$ and the remainder also divides $m$.

<!-- qard-id: ap-c74bd60599565786416e -->
> [!qard]- What are the steps of iterative Euclid?
> While $n\ne0$, compute the remainder, replace $m$ by $n$ and $n$ by the remainder; return $m$ when $n=0$.

<!-- qard-id: ap-bfb9434fd81131d2d1cc -->
> [!qard]- How does Euclid's operation count compare with downward GCD testing?
> Euclid uses $O(\log\min(m,n))$ remainder operations; downward testing can examine $\Theta(\min(m,n))$ candidates.

<!-- qard-id: ap-79de07d6d011a4bfb5cc -->
> [!qard]- How does consecutive-integer GCD testing work?
> Start at the smaller positive input and decrease the candidate until it divides both numbers. Unlike Euclid, it can inspect a linear number of candidate divisors.

<!-- qard-id: ap-017d1be092cd5dce70f5 -->
> [!qard]- Why is recursive Euclid tail recursive, and what space qualification follows?
> Its recursive result is returned directly, without later work. Constant stack use still depends on tail-call optimisation, which C++ does not guarantee.

### Course Resources And Study Expectations

<!-- qard-id: ap-46a4ba7815c1dd135350 -->
> [!qard]- What practical skills and study scope accompany the TOA algorithms?
> Implement and trace algorithms, analyse correctness and costs, and understand lecture material and delegated textbook sections unless excluded. Practicals progress through brute force, recursion/divide-and-conquer and DP.

### Specification And Models

<!-- qard-id: ap-3267a301bc6c0b446416 -->
> [!qard]- How do finiteness, definiteness and effectiveness differ as algorithm requirements?
> Terminate after finitely many steps; make every instruction unambiguous; and use steps that can actually be carried out. These are separate from producing the correct output.

<!-- qard-id: ap-a7febedd1ede552c4cc4 -->
> [!qard]- Why must an algorithm specify both its allowed inputs and its required output?
> Correctness is a claim over a defined domain; without preconditions and a result specification, “works correctly” is not a precise testable statement.

<!-- qard-id: ap-b44b65556e0d6aee0976 -->
> [!qard]- How does selecting an exact versus approximate answer affect algorithm design?
> It changes the permitted result guarantees and possibly the feasible cost; an approximation must be judged against the declared tolerance/quality requirement rather than silently replacing exact correctness.

<!-- qard-id: ap-554d6566f9e5c666d060 -->
> [!qard]- Why can an algorithm be optimal in one computational model but not another?
> Available operations and their assumed costs define the lower bound; changing representation, allowed information or operation costs can change which methods are possible or best.

<!-- qard-id: ap-ee1e96f6b0395e0efe27 -->
> [!qard]- Why can termination alone not establish total correctness?
> The program may halt with an invalid answer; show both progress/termination and satisfaction of the result specification for every valid input.

### Numerical And Implementation Qualifications

<!-- qard-id: ap-5237eb776ee2be920c09 -->
> [!qard]- Why might a mathematical closed form not be a reliable implementation?
> Finite precision, overflow and the cost of primitive operations can differ from the ideal mathematical expression; justify both the numerical result and the computational model.

<!-- qard-id: ap-ca47bea4fa2ab1f7d8df -->
> [!qard]- How does Euclid's remainder step make progress as well as preserve common divisors?
> With positive second operand, the remainder is nonnegative and smaller than it, so repeated steps eventually reach zero while leaving the GCD unchanged.

<!-- qard-id: ap-104ef831e7157a746ab5 -->
> [!qard]- What is the space difference between a recursive call's arithmetic work and its implementation stack?
> The recurrence may count one remainder operation per call while pending frames add storage; iteration or supported tail-call elimination can change stack use without changing the mathematical method.
