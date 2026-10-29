---
tags:
  - advanced-programming
---

# Aspect-Oriented Programming And Design Patterns Recap

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD18 Design patterns + AOP \[Auto-saved\].pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD18%20Design%20patterns%20%2B%20AOP%20%5BAuto-saved%5D.pdf), Johan Bontes, University of Cape Town, PDF pages 1–20  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: why AOP is needed, crosscutting concerns, advice, pointcuts and aspects, how weaving works (reflection), AspectJ, pros and cons, and the full design-patterns recap tables.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Why AOP?|Why AOP?]]
  - [[#Example: Capislack Bank|Example: Capislack Bank]]
  - [[#Crosscutting Concerns|Crosscutting Concerns]]
  - [[#Advice, Pointcut And Aspect|Advice, Pointcut And Aspect]]
  - [[#Pointcut Expressions|Pointcut Expressions]]
  - [[#Kinds Of Advice|Kinds Of Advice]]
  - [[#An Aspect In Code|An Aspect In Code]]
  - [[#How It Works: Reflection And AspectJ|How It Works: Reflection And AspectJ]]
  - [[#Pros And Cons Of AOP|Pros And Cons Of AOP]]
  - [[#Design Patterns Recap: Creational|Design Patterns Recap: Creational]]
  - [[#Design Patterns Recap: Structural|Design Patterns Recap: Structural]]
  - [[#Design Patterns Recap: Behavioural (Non-Lambda)|Design Patterns Recap: Behavioural (Non-Lambda)]]
  - [[#Design Patterns Recap: Behavioural (Lambda For The Win)|Design Patterns Recap: Behavioural (Lambda For The Win)]]

---

## Core Content

### Why AOP?

The Visitor pattern makes adding operations easy, but only if it was designed in ([Clean Code And The Visitor](17_Clean_Code_And_Visitor.md)). Design patterns must go in **at the start**. But what if you have an existing app that:

- was not designed with the right patterns
- "just grew", organically-ish, sort of

### Example: Capislack Bank

A banking app has grown organically over 40 years and now needs security added.

- Its classes are `Loans` (`AddLoan(client_id)`), `Insurances` (`AddInsurance(client_id)`), `Customers` (`AddCustomer(client_name)`) and `Buildings`.
- Adding features means adding operations, and adding operations to an existing OOP app is hard: "If only we could add the visitor pattern somehow."

### Crosscutting Concerns

#### Definitions

> **Crosscutting concern**: A requirement that cuts across many different classes and parts of the application: different classes need the same **intervention**, and scattered methods have the same **requirements**.

Examples from the bank:

- new transactions only with approved clients
- new clients only if their IDs are proper and they are not banned

![Crosscutting security aspect](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/18_Aspect_Oriented_Programming/crosscutting.svg)

*One security check must apply to `AddLoan` and `AddInsurance` in different classes. An aspect injects it into every matching method.*

### Advice, Pointcut And Aspect

#### Definitions

> **Advice**: A piece of code injected into one or more methods of your application.

> **Pointcut**: The location(s) the advice is injected into: before a method starts, after it ends, or around it.

> **Aspect**: Advice + pointcut.

### Pointcut Expressions

Pointcuts are defined with **regular expressions** matching class name plus function signature.

| Pointcut | Matches |
|---|---|
| `[A-Z]*s.Add*(client_id, *)` | A class starting with a capital and ending in `s`, with a method starting with `Add` whose first parameter is `client_id` |
| `[A-Z]*s.Add*(client_id,*) \| *.New*(*name, *)` | The same, **or** any method starting with `New` whose first parameter ends in `name` |

Matches can be **AND**-ed (must match all) or **OR**-ed (may match any).

### Kinds Of Advice

| Advice | Runs |
|---|---|
| **Before** | Before the method starts |
| **After** | After the method has finished, ignoring exceptions |
| **Around** | One part before, then the method, then a part after |
| **After exception** | Only when an exception happens |
| **After return** | After the method, only if no exception |

![Advice kinds](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/18_Aspect_Oriented_Programming/advice.svg)

*Advice can run before, after, around, after an exception, or after a normal return of each matched method.*

### An Aspect In Code

```java
@Aspect
public class CheckNewTransactions {
    private Security sec;
    public CheckNewTransactions(Security sec) { this.sec = sec; }

    @Before("execution(* [A-Z]*s.Add*(client_id,..))")
    public void beforeMethodExecution(JoinPoint joinPoint) {
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

Before every `Add…(client_id, …)` method on any matching class, the client is checked: a customer, not a criminal, not bankrupt. None of the 40-year-old classes are edited.

### How It Works: Reflection And AspectJ

#### Definitions

> **Reflection**: The ability of a process to examine, introspect and modify its own structure and behaviour.

| Kind | When | Mechanism | Also called |
|---|---|---|---|
| **Dynamic reflection** | Run time | Uses RTTI (run-time type information) | Injection |
| **Static reflection** | Compile time | The compiler "searches and replaces" in source code | Instrumentation |

**AspectJ** is Java's AOP framework (since 2001). It instruments source code in an extra compile step using the AspectJ **weaving** compiler.

### Pros And Cons Of AOP

| Pro | Con |
|---|---|
| **Modularity**: easily add crosscutting operations | **Debugging**: methods contain only part of the code; crosscuts can happen at any time |
| **Reusability**: makes DRY code easy (one aspect, many places) | **Complexity**: easy to weave very complex crosscuts, adding an extra dimension to the hierarchy |
| **Maintainability**: easy to patch existing code, even with a sub-optimal design | **Tooling**: the IDE may make crosscuts hard to see |
| **SOLID**: reduces dependencies; separates crosscutting concerns from the main logic | **Portability**: AOP is not portable across languages. Java has the best support; C++ not yet (maybe C++29) |
| **Scalability**: AOP-based crosscuts are lightweight | |
| **Testability**: simpler testing thanks to DRYer code | |

AOP is also the fix for the **shotgun surgery** antipattern ([Antipatterns](12_Antipatterns.md)).

### Design Patterns Recap: Creational

The three categories are **creational** (object-creation workarounds), **structural** (mid-level architecture) and **behavioural** (low-level design).

| Pattern | Does what | Why |
|---|---|---|
| **Factory** | Polymorphic construction of a single object | No virtual constructors |
| **Abstract factory** | Factory for multiple related objects | No virtual constructors |
| **Builder** | Constructs a complex object in parts | Composition |
| **Singleton** | Single globally available instance | Database wrappers, logging |
| **Prototype** | Clones an object (`Object.clone()`) | `a = b` only does a shallow copy |

### Design Patterns Recap: Structural

| Pattern | Does what | Why |
|---|---|---|
| **Adapter** | Connects two mismatching interfaces | Fix a mismatching API |
| **Proxy** | Caches a slow resource or encapsulates a big object | Speed |
| **Flyweight** | **Obsolete** | Use DOD instead |
| **Composite** | Recursive container (tree and/or jagged array) | A complex "list" |
| **Facade** | Simple interface around a complex object | Limit functionality |
| **Bridge** | Prevents combinatorial explosion | $10\times10=100$ (bad) versus $10+10=20$ (good) |
| **Decorator** | Adds new properties | E.g. add colour to shapes |

### Design Patterns Recap: Behavioural (Non-Lambda)

| Pattern | Does what | Why / how |
|---|---|---|
| **Memento** | Undo / snapshot | Avoids full cloning |
| **Iterator** | For-in loop | Magic behind the scenes that makes for-in work |
| **Visitor** | Makes adding behaviour easy | An abstract pattern with 3 variants, plus 1 to avoid |
| ↳ Cyclic visitor | Easy to add behaviour, hard to add objects | Pure OOP solution |
| ↳ Acyclic visitor | Easy to add objects and behaviour, but slow | `dynamic_cast` is slow because it walks up and down the inheritance tree |
| ↳ Variant visitor | Discriminated / tagged-union visitor: easy to add objects and behaviour, fully decoupled | "Variant = proper 1956 OOP done right" |
| ↳ Procedural visitor | **Do not use** | Not maintainable |

### Design Patterns Recap: Behavioural (Lambda For The Win)

| Pattern | Does what | With lambdas |
|---|---|---|
| **Command** | File → Save from menu, button and Ctrl+S | Link a lambda to an action |
| **Strategy** | Change the behaviour of an algorithm (e.g. sort) | A lambda steers the algorithm |
| **State** | Finite state machine | Use a Java enum class instead |
| **Template** | Multi-step algorithm | One lambda per step |
| **Observer** | Subscribe to events | One lambda per subscription; an interface notifies subscribers of changes |
| **Chain of responsibility** | Pipe-and-filter / message passing (MPI, a 1970s OOP paradigm) | One lambda per message handler |
| **Mediator** | Central node of communication | One lambda per communication node; also MPI |

A mediator reduces the number of links from all-pairs to a hub:

$$
\frac{n^2-n}{2}\ \text{links} \;\Longrightarrow\; n+1\ \text{links}
$$
