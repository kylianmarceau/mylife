---
tags:
  - advanced-programming
---

# Introduction To Functional Programming

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-1-Introduction.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-1-Introduction.pdf), James Gain, University of Cape Town, pages 1–23
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> What functional programming is, its core features (immutability, purity, first-class functions), where Haskell fits, and the benefits and costs of the paradigm.

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

| Part | Lectures | Lecturer | Content |
|---|---|---|---|
| Introduction | 2 | James Gain | What functional programming is and why to use it |
| Supporting theory | 3 | James Gain | Lazy evaluation, lambda calculus |
| Haskell | 10 | Cael Marquard | Core language features and coding examples |
| Other paradigms | 5 | James Gain | LLM-based code generation, logic programming, quantum programming |

| Assessment | CS3 | Honours |
|---|---|---|
| Test | Part of Test 2 | None |
| Closed practical | Mon 19 Oct and Thu 22 Oct | Mon 26 Oct (25%) |
| Exam (10 November) | 50% of a 2½-hour paper; DP requirement as per student notes | 75%, 1½-hour paper; no DP requirement |

Readings:

- Recommended textbook: Hutton, G. (2016), *Programming in Haskell* (2nd ed.), Cambridge University Press.
- Free option: Lipovača, M. (2011), *Learn You a Haskell for Great Good!*
- Additional readings are released progressively on Amathuba.

### Haskell

#### Definitions

> **Haskell**: A statically typed, lazily evaluated, pure functional programming language. It is named after Haskell Curry, a mathematician and computer scientist known for combinatory logic.

> **GHC (Glasgow Haskell Compiler)**: The standard Haskell compiler and interactive interpreter (GHCi).

Starting points: haskell.org, the Haskell Platform, and the EclipseFP plugin.

### What Is Functional Programming?

#### Definitions

> **Functional programming (FP)**: A form of declarative programming that builds programs by composing and applying mathematical functions.

> **First-class functions**: Functions that can be passed as parameters, returned as values and stored, just like any other data.

Core features:

| Feature | Meaning |
|---|---|
| **Immutable** | Once created, data cannot be modified |
| **Pure** | Functions deterministically produce the same output for the same input, without side effects |
| **First-class functions** | Functions are values: passed, returned and stored |

Not every functional language obeys all of these, and some non-functional languages borrow some of them.

### Declarative Programming

#### Definitions

> **Imperative programming**: A step-by-step "cookbook" approach that says **how** to compute a result.

> **Declarative programming**: Describes the logic and goal — **what** to compute — at a higher level of abstraction. State and control flow are managed by the system.

| Family | Style | Example languages |
|---|---|---|
| Imperative | How | Python, Java |
| Functional | What (declarative) | Haskell |
| Logic | What (declarative) | Prolog |

### Side Effects

#### Definitions

> **Side effect**: Any effect of a function beyond returning a value — accessing or changing something outside its local scope.

Imperative programs let functions:

- modify global variables,
- mutate their arguments,
- perform input/output,
- make network requests.

Nondeterminism is the consequence: you can't guarantee that a function called with the same inputs produces the same outputs. This makes programs hard to debug and reason about. Side effects are sometimes necessary, but FP controls them through immutable data and pure functions.

![Function with side causes and side effects](../../../diagrams/CSC3003S-Advanced%20Programming/FP/01_Introduction/side-effects.svg)

*An impure function depends on hidden inputs (side causes) and changes hidden outputs (side effects) beyond its arguments and return value.*

**Example**:

| Imperative (impure) | Functional (pure) |
|---|---|
| `global even = True` | `FUNC incr(INT value): INT` |
| `def incr(value):` | `    RETURN value+1` |
| `    global even` | |
| `    even = not even` | |
| `    if even: return value+1` | |
| `    else: return value+2` | |
| `print(incr(6))` → **8** | `print(incr(6))` → **7** |
| `print(incr(6))` → **7** | `print(incr(6))` → **7** |

The impure `incr` flips a global flag on every call, so the same call returns different answers.

### Immutable Data

#### Definitions

> **Immutable data**: Data bound to a name at initialisation that cannot afterwards be changed or overwritten.

| Statement | Allowed? | Why |
|---|---|---|
| `A = [1,2,3,4]` | ✓ | Initialising assignment |
| `A[0] = 0` | ✗ | Mutating assignment |

Instead of changing values in place, FP creates new values and data structures bound to new names.

### Pure Functions And Referential Transparency

#### Definitions

> **Pure function**: A function that behaves like a deterministic mathematical function: the same input always yields the same output, with no side effects.

> **Referential transparency**: An expression (e.g. a name or function call) can always be replaced by its evaluated value without changing the program's behaviour. Pure functions enable it.

Purity is hard to enforce in practice. These are **opaque** (not referentially transparent):

- Non-deterministic functions such as `time.now()` and `random.rand()`.
- Input from, and output to, an external source.

