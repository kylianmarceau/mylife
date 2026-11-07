---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 12 — Antipatterns"
---

# ASD 12 — Antipatterns

**Source note:** [Antipatterns](../../ASD/12_Antipatterns.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Antipatterns|Antipatterns]]
  - [[#Generic|Generic]]
  - [[#Object-Oriented|Object-Oriented]]
  - [[#Programming|Programming]]
  - [[#Methodological|Methodological]]

## Core Content

### Antipatterns

<!-- qard-id: ap-521a603b3d22d9e7f62e -->
> [!qard]- What is an antipattern?
> A common solution to a problem that is likely to be counterproductive (Koenig, 1995).

### Generic

<!-- qard-id: ap-57fa4bbb7113ee0bc602 -->
> [!qard]- What is abstraction inversion and its fix?
> Users re-implement hidden low-level functions via the public interface, so low-level features depend on high-level ones. Fix: keep dependencies acyclic.

<!-- qard-id: ap-4ce644fb8382d5783e5c -->
> [!qard]- What is a big ball of mud and its fix?
> Unstructured spaghetti code understandable only as one unit. Fix: design/architecture patterns and decomposition.

<!-- qard-id: ap-c794d0636b7acfb6dd3e -->
> [!qard]- What is the inner-platform effect?
> Turning an application into its own programming language for customisability — complex and a security nightmare.

<!-- qard-id: ap-fa8ed27856787742f44d -->
> [!qard]- What is a stovepipe system?
> A one-off system with narrow focus whose data can't be shared, built without architecture. Fix: use standard components.

<!-- qard-id: ap-26b7f7ea1c04c1fff495 -->
> [!qard]- What causes data races, and how are they mitigated?
> Unsynchronised concurrent access in multi-threaded code. Simplify threading, use MPI or proven components.

### Object-Oriented

<!-- qard-id: ap-aad860a242f30d95241d -->
> [!qard]- What is the circle–ellipse problem and its fix?
> Something looks IS-A but has different invariants, so inheritance violates Liskov. Fix: use a mixin, not inheritance.

<!-- qard-id: ap-20e191bb2deb359353cc -->
> [!qard]- What is a god object and its fix?
> One class doing everything for "easy" communication. Fix: a proper hierarchy and patterns for communication.

<!-- qard-id: ap-563b5f586a711185e4d6 -->
> [!qard]- What is sequential (temporal) coupling and its fix?
> Methods must be called in a set order (e.g. `init`). Fix: call earlier steps automatically, or use Template Method.

<!-- qard-id: ap-9b75e7c1e844e88beb11 -->
> [!qard]- What is the call-super antipattern and its fix?
> Subclasses must remember to call the parent method. Fix: Template Method.

<!-- qard-id: ap-fcdedf1160abc6ea3c2c -->
> [!qard]- What is an object orgy?
> Making everything public to gain access, breaking encapsulation and bloating interfaces.

<!-- qard-id: ap-9c171280d4eae31f9dd1 -->
> [!qard]- How should circular class dependencies be fixed?
> With design patterns such as Observer.

### Programming

<!-- qard-id: ap-d6ac836d38c41cc06da5 -->
> [!qard]- What is cargo cult programming?
> Using patterns or paradigms without understanding them.

<!-- qard-id: ap-6542512b3b766f087c92 -->
> [!qard]- What is coding by exception?
> Using exceptions for normal control flow — slow, hard to follow and can hide errors.

<!-- qard-id: ap-762d8288bcc33ecf47e1 -->
> [!qard]- What is shotgun surgery and its fix?
> One change requires edits in many places. Fix: refactor, or aspect-oriented programming.

<!-- qard-id: ap-4ec8d327ccdde203ab5c -->
> [!qard]- What is error hiding and its fix?
> Silently swallowing exceptions. Fix: fix the source; only handle understood or external errors.

### Methodological

<!-- qard-id: ap-316a1cb6c9d2b842b405 -->
> [!qard]- What is copy-paste programming?
> Pasting code (from Stack Overflow or elsewhere) without understanding it, creating non-DRY code with hidden assumptions.

<!-- qard-id: ap-0674bf7068b0e76c9ef3 -->
> [!qard]- What is premature optimisation and its fix?
> Clever "fast" code before knowing it's needed. Fix: pick a good algorithm, write straightforward code, profile and optimise only hot spots.

<!-- qard-id: ap-ab1f51edf603ace25597 -->
> [!qard]- What did Knuth say about premature optimisation?
> It's the root of all evil about 97% of the time — but don't pass up the critical 3%.

<!-- qard-id: ap-9598c968320c655f245c -->
> [!qard]- What is reinventing the (square) wheel?
> Assuming your problem is novel and building a custom solution instead of using a standard one.
