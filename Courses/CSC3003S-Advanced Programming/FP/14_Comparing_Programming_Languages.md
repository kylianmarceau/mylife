---
tags:
  - advanced-programming
---

# Comparing Programming Languages

**Subject**: CSC3003S Advanced Programming — Functional Programming (FP)  
**Source**: [FP-14-Comparing Programming Languages.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/FP/FP-14-Comparing%20Programming%20Languages.pdf), James Gain, University of Cape Town, PDF pages 1–14  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes placing FP among the other paradigms: procedural, object-oriented (class- and prototype-based), logic programming with Prolog, and multi-paradigm languages.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Purpose|Purpose]]
  - [[#Language Hierarchy|Language Hierarchy]]
  - [[#Imperative: Procedural And Object-Oriented|Imperative: Procedural And Object-Oriented]]
  - [[#Class-Based Versus Prototype-Based OO|Class-Based Versus Prototype-Based OO]]
  - [[#JavaScript: Prototypes And Flaws|JavaScript: Prototypes And Flaws]]
  - [[#Logic Programming|Logic Programming]]
  - [[#Prolog Syntax: Penguins Example|Prolog Syntax: Penguins Example]]
  - [[#Prolog Example: Lineage|Prolog Example: Lineage]]
  - [[#Prolog Solution Mechanism|Prolog Solution Mechanism]]
  - [[#Languages Cross Boundaries|Languages Cross Boundaries]]

---

## Core Content

### Purpose

This lecture steps back to place FP in context:

- Compare programming paradigms: their fundamental concepts, the style that embodies each philosophy (e.g. "Pythonic" code), and their benefits.
- Introduce **domain-specific languages**: Inform7 for interactive fiction ([Interactive Fiction](15_Interactive_Fiction.md)) and Qiskit for quantum programming.

### Language Hierarchy

![Language hierarchy](../../../diagrams/CSC3003S-Advanced%20Programming/FP/14_Comparing_Programming_Languages/language-hierarchy.svg)

*Programming languages split into imperative, declarative and other (domain-specific) branches. Haskell is declarative, functional, statically typed, lazy and pure.*

| Branch | Sub-branch | Examples |
|---|---|---|
| Imperative | Procedural | C, Pascal, Fortran |
| Imperative | OO, class-based | Java, Python, C++ |
| Imperative | OO, prototype-based | JavaScript |
| Declarative | Logic | Prolog |
| Declarative | Functional, dynamically typed | Lisp, Scheme |
| Declarative | Functional, statically typed, lazy/pure | Haskell |
| Declarative | Functional, statically typed, eager/impure | SML |
| Other | Domain-specific | Inform7, Qiskit (and "vibe coding") |

### Imperative: Procedural And Object-Oriented

#### Definitions

> **Procedural programming**: An early approach that organises code sequentially around procedures (functions).

> **Object-oriented programming (OOP)**: Data and functionality encapsulated together in objects.

| | Procedural | Object-oriented |
|---|---|---|
| Organisation | Sequential procedures | Objects bundling data and behaviour |
| Benefits | Abstraction, simplicity, performance | Code reuse (inheritance, polymorphism), modularity, security (encapsulation), abstraction |
| Versus FP | Allows mutability, explicit looping, tracks state change | Mutable object state |

### Class-Based Versus Prototype-Based OO

#### Definitions

> **Class-based OO**: A class is a static blueprint specified at compile time and instantiated as objects with specific data. Subclasses inherit from a superclass.

> **Prototype-based OO**: Objects are cloned and extended dynamically, potentially at run time, from template objects, with no concept of a class. Objects link to a **prototype chain** through **delegation**. This is not the same as C++ templates.

| | Class-based | Prototype-based |
|---|---|---|
| Template | Static class, fixed at compile time | Another object, changeable at run time |
| Reuse mechanism | Inheritance from a superclass | Delegation along the prototype chain |
| Examples | Java, Python, C++ | JavaScript |

### JavaScript: Prototypes And Flaws

- **Prototype**: objects point to a chain of other objects that define behaviour. Calling a property or method walks up the chain to find its definition.
- **Mutable**: objects in the chain can be altered at run time, e.g. `Object.setPrototypeOf(obj, newProto)`, and a new object can be added to the front of the chain.

![JavaScript prototype chain](../../../diagrams/CSC3003S-Advanced%20Programming/FP/14_Comparing_Programming_Languages/prototype-chain.svg)

*`myCat` has `name`; `makeSound()` is found on the Animal prototype and `toString()` on the Object prototype.*

The lecture calls JavaScript "the world's worst programming language":

| Problem | Detail |
|---|---|
| Rushed early development | Created for Netscape Navigator in 10 days, for client-side form validation and basic animation by non-coders |
| Flaws baked in | Kept backwards compatible so legacy scripts still work |
| Web monopoly | Browsers natively executed only HTML, CSS and JavaScript |
| Example | `sort` treats numbers as strings by default, so `10` comes before `2` |

### Logic Programming

#### Definitions

> **Logic programming**: Declarative programming built on formal logic.

> **Fact**: An unconditional statement.

> **Rule**: A logical relationship `head :- body`, where the head is true if the body is true.

> **Query**: A question used to infer answers from the facts and rules.

| Benefit | Meaning |
|---|---|
| Separation of logic and control | You state what is true; the engine decides how to search |
| Reversibility | A definition can often be run "both ways" (e.g. find parents or children) |

Use cases include expert systems, automated theorem proving and natural language processing.

### Prolog Syntax: Penguins Example

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
| `X`, `_Y` | Variables start with a capital letter or underscore |
| `tweety`, `'Tweety'` | Atoms start with a lowercase letter or are in single quotes |
| `,` / `;` | AND / OR |
| `\+` | NOT (negation as failure) |

### Prolog Example: Lineage

```prolog
% --- FACTS ---
male(bart). male(homer). male(herb). male(abraham). male(clancy).
female(lisa). female(maggie). female(marge). female(mona). female(jackie).

% parent(Parent, Child)
parent(marge, bart).
parent(marge, lisa).
% ... etc.

% --- RULES ---
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

% siblings share a parent and are not the same person
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% X is grandmother of Y if X is parent of Z, Z is parent of Y, X female
grandmother(X, Y) :- parent(X, Z), parent(Z, Y), female(X).
```

The facts follow the Simpsons family tree: Abraham and Mona are Homer and Herb's parents; Clancy and Jackie are Marge, Patty and Selma's parents; Bart, Lisa and Maggie are children of Homer and Marge; Ling is Selma's child. The query `?- sibling(bart, Who).` would return `lisa` (and `maggie`).

### Prolog Solution Mechanism

#### Definitions

> **Unification**: Attempting to instantiate variables so that two terms match.

> **Resolution**: Using a unified clause to either complete a proof or produce new subgoals.

> **Backtracking**: On failure, returning to the most recent choice point and trying the next alternative.

Prolog searches the query state space **depth-first**. For each subgoal:

1. Look for the first matching clause.
2. **Unify**, instantiating variables.
3. **Resolve**: reach a proof or generate more subgoals.
4. Explore that subgoal as deeply as possible; on failure, **backtrack** to the previous choice.

![Prolog search for is_penguin(X)](../../../diagrams/CSC3003S-Advanced%20Programming/FP/14_Comparing_Programming_Languages/prolog-search.svg)

*`is_penguin(X)` reduces to `has_feathers(X), can_swim(X)`. Trying `X = tweety` fails at `can_swim`, so Prolog backtracks and succeeds with `X = kowalski`.*

### Languages Cross Boundaries

Many languages pick elements from several paradigms and do not fit one category. **Python** is class-based object-oriented, procedural, and functional (lambda functions).

| Summary point | |
|---|---|
| Broad divide | Imperative versus declarative |
| Spanning the divide | Python, C++ |
| Logic programming | Declarative, built on formal logic; answers queries from facts and rules |
