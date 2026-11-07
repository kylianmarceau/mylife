---
tags:
  - advanced-programming
---

# Antipatterns

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD12 Antipatterns.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD12%20Antipatterns.pdf), Johan Bontes, University of Cape Town, pages 1–28
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Common counterproductive "solutions", grouped as generic software, object-oriented, programming and methodological antipatterns — each with its problem, the wrong solution, the result and the fix.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What An Antipattern Is|What An Antipattern Is]]
  - [[#Generic Software Antipatterns|Generic Software Antipatterns]]
  - [[#Object-Oriented Antipatterns|Object-Oriented Antipatterns]]
  - [[#Programming Antipatterns|Programming Antipatterns]]
  - [[#Methodological Antipatterns|Methodological Antipatterns]]

---

## Core Content

### What An Antipattern Is

#### Definitions

> **Antipattern** (Andrew Koenig, 1995): A common solution to a problem that is likely to be counterproductive. The name is a pun on the "Gang of Four" design patterns book.

Each antipattern below follows the same shape: a real **problem**, a tempting **wrong solution**, its **result**, and the **fix**.

### Generic Software Antipatterns

#### Abstraction inversion

| | |
|---|---|
| Problem | Users of a construct need its private functions |
| Wrong solution | Users re-implement the private functions in terms of the public interface — which itself uses (other) private functions |
| Result | Lower-level features depend on higher-level ones: the abstraction is "inverted" |
| Fix | Dependencies must form an acyclic graph (ideally a simple one) |

#### Big ball of mud

#### Definitions

> **Big ball of mud** (spaghetti code, rat's nest): A program with no discernible structure.

Dijkstra's "Go To Statement Considered Harmful": `goto` jumps put all code on a single level with no structure. That critique led to **structured programming** and the waterfall model.

| | |
|---|---|
| Problem | How to structure a program? |
| Wrong solution 1 | Just get started and see where the flow takes us |
| Wrong solution 2 | Use a system you don't understand |
| Result | Code understandable only as one complex unit; it can't be decomposed into independent items; hard to understand and untestable |
| Fix | Use design and architecture patterns plus decomposition |

#### Inner-platform effect

| | |
|---|---|
| Problem | Programmers want to make the application customisable |
| Wrong solution | Turn the application into a programming language |
| Result | A complex solution to a perhaps simple problem (an add-in would do); security becomes very hard |
| Fix | Sandbox the inner language — or just don't: it's a security nightmare |
| Examples | Plug-in based software (Firefox), MS Office (macros) |

#### Stovepipe system

#### Definitions

> **Stovepipe system**: A system procured and developed to solve one specific problem, with limited focus and functionality, whose data cannot easily be shared with other systems.

| | |
|---|---|
| Problem | No architecture up front; the app was built to do one thing, then features were added |
| Wrong solution | Reinvent the wheel for this one app; don't use shared functionality from other systems |
| Result | No code reuse; one-off systems are hard to test fully |
| Fix | Use standard components for extra functionality (databases, etc.) |

#### Data races

#### Definitions

> **Data race**: Two threads access the same memory concurrently, at least one writes, and there is no synchronisation.

| | |
|---|---|
| Problem | Task-parallel (multi-threaded) code is hard |
| Wrong solution | Not realising it's hard; not using a known good solution |
| Result | Sequencing problems in Java (data corruption); in C++ additionally **undefined behaviour** (bizarre side effects) |
| Fix | Simplify the threading model; use MPI; use known good components (hard!) |

### Object-Oriented Antipatterns

| Antipattern | Problem | Wrong solution | Result | Fix |
|---|---|---|---|---|
| **Circular dependencies** | The real-world model has a circular dependency, and OOP models the real world | Copy the cycle into the classes | SOLID violations, especially tight coupling | Design patterns, e.g. Observer |
| **Circle–ellipse problem** | Looks like an IS-A relationship, but the invariants differ (a circle can't stretch one axis) | Inheritance | Liskov substitution violated | Never violate Liskov. Bad: weaken the restrictions. Better: use a **mixin**, not inheritance. Some languages allow partial inheritance (e.g. Lisp) |
| **God object** | Communication between objects is complex | Put everything in one class so communication is "easy" | The OOP equivalent of spaghetti code; classes hard to debug | Create a proper hierarchy; use patterns to keep communication simple |
| **Sequential (temporal) coupling** | Some steps must happen in order (e.g. initialisation) | `init()` or numbered methods the caller must call in order | Code misbehaves if earlier steps didn't happen first | Automatically call `init`/step 1 when step 2 needs it; use the **Template Method** pattern |
| **Call super** | The superclass method has part of the needed code and the subclass the rest, but calling `super` is optional | Write "call super needed" in a comment | Code breaks when someone forgets | **Template Method** pattern; Lisp has `before`/`after`/`around` methods |
| **Object orgy** (unrestricted access) | Access to private members is needed | Make everything public | Encapsulation broken, no information hiding, huge public interfaces (violates the I in SOLID) | Design the interface properly; break the API if needed |

See [SOLID](13_SOLID.md) and [Design Patterns I](14_15_Design_Patterns_I.md) for the principles and patterns behind these fixes.

### Programming Antipatterns

#### Cargo cult programming

| | |
|---|---|
| Problem | Paradigms or patterns used without understanding |
| Wrong solution | More patterns |
| Result | Code that doesn't make sense and is hard to understand |
| Fix | Take this course (CSC3003S); add an experienced programmer; pair programming; code review |

#### Coding by exception

| | |
|---|---|
| Problem | Program flow is awkward |
| Wrong solution | Throw an exception to jump into a section of **non-exceptional** code — equivalent to a `goto` |
| Result | Poor performance; hard-to-understand code; errors accidentally hidden by handled exceptions |
| Fix | Read "Goto Considered Harmful"; use a nested function or `case` statement, redesign the logic — or even an honest `goto` |

#### Repeated code

Violates **DRY** (don't repeat yourself).

#### Shotgun surgery

| | |
|---|---|
| Problem | A small change is needed in many places |
| Wrong solution | Make lots of quick-and-dirty changes all over |
| Result | Unit tests and docs out of date; non-DRY code |
| Fix | Aspect-oriented programming (see [AOP](18_Aspect_Oriented_Programming.md)); refactor or rewrite |

#### Error hiding

| | |
|---|---|
| Problem | Exceptions break your code |
| Wrong solution | Silently swallow the exception |
| Result | Bugs persist but become undetectable |
| Fix | Find and fix the source of the error. Only handle exceptions that are well understood or due to outside factors |

### Methodological Antipatterns

#### Copy-paste programming

| | |
|---|---|
| Problem | The answer was on Stack Overflow — or worse, elsewhere in the code base — and "dunno why, but it seems to work" |
| Wrong solution | Copy-paste it as is, preferably in many places |
| Result | Non-DRY, undocumented code without unit tests; the pasted code carries hidden assumptions that differ from yours |
| Fix | DRY; make sure you understand your code and the assumptions in the Stack Overflow code |

**Variant** — repetitive tasks, each slightly different:

| | |
|---|---|
| Wrong solution | Copy the code for task 1 many times and tweak each copy |
| Result | Non-DRY, hard-to-read code; poor performance from overusing the L1 code cache |
| Fix | Isolate the basic task in a function; in C++ templates are your friend; design patterns |

#### Vibe coding

Generating code with an LLM without understanding it: "copy-paste programming ×2".

#### Premature optimisation

| | |
|---|---|
| Problem | Code needs to be fast, and it may or may not be |
| Wrong solution | Design overly clever, fast-looking solutions |
| Result | Unneeded complexity in the wrong places |
| Fix | Pick a good algorithm (with the right asymptotic run time); start with straightforward code; profile every iteration and optimise only where needed |

> "We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%." — Donald Knuth

#### Reinventing the (square) wheel

| | |
|---|---|
| Problem | You have a problem nobody else can solve — you're the A-Team |
| Wrong solution | Assume the problem is novel (it likely isn't) and invent a clever, novel solution |
| Result | Wasted time, possibly on a suboptimal solution |
| Fix | Most problems already have solutions: use the standard one, and check its quality |
