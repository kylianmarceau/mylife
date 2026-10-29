---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 03 — Agile"
---

# ASD 03 — Agile

**Source note:** [Agile](../../ASD/03_Agile.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Agile Values In Practice|Agile Values In Practice]]
  - [[#Quality And Feedback|Quality And Feedback]]
  - [[#The Manifesto 15 Years Later|The Manifesto 15 Years Later]]
  - [[#The 12 Agile Principles|The 12 Agile Principles]]
  - [[#Pareto's Law (80/20)|Pareto's Law (80/20)]]
  - [[#Recording User Stories And Task Size|Recording User Stories And Task Size]]
  - [[#Pair Programming|Pair Programming]]
  - [[#Code Review|Code Review]]
  - [[#Working Product At All Times|Working Product At All Times]]
  - [[#Values, Requirements And Delivery|Values, Requirements And Delivery]]

## Core Content

### Agile Values In Practice

<!-- qard-id: ap-230f73266357200ac6b9 -->
> [!qard]- What preferences do the four Agile manifesto values express?
> Individuals/interactions, working software, customer collaboration and responding to change are valued over processes/tools, comprehensive documentation, contract negotiation and following a plan. The latter still have value.

<!-- qard-id: ap-5e957bb05ffba9c49d11 -->
> [!qard]- Why must Agile teams be empowered?
> Ownership of estimates, implementation choices and commitments supports motivation and accountability; external micromanagement undermines self-management.

<!-- qard-id: ap-90a079fb845f475b4778 -->
> [!qard]- How does Agile usually handle a fixed budget and delivery date?
> Vary scope and deliver the highest-value core features first, rather than treating every requested feature as equally mandatory.

<!-- qard-id: ap-c318f70f5f46e1da4321 -->
> [!qard]- What does a user story's role–task–goal template capture?
> “As a [role], I want [task], so that [goal]”: who needs the feature, what they need and why it matters.

<!-- qard-id: ap-04d16e38940bd71d7f7b -->
> [!qard]- What do acceptance criteria add to a user story?
> Observable conditions or test cases defining successful behaviour, including important alternative and failure cases.

<!-- qard-id: ap-934e980e971d30ab6217 -->
> [!qard]- Why split work into small verifiable deliverables?
> Completion and quality become visible, feedback arrives sooner, and “almost finished” activities cannot hide stalled progress.

<!-- qard-id: ap-6e6669a56296cde26ba9 -->
> [!qard]- What does “barely sufficient requirements” mean, and what is its limit?
> Capture enough detail just in time to develop and test a feature, but investigate high-cost/high-likelihood risks and architectural interactions early.

<!-- qard-id: ap-c90b5a4a6685943534f8 -->
> [!qard]- Why is security a limit on deferring all design?
> It crosses many components and depends on consistent architecture; late patches may leave fundamental gaps.

### Quality And Feedback

<!-- qard-id: ap-d714f610fcf69143cefa -->
> [!qard]- What does “done means shippable” prevent?
> Features accumulating at “90% complete” without testing, review or integration. Completion includes agreed functional and non-functional quality criteria.

<!-- qard-id: ap-0c0ba30a387fb6019f16 -->
> [!qard]- Why keep an integrated working product throughout development?
> It enables real feedback and exposes incompatibilities and regressions early, before changes accumulate.

<!-- qard-id: ap-073cc24766d3d6b00a7f -->
> [!qard]- What is continuous integration?
> Integrating changes frequently and checking them with automated builds/tests so integration faults are discovered quickly.

<!-- qard-id: ap-973d4b5344662ae0e6ec -->
> [!qard]- Why should a broken shared build receive immediate attention?
> Further changes compound the problem and obscure its cause; restoring a trustworthy baseline keeps the team productive.

<!-- qard-id: ap-93321d4b72447ffe6d2b -->
> [!qard]- How can pair programming improve quality and team resilience?
> Continuous review and shared problem-solving reduce false starts, spread knowledge and support common ownership, at the cost of communication and coordination effort.

<!-- qard-id: ap-c4bffe587bf86d5d6c1c -->
> [!qard]- How does refactoring support Agile development?
> It improves internal structure without changing observable behaviour, keeping the code adaptable as requirements evolve.

<!-- qard-id: ap-2529a3578f94eefa8aaf -->
> [!qard]- Why observe user behaviour as well as asking what users want?
> Stated preferences may miss actual needs; working prototypes reveal difficulties and useful features through use.

### The Manifesto 15 Years Later

<!-- qard-id: ap-c80873ac4c9cbaed893a -->
> [!qard]- How does DevOps extend the delivery feedback loop, and what do shift left/right emphasise in the lecture?
> Join planning/coding/build/testing with release/deploy/operate/monitor. Shift left brings quality/design checks earlier; shift right studies behaviour, performance and resilience during operation.

<!-- qard-id: ap-8b2b68d45bbc034b1589 -->
> [!qard]- Why does person-to-person coordination become difficult as a team grows?
> A fully connected group has $n(n-1)/2$ pairwise communication paths. Small teams and clear interfaces reduce the coordination burden; interaction alone does not scale without structure.

### The 12 Agile Principles

<!-- qard-id: ap-b1d7b49186ae2840a1e6 -->
> [!qard]- How do the Agile principles translate customer collaboration into delivery practice?
> Deliver useful working software early and frequently, welcome change, and keep business people and developers engaged so feedback changes the next priorities.

<!-- qard-id: ap-e6c4d64c7457799bf9fc -->
> [!qard]- How do the Agile principles address team effectiveness and long-term quality?
> Support motivated self-organising teams, direct communication, a sustainable pace, technical excellence, simplicity and regular reflection/adaptation. Working software provides evidence of progress.

### Pareto's Law (80/20)

<!-- qard-id: ap-a582faa9323181cd9b00 -->
> [!qard]- How should the 80/20 idea influence prioritisation, and what is its limitation?
> Seek the smaller set of work producing most value, without treating 80/20 as an exact law. The high-value set is not necessarily knowable in advance; feedback helps discover it.

### Recording User Stories And Task Size

<!-- qard-id: ap-1516e0c307091da78442 -->
> [!qard]- What belongs on a user-story card, and why keep tasks small?
> A heading/estimate, conversation/background, and acceptance criteria. Tasks of roughly a working day, at most about 16 hours in the notes, expose daily progress and encourage concrete deliverables.

### Pair Programming

<!-- qard-id: ap-9f355d5253ac9513b43c -->
> [!qard]- What costs can make pair programming less suitable for a simple task?
> Constant communication, pace/skill mismatches, context switching and interpersonal dynamics can outweigh the review/learning benefit; choose deliberately rather than assuming every task needs a pair.

### Code Review

<!-- qard-id: ap-4b38fa71c6ba277debc4 -->
> [!qard]- Why can later code review miss problems that live collaboration might catch?
> Reviews may be superficial, context has faded, sunk effort discourages redesign and authors may rely too much on reviewers. Prompt substantive review and good communication address these risks.

### Working Product At All Times

<!-- qard-id: ap-d2bc9aa986dc5f6d9747 -->
> [!qard]- How does profiling resolve the “clarity first versus performance first” dispute in the lecture?
> Identify the small set of operations dominating real runtime and investigate architectural performance constraints early; avoid making all code clever based on guesses while retaining a clear measurable baseline.

### Values, Requirements And Delivery

<!-- qard-id: ap-802f6887ee044b2f9883 -->
> [!qard]- Does valuing working software over comprehensive documentation mean no documentation is useful?
> No. The preference guides trade-offs; architecture, security, shared understanding and assurance may still require explicit documentation.

<!-- qard-id: ap-e38983fd3943ed1b25d8 -->
> [!qard]- Does welcoming change mean an iteration must accept unlimited work without replanning?
> No. Adapt priorities and scope through the team's process while preserving a feasible focused delivery commitment.

<!-- qard-id: ap-47707f83209f3061aa68 -->
> [!qard]- Why does fixing time/cost require prioritised scope rather than merely working faster?
> Capacity is bounded. Delivering the most valuable complete features first preserves useful outcomes when lower-priority work must be deferred.

<!-- qard-id: ap-dfcec25bf52da3133de1 -->
> [!qard]- What does a user story intentionally leave out of its role–task–goal statement?
> Detailed implementation mechanics. It expresses the user's desired capability and value, with discussion and acceptance criteria supplying necessary detail.

<!-- qard-id: ap-e130cb042c132987dd5f -->
> [!qard]- Why capture an initial backlog before deferring feature details just in time?
> High-level stories support scope and feasibility estimates, while delaying uncertain detail avoids over-specifying work that may change.

<!-- qard-id: ap-288a607392d208c7c1b1 -->
> [!qard]- How do functional acceptance criteria differ from a non-functional quality requirement?
> They describe the observable capability/scenario; non-functional requirements constrain qualities such as response time, security or reliability. “Done” must meet both relevant kinds.

<!-- qard-id: ap-cde58b974f6cb51d40f5 -->
> [!qard]- How does a true prototype differ from a skeleton prototype in the Agile note?
> A true prototype is disposable learning code; a skeleton is intended to evolve into the final system, so its structural/quality consequences matter beyond the experiment.

<!-- qard-id: ap-a5138f0d6a30270f5a0a -->
> [!qard]- What should a nightly build produce beyond “my changed file compiles”?
> A complete reproducible installable product image, with automated checks, showing the integrated system can still be built and used.

<!-- qard-id: ap-edc6b60f7397e834fb6d -->
> [!qard]- Why does a shared Definition of Done support trust between iterations?
> Everyone evaluates completion against the same quality evidence rather than incompatible personal meanings of “finished”.

<!-- qard-id: ap-26b3c0eaeeca900385bf -->
> [!qard]- Why does rotating pairs reduce dependence on a single developer?
> Knowledge and ownership spread across the team, reducing the disruption when an individual is unavailable and helping others review/change the work.

<!-- qard-id: ap-a7f24151ce27bf759ef9 -->
> [!qard]- How does refactoring differ from adding a new user-visible feature?
> It changes internal organisation while preserving intended observable behaviour; features intentionally extend that behaviour. Use checks to distinguish the two effects.
