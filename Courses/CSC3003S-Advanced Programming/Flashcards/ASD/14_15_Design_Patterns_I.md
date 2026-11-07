---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 14–15 — Design Patterns I"
---

# ASD 14–15 — Design Patterns I

**Source note:** [Design Patterns I: GoF Patterns And Lambdas](../../ASD/14_15_Design_Patterns_I.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Patterns And Lambdas|Patterns And Lambdas]]
  - [[#Creational|Creational]]
  - [[#Structural|Structural]]
  - [[#Behavioural|Behavioural]]

## Core Content

### Patterns And Lambdas

<!-- qard-id: ap-9fc9baad602faff321d7 -->
> [!qard]- What is a design pattern?
> A reusable solution to a common design problem, capturing experience for reuse.

<!-- qard-id: ap-fc4cd152f8413f5b03d8 -->
> [!qard]- What made many design patterns obsolete?
> Lambdas (first-class functions) in modern languages.

<!-- qard-id: ap-953122e7324db5ceede1 -->
> [!qard]- What is a lambda capture?
> A variable from the enclosing scope stored inside the lambda — by value `[=]` or by reference `[&]` in C++.

<!-- qard-id: ap-7287282030c11ea4bfae -->
> [!qard]- How are Java lambdas limited compared with C++?
> Java captures are effectively const; C++ can capture by reference and modify outside variables.

<!-- qard-id: ap-591f74c3bb1edccd69ca -->
> [!qard]- How is a capturing lambda implemented internally?
> As a hidden class whose captures are member fields and whose body is a method.

<!-- qard-id: ap-8481df8d14ced8d02132 -->
> [!qard]- Name the three GoF pattern classes and their purpose.
> Creational (object creation), structural (assembling objects into structures), behavioural (communication between objects).

### Creational

<!-- qard-id: ap-4288d52d783f6c04f943 -->
> [!qard]- What is the factory method and why is it needed in Java/C++?
> Keeps construction logic in one place to create the right subclass; needed because these languages have no virtual constructors.

<!-- qard-id: ap-c0146b07fd04d99150ea -->
> [!qard]- What is the prototype pattern?
> Creating objects by cloning an existing one (`object.clone()`).

<!-- qard-id: ap-f407b70dbca09dfa6368 -->
> [!qard]- What is a singleton, and when is it appropriate?
> A class with exactly one global instance; appropriate for logging or database connections.

<!-- qard-id: ap-2bd38ca2edfe3f663bd7 -->
> [!qard]- Why is the singleton often an antipattern?
> Global state, hidden dependencies and tight coupling, hard testing, and a tendency to become a god object.

### Structural

<!-- qard-id: ap-216eda7a3f125dfabda1 -->
> [!qard]- What does Adapter do?
> Converts one interface to another so incompatible objects can work together.

<!-- qard-id: ap-838a01e0555ff9de42ee -->
> [!qard]- What does Bridge do?
> Uses composition instead of inheritance to avoid combinatorial class explosion ($10\times10$ classes become $10+10$).

<!-- qard-id: ap-a755588a11e5bd61b315 -->
> [!qard]- What does Decorator do?
> Wraps an object in objects with the same interface to add behaviours that can be stacked.

<!-- qard-id: ap-9ace66b468ebab16fadf -->
> [!qard]- What does Facade do?
> Provides a simple interface in front of a complex subsystem.

<!-- qard-id: ap-535ded072231309a6e29 -->
> [!qard]- What does Composite do?
> Treats containers and their parts uniformly in a tree, processing recursively.

<!-- qard-id: ap-dc05a8c0fdef1346dadd -->
> [!qard]- What does Flyweight do, and why do games avoid it?
> Shares repeated data between many objects. Games use DOD instead — flyweight is pointer-chasing AoS, while SoA gives linear access.

<!-- qard-id: ap-f02d9bb8e0cbfa238fb8 -->
> [!qard]- What does Proxy do?
> Acts as a gatekeeper or cache in front of another object or slow resource.

### Behavioural

<!-- qard-id: ap-9997d44732c86d4519dc -->
> [!qard]- What is chain of responsibility?
> Passing a request along handlers, each processing it and passing it on or dropping it.

<!-- qard-id: ap-e7f700d761ce300c3d96 -->
> [!qard]- What does the Command pattern solve, and how do lambdas replace it?
> Separates actions from UI controls (avoiding a class per button); a stored lambda per action does this directly.

<!-- qard-id: ap-1dba83ff26842b3dec49 -->
> [!qard]- What does Iterator provide?
> Visiting every element via first/next/current — built into modern `for-in` loops.

<!-- qard-id: ap-4c4cc079b438e00c21e5 -->
> [!qard]- What is the Mediator pattern?
> A central hub that components communicate through instead of directly, reducing cross-talk.

<!-- qard-id: ap-5dba69c3a86e458c6365 -->
> [!qard]- Describe the roles in the Memento pattern.
> The originator creates and restores its own snapshots; the memento holds state plus metadata; the caretaker stores snapshots.

<!-- qard-id: ap-b7fd5061f619ac9e1a62 -->
> [!qard]- What are Memento's uses and drawbacks?
> Uses: undo, transactions, saving. Drawbacks: RAM-heavy with many snapshots, needs immutable objects.

<!-- qard-id: ap-e17ff0eb0c90a1ffb174 -->
> [!qard]- What is the Observer pattern?
> Subscribers register with a publisher, which notifies all of them when its state changes.

<!-- qard-id: ap-172bb0f48760d35c8745 -->
> [!qard]- What is the State pattern and its pros?
> One class per state with the master delegating to the current state. Pros: SRP, OCP, no big switch (overkill for few states).

<!-- qard-id: ap-4641dcf7539f68e1c8d5 -->
> [!qard]- What is Template Method?
> The base class fixes an algorithm's steps; subclasses override only the varying steps.