### Where Haskell Fits And Typing

![Language tree](../../../diagrams/CSC3003S-Advanced%20Programming/FP/01_Introduction/language-tree.svg)

*Haskell is statically typed, functional, lazily evaluated and pure; SML is functional but eager and impure.*

| Branch | Examples |
|---|---|
| Dynamically typed (functional) | Lisp, Scheme |
| Statically typed, imperative | C++, Python, Java (as grouped in the source) |
| Statically typed, logic | Prolog |
| Statically typed, functional, eager / impure | SML |
| Statically typed, functional, lazy / pure | Haskell |

#### Definitions

> **Dynamic typing**: Data types are inferred automatically from values and established at run time, e.g. `pie = 3.14`.

> **Static typing**: Data types are declared in the code and established at compile time, e.g. `float pie = 3.14`.

| | Dynamic typing | Static typing |
|---|---|---|
| When types are fixed | Run time | Compile time |
| Advantages | Faster to code, more flexible | Fewer bugs, better compiler optimisation |
| Disadvantages | Possible run-time errors, potential performance cost | Slower to code, more verbose |

Haskell is statically typed but infers most types, so it avoids much of the verbosity.

### Functional Programming Style

| Imperative habit | Functional replacement |
|---|---|
| Mutating assignment | Create new allocations |
| Loops | Recursion — which can cause memory issues on both heap and stack |
| Step-by-step control flow | **Data-flow** design: compose simple functions and pipe data through them |

```haskell
-- Apply the square function to a list using map
square :: Int -> Int
square x = x * x

-- Result: [1, 4, 9, 16]
map square [1, 2, 3, 4]
```

### Benefits: Parallelism And Code Clarity

**Parallelism**

- Most imperative languages predate the multi-core era: C++ (1983), Python (1991), Java (1995).
- They handle parallelism with threads sharing state controlled by locks, semaphores and atomics. Proving correctness with side effects is a nightmare.
- FP sidesteps "writing while reading": immutable data can't be written after creation, and pure functions have no side effects.
- This is an excellent fit for **data-stream parallelism**.

**Code clarity**

- FP abstracts away execution detail: no worrying about memory locations, register states or pointer manipulation.
- It has native high-level operations such as `map`, `filter` and `reduce`, making code easier to write.
- Pure functions can be tested (and proved correct) in isolation — more unit testing, less integration testing.
- Once you know the formalism, code is easier to read.

### Costs: Overheads

![Abstraction versus performance](../../../diagrams/CSC3003S-Advanced%20Programming/FP/01_Introduction/abstraction-performance.svg)

*Higher abstraction (Haskell above Python above assembler above machine code) gives less fine-grained control over performance.*

| Cost | Explanation |
|---|---|
| Computation | The higher the abstraction, the less fine control. FP can win through static typing, compile-time reordering of operations and lazy evaluation, but imperative code wins overall through low-level optimisation. |
| Memory | Lazy evaluation and recursion impose stack and heap costs (see [Lazy Evaluation](02_Lazy_Evaluation.md)). |

### Industry Use And Mixing Paradigms

| Industry | Why FP is used |
|---|---|
| FinTech | Type safety, predictable performance |
| Integrated circuit design | Recursion |
| Telecoms and messaging | Concurrency, scalability |
| Natural language processing | Functional syntax |

**Best of both worlds?** C++ (lambda expressions), Python (`map`) and Java (`util.stream`) all add functional constructs to imperative languages. But:

- "Sprinkling `const` dust" does not magically remove side effects.
- Functional languages are immutable by default and need no thought.
- Imperative languages are mutable by default and need extreme discipline to stay functional.

A jack of all trades is a master of none.

### Example: The Countdown Problem

Inspired by the British TV quiz show *Countdown*:

- Given source numbers $[1, 3, 7, 10, 25, 50]$ and the operators $+, -, \times, \div$,
- construct an expression whose value is the target 765.
- Each source number may be used at most once.
- All numbers, including intermediate results, must be positive naturals.

One solution is $(25 - 10) \times (50 + 1) = 765$. There are 780 solutions; changing the target to 831 gives 0 solutions.

The brute-force approach builds a list of lists with all possible permutations. The search space is large, with many inadmissible partial results: about 33 million expressions, of which only about 5 million are valid.

Performance (2.8 GHz Core 2 Duo, 4 GB RAM, GHC 7.10.2):

| Version | One solution | All solutions |
|---|---|---|
| Brute-force functional | 0.108 s | 12.224 s |
| Optimised functional | 0.014 s | 1.312 s |

The speed-up comes from lazy evaluation and pruning the search space. A hand-tuned imperative version would be faster, but much harder to code, debug and optimise. This example is revisited once you have Haskell experience.

**Summary**: functional programming is a declarative style with immutable data and pure, first-class functions. It suits parallelism and high-level problem solving, at a potential cost in memory and performance.
