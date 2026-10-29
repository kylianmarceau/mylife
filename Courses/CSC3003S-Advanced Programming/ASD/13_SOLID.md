---
tags:
  - advanced-programming
---

# SOLID Design Principles

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD13 SOLID.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD13%20SOLID.pdf), Johan Bontes, University of Cape Town, PDF pages 1–45  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes on the five SOLID principles of object-oriented design, with the source's examples: Rectangle/GUI, Modem, extension mechanisms, Square/Rectangle, design by contract, TimedDoor, ATM and Copy.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#SOLID Overview|SOLID Overview]]
  - [[#S — Single Responsibility Principle|S — Single Responsibility Principle]]
  - [[#What Is A Responsibility?|What Is A Responsibility?]]
  - [[#O — Open–Closed Principle|O — Open–Closed Principle]]
  - [[#Extension Mechanisms|Extension Mechanisms]]
  - [[#L — Liskov Substitution Principle|L — Liskov Substitution Principle]]
  - [[#Square Is Not A Rectangle|Square Is Not A Rectangle]]
  - [[#Prefer Interfaces And Composition|Prefer Interfaces And Composition]]
  - [[#Design By Contract|Design By Contract]]
  - [[#No God Classes|No God Classes]]
  - [[#I — Interface Segregation Principle|I — Interface Segregation Principle]]
  - [[#D — Dependency Inversion Principle|D — Dependency Inversion Principle]]

---

## Core Content

### SOLID Overview

| Letter | Principle | One-line summary |
|---|---|---|
| **S** | Single responsibility | One reason to change |
| **O** | Open–closed | Extend without modifying |
| **L** | Liskov substitution | Subtypes must be usable wherever the base type is |
| **I** | Interface segregation | No fat interfaces |
| **D** | Dependency inversion | Depend on abstractions, not details |

### S — Single Responsibility Principle

#### Definitions

> **Single responsibility principle (SRP)**: A class or function must do one thing and do it well. "There should never be more than one reason for a class [function/module] to change." (R. Martin, ~1998)

**Violation**: `Rectangle` both draws itself and calculates its area.

- It entangles the computational geometry app with the graphical app.
- Changes to the drawing code can break the area calculation.
- Underneath, `Rectangle` is a compound object with a hidden cross-link between the graphics app and the geometric rectangle, giving **high fan-out**.

**Fix**: split it into `GeometricRectangle` (`area()`) and `Rectangle` (`draw()`), with the drawing rectangle using the geometric one.

- The hidden cross-link is removed and fan-out is low.
- Changes to drawing code cannot affect geometry.

![SRP violation and fix](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/srp.svg)

*Left: one Rectangle serves both applications and has two reasons to change. Right: each class has one responsibility.*

SRP collates four older ideas:

| Idea | Origin |
|---|---|
| Decomposition | Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", 1972 |
| Separation of concerns | Dijkstra, "On the role of scientific thought", 1974 |
| Coupling and cohesion | Constantine, *Structured Design*, 1975 |

In short: **gather together things that change for the same reasons; separate things that change for different reasons.**

### What Is A Responsibility?

A responsibility is **a reason for change**. Two reasons to change means an SRP violation. The pitfall is that humans naturally cluster responsibilities into groups:

```java
interface Modem {
    public void dial(String phonenr);
    public void hangup();
    public void send(char c);
    public char receive();
}
```

This looks cohesive, but it holds two responsibilities:

- **Connection control** determines the lifetime of the connection (`dial`, `hangup`).
- **Data control** sends and receives characters (`send`, `recv`).

![Modem responsibilities separated](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/modem.svg)

*Two interfaces, `DataChannel` and `Connection`, are both implemented by `ModemImplementation`, so clients depend only on the responsibility they use.*

### O — Open–Closed Principle

#### Definitions

> **Open–closed principle (OCP)**: "[Classes, modules, functions] should be open for extension, but closed for modification." (Meyer, 1988)

| Usual way | OCP |
|---|---|
| Starting code → changes scattered through it → clean up (hopefully) | Starting code → add a new feature as a new module → implement it there |

- **Open for extension**: a new module can extend the old one.
- **Closed for modification**: no source changes to the old module and no new features in old code. **Bug fixes are not modification.**

### Extension Mechanisms

| Mechanism | Languages | Notes |
|---|---|---|
| Class inheritance (non-virtual) | C++ | Impossible in Java |
| Interface inheritance (virtual methods) | Java, C++ | |
| Message handlers | Smalltalk, Objective-C, Windows API | |

**Non-virtual class inheritance** (C++):

```cpp
class Parent { void hi() { printf("hi"); } };
class Child: private Parent {
  void hi() { Parent::hi(); printf("C\n"); }
};  // warning: child method hides parent
```

**Virtual (polymorphic) inheritance versus pure interfaces**:

```cpp
class Parent { virtual void hi() { ... } };
class Child: private Parent {
  override void hi() { Parent::hi(); printf("Child\n"); }
};  // polymorphic inheritance is an antipattern

class IGreet { virtual void hi() = 0; };   // abstract (pure interface)
class Child: public IGreet {
  override void hi() { printf("hi Child\n"); }
};  // better: use interfaces
```

**Message passing** (WinAPI, Smalltalk, Objective-C; Petzold, *Programming Windows*). A window declares a handler for a message ID. If the handler returns false, the parent's handler is called. New behaviour is added by handling new messages, not by editing old code.

```pascal
const WM_MouseMove := 200;                  // message id
record TWMMouseMove; begin                  // message data
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

C++ compile-time polymorphism (CRTP, mixins in Rust, "deducing this" in C++23) is **out of scope** for ASD. Operator and function overloading is not OOP polymorphism.

### L — Liskov Substitution Principle

#### Definitions

> **Liskov substitution principle (LSP)** (Barbara Liskov, 1988): "If for each object $o_1$ of type $S$ there is an object $o_2$ of type $T$ such that for all programs $P$ defined in terms of $T$, the behaviour of $P$ is unchanged when $o_1$ is substituted for $o_2$, then $S$ is a subtype of $T$."

Martin's rephrasing: "Functions that use references to base classes must be able to use derived objects without knowing it."

**Blatant violation** (intentionally bad code):

```cpp
void DrawShape(Shape& s) {
  if (typeid(s) == typeid(Rect)) DrawR((Rect&)s);
  else if (typeid(s) == typeid(Circ)) DrawC((Circ&)s);
}
```

- `DrawShape` must know every shape's details.
- It breaks when new types are added (also violating OCP).
- It breaks if RTTI is disabled.

### Square Is Not A Rectangle

```cpp
struct Rectangle {
  void setWidth(const int w)  { width = w; }
  void setHeight(const int h) { height = h; }
  double getHeight() const { return height; }
  double getWidth()  const { return width; }
private:
  int width, height;
};

struct Square: public Rectangle {
  void setWidth(const int w)  { width = height = w; }
  void setHeight(const int h) { setWidth(h); }
};

void f(Rectangle& r) { r.setWidth(32); }  // breaks if r is a Square
```

1. Mathematically a square IS-A rectangle, but here `setWidth`/`setHeight` are not virtual. Through a `Rectangle&`, a `Square` uses the rectangle setters and ends up non-square.
2. "Fix: virtual all the things". This still breaks:

```cpp
void g(Rectangle& r) {
  r.setWidth(2);
  r.setHeight(3);
  assert(r.getWidth() * r.getHeight() == 6);  // fails for a Square (gives 9)
}
```

The **behavioural invariants differ**. A rectangle's width and height vary independently, a square's do not, so `Square` cannot substitute for `Rectangle`. This is the circle–ellipse antipattern ([Antipatterns](12_Antipatterns.md)).

> [!warning] <span style="color:#ffc778">Use inheritance only for pure IS-A</span>
> Use virtual inheritance only for pure IS-A relationships, and outside UI code these are rare.

### Prefer Interfaces And Composition

In Java all methods are virtual by default, so **almost never use inheritance**:

- Use **interfaces** instead.
- Use inheritance only when sure of an IS-A relationship.
- Use **encapsulation** (composition) for HAS-A relationships.

```java
interface IPart extends IDraw, IMore;
public class Whole implements IDraw {
    private IPart part;              // HAS-A
    public void draw() {
        this.draw_background();
        part.draw();
    }
}
```

### Design By Contract

#### Definitions

> **Design by contract** (Meyer, 1988): Methods declare **pre-conditions** (inputs and starting state), **post-conditions** (outputs and end state) and **invariants** (assertions in the middle). A subtype must honour its base type's contract, which is how LSP is checked.

C++26 contracts:

```cpp
bool canbe_normal(float3 v) { return v.x * v.y * v.z != 0.0; }
constexpr float3 normalize(float3 v) noexcept
  pre(canbe_normal(v))      // prevents division by 0, hence noexcept
  post(v: is_normal(v)) {
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

Older languages use `assert` for the same checks.

| Contracts | Errors |
|---|---|
| Get tooling support | Can be handled in code |
| Violations cannot be recovered from | Allow fallback options |

- Contract assertions catch only a subset of violations and cannot prove a whole program correct: program correctness is undecidable (Turing), and language support is not yet comprehensive.
- **Ariane 5 flight V88 (rocket 501)**: an integer overflow (not a problem in itself) raised an exception, which crashed the guidance system. Check your pre- and post-conditions.

### No God Classes

![God class detection](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/god-class.svg)

*A class is a god class when it uses many attributes of other classes directly AND has very high functional complexity AND has low cohesion.*

### I — Interface Segregation Principle

#### Definitions

> **Interface segregation principle (ISP)**: "Clients should not be forced to depend upon (parts of) interfaces that they do not use." Don't use fat interfaces.

**TimedDoor example**:

```java
public interface IDoor { void lock(); void unlock(); bool isDoorOpen(); }
public interface ITimerClient { void TimeOut(); }
public class Timer { void register(int timeout, TimerClient client); }
```

A naive design puts `ITimerClient` on the base `Door` (`Door implements IDoor, ITimerClient; TimedDoor extends Door`). Then every door depends on the timer interface, and if `ITimerClient` changes, `Door` must change even though plain doors don't use timers.

**Fix by delegation (Adapter pattern)**, needed when only single inheritance is available:

```java
public class TimerDoor implements IDoor {
  public DTAdaptor dta;
  public void regTimer(int end) {
    Time t = toTime(end);
    dta.register(t);
  }
}
```

![TimedDoor via adapter](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/timed-door.svg)

*`TimedDoor` IS-A `IDoor` and HAS-A `DoorTimerAdapter`, which IS-A `ITimerClient` and forwards time-outs back to the door.*

| Approach | How |
|---|---|
| Delegation / adapter | Implement one interface; embed an adapter for the other |
| Multiple interfaces | `TimerDoor implements IDoor, ITimerClient`; you still implement or embed the timer logic |
| C++ multiple inheritance | `class TimerDoor: public Door, public TimerClient`; rarely used because complex, except for abstract classes (interfaces) |

**ATM example**: deposit, withdrawal and transfer transactions all depend on one big `UI`, each using parts no other transaction needs. Split it into `DepositUI`, `WithdrawalUI` and `TransferUI`. Each transaction uses only its own UI, though the UIs may still be implemented by one overall UI.

- Transactions decouple into separate modules.
- An error in deposit can't cause an accidental withdrawal.

![ATM interface segregation](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/atm-isp.svg)

*Before, every transaction depends on the whole UI. After, each depends on a small interface of its own.*

### D — Dependency Inversion Principle

#### Definitions

> **Dependency inversion principle (DIP)**: (A) High-level modules should not depend on low-level modules; both should depend on abstractions. (B) Abstractions should not depend on details; details should depend on abstractions.

```cpp
// bad code: hard-wired to keyboard and printer
void Copy() {
  char c;
  while ((c = readKey()) != EOF) print(c);
}

// bad fix: a growing switch on devices
enum OutputDevice { printer, disk };
void Copy(OutputDevice dev) {
  int c;
  while ((c = ReadKeyboard()) != EOF) {
    if (dev == printer) WritePrinter(c);
    else WriteDisk(c);
  }
}

// solution: depend on Reader/Writer abstractions
interface Reader { char Read(); }
interface Writer { void Write(char c); }
void Copy(const Reader& r, Writer& w) {
  char c;
  while ((c = r.Read()) != EOF) w.Write(c);
}
```

![Dependency inversion](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/13_SOLID/dip-copy.svg)

*Traditionally Copy depends on concrete devices and cannot be reused. Inverted, Copy and the devices both depend on the Reader and Writer abstractions.*

**Why "inversion"?** In traditional structured design (1990s):

- high-level modules depend on low-level modules
- abstractions depend on details

But high-level modules hold the logic and policy:

- low-level changes must not break them
- we want to reuse them
- abstractions hide the low-level details

So the dependency direction is inverted.

> [!quote] Indirection
> "All problems in computer science can be solved by another layer of indirection." — Butler Lampson (often attributed to David Wheeler). "…Except the problem of too many layers of indirection", "…but that usually will create another problem."
