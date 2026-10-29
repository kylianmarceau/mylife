---
tags:
  - advanced-programming
---

# Software Engineering Methods

**Subject**: CSC3003S Advanced Programming — Advanced Software Development (ASD)  
**Source**: [ASD02 Methods.pdf](../../../Sources/CSC3003S%20-%20Advanced%20Programming/ASD/ASD02%20Methods.pdf), Johan Bontes, University of Cape Town, PDF pages 1–40  
**Generated**: 2026-10-24

> [!info] <span style="color:#66b3ff">Lecture reference</span>
> Complete source-based study notes: the project triangle, why projects fail, naïve approaches (code-and-fix, waterfall), wicked problems, and iterative development.

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Estimation Is The Core Problem|Estimation Is The Core Problem]]
  - [[#The Software Engineering Triangle|The Software Engineering Triangle]]
  - [[#Standish CHAOS Report Findings|Standish CHAOS Report Findings]]
  - [[#Think Big, Act Small|Think Big, Act Small]]
  - [[#Wasted Effort And YAGNI|Wasted Effort And YAGNI]]
  - [[#Economics Of Adding Features|Economics Of Adding Features]]
  - [[#Problems: Bad Communication And Crunch|Problems: Bad Communication And Crunch]]
  - [[#Software Entropy|Software Entropy]]
  - [[#Human Factors And Laziness|Human Factors And Laziness]]
  - [[#Agile Versus Waterfall: Risks And Fixes|Agile Versus Waterfall: Risks And Fixes]]
  - [[#Code And Fix|Code And Fix]]
  - [[#The Waterfall Method|The Waterfall Method]]
  - [[#Why Pure Waterfall Fails For Software|Why Pure Waterfall Fails For Software]]
  - [[#Wicked Problems And The Problem Matrix|Wicked Problems And The Problem Matrix]]
  - [[#The Cost Of Change|The Cost Of Change]]
  - [[#More Modern Processes|More Modern Processes]]
  - [[#Iterative Development|Iterative Development]]
  - [[#Benefits And Dangers Of Iteration|Benefits And Dangers Of Iteration]]
  - [[#Iterative Method Flavours|Iterative Method Flavours]]

---

## Core Content

### Estimation Is The Core Problem

The most common problem in software is not construction but **estimation**.

- Projects miss cost and schedule targets because **the targets are wrong**.
- Costing software is difficult, and little is known about accurate estimation, so targets are unreasonable.
- Targets are often set by the people least able to make them: marketers, managers and customers.
- Communicating abstract or conceptual ideas is hard. It can be hard to explain the difference between the easy and the virtually impossible (xkcd: checking whether a photo is in a national park is easy; checking whether it is of a bird needs a research team and five years).

### The Software Engineering Triangle

#### Definitions

> **Software engineering (project) triangle**: Time, cost, and scope/quality trade off against each other. You can fix at most two.

In the 1990s NASA adopted "Faster, better, cheaper". After a series of failed projects it abandoned the slogan, because all three cannot be satisfied in one project. Software engineers restate it as "**Faster, better, cheaper: pick 2 out of 3.**"

![Pick two](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/pick-two.svg)

*Any two corners are achievable at the expense of the third. All three at once is not possible.*

| Choose | Sacrifice | Result |
|---|---|---|
| Good + fast | Cost | Expensive |
| Good + cheap | Time | Slow |
| Fast + cheap | Quality | Low quality |

### Standish CHAOS Report Findings

Traditional resolution of all projects:

| Outcome | 2011 | 2012 | 2013 | 2014 | 2015 |
|---|---:|---:|---:|---:|---:|
| Successful | 39% | 37% | 41% | 36% | 36% |
| Challenged | 39% | 46% | 40% | 47% | 45% |
| Failed | 22% | 17% | 19% | 17% | 19% |

FY2011–2015: 44% of projects were on budget, 40% on time, and 56% on target.

Resolution by project size:

| Size | Successful | Challenged | Failed |
|---|---:|---:|---:|
| Grand | 6% | 51% | 43% |
| Large | 11% | 59% | 30% |
| Medium | 12% | 62% | 26% |
| Moderate | 24% | 64% | 12% |
| Small | 61% | 32% | 7% |

Large, complex projects: 2% successful, 42% challenged, 56% failed.

| All-size projects | Successful | Challenged | Failed |
|---|---:|---:|---:|
| Agile | 39% | 52% | 9% |
| Waterfall | 11% | 60% | 29% |

> [!warning] <span style="color:#ffc778">Criticism of Standish</span>
> Eveleens and Verhoef ("The Rise and Fall of the Chaos Report Figures", *IEEE Software*, 2010) argue that the figures are highly influenced by forecasting bias. Because the underlying data has unknown bias, any aggregation of it is unreliable.

### Think Big, Act Small

The secret to project success is to **limit size and complexity**. Size and complexity outweigh all other success factors.

- Break large projects into a **sequence of smaller ones**, prioritised by direct business value.
- Use stable, full-time, cross-functional teams that follow a disciplined approach.
- Quick solution: just say no to large projects. More sensibly, adopt a small-project strategy, which gives lower cost and fewer defects.
- Projects too often get too big to succeed. Teams are constantly asked to do more for less, but the real key is **doing less for less**.

### Wasted Effort And YAGNI

#### Definitions

> **YAGNI (You Ain't Gonna Need It)**: Build only what you need now. Avoid speculative development.

> **Gold plating** (bells and whistles): Adding features beyond what is required.

> **Speculative development**: Writing functionality now because "I'm sure I'll need it later".

| Feature usage | Share |
|---|---:|
| Always | 7% |
| Often | 13% |
| Sometimes | 16% |
| Rarely | 19% |
| Never | 45% |

Almost two-thirds of features are never or rarely used. Stop building them and productivity could roughly double. Speculative development adds complexity to code prematurely.

### Economics Of Adding Features

![Economics of adding features](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/feature-economics.svg)

*If cost grows linearly, returns keep outpacing it. Real production cost grows exponentially and eventually overtakes the returns, giving negative ROI.*

- **Profitable project**: returns outpace costs.
- **Ultimately unprofitable project**: features become a drag.
- **Fred Brooks** attributes the exponential cost curve to the **cost of communication**: for example, customer and developer must understand each other perfectly.
- New projects succeed while the cost curve is still flat. Once costs rise, they quickly overwhelm the value of new features.
- This applies to maintenance costs as well as new features.

### Problems: Bad Communication And Crunch

#### Definitions

> **Crunch**: Sustained, consistent overtime to meet a deadline. It is a side effect of other problems and a cause of burnout.

**Bad communication** (*Age of Booty*, Certain Affinity). The perceived and actual state of the game kept disconnecting. Designers kept refining matchmaking and party support long after programmers had simplified or cut those systems. Lack of attention, poor communication and wishful thinking meant designers found out the reality only very late.

**Crunch** (*Drawn to Life*, 5th Cell). "Consistent overtime is not fun." The team worked late weekdays and Saturdays for the whole second half of the project. The causes were a "perfect storm": inexperience with the platform, an ambitious game, a schedule that was too short, and little pre-production. They played catch-up from day one and took too many shortcuts.

### Software Entropy

#### Definitions

> **Entropy**: A measure of disorder in a physical system.

> **Software entropy**: A measure of code complexity, which tends to increase over time (also called software rot).

> **Technical debt**: Accumulated structural degradation from quick fixes and enhancements that must eventually be "repaid".

- An over-scoped design adds complexity at the start.
- Bug fixes and enhancements increase complexity and degrade structure.
- Most applications grow by 5–10% a year.
- Entropy makes changes and fixes hard and makes the code hard to understand.
- **Cure**: YAGNI at the start, and refactoring as you go.

### Human Factors And Laziness

| Factor | Meaning |
|---|---|
| **Yak shaving** | Pointless work only tangentially related to the goal |
| **Procrastination** | "Student syndrome": starting only at the last moment |
| **Gold plating** | Adding unrequired extras |
| **Task switching** | Losing time and focus moving between tasks |

**"We'll solve it later"**:

- **Essential problems** should be specified in early phases. Otherwise the requirements work is done later, plus extra tear-down and repair.
- **Accidental problems** should be flagged and analysed when found:
  - solution known: refactor
  - solution unknown: go back to requirements

### Agile Versus Waterfall: Risks And Fixes

| | Agile | Waterfall |
|---|---|---|
| Shape | One big project becomes many small iterative projects | One big project: "eat the whole elephant" |
| Use when | Requirements are uncertain | The problem is well understood (few accidental problems) |
| Risk | Too little preparation; late fixes cost about 100× more | Preparation phases (requirements, analysis) must be near-perfect |
| Fix | Take time to figure out the basics, e.g. throw-away prototypes to shake out wicked problems | Use all the learnings from previous projects; prototype anything not fully worked out |

### Code And Fix

#### Definitions

> **Code and fix**: The naïve first approach, really the absence of a methodology. There is little or no planning, and development dives straight into implementation.

- It is reactive and ends with bugs.
- If bugs multiply faster than they are fixed, you get a **"death spiral"** and the project is cancelled.
- The non-fix is **crunch time**, sometimes seen as a badge of honour, but it leads to burnout.

### The Waterfall Method

#### Definitions

> **Waterfall method**: A sequential process in which each phase completes before the next begins, as in building construction.

![Waterfall method](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/waterfall.svg)

*Analysis → requirements → design → implementation → testing → operation. It works for buildings, which use standard patterns, are fully understood and can be fully simulated, so going back up is rarely needed.*

**FIU pedestrian bridge (2018) case study**:

| Phase | What happened |
|---|---|
| Analysis | "Must have redundancy", which in practice meant use a traditional design |
| Requirements | FIU: "Must be unique", giving a single-truss design, the first and only one in the world |
| Design | Primary engineer made wrong calculations; the second reader was "sleeping on the job" |
| Implementation | Built as per the faulty design |
| Testing | Cracks appeared; the fix was to loosen and re-tension a tensioner |
| Operation | After loosening, the bridge collapsed |

### Why Pure Waterfall Fails For Software

- Preceding phases must be perfect, but software is infinitely changeable.
- The pure model allows no "go-around". That makes sense for buildings but not software:
  - coding problems may require redesign
  - testing issues may require redesign
  - user acceptance, operational and maintenance issues may all require it too
- Big projects fail much more often than small ones.

### Wicked Problems And The Problem Matrix

#### Definitions

> **Wicked problem**: An *unknown unknown*. It cannot be anticipated, is not yet solved, and becomes visible only late, in implementation, testing or operation.

Software is full of wicked problems because it is much more complex than hardware. An engineering example is the Tacoma Narrows Bridge collapse (7 November 1940), caused by an effect nobody had foreseen.

| Solved? \ Foreseen? | Yes, clear | No, foggy |
|---|---|---|
| **Yes** | **Known known**: use the standard solution | **Unknown known**: refactor |
| **Not yet** | **Known unknown**: fix in requirements/analysis | **Unknown unknown**: go back to the start |
| **Shows up at** | Requirements/analysis | Coding/testing/deployment |

### The Cost Of Change

The cost of change increases exponentially with time. Fear of change motivates conservative design decisions. A late change can cost **1000×** an early one:

| Stage | Effort |
|---|---|
| Write a spec | 5 minutes |
| Program the feature | 2 days |
| Test before deployment | 2 weeks |
| Patch a problem after deployment | 1 month |

### More Modern Processes

- **Lighter than waterfall**: less documentation, fewer procedures.
- **Release multiple versions** during development: parallel development, prototypes.
- **Skateboard**: do only what is required, with no extra requirements (build a usable skateboard before the car).
- **Design for change**: change is inevitable.

### Iterative Development

#### Definitions

> **Iterative (incremental) software development**: A process that reaches the goal in a series of ever-improving delivery cycles.

> **Prototyping**: Repeatedly cycling requirements → prototype → tests.

> **Rapid Application Development (RAD)**: Cycling requirements → design → develop → deploy (test) → learning (reflect).

1. Plan development.
2. Undertake development.
3. Generate a prototype.
4. Get user feedback.
5. Develop again.

![Iterative cycle](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/iterative-cycle.svg)

*Plan → develop → test → release, with user feedback starting the next iteration.*

The big difference: instead of 18 months to build and evaluate one big project, build and show a new version every **2–4 weeks**. This requires:

- team members close together and close to the customer
- agreeing on good ideas in hours, not months
- teams that become experts through intense hands-on problem solving and testing

The result meets users' **real, tested** needs, not "perceived" needs.

![Iterative steering](../../../diagrams/CSC3003S-Advanced%20Programming/ASD/02_Software_Engineering_Methods/iterative-steering.svg)

*Each iteration is evaluated (a green light), the target is re-estimated, and the course is adjusted until v1.0 succeeds.*

### Benefits And Dangers Of Iteration

| Benefits | Danger |
|---|---|
| Favoured by start-ups; greatly reduces the risk of failure | The intense focus on high-priority features means alternative concepts never get explored |
| With only one shot at success, you steer using information rather than launching blindly | Good ideas can be lost; you may reach a "small success" while missing bigger opportunities |
| Long term: more value sooner, with lower overall risk | |

### Iterative Method Flavours

| Method | Originator | Key features |
|---|---|---|
| **Agile** | Agile Manifesto | Mini software projects; face-to-face communication |
| **RAD** | James Martin | Voice of the customer; collaborative; rigid schedule |
| **XP** (Extreme Programming) | Kent Beck | Design on the fly; unit testing of all code; pair programming; refactoring |
| **Scrum** | Takeuchi, Nonaka, Schwaber | Teams "scrum down" in short iterations (sprints); empirical process |

See [Agile](03_Agile.md) and [Scrum](04_Scrum.md).
