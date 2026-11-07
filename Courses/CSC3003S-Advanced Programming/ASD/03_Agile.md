---
tags:
  - advanced-programming
---

# Agile

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD03 Agile.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD03%20Agile.pdf), Johan Bontes, University of Cape Town, pages 1–40
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> The Agile manifesto and principles (and their limits), barely sufficient requirements and user stories, fixed timescales with variable scope, a working product at all times, and pair programming.

> [!note] <span style="color:#ffc778">Examinability</span>
> All material is examinable unless stated otherwise (purple slide topics are not). The exam is mostly about understanding — don't just memorise lists.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The Agile Manifesto|The Agile Manifesto]]
  - [[#The Manifesto Fifteen Years Later|The Manifesto Fifteen Years Later]]
  - [[#Business Reality: Security First|Business Reality: Security First]]
  - [[#The Twelve Agile Principles|The Twelve Agile Principles]]
  - [[#Empowered Teams|Empowered Teams]]
  - [[#Pareto's Law|Pareto's Law]]
  - [[#Barely Sufficient Requirements|Barely Sufficient Requirements]]
  - [[#User Stories|User Stories]]
  - [[#Recording User Stories And Sizing Work|Recording User Stories And Sizing Work]]
  - [[#Incremental Design|Incremental Design]]
  - [[#Fixed Timescale And Budget, Variable Scope|Fixed Timescale And Budget, Variable Scope]]
  - [[#The Agile Development Cycle And Definition Of Done|The Agile Development Cycle And Definition Of Done]]
  - [[#Working Product At All Times|Working Product At All Times]]
  - [[#Pair Programming|Pair Programming]]
  - [[#Code Review|Code Review]]

---

## Core Content

### The Agile Manifesto

#### Definitions

> **Agile Manifesto (2001)**: "We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value: individuals and interactions over processes and tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan. That is, while there is value in the items on the right, we value the items on the left more."

![Agile manifesto values](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/03_Agile/manifesto-values.svg)

*Each value pair keeps the right-hand item but prioritises the left-hand item.*

| Valued more | Over |
|---|---|
| Individuals and interactions | Processes and tools |
| Working software | Comprehensive documentation |
| Customer collaboration | Contract negotiation |
| Responding to change | Following a plan |

Signatories include Kent Beck, Mike Beedle, Arie van Bennekum, Alistair Cockburn, Ward Cunningham, Martin Fowler, James Grenning, Jim Highsmith, Andrew Hunt, Ron Jeffries, Jon Kern, Brian Marick, Robert C. Martin, Steve Mellor, Ken Schwaber, Jeff Sutherland and Dave Thomas.

### The Manifesto Fifteen Years Later

By 2015 the balance had shifted back: the right-hand items (processes, documentation, contracts, plans) proved to matter more than the manifesto suggested. Each side has trade-offs.

**Processes and tools versus individuals and interactions:**

| Aspect | Processes and tools | Individuals and interactions |
|---|---|---|
| Communication | Easy | Hard |
| Division of labour | Clear | Less so |
| Task switching | Few distractions | Many |
| Team structure | Hierarchy | Democracy |

**Waterfall (comprehensive documentation, contract negotiation) versus Agile (working software, customer collaboration):**

| Aspect | Waterfall | Agile |
|---|---|---|
| Communication | Easy | Hard |
| Division of labour | Clear | Not clear |
| Works well for | Known problems | Novel development |
| Final product = plan? | ✓ | ✗ |

### Business Reality: Security First

In 2025 the top three business problems are security, security and security. Security must be addressed in the **architecture**:

- More planning is needed.
- Defined secure patterns must be followed (memory, encryption, authentication).
- Security cannot be "bolted on" in the final iterations.
- It is hard to test for.
- Users don't understand security and don't want it, because more security means less usability.
- Insecure software is a high-probability, high-cost risk, so it must be avoided.

This cuts against Agile's "design as you go" instincts.

### The Twelve Agile Principles

1. **Satisfy the customer** through early and continuous delivery of valuable software.
2. **Welcome changing requirements**, even late in development.
3. **Deliver working software frequently**.
4. Business people and developers must **work together** daily.
5. Build projects around **motivated individuals**; give them the support they need and **trust** them.
6. The most efficient and effective way to convey information is **face-to-face conversation**.
7. **Working software** is the primary measure of progress.
8. Sponsors, developers and users should be able to **maintain a constant pace** indefinitely.
9. Continuous attention to **technical excellence** and good design.
10. **Simplicity** — the art of maximising the amount of work not done — is essential.
11. The best architectures, requirements and designs emerge from **self-organising teams**.
12. The team regularly **reflects** on how to become more effective and adjusts its behaviour.

### Empowered Teams

- The project team must have **sole responsibility** for delivering the product.
- Any outside interference is disruptive and reduces motivation.
- Together, the team must establish and clarify the requirements, prioritise them, agree the tasks to deliver them, and estimate the effort.
- This ensures buy-in and commitment from the outset, and a real sense of ownership when challenges arise.

### Pareto's Law

#### Definitions

> **Pareto's law (80/20 rule)**: Typically about 80% of results come from about 20% of the effort. Named after Vilfredo Pareto (1848–1923).

- The split is arbitrary — it could as well be 75/35, or simply "most/minority".
- Try to focus on the important 20% of effort that gives the best results.
- The problem: no-one knows **which** 20% will deliver 80% of the results.

### Barely Sufficient Requirements

Agile requirements are **barely sufficient**:

- Captured at a high level, piecemeal, **just in time** for each feature to be developed.
- The minimum needed to enable development and testing; minimise time on anything that isn't part of the product.
- Understood well enough to set the scope and give high-level budget estimates.
- Captured in **collaborative workshops** so all team members understand them and can contribute, challenge and understand what's needed and why.

The lecturer's critique of each point:

| Agile claim | Caveat |
|---|---|
| Capture requirements piecemeal, just in time | Only acceptable for low-probability, low-cost risks; a risk assessment is needed |
| Barely sufficient detail | Only for features not yet well understood; you must still understand interactions and security |
| Collaborative workshops where everyone contributes | An extreme form of democracy ("anarchy") that disregards formal and informal power |

### User Stories

#### Definitions

> **User story**: A simple statement, in business language everyone understands, of what a user wants to do with a feature. Similar to a use case but lighter and simpler. Most Agile teams represent each requirement as a user story.

Form:

> As a **[user role]**, I want to **[task]**, so I can **[goal]**.

A story covers the **who, what and why** of a feature — not the **how**. Job-listing site examples:

- As a job seeker, I want to search for a job, so I can advance my career.
- As a recruiter, I want to post a job vacancy, so I can find a new team member.

Capturing stories:

- At the start, capture an initial list of stories up front, useful for estimating and planning.
- Defer the details until the story is prioritised and due for development.
- Users often tell stories about their current system's failings and how things could work better; capture these as user stories as they are told.
- Traditional projects capture them in a lengthy analysis process and a lengthy document — not user-friendly.

**First rule of usability: don't listen to users.**

> "To design the best UX, pay attention to what users do, not what they say. Self-reported claims are unreliable, as are user speculations about future behavior. Users do not know what they want." — Jakob Nielsen

> "A lot of times, people don't know what they want until you show it to them." — Steve Jobs

What Jobs meant: users know what they (don't) want, but don't know what they **need** until you show it to them.

### Recording User Stories And Sizing Work

User stories are written on postcard-sized cards in three parts:

| Part | Content |
|---|---|
| Heading | Name/description, reference numbers, estimated size, etc. |
| Conversation (front) | Background (who, why) and what the system should do; a sketch or diagram; notes on how it should function |
| Acceptance criteria (back) | Test cases that reveal scenarios users, developers or analysts may not have thought of |

A card forces requirements into small, manageable pieces of functionality — single features.

- Cards can be supported by documentation, but keep it to the bare minimum, always in very small units.
- Break requirements into tasks of **at most 16 hours**, preferably **8 hours**, so progress can be measured daily.
- All items are **deliverables**, not activities or tasks: you can see a deliverable to judge its quality and completeness, but you can't see a task.

### Incremental Design

Agile does not follow top-down design (as in Fred Brooks's waterfall view).

| Top-down design | Agile incremental design |
|---|---|
| Time spent on design is worth it if it saves reworking the design many times | Design is always the same size as the system |
| Plan the structure up front | "You can't possibly anticipate the problems and alternatives that will arise once you start coding" |

Critique: that Agile claim describes unknown unknowns, which is **not true for most problems**. If a new need requires major changes, Agile accepts that as the price of flexibility — perhaps the feature wasn't known at the start, or the need might have gone away had it been known.

### Fixed Timescale And Budget, Variable Scope

In Agile development **requirements evolve but timescales are fixed**.

| Traditional development | Agile development |
|---|---|
| Capture all known requirements up front | Assume requirements will change |
| Changes go through change control | However much analysis you do, you can't know what you want until you see and use the software |
| Users are told late changes are expensive, so they include everything they ever dreamed of | External conditions may change while you analyse and design |
| Projects start bloated; users may use only 20% of the product, and no-one knows which 20% | Build the core first |

Business expects teams to deliver the agreed requirements on time, within budget and at acceptable quality. In Agile:

- **scope is variable**; cost and timescale are not;
- this only works if the core, highest-priority features are delivered in the earliest iterations;
- result: fixed budget, fewer resources, fixed launch date.

### The Agile Development Cycle And Definition Of Done

The cycle is **analyse → develop → test → repeat**, one feature at a time, in priority order. Each feature must be fully developed to the point it could ship.

| Advantages |
|---|
| Some risks reduced (though others increase) |
| Higher perceived value: some benefits delivered early |
| More flexibility |
| Better cost management |

#### Definitions

> **Done**: In Agile, "done" means **shippable**. Every feature in an iteration must be 100% complete by its end.

![Definition of done](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/03_Agile/definition-of-done.svg)

*A feature is done only when every check passes and the product owner accepts it.*

A feature is done when:

1. unit tests pass,
2. code is reviewed,
3. acceptance criteria pass,
4. functional tests pass,
5. non-functional requirements are met,
6. the product owner accepts the user story.

Ideally each iteration produces a release. A feature may depend on work in progress, but on its own merit it should be shippable. Finishing each feature before the next avoids a system where several features are "90% complete" or untested.

### Working Product At All Times

- The best way to get user feedback is to give users a product, even a work in progress. Prototypes beat documents.
- Effort spent getting a broken product working again is a missed opportunity for valuable work.

**Agile sandcastles**: waterfall builds a very detailed specification, then a design, then builds and tests, then drowns in change requests ("Err…") before a patched-up deployment. Agile builds a small but complete sandcastle in Sprint 0 and grows it sprint by sprint, so there is always a working castle.

**Prototypes** are an inexpensive way to try out ideas and understand as many issues as possible before the real implementation. Prototyping risky problems raises the chance of always having a working product.

| Prototype class | Purpose |
|---|---|
| **True prototype** | Test implementation to understand a problem before implementing it for real (thrown away) |
| **Skeleton** | Intended to gradually grow into the final solution |

**Continuous integration**:

- Integrate changes continuously, at least daily, so modules fit together and the product keeps working.
- Avoid the bad habit of checking files out and not checking in until the work is "done".
- Gradual change means integration problems and regressions are caught early.

**Nightly builds**:

- Rebuild the software from scratch daily; the result should be an installable product image.
- Include as many automated tests as possible.
- If the build or tests fail, fix that first. No-one integrates more work until the build succeeds again; otherwise bad changes pile up and threaten quality.

**Don't neglect performance**:

| View | Argument |
|---|---|
| Clarity first | Get code clear, then optimise the 1–3% that needs it |
| Performance first | If you don't code for performance from the start, the code will always be slow |

A few critical loops dominate performance — use **profiling tools** to find them.

### Pair Programming

#### Definitions

> **Pair programming**: Two programmers sit together and write every line of code, one at the keyboard and the other supporting. Two programmers plus one computer form the atomic unit of XP development. Pairs form dynamically; development is "egoless".

> **Refactoring**: Improving the quality of code without changing its functionality.

| Advantages |
|---|
| Informal review: every line is seen by at least two people |
| Common ownership: individuals aren't blamed for problems; the team is collectively responsible for the system and for fixing it |
| Spreads knowledge across the team, reducing risk if someone leaves |
| Motivates refactoring, since the whole team benefits |

**Productivity**: similar to two people working independently, because of fewer false starts and less rework, and fewer bugs thanks to informal inspection. Pairing experienced with inexperienced developers helps training, but experienced developers may lose productivity in exchange for quality. Pair for complex tasks, perhaps not simple ones.

| Challenges |
|---|
| Working at a partner's pace is exhausting — too slow and too fast are both tiring |
| Constant communication needs empathy and interpersonal skills |
| Different skill levels make contribution and pace hard to estimate |
| Power dynamics (gender, seniority, race, degree) |
| No time alone — introverts recharge alone |
| Pair rotation causes context switching |

### Code Review

A good code review process also ensures every change is seen by at least one other person. Its challenges, compared with pairing:

- It is easy to do sloppy or superficial reviews.
- The developer may over-rely on the reviewer.
- Little communication between programmer and reviewer.
- **Sunk cost**: the code is already written, so asking for a refactor feels like wasted effort.
- A long gap between making and finding a bug ("what was I thinking when I wrote that?").
