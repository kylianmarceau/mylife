---
tags:
  - advanced-programming
---

# GoF Design Patterns I

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD15-Design Patterns.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD15-Design%20Patterns.pdf), PDF pages 1–66, and [ASD14-Design Patterns.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD14-Design%20Patterns.pdf), PDF pages 1–61. Johan Bontes, University of Cape Town; content adapted from Shvets, *Dive Into Design Patterns* (refactoring.guru)  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> ASD14 and ASD15 are the same deck. ASD15 (17 Aug) is ASD14 (13 Aug) plus five picture-only joke slides introducing lambdas, so this one note covers both sources. It includes lambdas as a pattern-killer, the three pattern classes, and the creational, structural and behavioural patterns covered.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Design Patterns Are|What Design Patterns Are]]
  - [[#Lambdas Make Many Patterns Obsolete|Lambdas Make Many Patterns Obsolete]]
  - [[#Three Classes Of Patterns|Three Classes Of Patterns]]
  - [[#Creational: Factory Method|Creational: Factory Method]]
  - [[#Creational: Prototype|Creational: Prototype]]
  - [[#Creational: Singleton|Creational: Singleton]]
  - [[#Structural: Adapter|Structural: Adapter]]
  - [[#Structural: Bridge|Structural: Bridge]]
  - [[#Structural: Decorator|Structural: Decorator]]
  - [[#Structural: Facade|Structural: Facade]]
  - [[#Structural: Composite|Structural: Composite]]
  - [[#Structural: Flyweight|Structural: Flyweight]]
  - [[#Structural: Proxy|Structural: Proxy]]
  - [[#Behavioural: Chain Of Responsibility|Behavioural: Chain Of Responsibility]]
  - [[#Behavioural: Command|Behavioural: Command]]
  - [[#Behavioural: Iterator And Mediator|Behavioural: Iterator And Mediator]]
  - [[#Behavioural: Memento|Behavioural: Memento]]
  - [[#Behavioural: Observer|Behavioural: Observer]]
  - [[#Behavioural: State (And Strategy)|Behavioural: State (And Strategy)]]
  - [[#Behavioural: Template Method|Behavioural: Template Method]]

---

## Core Content

### What Design Patterns Are

#### Definitions

> **Design pattern**: A reusable solution to a general problem that software developers face. "Patterns … are ways to describe best practices, good designs, and capture experience in a way that it is possible for others to reuse this experience" (hillside.net).

> **GoF**: The "Gang of Four" (Gamma, Helm, Johnson, Vlissides), authors of *Design Patterns* (1994).

**New language features, especially lambdas, have made many patterns obsolete.**

### Lambdas Make Many Patterns Obsolete

#### Definitions

> **Lambda**: An anonymous function that can **capture** outside variables.

> **Capture**: Bringing a variable from the enclosing scope into the lambda, by value or by reference.

Lambdas arrived in Lisp (1960), Python 2.2 (2002; a broken version in 1994), C++11 (2011/12) and Java SE 8 (2014).

In a von Neumann computer code and data are the same thing. OOP separates them: methods are fixed code and members are variable data. In functional code, **data can also be a function**.

```cpp
int i;
const auto X = [=]        // capture: [=] by value, [&] by reference
  (/* optional params */)
  mutable                 // by-value captures are const unless mutable
{
   i++;                   // error in Java (captures are always const)
   int a = i + 2;         // valid in Java
};
```

- A named lambda has no dedicated type; two identical lambdas have **different** types.
- **Java lambdas are somewhat broken**: captures are always const, so they are no more powerful than named functions.
- In other languages, capture by reference means changes inside the lambda change the outside value, which is very powerful (e.g. sorting).
- **Lambdas are data**: you can store them in a collection of "workers" and call each one:

```cpp
for (auto a: WorkList) { a(); }     // C++
for (var a: WorkList)  { a(); }     // Java
```

- Anything in scope when the lambda is defined can be captured. When in doubt, pass items as parameters: `a(i1)` in C++ (anything by reference), or `a(i2)` in Java with a mutable object such as `MyInteger`.

**Internally, every capture becomes a member field**:

```cpp
int i = 0; int r = 10;
auto lambda = [&](){ i++; r++; };

// is compiled roughly as:
class lambda {
  int& i; int& r;
  lambda(int& i, int& r): i(i), r(r) {}
  void dostuff() { i++; r++; }
};
```

### Three Classes Of Patterns

![Pattern catalogue](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/catalogue.svg)

*Creational patterns create objects, structural patterns assemble them, and behavioural patterns organise their communication.*

| Class | Purpose | Patterns (one-line summary) |
|---|---|---|
| **Creational** | Create objects without knowing all the details | Factory method (polymorphic construction); Abstract factory (more complex construction); Builder (build in stages); Singleton ("there can be only one"); Prototype (Java `object.clone()`) |
| **Structural** | Assemble objects into flexible, efficient structures | Adapter (match different interfaces); Bridge (prevent combinatorial explosion); Composite (split a big object into parts); Decorator (wrapper adding functionality); Facade (simplified interface); Flyweight (cache redundant data); Proxy (gatekeeper restricting access) |
| **Behavioural** | Communication between objects | Chain of responsibility (message passing); Command (action objects); Iterator (visit every element); Mediator (reduce cross-talk); Memento (snapshot/undo); Observer (subscribe to events); State (finite state machine); Strategy (object per algorithm); Template (algorithm blueprint); Visitor (command++) |

### Creational: Factory Method

#### Definitions

> **Factory method**: Keep construction details in one place (a factory) that creates the right subclass from a description, i.e. polymorphic construction.

- Polymorphism needs virtual methods, but **Java and C++ have no virtual constructors**. In C++ the child object is constructed in the wrong order for this.
- Pascal (Delphi) has virtual constructors through class references: `firstClass := TChild; first := firstClass.Create();` constructs a `TChild`.

```pascal
type TParentClass = class of TParent;        // class type: describes a family
constructor TParent.Create() virtual;  begin Writeln('Parent.Create'); end;
constructor TChild.Create()  override; begin Writeln('Child.Create');  end;
var firstClass: TParentClass; first: TParent;
begin
  firstClass := TChild;
  first := firstClass.Create();              // virtual construction
end.
```

**Java problem**: recreating objects from a text file of serialised data.

- You cannot restrict constructor signatures (they aren't virtual).
- You cannot call `Parent.MakeChild` without naming the child.
- There is no `Object.fromString()` that returns a new object.

**Solution**: a factory.

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
```

Leaving out `default` lets the compiler or linter warn about unhandled enum values, catching missing cases early ("shift left").

### Creational: Prototype

#### Definitions

> **Prototype**: Create new objects by cloning an existing one.

- **Java**: a single object hierarchy plus virtual methods give polymorphic `object.clone()`.
- **C++**: no virtual methods are needed. Use a concept (compile-time duck typing) to restrict the method signature:

```cpp
template <typename T>
concept Clonable = requires (const T t) {
    { t.clone() } -> same_as<T&>;
};
auto clone(const Clonable auto& object) { return object.clone(); }
```

### Creational: Singleton

#### Definitions

> **Singleton**: A class guaranteed to have exactly one instance, with global access to it.

```java
public /*final*/ class Singleton {
  private static bool isInitDone = false;                 // lazy init
  private static final Singleton instance = new Singleton();
  private Singleton() {}                                  // clients cannot create more
  public static Singleton getInstance() {
    if (!isInitDone) { /* do initialisation */ }
    return instance;
  }
}
```

Is it a pattern or an antipattern?

| For | Against |
|---|---|
| Memory use, performance, consistency | A global shared resource accessible everywhere, and global state is bad and too tempting |
| Correct uses: **logging**, a **database connection** | Massively overused when GoF appeared |
| | Breaks if more than one instance turns out to be needed |
| | Hidden dependencies and tight coupling: it "allows your code to lie about its dependencies" |
| | Others may add mutable state to a previously immutable singleton |
| | Hard to test without including the singleton (fix: mock it) |
| | One singleton as "CEO of the application" making all decisions is a god object |

### Structural: Adapter

#### Definitions

> **Adapter**: Converts one interface into another so incompatible objects can work together.

![Adapter](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/adapter.svg)

*An XML-based app cannot feed a JSON-only analytics library directly. An XML-to-JSON adapter sits between them.*

```java
public class Adapter implements IXML_er, IJSON_er {
  public void writeToDB(XML xdata) {
    JSON jdata = toJSON(xdata);
    json_db.write(jdata);
  }
}
```

### Structural: Bridge

#### Definitions

> **Bridge**: "Separates abstraction from implementation". It uses composition across independent dimensions instead of inheritance, so new dimensions can be added to the model.

1. Use inheritance only for IS-A relationships.
2. These are rare.
3. Very rare outside UI.
4. Bridge: use composition instead of inheritance.

![Bridge](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/bridge.svg)

*Shapes × colours by inheritance needs $m\times n$ classes. With a Shape that contains a Color, the hierarchies vary independently with $m+n$ classes.*

Example: a cross-platform GUI app. Instead of writing controls for each OS, create a display layer (the bridge) that abstracts each OS's implementation.

### Structural: Decorator

#### Definitions

> **Decorator**: Wraps an object in decorator objects that share its interface, each adding behaviour before or after delegating to the wrapped object.

The problem: a `Notifier` with SMS, Facebook and Slack subclasses (version 1) needs a subclass per **combination** (SMS+Slack, SMS+Facebook+Slack, …) in version 2, a class explosion.

![Decorator](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/decorator.svg)

*`BaseDecorator` IS-A Notifier and HAS-A Notifier (the wrappee). Concrete decorators call `super.send()` and add their own channel, so they can be stacked in any combination.*

The principle: **inheritance is rarely the best solution; to combine traits, use aggregation.**

### Structural: Facade

#### Definitions

> **Facade**: A simple interface around a complex model or subsystem.

A webshop is a facade. You order a product from a vendor, shipped to a location by a courier, with VAT payable to SARS, paid by credit card through your bank. None of those actors is your problem: you just fill in a few fields on a form.

![Facade](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/facade.svg)

*The application calls one method, `convertVideo(filename, format)`. The facade orchestrates the codec, bitrate, audio and file classes behind it.*

### Structural: Composite

#### Definitions

> **Composite**: A container (list or tree) that may contain items or other containers, all behind the same interface, so you can iterate over everything recursively.

![Composite](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/composite.svg)

*An order box contains products and smaller boxes. Asking any node for its price recurses through its children.*

### Structural: Flyweight

#### Definitions

> **Flyweight**: Saves memory by sharing the repeated (**intrinsic**, immutable) state between many objects, keeping only the unique (**extrinsic**, mutable) state per object.

**Problem**: a game fires a million particles. Each stores coords (8 B), vector (16 B), speed (4 B), colour (4 B) and a sprite (20 KB), about 21 KB each:

$$
21\text{ KB}\times 1\,000\,000 \approx 21\text{ GB}
$$

**GoF solution**: split each particle into `MovingParticle` (coords, vector, speed: unique) and a shared `Particle` (colour, sprite: repeated). Many moving particles point to a few shared ones.

![Flyweight](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/flyweight.svg)

*The 20 KB sprite is stored once per particle type instead of once per particle.*

> [!warning] <span style="color:#ffc778">The lecturer crosses this out</span>
> Games don't use flyweight; they use **data-oriented design**. Iterating a million objects is too slow: an array of structures (AoS) means pointer chasing. Games use a structure of arrays (SoA) for linear access. See [Data-Oriented Design](05B_Data_Oriented_Design.md).

### Structural: Proxy

#### Definitions

> **Proxy**: A gatekeeper with the same interface as the real object that controls access to it, e.g. a cache between a program and a slow resource.

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

### Behavioural: Chain Of Responsibility

#### Definitions

> **Chain of responsibility**: Each handler receives a request, processes it, then passes it on or drops it.

![Chain of responsibility](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/chain.svg)

*Instead of one blob doing authentication and authorisation, a chain of small handlers each checks one thing before the request reaches the ordering system.*

The source demo is a text-cleaning pipeline of handlers.

### Behavioural: Command

#### Definitions

> **Command**: Turns an action into an object (or lambda) separate from the UI element that triggers it.

Making `OKButton` IS-A `Button` ("yikes") causes:

- confusion of property versus class
- an explosion of classes (`SaveButton`, `OpenButton`, `PrintButton`, …)
- business logic everywhere and duplicated code
- tight UI–logic coupling

A command object shared by the button, menu item and shortcut gives **no duplication and loose coupling**.

![Command](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/command.svg)

*Every UI trigger for "save" calls the same Save command, which calls the business logic.*

With lambdas, no OOP workaround is needed:

```cpp
type Command: []{} -> bool;                      // lambda returning bool
const emptyCommand: Command = [&]{ return false; };
class UIControl: public InvisibleControl {
public:
  action: Command = emptyCommand;                // do nothing by default
  bool execute() final { return action(); }
};
form1.Actions.Add(ID_SaveAs, [&]{                // [&] captures context
  if (savedialog1.execute()) {                   // user pressed OK
    auto filename = savedialog1.filename;
    editor1.SaveToFile(filename);
  }
});
```

### Behavioural: Iterator And Mediator

#### Definitions

> **Iterator**: Walk through every item of a collection using `first`, `next` and `current` methods.

> **Mediator**: A central hub that connects multiple components so they don't talk to each other directly (a "fancy version of the command pattern").

```pseudo
for (a in Collection) { a.dostuff() }
// runs as:
c.First();             // current = c[-1]
while (c.next()) {     // current = c[0], c[1], ...
  a = c.current(); a.dostuff();
}
```

Design custom collections with `first`, `next` and `current`. Every modern language has for-in loops, so iterator no longer needs an OOP workaround.

### Behavioural: Memento

#### Definitions

> **Memento**: Saving and restoring an object's state without exposing its private details.

**Problem**: the program must save state from one or more objects. It must not access their private details, and cloning isn't an option (unsafe because of links to other objects).

**Solution**:

- The object (originator) creates a **snapshot** of its own state.
- A **memento** adds metadata (date, command).
- A **caretaker** stores the snapshots.

![Memento](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/memento.svg)

*The editor makes and restores its own immutable snapshots. The caretaker keeps the history without seeing inside.*

```java
class Editor implements IUndo {
  String text;        // gets saved
  Window owner;       // not saved
  EditorSnapshot makeSnapshot();
  void restoreSnapshot(EditorSnapshot restorePoint);
}
class EditorSnapshot implements IMemento immutable { String text; }
interface IMementoList immutable {               // multiple objects restored together
  property int id; property Datetime timestamp;
  property CommandId reason; property List<IMemento> sources;
  void restore() { for (s in sources) { s.source.restoreSnapshot(s); } }
}
class Caretaker {
  List<IMementoList> snapshots;
  void add(IMementoList item);
  void restore(int id) { getById(snapshots, id).restore(); }
}
```

| Useful for | Pro | Con |
|---|---|---|
| Undo; transactions (commit/rollback); save to file | Saves state without knowing objects' internals; the caretaker tracks snapshots | Can use a lot of RAM; may need to track originals to destroy obsolete snapshots; needs immutable objects |

### Behavioural: Observer

#### Definitions

> **Observer**: Interested objects **subscribe** to a publisher and are notified when its state changes.

Example: rather than clients checking the store every day for the new iPhone, the store emails all subscribed clients when it arrives.

```java
interface IObserver  { void update(msg); }
interface IPublisher {
  void subscribe(IObserver client);
  void unsubscribe(IObserver client);
}
class Publisher implements IPublisher {
  List<IObserver> clients;
  private void update(msg) { for (c in clients) { c.update(msg); } }
}
```

![Observer](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/observer.svg)

*The publisher keeps a subscriber list and calls `update(msg)` on each. MVC views are observers of the model.*

### Behavioural: State (And Strategy)

#### Definitions

> **State**: Implements a finite state machine with an `IState` interface and one class per state. The master object switches between state objects and delegates state-specific work to the current one.

**Problem**: a complex `switch` on a state string controls behaviour (e.g. a document moving draft → moderation → published, depending on user role).

```java
interface IPlayState { property AudioPlayer player; void pressPlay(); }
class PlayState implements IPlayState {
  void pressPlay() { player.setState(new PauseState()); player.pauseMusic(); }
}
class PauseState implements IPlayState {
  void pressPlay() { player.setState(new PlayState()); player.playMusic(); }
}
class MusicPlayer {
  IPlayState state = new PauseState();
  Button playButton(state.pressPlay);
}
```

![State](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/state.svg)

*Pressing play in PauseState starts the music and switches to PlayState, and vice versa.*

| Pro | Con |
|---|---|
| Single responsibility: one state per class | Overkill with only a few simple states |
| Open–closed: change state details without changing the player class | |
| Eliminates complex state-machine code; the master is in exactly one state | |

States sharing code can inherit from or contain shared classes. **Strategy** is a more complex version of State and is **out of scope**.

### Behavioural: Template Method

#### Definitions

> **Template method**: Define the skeleton of an algorithm in a base class (class A) and let subclasses (class B) override specific steps.

**Problem**: several versions of an algorithm repeat the same code, which violates DRY.

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
  void addPlants()     { /* add coffee */ }   // no sugar, no milk (duh)
}
```

![Template method](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/14_15_Design_Patterns_I/template.svg)

*`DataMiner.mine()` fixes the sequence of steps. Subclasses override file-format steps; analysis and reporting have default implementations.*

Pro: clients override only certain parts of a large algorithm, so changes to other parts affect them less. Template method also fixes the **call super** and **sequential coupling** antipatterns ([Antipatterns](12_Antipatterns.md)). The remaining pro/con rows on the source's Template slide repeat the State slide.
