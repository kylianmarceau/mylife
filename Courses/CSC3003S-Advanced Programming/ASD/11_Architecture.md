---
tags:
  - advanced-programming
---

# Software Architecture And Architectural Patterns

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD11-Architecture.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD11-Architecture.pdf), Johan Bontes (slides modified from Prof. Edwin Blake), University of Cape Town, pages 1–48
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> The architecture-centred approach, why patterns encapsulate experience, the key architectural patterns (layered, repository, client–server, pipe and filter, MVC), multi-tier layered architectures, realising non-functional requirements, and generic application architectures.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Architecture-Centred Approach|The Architecture-Centred Approach]]
  - [[#What Software Architecture Is|What Software Architecture Is]]
  - [[#Patterns Are Encapsulated Experience|Patterns Are Encapsulated Experience]]
  - [[#Layered Architecture Pattern|Layered Architecture Pattern]]
  - [[#Repository Pattern|Repository Pattern]]
  - [[#Client–Server Pattern|Client–Server Pattern]]
  - [[#Pipe And Filter Pattern|Pipe And Filter Pattern]]
  - [[#Cohesion And Coupling|Cohesion And Coupling]]
  - [[#Model-View-Controller|Model-View-Controller]]
  - [[#MVC Components In Detail|MVC Components In Detail]]
  - [[#Multi-Tier Layered Architectures|Multi-Tier Layered Architectures]]
  - [[#Application Coordination And Model-View Separation|Application Coordination And Model-View Separation]]
  - [[#Benefits Of Layering And Real-World Stacks|Benefits Of Layering And Real-World Stacks]]
  - [[#Realising Non-Functional Requirements|Realising Non-Functional Requirements]]
  - [[#Application Architectures|Application Architectures]]

---

## Core Content

### The Architecture-Centred Approach

- This approach emphasises **design**, which pervades engineering activities and is an important part of computer science.
- Misreading Agile's lean documentation leads to **inadequate architectural design information**.
- **Architectural decisions are system-wide and strategic**: use object orientation, choose the overall architectural pattern, choose APIs.
- **Tactical decisions are local and detailed**: use of design patterns, refactoring decisions, etc.

Requirements and analysis lead to design, in a loop:

1. We are investigators learning about a problem (analysis: use cases, system sequence diagrams, domain model).
2. We change roles and become designers making a working solution (design: architecture, interaction diagrams, class diagrams).
3. Go to 1.

### What Software Architecture Is

#### Definitions

> **Software architecture**: The large-scale, big ideas of a system — its motivations, constraints, organisation, patterns, responsibilities and connections.

Architecture is very concerned with **non-functional requirements**: ensuring they can be met, or, if not, suggesting trade-offs (e.g. trends, cost, maintainability).

### Patterns Are Encapsulated Experience

#### Definitions

> **Architectural pattern**: A reusable template for the overall structure of a system that encapsulates the basic approach to a class of similar problems.

- Much of your programming style is the way you **structure** solutions, not the minute details of code. Reusing structure across projects gives all the benefits of reuse.
- Architecture never starts from an empty slate: new designs build on previous similar ones. The IT community has many past solutions, but has made little progress documenting the experience — architectural templates describe it best.
- Like accountancy: every factory follows the same procedures, the same blueprint.

Aims:

- Enhance the reusability of object-oriented code — well-structured OO systems have recurring patterns of classes and objects.
- Knowing what worked before makes designers more productive and designs more flexible and reusable.

Benefits of architectural patterns:

| Benefit |
|---|
| Capture expertise and communicate it to non-experts |
| A common language among developers |
| Better design understandability |
| Easier reuse of good designs; avoid non-reusable alternatives |
| Easier design modification |
| Better documentation — start system documentation with a UML design pattern |

### Layered Architecture Pattern

| Field | Content |
|---|---|
| **Problem** | Building new facilities on top of existing systems; development spread across teams (one team per layer); multi-level security needed |
| **Solution** | Organise the system into layers of related functionality. Each layer provides services to the layer above. The lowest layers are core services used throughout the system |
| **Pros** | A layer can be swapped for another with the same interface. Redundant facilities (e.g. authentication) can be provided in each layer for dependability |
| **Cons** | Clean separation between layers is hard in practice; high layers may need to talk directly to low ones. Multiple levels can make it slow |

![Layered architecture](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/layered.svg)

*UI (Swing, Web) sits on the domain (Sales, Payments, Taxes), which sits on technical services (Persistence, Logging, RulesEngine).*

### Repository Pattern

| Field | Content |
|---|---|
| **Problem** | Large volumes of information must be stored for a long time; or a data-driven system where adding data triggers an action or tool |
| **Solution** | Store all data in a central repository accessible to all components; components interact **only** through the repository |
| **Pros** | Components are independent. A change by one component propagates to all. All data is managed in one place (e.g. one backup) |
| **Cons** | The repository is a **single point of failure**. Routing all traffic through it may be slow. Distributing it across machines is complex |

![Repository pattern](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/repository.svg)

*Clients' business logic persists to and queries a shared repository rather than talking to each other.*

### Client–Server Pattern

| Field | Content |
|---|---|
| **Problem** | Shared-database data must be accessed from many locations; servers must be replicable; load is variable |
| **Solution** | Organise functionality into services, each on a separate server. Clients use the services |
| **Pros** | Servers can be distributed across a network and added or upgraded with minimal disruption. General functionality (e.g. printing) is available to all clients, which don't implement it |
| **Cons** | Each service is a single point of failure (denial-of-service or server failure). Performance may be unpredictable (network). Management problems if servers belong to different organisations |

![Client-server film library](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/client-server.svg)

*Clients 1…n reach catalogue, video, picture and web servers over the Internet; each server owns its store.*

### Pipe And Filter Pattern

#### Definitions

> **Filter**: A discrete processing component that performs one type of data transformation.

> **Pipe**: The connection through which data flows from one filter to the next.

| Field | Content |
|---|---|
| **Problem** | Data processing (batch or transaction) where inputs are processed in stages to produce related outputs |
| **Solution** | Each filter performs one transformation; data flows through pipes from component to component |
| **Pros** | Easy to understand; supports transformation reuse; workflow style matches many business processes; adding transformations is simple; can be sequential or concurrent |
| **Cons** | The data format between transformations must be standardised, so each filter decodes input and encodes output — extra overhead. Transformations with incompatible data structures can't be reused |

![Pipe and filter](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/pipe-filter.svg)

*Source → Filter 1 → Filter 2 → Sink, e.g. Document (XML) → Enrich (internal XML) → Generate (HTML) → Display.*

### Cohesion And Coupling

#### Definitions

> **Cohesion**: Communication **within** a module — how strongly its parts belong together.

> **Coupling**: Communication **between** modules — how strongly they depend on each other.

The key aim of all these patterns: **minimise coupling and maximise cohesion**.

### Model-View-Controller

| Field | Content |
|---|---|
| **Problem** | Multiple ways to view and interact with data; or future interaction and presentation are unknown |
| **Solution** | Separate presentation and interaction from the data, using three interacting components |
| **Pros** | Decouples data from its representation; the same data can be shown in different ways |
| **Cons** | Extra code and complexity when the data model and interactions are simple |

| Component | Role |
|---|---|
| **Model** | Manages the system data and operations — the representation of the application |
| **View** | Defines and manages presentation — how information is displayed |
| **Controller** | Manages user interaction (key presses, mouse clicks) — maps user actions to operations on the model, passing them to the view and model |

![Model-View-Controller](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/mvc.svg)

*The controller initiates changes in the model; the model notifies its subscribed views, which redraw by querying it.*

MVC is a special case of the repository architecture: the model implements the central data store, and the controller explicitly dictates control flow.

### MVC Components In Detail

**Model**:

- Carries out some task, with no concern for "look and feel".
- Has a purely functional public interface: **query methods** (get current state) and **mutator methods** (modify state).
- Lets views **register** and **notifies** registered views when its state changes. In Java: a class extending `java.util.Observable`, whose superclass provides register/notify.

**View**:

- Provides the GUI for a model and displays it by querying the model.
- When the user manipulates the view, it informs the controller.
- In Java: built with AWT or Swing; implements `java.util.Observer`.

**Controller**:

- Views link to (possibly multiple) controllers.
- When the user interacts with a linked view, the controller calls the model's mutator methods.
- The model then notifies **all** registered views, which update the display.
- In Java: controllers are event listeners.

Sequence for one user action:

1. The user manipulates a view.
2. The view informs its controller.
3. The controller calls a model mutator.
4. The model notifies all registered views.
5. Each view queries the model and redraws.

### Multi-Tier Layered Architectures

Advice: separate presentation from application logic and other concerns.

#### Definitions

> **Layer**: A coarse-grained group of classes, subsystems or packages with cohesive responsibility for a major aspect of the system. Higher layers call the services of lower layers.

> **Strict layered architecture**: Each layer uses only the layer directly below it.

> **Relaxed layered architecture**: A layer may skip layers below it.

Typical layers, from most application-specific to most general (lower layers are wider, i.e. more widely applicable):

| Layer | Also called | Contents |
|---|---|---|
| UI | Presentation, View | GUI windows, reports, speech interface; HTML, XML, XSLT, JSP, JavaScript |
| Application | Workflow, Process, Mediation, Controller | Handles presentation requests; workflow; session state; window/page transitions; consolidating data for presentation |
| Domain | Business, Application logic, Model | Handles application requests; domain rules; domain services (POS, inventory), possibly shared by several applications |
| Business infrastructure | Low-level business services | Very general business services used in many domains, e.g. `CurrencyConverter` |
| Technical services | Technical infrastructure, high-level technical services | Relatively high-level services and frameworks: persistence, security |
| Foundation | Core/base services, low-level infrastructure | Data structures, threads, maths, file, DB and network I/O |

![Typical layers](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/layer-stack.svg)

*Dependencies point downward; lower layers are more general and more reusable.*

In UML, logical partitioning is shown with **package diagrams**, e.g. a UI package (Summaries, Editors), a Domain package (Core, Evaluation, Policies) and a Services package (Persistence, Logging, Reporting, Security). Packages can group classes, other packages, use cases, etc.

### Application Coordination And Model-View Separation

**Application coordination layer**: consider a layer whose objects represent **use cases** (e.g. `RentingVideoUCHandler`, `PayingFinesUCHandler`) and may hold session state. It sits between the UI and the domain.

#### Definitions

> **Model-view separation principle**: Model (domain-layer) objects must not know about view (UI-layer) objects, and domain responsibilities must not be given to view objects.

Benefits:

- better separation of concerns and lower coupling;
- the domain layer can be reused with another UI;
- multiple views of one model become easy (e.g. desktop and web UIs for the same application).

### Benefits Of Layering And Real-World Stacks

- The system is easier to comprehend: each layer has a specific purpose.
- High cohesion within layers, low coupling between them.
- Source changes don't ripple through the system; they stay within a layer.
- Low coupling makes it easy to swap a lower-layer service for another technology — e.g. replace the database without rewriting application logic.
- Lower layers contain more reusable functionality.

**Internet stack (TCP/IP model)**:

| Layer | Examples |
|---|---|
| Application (incl. presentation, session) | HTTP, FTP, DNS, SMTP, SSH, TLS/SSL |
| Transport | TCP, UDP |
| Network | IP (IPv4, IPv6) |
| (Data) link | PPP, MAC, FDDI |
| Physical | 10BASE-T, POTS, 802.11a/b/g/n |

RFC 1958 (1996): over 25 years the Internet grew by factors of 1000 (backbone speed) to 1 000 000 (hosts), so "the principle of constant change is perhaps the only principle of the Internet that should survive indefinitely."

**Web 2.0 reference architecture**:

| Tier | Role | Examples |
|---|---|---|
| Client application tier | User's view of services | Web browsers, Flash, Acrobat, iTunes |
| Connectivity | Means of reaching services | XML over HTTP |
| Service tier | Packages resources as services and controls what goes in and out | Application servers: SOAP, EJB, PHP, Rails, ASP |
| Resource tier | Back-end data or processing capabilities | Databases, back-end systems |
| Design, development and governance tools | Building the web apps | Dreamweaver, Xcode, DashCode, IDEs |

### Realising Non-Functional Requirements

| Requirement | Architectural approach |
|---|---|
| **Performance** | Localise critical operations and minimise communication; use large rather than fine-grained components; allow for concurrency |
| **Security** | Use a layered architecture with critical assets in the inner layers |
| **Safety** | Localise safety-critical features in a small number of subsystems |
| **Availability** | Include redundant components and fault-tolerance mechanisms; allow components to be replaced without stopping the system |
| **Maintainability** | Use fine-grained, replaceable components; avoid global/shared data structures |

Note the conflicts: performance wants large components, maintainability wants fine-grained ones.

Architecture also serves **beforehand**:

- as a design plan for negotiating system requirements;
- to structure discussions with clients, developers and managers;
- as an essential complexity-management tool that hides details so designers can focus on key abstractions.

### Application Architectures

So far architecture was viewed through control, distribution and structure. An alternative is the **application perspective**: generic models of application types help us understand and compare applications.

![Application architectures](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/11_Architecture/application-architectures.svg)

*Four generic application types, each with a characteristic structure.*

| Type | Description | Examples |
|---|---|---|
| **Data processing** | Data-driven; processes data in **batches** without user intervention | Billing, payroll |
| **Transaction processing** | Data-centred; processes user requests and updates a database | E-commerce, reservations |
| **Event processing** | Actions depend on interpreting events from the environment | Games, word processors, real-time systems |
| **Language processing** | User intentions are written in a formal language that the system processes and interprets | Compilers, command interpreters |

Real applications may combine types.

**Data processing (input–process–output)**:

1. **Input** reads data from a file or database, checks validity and queues valid data.
2. **Process** takes a transaction from the queue, computes, and creates a new result record.
3. **Output** reads the records, formats them and writes them to the database or a printer.

**Transaction processing**: processes user requests for information from, or updates to, a database. To a user, a transaction is any coherent sequence of operations that satisfies a goal (e.g. "find flight times from London to Paris"). Users make asynchronous requests that a **transaction manager** processes. Information can be accessed and modified remotely by many users.

**Event processing — editing systems** are naturally object-oriented:

| Component | Role |
|---|---|
| Screen | Monitors screen memory and detects events |
| Event | Recognises events and passes them on for processing |
| Command | Executes a user command |
| Editor data | Manages the editor data structure |
| Ancillary data | Manages other data, such as styles and preferences |
| File system | Manages file I/O |
| Display | Updates the screen display |

User-interface events are detected and an in-memory data structure is modified.

**Language processing — compilers** translate source code into another language (e.g. assembler) and may interpret the instructions:

1. **Lexical analysis** (lexical analyser) → tokens, filling the **symbol table**.
2. **Syntactic analysis** (syntax analyser) → an **abstract syntax tree (AST)**.
3. **Semantic analysis** (semantic analyser), using the symbol table and syntax tree.
4. **Code generation** (code generator).
