---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 14 — GoF Design Patterns I"
---

# ASD 14 — GoF Design Patterns I

**Source note:** [GoF Design Patterns I](../../ASD/14_15_Design_Patterns_I.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Choosing Patterns|Choosing Patterns]]
  - [[#Creation|Creation]]
  - [[#Structure|Structure]]
  - [[#Behaviour|Behaviour]]
  - [[#Lambdas Make Many Patterns Obsolete|Lambdas Make Many Patterns Obsolete]]
  - [[#Structural: Flyweight|Structural: Flyweight]]
  - [[#Behavioural: State (And Strategy)|Behavioural: State (And Strategy)]]
  - [[#Pattern Mechanics And Trade-offs|Pattern Mechanics And Trade-offs]]

## Core Content

### Choosing Patterns

<!-- qard-id: ap-4fa9a5fb41921e473329 -->
> [!qard]- How do creational, structural and behavioural patterns differ?
> They organise object creation, object composition, and responsibility/communication respectively. Choose a pattern to solve a concrete recurring problem.

<!-- qard-id: ap-cce43cead44c59058ff6 -->
> [!qard]- How can a lambda replace a small Command or callback class?
> A function value can store and pass the operation, capturing needed context without defining a dedicated class for each action.

<!-- qard-id: ap-4f6e7a89dd6a6ed86dbc -->
> [!qard]- What differs between capture by value and by reference?
> By-value captures store a copy; by-reference captures refer to the original state. References require suitable lifetimes, and mutation can affect shared state.

### Creation

<!-- qard-id: ap-bb6c4e319d013dab0254 -->
> [!qard]- What problem does a Factory solve?
> Clients need an appropriate concrete object without spreading construction details. The factory chooses and constructs an implementation behind a common abstraction.

<!-- qard-id: ap-a0d74d415cb4ed98eadd -->
> [!qard]- When is Prototype useful?
> Create a new object by cloning an existing configured example, while deciding whether shared/referenced state should also be copied.

<!-- qard-id: ap-9d1f11c3fefd1d3e8521 -->
> [!qard]- What does Singleton guarantee, and what is its main design risk?
> One globally accessible instance; it can hide dependencies, introduce shared mutable state and make isolation/testing difficult.

<!-- qard-id: ap-b8462c293e4873fc0805 -->
> [!qard]- How do Factory, Abstract Factory and Builder differ in the problem they organise?
> A factory selects/constructs a concrete object; an abstract factory constructs a related family through a common interface; a builder assembles a complex result in stages. The latter two are briefly named in the catalogue/recap.

<!-- qard-id: ap-d3b4f45a39fb7ce75579 -->
> [!qard]- Why does the enum-based factory example avoid silently handling every unknown case in a generic default?
> Explicit alternatives help tools/review reveal missing variants as the set grows; truly unknown input still needs deliberate failure handling. Do not assume a compiler warns automatically for every switch form.

### Structure

<!-- qard-id: ap-f36a210fe9af85f1d8c7 -->
> [!qard]- When should you use an Adapter?
> Existing interfaces do not match; wrap one component to translate the expected operations/data into what it supports.

<!-- qard-id: ap-0e6b290b7aeb1402edea -->
> [!qard]- How does Bridge prevent a class explosion?
> Separate independently varying dimensions into composed hierarchies, such as shapes and colours, rather than a subclass for every combination.

<!-- qard-id: ap-1d75cb171a4992cff560 -->
> [!qard]- How does Decorator add optional behaviour?
> Wrap an object with another implementing the same interface, delegating and adding behaviour before or after; wrappers can be stacked.

<!-- qard-id: ap-ebdeb5fd846a9e29cfdd -->
> [!qard]- How does Facade differ from Adapter?
> A Facade offers a simpler entry point to a complex subsystem; an Adapter translates an incompatible interface into a required one.

<!-- qard-id: ap-6cee3077282d42acc441 -->
> [!qard]- What does Composite let a client treat uniformly?
> Individual leaves and containers of other components through one interface, supporting recursive operations on a tree.

<!-- qard-id: ap-045c79e9d41bc367fbd4 -->
> [!qard]- How does Flyweight reduce memory?
> Share repeated intrinsic state among many logical objects and keep varying extrinsic state separately. Shared intrinsic state should be immutable.

<!-- qard-id: ap-1c0fdc39e5822abeee3e -->
> [!qard]- How does a Proxy differ in intent from a Decorator?
> Both may preserve an interface, but a Proxy controls access or manages a resource (e.g. caching/lazy loading); a Decorator adds behaviour/features.

### Behaviour

<!-- qard-id: ap-53c4bfc771df97b3534a -->
> [!qard]- What does Chain of Responsibility do?
> Pass a request through handlers, each deciding whether to process, continue or stop, reducing dependence on one monolithic receiver.

<!-- qard-id: ap-35262fc67a55ab85745f -->
> [!qard]- How does Command decouple UI from business logic?
> Represent an action separately so a button, menu and keyboard shortcut can invoke the same operation without duplicating it.

<!-- qard-id: ap-4ed7796c338d76b8d17c -->
> [!qard]- What does Iterator hide from a collection's client?
> Traversal mechanics and storage representation, exposing a consistent way to obtain successive elements.

<!-- qard-id: ap-33c5b061033729f0998b -->
> [!qard]- How does Mediator reduce direct component dependencies?
> Components communicate through a coordinating hub rather than all knowing one another, simplifying links while risking an overgrown mediator.

<!-- qard-id: ap-b9b856bcc338c9b10de8 -->
> [!qard]- How does Memento support undo without exposing internals?
> The originator creates/restores its snapshot; a caretaker stores snapshots without interpreting private state. Snapshot history can consume substantial memory.

<!-- qard-id: ap-662a865090f688d54693 -->
> [!qard]- How does Observer decouple a publisher from interested clients?
> Clients subscribe through a notification interface; the publisher notifies them of changes without knowing their concrete roles.

<!-- qard-id: ap-1c6f9deacf033fbeea8d -->
> [!qard]- How does State organise state-dependent behaviour?
> A context delegates to its current state object; each state supplies its behaviour and transitions instead of a large repeated switch.

<!-- qard-id: ap-8fe5e621e81069fb91bd -->
> [!qard]- How does Template Method organise related algorithms?
> Fix the overall algorithm sequence and let implementations override selected steps, keeping shared order and work in one place.

<!-- qard-id: ap-6ef44fb21c2a713c664c -->
> [!qard]- Why can adding patterns unnecessarily harm a design?
> Extra classes, indirection and extension mechanisms increase complexity when the problem does not need them.

### Lambdas Make Many Patterns Obsolete

<!-- qard-id: ap-0cc95f24d525a6695ba9 -->
> [!qard]- What Java capture restriction differs from a by-reference mutable C++ capture?
> Captured local variables in Java must be final/effectively final; their referenced objects can still be mutable. C++ reference captures can update the original variable but must not outlive it.

### Structural: Flyweight

<!-- qard-id: ap-d0ce18e5e73207f87927 -->
> [!qard]- Why does the lecture prefer DOD over a million pointer-linked flyweight particles in its game example?
> Sharing the sprite saves memory, but indirect traversal can still be slow. Separating hot coordinate/state arrays and shared cold assets addresses access locality as well as duplicate storage.

### Behavioural: State (And Strategy)

<!-- qard-id: ap-cedfdc5367b2349445a6 -->
> [!qard]- When can State or Template Method be excessive, and what lighter alternative can express variation?
> A few simple states or steps may need only an enum/branch or passed function values. Add class-based extension structure only when its separation and reuse justify the extra indirection; Strategy is marked outside the detailed treatment here.

### Pattern Mechanics And Trade-offs

<!-- qard-id: ap-6c29c61fd72012813f65 -->
> [!qard]- How does Factory centralise a dependency that otherwise appears at many call sites?
> It encapsulates concrete-type selection and construction details, so callers depend on the product abstraction and creation request rather than each subclass constructor.

<!-- qard-id: ap-51e124a96d95fd5f046c -->
> [!qard]- Why can copying an object reference fail to implement Prototype's intended cloning?
> It may alias the same object; even a shallow copy can share referenced mutable state. Decide which parts of the new object's state must be independent.

<!-- qard-id: ap-ae071bd6b76a51a301e5 -->
> [!qard]- How does Singleton's global access hide a dependency?
> A component can use the singleton without declaring it in its interface/constructor, making its required environment and test setup less visible.

<!-- qard-id: ap-d391bfa1dd9eb5d27233 -->
> [!qard]- Why can a mutable Singleton make tests order-dependent?
> Shared state survives between users/tests unless reset or isolated, so one action changes another's starting conditions.

<!-- qard-id: ap-3d0183dda26f6da38836 -->
> [!qard]- How does Adapter preserve an existing useful implementation?
> Translate its interface/data format for the new client rather than rewriting either component's underlying responsibility.

<!-- qard-id: ap-9ccec79bbc9af9a21fb7 -->
> [!qard]- How does Bridge differ from adapting two already incompatible interfaces?
> Bridge proactively separates independently varying abstraction and implementation dimensions; Adapter reconciles an existing mismatch.

<!-- qard-id: ap-2cb3a0c0458979042de5 -->
> [!qard]- Why should a Decorator expose the wrapped object's common interface?
> Clients can use a wrapped instance wherever the original interface is expected, while stacked wrappers delegate and add optional behaviour.

<!-- qard-id: ap-3c0b27ebd21f1caa197a -->
> [!qard]- Why can subclassing every combination of optional features cause combinatorial growth?
> Each independent option multiplies the combinations; composition/decorators combine behaviours without a dedicated class for every combination.

<!-- qard-id: ap-68d63884c392be40001c -->
> [!qard]- What does Composite's recursive interface let an aggregate operation do?
> Ask each child for the same operation and combine results, regardless of whether the child is a leaf or another container.

<!-- qard-id: ap-e97a361a90e1a38863d4 -->
> [!qard]- How do intrinsic and extrinsic state differ in Flyweight?
> Intrinsic state is shared across logical instances and should be immutable; extrinsic state varies per use and must be supplied/stored separately.

<!-- qard-id: ap-abd420bdde529fd9d516 -->
> [!qard]- Why does a Proxy normally preserve the real subject's interface?
> It can mediate access transparently, adding lazy creation, caching or access control while clients request the same subject operation.

<!-- qard-id: ap-dce5602dbbafcbd26ba7 -->
> [!qard]- What determines whether Chain of Responsibility passes a request onward?
> Each handler's policy: it may process, reject, stop or delegate. A chain is not automatically a broadcast where every handler must run.

<!-- qard-id: ap-8bf4b73b8eaf94fc6add -->
> [!qard]- How do Mediator and Observer reduce different communication problems?
> Mediator coordinates interactions through a hub; Observer notifies subscribers of publisher changes. A mediator need not be the authoritative data model or a subscription broadcaster.

<!-- qard-id: ap-ee38e4a69e8a4bf69c54 -->
> [!qard]- Why must a Memento contain a trustworthy snapshot rather than just mutable aliases to current state?
> Later edits through shared references could change the supposed past state, defeating restore/undo. Preserve the intended snapshot independence.

<!-- qard-id: ap-82b5494358a7f4b2a887 -->
> [!qard]- What should a Template Method keep fixed while allowing hooks to vary?
> The valid algorithm skeleton/order and required shared work; only intended steps are customisable, preventing omitted essential operations.
