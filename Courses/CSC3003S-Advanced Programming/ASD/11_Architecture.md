---
tags:
  - advanced-programming
---

# Software Architecture And Architectural Patterns

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD11-Architecture.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD11-Architecture.pdf), Johan Bontes (slides modified from Prof. Edwin Blake), University of Cape Town, PDF pages 1–48  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: the architecture-centred approach, why architectural patterns help, the key patterns (layered, repository, client–server, pipe and filter, MVC), layered architectures in depth, realising non-functional requirements, and generic application architectures.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Architecture-Centred Approach|Architecture-Centred Approach]]
  - [[#From Analysis To Design|From Analysis To Design]]
  - [[#What A Software Architecture Is|What A Software Architecture Is]]
  - [[#Architectural Patterns: Encapsulated Experience|Architectural Patterns: Encapsulated Experience]]
  - [[#Layered Architecture Pattern|Layered Architecture Pattern]]
  - [[#Repository Pattern|Repository Pattern]]
  - [[#Client–Server Pattern|Client–Server Pattern]]
  - [[#Pipe And Filter Pattern|Pipe And Filter Pattern]]
  - [[#Cohesion And Coupling|Cohesion And Coupling]]
  - [[#Model–View–Controller (MVC)|Model–View–Controller (MVC)]]
  - [[#Layered Architectures In Depth|Layered Architectures In Depth]]
  - [[#Model–View Separation And Layer Benefits|Model–View Separation And Layer Benefits]]
  - [[#Layered Examples: Internet Stack And Web 2.0|Layered Examples: Internet Stack And Web 2.0]]
  - [[#Realising Non-Functional Requirements|Realising Non-Functional Requirements]]
  - [[#Purpose Of Architecture|Purpose Of Architecture]]
  - [[#Generic Application Architectures|Generic Application Architectures]]

---

## Core Content

### Architecture-Centred Approach

- The course emphasises design. Design pervades engineering and is an important part of computer science.
- Misreading Agile's lean documentation leads to **inadequate architectural design information**.

| Architecture decisions | Tactical decisions |
|---|---|
| **System-wide, strategic** | **Local, detailed** |
| Use object orientation; choose the overall architectural pattern; choose APIs | Use of design patterns, refactoring decisions, … |

### From Analysis To Design

Development alternates roles:

1. As **investigators**, learn about the problem (analysis).
2. As **designers**, build a working solution (design).
3. Go to 1.

| Analysis artefacts | Design artefacts |
|---|---|
| Use cases, system sequence diagrams, domain model | Architecture, interaction diagrams, class diagrams |

### What A Software Architecture Is

#### Definitions

> **Software architecture**: The large-scale "big ideas" of a system: its motivations, constraints, organisation, patterns, responsibilities and connections.

Architecture is especially concerned with **non-functional requirements**: ensuring they can be met, or suggesting trade-offs if they cannot (trends, cost, maintainability).

### Architectural Patterns: Encapsulated Experience

#### Definitions

> **Architectural pattern**: An architectural template encapsulating a proven basic approach to a recurring type of problem.

- Much of a programming style is how solutions are **structured**, not the small details. Reusing structure across projects gives all the benefits of reuse.
- Architecture never starts from a blank slate. New designs build on previous similar designs, like accountancy, where every factory uses the same procedures and blueprint.
- Well-structured OO systems contain recurring patterns of classes and objects. Knowing what worked before makes designers more productive and designs more flexible and reusable.

The benefits of patterns:

- they capture expertise and communicate it to non-experts
- they give developers a **common language**
- designs become more understandable and easier to modify
- good designs are easier to reuse, and non-reusable alternatives easier to avoid
- documentation improves: start system documentation with the UML design pattern

### Layered Architecture Pattern

| | Layered architecture |
|---|---|
| **Problem** | Building new facilities on top of existing systems; development spread across teams (one team per layer); multi-level security |
| **Solution** | Organise the system into layers of related functionality. Each layer provides services to the layer above; the lowest layers are core services used throughout. |
| **Pro** | A layer can be swapped for another with the same interface. Redundant facilities (e.g. authentication) in each layer increase dependability. |
| **Con** | Clean separation is often hard in practice; high layers may need to call low layers directly; multiple levels can be slow. |

![Layered architecture](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/layered.svg)

*UI (Swing, Web) calls the Domain (Sales, Payments, Taxes), which calls Technical Services (Persistence, Logging, RulesEngine).*

### Repository Pattern

| | Repository |
|---|---|
| **Problem** | Large volumes of information stored for a long time; data-driven systems where adding data triggers an action |
| **Solution** | Store all data in a central repository accessible to all components. Components interact **only** through the repository. |
| **Pro** | Components are independent; changes propagate to all components; data is managed in one place (e.g. single backups) |
| **Con** | The repository is a **single point of failure**; routing all traffic through it may be slow; distributing it is complex |

![Repository](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/repository.svg)

*Clients persist to and query the repository; they never talk to each other directly.*

### Client–Server Pattern

| | Client–server |
|---|---|
| **Problem** | Shared data accessed from many locations; servers must be replicable; load is variable |
| **Solution** | Organise functionality into services, each on a separate server; clients use these services |
| **Pro** | Servers can be distributed across a network and added or upgraded with little disruption; general functionality (e.g. printing) is available to all clients, which don't implement it themselves |
| **Con** | Each service is a single point of failure (denial-of-service, server failure); network performance may be unpredictable; management problems if servers belong to different organisations |

![Client–server film library](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/client-server.svg)

*Clients reach catalogue, video, picture and web servers over the Internet. Each server owns its own store.*

### Pipe And Filter Pattern

| | Pipe and filter |
|---|---|
| **Problem** | Data processing (batch or transaction) where inputs pass through stages to produce outputs |
| **Solution** | Each filter is discrete and performs one transformation; data flows through pipes from one to the next |
| **Pro** | Easy to understand; supports reuse of transformations; matches many business workflows; adding transformations is simple; can be sequential or concurrent |
| **Con** | The data format between stages must be standardised; each filter decodes and re-encodes, adding overhead; incompatible data structures prevent reuse |

![Pipe and filter](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/pipe-filter.svg)

*A document source is enriched, rendered to HTML, and displayed. Each pipe carries an agreed format.*

### Cohesion And Coupling

#### Definitions

> **Cohesion**: Communication **within** a module.

> **Coupling**: Communication **between** modules.

The key aim of these patterns is to **minimise coupling and maximise cohesion**.

### Model–View–Controller (MVC)

| | MVC |
|---|---|
| **Problem** | Many ways to view and interact with data, or future presentation and interaction are unknown |
| **Solution** | Separate presentation and interaction from data. The **Model** manages data and operations; the **View** manages presentation; the **Controller** handles user interaction (keys, clicks) and passes it to the View and Model. |
| **Pro** | Decouples data from representation; the same data can be shown in different ways |
| **Con** | Extra code and complexity for simple data models and interactions |

![MVC](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/mvc.svg)

*The controller calls model mutators. The model notifies all registered views, which query it to redraw.*

MVC is a special case of the **repository** architecture: the model is the central data store, and the controller explicitly dictates control flow.

| Component | Role | Java mechanism |
|---|---|---|
| **Model** | Carries out the task with no concern for look and feel; a purely functional public interface of **query** (get state) and **mutator** (modify state) methods; registers views and notifies them when state changes | Extends `java.util.Observable` (register/notify) |
| **View** | Provides the GUI; displays by querying the model; informs the controller when the user manipulates it | AWT/Swing; implements `java.util.Observer` |
| **Controller** | Linked to views; on user interaction calls model mutators; the model then notifies **all** registered views | Event listeners |

### Layered Architectures In Depth

#### Definitions

> **Layer**: A coarse-grained group of classes, subsystems or packages with cohesive responsibility for a major aspect of the system.

> **Strict layered architecture**: A layer uses only the layer directly below.

> **Relaxed layered architecture**: A layer may skip layers.

"Higher" layers call the services of "lower" layers. Typical OO layers are UI, then application logic and domain objects, then technical services (application-independent and reusable).

![Typical layer stack](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/layer-stack.svg)

*Upper layers are more application-specific. Lower layers are wider in applicability and are depended on by those above.*

In UML the logical partitioning is shown with **package diagrams**:

- UI packages: Summaries, Editors
- Domain packages: Core, Evaluation, Policies
- Services packages: Persistence, Logging, Reporting, Security

Packages group classes, other packages and use cases.

**Application coordination layer.** Consider a layer whose objects represent **use cases** and may hold session state, e.g. `RentingVideoUCHandler` and `PayingFinesUCHandler`. It sits between UI and Domain.

### Model–View Separation And Layer Benefits

#### Definitions

> **Model–view separation principle**: Model (domain-layer) objects must not know about View (UI) objects, and domain responsibilities must not be assigned to View objects.

- This gives better separation of concerns and lower coupling.
- An independent domain layer can be reused with another UI, e.g. application and web UIs over one domain.
- It supports multiple views of one model.

More benefits of layering:

- The system is easier to understand: each layer has a specific purpose.
- High cohesion within layers, low coupling between them.
- Changes do not ripple through the system; they stay within a layer.
- Low coupling makes it easy to swap a lower-layer technology, e.g. replace the database without rewriting application logic.
- Lower layers contain more reusable functionality.

### Layered Examples: Internet Stack And Web 2.0

| Layer | Protocols |
|---|---|
| Application / session / presentation | HTTP, FTP, DNS, SMTP, SSH, TLS/SSL |
| Transport | TCP, UDP |
| Network | IP (IPv4, IPv6) |
| (Data) link | PPP, MAC, FDDI |
| Physical | 10BASE-T, POTS, 802.11a/b/g/n |

RFC 1958 (1996): over 25 years the Internet grew by factors of 1000 (backbone speed) to 1 000 000 (hosts). "The principle of constant change is perhaps the only principle of the Internet that should survive indefinitely."

**Web 2.0 reference architecture**:

| Tier | Contents |
|---|---|
| Client application tier | The user's view of services: browsers, Flash, Acrobat, iTunes |
| Connectivity | Standards and protocols, e.g. XML over HTTP |
| Service tier | Packages resources as services and controls what goes in and out (SOAP, EJB, PHP, Rails, ASP) |
| Resource tier | Back-end capabilities (data or processing) |
| Tools (cross-cutting) | Design, development and governance tools (Dreamweaver, Xcode, IDEs) |

### Realising Non-Functional Requirements

| Requirement | Architectural tactic |
|---|---|
| **Performance** | Localise critical operations and minimise communication; use large rather than fine-grained components; allow concurrency |
| **Security** | A layered architecture with critical assets in the inner layers |
| **Safety** | Localise safety-critical features in a few subsystems |
| **Availability** | Redundant components and fault-tolerance mechanisms; replace components without stopping the system |
| **Maintainability** | Fine-grained, replaceable components; avoid global or shared data structures |

Some of these conflict: performance wants large components, maintainability fine-grained ones. Architecture is about trade-offs.

### Purpose Of Architecture

Before construction, the architecture:

- serves as a design plan for **negotiating requirements**
- structures discussions with clients, developers and managers
- is an essential tool for **complexity management**, hiding details so designers can focus on the key abstractions

### Generic Application Architectures

This is an alternative perspective: architectures by **application type**. The two fundamental business models are **batch** and **transaction** processing.

| Type | Description | Examples |
|---|---|---|
| **Data processing** | Data-driven; processes data in batches without user intervention | Billing, payroll |
| **Transaction processing** | Data-centred; processes user requests and updates a database | E-commerce, reservations |
| **Event processing** | Actions depend on interpreting events from the environment | Games, word processors, real-time systems |
| **Language processing** | User intentions are written in a formal language that the system processes | Compilers, command interpreters |

Many systems combine types.

![Application architectures](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/application-architectures.svg)

*Batch systems follow input → process → output. Compilers chain lexical, syntactic and semantic analysis into code generation, sharing a symbol table and syntax tree.*

**Data processing (input–process–output)**:

1. **Input** reads data from a file or database, validates it, and queues valid data.
2. **Process** takes a transaction from the queue, computes, and creates a result record.
3. **Output** formats the records and writes them to the database or a printer.

**Transaction processing.** To the user, a transaction is any coherent sequence of operations that satisfies a goal, e.g. "find the times of flights from London to Paris". Users make **asynchronous** requests that a **transaction manager** processes against the database, letting many users access and modify it remotely.

**Event processing: an editing system**, which is naturally object-oriented:

| Component | Responsibility |
|---|---|
| Screen | Monitors screen memory and detects events |
| Event | Recognises events and passes them on for processing |
| Command | Executes a user command |
| Editor data | Manages the editor's data structure |
| Ancillary data | Manages other data, such as styles and preferences |
| File system | Manages file I/O |
| Display | Updates the screen display |

User-interface events are detected and an in-memory data structure is modified.

**Language processing: a compiler.** Lexical analysis → syntactic analysis (builds the abstract syntax tree) → semantic analysis → code generation, all using the symbol table. Compilers translate source into another language (e.g. assembler), and interpreters execute the instructions directly.
