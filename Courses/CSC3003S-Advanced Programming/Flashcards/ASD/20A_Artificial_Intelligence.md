---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "ASD 20A — Artificial Intelligence In Software Development"
---

# ASD 20A — Artificial Intelligence In Software Development

**Source note:** [Artificial Intelligence In Software Development](../../ASD/20A_Artificial_Intelligence.md)

Exam recall cards for definitions, distinctions, mechanisms, assumptions and limits. Example-specific arithmetic and explicitly non-examinable reference cards are omitted.

## Contents

- [[#Core Content|Core Content]]
  - [[#Interpreting The Lecture|Interpreting The Lecture]]
  - [[#Evaluating AI-Assisted Work|Evaluating AI-Assisted Work]]
  - [[#Perception: Neural Networks|Perception: Neural Networks]]
  - [[#AlexNet And Hardware Progress|AlexNet And Hardware Progress]]
  - [[#Perception Plus Reasoning?|Perception Plus Reasoning?]]
  - [[#Problems With Matrix-Multiply AI|Problems With Matrix-Multiply AI]]
  - [[#The Hype Cycle|The Hype Cycle]]
  - [[#Developers And AI: Stack Overflow Survey 2025|Developers And AI: Stack Overflow Survey 2025]]
  - [[#UCT CS Generative AI Policy|UCT CS Generative AI Policy]]
  - [[#Security Of AI-Generated Code|Security Of AI-Generated Code]]
  - [[#Models And Evidence|Models And Evidence]]

## Core Content

### Interpreting The Lecture

<!-- qard-id: ap-aa9b59dcb63758b95977 -->
> [!qard]- Which three AI families does the lecture distinguish?
> Knowledge representation (facts/concepts/relations), reasoning (inference and problem-solving models), and perception (learned neural patterns). This is the lecture's organising distinction.

<!-- qard-id: ap-b0a9a376c0143f3b13e4 -->
> [!qard]- What is an ontology compared with a knowledge base?
> An ontology organises concepts and relationships; a knowledge base stores domain facts and rules used to answer questions.

<!-- qard-id: ap-d5e486bdfe4f63ff0572 -->
> [!qard]- What is defeasible reasoning?
> Reasoning whose conclusions can be withdrawn when new information defeats the assumptions or rules supporting them.

<!-- qard-id: ap-8ee807cb9df00a8ec345 -->
> [!qard]- Why can exact formal reasoning be computationally expensive?
> Useful problem encodings may require combinatorial search, including NP-hard optimisation or satisfiability problems; tractability depends on the specific model.

<!-- qard-id: ap-5d5808cd6f8c0057ab4b -->
> [!qard]- Why do GPUs suit many neural-network operations?
> Large matrix operations contain many independent arithmetic operations that parallel hardware can process together.

<!-- qard-id: ap-abf2660e27d5560951f2 -->
> [!qard]- What trade-off does reduced numerical precision introduce?
> Smaller representations can reduce memory and increase throughput, but may lose numerical accuracy; suitability depends on the workload and technique.

### Evaluating AI-Assisted Work

<!-- qard-id: ap-0da3305bf690a5ed6bee -->
> [!qard]- What do diminishing returns to extra compute mean?
> Increasing resources by a large factor produces a smaller proportional quality gain; impressive progress over time does not alone establish efficient scaling.

<!-- qard-id: ap-30b48e288b3352d98622 -->
> [!qard]- Why is a benchmark or survey percentage not a universal AI capability guarantee?
> It depends on the sampled tasks, models, participants and measurement design; different contexts may produce different results.

<!-- qard-id: ap-fead26e35a7d33730b31 -->
> [!qard]- What caveats does the lecture raise about short-term studies of AI-assisted learning?
> Controlled settings may not generalise, publication/funding bias may affect evidence, and short-term gains do not establish long-term understanding.

<!-- qard-id: ap-660418ff42ab23584514 -->
> [!qard]- Why does syntactically correct AI-generated code still need security review and tests?
> Compilation checks structure/type rules, not all intended behaviour or security properties; the lecture's cited security study found substantial vulnerabilities.

<!-- qard-id: ap-70e95971764221540e87 -->
> [!qard]- Why must a developer understand code they submit, regardless of how it was generated?
> They must explain assumptions, judge correctness, maintain it and find failures; outsourcing generation does not supply that understanding or remove responsibility.

### Perception: Neural Networks

<!-- qard-id: ap-b8df48540138e93f7744 -->
> [!qard]- What do the lecture's square-matrix scaling formulas describe?
> Storing an $n\times n$ dense matrix uses $O(n^2)$ entries; conventional multiplication of two such matrices uses $O(n^3)$ arithmetic work. These illustrate resource growth, not a universal cost formula for every neural-network layer.

### AlexNet And Hardware Progress

<!-- qard-id: ap-f85bc935b9c7ff76cafc -->
> [!qard]- Why is AlexNet used as a milestone in the lecture?
> The 2012 convolutional network demonstrated the benefit of deeper learned image features and GPU-parallel training, contrasting with earlier smaller/shallow approaches. The lesson concerns algorithm/hardware progress rather than memorising layer counts.

### Perception Plus Reasoning?

<!-- qard-id: ap-cefc2bfd70b885b1f1b5 -->
> [!qard]- What distinction does the lecturer draw between neural “reasoning” claims and explicit formal reasoning?
> The lecturer contrasts learned pattern-based outputs with explicit facts, constraints and inference rules. Treat claims that these can never be combined, or that a marketing label establishes formal guarantees, as claims requiring evidence rather than definitions.

### Problems With Matrix-Multiply AI

<!-- qard-id: ap-751e53d16c04a52ff61e -->
> [!qard]- How should the notes' proposed link between floating-point infinities and confabulation be interpreted?
> It is the lecturer's stated suspicion, not an established explanation. Numerical issues and generated false claims need evidence linking the mechanism to behaviour; do not promote a speculation into a proven cause.

### The Hype Cycle

<!-- qard-id: ap-1c70efef21fbe6b13f86 -->
> [!qard]- What are the stages of the hype-cycle model discussed in the lecture?
> Technology trigger, inflated expectations, disillusionment, enlightenment and a productivity plateau. It is a descriptive model for expectations/adoption, not a precise forecast of a technology's capabilities.

### Developers And AI: Stack Overflow Survey 2025

<!-- qard-id: ap-bc244585b7d732cb6b23 -->
> [!qard]- What tension does the lecture highlight in the 2025 developer survey?
> Reported adoption/planned use is high (84%), while distrust of accuracy (46%) exceeds trust (33%). Widespread use therefore does not establish confidence in correctness, especially on complex work; these are that survey's figures.

### UCT CS Generative AI Policy

<!-- qard-id: ap-35df01b48b413a6ad35c -->
> [!qard]- What AI-use rules are recorded in the course note, and how should their scope be read?
> The note says second/third-year use must be declared, work must remain mostly human and understanding can be assessed, while first-year use is prohibited. This recalls the supplied course policy record, not an independent verification of the current university policy.

### Security Of AI-Generated Code

<!-- qard-id: ap-90a8471c0137e6d8ebe7 -->
> [!qard]- What result and limitations accompany the lecture's cited 2025 code-security study?
> It reports about 55% secure generations overall, with strong variation by weakness/language and little improvement from model size in that evaluation. This does not mean every model/task has a fixed 45% vulnerability probability.

### Models And Evidence

<!-- qard-id: ap-15ad286b28edc1c3294a -->
> [!qard]- What must an exact reasoning model get right before its computed answer is useful?
> The facts, constraints and objectives must accurately model the intended problem; exact inference over wrong assumptions can still give an unsuitable real-world answer.

<!-- qard-id: ap-981216d7a01ac7d286dc -->
> [!qard]- Why can a hand-curated ontology be difficult to maintain as a domain grows?
> Concepts, exceptions and relationships need human modelling/updating, and ambiguous boundaries may not fit a single rigid classification.

<!-- qard-id: ap-0e5fa986e0fcd6bc6133 -->
> [!qard]- How does learning representations differ from explicitly authoring domain rules?
> A neural model derives parameters from examples; an explicit knowledge/reasoning system represents selected relationships/constraints directly. Their outputs have different routes to justification.

<!-- qard-id: ap-d1973c248c11d90b6069 -->
> [!qard]- Why does more compute not by itself establish better resource efficiency?
> Compare quality gained per resource increment, not only absolute quality; diminishing improvements can coexist with larger and more capable systems.

<!-- qard-id: ap-afc0beb7ceac365f9dec -->
> [!qard]- What is the precision–throughput/memory trade-off in smaller numeric formats?
> Fewer bits store/move more values and may enable faster hardware operations, but quantisation/rounding can affect results; assess the model and format rather than assuming equivalence.

<!-- qard-id: ap-2f4be25f8677d2575d91 -->
> [!qard]- Why is a neural model's confident-looking answer not a correctness certificate?
> Fluency or a likely generated continuation does not establish that the underlying facts, reasoning steps or code satisfy the intended specification.

<!-- qard-id: ap-053409bba21529ec1004 -->
> [!qard]- How does Bloom's taxonomy distinguish recall from higher-order learning?
> Remembering/understanding basic material differs from applying, analysing, evaluating and creating; convenient production of an answer does not prove the learner can perform those operations unaided.

<!-- qard-id: ap-699197109235576ee807 -->
> [!qard]- Why can short-term assisted performance differ from retained independent understanding?
> Assistance may supply steps the student has not learned to reconstruct; assess later unaided explanation/application as well as immediate task completion.

<!-- qard-id: ap-36a04c8c787e5eb86b09 -->
> [!qard]- What is publication bias in interpreting a learning meta-study?
> Positive/significant findings may be more likely to appear in the collected published literature than null/negative results, skewing the apparent evidence.

<!-- qard-id: ap-91e969c97167ef700019 -->
> [!qard]- Why can security pass rates differ substantially between weakness categories?
> A generator may reproduce safe patterns for one boundary but systematically mishandle another. Aggregate accuracy obscures which specific controls still fail.

<!-- qard-id: ap-6d97149f2cc219c88be6 -->
> [!qard]- Why does AI-generated code shift rather than eliminate developer responsibility?
> Requirements, review, testing, security and maintenance still need accountable human judgement; faster generation does not supply evidence those obligations are met.
