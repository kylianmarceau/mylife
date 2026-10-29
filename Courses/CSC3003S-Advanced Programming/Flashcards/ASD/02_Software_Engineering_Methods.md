---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 02 — Software Engineering Methods"
---

# ASD 02 — Software Engineering Methods

**Source note:** [Software Engineering Methods](../../ASD/02_Software_Engineering_Methods.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Choosing A Development Method|Choosing A Development Method]]
  - [[#Feedback And Sustainable Work|Feedback And Sustainable Work]]
  - [[#Estimation Is The Core Problem|Estimation Is The Core Problem]]
  - [[#Standish CHAOS Report Findings|Standish CHAOS Report Findings]]
  - [[#Economics Of Adding Features|Economics Of Adding Features]]
  - [[#Human Factors And Laziness|Human Factors And Laziness]]
  - [[#Wicked Problems And The Problem Matrix|Wicked Problems And The Problem Matrix]]
  - [[#The Waterfall Method|The Waterfall Method]]
  - [[#Iterative Method Flavours|Iterative Method Flavours]]
  - [[#Planning And Change|Planning And Change]]

## Core Content

### Choosing A Development Method

<!-- qard-id: ap-98b640b51271f018c179 -->
> [!qard]- What trade-off does the software project triangle express?
> Time, cost and scope/quality constrain each other. Tightening one requires adjusting another; promising improvements in all three without a credible change is unrealistic.

<!-- qard-id: ap-d8dec8d7bd3c733a4702 -->
> [!qard]- Why break a large project into smaller deliveries?
> Smaller scope reduces complexity and coordination, produces useful feedback sooner, and limits the cost of a failed assumption.

<!-- qard-id: ap-4d481789cdd33f3bddc9 -->
> [!qard]- What is YAGNI, and how does it prevent gold plating?
> “You Ain't Gonna Need It”: implement justified current needs rather than speculative features, avoiding unnecessary complexity and maintenance.

<!-- qard-id: ap-ea0cfb58074f3ea55764 -->
> [!qard]- How do software entropy and technical debt affect later work?
> Structural degradation and expedient shortcuts make changes harder, riskier and more expensive; continued refactoring helps control them.

<!-- qard-id: ap-632c2889e003b5e8d998 -->
> [!qard]- What is code-and-fix, and why is it risky?
> Begin implementation with little planning and repair problems reactively. Uncontrolled defects and design problems can grow faster than fixes.

<!-- qard-id: ap-3764c43b99e322c337be -->
> [!qard]- What assumption makes a sequential waterfall process vulnerable in software?
> It relies on earlier decisions being sufficiently complete and correct before later phases expose their consequences; discoveries may require substantial rework.

<!-- qard-id: ap-629d93d889d426cea73b -->
> [!qard]- When is more up-front planning useful, and when is iteration especially useful?
> Known, stable requirements benefit from established designs and planning; uncertain requirements benefit from short feedback cycles. High-risk fundamentals still need early investigation.

<!-- qard-id: ap-76209e4afe3be47652ad -->
> [!qard]- What are “unknown unknowns” in the lecture's discussion of wicked problems?
> Important problems not anticipated during planning that become visible only through implementation, testing or operation.

### Feedback And Sustainable Work

<!-- qard-id: ap-46884a25017123d5c154 -->
> [!qard]- How does iterative development reduce uncertainty?
> Repeatedly build, test and show a working version, then use feedback to revise requirements, priorities and design.

<!-- qard-id: ap-32694fc080a1d8159e7d -->
> [!qard]- What is the difference between a throw-away prototype and an evolving product increment?
> The prototype investigates an uncertain idea and may be discarded; the increment extends software intended for continued delivery.

<!-- qard-id: ap-845182ed21c01bc9ace1 -->
> [!qard]- What is a danger of focusing only on the next iteration's priorities?
> Alternative designs or opportunities may never be explored, so locally successful steps can miss a better overall solution.

<!-- qard-id: ap-f028dfe60a5b52d7a617 -->
> [!qard]- Why is sustained crunch a poor response to an unrealistic plan?
> It hides estimation or scope problems, increases fatigue and shortcuts, and risks burnout and more defects. Adjust the plan and causes.

### Estimation Is The Core Problem

<!-- qard-id: ap-70e09c5563159599232f -->
> [!qard]- Why does the lecture treat estimation and communication as major causes of missed targets?
> Targets can be unrealistic because effort and difficulty are poorly understood, especially by people setting them without implementation knowledge. Communicating assumptions and uncertainty is part of planning.

### Standish CHAOS Report Findings

<!-- qard-id: ap-1b74527c64d571ac3c77 -->
> [!qard]- What conclusion and evidence caveat accompany the CHAOS tables?
> The reported data favour smaller projects and Agile over large/waterfall efforts, but unknown sampling/forecasting biases make the percentages unreliable as universal success probabilities.

### Economics Of Adding Features

<!-- qard-id: ap-1dcadbe43c9b3dfbadca -->
> [!qard]- Why can another feature reduce a product's overall return?
> It adds interactions, coordination, validation and future maintenance costs as well as initial implementation; marginal value may fall below that growing total cost.

### Human Factors And Laziness

<!-- qard-id: ap-960c5fd9b757aa81ef81 -->
> [!qard]- How do yak shaving, procrastination, gold plating and task switching waste effort?
> Tangential work delays the goal; late starts compress useful time; unnecessary extras enlarge scope; switching tasks repeatedly incurs context-recovery costs.

### Wicked Problems And The Problem Matrix

<!-- qard-id: ap-b9930da726d7e366964e -->
> [!qard]- How does the lecture's known/unknown problem matrix guide responses?
> Foreseen and solved: reuse a standard solution. Foreseen but unsolved: investigate in requirements/analysis. Newly discovered with a known fix: refactor. Unanticipated and unsolved: revisit assumptions and requirements.

### The Waterfall Method

<!-- qard-id: ap-a95b30d98e4a9652c5ff -->
> [!qard]- What sequence does the notes' waterfall model follow, and why do late discoveries hurt?
> Analysis, requirements, design, implementation, testing and operation. A defect in an early assumption may require revisiting several completed stages, so delayed feedback magnifies rework.

### Iterative Method Flavours

<!-- qard-id: ap-ff670bf2e8374b2731e4 -->
> [!qard]- How do RAD, XP and Scrum emphasise different parts of iterative development?
> RAD stresses customer collaboration and rapid fixed-schedule cycles; XP stresses tests, pair programming and refactoring; Scrum organises inspection/adaptation through sprints. All use feedback rather than one final delivery.

### Planning And Change

<!-- qard-id: ap-5f3ca2aa4d1e7e1f78cb -->
> [!qard]- How does fixing scope and deadline constrain the remaining project trade-offs?
> Resources/cost or achieved quality must absorb pressure; estimates do not become feasible merely because all desired constraints were declared fixed.

<!-- qard-id: ap-72ba072f6e20842814b3 -->
> [!qard]- Why can a “successful” forecast-based project statistic misrepresent useful delivery?
> Meeting an inaccurate initial budget/schedule is different from delivering stakeholder value; definitions and forecasting bias affect the classification.

<!-- qard-id: ap-fa058e6af9a450f9dc27 -->
> [!qard]- How does speculative development create maintenance cost even if nobody uses the feature?
> The code still needs integration, understanding, tests and compatibility with later changes; its interactions remain part of the system's complexity.

<!-- qard-id: ap-8ee8cc8d2648881208ad -->
> [!qard]- What does “do less for less” mean as a project strategy?
> Reduce scope to valuable achievable outcomes rather than demanding the same large scope from fewer resources, then deliver and learn incrementally.

<!-- qard-id: ap-222f0379e98d5c9e43d0 -->
> [!qard]- Why does technical debt not mean every shortcut is automatically irrational?
> A deliberate shortcut may serve a constraint, but its future consequences and repayment need recognition; unmanaged accumulated degradation makes later work harder.

<!-- qard-id: ap-e1b3680421ba664fe636 -->
> [!qard]- How should a newly found problem with a known solution differ from a fundamental unsolved requirement?
> Apply a controlled repair/refactoring for the known issue; revisit requirements/design assumptions when the essential problem itself remains unresolved.

<!-- qard-id: ap-ac407c4892150d3e4440 -->
> [!qard]- Why can uncertainty justify a throw-away prototype before the production design?
> It tests a risky assumption cheaply before the team commits to dependencies, quality guarantees and maintenance of the final implementation.

<!-- qard-id: ap-e3ba9897df44ab87ae28 -->
> [!qard]- How does a short iteration's feedback change the next plan?
> Compare real behaviour and stakeholder needs with assumptions, then revise scope/priorities/design rather than simply repeating the original schedule unchanged.

<!-- qard-id: ap-9c67f782fd360641cece -->
> [!qard]- What does evolving delivery require from the team and customer?
> Fast communication, access to feedback and the ability to integrate/test working changes frequently; short deadlines without that support do not produce useful learning.

<!-- qard-id: ap-c336a5ca158ce0d2b390 -->
> [!qard]- Why can pure waterfall's “finish this phase first” assumption clash with software discovery?
> Implementation, testing and use can reveal requirements or design flaws that were unknowable or missed earlier, requiring feedback across phase boundaries.

<!-- qard-id: ap-ad9684083e13a658089c -->
> [!qard]- How does RAD's reflection step distinguish a feedback cycle from repeated coding alone?
> Learning from the deployed/tested version informs the next requirements and design; repeating construction without evaluation does not reduce the same uncertainty.
