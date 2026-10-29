---
tags:
  - advanced-programming
---

# Project Management

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD05-ProjMan.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD05-ProjMan.pdf), Johan Bontes, University of Cape Town, PDF pages 1–47  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: projects versus processes, managing complexity, design levels, scope and requirements, planning (SMART goals, deliverables, schedule, supporting plans), milestones, and metrics (DORA, KPIs, pitfalls).

> [!note] <span style="color:#b89aff">Not examinable</span>
> Slides with purple titles are marked not examinable: project-management tools, the requirement checklists, and the architecture topic list. They are summarised briefly below for completeness.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Project Versus Process|Project Versus Process]]
  - [[#What Project Management Is|What Project Management Is]]
  - [[#No Silver Bullet: Essential And Accidental Complexity|No Silver Bullet: Essential And Accidental Complexity]]
  - [[#Managing Complexity (Dijkstra)|Managing Complexity (Dijkstra)]]
  - [[#Good Design Properties|Good Design Properties]]
  - [[#Design Levels|Design Levels]]
  - [[#Level 1: Requirements And Scope|Level 1: Requirements And Scope]]
  - [[#Stakeholders And Feasibility|Stakeholders And Feasibility]]
  - [[#Why Prepare And Why Explicit Requirements|Why Prepare And Why Explicit Requirements]]
  - [[#Levels 2–5: Subsystems, Classes, Routines|Levels 2–5: Subsystems, Classes, Routines]]
  - [[#Planning: SMART Goals, Deliverables, Schedule|Planning: SMART Goals, Deliverables, Schedule]]
  - [[#The Mythical Man-Month|The Mythical Man-Month]]
  - [[#Supporting Plans And Management Activities|Supporting Plans And Management Activities]]
  - [[#Milestones And Deliverables|Milestones And Deliverables]]
  - [[#DORA Metrics|DORA Metrics]]
  - [[#KPIs, Velocity And Code-Quality Metrics|KPIs, Velocity And Code-Quality Metrics]]
  - [[#Metric Pitfalls And SMART Metrics|Metric Pitfalls And SMART Metrics]]

---

## Core Content

### Project Versus Process

| | Process | Project |
|---|---|---|
| Nature | Routine | Ad hoc |
| Duration | Continuous | Fixed start and end |
| Inputs, outputs, tasks | Known and documented | Uncertain |
| Success rate | $>99\%$ | $\approx 50\%$ |
| Emphasis | Small improvements | Creation from scratch |
| Control | Fixed measurements | Outcome versus desires |
| Measurement | Money in = money out | Meets requirements |

A factory assembly line is a process. Software development is a project. In short: process good, project bad.

### What Project Management Is

#### Definitions

> **Project management**: Ensuring software is delivered on time, within budget, and to requirements (on quality). Software development is always constrained by budget and time.

Systems development needs careful management because of **dependencies, people and organisation**:

- Software artefacts depend on each other, so production must be planned, monitored and coordinated to be efficient, effective and on time.
- Projects often involve many developers, some specialists, needed at different times.
- Activities must follow a sequence. You can only test components once they are built, although test scripts and harnesses can be prepared earlier.

### No Silver Bullet: Essential And Accidental Complexity

#### Definitions

> **No silver bullet** (Brooks, 1987): No single technique fixes the inherent complexity of software design and development.

> **Essential problems**: Difficulties inherent in the problem itself (requirements, scope).

> **Accidental problems**: Difficulties caused by how we build it (process, tools, people).

- **Complexity is the problem** and must be managed.
- Computer science spans about $10^{13}$ orders of magnitude of scale, more than any other discipline.

Ineffective designs come from:

- a complex solution to a simple problem
- a simple, faulty solution to a complex problem
- a complex, faulty solution to a complex problem

### Managing Complexity (Dijkstra)

1. **Minimise the essential complexity** you must hold in your head at once:
   - problem decomposition: break the project into simple pieces
   - loose coupling
   - clean interfaces with no hidden gotchas
2. **Keep accidental complexity from proliferating**, through tools (language) and frameworks.

All other goals are secondary to managing complexity.

### Good Design Properties

| Property | Meaning |
|---|---|
| **Minimal complexity** | Easy to understand |
| **Ease of maintenance** | Documented and understandable |
| **Loose coupling** | Interfaces using abstraction, encapsulation and information hiding |
| **Extensible** | Easy to extend |
| **Reusable** | DRY: don't repeat yourself |
| **High fan-in** | Low-level classes are reused often |
| **Low fan-out** | A high-level class or function uses few lower-level ones |
| **Leanness** | "Make everything as simple as possible, but not simpler" |
| **Stratified** | A consistent view at every level of decomposition |
| **Standardised** | Uses common, proven patterns |

Project-management tools (not examinable) can be mixed and matched for the capstone project.

### Design Levels

![Design levels](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/design-levels.svg)

*Design proceeds from choosing a methodology, through project requirements, subsystems and classes, down to routines and source code.*

**Level 0: pick a methodology** (a software development life cycle, SDLC), e.g. the Unified Process or Waterfall (Royce, 1970). Royce's waterfall runs: system requirements → software requirements → analyse → design → code → test → deploy.

### Level 1: Requirements And Scope

#### Definitions

> **Scope**: What the software will deliver, described by narratives, use cases or requirements, and bounded by constraints.

> **Use case**: A scenario-based description of the user's interaction with the software, from the user's point of view.

Project requirements cover:

- functions and features delivered to end users
- data input and output
- content presented to users
- performance, constraints, external interfaces and reliability that bound the system

Scope is defined by:

- **narrative descriptions** after talking with stakeholders
- **use cases**
- **requirements**: functionality, performance, …
- **constraints**: external hardware, memory, existing infrastructure, time and budget

### Stakeholders And Feasibility

#### Definitions

> **Stakeholder**: Someone impacted by the project: the sponsor, the client for the deliverables, users, the project manager and the team.

> **Feasibility**: Whether we have the resources to build the software in scope.

Goals (scope) derive from stakeholders' needs and expectations. Find the **true needs** that create real benefits, and prioritise them.

![Stakeholder onion](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/stakeholder-onion.svg)

*Users, system admins and support staff sit closest to the product. Management, purchasing, legal and sales form the next ring. Regulators, media, the public, suppliers, clients and financial beneficiaries form the wider environment.*

To determine feasibility, find the resources the scope requires; this is not just money. The resources are people, hardware and tools, reusable components, and time and money.

### Why Prepare And Why Explicit Requirements

Preparing up front:

- **reduces risk**: more preparation means a greater chance of success
- **improves efficiency**: 80% of development time is spent finding and fixing bugs (McConnell, *Code Complete*)

Writing requirements down explicitly:

- lets the **client**, not the programmer, drive functionality
- explicit requirements can be reviewed by the client; code cannot
- changing requirements later is more expensive
- specifying requirements is key to success; stable requirements are the holy grail (no cost overruns)
- make sure users know the cost of changes, and use a process that allows change: a change control procedure, or Agile/evolutionary delivery

The requirement checklists (not examinable):

| Functional — have you specified… | Quality (non-functional, see ISO 25010) | Are requirements… |
|---|---|---|
| All inputs and outputs, file formats | Response time (latency), performance | **Complete**: missing info documented; acceptable if satisfied; realistic |
| Hardware/software and external interfaces (incl. errors, protocols) | Security, reliability | **Correct**: in users' language; no conflicts; acceptable trade-offs |
| All user tasks, the UI, data into and out of tasks | Resource use, maintainability, a success/failure benchmark | Detailed, understandable to coders, relevant, testable, adaptable |

Architecture topics (not examinable): languages and tools, subsystems, major classes, data design, business rules, UI, resources, security, performance, scalability, I/O, error processing and fault tolerance, buy-versus-build.

### Levels 2–5: Subsystems, Classes, Routines

**Level 2: subsystems.**

- Plan self-contained units that can be assigned to different people.
- Pick frameworks ("buy vs build").
- Plan interactions based on a hierarchy.

![Subsystem interactions](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/subsystems.svg)

*Unrestricted interactions give high fan-out and complexity. Rule-based, hierarchical interactions keep fan-out low.*

**Level 3: division into classes.** The application-level classes are identified with their attributes, methods and associations. The source example is a billing system: `Employee` (name, title, billingRate, `GetHoursForMonth()`), `Timecard` (hours, date, projectCode), `Client` (name, billingAddress, accountBalance, `EnterPayment()`) and `Bill` (billDate, `BillForClient()`), linked by associations such as billingEmployee, clientToBill and billingRecords.

**Level 4: division of classes into routines.** These steps are iterative and can be done out of order:

1. Design object attributes: methods and data.
2. Decide what can be done to each object.
3. Define interactions with other objects.
4. Partition into private, protected and public parts.
5. Define the public interface.

This depends on the paradigm. OOP models real-world objects; DOD (data-oriented design) models program data flows.

**Level 5: design routines and data.**

- Check requirements (performance, functionality).
- Give the routine a good name, *verbObject*, so the name documents behaviour, and follow a naming convention.
- Add documentation, especially requirements.
- Follow language-appropriate design patterns.
- Design parameters and return values (const correctness).
- Design invariants and checks: defend against bad input with **pre-conditions** (inputs, start state), **post-conditions** (outputs, end state) and **assertions**.
- Implementation starts with pseudocode (in some methodologies it comes later).

### Planning: SMART Goals, Deliverables, Schedule

#### Definitions

> **SMART goals**: Specific, Measurable, Agreed upon, Realistic, Time-based.

> **Deliverable**: An item that must be delivered to meet the goals. It is verifiable and specific, has a stakeholder who needs it, a delivery date and quality standards.

Example deliverable quality standards:

- the software runs
- unit test coverage
- zero compiler warnings at a high warning level
- documents meet the specified format

**Schedule**: the effort needed and the people and resources required. Update the schedule as deliverables change. If it is unrealistic, the options are:

| Option | Drawback |
|---|---|
| Delay the deadline | Late delivery |
| Add resources | More expensive; the mythical man-month |
| Reduce scope (fewer deliverables) | The only option that makes sense for the capstone |

### The Mythical Man-Month

#### Definitions

> **Mythical man-month** (Brooks, 1975): Adding people does not reduce completion time proportionally. Productivity per person falls because of team management and communication overhead, and eventually adding people lengthens the project ("too many cooks").

In the source model, a 1M-transistor chip is designed where one designer produces 5000 transistors/month and each additional designer reduces everyone's rate by 100. So two designers produce 4900 each.

$$
\text{team output}(n)=n\bigl(5000-100(n-1)\bigr),\qquad \text{months}(n)=\frac{10^6}{\text{team output}(n)}
$$

![Mythical man-month](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/mythical-man-month.svg)

*Team output peaks at about 25 designers (about 15 months). Beyond that, more designers make the project slower: 40 designers need about 23 months.*

### Supporting Plans And Management Activities

| Plan | Contents |
|---|---|
| **Human resource plan** | Key staff and organisations (skills, roles, responsibilities); number and type of people; start dates, duration, how to get them |
| **Communications plan** | Who needs updates and how: weekly reviews, progress reports and demos, revised schedules |
| **Risk management plan** | Identify as many risks as possible; respond with **ARTA**: Accept, Reduce, Transfer, Avoid |

| Area | Covers |
|---|---|
| **People** | Project managers, team leaders, the software team, customers, end users |
| **Product** | Scope, requirements, decomposition |
| **Process** | Start with a skateboard and refine iteratively (SDLC, Unified Process) |
| **Project** | Resources, scheduling, risks, tracking |
| **Price** | Budget, cost control, bookkeeping |

### Milestones And Deliverables

#### Definitions

> **Activity**: A task that takes time, with a duration and due date.

> **Precursor**: An activity that others depend on.

> **Milestone**: The completion of an activity: a recognisable end product of a task (e.g. handing the system over for testing) with a **formal, measurable output**. "Coding 80% complete" is not adequate.

> **Deliverable**: A project result delivered to the customer.

### DORA Metrics

#### Definitions

> **DORA metrics**: Four delivery-performance measures from DevOps Research and Assessment.

| Metric | Measures |
|---|---|
| **Change lead time** | Time to implement, test and deliver a feature (first commit to deployment) |
| **Deployment frequency** | Number of deployments in a period |
| **Change failure rate** | Failed changes as a percentage of all changes |
| **Mean time to recovery (MTTR)** | Time to restore service after a production failure |

**Criticisms**:

- DORA cannot compare teams, because complexity, expertise and subject matter differ.
- It does not address business risk. You must do a (hard) risk analysis, track risk indicators, and act on measurements.

**Culture**: support a generative culture, encourage learning, facilitate collaboration between teams, provide resources and tools that make work meaningful, and support or embody transformational leadership.

### KPIs, Velocity And Code-Quality Metrics

#### Definitions

> **Key performance indicator (KPI)**: A measurable value tracking how effectively the team meets its objectives.

> **Cyclomatic complexity**: A measure of how many independent logic paths code has.

> **Defect density**: Defects per thousand lines of code (KLOC).

> **Code churn**: How often code changes, often a sign of instability or unclear requirements.

| Category | Examples |
|---|---|
| **KPIs** | Throughput (tasks or stories per sprint); cycle time (issue creation to resolution); bug fix rate; release frequency; customer-reported defects |
| **Productivity / velocity** | Story points per sprint; burndown charts; pull-request metrics (time to review, merge, deploy); commit frequency (use carefully); rework percentage |
| **Code quality** | Code coverage; cyclomatic complexity; defect density; code churn; technical debt |

### Metric Pitfalls And SMART Metrics

| Pitfall | Example |
|---|---|
| **Non-metrics** | Lines of code, commit counts, hours worked |
| **Over-measurement** | Poor signal-to-noise ratio; bureaucratic overhead |
| **Stack ranking** | Fire the bottom x% and promote the top x% on some metric, then hire to fill the gap |
| **Ignoring context** | Complex work takes longer; quantification problems |

- **Many metrics are relative**: absolute values may be meaningless, and what matters is improvement over time. As long as we are improving, we are winning.
- **Gaming the system** happens. A **moral hazard** is when wrong incentives create harmful outcomes.
- Metrics should be **SMART** too, expressed as counts, percentages, sums or totals, averages, or ratios.
