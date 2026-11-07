---
tags:
  - advanced-programming
---

# Comparing Programming Languages

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)
**Source**: [FP-14-Comparing Programming Languages.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-14-Comparing%20Programming%20Languages.pdf), James Gain, University of Cape Town, pages 1–14
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Places functional programming in context: the language hierarchy, procedural and object-oriented (class-based versus prototype-based) programming, JavaScript's flaws, logic programming in Prolog, and languages that cross paradigm boundaries.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Why Compare Paradigms?|Why Compare Paradigms?]]
  - [[#The Language Hierarchy|The Language Hierarchy]]
  - [[#Imperative Programming: Procedural And Object-Oriented|Imperative Programming: Procedural And Object-Oriented]]
  - [[#Class-Based Versus Prototype-Based OOP|Class-Based Versus Prototype-Based OOP]]
  - [[#JavaScript: Prototypes And Flaws|JavaScript: Prototypes And Flaws]]
  - [[#Logic Programming|Logic Programming]]
  - [[#Prolog Syntax: The Penguin Example|Prolog Syntax: The Penguin Example]]
  - [[#Prolog Example: Lineage|Prolog Example: Lineage]]
  - [[#How Prolog Solves Queries|How Prolog Solves Queries]]
  - [[#Languages Cross Boundaries|Languages Cross Boundaries]]

---

## Core Content

### Why Compare Paradigms?

This lecture steps back to place functional programming in context:

- comparing programming paradigms — their fundamental concepts, and the coding style that embodies each philosophy (e.g. "Pythonic" code);
- their benefits;
- **domain-specific languages**, such as Inform 7 for interactive fiction and Qiskit for quantum programming.

### The Language Hierarchy

![Programming language hierarchy](../../../diagrams/CSC3003S-Advanced%20Programming/FP/14_Comparing_Programming_Languages/language-hierarchy.svg)

*Languages split into imperative and declarative families, each with sub-paradigms; typing discipline cuts across them.*

| Family | Paradigm | Sub-type | Examples |
|---|---|---|---|
| Imperative | Procedural | — | C, Pascal, Fortran |
| Imperative | Object-oriented | Class-based | Java, Python, C++ |
| Imperative | Object-oriented | Prototype-based | JavaScript |
| Declarative | Logic | — | Prolog |
| Declarative | Functional | Lazy / pure | Haskell |
| Declarative | Functional | Eager / impure | SML |
| Declarative | Functional (dynamically typed) | — | Lisp, Scheme |
| Other | Domain-specific | — | Inform 7, Qiskit |
| Other | "Vibe coding" (LLM-generated code) | — | — |

Languages are also divided into dynamically and statically typed.

### Imperative Programming: Procedural And Object-Oriented

#### Definitions

> **Procedural programming**: An early approach that organises code sequentially around procedures (functions).

> **Object-oriented programming (OOP)**: Encapsulates data and functionality together in objects.

| | Procedural | Object-oriented |
|---|---|---|
| Organisation | Sequential procedures | Objects bundling data and behaviour |
| Benefits | Abstraction, simplicity, performance | Code reuse (inheritance, polymorphism), modularity, security (encapsulation), abstraction |
| Versus FP | Allows mutability, explicit loops and tracked state change | Same, plus encapsulated mutable state |

### Class-Based Versus Prototype-Based OOP

#### Definitions

> **Class-based OOP**: A class is a static blueprint, specified at compile time, that is instantiated as objects with specific data. Subclasses inherit from a superclass.

> **Prototype-based OOP**: Objects are cloned and extended dynamically (possibly at run time) from template objects, with no concept of a class. Objects link to a **prototype chain** through **delegation**. (Not the same as C++ templates.)

| | Class-based | Prototype-based |
|---|---|---|
| Template | Class (static blueprint) | Another object (prototype) |
| When fixed | Compile time | Can change at run time |
| Reuse mechanism | Subclass inheritance | Delegation along a prototype chain |
| Examples | Java, Python, C++ | JavaScript |

### JavaScript: Prototypes And Flaws

In JavaScript, objects point to a chain of other objects that define behaviour.

- Accessing a property or method walks **up the chain** until the definition is found.
- The chain is **mutable**: objects in it can be changed at run time (e.g. `Object.setPrototypeOf(obj, newProto)`), and a new object can be added to the front.

![JavaScript prototype chain](../../../diagrams/CSC3003S-Advanced%20Programming/FP/14_Comparing_Programming_Languages/prototype-chain.svg)

*`myCat` has `name`; `makeSound()` is found on `Animal.prototype` and `toString()` on `Object.prototype`.*

**"The world's worst programming language"**:

| Cause | Detail |
|---|---|
| Rushed early development | Created for Netscape Navigator in 10 days, for client-side form validation and simple animations by non-coders |
| Flaws baked in | Kept backwards compatible so legacy web scripts keep working |
| Web monopoly | Browsers natively executed only HTML, CSS and JavaScript |

Example flaw: `sort` treats numbers as strings by default, so `10` sorts before `2` lexicographically.

### Logic Programming

#### Definitions

> **Logic programming**: A form of declarative programming built on formal logic.

> **Fact**: An unconditional statement.

> **Rule**: A logical relationship `head :- body`, where the head is true if the body is true.

> **Query**: A question used to infer answers from the facts and rules.

| Benefit | Meaning |
|---|---|
| Separation of logic and control | You state what is true; the system decides how to search |
| Reversibility | A definition can often be run both ways (e.g. find children of X, or parents of Y) |

Use cases: expert systems, automated theorem proving, natural language processing.

### Prolog Syntax: The Penguin Example

```prolog
% --- FACTS ---
has_feathers(tweety).
has_feathers(kowalski).
can_swim(kowalski).

% --- RULES ---
% An animal is a bird if it has feathers.
is_bird(X) :-
    has_feathers(X).

% An animal is a penguin if it is a bird and can swim.
is_penguin(X) :-
    is_bird(X),
    can_swim(X).

% Birds can usually fly, unless they are a penguin!
can_fly(X) :-
    is_bird(X),
    \+ is_penguin(X).   % "\+" means NOT in Prolog
```

| Syntax | Meaning |
|---|---|
| `:-` | Read as "if" |
| `.` | Terminates every clause |
| Capital letter or `_` first | Variable (`X`) |
| Lowercase first, or in single quotes | Atom (`tweety`) |
| `,` | AND |
| `;` | OR |
| `\+` | NOT |
| `%` | Comment |

### Prolog Example: Lineage

Facts about the Simpsons family:

```prolog
% --- FACTS ---
male(bart). male(homer). male(herb). male(abraham). male(clancy).
female(lisa). female(maggie). female(marge). female(mona). female(jackie).

% Parent relationships: parent(Parent, Child)
parent(marge, bart).
parent(marge, lisa).
% ... etc.
```

Rules:

```prolog
% X is the father of Y if X is the parent of Y and X is male.
father(X, Y) :- parent(X, Y), male(X).

% X is the mother of Y if X is the parent of Y and X is female.
mother(X, Y) :- parent(X, Y), female(X).

% X and Y are siblings if they share a parent and X is not Y.
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% X is the grandmother of Y if X is a parent of Z, Z is a parent of Y, and X is female.
grandmother(X, Y) :- parent(X, Z), parent(Z, Y), female(X).
```

`\=` means "does not unify with". Without `X \= Y`, everyone would be their own sibling.

### How Prolog Solves Queries

#### Definitions

> **Unification**: Attempting to make two terms equal by instantiating variables.

> **Resolution**: Replacing a goal with the body of a matching rule — either proving it or generating more subgoals.

> **Backtracking**: On failure, returning to the most recent choice point and trying the next alternative.

Prolog searches the query's state space **depth-first**, using unification, resolution and backtracking. For each subgoal:

1. Look for the first matching clause.
2. **Unify** to instantiate variables.
3. **Resolve**: this proves the subgoal or produces new subgoals.
4. Explore each subgoal as deeply as possible; on failure, **backtrack** to the previous choice.

Trace for `is_penguin(X)`:

| Step | Goal(s) | Outcome |
|---|---|---|
| 1 | `is_penguin(X)` | Resolve with the rule |
| 2 | `is_bird(X), can_swim(X)` | Resolve `is_bird` |
| 3 | `has_feathers(X), can_swim(X)` | First fact: $X = $ `tweety` |
| 4 | `can_swim(tweety)` | **Fail** — backtrack |
| 5 | `has_feathers(X)` | Next fact: $X = $ `kowalski` |
| 6 | `can_swim(kowalski)` | **Succeed** |
| 7 | — | Answer: `is_penguin(kowalski)` |

![Prolog depth-first search](../../../diagrams/CSC3003S-Advanced%20Programming/FP/14_Comparing_Programming_Languages/prolog-search.svg)

*The search first tries `tweety`, fails on `can_swim`, backtracks to the next `has_feathers` fact and succeeds with `kowalski`.*

### Languages Cross Boundaries

Many languages pick and choose elements from several paradigms and don't fit one category. Python, for example, is:

- class-based object-oriented,
- procedural, and
- functional in parts (lambda functions, `map`).

**Summary**: there is a broad divide between imperative and declarative programming, but some languages (e.g. Python, C++) span it. Logic programming is declarative, built on formal logic, and answers queries using facts and rules.
