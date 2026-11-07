---
tags:
  - advanced-programming
---

# Design Patterns II: Clean Code And The Visitor Pattern

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD17-Design Patterns II.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD17-Design%20Patterns%20II.pdf), Johan Bontes, University of Cape Town, pages 1–29
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Clean-coding principles (DRY, one task, meaningful names, no littering, no magic constants, const correctness), then the Visitor pattern and its alternatives: procedural switch, `std::variant` + `std::visit`, and the acyclic visitor. Iterator and Memento are recapped from [Design Patterns I](14_15_Design_Patterns_I.md).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Clean Coding Principles|Clean Coding Principles]]
  - [[#DRY: Don't Repeat Yourself|DRY: Don't Repeat Yourself]]
  - [[#OneTask: Do One Thing|OneTask: Do One Thing]]
  - [[#Meaningful Names|Meaningful Names]]
  - [[#No Littering|No Littering]]
  - [[#No Magic Constants|No Magic Constants]]
  - [[#Const Correctness|Const Correctness]]
  - [[#Behavioural Patterns Recap And Examples|Behavioural Patterns Recap And Examples]]
  - [[#The Visitor Pattern|The Visitor Pattern]]
  - [[#Visitor Pros And Cons|Visitor Pros And Cons]]
  - [[#Procedural Alternative|Procedural Alternative]]
  - [[#std::variant And std::visit|std::variant And std::visit]]
  - [[#Performance Comparison|Performance Comparison]]
  - [[#The Acyclic Visitor|The Acyclic Visitor]]
  - [[#Visitor Recap|Visitor Recap]]

---

## Core Content

### Clean Coding Principles

| Principle | Meaning |
|---|---|
| **DRY** | Don't repeat yourself |
| **OneTask** | Do only one thing in a function or class |
| **Meaningful names** | Names that tell the reader what things are and do |
| **No littering** | No stale comments or commented-out code |
| **No magic constants** | Name your numbers and strings |
| **Const correctness** | Mark what must not change |

### DRY: Don't Repeat Yourself

If two functions both contain steps X, Y (and Z), extract each step into a function and call it:

```text
void doThis() {          void doThis2() {
    X - - -                  doX();
    Y - - -       →          doY();
    Z - - -                  doZ();
}                        }

void doThat() {          void doThat2() {
    X - - -       →          doX();
    Y - - -                  doY();
}                        }
```

### OneTask: Do One Thing

A function doing X, Y and Z with five parameters becomes a coordinator of three single-purpose functions, each taking only what it needs:

```text
void doThis(a, b, c, d, e) {      void doThis2(a, b, c) {
    X - - -                           doX(a, b);
    Y - - -              →            doY(b);
    Z - - -                           doZ(c);
}                                 }
```

This is the single responsibility principle at function level (see [SOLID](13_SOLID.md)).

### Meaningful Names

Code is written for humans first, computers second.

| Rule | Example |
|---|---|
| Functions are `verbNoun` | `readFile`, `computeTax` |
| Variables are two or more nouns | `fuelLevel`, `retryCount` |
| Include the unit of measure | `fuelLiters`, `timeoutSecs`, `massKg` |
| Long scope → long name; short scope → short name | `for (i …)` only within a loop; more descriptive names for longer scopes |
| Limit the lifetime (scope) of variables | Declare close to use |
| No Hungarian notation | Not `szFilename`, `ui32_counter` — use strong types instead |
| Consistent names | `begin`/`end`, `isDone`, … |

### No Littering

- Code is always up to date; comments are not.
- Put more of the description into the code and less into comments.
- Remove commented-out code — use the version control system (git) instead.
- Use comments to explain **why**; let the code explain **how/what**.

### No Magic Constants

#### Definitions

> **Magic constant**: A naked number or string in code with no explanation.

```c
a += 100;                 // why 100, not 101? what is 100?
if ('zorg' == name) {...} // hidden back door?
```

Name constants instead:

```c
const int LevelOffset = 100;    // levels are 100 units apart
const auto superuser = 'zorg';  // definitely a back door
```

Benefits:

- the intention is clear;
- each constant is defined in one place (DRY), so it's easy to update;
- you can document named constants.

### Const Correctness

| Language | Mechanism |
|---|---|
| Java | `@ReadOnly`, `final` |
| C++, Rust | `const` |
| Python | Not supported |

Benefits:

- Enables **pure functions** with no side effects.
- `const`/`final` variables keep their initial value, so they're easy to reason about and simplify debugging.
- Compiler optimisation can fold away extra variables.

### Behavioural Patterns Recap And Examples

The behavioural patterns (chain of responsibility, command, iterator, mediator, memento, observer, state, strategy, template method, visitor) and the Iterator and Memento details are as in [Design Patterns I](14_15_Design_Patterns_I.md#Iterator).

Code examples for builder, adapter, decorator, iterator, visitor, state, chain of responsibility, strategy and observer are provided as Compiler Explorer (godbolt.org) links in the slides.

### The Visitor Pattern

#### Definitions

> **Visitor**: Adds new operations to a type hierarchy without changing the types. Each operation is a visitor class with one `visit` method per type; each type has an `accept(visitor)` method that calls back `visitor.visit(this)` ("double dispatch").

In OOP it's easy to add **types** (just add a class) but hard to add **operations**: operations are a second dimension, while a class hierarchy is one-dimensional. Visitor turns operations into their own hierarchy.

![GoF visitor](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/17_Clean_Code_And_Visitor/gof-visitor.svg)

*Shapes accept a ShapeVisitor; Rotate and Draw implement a visit method per shape. The visitor names every shape and every shape names the visitor — a cycle.*

1. `Shape` declares `accept(ShapeVisitor v)`.
2. `Circle::accept(v)` calls `v.visit(this)`, selecting `visit(Circle)`.
3. Each operation (`Rotate`, `Draw`) is a `ShapeVisitor` with `visit(Circle)` and `visit(Square)`.
4. A new operation is a new visitor class; a new shape means editing every visitor.

### Visitor Pros And Cons

| Pros | Cons |
|---|---|
| Operations can be added easily (OCP) | Hard to add new types (shapes) |
| Hides operations' implementation details (SRP) | Operations are limited to the types' public interfaces |
| | Requires a base class (risk of a god object) |
| | Needs heap allocation and memory management |
| | Requires virtual functions (extra indirection) |
| | **Has a cyclic dependency** — `ShapeVisitor` depends on every shape, and every shape depends on `ShapeVisitor` |

### Procedural Alternative

A procedural solution — an enum type tag plus a `switch` in each operation:

- needs heap-allocated objects;
- relies on `switch` statements;
- is impossible to maintain (every new type means editing every switch).

### std::variant And std::visit

A modern C++ solution:

```cpp
class Circle { /* ... */ };
class Square { /* ... */ };
using Shape = std::variant<Circle, Square>;

struct Draw {
    void operator()(const Circle&) const { /* ... */ }
    void operator()(const Square&) const { /* ... */ }
};

std::vector<Shape> shapes = { Circle{1.0}, Square{2.0} };
for (const auto& s : shapes) std::visit(Draw{}, s);
```

#### Definitions

> **`std::variant`**: A type-safe sum type (tagged union) holding exactly one of several alternative types, stored by value.

> **`std::visit`**: Calls the overload of a function object matching the type currently held by a variant.

![std::variant and std::visit](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/17_Clean_Code_And_Visitor/variant-visit.svg)

*Shapes and operations are independent; the variant ties them together, so dependencies point one way across the architectural boundary.*

No cycles; easy to add operations **and** types; satisfies OCP and SRP.

| Pros | Cons |
|---|---|
| Operations can be added easily (OCP) | Mixing big and small types carries large overhead (the variant is as big as its largest alternative) — fix with the Proxy pattern |
| Hides operations' implementation details (SRP) | `std::variant` is bad at hiding implementation details (information hiding) |
| Easy to add types | |
| Operations can use all type details | |
| No manual heap allocation (automatic destruction) | |
| No virtual functions; no cyclic dependency | |
| Faster than the OOP visitor; static polymorphism is faster and easier to optimise | |

### Performance Comparison

![Visitor performance](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/17_Clean_Code_And_Visitor/visitor-performance.svg)

*Approximate run times under GCC 11.2 and Clang 12.0.1: the enum and OO solutions and classic visitor are slowest; `std::variant` and `mpark::variant` are fastest.*

### The Acyclic Visitor

#### Definitions

> **Acyclic visitor**: A visitor variant that breaks the dependency cycle by splitting the visitor interface into an empty base `AbstractVisitor` and one small `Visitor<T>` interface per type.

```cpp
class AbstractVisitor {                 // high level
public:
    virtual ~AbstractVisitor() = default;
};

template <typename T>
class Visitor {                         // high level
public:
    virtual ~Visitor() = default;
    virtual void visit(const T&) const = 0;
};

class Shape {                           // high level
public:
    virtual ~Shape() = default;
    virtual void accept(const AbstractVisitor&) = 0;
};

// ---------------- architectural boundary ----------------

class Circle : public Shape { public: Circle(double rad); /* ... */ };
class Square : public Shape { public: Square(double side); /* ... */ };

class Draw : public AbstractVisitor,
             public Visitor<Circle>,
             public Visitor<Square> {
public:
    void visit(const Circle& circle) const override;
    void visit(const Square& square) const override;
};
```

Each shape's `accept` checks (via `dynamic_cast`) whether the visitor implements `Visitor<ItsOwnType>`. All dependencies point from low-level classes up to high-level abstractions, so there is no cycle. **Drawback: it is slow — very slow** (run-time type checks on every visit).

### Visitor Recap

| Approach | Good for | Notes |
|---|---|---|
| Classic visitor | Adding operations | Bad for adding types; cyclic |
| `std::variant` + `std::visit` | Adding operations and types | **Preferred in most scenarios** |
| Acyclic visitor | Also adding types | Slow — use if overhead isn't an issue. In Java you have no choice |
