---
tags:
  - advanced-programming
---

# Agile

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD03 Agile.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD03%20Agile.pdf), Johan Bontes, University of Cape Town, PDF pages 1–40  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: the Agile manifesto and its critique, empowered teams, barely sufficient requirements and user stories, fixed timescales, a working product at all times, and pair programming.

> [!tip] <span style="color:#5ad4b5">What is examinable</span>
> All ASD material is examinable unless marked otherwise. **Purple** slide text is not examinable, and **blue** terms are highly likely to be examined. The exam is mostly about understanding, so do not memorise lists.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Agile Manifesto|The Agile Manifesto]]
  - [[#The Manifesto 15 Years Later|The Manifesto 15 Years Later]]
  - [[#The Reality Of Business In 2025: Security|The Reality Of Business In 2025: Security]]
  - [[#The 12 Agile Principles|The 12 Agile Principles]]
  - [[#Teams Must Be Empowered|Teams Must Be Empowered]]
  - [[#Pareto's Law (80/20)|Pareto's Law (80/20)]]
  - [[#Barely Sufficient Requirements|Barely Sufficient Requirements]]
  - [[#User Stories|User Stories]]
  - [[#Recording User Stories And Task Size|Recording User Stories And Task Size]]
  - [[#Incremental Design|Incremental Design]]
  - [[#Fixed Timescale And Budget, Variable Scope|Fixed Timescale And Budget, Variable Scope]]
  - [[#The Agile Development Cycle|The Agile Development Cycle]]
  - [[#Done Means Done|Done Means Done]]
  - [[#Working Product At All Times|Working Product At All Times]]
  - [[#Pair Programming|Pair Programming]]
  - [[#Code Review|Code Review]]

---

## Core Content

### The Agile Manifesto

#### Definitions

> **Agile manifesto** (2001): "We are uncovering better ways of developing software by doing it and helping others do it." It states four value preferences.

![Agile manifesto values](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/03_Agile/manifesto-values.svg)

*"While there is value in the items on the right, we value the items on the left more."*

Its signatories were Kent Beck, Mike Beedle, Arie van Bennekum, Alistair Cockburn, Ward Cunningham, Martin Fowler, James Grenning, Jim Highsmith, Andrew Hunt, Ron Jeffries, Jon Kern, Brian Marick, Robert C. Martin, Steve Mellor, Ken Schwaber, Jeff Sutherland and Dave Thomas.

### The Manifesto 15 Years Later

By 2015 practice had moved towards **DevOps**: a continuous loop joining development and operations.

![DevOps loop](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/03_Agile/devops-shift.svg)

*Dev (plan, code, build, test) and Ops (release, deploy, operate, monitor) form one loop. "Shift left" moves design verification earlier; "shift right" emphasises performance, resilience and reliability.*

The lecturer critiques the manifesto's preferences:

| Factor | Processes and tools | Individuals and interactions |
|---|---|---|
| Communication | Easy | Hard |
| Division of labour | Clear | Less so |
| Task switching | Few distractions | Many |
| Team structure | Hierarchy | Democracy |

| Factor | Waterfall (documentation, contracts) | Agile (working software, collaboration) |
|---|---|---|
| Communication | Easy | Hard |
| Division of labour | Clear | Not clear |
| Works well for | Known problems | Novel development |
| Final = plan? | Yes | No |

![Communication paths](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/03_Agile/communication-paths.svg)

*Communication paths grow as $n(n-1)/2$, so person-to-person interaction gets hard as teams grow. That is why individuals-and-interactions approaches favour small teams.*

### The Reality Of Business In 2025: Security

The top three problems are security, security and security. Security must be addressed **in the architecture**:

- More planning is needed.
- Defined secure patterns must be followed (memory, encryption, authentication).
- Security cannot be "bolted on" in the final iterations.
- It is hard to test for.
- Users do not understand security and don't want it, because more security means less usability.
- Insecure software has high probability and high cost, so the risk must be **avoided**.

This is a limit of pure Agile: deferring design is dangerous for cross-cutting concerns like security.

### The 12 Agile Principles

1. Satisfy the customer through early and continuous delivery of valuable software.
2. Welcome changing requirements, even late in development.
3. Deliver working software frequently.
4. Business people and developers must work together.
5. Build projects around motivated individuals; give them the support they need and trust them.
6. The most efficient and effective method of conveying information is face-to-face conversation.
7. Working software is the primary measure of progress.
8. Sponsors, developers and users should be able to maintain a constant pace indefinitely.
9. Continuous attention to technical excellence and good design.
10. Simplicity, the art of maximising the amount of work *not* done, is essential.
11. The best architectures, requirements and designs emerge from self-organising teams.
12. The team regularly reflects on how to become more effective and adjusts its behaviour.

### Teams Must Be Empowered

- The project team must have **sole responsibility** for delivering the product.
- Any interference is disruptive and reduces motivation.
- Together, the team must:
  1. establish and clarify the requirements
  2. prioritise them
  3. agree on the tasks to deliver them
  4. estimate the effort
- This secures **buy-in and commitment** from the start, and when challenges arise the team feels real **ownership**.

### Pareto's Law (80/20)

#### Definitions

> **Pareto's law (80/20 rule)**: Typically about 80% of results come from about 20% of the effort. The split is arbitrary; it could be 75/25 or simply "most/minority". Named after Vilfredo Pareto (1848–1923).

- Focus on the important 20% of effort that gives the best results.
- **Problem**: no one knows in advance which 20% will deliver 80% of the results.

### Barely Sufficient Requirements

#### Definitions

> **Barely sufficient requirements**: The minimum needed to enable development and testing, captured at a high level, piecemeal and **just-in-time** for each feature.

| Agile practice | Lecturer's qualification |
|---|---|
| Capture requirements at a high level, piecemeal, just-in-time | Only for low-probability, low-cost risks; a risk assessment is needed |
| Barely sufficient: minimise time on anything not part of the product | Only for features that are not well understood |
| Understand enough for scope and high-level budget estimates | You must also understand interaction and security aspects |
| Capture requirements in collaborative workshops so everyone can contribute and challenge | An extreme form of democracy ("aka anarchy") that disregards formal and informal power |

### User Stories

#### Definitions

> **User story**: A simple statement in business language of what a user wants to do with a feature. It is similar to a use case but lighter and simpler.

The template:

> As a **[user role]**, I want to **[task]**, so I can **[goal]**.

It focuses on the **who, what and why**, not *how*. Two examples from a job site:

- As a **job seeker**, I want to **search for a job**, so I can **advance my career**.
- As a **recruiter**, I want to **post a job vacancy**, so I can **find a new team member**.

**Capture an initial list at the start**, which is useful for estimating and planning. Defer the details until a story is prioritised and due for development. Users often tell stories about failings of their current system and how things could work better; capture these as user stories as they are told. Traditional projects bury such stories in a lengthy, user-unfriendly analysis document.

**Don't (just) listen to users**:

- "Pay attention to what users do, not what they say … Users do not know what they want." — Jakob Nielsen
- "A lot of times, people don't know what they want until you show it to them." — Steve Jobs
- The lecturer's reading: users know what they don't want, but not what they **need**, until you show them.

### Recording User Stories And Task Size

User stories are written on postcard-sized cards with three parts:

| Part | Contents |
|---|---|
| **Heading** | Name/description, reference numbers, estimated size |
| **Conversation** (front) | Background (who, why), what the system should do, a sketch, notes on how it should work |
| **Acceptance criteria** (back) | Test cases covering scenarios users, developers or analysts may not have thought of |

- Cards force requirements into small, manageable, **single features**.
- Supporting documentation is kept to the bare minimum, in very small units.
- Break requirements into tasks of **$\le 16$ hours, preferably 8**, so progress can be measured daily.
- All items are **deliverables, not activities**: you can see a deliverable and judge its quality and completeness, but you cannot see a task.

### Incremental Design

| Top-down design (Fred Brooks, waterfall) | Agile incremental design |
|---|---|
| Time in design is worth it if it saves reworking the design many times | Design is always the same size as the system |
| Plan the whole design first | "You can't possibly anticipate the problems and alternatives that will arise once you start coding" |

The lecturer notes that this argument assumes unknown unknowns, which is **not true for most problems**. If a new need requires major changes, that is the trade-off for flexibility. Perhaps the feature was unknown at the start, or it would have disappeared had it been known.

### Fixed Timescale And Budget, Variable Scope

Traditional development captures all known requirements up front. Changes go through **change control**, and users are told late changes are expensive, so they include everything they ever dreamed of. But:

- users may use only about 20% of the product, so many projects start bloated
- no one knows at the outset which 20%
- you cannot think of everything; things change and are understood differently

Agile **assumes changing requirements**. You cannot really know what you want until you see and use the software, and conditions can change during analysis.

| | Traditional | Agile |
|---|---|---|
| Fixed | Scope (requirements) | Cost and timescale |
| Variable | Cost and time (overruns) | Scope |
| Requires | Full up-front analysis | Delivering the core, highest-priority features in the earliest iterations |
| Result | Bloat, change control | Fixed budget, fewer resources, fixed launch date |

### The Agile Development Cycle

The cycle is **analyse → develop → test → repeat**, done for each feature, one feature at a time, in **priority order**. Each feature must be fully developed to the point it could ship.

- Some risks are reduced and others increased.
- It increases perceived value by delivering some benefits early.
- It gives more flexibility and better cost management.

### Done Means Done

#### Definitions

> **Done**: In Agile, "DONE" means **shippable**. Features in an iteration must be 100% complete by its end.

![Definition of done](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/03_Agile/definition-of-done.svg)

*A story is done only when unit tests pass, the code is reviewed, acceptance criteria and functional tests pass, non-functional requirements are met, and the Product Owner accepts it.*

- Ideally each iteration results in a release.
- A feature may rely on work in progress, but on its own merit it should be shippable.
- Finishing each feature before the next avoids many features sitting at 90% complete or untested.

### Working Product At All Times

The best way to get user feedback is to give them a product, even work in progress; a prototype is better than a document. Effort spent restoring a broken product is a missed opportunity for valuable work.

#### Definitions

> **True prototype**: A test implementation to understand a problem before implementing it for real.

> **Skeleton prototype**: A prototype intended to gradually turn into the final solution.

> **Continuous integration**: Integrating changes frequently (at least daily) so modules fit together and regressions are caught early.

> **Nightly build**: Rebuilding the whole product from scratch daily into an installable image, with as many automated tests as possible.

| Practice | Key points |
|---|---|
| **Prototypes** | An inexpensive way to try ideas and understand issues before the real implementation; prototype risky problems |
| **Continuous integration** | Avoid the habit of keeping files checked out until done; integrate daily so problems surface early |
| **Nightly builds** | If the build or tests fail, fix that first; no one integrates more work until it succeeds, or bad changes accumulate |
| **Performance** | Don't neglect it |

On performance, one camp says get clarity first and then optimise the 1–3% of code that needs it. The other says code for performance from the start or the code will always be slow. A few critical loops dominate, so use **profiling tools**.

### Pair Programming

#### Definitions

> **Pair programming**: Two programmers sit together and write every line of code on one computer. One types and the other supports. "2 programmers + 1 computer" is the atomic unit of XP development.

> **Refactoring**: Improving the quality of code without altering its functionality.

Pairs are formed dynamically, and the practice is **egoless** development.

| Advantages | Challenges |
|---|---|
| Informal review: every line is seen by at least two people | Working at a partner's pace (too slow or too fast) is exhausting |
| Common ownership: individuals are not blamed; the team is collectively responsible | Constant communication needs empathy and interpersonal skills |
| Spreads knowledge, reducing risk if someone leaves | Different skill levels make contribution and pace hard to estimate |
| Motivates refactoring, since the whole team benefits | Power dynamics (gender, seniority, race, degree) |
| Pairing experienced with inexperienced developers trains people | No alone time (introverts recharge alone) |
| Fewer false starts, less rework, fewer bugs | Pair rotation causes context switching |

**Productivity** is similar to two people working independently, thanks to fewer false starts, less rework and less bug fixing. Experienced developers may lose some productivity in exchange for quality. Pair on complex tasks, perhaps not simple ones.

### Code Review

A good code review process ensures every change is reviewed by at least one other person. Its weaknesses compared with pairing:

- Reviews are easily sloppy or superficial.
- Developers over-rely on the reviewer.
- There is little communication between programmer and reviewer.
- **Sunk cost**: the code is already done, so asking for a refactor feels like wasted effort.
- There is a long gap between making and finding bugs ("what was I thinking?").
