---
tags:
  - advanced-programming
---

# Software Engineering Methods

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)
**Source**: [ASD02 Methods.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD02%20Methods.pdf), Johan Bontes, University of Cape Town, pages 1–40
**Generated**: 2026-11-06

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Faster/better/cheaper (pick two), why software projects fail, naïve approaches (code-and-fix, waterfall), wicked problems, and iterative development.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Estimation Is The Core Problem|Estimation Is The Core Problem]]
  - [[#Faster, Better, Cheaper: Pick Two|Faster, Better, Cheaper: Pick Two]]
  - [[#The Standish CHAOS Report|The Standish CHAOS Report]]
  - [[#Think Big, Act Small|Think Big, Act Small]]
  - [[#Wasted Effort And YAGNI|Wasted Effort And YAGNI]]
  - [[#The Economics Of Adding Features|The Economics Of Adding Features]]
  - [[#Problems: Bad Communication And Crunch|Problems: Bad Communication And Crunch]]
  - [[#Software Entropy And Human Factors|Software Entropy And Human Factors]]
  - [[#Laziness And Choosing A Methodology|Laziness And Choosing A Methodology]]
  - [[#Code And Fix|Code And Fix]]
  - [[#The Waterfall Method|The Waterfall Method]]
  - [[#Wicked Problems And The Problem Matrix|Wicked Problems And The Problem Matrix]]
  - [[#Change Gets Exponentially More Expensive|Change Gets Exponentially More Expensive]]
  - [[#Modern Processes: Prototyping And RAD|Modern Processes: Prototyping And RAD]]
  - [[#Iterative Development|Iterative Development]]
  - [[#Iterative Method Flavours|Iterative Method Flavours]]

---

## Core Content

### Estimation Is The Core Problem

- The most common problem in software systems is not **construction** but **estimation**.
- Projects fail to meet cost and schedule because those **targets are wrong**.
- Costing software is difficult, and we know little about accurate estimation, so targets are unreasonable.
- Targets are often set by the people least able to make them: marketers, managers and customers.
- Communicating abstract or conceptual ideas is hard.

### Faster, Better, Cheaper: Pick Two

In the 1990s NASA adopted the slogan "Faster, better, cheaper". After a series of unsuccessful projects, they abandoned it: all three can't be satisfied at once. Software engineers restate the goal as **"Faster, better, cheaper: pick 2 out of 3."**

![Faster, better, cheaper: pick two](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/pick-two.svg)

*The project triangle: time, cost, and scope & quality. Fixing two determines the third.*

| Corner | Meaning |
|---|---|
| Time | Faster |
| Scope & quality | Better |
| Cost | Cheaper |

### The Standish CHAOS Report

The Standish Group's CHAOS Report (2015) surveys project outcomes.

Projects meeting each target (FY2011–2015):

| Target | Yes | No |
|---|---|---|
| On budget | 44% | 56% |
| On time | 40% | 60% |
| On target (scope) | 56% | 44% |

Traditional resolution for all projects:

| Outcome | 2011 | 2012 | 2013 | 2014 | 2015 |
|---|---|---|---|---|---|
| Successful | 39% | 37% | 41% | 36% | 36% |
| Challenged | 39% | 46% | 40% | 47% | 45% |
| Failed | 22% | 17% | 19% | 17% | 19% |

Resolution by project size:

| Size | Successful | Challenged | Failed |
|---|---|---|---|
| Grand | 6% | 51% | 43% |
| Large | 11% | 59% | 30% |
| Medium | 12% | 62% | 26% |
| Moderate | 24% | 64% | 12% |
| Small | 61% | 32% | 7% |

Resolution by method (all sizes):

| Method | Successful | Challenged | Failed |
|---|---|---|---|
| Agile | 39% | 52% | 9% |
| Waterfall | 11% | 60% | 29% |

**Caveat**: Standish's methods have been increasingly criticised. Eveleens and Verhoef ("The Rise and Fall of the Chaos Report Figures", *IEEE Software*, 2010) argue the figures for individual organisations don't reflect reality and are highly influenced by forecasting biases, so any aggregation is unreliable.

### Think Big, Act Small

"Just say no" to large projects:

- The secret to project success is to **limit size and complexity**; these outweigh all other success factors.
- Break large projects into a sequence of smaller ones, prioritised by direct business value.
- Use stable, full-time, cross-functional teams following a disciplined approach.
- The quick solution is to say no to large projects; more sensibly, adopt a **small-project strategy** — lower cost, with fewer defects.
- Projects too often get too big to succeed. Teams are constantly asked to do more for less, but the real key to success is **doing less for less**.

### Wasted Effort And YAGNI

#### Definitions

> **YAGNI ("You Ain't Gonna Need It")**: Build only what you need now; avoid speculative development.

> **Gold plating (bells and whistles)**: Adding features or polish beyond what is required.

Feature usage:

| Used | Share of features |
|---|---|
| Always | 7% |
| Often | 13% |
| Sometimes | 16% |
| Rarely | 19% |
| Never | 45% |

Almost two thirds of features are rarely or never used. Stop developing them and productivity could double.

YAGNI counters thinking like "I'm sure I'll need extra functionality later, so I'll write it now". Speculative development adds complexity to the code prematurely.

### The Economics Of Adding Features

![Economics of adding features](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/feature-economics.svg)

*Returns from features grow roughly linearly while production cost grows exponentially, so after some point extra features give negative return on investment.*

| Project type | Shape |
|---|---|
| Profitable | Returns outpace costs throughout |
| Ultimately unprofitable | Early positive ROI, then features become a drag and ROI turns negative |

The cost curve of software is **exponential**:

- Fred Brooks attributes this to the **cost of communication** — e.g. customer and developer must understand each other perfectly.
- New projects succeed because the cost curve is still flat.
- Once costs start rising, they quickly overwhelm the value added by new features.
- This applies to maintenance costs, not just new features.

### Problems: Bad Communication And Crunch

**Bad communication** — *Age of Booty* (Certain Affinity, Max Hoberman): there were many disconnects between the perceived and actual state of the game. Designers kept refining plans for sophisticated features (matchmaking, party support) long after programmers had drastically simplified or cut them. Lack of attention, poor communication and wishful thinking meant designers believed features were far more advanced than they were, and only found out very late.

**Crunch** — *Drawn to Life* (5th Cell, Joseph Tringali): a "perfect storm" of inexperience with the platform, an ambitious game and a schedule that was too short. With little pre-production, the team played catch-up from day one, taking shortcuts and working late weekdays and Saturdays for the whole second half of the project.

- **Crunch** is a side effect of other problems and a cause of **burnout**.

### Software Entropy And Human Factors

#### Definitions

> **Entropy**: A measure of disorder in a physical system.

> **Software entropy**: A measure of code complexity; it tends to increase over time ("software rot").

> **Technical debt**: Accumulated structural degradation from shortcuts, fixes and enhancements that makes future change harder.

- Over-scoped design adds complexity at the start.
- Bug fixes and enhancements increase complexity and degrade structure (technical debt).
- Most applications grow by 5–10% a year.
- Entropy makes code hard to change, fix and understand.
- The cure: **YAGNI at the start** and **refactoring as you go**.

Human factors that waste effort:

| Factor | Meaning |
|---|---|
| **Yak shaving** | Pointless work only tangentially related to the goal |
| **Procrastination** ("student syndrome") | Starting work only near the deadline |
| **Gold plating** | Unneeded extras |
| **Task switching** | Losing time and focus moving between tasks |

### Laziness And Choosing A Methodology

"We'll solve it later" is costly:

- **Essential problems** should be specified in the early phases. Otherwise you do the requirements work later, plus extra tear-down and repair.
- **Accidental problems** should be flagged and analysed when found:
  - solution known → refactor;
  - solution unknown → back to requirements.

| Methodology | Approach | Risk | Fix |
|---|---|---|---|
| Agile | One big project → many small iterative projects | Too little preparation; late fixes cost up to 100× more | Take time to work out the basics, e.g. throw-away prototypes to shake out wicked problems |
| Waterfall | One big project — "eat the whole elephant" | Requirements and analysis must be near perfect | Use only when the problem is well understood (few accidental problems); reuse lessons from earlier projects; prototype anything not fully worked out |

### Code And Fix

Code-and-fix is the naïve first approach — really the **absence** of a methodology.

- Little or no planning; dive straight into implementation.
- Reactive; ends with bugs.
- If bugs multiply faster than they can be fixed: a **death spiral**, and the project is cancelled.
- The non-fix is **crunch time**, sometimes worn as a badge of honour, but it causes burnout.

### The Waterfall Method

#### Definitions

> **Waterfall method**: A sequential process — requirements specification, analysis, design, implementation, testing and integration, operation and maintenance — where each phase completes before the next begins.

![Waterfall method](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/waterfall.svg)

*Each phase flows into the next with no way back, which suits fully understood problems only.*

Waterfall comes from building projects, where it suits because:

- changes are too hard or expensive, so only minor tweaks are possible;
- the problem is fully understood and can be fully simulated;
- the core structure is preserved and mostly standard patterns are used.

**Case: FIU pedestrian bridge**

| Phase | What happened |
|---|---|
| Requirements | "Must have redundancy" (i.e. use a traditional design), but FIU wanted it to "be unique" |
| Design | A single-truss design, the first and only one in the world; the primary engineer's calculations were wrong and the second reviewer missed it |
| Implementation | Built as per the faulty design |
| Testing | Cracks appeared; the fix (loosen and re-tension a tensioner) caused the bridge to collapse |

Why pure waterfall cannot work for software:

- Every preceding phase must be perfect, but software is infinitely changeable.
- The pure model allows no going back, yet coding, testing, user acceptance, operational and maintenance issues can all require redesign.
- Big projects fail much more often than small ones.

### Wicked Problems And The Problem Matrix

#### Definitions

> **Wicked problem**: An "unknown unknown" — a problem that cannot be anticipated and only becomes visible late (in implementation, testing or operation). Software is full of them, because it is much more complex than hardware.

The Tacoma Narrows bridge collapse (7 November 1940) is the classic physical example: a failure mode nobody had foreseen.

| | Solved: yes, clear | Solved: no, foggy |
|---|---|---|
| **Foreseen: yes** | **Known known** — use a standard solution | **Unknown known** — refactor |
| **Foreseen: not yet** | **Known unknown** — fix in requirements/analysis | **Unknown unknown** (wicked) — go back to the start |

Known unknowns show up during requirements and analysis; unknown unknowns show up during coding, testing or deployment.

### Change Gets Exponentially More Expensive

- The cost of change rises exponentially with time, which motivates conservative, fear-driven design.
- A change late in the process can cost **1000 times** as much as early on:

| Stage | Cost of the same change |
|---|---|
| Writing the spec | 5 minutes |
| Programming the feature | 2 days |
| Testing before deployment | 2 weeks |
| Patching after deployment | 1 month |

### Modern Processes: Prototyping And RAD

Modern processes are lighter than waterfall:

- less documentation and fewer procedures;
- multiple versions released during development;
- parallel development and prototypes;
- "**skateboard**" first: build only what's required, no extra requirements;
- **design for change**, because change is inevitable.

**Prototyping** cycles between requirements, a prototype and tests.

**Rapid Application Development (RAD)** cycles: requirements → design → develop → deploy (test) → learn (reflect) → requirements.

### Iterative Development

#### Definitions

> **Iterative (incremental) development**: A process that reaches the goal through a series of ever-improving delivery cycles.

The cycle: plan → develop → test → release → feedback → plan …

![Iterative cycle](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/iterative-cycle.svg)

*Each loop produces a working version and user feedback that steers the next one.*

![Iterative steering](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/iterative-steering.svg)

*Each iteration corrects course toward the real target using feedback, instead of aiming once and hoping.*

**The big difference**: instead of 18 months to create and evaluate one big project, build and show a new version to users every 2–4 weeks. This requires:

- team members close together and close to the customer;
- agreement on good ideas in hours, not months;
- teams that become experts through intense hands-on problem solving and testing.

The result is a real system meeting users' real, tested needs, not "perceived" needs.

| Benefits | Danger |
|---|---|
| Favoured by small start-ups | Intense focus on only high-priority features means many alternative concepts are never explored |
| Greatly reduces the risk of failure — with only one shot at success, you steer using information instead of launching blindly | Good ideas can be lost: you may iterate to a **small success** and miss bigger opportunities elsewhere |
| Long term: more value sooner, with lower overall risk | |

### Iterative Method Flavours

| Method | Originators | Key features |
|---|---|---|
| **Agile** ("Agile Manifesto") | — | Mini software projects; face-to-face communication |
| **RAD** (Rapid Application Development) | James Martin | Voice of the customer; collaborative; rigid schedule |
| **XP** (Extreme Programming) | Kent Beck | Design on the fly; unit testing of all code; pair programming; refactoring |
| **Scrum** | Takeuchi, Nonaka, Schwaber | Teams "scrum down" in short iterations (sprints); empirical process |
