---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 13 — SOLID Design Principles"
---

# ASD 13 — SOLID Design Principles

**Source note:** [SOLID Design Principles](../../ASD/13_SOLID.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#SOLID|SOLID]]
  - [[#Single Responsibility|Single Responsibility]]
  - [[#Open–Closed|Open–Closed]]
  - [[#Liskov Substitution|Liskov Substitution]]
  - [[#Interface Segregation|Interface Segregation]]
  - [[#Dependency Inversion|Dependency Inversion]]

## Core Content

### SOLID

<!-- qard-id: ap-a8f61dfb16ebe09cab59 -->
> [!qard]- What does SOLID stand for?
> Single responsibility, Open–closed, Liskov substitution, Interface segregation, Dependency inversion.

### Single Responsibility

<!-- qard-id: ap-b21d9bd21afbcf3c012e -->
> [!qard]- State the single responsibility principle.
> A class should have only one reason to change.

<!-- qard-id: ap-f794d7fd861bb63018d6 -->
> [!qard]- What counts as a responsibility?
> A reason for change.

<!-- qard-id: ap-3f396f4f98a3b9eb2b09 -->
> [!qard]- Why does a `Rectangle` with `draw()` and `area()` violate SRP?
> Drawing and geometry change for different reasons, entangling two applications; split into `GeometricRect` and `Rectangle`.

<!-- qard-id: ap-d6889624e04982ca5d28 -->
> [!qard]- How should a `Modem` interface be split under SRP?
> Into connection control (`dial`, `hangup`) and data control (`send`, `receive`).

<!-- qard-id: ap-53dc7c30913c874ed740 -->
> [!qard]- Which older principles does SRP combine?
> Decomposition (Parnas), separation of concerns (Dijkstra), coupling and cohesion (Constantine).

### Open–Closed

<!-- qard-id: ap-4ad0d600f059ca19c828 -->
> [!qard]- State the open–closed principle.
> Modules should be open for extension but closed for modification (Meyer).

<!-- qard-id: ap-f4b1c7168db37d2fea61 -->
> [!qard]- Is fixing a bug a modification under OCP?
> No — bug fixes are allowed.

<!-- qard-id: ap-b82618e1a78b62cb628d -->
> [!qard]- Name three mechanisms for extension without modification.
> Class inheritance, interface inheritance (virtual methods), message handlers.

<!-- qard-id: ap-13d687015f9b71bbb82a -->
> [!qard]- Why prefer pure interfaces over polymorphic class inheritance?
> Overriding concrete virtual methods is an antipattern; interfaces carry no implementation to break.

### Liskov Substitution

<!-- qard-id: ap-468c5eabd0bf904323d4 -->
> [!qard]- State the Liskov substitution principle.
> Code using a base type must work with any subtype without knowing it.

<!-- qard-id: ap-963ee293a25d0180f10f -->
> [!qard]- Why does checking `typeid` in `DrawShape` violate LSP?
> The function must know every subtype, breaking when new types are added or RTTI is off.

<!-- qard-id: ap-64e4701d371116459615 -->
> [!qard]- Why isn't a `Square` a `Rectangle` in code?
> Setting width then height breaks a square's invariant, so code relying on rectangle behaviour fails.

<!-- qard-id: ap-13cc5646e6fb7727d822 -->
> [!qard]- When should inheritance be used, per LSP?
> Only for pure IS-A relationships (rare outside UIs); otherwise interfaces, and composition for HAS-A.

<!-- qard-id: ap-e138d7d55a35ea4a917b -->
> [!qard]- How does design by contract support LSP?
> Pre- and post-conditions state each method's promises; subtypes must honour them.

<!-- qard-id: ap-515b38732fe0e66a87e4 -->
> [!qard]- Contract violations versus errors?
> Contract violations can't be recovered from; errors can be handled with fallbacks.

<!-- qard-id: ap-88f801053f19c4e3fcb7 -->
> [!qard]- What three detection rules identify a god class?
> It uses many attributes of other classes directly, has very high complexity, and has low cohesion.

### Interface Segregation

<!-- qard-id: ap-34f8f86118be3245f99e -->
> [!qard]- State the interface segregation principle.
> Clients shouldn't be forced to depend on interfaces they don't use.

<!-- qard-id: ap-b6a625325dbd26c717e8 -->
> [!qard]- Why shouldn't `Door` implement `ITimerClient`?
> Every door would depend on the timer interface and change when it changes.

<!-- qard-id: ap-c0d9247c3dd003ab0c19 -->
> [!qard]- How is a timed door built with single inheritance?
> `TimedDoor` implements `IDoor` and delegates timer callbacks to an adapter (Adapter pattern).

<!-- qard-id: ap-6b863545e382fd7139f0 -->
> [!qard]- How does ISP apply to an ATM?
> Split the fat UI into deposit, withdrawal and transfer UIs, so each transaction depends only on its own.

### Dependency Inversion

<!-- qard-id: ap-cd80b84f55c75c1ccb33 -->
> [!qard]- State the dependency inversion principle.
> High-level modules shouldn't depend on low-level ones; both should depend on abstractions, and details on abstractions.

<!-- qard-id: ap-da388d1c03ce0e21de95 -->
> [!qard]- How does DIP fix a `Copy` routine tied to keyboard and printer?
> Make `Copy` use `Reader` and `Writer` interfaces, so any device can be plugged in.

<!-- qard-id: ap-7346dfd1443ae76259dc -->
> [!qard]- Why is it called "inversion"?
> Traditional design has policy depending on details; DIP reverses the arrows so details depend on abstractions, making high-level modules reusable.
