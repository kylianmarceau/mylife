---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 11 — Software Architecture And Architectural Patterns"
---

# ASD 11 — Software Architecture And Architectural Patterns

**Source note:** [Software Architecture And Architectural Patterns](../../ASD/11_Architecture.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Architecture|Architecture]]
  - [[#Patterns|Patterns]]
  - [[#Layering|Layering]]
  - [[#Non-Functional Requirements And Applications|Non-Functional Requirements And Applications]]

## Core Content

### Architecture

<!-- qard-id: ap-2a1530566a213b548ee9 -->
> [!qard]- What is software architecture?
> The large-scale structure of a system — its motivations, constraints, organisation, patterns, responsibilities and connections.

<!-- qard-id: ap-9a8777a9c866582adcd7 -->
> [!qard]- Architectural versus tactical decisions?
> Architectural decisions are system-wide and strategic (paradigm, overall pattern, APIs); tactical ones are local (design patterns, refactoring).

<!-- qard-id: ap-6a0c6520cddf30daa1af -->
> [!qard]- Why does architecture care about non-functional requirements?
> It must ensure they can be met, or propose trade-offs.

<!-- qard-id: ap-b17bf9b8519f0bbd5aac -->
> [!qard]- What is an architectural pattern?
> A reusable template for overall system structure, encapsulating experience with a class of problems.

<!-- qard-id: ap-77477f99c1e6f954f1f4 -->
> [!qard]- Name four benefits of architectural patterns.
> Communicate expertise, common vocabulary, easier reuse and modification, better documentation.

<!-- qard-id: ap-07aa2e63ee34d9d77d3e -->
> [!qard]- What is the key aim of cohesion and coupling?
> Maximise cohesion (within modules) and minimise coupling (between modules).

### Patterns

<!-- qard-id: ap-31523d4cbf98fccff130 -->
> [!qard]- Describe the layered architecture and its pros and cons.
> Layers of related functionality, each serving the one above. Pros: swappable layers, per-layer security. Cons: clean separation is hard; many levels can be slow.

<!-- qard-id: ap-d3dca39379e8f89e566d -->
> [!qard]- Describe the repository pattern and its pros and cons.
> All components share a central data store and interact only through it. Pros: independent components, one place for data. Cons: single point of failure, possible bottleneck.

<!-- qard-id: ap-8fd2ccc341ecf2d5337d -->
> [!qard]- Describe the client–server pattern and its pros and cons.
> Functionality split into services on separate servers used by clients. Pros: distributed, upgradable, shared services. Cons: each server is a point of failure; network-dependent performance.

<!-- qard-id: ap-c7d2604624a3b86f18b0 -->
> [!qard]- Describe pipe and filter and its pros and cons.
> Filters each transform data, connected by pipes. Pros: simple, reusable, matches workflows. Cons: needs a standard data format; encode/decode overhead.

<!-- qard-id: ap-f0a8b1d6e679f8bf7300 -->
> [!qard]- What problem does MVC solve?
> Multiple or unknown ways of presenting and interacting with the same data.

<!-- qard-id: ap-9598278d7e9dbb447241 -->
> [!qard]- What do the Model, View and Controller do?
> Model: data and operations. View: presentation. Controller: maps user actions to model operations.

<!-- qard-id: ap-718340ede1f7a44beb60 -->
> [!qard]- Describe the MVC update cycle.
> User acts on a view; the controller calls a model mutator; the model notifies all registered views; views query the model and redraw.

<!-- qard-id: ap-24bf77ddc248f005ca00 -->
> [!qard]- MVC is a special case of which architecture?
> Repository — the model is the central store.

### Layering

<!-- qard-id: ap-61f7ef8c492ef0a96dd0 -->
> [!qard]- Strict versus relaxed layering?
> Strict: a layer uses only the one directly below. Relaxed: it may skip layers.

<!-- qard-id: ap-3a79085a2fd8c4c49766 -->
> [!qard]- List typical layers from top to bottom.
> UI, application, domain, business infrastructure, technical services, foundation.

<!-- qard-id: ap-17ff102852562f23ed34 -->
> [!qard]- What is the model–view separation principle?
> Domain objects must not know about UI objects, and domain logic must not live in the UI.

<!-- qard-id: ap-6d33d38491ef17b35183 -->
> [!qard]- Give three benefits of layered architecture.
> Easier comprehension, changes confined to one layer, easily swapped lower layers (e.g. replace the database).

### Non-Functional Requirements And Applications

<!-- qard-id: ap-7d5e58b15fac0c2a68f2 -->
> [!qard]- How should architecture support performance and security?
> Performance: localise critical operations, use large components, allow concurrency. Security: critical assets in inner layers.

<!-- qard-id: ap-814c5d6c405f34ad3da8 -->
> [!qard]- How should architecture support availability and maintainability?
> Availability: redundancy and hot-swappable components. Maintainability: fine-grained replaceable components, no shared global data.

<!-- qard-id: ap-b40416d75e882525de87 -->
> [!qard]- Name the four generic application types.
> Data processing (batch), transaction processing, event processing, language processing.

<!-- qard-id: ap-20b43554eb634d2747fb -->
> [!qard]- What is the structure of a data processing (batch) system?
> Input (validate and queue) → process → output.

<!-- qard-id: ap-78af288f44c294fea4e1 -->
> [!qard]- What are the stages of a compiler?
> Lexical analysis, syntax analysis (AST), semantic analysis, code generation, sharing a symbol table.
