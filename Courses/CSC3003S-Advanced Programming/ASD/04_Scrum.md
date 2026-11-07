---
tags:
  - advanced-programming
---

# Scrum

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD04 Scrum.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD04%20Scrum.pdf), Johan Bontes, University of Cape Town, pages 1–45
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Scrum as a concrete Agile implementation: early learning, roles, artefacts and events, the sprint flow and meetings, backlogs and burndown charts, and common ways Scrum goes wrong.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#What Scrum Is|What Scrum Is]]
  - [[#Late Versus Early Learning|Late Versus Early Learning]]
  - [[#Scrum Vocabulary|Scrum Vocabulary]]
  - [[#Scrum Roles|Scrum Roles]]
  - [[#Pigs And Chickens|Pigs And Chickens]]
  - [[#Scrum Artefacts And Commitments|Scrum Artefacts And Commitments]]
  - [[#Scrum Events|Scrum Events]]
  - [[#Scrum Rules|Scrum Rules]]
  - [[#Scrum Flow And Sprints|Scrum Flow And Sprints]]
  - [[#Sprint Planning Meeting|Sprint Planning Meeting]]
  - [[#Daily Scrum Meeting|Daily Scrum Meeting]]
  - [[#During The Sprint|During The Sprint]]
  - [[#Sprint Review And Retrospective|Sprint Review And Retrospective]]
  - [[#Product Backlog And Sprint Backlog|Product Backlog And Sprint Backlog]]
  - [[#Burndown Charts|Burndown Charts]]
  - [[#What Can Go Wrong|What Can Go Wrong]]

---

## Core Content

### What Scrum Is

#### Definitions

> **Scrum**: A concrete implementation of Agile. Agile is a philosophy; Scrum is a specific way of doing it.

- According to the State of Agile survey (just another online survey), 63% of Agile projects use Scrum.
- **Warning**: Scrum is not a silver bullet or a panacea for all development ills. It does not compensate for lack of training or experience, and the team has defined roles that must be filled properly.

### Late Versus Early Learning

| | Waterfall | Scrum |
|---|---|---|
| Strategy | **Late learning**: delays true understanding of the system | **Early learning**: it pays to learn early |
| Integration | Big-bang integration at the end | Early, continuous integration |
| Knowledge growth | Almost no knowledge (risk reduction) until the "moment of truth" — final integration | Knowledge and risk reduction grow steadily |
| Up-front design | Required | Only reduces risk if the problem is well understood |

![Late versus early learning](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/knowledge-curves.svg)

*In waterfall, knowledge stays flat until final integration; in Scrum it rises with each integrated increment.*

### Scrum Vocabulary

| Term | Meaning |
|---|---|
| Goal | The end objective |
| **Sprint** | A fixed time-box of at most one month |
| Planning | Items to do plus the schedule |
| Product | The software to be built; must be an independent artefact |
| **Backlog** | Work items, ordered by priority |
| Team | At most 10 people, no sub-teams, no hierarchy |
| **Scrum Master (SM)** | Coach and mentor of the team; liaison to management |
| **Daily scrum** | A 15-minute meeting to discuss progress |
| **Increment** | The outcome of a sprint: a concrete stepping stone toward the product goal |
| **Definition of done** | The agreed quality; the work is finished |
| Undone work | Unfinished, or quality not OK |
| **Sprint review** | Inspect the outcome and future adaptations |
| **Sprint retrospective** | How to improve quality and effectiveness |

### Scrum Roles

A Scrum team has 10 people or fewer (fewer is better). Need more people? Split the product and form several Scrum teams.

| Role | Count | Responsibilities |
|---|---|---|
| **Scrum Master** | 1 | Guards quality; removes obstacles to progress; chairs Scrum events; trains the team (e.g. in pair programming); is **not a leader but a servant**; can be shared by several teams |
| **Product Owner** | 1 | Owns the project goal; plans the product backlog and its priorities; communicates with customers; liaises with the organisation, which provides funding |
| **Developers** | $n - 2$ | Must have all the skills needed; develop quality work to the definition of done; do sprint and daily planning |

![Scrum roles](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/scrum-roles.svg)

*The Product Owner faces the customer and organisation, the Scrum Master serves and protects the team, and developers build the increment.*

The team itself looks at the requirements, considers the available technology, evaluates its own skills, and decides how to build the functionality — modifying its approach daily. The heart of Scrum is the iterations plus this creative process.

### Pigs And Chickens

| | Pigs | Chickens |
|---|---|---|
| Who | Team members: SM, PO, developers | Customers, users, vendors, management |
| Involvement | **Committed** | **Involved** — needed, but indirectly |

From the joke: in a ham-and-eggs breakfast, the chicken is involved but the pig is committed. Scrum is about empowering the pigs and getting the chickens out of the kitchen.

### Scrum Artefacts And Commitments

Artefacts represent work or value. Each contains a **commitment** that adds transparency and focus, against which progress can be measured.

| Artefact | What it is | Commitment | Commitment meaning | Characteristics |
|---|---|---|---|---|
| **Product backlog** | Emergent, ordered list of what's needed to improve the product | Product goal | Future state of the product, used to plan sprints | Clear, concise, transparent in the backlog |
| **Sprint backlog** | Set of product backlog items to work on in the sprint | Sprint goal | Single objective for the sprint | Flexible in how it's achieved; if impossible, cancel the sprint |
| **Increment** | Concrete stepping stone toward the product goal | Definition of done | Formal quality standard all developers commit to | A sprint makes at least one increment; not quality → not done |

### Scrum Events

#### Definitions

> **Scrum event**: A formal opportunity to inspect and adapt Scrum artefacts. All events happen inside a sprint, at a regular time and place; ideally there are no meetings outside events.

| Event | Time-box | Inputs (subject) | Output | Participants |
|---|---|---|---|---|
| Sprint | ≤ 1 month (typically 2 weeks) | — | Increments | Mostly developers |
| Sprint planning | ≤ 8 hours (for a 1-month sprint) | Product backlog, product goal, definition of done | Sprint backlog, sprint goal | Scrum team |
| Sprint review | ≤ 4 hours | Increment, sprint, product backlog, progress toward goal | Updated product backlog | Scrum team, stakeholders |
| Sprint retrospective | ≤ 3 hours | Sprint, definition of done | Actionable improvements, updated definition of done | Scrum team |
| Daily scrum | 15 minutes, daily | Progress toward sprint goal | Progress toward sprint goal | Developers |

### Scrum Rules

- The Scrum Master is the **rule-master**; rules mean everyone knows how to play.
- If rules aren't enforced, people waste time working out what to do; if disputed, everyone waits for a resolution.
- The rules have worked in thousands of successful projects.
- To change rules, use the sprint retrospective:
  - changes should come from the team, not management;
  - only once the Scrum Master is convinced everyone understands how Scrum works — no rule changes until then.

### Scrum Flow And Sprints

1. Every project starts with a **vision** (in XP terms, the "system metaphor"), which leads to the logical architecture.
2. The **Product Owner** produces the **product backlog**: functional and non-functional requirements that, once built, deliver the vision. It is prioritised by likely value and divided into proposed releases.
3. Work is done in **sprints** of at most 20 consecutive workdays (a month), each starting with a sprint planning meeting.
4. Each day of the sprint has a 24-hour cycle with a daily scrum.
5. Each sprint ends with a **potentially shippable product increment**.

![Scrum sprint flow](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/sprint-flow.svg)

*The prioritised product backlog feeds a sprint backlog; daily scrums run inside the sprint loop, which produces a shippable increment.*

### Sprint Planning Meeting

Time-boxed to **8 hours**, which prevents hand-wringing about what's possible: the goal is to get to work, not think about working.

Inputs: product backlog, team capabilities, business conditions, technology, the current product. Outputs: sprint goal and sprint backlog.

It has two segments of at most 4 hours each:

| Segment | Purpose | Who decides |
|---|---|---|
| 1. Select product backlog | The PO says what's desired; the team says how much it believes it can turn into an increment, to demonstrate at the sprint review | Team suggests and decides **how many** items; the PO makes the **selection** |
| 2. Prepare sprint backlog | The team works out how to turn the selected items into an increment; the PO answers questions; others only observe or answer | Team manages its own work |

The output of segment 2 is the sprint backlog: tasks, time estimates and assignments. It needn't be complete, but must be complete enough for every member to commit, and to carry them through the first part of the sprint while they devise more tasks.

### Daily Scrum Meeting

- Time-boxed to **15 minutes**, regardless of team size.
- Same place, same time every workday — ideally first thing, so members think about yesterday and today.
- All team members attend (remotely if necessary, or another member reports why they're absent).
- The Scrum Master starts on time regardless of who's present; latecomers pay a fine to the Scrum Master immediately.

The Scrum Master asks everyone three questions:

1. What did you do yesterday?
2. What will you do today?
3. What stands in the way of getting your work done?

One person talks while others listen. Answers are short — no digressions:

$$
\frac{15\text{ min}}{3\text{ questions} \times \text{people present}} \approx 30 \text{ seconds per answer}
$$

Purpose: synchronise the team's work daily and schedule any meetings needed to help progress. Chickens may attend but may not communicate (verbally or otherwise) or initiate follow-up meetings with pigs.

### During The Sprint

**Time-boxing**: a sprint is at most 30 days (more typically 2 weeks). This is:

- the time a team needs to build something of significant interest to the PO and stakeholders and make it potentially shippable;
- the maximum time to work without artefacts and documentation supporting the thought process;
- the maximum time most stakeholders will wait without losing interest or belief that the team is doing something meaningful.

**Rules during the sprint**:

- The team may seek outside advice, help and support, but receives **no unsolicited advice**. It is self-managing.
- The team has committed to the selected backlog, which is **frozen** until the sprint ends.

**Changing the sprint backlog**:

| Situation | Action |
|---|---|
| Team can't complete the sprint backlog | Consult the PO on which items to remove; if too many go, the Scrum Master can terminate the sprint |
| Team wants to do more | Ask the PO which product backlog items to add |

**Non-viable sprint**: the Scrum Master may terminate the sprint (at the team's or PO's request) and start a new planning meeting if:

- the technology proves unworkable;
- business conditions change so the sprint has no business value;
- anyone outside the team interferes during the sprint.

**Team responsibilities** — two administrative tasks:

1. Attend the daily scrum.
2. Keep the sprint backlog up to date and publicly visible: add new tasks as they arise and update each task's estimated remaining hours daily.

### Sprint Review And Retrospective

**Sprint review** (≤ 4 hours, ≤ 1 hour of preparation):

- The team presents increments to the PO and stakeholders.
- "Done" means complete and shippable; if "done" means anything else, make sure the PO and stakeholders understand. Anything not done cannot be presented.
- Topics: sprint goal, sprint backlog, completed product backlog items; what went well and what didn't; stakeholder questions; a stakeholder poll on impressions, needs and their priorities.
- The PO then adds and reorders product backlog items.

**Sprint retrospective** (≤ 3 hours; team, Scrum Master and optionally the PO):

1. Each member briefly answers: What went well last sprint? What could be improved next sprint?
2. The Scrum Master summarises the answers.
3. The team prioritises the issues and discusses improvements, facilitated by the Scrum Master.
4. Actionable items can become high-priority non-functional product backlog items.

### Product Backlog And Sprint Backlog

Scrum's artefacts — product backlog, sprint backlog and burndown charts — can be managed in a spreadsheet or cloud tools (consider support for distributed teams).

**Product backlog**: a prioritised list of first-cut refinements. The PO can reorder items and add new ones at any time, which brings agility and change.

| Backlog item | Estimate (person-weeks) |
|---|---|
| Break props into separate rigid bodies | — |
| Arrow projectiles stick to environment | 0.5 |
| Ragdolls can lose limbs | — |
| NPCs avoid dynamite thrown at them | — |
| Improve exception handling | 0.5 |

**Sprint backlog**: what will be "done" during the sprint, each item with an estimate (usually hours). The team must update it throughout. Keeping it current lets you measure the team's **velocity** and gives early warning of trouble.

Example update (Sprint 1): remaining hours fall day by day — 152, 144, 136, 124, 116, 112, 106 — across items such as fixing login-screen formatting, correcting legacy report code, modifying user-file handling, adding network error handling, adding company logos, a de-jitter algorithm, a workflow design change and supervision; 19 days of work in the sprint.

### Burndown Charts

#### Definitions

> **Burndown chart**: A graph of the sprint backlog's remaining hours against sprint days, showing the rate at which work is completed.

- It should show a steady drive to zero hours remaining — a sustainable pace.
- Some work takes longer and some shorter, so it won't be a perfect straight line.
- At the start nothing is done, so the chart starts at the full estimate.
- You can see at a glance whether work is on track.

![Sprint burndown chart](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/04_Scrum/burndown.svg)

*Remaining hours plotted against sprint days; a line staying above the ideal diagonal means the team is behind.*

| Burndown | Likely causes |
|---|---|
| Too slow | Inexperienced developers, hard roadblocks, distractions, bad planning |
| Too fast | Overestimated work (also a planning problem) |

### What Can Go Wrong

| Problem | Description | Remedy |
|---|---|---|
| **Loss of rhythm** | Sprints vary in length, so they feel like arbitrary units chosen by outside forces and are hard to plan | Keep every sprint the same length |
| **Talking chickens** | Chickens ask questions or comment at the daily scrum; allowing useful comments is a slippery slope | Be strict: only pigs speak |
| **Missing pigs** | Flex time and night-working developers mean members miss or are late for daily scrums | Same time and place daily builds rhythm; if many miss often, the meeting is probably too long or straying from the three questions; skipping only for emergencies |
| **Specialised job roles** | Architect, designer, DBA, tester roles undermine "we're all in this together" | Teams needn't be all generalists, but every specialist must accept responsibility for the whole system |
| **Daily scrum for the Scrum Master** | It becomes a status report to the SM, who notes who committed to what and why tasks slipped | The SM is a servant. The scrum coordinates everyone; members commit in front of peers. The SM doesn't rebuke unmet commitments — peers' awareness is enough |
| **Scrum Master assigns work** | Work is assigned instead of signed up for | Self-organisation is fundamental; even occasional assignment undermines developers' responsibility. Teams must feel completely in control of their work |
