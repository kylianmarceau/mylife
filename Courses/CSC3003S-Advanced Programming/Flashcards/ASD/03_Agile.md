---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 03 — Agile"
---

# ASD 03 — Agile

**Source note:** [Agile](../../ASD/03_Agile.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Manifesto|Manifesto]]
  - [[#Requirements|Requirements]]
  - [[#Timescale And Done|Timescale And Done]]
  - [[#Working Product|Working Product]]
  - [[#Pair Programming|Pair Programming]]

## Core Content

### Manifesto

<!-- qard-id: ap-07f594f233458bc6325b -->
> [!qard]- State the four Agile Manifesto values.
> Individuals and interactions over processes and tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan.

<!-- qard-id: ap-2093d6ed6859aa357f9c -->
> [!qard]- Does the manifesto say the right-hand items have no value?
> No — they have value, but the left-hand items are valued more.

<!-- qard-id: ap-93550e4789746434ad59 -->
> [!qard]- What trade-offs do processes/documentation have versus Agile?
> Processes and waterfall: easy communication, clear division of labour, plan = final product, good for known problems. Agile: harder communication, less clear roles, suits novel development.

<!-- qard-id: ap-63894ab480f281eaa3cc -->
> [!qard]- Why does security challenge pure Agile?
> Security must be designed into the architecture up front and can't be bolted on in late iterations.

<!-- qard-id: ap-a1e7066719a43d34c9b3 -->
> [!qard]- Name five of the twelve Agile principles.
> E.g. early continuous delivery; welcome changing requirements; working software measures progress; face-to-face communication; simplicity (maximise work not done); self-organising teams; regular reflection.

<!-- qard-id: ap-cd14f6f688b51e4a05dd -->
> [!qard]- Why must Agile teams be empowered?
> Sole responsibility for delivery gives buy-in and ownership; outside interference reduces motivation.

### Requirements

<!-- qard-id: ap-5376bab28c5191e1b216 -->
> [!qard]- What is Pareto's law?
> About 80% of results come from 20% of effort — but no one knows which 20%.

<!-- qard-id: ap-461d160317b0ef242636 -->
> [!qard]- What are "barely sufficient" requirements?
> High-level requirements captured just in time, with the minimum detail needed to develop and test a feature.

<!-- qard-id: ap-e4de4eda471e58b26ae8 -->
> [!qard]- What caveats apply to barely sufficient requirements?
> Only acceptable for low-risk, poorly understood features; interactions and security still need understanding; risk assessment is needed.

<!-- qard-id: ap-74e812375d714f87e5f0 -->
> [!qard]- What is a user story and its standard form?
> A short business-language requirement: "As a [role], I want to [task], so I can [goal]" — who, what, why, not how.

<!-- qard-id: ap-8b051eb86956f56ee189 -->
> [!qard]- What are the three parts of a user story card?
> Heading (name, ID, size estimate), conversation (background, sketch, notes) and acceptance criteria (test cases).

<!-- qard-id: ap-71ba7c152d2e3bcebc3f -->
> [!qard]- How big should Agile tasks be?
> At most 16 hours, preferably 8, so progress is measurable daily; items are deliverables, not activities.

<!-- qard-id: ap-a9cb0067a1111d5c6e3b -->
> [!qard]- Why "don't listen to users", per Nielsen and Jobs?
> Users can't reliably say what they need — watch what they do and show them working software.

### Timescale And Done

<!-- qard-id: ap-b8ff90b64fa191134f44 -->
> [!qard]- In Agile, what is fixed and what varies?
> Time and budget are fixed; scope varies, with the highest-priority features delivered first.

<!-- qard-id: ap-6c44696abd5a1638e748 -->
> [!qard]- What is Agile's development cycle?
> Analyse, develop, test — one feature at a time, in priority order, each fully shippable.

<!-- qard-id: ap-4a987516070a75db672b -->
> [!qard]- What does "done" mean in Agile?
> Shippable: unit tests pass, code reviewed, acceptance and functional tests pass, non-functional requirements met, product owner accepts.

<!-- qard-id: ap-6cc9a0da43194a709f85 -->
> [!qard]- Why finish each feature before starting the next?
> It avoids many features sitting at "90% complete" or untested.

### Working Product

<!-- qard-id: ap-94a211c746f3385a988c -->
> [!qard]- True prototype versus skeleton prototype?
> A true prototype is thrown away after exploring a problem; a skeleton grows into the final product.

<!-- qard-id: ap-6dd4e0fbd2f886d2fc1b -->
> [!qard]- What is continuous integration?
> Integrating changes into the shared code at least daily so problems surface early.

<!-- qard-id: ap-70f72d2c235eaebe053c -->
> [!qard]- What should happen when a nightly build fails?
> Fix it first; no one integrates more work until the build passes again.

<!-- qard-id: ap-bcb0214283bc744532a9 -->
> [!qard]- How should performance be handled, per Agile?
> Don't neglect it; a few critical loops dominate, so find them with profiling tools.

### Pair Programming

<!-- qard-id: ap-37964956b7c941bc39d5 -->
> [!qard]- What is pair programming?
> Two programmers at one computer writing every line together, one typing and one supporting.

<!-- qard-id: ap-daf02635eea4513a5d28 -->
> [!qard]- Give three advantages of pair programming.
> Continuous informal review, collective code ownership and knowledge spreading, motivation to refactor.

<!-- qard-id: ap-aa8cc764bfc0612525fb -->
> [!qard]- Give three challenges of pair programming.
> Pace mismatch is exhausting; needs strong interpersonal skills; power dynamics and no time alone.

<!-- qard-id: ap-895c70ac822b1991850f -->
> [!qard]- What are code review's weaknesses compared with pairing?
> Superficial reviews, over-reliance on the reviewer, sunk-cost reluctance to refactor, long gap between bug and discovery.

<!-- qard-id: ap-0eaca300aa1fae9b61b0 -->
> [!qard]- What is refactoring?
> Improving code's internal quality without changing its behaviour.
