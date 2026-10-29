---
tags:
  - advanced-programming
---

# Antipatterns

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD12 Antipatterns.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD12%20Antipatterns.pdf), Johan Bontes, University of Cape Town, PDF pages 1–28  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes. Every antipattern is given as **problem → wrong solution → result → fix**, grouped into generic, object-oriented, programming and methodological antipatterns.

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

> **Antipattern** (Andrew Koenig, 1995): A common solution that is likely to be counterproductive. The name is a pun on the Gang of Four *Design Patterns* book.

Each antipattern below has four parts:

- a **problem**
- a tempting **wrong solution**
- the bad **result**
- the **fix**

### Generic Software Antipatterns

#### Definitions

> **Abstraction inversion**: Lower-level features end up depending on higher-level ones.

> **Big ball of mud** (spaghetti code, rat's nest): Code that can only be understood as one complex, undecomposable unit.

> **Inner-platform effect**: Turning an application into its own programming language to make it customisable.

> **Stovepipe system**: A system built for one specific problem, with limited focus and functionality, whose data cannot easily be shared with other systems.

> **Data race**: Concurrent threads access shared data without correct synchronisation.

| Antipattern | Problem | Wrong solution | Result | Fix |
|---|---|---|---|---|
| **Abstraction inversion** | Users of a construct need its private functions | Users re-implement the private functions using the public interface, which itself uses (other) private functions | Lower-level features depend on higher-level ones | Dependencies must form an **acyclic graph**, ideally a simple one |
| **Big ball of mud** | How to structure a program? | (1) Just start and see where the flow goes; (2) use a system you don't understand | Code understood only as one complex unit; can't be decomposed; hard to understand; untestable | Design and architecture patterns plus decomposition |
| **Inner-platform effect** | Programmers want to add customisability | Turn the app into a programming language | A complex solution to a perhaps simple problem (an add-in would do); security becomes very hard | Sandbox the inner language, or just don't (security nightmare). Examples: plug-in software (Firefox), MS Office |
| **Stovepipe system** | No architecture up front; an app built to do one thing accumulates features | Reinvent the wheel for this app only; don't use shared functionality | No code reuse; one-off systems are hard to test fully | Use standard components (DB, etc.) for extra functionality |
| **Data races** | Task-parallel (multi-threaded) code is hard | Not realising how hard it is; not using a known good solution | Sequencing problems and data corruption in Java; in C++, undefined behaviour with bizarre side effects | Simplify the threading model; MPI; known good components (hard!) |

Big ball of mud connects to Dijkstra's "Go To Statement Considered Harmful". Unrestricted `goto` puts all code on one level with no structure, which led to structured programming (and the waterfall model).

### Object-Oriented Antipatterns

#### Definitions

> **God object**: One class that does everything.

> **Sequential (temporal) coupling**: Methods must be called in a particular order (e.g. `init` first) for the code to work.

> **Call super**: A subclass override must remember to call the superclass method for correct behaviour.

> **Object orgy**: Unrestricted access to an object's members, e.g. everything public.

| Antipattern | Problem | Wrong solution | Result | Fix |
|---|---|---|---|---|
| **Circular dependencies** | The real-world model has circular dependencies, and OOP models the real world | Copy the circularity into the classes | SOLID violations, especially tight coupling | Design patterns, e.g. **observer** |
| **Circle–ellipse problem** | Looks like IS-A, but the invariants differ | Inheritance | Liskov substitution violated | Never violate Liskov. Weakening restrictions is bad; **mixins** instead of inheritance are better; some languages (e.g. Lisp) allow partial inheritance |
| **God object** | Communication between objects is complex | Put everything in one class for easy communication | The OOP equivalent of spaghetti code; hard to debug | A proper hierarchy; patterns to keep communication simple |
| **Sequential (temporal) coupling** | Some steps must happen in order (e.g. init) | `init` or numbered methods the caller must call in order | Code misbehaves if earlier steps were skipped | Call init/step 1 automatically from step 2; use the **template method** pattern |
| **Call super** | The superclass method has part of the needed code and the subclass the rest; calling super is optional | Write "call super needed" in a comment | Code breaks if the parent method isn't called | **Template method** pattern; Lisp's `before`/`after`/`around` methods |
| **Unrestricted access (object orgy)** | Access to private members is needed | Make everything public | Broken encapsulation; no information hiding; huge public interfaces (violates the **I** in SOLID) | Properly design the interface; break the API if needed |

In the circle–ellipse problem, a `Circle` IS-A `Ellipse` mathematically. But an ellipse can stretch one axis, and a circle must keep both equal, so a `Circle` cannot substitute for an `Ellipse` everywhere. See [SOLID](13_SOLID.md).

### Programming Antipatterns

#### Definitions

> **Cargo cult programming**: Using paradigms or patterns without understanding them.

> **Coding by exception**: Using exceptions for ordinary control flow.

> **Shotgun surgery**: A small change requires edits in many places.

> **Error hiding**: Silently swallowing exceptions.

| Antipattern | Problem | Wrong solution | Result | Fix |
|---|---|---|---|---|
| **Cargo cult programming** | Paradigms or patterns used without understanding | More patterns | Code doesn't make sense; hard to understand | CSC3003S; add an experienced programmer; pair programming; code review |
| **Coding by exception** | Program flow is awkward | Throw an exception to jump into a section of non-exceptional code, equivalent to a GOTO | Poor performance; hard to understand; errors accidentally hidden by handlers | Read "goto considered harmful"; use a nested function, a case statement, or redesign the logic (perhaps even a GOTO) |
| **Repeated code** | — | — | — | **DRY** (don't repeat yourself) |
| **Shotgun surgery** | Small changes needed in many places | Quick-and-dirty edits all over | Unit tests and docs out of date; non-DRY code | Aspect-oriented programming; refactor or rewrite |
| **Error hiding** | Exceptions break your code | Silently swallow the exception | Bugs persist but are undetectable | Investigate and fix the source; handle only well-understood exceptions or ones caused by outside factors |

### Methodological Antipatterns

#### Definitions

> **Premature optimisation**: Optimising before knowing where performance matters.

> **Reinventing the (square) wheel**: Building your own solution to an already-solved problem, often worse.

| Antipattern | Problem | Wrong solution | Result | Fix |
|---|---|---|---|---|
| **Copy-paste programming** | The answer was on Stack Overflow, or worse, elsewhere in the code base; "dunno why, but it seems to work" | Paste it as is, preferably in many places | Non-DRY, undocumented, untested code; pasted code carries hidden assumptions that differ from yours | DRY; understand your code and the assumptions in the SO code |
| **Copy-paste code (variant tasks)** | Repetitive tasks, each slightly different | Copy task 1's code many times and tweak each copy | Non-DRY and hard to read; poor performance from overusing the L1 code cache | Isolate the basic task in a function; C++ templates; design patterns |
| **Vibe coding** | — | — | "See copy-paste programming × 2" | — |
| **Premature optimisation** | Code must be fast, and may or may not be | Overly clever, fast-looking designs | Unneeded complexity in the wrong places | Pick a good algorithm (right asymptotic run time), start with straightforward code, **profile** each iteration, optimise only where needed |
| **Reinventing the (square) wheel** | "No one else can solve this; we are the A-team" | Assume the problem is novel (it likely isn't) and invent a clever solution | Wasted time, possibly a suboptimal solution | Most problems already have standard solutions; use one, after checking its quality |

> [!quote] Knuth on optimisation
> "We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%."
