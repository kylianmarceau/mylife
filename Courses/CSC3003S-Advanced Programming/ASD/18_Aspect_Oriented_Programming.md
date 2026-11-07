---
tags:
  - advanced-programming
---

# Aspect-Oriented Programming And Design Patterns Recap

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD18 Design patterns + AOP [Auto-saved].pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD18%20Design%20patterns%20%2B%20AOP%20%5BAuto-saved%5D.pdf), Johan Bontes, University of Cape Town, pages 1–20
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Why aspect-oriented programming exists, crosscutting concerns, advice, pointcuts and aspects, how weaving works via reflection, AspectJ, AOP's pros and cons, and a summary table of every design pattern covered.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Why AOP?|Why AOP?]]
  - [[#Crosscutting Concerns|Crosscutting Concerns]]
  - [[#Advice, Pointcuts And Aspects|Advice, Pointcuts And Aspects]]
  - [[#Pointcut Expressions|Pointcut Expressions]]
  - [[#Kinds Of Advice|Kinds Of Advice]]
  - [[#An Aspect In Java|An Aspect In Java]]
  - [[#How It Works: Reflection And Weaving|How It Works: Reflection And Weaving]]
  - [[#AOP Pros And Cons|AOP Pros And Cons]]
  - [[#Design Patterns Recap: Creational|Design Patterns Recap: Creational]]
  - [[#Design Patterns Recap: Structural|Design Patterns Recap: Structural]]
  - [[#Design Patterns Recap: Behavioural (Non-Lambda)|Design Patterns Recap: Behavioural (Non-Lambda)]]
  - [[#Design Patterns Recap: Behavioural (Lambda For The Win)|Design Patterns Recap: Behavioural (Lambda For The Win)]]

---

## Core Content

### Why AOP?

Recall the [Visitor pattern](17_Clean_Code_And_Visitor.md#The%20Visitor%20Pattern): it makes it easy to add **operations** to a type hierarchy — but only if you designed it in from the start.

Design patterns need to be put in at the start. But what if you have an existing application that:

- wasn't designed with the right patterns, and
- just grew "organically-ish, sort of"?

**Example — Capislack Bank**: a banking app that grew organically over 40 years now needs security added.

- Adding features means adding new **operations**.
- Adding operations to an existing OOP app is hard.
- If only we could add the visitor pattern somehow… That is what AOP provides.

### Crosscutting Concerns

#### Definitions

> **Crosscutting concern**: A requirement that applies across many unrelated classes and methods — the same intervention needed in different parts of the application.

> **Aspect-oriented programming (AOP)**: A technique for adding crosscutting behaviour to existing code by injecting it at specified locations, without editing each location.

Characteristics:

- Different classes and interfaces need the same intervention.
- Scattered methods have the same requirements.
- The same concerns appear in different parts of the application, cutting across many classes.

Bank examples:

- new transactions only with approved clients;
- new clients only if their IDs are proper and they are not banned.

![Crosscutting security aspect](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/18_Aspect_Oriented_Programming/crosscutting.svg)

*One security check cuts across many classes of the bank app; AOP applies it everywhere from one place.*

Without AOP, this would be **shotgun surgery** (see [Antipatterns](12_Antipatterns.md#Shotgun%20surgery)).

### Advice, Pointcuts And Aspects

#### Definitions

> **Advice**: A piece of code injected into one or more methods of your application.

> **Pointcut**: The location(s) where an advice is injected — before a method starts, after it ends, or around it.

> **Aspect**: Advice + pointcut.

> **Join point**: A specific point in the program (e.g. a method execution) where advice can run; a pointcut selects a set of join points.

### Pointcut Expressions

Pointcuts are defined with a pattern (regular-expression-like) matching class names and function signatures.

| Pointcut | Matches |
|---|---|
| `[A-Z]*s.Add*(client_id, *)` | A class whose name starts with a capital and ends in `s`, with a method starting with `Add` whose first parameter is `client_id` |
| `[A-Z]*s.Add*(client_id,*) \| *.New*(*name, *)` | The same, **or** any method starting with `New` whose first parameter name ends in `name` |

Matches can be **AND**ed (must match all) or **OR**ed (may match any).

### Kinds Of Advice

| Advice | Runs |
|---|---|
| **Before** | Before the method starts |
| **After** | After the method finishes, regardless of exceptions |
| **Around** | Part before, then the method, then part after |
| **After exception** | Only when an exception happens |
| **After return** | After the method, only if no exception |

![Advice kinds](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/18_Aspect_Oriented_Programming/advice.svg)

*Advice can be woven in before, after or around a method, or only on normal return or on exception.*

### An Aspect In Java

```java
@Aspect
public class CheckNewTransactions {
    private Security sec;
    public CheckNewTransactions(Security sec) { this.sec = sec; }

    @Before("execution(* [A-Z]*s.Add*(client_id,..))")   // pointcut
    public void beforeMethodExecution(JoinPoint joinPoint) { // advice
        Object[] args = joinPoint.getArgs();
        if (args[0] instanceof Integer) {
            final var client_id = (int) args[0];
            sec.check(is_customer(client_id));
            sec.check(!is_criminal(client_id));
            sec.check(!is_bankrupt(client_id));
        }
    }
}
```

Before every matching `Add…(client_id, …)` method runs, the client is checked — without touching any of those methods.

### How It Works: Reflection And Weaving

#### Definitions

> **Reflection**: The ability of a process to examine, introspect and modify its own structure and behaviour.

| | Dynamic reflection | Static reflection |
|---|---|---|
| When | At run time | At compile time |
| How | Uses RTTI (run-time type information) | The compiler does "search and replace" on the source code |
| Also called | Injection | Instrumentation |

#### Definitions

> **Weaving**: Inserting aspects into the program at their pointcuts.

**AspectJ** (Java AOP, since 2001) instruments source code with an extra compile step, using the AspectJ **weaving compiler**.

### AOP Pros And Cons

| Pros | Cons |
|---|---|
| **Modularity**: crosscutting operations are easy to add | **Debugging**: class methods contain only part of the code; crosscuts can happen at any time |
| **Code reusability**: makes DRY code easy (one aspect applied in many places) | **Complexity**: easy to weave very complex crosscuts — it adds an extra dimension to your hierarchy |
| **Maintainability**: easy to patch existing code, even with a sub-optimal design | **Tooling**: the IDE may make crosscuts hard to see |
| **SOLID**: reduces dependencies; separates crosscutting concerns from main logic | **Portability**: not portable across languages; Java has the best support, C++ not yet (maybe C++29) |
| **Scalability**: AOP crosscuts are lightweight | |
| **Testability**: simpler testing because the code is DRYer | |

### Design Patterns Recap: Creational

The three categories:

| Category | Role |
|---|---|
| Creational | Object-creation workarounds |
| Structural | Mid-level architecture |
| Behavioural | Low-level design |

| Pattern | Does what? | Why? |
|---|---|---|
| Factory | Polymorphic construction of a single object | No virtual constructors |
| Abstract factory | Factory for multiple related objects | Same — no virtual constructors |
| Builder | Constructs a complex object in parts | Composition |
| Singleton | A single, globally available instance | Database wrappers, logging |
| Prototype | Clone an object (`Object.clone()`) | `a = b` only does a shallow copy |

### Design Patterns Recap: Structural

| Pattern | Does what? | Why? |
|---|---|---|
| Adapter | Connects two mismatching interfaces | Fix a mismatching API |
| Proxy | Caches a slow resource / encapsulates a big object | Speed |
| Flyweight | Obsolete | Use DOD instead |
| Composite | Recursive container (tree and/or jagged array) | A complex "list" |
| Facade | Simple interface around a complex object | Limit functionality |
| Bridge | Prevents combinatorial explosion | $10 \times 10 = 100$ classes (bad) vs $10 + 10 = 20$ (good) |
| Decorator | Adds new properties | e.g. add colour to shapes |

### Design Patterns Recap: Behavioural (Non-Lambda)

| Pattern | Does what? | Why? / notes |
|---|---|---|
| Memento | Undo / snapshot | Avoids full cloning |
| Iterator | `for-in` loop | The magic behind the scenes that makes `for-in` work |
| Visitor | Makes adding behaviour easy | An abstract pattern: 3 variants plus 1 to avoid |
| — Cyclic (classic) visitor | Easy to add behaviour, hard to add objects | The pure OOP solution |
| — Acyclic visitor | Easy to add objects and behaviour, but slow | `dynamic_cast` is slow because it walks up and down the inheritance tree |
| — Variant visitor | Discriminated / tagged-union visitor: easy to add objects and behaviour, fully decoupled | "Variant = proper 1956 OOP done right" |
| — Procedural visitor | Do not use | Not maintainable |

### Design Patterns Recap: Behavioural (Lambda For The Win)

With lambdas, most behavioural patterns reduce to "a lambda per …":

| Pattern | Does what? | Lambda version |
|---|---|---|
| Command | e.g. File → Save via menu, button and Ctrl+S | Link a lambda to an action |
| Strategy | Changes the behaviour of an algorithm (e.g. sort) | A lambda steers the algorithm |
| State | Finite state machine | Use a Java `enum` class instead |
| Template method | Multi-step algorithm | A lambda per step |
| Observer | Subscribe to events; notifies subscribers of changes | A lambda per subscription |
| Chain of responsibility | Pipe-and-filter / message passing (MPI: message passing interface, a 1970s OOP paradigm) | A lambda per message handler |
| Mediator | Central node of communication | A lambda per communication node; also MPI |

The mediator reduces the number of links between $n$ components from all pairs to one link each to the hub:

$$
\frac{n^2 - n}{2} \text{ links} \quad\longrightarrow\quad n + 1 \text{ links}
$$
