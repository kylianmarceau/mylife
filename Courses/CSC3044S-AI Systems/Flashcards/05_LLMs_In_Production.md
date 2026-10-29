---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "05 — Putting LLMs into Production: Software, People, and Client Onboarding"
---

# 05 — Putting LLMs into Production: Software, People, and Client Onboarding

**Source note:** [Putting LLMs into Production: Software, People, and Client Onboarding](../05_LLMs_In_Production.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#Models, harnesses, and architectural variety|Models, harnesses, and architectural variety]]
  - [[#Design the interface around the task|Design the interface around the task]]
  - [[#Client onboarding: document fields and conditional rules|Client onboarding: document fields and conditional rules]]
  - [[#Generation, review, and backend integration|Generation, review, and backend integration]]
  - [[#Context, prompt design, and improvement|Context, prompt design, and improvement]]

## Core Content

### Models, harnesses, and architectural variety

<!-- qard-id: ais-3c2c80eb9fb89342880b -->
> [!qard]- What are an LLM and a harness in a production system?
> The LLM processes/generates language; the harness organizes its context, tools, execution, and permissions in a software environment.

<!-- qard-id: ais-5b5ee6b2e3aa627cbc6f -->
> [!qard]- What are a Transformer, attention, and an embedding?
> A Transformer combines token representations through attention; attention weights representations’ relevance; an embedding is a numerical vector representation of a token or item.

<!-- qard-id: ais-599c06c735befde30b3b -->
> [!qard]- What is a mixture of experts?
> A design routing computation through selected expert modules.

<!-- qard-id: ais-031ee8c99344a5bddb23 -->
> [!qard]- What components are shown in the encoder-decoder Transformer overview?
> Positional information, attention, feedforward transformations, residual additions, normalization, and an output probability distribution.

<!-- qard-id: ais-478d1200651d58dbd43d -->
> [!qard]- Why does a decoder use masking and encoder-decoder attention?
> Masking prevents future-output access in autoregressive generation; encoder-decoder attention lets it use the encoded input.

<!-- qard-id: ais-4223aee1b5e5aa471c05 -->
> [!qard]- Which dimensions of LLM architecture can vary?
> Attention design, normalization, feedforward structure, context window, and expert routing.

<!-- qard-id: ais-ecb7d4122091571cc252 -->
> [!qard]- What architectural features characterize the lecture’s Llama gallery example?
> Grouped-query attention, dense feedforward layers, and RMS normalization.

<!-- qard-id: ais-2689a7e3ba158ef2edf6 -->
> [!qard]- What architectural features characterize the lecture’s DeepSeek gallery example?
> Multi-head latent attention and routed MoE; its initial three blocks are dense.

<!-- qard-id: ais-ee0f600be6239555475a -->
> [!qard]- What architectural features characterize the lecture’s Gemma gallery example?
> Local sliding-window and global attention, with pre/post normalization and a local/global ratio of $5:1$ in the displayed configuration.

<!-- qard-id: ais-015287686ef5d5951a69 -->
> [!qard]- Why distinguish total and active MoE parameters?
> Total size measures stored capacity; active parameters determine per-token computation. The DeepSeek illustration has $671$ billion total and about $37$ billion active.

<!-- qard-id: ais-6ba69c49e5102866b33e -->
> [!qard]- What expert selection is shown in the DeepSeek illustration?
> One shared expert and eight selected routed experts per inference step.

<!-- qard-id: ais-c441bb8784e9e3f4fb6e -->
> [!qard]- How should the gallery’s model dimensions and product labels be interpreted?
> As lecture-recorded configurations, not verified current specifications or rankings.

<!-- qard-id: ais-f64c173f14af148b0ec9 -->
> [!qard]- What is the practical model-selection unit emphasized by the guest lecture?
> The model-harness-workflow combination serving the domain, rather than a model name alone.

### Design the interface around the task

<!-- qard-id: ais-925508efddbb98e47ee3 -->
> [!qard]- What is a user interface?
> Controls and representations through which people use a system.

<!-- qard-id: ais-e68546eb3aec62a02cad -->
> [!qard]- What does human in the loop mean?
> People inspect, correct, or approve system outputs in the workflow.

<!-- qard-id: ais-571f0d565f7b220768a4 -->
> [!qard]- What is an AI-native workflow?
> A workflow designed around how model assistance contributes to the task.

<!-- qard-id: ais-0b422af73c7b9761c46b -->
> [!qard]- Why is adding a chat panel not enough to integrate AI into an application?
> The panel must connect to application state and task objects; otherwise users may need to transfer context and outputs manually.

<!-- qard-id: ais-988c40dbdb82c14aa54d -->
> [!qard]- How do separate chat, integrated generation, and correction UI differ?
> Separate chat asks users to describe tasks; integrated generation edits current task objects; correction UI supports direct inspection and fixes to structured fields.

<!-- qard-id: ais-83472b8cfce6f77e7d82 -->
> [!qard]- Why can a task-specific control be better than repeated free-text instructions?
> It supplies relevant state and makes specific structured outputs easy to generate, inspect, and correct.

<!-- qard-id: ais-bf18189754ae75f0f652 -->
> [!qard]- Does “UI beats text” imply conversation is always worse?
> No. The claim concerns the structured review task; conversation remains useful for ambiguous requests.

### Client onboarding: document fields and conditional rules

<!-- qard-id: ais-286d177ced649a239ecd -->
> [!qard]- What is a capture field?
> A document field extracted or entered for later processing.

<!-- qard-id: ais-49463af650a55fc1be0a -->
> [!qard]- What is a verification rule?
> A check on document information applied according to business conditions.

<!-- qard-id: ais-273fd4f6ce051bb279e5 -->
> [!qard]- What is a rule tree?
> A hierarchy whose parent conditions determine the context for child checks.

<!-- qard-id: ais-6f384f7f0a2c3c4a8b03 -->
> [!qard]- Why is document onboarding an attractive structured-assistance task?
> Many document types and capture fields require numerous rules, making manual configuration tedious and prone to inconsistent checks.

<!-- qard-id: ais-f85a0f5f9bed45252e01 -->
> [!qard]- What document and field scale is described in the onboarding case?
> Documents around $30$ pages, $200$–$300$ capture fields, and $100$–$200$ document types, with approximately one rule per field.

<!-- qard-id: ais-df553458c011f9a799ab -->
> [!qard]- Which capture-field and investor-type categories are listed?
> Personal/contact fields such as name, date of birth, email, phone, and address; investor types include individuals, joint holders, corporations, and trusts/nominees.

<!-- qard-id: ais-115d883548d3e48ffadc -->
> [!qard]- Why does parent-child rule structure carry semantic meaning?
> A parent scopes the applicable entity or condition; child checks must be valid within that context rather than merely indented visually.

<!-- qard-id: ais-deda5363efcd8dba96bd -->
> [!qard]- Why should a presence check precede a database-value comparison?
> A dependent comparison needs the field to exist before its value can be meaningfully checked.

### Generation, review, and backend integration

<!-- qard-id: ais-be23cc1c7716a56b8d52 -->
> [!qard]- What are an API, JSON, and a field alias?
> An API defines software request/result exchange; JSON structures objects, arrays, and values; a field alias links a rule to a known captured field.

<!-- qard-id: ais-c861d51d4fc9b5e97be3 -->
> [!qard]- What is the model-assisted rule-generation workflow?
> User supplies rules, app assembles context, LLM returns JSON checks, UI renders them, user reviews/corrects, then the system imports or persists them.

<!-- qard-id: ais-0b8f541e8fcd619e2391 -->
> [!qard]- What technologies and roles are recorded in the onboarding stack?
> Vue JS for UI/correction, Golang API for coordination, Postgres for storage, and Azure GPT for generation/review.

<!-- qard-id: ais-5260ffd1d9a904b4da15 -->
> [!qard]- Why did this application favor a simple harness?
> A controlled flow and explicitly formatted context sufficed; tool-heavy loops can run indefinitely, and dynamic subagents add unnecessary complexity when the task does not need them.

<!-- qard-id: ais-551bda39ced2859bc1b6 -->
> [!qard]- Do multiple processing stages require an open-ended delegating agent?
> No. A developer-defined staged workflow can perform them without dynamic action selection or delegation.

<!-- qard-id: ais-28d4bc76a1eba3029241 -->
> [!qard]- Why was review developed before generation?
> Establish acceptance rules first, then make the generator follow the same rules.

<!-- qard-id: ais-b5ab65698362c47c2c84 -->
> [!qard]- What is an exact duplicate sibling check?
> A sibling with the same check type and intent as another, creating redundant validation.

<!-- qard-id: ais-04e85be2276d041f8cd9 -->
> [!qard]- What is parent-child inconsistency in generated checks?
> A child targets an entity incompatible with its parent’s scope.

<!-- qard-id: ais-495cd495754af438d5ef -->
> [!qard]- What are missing mapping and prerequisite failures?
> A generated check lacks a valid captured-field link or depends on a missing/inappropriate parent check.

<!-- qard-id: ais-83d64b249c0068e820ee -->
> [!qard]- Why put failure cases in both generation and review prompts?
> Concrete shared criteria help generation avoid errors and review detect them consistently.

### Context, prompt design, and improvement

<!-- qard-id: ais-b6c5d215baceaa0520f3 -->
> [!qard]- What is prompt engineering?
> Designing instructions, examples, and context to guide model behavior.

<!-- qard-id: ais-cb7bfd3c8e4e6eb4ccd3 -->
> [!qard]- What is weight fine-tuning?
> Updating model parameters with additional training.

<!-- qard-id: ais-0d68de2fac9154982478 -->
> [!qard]- What is a textual gradient?
> Natural-language feedback describing how a prompt or intermediate output should improve.

<!-- qard-id: ais-1ee35d414817a2d6130a -->
> [!qard]- Which context blocks support faithful rule generation?
> User rules and conditional structure, field aliases (`field_alias_id`), comment presets (`comment_id`), and comment parameters (`comment_parameter_id`).

<!-- qard-id: ais-d0c850ae654d107f0b86 -->
> [!qard]- What output constraints should the rule-generation prompt impose?
> Business-readable check names, valid mappings, and a `skipped_reason` when a rule is too unclear to implement faithfully.

<!-- qard-id: ais-047e7daac123af4a8c7c -->
> [!qard]- Why are semantically mismatched prompt examples dangerous?
> The model can copy their inconsistency instead of learning the intended input-to-output mapping.

<!-- qard-id: ais-c5a6376daba9a238da8c -->
> [!qard]- What deployment constraints affect model choice?
> Approval restrictions, region, compliance requirements, and domain performance.

<!-- qard-id: ais-69a95c5d85089d86cc08 -->
> [!qard]- Why should one deployment’s fine-tuning restrictions not be generalized to all models?
> They describe the options in that case and can differ across model families or deployments.

<!-- qard-id: ais-c68ec1b18e79cf5b3126 -->
> [!qard]- What is the iterative prompt-improvement procedure?
> Test representative rules, inspect outputs/corrections, add aligned instructions/examples for recurring errors, rerun old and new cases, and retain changes that improve quality.

<!-- qard-id: ais-4684e9684f148a1b1a61 -->
> [!qard]- How does TextGrad’s optimization analogy differ from ordinary backpropagation?
> Numerical gradients update neural parameters; textual feedback can revise prompts or intermediate outputs in a black-box workflow.

<!-- qard-id: ais-ec62896cb507134ea9e2 -->
> [!qard]- Does reward-style wording in a prompt create a training reward or change runtime permissions?
> No. It is input text; effects must be evaluated within actual system constraints.

<!-- qard-id: ais-6c755934491eb9753e86 -->
> [!qard]- What does the human-model-interface view emphasize?
> The LLM is situated in an application environment with concrete user actions, review, and workflow state.
