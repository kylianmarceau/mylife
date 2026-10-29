---
tags:
  - advanced-programming
---

# Functional Programming — Introduction

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-1-Introduction.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-1-Introduction.pdf), James Gain, University of Cape Town, PDF pages 1–23  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes for the opening FP lecture: what functional programming is, why it is used, and what it costs.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Course Structure, Evaluation And Readings|Course Structure, Evaluation And Readings]]
  - [[#Haskell|Haskell]]
  - [[#What Is Functional Programming?|What Is Functional Programming?]]
  - [[#Declarative Programming|Declarative Programming]]
  - [[#Side Effects|Side Effects]]
  - [[#Immutable Data|Immutable Data]]
  - [[#Pure Functions And Referential Transparency|Pure Functions And Referential Transparency]]
  - [[#Where Haskell Fits And Typing|Where Haskell Fits And Typing]]
  - [[#Functional Programming Style|Functional Programming Style]]
  - [[#Benefits: Parallelism And Code Clarity|Benefits: Parallelism And Code Clarity]]
  - [[#Costs: Overheads|Costs: Overheads]]
  - [[#Industry Use And Mixing Paradigms|Industry Use And Mixing Paradigms]]
  - [[#Example: The Countdown Problem|Example: The Countdown Problem]]

---

## Core Content

### Course Structure, Evaluation And Readings

The FP section has four parts.

| Part | Lectures | Lecturer | Topics |
|---|---:|---|---|
| Introduction | 2 | James Gain (JG) | The what and why of functional programming |
| Supporting theory | 3 | JG | Lazy evaluation, lambda calculus |
| Haskell | 10 | Cael Marquard (CM) | Core language features and coding examples |
| Other programming paradigms | 5 | JG | LLM-based code generation, logic programming, quantum programming |

| Assessment | CS3 | Honours |
|---|---|---|
| Test | Part of Test 2 | None |
| Closed prac | Mon 19 Oct and Thu 22 Oct | Mon 26 Oct (25%) |
| Exam | 10 November, 50% of a $2\tfrac{1}{2}$-hour paper 1 | 10 November, $1\tfrac{1}{2}$-hour paper (75%) |
| DP requirement | As per notes to students | None |

- **Recommended textbook**: Hutton, G. (2016) *Programming in Haskell* (2nd ed.). Cambridge University Press.
- **Free option**: Lipovaca, M. (2011) *Learn You a Haskell for Great Good!*
- **Additional readings**: released progressively under the Readings tab on Amathuba.

### Haskell

#### Definitions

> **Haskell**: A statically-typed, lazily-evaluated, pure functional programming language.

> **Glasgow Haskell Compiler (GHC)**: The standard Haskell compiler and interactive interpreter.

- Haskell is the language used in this course.
- It is named after **Haskell Curry**, a mathematician and computer scientist known for **combinatory logic**.
- Starting point: `https://www.haskell.org`; platform: `https://www.haskell.org/platform/`; an EclipseFP plugin also exists.

### What Is Functional Programming?

#### Definitions

> **Functional programming**: A form of declarative programming built by composing and applying mathematical functions.

> **Immutable**: Once created, data cannot be modified.

> **Pure**: A function deterministically produces the same output for the same input, with no side effects.

> **First-class functions**: Functions can be passed as parameters, returned as values, and stored.

The three defining features are immutability, purity, and first-class functions.

- Not every functional language obeys all three features.
- Some non-functional languages borrow individual elements.

### Declarative Programming

#### Definitions

> **Declarative programming**: Describing *what* result is wanted rather than *how* to compute it.

> **Imperative programming**: A step-by-step "cookbook" approach that spells out how to compute a result.

| Imperative | Declarative |
|---|---|
| Step-by-step cookbook | Describes the logic; goal-oriented |
| Programmer manages state and control flow | State and control flow are managed by the system |
| Lower level of abstraction | Higher level of abstraction |
| Python, Java | Functional (Haskell) and logic (Prolog) |

Functional and logic programming are both declarative paradigms; imperative programming is not.

### Side Effects

#### Definitions

> **Side effect**: An interaction in which a function accesses or changes something outside its local scope.

Imperative functions can produce side effects by:

- modifying global variables
- mutating function arguments
- performing input/output
- making network requests

**Nondeterminism** follows: you cannot guarantee that a function called with the same inputs always returns the same output. This makes code hard to debug and reason about. Side effects are sometimes necessary, and FP controls them with immutable data and pure functions.

![Impure function with side causes and side effects](../../../diagrams/CSC3003S-Advanced%20Programming/FP/01_Introduction/side-effects.svg)

*An impure function has hidden inputs (side causes) and hidden outputs (side effects) beyond its arguments and return value.*

The side-effecting `incr` below flips a global flag on each call, so the same call returns different results:

```python
even = True
def incr(value):
    global even
    even = not even
    if even:
        return value + 1
    else:
        return value + 2

print(incr(6))   # 8
print(incr(6))   # 7
```

The pure version depends only on its argument:

```pseudo
FUNC incr(INT value): INT
    RETURN value + 1

print(incr(6))   -- 7
print(incr(6))   -- 7
```

### Immutable Data

#### Definitions

> **Immutable data**: Data bound to a name during initialisation that cannot afterwards be changed or overwritten.

| Operation | Example | Allowed? |
|---|---|---|
| Initialising assignment | `A = [1,2,3,4]` | Yes |
| Mutating assignment | `A[0] = 0` | No |

Instead of changing data in place, FP creates new values and data structures attached to new names.

### Pure Functions And Referential Transparency

#### Definitions

> **Pure function**: A function that behaves like a deterministic mathematical function: the same input always yields the same output, and there are no side effects.

> **Referential transparency**: An expression (such as a name or function call) can always be replaced by its evaluated value without changing program behaviour.

Purity is what enables referential transparency. It is hard to enforce in practice:

- Non-deterministic functions such as `time.now()` and `random.rand()` are **opaque** (not referentially transparent).
- Input from, and output to, an external source is opaque.

### Where Haskell Fits And Typing

![Programming language tree](../../../diagrams/CSC3003S-Advanced%20Programming/FP/01_Introduction/language-tree.svg)

*Haskell is a functional, statically typed, lazily evaluated and pure language. Functional and logic languages together form the declarative family.*

#### Definitions

> **Dynamic typing**: Data types are inferred automatically from values and established at run time, e.g. `pie = 3.14`.

> **Static typing**: Data types are declared in code and established at compile time, e.g. `float pie = 3.14`.

| | Dynamic | Static |
|---|---|---|
| When types are fixed | Run time | Compile time |
| Advantages | Faster to code, greater flexibility | Fewer bugs, better compiler optimisation |
| Disadvantages | Possible run-time errors, potential performance cost | Slower to code, more verbose |
| Functional examples | Lisp, Scheme | Haskell (lazy, pure), SML (eager, impure) |

Haskell infers types too, but it is still statically typed: the types are checked at compile time.

### Functional Programming Style

| Imperative habit | Functional replacement |
|---|---|
| Mutating assignment | Create new allocations |
| Loops | Function recursion (can cause memory issues on both heap and stack) |
| Step-by-step control flow | Data-flow: compose simple functions and pipe data through them |

```haskell
-- Apply the square function to a list using map
square :: Int -> Int
square x = x * x

map square [1, 2, 3, 4]   -- Result: [1, 4, 9, 16]
```

### Benefits: Parallelism And Code Clarity

Most imperative languages predate multi-core hardware: C++ (1983), Python (1991), Java (1995).

- They handle parallelism with threads that share state, controlled by locks, semaphores and atomics.
- Proving such code correct when side effects are present is very hard.

FP sidesteps the "writing while reading" problem:

- **Immutability**: data cannot be written once created.
- **Purity**: there are no side effects.
- The result fits **data-stream parallelism** very well.

FP also improves code clarity:

- It abstracts away execution detail: no memory locations, register states or pointer manipulation.
- High-level operations such as `map`, `filter` and `reduce` are native.
- Pure functions can be tested, and proved correct, in isolation. That means more unit testing and less integration testing.
- Once you know the formalism, code is easier to read.

### Costs: Overheads

#### Definitions

> **Computation overhead**: Performance lost because a higher level of abstraction gives less fine control over execution.

> **Memory overhead**: Extra stack and heap use, caused in FP mainly by lazy evaluation and recursion.

![Abstraction versus performance](../../../diagrams/CSC3003S-Advanced%20Programming/FP/01_Introduction/abstraction-performance.svg)

*Moving up from machine code to languages like Haskell raises abstraction and gives up low-level performance control.*

- Functional code can gain from static typing, from reordering operations at compile time, and from lazy evaluation at run time.
- Imperative code still wins overall through low-level optimisation.
- Lazy evaluation and recursion can impose stack and heap costs (see [Lazy Evaluation](02_Lazy_Evaluation.md)).

### Industry Use And Mixing Paradigms

| Industry | Why FP is used |
|---|---|
| FinTech | Type safety, predictable performance |
| Integrated circuit design | Recursion |
| Telecoms and messaging | Concurrency, scalability |
| Natural language processing | Functional syntax |

Imperative languages have added functional constructs: C++ lambda expressions, Python `map`, and Java `util.stream`. This gives only part of the benefit:

- "Sprinkling const dust" does not remove side effects.
- Functional languages are **immutable by default**, so purity needs no extra thought.
- Imperative languages are **mutable by default**, so staying pure needs extreme discipline.
- "A jack of all trades is a master of none."

### Example: The Countdown Problem

#### Definitions

> **Countdown problem**: Given source numbers and the operators $+,-,\times,\div$, build an expression whose value equals a target. Each source number is used at most once, and every value, including intermediate results, must be a positive natural number.

The problem is inspired by the British quiz show *Countdown*. Source numbers are $1,3,7,10,25,50$ and the target is $765$.

- One solution: $(25-10)\times(50+1)=765$.
- There are $780$ solutions; changing the target to $831$ gives $0$ solutions.
- **Brute force** builds a list of lists of all permutations. The search space is large and contains many inadmissible partial results. For example, $[1,3,7,10,25,50]$ with target $765$ has about $33$ million expressions, of which only about $5$ million are valid.

| Version (2.8 GHz Core 2 Duo, 4 GB RAM, GHC 7.10.2) | One solution | All solutions |
|---|---:|---:|
| Brute-force functional | 0.108 s | 12.224 s |
| Optimised functional | 0.014 s | 1.312 s |

The speed-up comes from lazy evaluation and pruning the search space. Hand-tuned imperative code would be faster, but much harder to write, debug and optimise. The course returns to this example once you have Haskell experience.

> [!tip] <span style="color:#5ad4b5">Takeaway</span>
> FP is declarative programming with immutable data and pure, first-class functions. It suits parallelism and high-level problem solving, at a possible cost in memory and performance.
