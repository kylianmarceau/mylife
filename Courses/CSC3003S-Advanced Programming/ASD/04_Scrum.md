---
tags:
  - advanced-programming
---

# Scrum

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD04 Scrum.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD04%20Scrum.pdf), Johan Bontes, University of Cape Town, PDF pages 1–45  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: Scrum vocabulary, roles, artefacts and events, the sprint flow and meetings, backlogs and burndown charts, and what goes wrong.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Scrum Is|What Scrum Is]]
  - [[#Late Versus Early Learning|Late Versus Early Learning]]
  - [[#Scrum Lingo|Scrum Lingo]]
  - [[#Scrum Roles|Scrum Roles]]
  - [[#Pigs And Chickens|Pigs And Chickens]]
  - [[#Scrum Artefacts And Commitments|Scrum Artefacts And Commitments]]
  - [[#Scrum Events|Scrum Events]]
  - [[#Scrum Rules|Scrum Rules]]
  - [[#Scrum Flow And Sprints|Scrum Flow And Sprints]]
  - [[#Sprint Planning Meeting|Sprint Planning Meeting]]
  - [[#Daily Scrum|Daily Scrum]]
  - [[#During The Sprint|During The Sprint]]
  - [[#Sprint Review And Retrospective|Sprint Review And Retrospective]]
  - [[#Product Backlog, Sprint Backlog And Burndown|Product Backlog, Sprint Backlog And Burndown]]
  - [[#What Can Go Wrong|What Can Go Wrong]]

---

## Core Content

### What Scrum Is

#### Definitions

> **Scrum**: A concrete implementation of Agile. Agile is the philosophy, Scrum the concrete process. About 63% of Agile projects use Scrum (State of Agile survey, "just another online survey").

> [!warning] <span style="color:#ffc778">Not a silver bullet</span>
> Scrum does not compensate for lack of training or experience, its team has defined roles, and it is not a cure for every development ill.

### Late Versus Early Learning

![Knowledge curves](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/knowledge-curves.svg)

*Waterfall delivers almost no knowledge or risk reduction until big-bang integration. Scrum's early, continuous integration builds knowledge from the start.*

| | Waterfall | Scrum |
|---|---|---|
| Strategy | **Late learning**; delays true understanding of the system | **Learn early** in the project |
| Knowledge arrives | At the "moment of truth": final integration | Continuously, through early integration |
| Development sequence | Big-bang | Indifferent with respect to knowledge |
| Up-front design | Assumes it reduces risk | Reduces risk only if the problem is well understood |

### Scrum Lingo

| Term | Meaning |
|---|---|
| **Goal** | The end objective |
| **Sprint** | A fixed time box of $\le 1$ month |
| **Planning** | Items to do plus schedule |
| **Product** | The software to be built; must be an independent artefact |
| **Backlog** | Work items ordered by priority |
| **Team** | $\le 10$ people, no sub-teams, no hierarchy |
| **Scrum Master (SM)** | Coach and mentor of the team; liaison to management |
| **Daily Scrum** | 15-minute progress meeting |
| **Increment** | Outcome of a sprint: a concrete stepping stone toward the Product Goal |
| **Definition of done** | Agreed quality; the work is finished |
| **Undone work** | Not finished, or quality not OK |
| **Sprint review** | Inspect the outcome and future adaptations |
| **Sprint retrospective** (slides: "introspective") | How to improve quality and effectiveness |

### Scrum Roles

![Scrum roles](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/scrum-roles.svg)

*One Scrum Master, one Product Owner and $n-2$ developers in a team of at most 10 (fewer is better).*

| Role | Responsibilities |
|---|---|
| **Scrum Master** (1) | A servant, not a leader. Removes obstacles to progress, chairs Scrum events, liaises between the team and the organisation, coaches (e.g. training through pair programming). |
| **Product Owner** (1) | Develops the product goal, plans and prioritises the product backlog, communicates with customers, provides funding. Can be shared by multiple teams. |
| **Developers** ($n-2$) | Have all the skills needed, do sprint and daily planning, and guard quality through the "definition of done". |

Need more people? Split the product and run multiple Scrum teams.

The team itself examines the requirements, considers the available technology, evaluates its own skills, and decides how to build the functionality, adjusting daily. **The heart of Scrum is the iterations and the creative process.**

### Pigs And Chickens

#### Definitions

> **Pigs**: Team members (SM, PO, developers): fully committed.

> **Chickens**: Customers, users, vendors, management: involved and needed, but indirectly.

The name comes from the joke about a ham-and-eggs breakfast: the chicken is involved, the pig is committed. Scrum is about empowering the pigs and **getting the chickens out of the kitchen**.

### Scrum Artefacts And Commitments

Artefacts represent work or value. Each carries a **commitment** that adds transparency and focus, so progress can be measured against it.

| Artefact | What it is | Commitment | What the commitment is | Characteristics |
|---|---|---|---|---|
| **Product backlog** | Emergent, ordered list of what is needed to improve the product | **Product goal** | Future state of the product, used to plan sprints | Clear and concise; transparent in the backlog |
| **Sprint backlog** | The set of product backlog items for this sprint | **Sprint goal** | Single objective for the sprint | Flexible in how it is achieved; if impossible, cancel the sprint |
| **Increment** | Concrete stepping stone toward the product goal | **Definition of done** | Formal definition of quality all developers commit to | A sprint makes $\ge 1$ increments; not quality means not done |

### Scrum Events

Events happen only inside a sprint. Each is a formal opportunity to inspect and adapt artefacts, held at a regular time and place. Ideally there are no meetings outside them.

| Event | Duration (1-month sprint) | Subject | Output | Participants |
|---|---|---|---|---|
| **Sprint** | $\le 1$ month (typically 2 weeks) | — | Increments | Mostly developers |
| **Sprint planning** | $\le 8$ h | Product backlog, product goal, definition of done | Sprint backlog, sprint goal | Scrum team |
| **Sprint review** | $\le 4$ h | Increment, sprint, product backlog, progress toward the product goal | Updated product backlog | Scrum team and stakeholders |
| **Sprint retrospective** | $\le 3$ h | Sprint, definition of done | Actionable improvements, definition of done | Scrum team |
| **Daily scrum** | 15 min daily | Progress toward the sprint goal | Progress toward the sprint goal | Developers |

### Scrum Rules

- The **Scrum Master is the rule-master**. Rules mean everyone knows how to play.
- Unenforced rules waste time while people work out what to do, and disputed rules waste time while everyone waits for a resolution.
- The rules have worked in thousands of successful projects.
- **Changing rules** happens only in the sprint retrospective. Changes must come from the team, not management, and only once the Scrum Master is convinced everyone understands how Scrum works.

### Scrum Flow And Sprints

1. A project starts with a **vision** (in XP terms, the "system metaphor"), which leads to the logical architecture.
2. The Product Owner produces the **product backlog**: functional and non-functional requirements that together deliver the vision. It is prioritised by likely value and divided into proposed releases.
3. Work is done in **sprints** of $\le 20$ consecutive workdays (a month), each starting with a sprint planning meeting.
4. Each sprint produces a **potentially shippable product increment**.

![Sprint flow](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/sprint-flow.svg)

*The PO's product backlog feeds sprint planning, which produces the team's sprint backlog. The sprint runs with a 24-hour daily scrum cycle and ends in a shippable increment.*

The sprint is **time-boxed** to $\le 30$ days (typically 2 weeks) because that is:

- enough time for the team to build something of significant interest to the PO and stakeholders, in a potentially shippable state
- the maximum time to work without artefacts and documentation to support thinking
- the maximum time most stakeholders will wait without losing interest or belief that the team is doing something meaningful

### Sprint Planning Meeting

The meeting lasts at most 8 hours, in two segments of up to 4 hours each.

| Inputs | Outputs |
|---|---|
| Product backlog, team capabilities, business conditions, technology, current product | Sprint goal, sprint backlog |

**Segment 1: select items.**

- The team selects product backlog items it believes it can turn into an increment, to demonstrate at the sprint review.
- The PO says what is desired and makes the backlog selection; the team makes suggestions and decides **how many** items to include.

**Segment 2: prepare the sprint backlog.**

- The team manages its own work and works out how to turn the items into an increment. The PO answers questions; others only observe.
- The output is the sprint backlog: tasks, time estimates and assignments.
- It may be incomplete, but must be complete enough for every member's commitment and to carry the team through the first part of the sprint while more tasks are devised.

The time box prevents hand-wringing about what is possible. The goal is to get to work, not to think about working.

### Daily Scrum

- **Time-boxed to 15 minutes** regardless of team size.
- Same place, same time every workday, ideally first thing so members think about yesterday and today.
- **All team members attend**, remotely if needed, or someone reports why they are absent.
- It starts on time whoever is present; latecomers pay a fine to the Scrum Master.

The SM asks everyone three questions:

1. What did you do yesterday?
2. What will you do today?
3. What stands in the way of getting your work done?

One person talks while the others listen. Answers are short, with no digressions:

$$
\frac{15\text{ min}}{3\text{ questions} \times \text{people present}} \approx 30\text{ s per answer}
$$

- **Purpose**: synchronise everyone's work daily and schedule any meetings needed to help progress.
- **Chickens** may attend but cannot communicate, verbally or otherwise, and cannot start follow-up meetings with pigs.

### During The Sprint

- The team may seek outside advice, help and information, but **no unsolicited advice** is given. The team is self-managing.
- The committed backlog is **frozen** until the end of the sprint.
- **Can't finish?** The team consults the PO on which items to remove. If too many are removed, the SM can terminate the sprint.
- **Want more?** The team asks the PO which product backlog items to add.

A **non-viable sprint** may be terminated by the SM, at the team's or PO's request, followed by a new sprint planning meeting. A sprint can become non-viable when:

- the technology proves unworkable
- business conditions change so the sprint no longer has value
- someone outside the team interferes during the sprint

The team has two administrative duties during a sprint:

1. Attend the daily scrum.
2. Keep the sprint backlog up to date and publicly visible: add new tasks as they are conceived and update the daily estimated hours remaining.

### Sprint Review And Retrospective

**Sprint review** ($\le 4$ h, at most 1 h of preparation):

- The team presents the increment(s) to the PO and stakeholders.
- Only work that is **done** (complete and shippable) can be presented. If "done" means something else, make sure the PO and stakeholders understand it.
- Topics: the sprint goal, the completed sprint and product backlog items, what went well and what didn't, stakeholder questions, and a poll of stakeholder impressions, needs and priorities.
- The PO adds and reorders product backlog items.

**Sprint retrospective** ($\le 3$ h; team, SM, and optionally the PO):

1. Each member briefly answers: *What went well last sprint? What could improve next sprint?*
2. The SM summarises.
3. The team prioritises the issues and discusses improvements, with the SM facilitating.
4. Actionable items can become high-priority **non-functional** product backlog items.

### Product Backlog, Sprint Backlog And Burndown

#### Definitions

> **Product backlog**: A prioritised list of first-cut refinements. The PO is free to reorder it and add new items, which is where agility and change come in.

> **Sprint backlog**: The list of things that will be done in the sprint, each with an estimate (usually hours), updated throughout the sprint.

> **Velocity**: How fast a team completes work, measured from sprint backlog updates.

> **Burndown chart**: A graph of the sprint backlog's hours remaining against days, showing the rate at which work is completed.

Backlogs can be kept in a spreadsheet or a cloud tool; consider support for distributed teams. A sample product backlog from a game, with estimates in person-weeks:

| Backlog item | Estimate |
|---|---|
| Break props into separate rigid bodies | — |
| Arrow projectiles stick to environment | 0.5 |
| Ragdolls can lose limbs | — |
| NPCs avoid dynamite thrown at them | — |
| Improve exception handling | 0.5 |

Keeping the sprint backlog updated gives the team's **velocity** and acts as an **early warning**. The sample sprint shows hours remaining falling $152 \to 144 \to 136 \to 124 \to 116 \to 112 \to 106$ over its first days, with minor items, major items and supervision assigned to owners.

![Burndown chart](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/burndown.svg)

*The ideal is a steady drive to zero hours, a sustainable pace. Real lines are not perfectly straight. Staying above the line means too slow, falling well below it means too fast.*

Burning down **too slowly** can be caused by inexperienced developers, hard roadblocks, distractions or bad planning. Burning down **too fast** suggests the sprint was under-committed or badly estimated.

### What Can Go Wrong

| Problem | Why it hurts | Remedy |
|---|---|---|
| **Loss of rhythm** | Sprints of different lengths feel like arbitrary units chosen by outside forces and make planning hard | Keep every sprint the same length |
| **Talking chickens** | A chicken allowed one useful comment is a slippery slope | Only pigs speak; be strict |
| **Missing pigs** | Flexible hours and night-owl developers mean people are late or absent; the rhythm breaks | Same time and place daily. If many miss it, the meeting is probably too long or straying from the 3 questions. Skip only in emergencies. |
| **Specialised job roles** | Architect, DBA, tester roles undermine "we're all in this together" | The team need not be all generalists, but each specialist must take responsibility for the whole system |
| **Daily scrum is for the SM** | It becomes a status report to the SM, who notes who failed to do what | The SM is a servant. The scrum coordinates the team and makes commitments public among peers; no rebukes, since unmet commitments already feel bad enough |
| **SM assigns work** | Undermines self-organisation; even occasional assignment is harmful | Developers sign up for work and must feel fully in control of it |
