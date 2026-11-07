---
tags:
  - advanced-programming
---

# Project Management

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD05-ProjMan.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD05-ProjMan.pdf), Johan Bontes, University of Cape Town, pages 1–47
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Projects versus processes, managing complexity, good design properties, the six design levels (methodology to routines), requirements and scope, planning (SMART goals, deliverables, schedules, the mythical man-month, supporting plans), milestones, and metrics (DORA, KPIs, pitfalls).

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Project Versus Process|Project Versus Process]]
  - [[#What Project Management Is|What Project Management Is]]
  - [[#No Silver Bullet: Managing Complexity|No Silver Bullet: Managing Complexity]]
  - [[#Good Design Properties|Good Design Properties]]
  - [[#The Design Levels|The Design Levels]]
  - [[#Level 0: Pick A Methodology|Level 0: Pick A Methodology]]
  - [[#Level 1: Requirements And Scope|Level 1: Requirements And Scope]]
  - [[#Stakeholders And Feasibility|Stakeholders And Feasibility]]
  - [[#Why Explicit Requirements?|Why Explicit Requirements?]]
  - [[#Requirements Checklist|Requirements Checklist]]
  - [[#Architecture Checklist|Architecture Checklist]]
  - [[#Levels 2–5: Subsystems, Classes And Routines|Levels 2–5: Subsystems, Classes And Routines]]
  - [[#Project Planning: Goals, Deliverables And Schedule|Project Planning: Goals, Deliverables And Schedule]]
  - [[#The Mythical Man-Month|The Mythical Man-Month]]
  - [[#Supporting Plans And Management Activities|Supporting Plans And Management Activities]]
  - [[#Milestones And Deliverables|Milestones And Deliverables]]
  - [[#DORA Metrics|DORA Metrics]]
  - [[#KPIs, Productivity And Code Quality Metrics|KPIs, Productivity And Code Quality Metrics]]
  - [[#Metric Pitfalls And SMART Metrics|Metric Pitfalls And SMART Metrics]]

---

## Core Content

### Project Versus Process

| Aspect | Process | Project |
|---|---|---|
| Nature | Routine | Ad hoc |
| Duration | Continuous | Fixed start and end |
| Inputs, outputs, tasks | Known and documented | Uncertain |
| Success rate | > 99% | ~50% |
| Emphasis | Small improvements | Creation from scratch |
| Control | Fixed measurements | Outcome versus desires |
| Measurement | \$ input = \$ output | Meets requirements |

Process good, project bad: projects are inherently riskier, which is why they need management.

### What Project Management Is

#### Definitions

> **Project management**: Ensuring software is delivered on time, within budget and as per requirements (at the required quality).

Software development is always subject to budget and time constraints. It needs careful management because of **dependencies, people and organisation**:

- Software artefacts depend on each other, so production must be planned, monitored and coordinated to be efficient, effective and on time.
- Many developers are involved, some with specialised skills needed at different times.
- Activities must follow a sequence — e.g. you can only test components once they're developed, though test scripts and harnesses can be prepared earlier.

### No Silver Bullet: Managing Complexity

> "There is no single technique that fixes the inherent complexity of software design and development." — Fred Brooks, *No Silver Bullet* (1987)

#### Definitions

> **Essential problems**: Difficulties inherent in the problem — requirements and scope.

> **Accidental problems**: Difficulties from how we work — process, tools and people.

- Complexity is the problem, and it must be managed. Computer science uniquely spans about $10^{13}$ orders of magnitude.
- Ineffective designs come from:
  - a complex solution to a simple problem;
  - a simple, faulty solution to a complex problem;
  - a complex, faulty solution to a complex problem.

**Dijkstra: manage complexity.** All other goals are secondary.

- **Minimise essential complexity** held in your head at any one time:
  - decompose the problem into simple pieces,
  - keep coupling loose,
  - use clean interfaces with no hidden gotchas.
- **Keep accidental complexity from proliferating**: tools (language) and frameworks.

### Good Design Properties

| Property | Meaning |
|---|---|
| Minimal complexity | Easy to understand |
| Ease of maintenance | Documented and understandable |
| Loose coupling | Interfaces using abstraction, encapsulation and information hiding |
| Extensible | Easy to extend |
| Reusable | **DRY** — don't repeat yourself |
| High fan-in | Low-level classes are reused often |
| Low fan-out | A high-level class or function uses few lower-level ones |
| Leanness | "Make everything as simple as possible, but not simpler" |
| Stratified | A consistent view at every level of decomposition |
| Standardised | Uses common, proven patterns |

Project management tools (many exist) can be mixed and matched for the capstone project.

### The Design Levels

![Design levels](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/design-levels.svg)

*Design proceeds from choosing a methodology down through project, subsystems, classes and routines to source code.*

| Level | Focus |
|---|---|
| 0 | Methodology |
| 1 | Project: requirements, scope, architecture |
| 2 | Subsystems |
| 3 | Classes / packages |
| 4 | Routines: methods and data in classes |
| 5 | Routine design and source code |

### Level 0: Pick A Methodology

#### Definitions

> **SDLC (software development life cycle)**: The overall sequence of phases a methodology follows.

Options include the **Unified Process** and **waterfall** (Royce, 1970): system requirements → software requirements → analyse → design → code → test → deploy.

### Level 1: Requirements And Scope

**Project requirements** describe:

- the functions and features delivered to end users;
- the data input and output;
- the content presented to users as they use the software;
- the performance, constraints, external interfaces and reliability that bound the system.

**Scope** is defined by:

| Means | Description |
|---|---|
| Narrative descriptions | Written after communicating with stakeholders |
| **Use cases** | Scenario-based descriptions of the user's interaction, from the user's point of view |
| Requirements | Functionality, performance, … |
| Constraints | Limits: external hardware, memory, existing infrastructure, time and budget |

**Why prepare?**

- **Reduce risk**: more preparation, greater chance of success.
- **Efficiency**: 80% of development time is spent finding and fixing bugs (McConnell, *Code Complete*, 2004).

### Stakeholders And Feasibility

#### Definitions

> **Stakeholder**: Someone impacted by the project — the sponsor, the client for the deliverables, system users, the project manager and team.

Goals (scope) derive from stakeholders' needs and expectations. Find the **true needs** that create real benefits, and prioritise them.

![Stakeholder onion](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/stakeholder-onion.svg)

*Rings closer to the product are more directly affected: users and operators, then the business (management, sales, legal, purchasing), then the wider environment (regulators, media, suppliers, the public).*

**Feasibility**: given the scope, determine the resources required — and answer "Do we have the resources to build this?" Resources are not just money:

- people,
- hardware and tools,
- reusable components,
- time and money.

### Why Explicit Requirements?

- They let the **client**, not the programmer, drive functionality.
- The client can review explicit requirements; they can't review code.
- Changing requirements later is more expensive.
- Specifying requirements is key to success; **stable requirements are the holy grail** — no cost overruns.
- Make sure users know the cost of requirement changes.
- Use an approach that allows for change: a change control procedure, or Agile/evolutionary delivery.

### Requirements Checklist

Have you specified:

| Functional | Quality (non-functional) — see ISO 25010 |
|---|---|
| All inputs and all outputs | Response time (latency) |
| File formats | Performance |
| Hardware and software interfaces | Security |
| External interfaces (including errors and protocols) | Reliability |
| All user tasks | Resource use (memory, storage) |
| User interface | Maintainability |
| Data into and out of user tasks | Definition of success/failure (benchmark) |

Are the requirements:

| Complete | Correct |
|---|---|
| Missing information at the start documented? | Written in the users' language, and do users agree? |
| If the program satisfies them, will it be accepted? | No conflicting requirements |
| Realistic and relevant — impossible and nonsense requirements removed? | Acceptable trade-offs for competing requirements (e.g. speed vs quality) |
| | Detailed enough, and consistently so |
| | Understandable to coders, and do coders agree? |
| | Relevant and testable |
| | Adaptable — possible changes specified |

### Architecture Checklist

Architecture decisions with system-wide implications:

- programming languages and tools;
- program organisation into subsystems;
- major classes;
- data design;
- business rules;
- user interface;
- resources (database, memory, threads);
- security, performance, scalability;
- I/O;
- error processing and fault tolerance;
- buy versus build (frameworks).

### Levels 2–5: Subsystems, Classes And Routines

**Level 2 — subsystems**:

- Plan subsystems as self-contained units that can be assigned to different people.
- Pick frameworks (buy vs build).
- Plan interactions based on a hierarchy.

![Subsystem interactions](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/subsystems.svg)

*Left: unrestricted interactions and high fan-out make a complex system. Right: rule-based, hierarchical interactions with low fan-out keep it simple.*

**Level 3 — classes**: divide each subsystem into classes and packages.

**Level 4 — routines**: divide classes into routines. The steps are iterative and can be done out of order:

1. Design object attributes: methods and data.
2. Decide what can be done to each object.
3. Design interactions with other objects.
4. Partition into private, protected and public parts.
5. Define the public interface.

This depends on paradigm: OOP models real-world objects; data-oriented design (DOD) models the program's data flows.

**Level 5 — routines and data**:

- Check requirements (performance, functionality).
- Give it a good name in **verbObject** form, so the name documents behaviour; follow a naming convention.
- Add necessary documentation, especially requirements.
- Follow design patterns (language-dependent).
- Design parameters and return values (const correctness).
- Design invariants and checks (assertions, exceptions) to defend against bad input:
  - **pre-conditions** (inputs, the object's start state),
  - **post-conditions** (outputs, the object's end state),
  - assertions.
- Implementation (later in some methodologies) — start with pseudocode.

### Project Planning: Goals, Deliverables And Schedule

**Goals** should be **SMART**:

| Letter | Goal setting |
|---|---|
| S | Specific |
| M | Measurable |
| A | Agreed upon |
| R | Realistic |
| T | Time-based |

**Deliverables** are the items that must be delivered to meet the goals.

- Verifiable and specific (e.g. a report, executable code).
- Each has a stakeholder who needs it and a delivery date.
- Each has quality standards, e.g. the software runs; unit-test coverage; zero compiler warnings at a high warning level; documents meet a specified format.

**Schedule**: the effort (time), people and other resources required. Updating the deliverables updates the schedule. If the schedule is unrealistic, either:

1. delay the deadline;
2. add resources — more expensive, and see the mythical man-month; or
3. reduce scope (fewer deliverables) — the only option that makes sense for the capstone.

### The Mythical Man-Month

#### Definitions

> **The mythical man-month** (Brooks, 1975): In theory adding designers reduces completion time; in reality productivity per designer falls because of team management and communication overheads, and at some point adding people lengthens the project ("too many cooks").

Example: a 1-million-transistor design. One designer produces 5000 transistors/month, and each additional designer reduces everyone's output by 100/month (so 2 designers produce 4900 each).

$$
\text{individual output}(n) = 5000 - 100(n-1), \qquad \text{team output}(n) = n\,\big(5100 - 100n\big)
$$

$$
\text{months to finish} = \frac{1\,000\,000}{\text{team output}(n)}
$$

| Designers $n$ | ≈5 | ≈10 | ≈15 | ≈20 | ≈25 | ≈30 | ≈35 | ≈40 |
|---|---|---|---|---|---|---|---|---|
| Months to finish | 43 | 24 | 19 | 16 | 15 | 16 | 18 | 23 |

![The mythical man-month](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/05A_Project_Management/mythical-man-month.svg)

*Team output peaks at about 25 designers and then falls, so completion time rises again; individual output falls steadily.*

### Supporting Plans And Management Activities

| Plan | Content |
|---|---|
| **Human resource plan** | Key staff and organisations: skills, roles and responsibilities; number and type of people; start dates, durations and how to get them |
| **Communications plan** | Who must be kept updated and how: weekly review meetings, progress reports and demos, revised schedules |
| **Risk management plan** | Identify as many risks as possible and treat each by **ARTA**: Accept, Reduce, Transfer or Avoid |

Management activities cover the four Ps:

| Area | Concerns |
|---|---|
| **People** | Project managers, team leaders, software team, customers, end users |
| **Product** | Scope, requirements, decomposition |
| **Process** | Start with a skateboard and refine iteratively; SDLC, Unified Process |
| **Project** | Resources, scheduling, risks, tracking |
| **Price** | Budget, cost control, bookkeeping |

### Milestones And Deliverables

#### Definitions

> **Activity**: A task that takes time, with a duration and a due date.

> **Precursor**: An activity that others depend on, so it must precede them.

> **Milestone**: The completion of an activity, with a recognisable end product (e.g. handing over a system for testing). It needs a formal, measurable output — "coding 80% complete" is not adequate.

> **Deliverable**: A project result that is delivered to the customer.

### DORA Metrics

#### Definitions

> **DORA metrics**: Four delivery-performance metrics from the DevOps Research and Assessment programme.

| Metric | Meaning |
|---|---|
| **Change lead time** | Time to implement, test and deliver code for a feature, from first commit to deployment |
| **Deployment frequency** | Number of deployments in a given period |
| **Change failure rate** | Percentage of changes that fail, out of all changes |
| **Mean time to recovery (MTTR)** | Time to restore service after a production failure |

Criticisms:

- They can't be used to compare teams: complexity, expertise and subject matter differ.
- They don't address business risk. You must do a risk analysis (hard), track risk indicators, and reduce risk through measurement-based actions.

DORA culture recommendations:

- support a **generative culture**;
- encourage and support learning;
- support collaboration among teams;
- provide resources and tools that make work meaningful;
- support or embody transformational leadership.

### KPIs, Productivity And Code Quality Metrics

#### Definitions

> **KPI (key performance indicator)**: A measurable value showing how effectively a team is achieving its objectives.

| Category | Metric | Meaning |
|---|---|---|
| KPIs | Throughput | Tasks or user stories completed per sprint |
| | Cycle time | Average time from issue creation to resolution |
| | Bug fix rate | How quickly identified defects are resolved |
| | Release frequency | Cadence of production deployments |
| | Customer-reported defects | Post-release issues, showing testing effectiveness |
| Productivity and velocity | Velocity | Story points completed per sprint, showing consistency |
| | Burndown charts | Visual progress toward sprint goals |
| | Pull request metrics | Time to review, merge and deploy changes |
| | Commit frequency | Commits per developer — use carefully to assess engagement |
| | Rework percentage | Share of time spent fixing or redoing earlier work |
| Code quality | Code coverage | Percentage of code tested by automated tests |
| | Cyclomatic complexity | How complex the logic paths are |
| | Defect density | Defects per thousand lines of code (KLOC) |
| | Code churn | Frequency of code changes — often a sign of instability or unclear requirements |
| | Technical debt | The cost of delayed refactoring or poor design choices |

### Metric Pitfalls And SMART Metrics

| Pitfall | Description |
|---|---|
| Non-metrics | Lines of code, commit counts, hours worked |
| Over-measurement | Poor signal-to-noise ratio; bureaucratic overhead |
| Stack ranking | Fire the bottom $x\%$ on metric $y$, promote the top $x\%$, hire to fill the gap |
| Ignoring context | Complex work takes longer; quantification problems |

- **Many metrics are relative**: absolute values may be meaningless. What matters is improvement over time — as long as we're improving, we're winning.
- **Gaming the system** happens. A **moral hazard** arises when the wrong incentives create harmful outcomes.

Metrics should also be SMART:

| Letter | Question |
|---|---|
| Specific | What exactly is an indicator of success? |
| Measurable | Can you physically track the KPI? |
| Achievable | Are the KPIs realistic? |
| Relevant | Do the KPIs reflect the business's overall goals? |
| Time-framed | When should the KPIs be met? |

SMART metrics take the form of counts, percentages, sums or totals, averages, and ratios.
