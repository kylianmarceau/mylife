---
tags:
  - advanced-programming
---

# Design Patterns I: GoF Patterns And Lambdas

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD14-Design Patterns.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD14-Design%20Patterns.pdf) (61 pages) and [ASD15-Design Patterns.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD15-Design%20Patterns.pdf) (66 pages), Johan Bontes, University of Cape Town. ASD15 is a revised version of ASD14 (same content plus demo links and an updated chain-of-responsibility example), so both are covered in this one note. Content adapted from *Dive Into Design Patterns* (refactoring.guru).
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> What design patterns are, how lambdas made many obsolete, the three GoF pattern classes, and the creational, structural and behavioural patterns covered in the course.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Design Patterns Are|What Design Patterns Are]]
  - [[#Lambdas|Lambdas]]
  - [[#Anatomy Of A Lambda And Captures|Anatomy Of A Lambda And Captures]]
  - [[#The Three Pattern Classes|The Three Pattern Classes]]
  - [[#Factory Method|Factory Method]]
  - [[#Prototype|Prototype]]
  - [[#Singleton|Singleton]]
  - [[#Adapter|Adapter]]
  - [[#Bridge|Bridge]]
  - [[#Decorator|Decorator]]
  - [[#Facade|Facade]]
  - [[#Composite|Composite]]
  - [[#Flyweight|Flyweight]]
  - [[#Proxy|Proxy]]
  - [[#Chain Of Responsibility|Chain Of Responsibility]]
  - [[#Command|Command]]
  - [[#Iterator|Iterator]]
  - [[#Mediator|Mediator]]
  - [[#Memento|Memento]]
  - [[#Observer|Observer]]
  - [[#State|State]]
  - [[#Strategy|Strategy]]
  - [[#Template Method|Template Method]]

---

## Core Content

### What Design Patterns Are

#### Definitions

> **Design pattern**: A reusable solution to a general problem that software developers face. "Patterns … are ways to describe best practices, good designs, and capture experience in a way that it is possible for others to reuse this experience." — hillside.net

> **GoF patterns**: The patterns catalogued by the "Gang of Four" (Gamma, Helm, Johnson, Vlissides) in *Design Patterns* (1994).

New language features — especially **lambdas** — have made many patterns obsolete.

### Lambdas

#### Definitions

> **Lambda**: An anonymous function that can **capture** variables from its surrounding scope. Because it is a value, it can be stored, passed and called later.

| Language | Lambdas since |
|---|---|
| Lisp | 1960 |
| Python | 2.2 (2002); a broken version already in 1994 |
| C++ | C++11 |
| Java | Java SE 8 (2014) |

A Von Neumann computer treats code and data the same. OOP separates them: in a class, the methods (code) are fixed and the members (data) vary. In functional code, **data can also be a function** — and that is what lambdas bring to OOP languages.

### Anatomy Of A Lambda And Captures

```cpp
int i;
const auto X = [=/&, ...] (params) const/mutable {
    i++;            // error in Java
    int a = i + 2;  // valid in Java
};
```

| Part | Meaning |
|---|---|
| `const auto X =` | A named lambda; it has no dedicated type (two identical lambdas have different types) |
| `[=]` / `[&]` | Capture list: `[=]` captures by value, `[&]` by reference |
| `(params)` | Optional parameters |
| `const` / `mutable` | Whether by-value captures may be modified |
| `{ ... }` | Body; the outside `i` has been captured |

| | Java lambdas | Lambdas in other languages (e.g. C++) |
|---|---|---|
| Captures | Always effectively `const` ("somewhat broken") | Can capture by reference |
| Power | No more powerful than named functions | Changes inside the lambda change the outside value — very powerful (e.g. sorting with a counting comparator) |

**Lambdas are data**: you can put them in a collection of "workers" and call each one:

```cpp
for (auto a : WorkList) { a(); }   // C++
```
```java
for (var a : WorkList) { a(); }    // Java
```

**What can be captured?** Anything in scope when the lambda was defined. When in doubt, pass items as parameters instead:

```cpp
int i1;                              // C++ can pass anything by reference
for (auto a : WorkList) { a(i1); }
```
```java
MyInteger i2;                        // an Object is passed by reference
for (var a : WorkList) { a(i2); }
```

**Internally**, each capture becomes a member field of a hidden class:

```cpp
int i = 0;
int r = 10;
auto lambda = [&]() { i++; r++; };

// is compiled roughly as:
class lambda {
    int& i;
    int& r;
    lambda(int& i, int& r) : i(i), r(r) {}
    void dostuff() { i++; r++; }
};
```

### The Three Pattern Classes

| Class | Purpose | Patterns covered |
|---|---|---|
| **Creational** | Create objects without having to know all the details | Factory method, abstract factory, builder, singleton, prototype |
| **Structural** | Assemble objects into larger structures that are flexible and efficient | Adapter, bridge, composite, decorator, facade, flyweight, proxy |
| **Behavioural** | Communication between objects | Chain of responsibility, command, iterator, mediator, memento, observer, state, strategy, template method, visitor |

![GoF pattern catalogue](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/catalogue.svg)

*The GoF catalogue grouped into creational, structural and behavioural patterns.*

Creational summary:

| Pattern | In a phrase |
|---|---|
| Factory method | Polymorphic construction |
| Abstract factory | More complex construction (families of objects) |
| Builder | Build in stages |
| Singleton | "There can be only one" |
| Prototype | Java's `object.clone()` |

### Factory Method

#### Definitions

> **Factory method**: Keeps object-construction details in one place, so code can create the right subclass without naming it — "polymorphic construction".

Polymorphism needs virtual methods, but Java and C++ have **no virtual constructors**. Some languages do, e.g. Pascal (Delphi), using class references:

```pascal
type TParentClass = class of TParent;   // class type: describes the family

constructor TParent.Create() virtual;
begin Writeln('Parent.Create'); end;

constructor TChild.Create() override;
begin
    // inherited Create();
    Writeln('Child.Create');
end;

var firstClass: TParentClass; first: TParent;
begin
    firstClass := TChild;
    first := firstClass.Create();   // creates a TChild polymorphically
end.
```

Why not in C++/Java? In C++ the order of construction would be wrong (the child would be created first); Pascal constructs the parent first (it got objects later, with the flaw fixed).

**Java problem**: recreate objects from a text file of serialised object data.

- You can't restrict a constructor's signature, and constructors aren't virtual.
- You can't call a `Parent.MakeChild` method without naming the child.
- There's no `Object.fromString()` that returns a new object.

**Solution**: keep the constructor details in one place — a factory.

```java
public Shape shapeFactory(ShapeId shapeId, String params)
        throws UnknownShapeException {
    switch (shapeId) {
        case ID_oval: return new RoundRect(params, 100);
        case ID_rect: return new RoundRect(params, 0);
        case ID_blob: return new Blob(params);
        // shift left: never use default!
    }
    throw new UnknownShapeException(shapeId, params);
}

public class Circle extends Shape {
    public Circle(String params) { ... }
}
```

Leaving out `default` means the compiler can warn about unhandled enum values, catching mistakes early (shift left).

### Prototype

#### Definitions

> **Prototype**: Create new objects by cloning an existing one.

- **Java**: a single object hierarchy plus virtual methods makes it polymorphic: `object.clone()`.
- **C++**: no virtual methods needed — use duck typing and restrict the method signature with a concept:

```cpp
template <typename T>
concept Clonable = requires (const T t) {
    { t.clone() } -> same_as<T&>;
};

// clone factory method
auto clone(const Clonable auto& object) {
    return object.clone();
}
```

### Singleton

#### Definitions

> **Singleton**: A class that allows only one instance, with a global access point to it.

```java
public /*final*/ class Singleton {
    private static boolean isInitDone = false;   // lazy init
    private static final Singleton instance = new Singleton();
    // private constructor: clients cannot create more
    private Singleton() {}
    public static Singleton getInstance() {
        if (!isInitDone) { /* do initialisation */ }
        return instance;
    }
}
```

Pattern or antipattern?

| For | Against |
|---|---|
| Memory use, performance, consistency | When the GoF book appeared, it was used far too much |
| A global shared resource accessible everywhere | Breaks if more than one is actually needed |
| Used correctly for logging and database connections | Misused, it creates hidden dependencies and tight coupling |
| | It lets code **lie about its dependencies**, and you can't trust other programmers not to add mutable state to a previously immutable singleton |
| | Global state is bad and too tempting; the "CEO of the application" making all decisions becomes a god object |
| | Hard to test code without including the singleton (fix by mocking it) |

### Adapter

#### Definitions

> **Adapter**: A wrapper that lets objects with incompatible interfaces work together by converting one interface into another.

Example: an app produces XML, but the database only accepts JSON.

```java
public class Adapter implements IXML_er, IJSON_er {
    public void writeToDB(XML xdata) {
        JSON jdata = toJSON(xdata);
        json_db.write(jdata);
    }
}
```

![Adapter](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/adapter.svg)

*The client talks XML to the adapter, which converts to JSON for the database.*

### Bridge

#### Definitions

> **Bridge**: "Separates abstraction from implementation" (GoF) — use **composition instead of inheritance** to avoid a combinatorial explosion of subclasses.

1. Use inheritance only for IS-A relationships.
2. These are rare — very rare outside UIs.
3. Bridge uses composition instead, which lets you add new dimensions to the model.

Example: `Shape` × `Color` by inheritance needs `RedCircle`, `BlueCircle`, `RedSquare`, `BlueSquare`, … Instead, `Shape` **has a** `Color`. Similarly, for a cross-platform GUI, don't build every control for every OS: create a display layer (the bridge) that abstracts each OS's display implementation.

![Bridge](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/bridge.svg)

*Two independent hierarchies joined by a has-a link, so they vary separately instead of multiplying.*

### Decorator

#### Definitions

> **Decorator**: A wrapper that adds new behaviour to an object by wrapping it in an object with the same interface; wrappers can be stacked.

Inheritance is rarely the best solution. To combine traits (e.g. a notifier that sends email **and** SMS **and** Slack messages), use aggregation: wrap the base object in decorators rather than creating a subclass for every combination.

![Decorator](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/decorator.svg)

*Each decorator wraps another component with the same interface and adds one trait before or after delegating.*

### Facade

#### Definitions

> **Facade**: A simple interface in front of a complex subsystem.

A webshop: as a client you order a product, from a vendor, to a location, by a shipping company, with VAT payable to SARS, paid online by credit card via your bank. None of those entities is your problem — you fill in a few form fields. The form is the facade.

![Facade](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/facade.svg)

*The client calls one simple facade, which coordinates the many subsystems behind it.*

### Composite

#### Definitions

> **Composite**: Composes objects into tree structures so that a container and its parts can be treated uniformly.

- The composite class is a container — a list or a tree — that may contain other containers.
- Operations iterate **recursively** over everything inside the container (e.g. the total price of a box of boxes of products).

![Composite](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/composite.svg)

*Leaves and containers share one interface; a container forwards each operation to its children recursively.*

### Flyweight

#### Definitions

> **Flyweight**: Shares common (intrinsic) data between many objects instead of duplicating it, to save memory.

- **Problem**: many objects contain duplicate information (e.g. every particle in a game storing its own colour and sprite), consuming too much memory.
- **Solution**: move the shared data into a shared flyweight object that many objects reference.

![Flyweight](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/flyweight.svg)

*Many lightweight objects keep only their unique state and point to one shared object holding the repeated data.*

But games don't actually use flyweight — they use **data-oriented design** (see [DOD](05B_Data_Oriented_Design.md)):

- Iterating 1 000 000 objects is too slow.
- Flyweight is an **AoS** (array of structures) solution: pointer chasing.
- Games use **SoA** (structure of arrays), giving linear access.

### Proxy

#### Definitions

> **Proxy**: A stand-in that controls access to another object — a gatekeeper — often a cache between a program and a slow resource.

Examples: web proxies (Nginx, Squid), database proxies, disk proxies.

```java
interface IDisk {
    List<String> getFileList(String path);
    Vector<byte> readData(String file);
}

class DiskProxy implements IDisk {
    List<Vector<byte>> Cache;
    Disk hd;
    Vector<byte> readData(String file) {
        if (file in Cache) { return Cache.getFile(file); }
        else {
            data = hd.getFile(file);
            Cache.Add(data);
            return data;
        }
    }
}
```

Structural summary:

| Pattern | In a phrase |
|---|---|
| Adapter | Match objects with different interfaces |
| Bridge | Prevent combinatorial explosion |
| Composite | Split a big object into parts |
| Decorator | Wrapper to add new functionality |
| Facade | Simplified interface around an object |
| Flyweight | Cache redundant data to save space |
| Proxy | Gatekeeper restricting access to a class |

### Chain Of Responsibility

#### Definitions

> **Chain of responsibility**: A request passes along a chain of handlers; each one receives the request, processes it, then passes it on or drops it.

Behavioural summary:

| Pattern | In a phrase |
|---|---|
| Chain of responsibility | Message passing |
| Command | Action objects |
| Iterator | Visit every element |
| Mediator | Reduce cross-talk |
| Memento | Snapshot / undo |
| Observer | Subscribe to events |
| State | Finite state machine |
| Strategy | Object per algorithm |
| Template method | Algorithm blueprint |
| Visitor | Command++ (see [Clean Code And Visitor](17_Clean_Code_And_Visitor.md)) |

**WinAPI mouse messages** (a window `Form1` containing `Panel1` containing `Button1`):

| Option | How the chain works |
|---|---|
| 1. Every link knows the next | Msg 1: `Button1.OnMouseOver` draws a glow and drops the message. Msg 2: `Panel1.OnMouseOver` does nothing and calls its owner's `OnMouseOver`; `Form1.OnMouseOver` flashes the caption; no owner, so drop |
| 2. Links don't know each other | WinAPI iterates (iterator pattern) over controls top-most to bottom-most: traverse the tree doing hit tests, descending into children until no more hits (the top-most control). Then visit the hit controls in reverse order; each handler returns `true` to pass the message on or `false` to stop |

ASD15 replaces this with a "clean text" demo: each handler in the chain cleans one aspect of a text (e.g. trimming, normalising) before passing it on.

![Chain of responsibility](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/chain.svg)

*Each handler either handles the request and stops, or passes it to the next handler.*

### Command

#### Definitions

> **Command**: Turns an action into an object (or lambda) so it can be stored, passed and executed separately from the UI that triggers it.

Problem: is `OKButton` IS-A `Button`? Yikes — subclassing every button for its action causes:

| Without Command | With Command |
|---|---|
| Confusion of property and class | No code duplication |
| Explosion of classes | Loose coupling between UI and logic |
| Business logic everywhere | |
| Duplicated code | |
| Tight UI–logic coupling | |

With lambdas, no OOP workaround is needed:

```text
type Command: [] {} -> bool;                  // lambda returning bool
const emptyCommand: Command = [&]{ return false; };

class UIControl : public InvisibleControl {
public:
    action: Command = emptyCommand;           // do nothing
    bool execute() final { return action(); }
}

//                             +--- [&] = capture context
form1.Actions.Add(ID_SaveAs, [&]{
    if (savedialog1.execute()) {              // user pressed OK
        auto filename = savedialog1.filename;
        editor1.SaveToFile(filename);
    }
});
```

![Command](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/command.svg)

*UI controls hold a command; executing the control runs the command, keeping business logic out of the UI classes.*

### Iterator

#### Definitions

> **Iterator**: Walks through every item of a collection without exposing its internal structure.

A collection provides `first`, `next` and `current` methods. A `for (a in Collection) { a.dostuff(); }` loop runs:

```text
c.First();            // current = c[-1]
while (c.next()) {    // current = c[0], c[1], c[2], ...
    a = c.current();
    a.dostuff();
}
```

Design custom collections with `first`, `next` and `current`. Every modern language has `for-in` loops, so no OOP workaround is needed.

### Mediator

#### Definitions

> **Mediator**: A central hub that connects multiple components so they don't talk to each other directly — reducing cross-talk. A fancy version of the command pattern.

### Memento

#### Definitions

> **Memento**: A snapshot of an object's state, created by the object itself, so state can be restored later without exposing private details.

Problem: a program must save the state of one or more objects, but

- must not access their private details, and
- cloning isn't an option (unsafe, because of links to other objects).

Solution:

| Role | Responsibility |
|---|---|
| **Originator** (the object) | Creates a snapshot of its own state, and restores from one |
| **Memento** | The snapshot, plus metadata (date, command) |
| **Caretaker** | Stores and manages snapshots |

```java
class Editor implements IUndo {
    String text;     // gets saved
    Window owner;    // not saved
    EditorSnapshot makeSnapshot();                          // IUndo
    void restoreSnapshot(EditorSnapshot restorePoint);      // IUndo
}

class EditorSnapshot implements IMemento immutable { String text; }

interface IMemento immutable {
    property int id;
    property IUndo source;
}

interface IMementoList immutable {   // if several objects must be restored
    property int id;
    property Datetime timestamp;
    property CommandId reason;
    property List<IMemento> sources;
    void restore() { for (s in sources) { s.source.restoreSnapshot(s); } }
}

class Caretaker {                    // manages snapshots
    List<IMementoList> snapshots;
    void add(IMementoList item);
    void restore(int id) {
        restorepoint = getById(snapshots, id);
        restorepoint.restore();
    }
}
```

![Memento](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/memento.svg)

*The editor creates and restores its own snapshots; the caretaker only stores them.*

Uses: undo (revert to a save point), transactions (commit/rollback), saving to file.

| Pro | Con |
|---|---|
| Saves state without knowing objects' internal details | Can use a lot of RAM with many snapshots |
| The caretaker tracks snapshots | May need to track originals (if not permanent) to destroy obsolete snapshots |
| | Needs immutable objects |

### Observer

#### Definitions

> **Observer** (publish–subscribe): Interested objects subscribe to a publisher, which notifies all subscribers when its state changes.

Problem: you're waiting for the iPhone 35. You could check in at the store every day (polling), or the store could email everyone. Better: interested clients **subscribe** to updates.

```java
interface IObserver {
    void update(msg);
}

interface IPublisher {
    void subscribe(IObserver client);
    void unsubscribe(IObserver client);
}

class Publisher implements IPublisher {
    List<IObserver> clients;
    private void update(msg) {
        for (c in clients) { c.update(msg); }
    }
}
```

![Observer](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/observer.svg)

*Subscribers register with the publisher; one state change notifies every subscriber.*

### State

#### Definitions

> **State**: Implements a finite state machine with one class per state; the master object delegates behaviour to its current state object, which switches states.

- **Problem**: a complex `case` statement controls the state.
- **Solution**: an `IState` interface; one class per state; the master object switches state and calls the state object to do the state's work.

**Music player**:

```java
interface IPlayState {
    property AudioPlayer player;
    void pressPlay();   // play/pause
}

class PlayState implements IPlayState {
    void pressPlay() {                  // play -> pause
        player.setState(new PauseState());
        player.pauseMusic();
    }
}

class PauseState implements IPlayState {
    void pressPlay() {                  // pause -> play
        player.setState(new PlayState());
        player.playMusic();
    }
}

class MusicPlayer {
    IPlayState state = new PauseState();
    Button playButton(state.pressPlay);
}
```

![State pattern music player](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/state.svg)

*Pressing play in PauseState switches to PlayState and vice versa; the player just forwards the button press.*

States with shared code can inherit from, or contain, shared classes.

| Pro | Con |
|---|---|
| Single responsibility: one state per class | Overkill with only a few simple states |
| Open–closed: change state details without changing the player class | |
| Eliminates complex state-machine conditionals; the master can only be in one state | |

### Strategy

#### Definitions

> **Strategy**: One object per interchangeable algorithm, selected at run time — a more complex version of State. Out of scope for this course.

### Template Method

#### Definitions

> **Template method**: Defines the skeleton of an algorithm in a base class, leaving the detailed steps to subclasses.

- **Problem**: different versions of an algorithm repeat the same code in each version, violating DRY.
- **Solution**: put the steps (skeleton) in class A and the details in class B.

```java
class BrewMaster {
    void boilWater()     { print("boil water"); }
    void addPlants()     { /* do nothing */ }
    void removePlants()  { /* do nothing */ }
    void addCondiments() { /* do nothing */ }
}

class BrewTea extends BrewMaster {
    void addPlants()     { /* hang tea bag */ }
    void removePlants()  { /* remove tea bag */ }
    void addCondiments() { /* just sugar, no milk */ }
}

class BrewCoffee extends BrewMaster {
    void addPlants() { /* add coffee */ }
    // no sugar, no milk (duh)
}
```

![Template method](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/template.svg)

*The base class fixes the order of steps; subclasses override only the steps that differ.*

Pro: clients can override only certain parts of a large algorithm, so they are less affected by changes to other parts. Template method is also the fix for the sequential-coupling and call-super antipatterns (see [Antipatterns](12_Antipatterns.md#Object-Oriented%20Antipatterns)).
