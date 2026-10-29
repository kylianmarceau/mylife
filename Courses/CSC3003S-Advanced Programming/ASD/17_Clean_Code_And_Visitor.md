---
tags:
  - advanced-programming
---

# Design Patterns II: Clean Code And The Visitor

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD17-Design Patterns II.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD17-Design%20Patterns%20II.pdf), Johan Bontes, University of Cape Town, PDF pages 1–29  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: clean-coding principles, the behavioural pattern overview and iterator recap, the Visitor pattern compared with `std::variant`/`std::visit` and the acyclic visitor, and a Memento recap.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Clean Coding Principles|Clean Coding Principles]]
  - [[#DRY And OneTask|DRY And OneTask]]
  - [[#Meaningful Names|Meaningful Names]]
  - [[#No Littering And No Magic Constants|No Littering And No Magic Constants]]
  - [[#Const Correctness|Const Correctness]]
  - [[#Behavioural Patterns Recap And Examples|Behavioural Patterns Recap And Examples]]
  - [[#The Visitor Pattern|The Visitor Pattern]]
  - [[#The Visitor's Cyclic Dependency|The Visitor's Cyclic Dependency]]
  - [[#Procedural Alternative|Procedural Alternative]]
  - [[#Modern Alternative: std::variant + std::visit|Modern Alternative: std::variant + std::visit]]
  - [[#Acyclic Visitor|Acyclic Visitor]]
  - [[#Performance And Recap|Performance And Recap]]
  - [[#Memento Recap|Memento Recap]]

---

## Core Content

### Clean Coding Principles

| Principle | Meaning |
|---|---|
| **DRY** | Don't repeat yourself |
| **OneTask** | Do only one thing in a function or class |
| **Meaningful names** | Code is written for humans first |
| **No littering** | No stale comments or commented-out code |
| **No magic constants** | Name every literal |
| **Const correctness** | Mark what may not change |

### DRY And OneTask

#### Definitions

> **DRY (don't repeat yourself)**: Factor shared steps into functions instead of duplicating code.

> **OneTask**: Each function or class does exactly one thing, which is SRP at function level.

```cpp
// repeated blocks X, Y, Z inline          // DRY version
void doThis() { /* X… Y… Z… */ }           void doThis2() { doX(); doY(); doZ(); }
void doThat() { /* X… Y… */ }              void doThat2() { doX(); doY(); }

// one function doing many tasks with 5 params → split, each taking only what it needs
void doThis2(a, b, c) { doX(a, b); doY(b); doZ(c); }
```

### Meaningful Names

Code is written for humans first, computers second.

- **Functions**: verbNoun.
- **Variables**: two or more nouns, including the **unit of measure** (litres, secs, kg).
- **Long scope means a long name.** `for (i …)` used only inside a loop can be short; longer scopes need descriptive names.
- **Limit the lifetime (scope)** of variables.
- **No Hungarian notation** (`szFilename`, `ui32_counter`). Use **strong types** instead.
- **Consistent names**: `begin`/`end`, `isDone`, …

### No Littering And No Magic Constants

**No littering.** Code is always up to date; comments are not.

- Put more description into code and less into comments.
- Remove commented-out code; the version control system (git) keeps history.
- Comments explain **why**; the code explains **how and what**.

**No magic constants.** A magic constant is a naked number or string in code:

```cpp
a += 100;                        // why 100, not 101? what is 100?
if ('zorg' == name) { ... }      // hidden backdoor?

const int LevelOffset = 100;     // levels are 100 units apart
const auto superuser = 'zorg';   // definitely a backdoor
```

Naming constants:

- makes the intention clear
- defines each constant in one place (DRY), so it is easy to update
- lets you document it

### Const Correctness

| Language | Mechanism |
|---|---|
| Java | `@ReadOnly`, `final` |
| C++, Rust | `const` |
| Python | Not supported |

- Const correctness allows **pure functions** (no side effects).
- `const`/`final` variables are easy to reason about, keep their initial value, simplify debugging, and let the compiler fold extra variables away.

### Behavioural Patterns Recap And Examples

The behavioural patterns are Chain of responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template and Visitor; see [Design Patterns I](14_15_Design_Patterns_I.md). Iterator is recapped there: modern for-in loops replace the OOP workaround.

The deck links to runnable Compiler Explorer (godbolt) examples for Builder, Adapter, Decorator, Iterator, Visitor, State, Chain of responsibility, Strategy and Observer.

### The Visitor Pattern

#### Definitions

> **Visitor (GoF)**: Adds operations to a type hierarchy by putting each operation in its own visitor class. Each type implements `accept(visitor)`, which calls back `visitor.visit(this)` (double dispatch).

In OOP it is **easy to add types** (just add a class) but **hard to add operations**. Operations are a second dimension, and a class hierarchy is one-dimensional.

![GoF visitor](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/17_Clean_Code_And_Visitor/gof-visitor.svg)

*Operations (Rotate, Draw) form a ShapeVisitor hierarchy and types (Circle, Square) form a Shape hierarchy. Each refers to the other.*

| Pros | Cons |
|---|---|
| Operations are easy to add (**OCP**): new operations without modifying existing code | Hard to add new types (shapes): every visitor must change |
| Hides the implementation details of operations (**SRP**: the changing aspect is extracted) | Operations are limited to the types' public interface |
| | Requires a base class (tending to a god object) |
| | Needs heap allocation and memory management |
| | Requires virtual functions (extra indirection) |
| | **Has a cyclic dependency!** |

### The Visitor's Cyclic Dependency

- `Shape` declares `accept(ShapeVisitor&)`, so it depends on `ShapeVisitor`.
- `ShapeVisitor` declares `visit(const Circle&)` and `visit(const Square&)`, so it depends on every concrete shape.
- Concrete shapes depend on `Shape`.

So the high-level, stable side (shapes) and the low-level, volatile side (operations like `Draw`) depend on each other across the architectural boundary. Only part of the dependency is inverted, and adding a shape forces changes throughout.

### Procedural Alternative

A procedural solution switches on a type tag:

- it needs heap-allocated objects
- it relies on a switch statement
- it is impossible to maintain

### Modern Alternative: std::variant + std::visit

#### Definitions

> **`std::variant`**: A C++ type-safe union holding exactly one of a fixed set of types.

> **`std::visit`**: Calls the overload of a callable that matches the variant's current type: static (compile-time) polymorphism.

```cpp
struct Circle { /* … */ };
struct Square { /* … */ };
using Shape = std::variant<Circle, Square>;

struct Draw {
  void operator()(const Circle& c) const { /* … */ }
  void operator()(const Square& s) const { /* … */ }
};

std::visit(Draw{}, shape);
```

![std::variant + std::visit](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/17_Clean_Code_And_Visitor/variant-visit.svg)

*Shapes know nothing about operations. The variant alias and the operations depend downward only, an automatic inversion of dependencies with no cycle.*

| Pros | Cons |
|---|---|
| Operations easy to add (**OCP**) | Mixing big and small types carries large overhead (fix with the **proxy** pattern) |
| Hides operation details (**SRP**) | `std::variant` is bad at hiding implementation details (information hiding) |
| Types easy to add | |
| Operations can use all type details | |
| No manual heap allocation (automatic destruction) | |
| No virtual functions; static polymorphism, easier to optimise | |
| No cyclic dependency | |
| Faster than the OOP visitor | |

### Acyclic Visitor

#### Definitions

> **Acyclic visitor**: Breaks the cycle with an empty `AbstractVisitor` base plus a templated `Visitor<T>` interface per type. Each shape's `accept` does a `dynamic_cast` to the right `Visitor<T>`.

```cpp
class AbstractVisitor { public: virtual ~AbstractVisitor() = default; };

template <typename T>
class Visitor { public: virtual void visit(const T&) const = 0; };

class Circle : public Shape {
  void accept(const AbstractVisitor& v) const override {
    if (auto cv = dynamic_cast<const Visitor<Circle>*>(&v)) cv->visit(*this);
  }
};

class Draw : public AbstractVisitor, public Visitor<Circle>, public Visitor<Square> {
  void visit(const Circle&) const override;
  void visit(const Square&) const override;
};
```

`Shape` now depends only on the empty `AbstractVisitor`. Operations opt in to the types they handle, so types are also easy to add. **Drawback: very slow**, because of the `dynamic_cast`.

### Performance And Recap

![Visitor performance](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/17_Clean_Code_And_Visitor/visitor-performance.svg)

*The classic visitor is slowest. `std::variant` is close to the enum solution, and `mpark::variant` is fastest, especially with Clang. Values are approximate, read from the source chart.*

| Approach | When to use |
|---|---|
| **Visitor** | Good for adding operations; bad for adding types |
| **std::variant + std::visit** | **Preferred in most scenarios** |
| **Acyclic visitor** | Also good for adding types, but slow. Use it when overhead is not an issue. In Java you have no choice. |

### Memento Recap

The deck repeats the Memento pattern: the originator creates its own immutable snapshot, the memento adds metadata, and the caretaker stores snapshots for undo, transactions and save-to-file. Its cost is RAM use and the need for immutable objects. The full treatment is in [Design Patterns I](14_15_Design_Patterns_I.md).
