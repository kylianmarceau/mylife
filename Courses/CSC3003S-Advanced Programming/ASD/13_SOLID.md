---
tags:
  - advanced-programming
---

# SOLID Design Principles

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD13 SOLID.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD13%20SOLID.pdf), Johan Bontes, University of Cape Town, pages 1–45
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> The five SOLID object-oriented design principles — Single responsibility, Open–closed, Liskov substitution, Interface segregation and Dependency inversion — with their classic examples and design by contract.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#SOLID Overview|SOLID Overview]]
  - [[#Single Responsibility Principle|Single Responsibility Principle]]
  - [[#What Counts As A Responsibility|What Counts As A Responsibility]]
  - [[#Open–Closed Principle|Open–Closed Principle]]
  - [[#Ways To Extend Without Modifying|Ways To Extend Without Modifying]]
  - [[#Liskov Substitution Principle|Liskov Substitution Principle]]
  - [[#The Square–Rectangle Violation|The Square–Rectangle Violation]]
  - [[#Design By Contract|Design By Contract]]
  - [[#No God Classes|No God Classes]]
  - [[#Interface Segregation Principle|Interface Segregation Principle]]
  - [[#The Timed Door|The Timed Door]]
  - [[#The ATM Example|The ATM Example]]
  - [[#Dependency Inversion Principle|Dependency Inversion Principle]]
  - [[#Why "Inversion"?|Why "Inversion"?]]

---

## Core Content

### SOLID Overview

| Letter | Principle | One-line summary |
|---|---|---|
| S | Single responsibility | A class has one reason to change |
| O | Open–closed | Open for extension, closed for modification |
| L | Liskov substitution | Subtypes must be usable wherever their base type is |
| I | Interface segregation | No client depends on methods it doesn't use |
| D | Dependency inversion | Depend on abstractions, not details |

### Single Responsibility Principle

#### Definitions

> **Single responsibility principle (SRP)**: A class (or function or module) must do one thing and do it well. "There should never be more than one reason for a class to change." — Robert C. Martin, *The Principles of OOD*, ~1998.

**Violation**: a `Rectangle` class does both drawing (`draw()`) and area calculation (`area()`).

- It entangles the computational geometry application and the graphical application.
- Really, `Rectangle` is a compound object, with a hidden cross-link between the graphics app and geometry, and high fan-out.
- Changes to the drawing code can break the area calculation.

**Fix**: split it. `GeometricRect` provides `area()` for the geometry app; `Rectangle` provides `draw()` for the graphics app and uses `GeometricRect`.

- The hidden cross-link is removed and fan-out is low.
- Changes to drawing code can't affect geometry.

![SRP violation and fix](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/srp.svg)

*Left: one Rectangle with two reasons to change. Right: geometry and drawing in separate classes.*

### What Counts As A Responsibility

#### Definitions

> **Responsibility**: A reason for change. If a class has two reasons to change, it violates SRP.

The pitfall: humans naturally cluster responsibilities into groups. This modem interface looks cohesive:

```java
interface Modem {
    public void dial(String phonenr);
    public void hangup();
    public void send(char c);
    public char receive();
}
```

But it holds two responsibilities that change for different reasons:

| Responsibility | Methods |
|---|---|
| **Connection control** — the lifetime of the connection | `dial`, `hangup` |
| **Data control** — sending and receiving characters | `send`, `receive` |

![Modem responsibilities separated](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/modem.svg)

*Separate `Connection` and `DataChannel` interfaces; one modem implementation can still implement both.*

SRP is really a collation of four older principles:

| Principle | Source |
|---|---|
| Decomposition | Parnas, "On the Criteria to Be Used in Decomposing Systems into Modules", 1972 |
| Separation of concerns | Dijkstra, "On the role of scientific thought", 1974 |
| Coupling and cohesion | Constantine, *Structured Design*, 1975 |

> Gather together the things that change for the same reasons. Separate the things that change for different reasons.

### Open–Closed Principle

#### Definitions

> **Open–closed principle (OCP)**: "Classes, modules, functions should be open for extension, but closed for modification." — Meyer, *Object-Oriented Software Construction*, 1988.

| | Meaning |
|---|---|
| **Open for extension** | A new module can extend the old one |
| **Closed for modification** | No source changes to the old module — no new features in old source code. (Bug fixes are not modification.) |

The workflow: start with the existing code, clean it up (hopefully), then **add** the new feature in new code rather than editing the old.

### Ways To Extend Without Modifying

| Mechanism | Example languages |
|---|---|
| Class inheritance (non-virtual) | C++ (impossible in Java) |
| Interface inheritance (virtual methods) | Java |
| Message handlers | Smalltalk, Objective-C, Windows API |

**Non-virtual class inheritance (C++)**:

```cpp
class Parent {
    void hi() { printf("hi"); }
};
class Child : private Parent {
    void hi() { Parent::hi(); printf("C\n"); }
};  // warning: child method hides parent
```

**Virtual (polymorphic) inheritance**:

```cpp
class Parent { virtual void hi() { ... } };
class Child : private Parent {
    override void hi() { Parent::hi(); printf("Child\n"); }
};  // polymorphic inheritance is an antipattern
```

**Pure interface** — better:

```cpp
class IGreet { virtual void hi() = 0; };   // abstract
class Child : public IGreet {
    override void hi() { printf("hi Child\n"); }
};  // better to use interfaces
```

C++ also has compile-time polymorphism (CRTP, "deducing this" in C++23; mixins in Rust) — out of scope for ASD. Operator or function overloading is **not** OOP polymorphism.

**Message passing** (Windows API, Smalltalk, Objective-C): each message has an ID and a data record; a handler is bound to a message ID. If the handler returns false, the parent's handler is called.

```pascal
const WM_MouseMove := 200;  // message id
record TWMMouseMove;
begin                       // message data
    MsgId: int := WM_MouseMove;
    keys: set of [ctrl, alt, shift, caps, win, menu];
    buttons: set of [bL, bR, bM, b4, b5, b6, b7, b8];
    pos: TPoint;
end;

function TWindow.MouseMove(Msg: TWMMouseMove) message WM_MouseMove: bool;
begin
    result := (bL in Msg.buttons) and (Msg.keys = []);
    if result then begin
        DrawLine(prev, Msg.pos);
        prev := Msg.pos;
    end;
end;  // result = false? call parent's handler

SendMessage(Window1, MouseData);  // WinAPI sends this when the mouse moves
```

(Petzold, *Programming Windows*, 5th ed., 1998.)

### Liskov Substitution Principle

#### Definitions

> **Liskov substitution principle (LSP)** (Barbara Liskov, 1988): "If for each object $o_1$ of type $S$ there is an object $o_2$ of type $T$ such that for all programs $P$ defined in terms of $T$, the behaviour of $P$ is unchanged when $o_1$ is substituted for $o_2$, then $S$ is a subtype of $T$." In short: functions that use references to base classes must be able to use derived objects without knowing it.

**Blatant violation**:

```cpp
// intentionally bad code
void DrawShape(Shape& s) {
    if (typeid(s) == typeid(Rect)) DrawR((Rect&)s);
    else if (typeid(s) == typeid(Circ)) DrawC((Circ&)s);
}
```

- `DrawShape` must know every `Shape` subtype's details.
- It breaks when new types are added (also violating OCP).
- It breaks if RTTI (run-time type information) is disabled.

### The Square–Rectangle Violation

Is a square a rectangle? Mathematically yes — but not behaviourally.

```cpp
struct Rectangle {
    void setWidth(const int w)  { width = w; }
    void setHeight(const int h) { height = h; }
    double getHeight() const { return height; }
    double getWidth()  const { return width; }
private:
    int width, height;
};

struct Square : public Rectangle {
    void setWidth(const int w)  { width = height = w; }
    void setHeight(const int h) { setWidth(h); }
};

void f(Rectangle& r) { r.setWidth(32); }   // breaks if r is a Square
```

Because `setWidth`/`setHeight` aren't virtual, `f` calls `Rectangle::setWidth` on a square and breaks its invariant (width = height).

"Fix" it by making everything virtual — and it still breaks:

```cpp
void g(Rectangle& r) {
    r.setWidth(2);
    r.setHeight(3);
    assert(r.getWidth() * r.getHeight() == 6);  // fails if r is a Square
}
```

`g` relies on Rectangle's behaviour (setting height leaves width alone), which Square doesn't honour.

- Only use virtual inheritance for **pure IS-A relationships**. Outside of UIs, these are rare.
- In Java all methods are virtual by default. You should almost never use inheritance:
  - use **interfaces** instead;
  - use inheritance only if you're sure of an IS-A relationship;
  - use **encapsulation** (composition) for HAS-A relationships.

```java
interface IPart extends IDraw, IMore {}

public class Whole implements IDraw {
    private IPart part;
    public void draw() {
        this.draw_background();
        part.draw();
    }
}
```

### Design By Contract

To honour LSP, methods should declare **pre-conditions** and **post-conditions** (Meyer, 1988). A subtype may weaken pre-conditions and strengthen post-conditions, but never the reverse.

**C++26 contracts**:

```cpp
bool canbe_normal(float3 v) { return v.x * v.y * v.z != 0.0; }

constexpr float3 normalize(float3 v) noexcept
    pre(canbe_normal(v))      // prevents division by 0, hence noexcept
    post(v: is_normal(v))
{
    const auto norm = std::hypot(v.x, v.y, v.z);
    contract_assert(norm != 0.0);
    v.x /= norm; v.y /= norm; v.z /= norm;
    return v;
}

int main() {
    const auto v = normalize({0.3, 0.4, 0.5});  // succeeds
    const auto w = normalize({0, 0, 0});        // fails pre- and post-condition
}
```

Older languages use assertions for the same checks.

**Ariane 5 flight V88 (rocket 501)**: an integer overflow (not a problem in itself) raised an exception, which crashed the guidance system and destroyed the rocket. Check your pre- and post-conditions.

| | Contracts | Errors |
|---|---|---|
| Violation | Cannot be recovered from | Can be accommodated in code with fallback options |
| Tooling | Supported by tools | — |

| Contract part | Checks |
|---|---|
| Pre-condition | Input parameters and the object's starting state |
| Post-condition | Output and the object's end state |
| Invariant ("middle condition") | Assertions in the middle |

Contract assertions catch only a subset of violations and can't prove full correctness: program correctness is **undecidable** (Turing), and language features are not yet comprehensive.

### No God Classes

![God class detection](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/god-class.svg)

*A class is a god class when it directly uses many attributes of other classes AND has very high functional complexity AND low cohesion.*

A god class concentrates many responsibilities, violating SRP (see [Antipatterns](12_Antipatterns.md#Object-Oriented%20Antipatterns)).

### Interface Segregation Principle

#### Definitions

> **Interface segregation principle (ISP)**: Don't use fat interfaces. "Clients should not be forced to depend upon (parts of) interfaces that they do not use."

### The Timed Door

```java
public interface IDoor {
    public void lock();
    public void unlock();
    public boolean isDoorOpen();
}

public interface ITimerClient {
    public void TimeOut();
}

public class Timer {
    public void register(int timeout, TimerClient client);
}
```

How do we make a door that sounds an alarm if left open too long?

**Bad**: `public class Door implements IDoor, ITimerClient;` and `public class TimedDoor extends Door;`. Now every `Door` depends on `ITimerClient`. When `ITimerClient` changes, `Door` must change too, even though plain doors don't use timers. (Java has only single class inheritance.)

**Solution — separate using delegation (Adapter pattern)**:

```java
public class TimerDoor implements IDoor {
    public DTAdaptor dta;
    public void regTimer(int end) {
        Time t = toTime(end);
        dta.register(t);
    }
}
```

`TimedDoor` *is an* `IDoor` and *has an* adapter that *is an* `ITimerClient`; the adapter calls back into the door on `TimeOut`.

![Timed door via adapter](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/timed-door.svg)

*With single inheritance, TimedDoor implements IDoor and delegates timer callbacks to a DoorTimerAdapter.*

Alternatives:

| Approach | Code | Note |
|---|---|---|
| Implement multiple interfaces | `class TimerDoor implements IDoor, ITimerClient { DTAdaptor dta; void register(Time t) { dta.register(t); } }` | You still implement or embed the relevant objects |
| C++ multiple inheritance | `class TimerDoor : public Door, public TimerClient { /* inherits register */ };` | Rarely used because complex, except for abstract classes (= interfaces) |

### The ATM Example

An ATM has deposit, withdrawal and transfer transactions.

- **Bad**: one fat `UI` interface used by every transaction. Each transaction uses parts no other needs.
- **Good**: split it into `DepositUI`, `WithdrawalUI` and `TransferUI`. Each transaction depends only on its own UI interface; internally the UIs can still use the overall UI.

Benefits: transactions decouple into separate modules, and errors in deposit can't lead to accidental withdrawals.

![ATM interface segregation](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/atm-isp.svg)

*Before: every transaction depends on the whole UI. After: each depends only on its own segregated interface.*

### Dependency Inversion Principle

#### Definitions

> **Dependency inversion principle (DIP)**: (A) High-level modules should not depend on low-level modules; both should depend on abstractions. (B) Abstractions should not depend on details; details should depend on abstractions.

```c
// bad code
void Copy() {
    char c;
    while ((c = readKey()) != EOF) {
        print(c);
    }
}
```

Problem: `Copy` can't be reused in other contexts. A bad fix adds a switch:

```c
// bad fix
enum OutputDevice { printer, disk };   // more devices...
void Copy(OutputDevice dev) {
    int c;
    while ((c = ReadKeyboard()) != EOF) {
        if (dev == printer) { WritePrinter(c); }
        else { WriteDisk(c); }
    }
}
```

Every new device means modifying `Copy` (violating OCP).

Solution: make `Copy` depend on reader and writer **abstractions**:

```cpp
interface Reader { char Read(); }
interface Writer { void Write(char c); }

void Copy(const Reader& r, Writer& w) {
    char c;
    while ((c = r.Read()) != EOF) {
        w.Write(c);
    }
}
```

`Copy` now supports any device.

![Dependency inversion for Copy](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/dip-copy.svg)

*Traditional: Copy depends on concrete keyboard and printer code. Inverted: Copy and the concrete devices both depend on Reader and Writer.*

### Why "Inversion"?

| Traditional structured design (1990s) | Dependency inversion |
|---|---|
| High-level modules depend on low-level modules | Both depend on abstractions |
| Abstractions depend on details | Details depend on abstractions |
| High-level modules can't be reused | High-level modules are easy to reuse |

High-level modules contain the logic and policy; low-level changes must not break them, and we want to reuse them. Abstractions hide the low-level details. The dependency arrow now points **up** from details to abstractions — inverted.

> "All problems in computer science can be solved by another layer of indirection." — Butler Lampson
>
> "…except the problem of too many layers of indirection" / "…but that usually will create another problem." — David Wheeler
