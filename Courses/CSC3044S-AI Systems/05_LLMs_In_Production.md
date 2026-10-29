---
tags:
  - ai-systems
---

# Putting LLMs into Production: Software, People, and Client Onboarding

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3044S Artificial Intelligence: AI Systems  
> **Source**: [2026-CSC3044S-Lecture 5-Agent Architectures (LLMs).pdf](../../Sources/CSC3044S%20-%20AI%20Systems/2026-CSC3044S-Lecture%205-Agent%20Architectures%20%28LLMs%29.pdf), Isazi guest lecture; speaker not named in the supplied deck; September 2026, slides 1-67  
> **Generated**: 2026-10-01  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Models, harnesses, and architectural variety|Models, harnesses, and architectural variety]]
  - [[#Design the interface around the task|Design the interface around the task]]
  - [[#Client onboarding: document fields and conditional rules|Client onboarding: document fields and conditional rules]]
  - [[#Generation, review, and backend integration|Generation, review, and backend integration]]
  - [[#Context, prompt design, and improvement|Context, prompt design, and improvement]]

---

## Core Content

### Models, harnesses, and architectural variety

#### Definitions

> **Large language model (LLM)**: A learned model that processes and generates language.

> **Harness**: Software organizing a model's context, tools, execution, and permissions.

> **Transformer**: A neural architecture using attention to combine information across token representations.

> **Attention**: A mechanism weighting the relevance of different representations to a current computation.

> **Embedding**: A numerical vector representation of an input token or other item.

> **Mixture of experts (MoE)**: A design routing computation through selected expert modules.

A model diagram and a coding-harness mascot illustrate different layers of a system. The transformer supplies model computation; the harness makes it useful in a software environment.

![Models, harnesses, and architectural variety: transformer encoder decoder](../../diagrams/CSC3044S-AI%20Systems/05_LLMs_In_Production/transformer_encoder_decoder.svg)

*A structural reconstruction of the transformer overview: the decoder uses past outputs and encoded input before producing output probabilities.*

The encoder-decoder illustration uses positional information, attention, feed-forward transformations, residual additions, normalization, and an output probability distribution. Decoder masking prevents access to future output tokens during autoregressive generation; encoder-decoder attention lets the decoder use encoder outputs.

The architecture gallery compares models whose computation differs even though each is called an LLM. Relevant distinctions include attention design, normalization, feed-forward structure, context window, and expert routing.

| Gallery example | Distinctive structure | Architecture labels recorded in the diagram |
|---|---|---|
| Llama 3.2, 3B | Grouped-query attention; dense feed-forward; RMS normalization | 28 blocks; 24 attention heads; embedding size $3072$; feed-forward size $8192$; context $128\mathrm{k}$ |
| DeepSeek V3/R1, 671B | Multi-head latent attention; routed MoE | 61 blocks; 128 heads; embedding size $7168$; context $128\mathrm{k}$; first three blocks dense |
| Gemma 4, 31B | Local sliding-window and global attention; pre/post normalization | 60 blocks; local/global ratio $5:1$; embedding size $5376$; feed-forward size $21504$; context $256\mathrm{k}$ |

*These values reconstruct the gallery illustrations in the supplied lecture, rather than asserting a current model specification or ranking.*

The DeepSeek illustration distinguishes $671\mathrm{B}$ total parameters from about $37\mathrm{B}$ active per inference step, with one shared expert and eight selected routed experts. Total size and per-token computation are different quantities.

![Models, harnesses, and architectural variety: attention backbone and experts](../../diagrams/CSC3044S-AI%20Systems/05_LLMs_In_Production/attention_backbone_and_experts.svg)

*The gallery shares a repeated attention/feed-forward backbone while varying attention, normalization, and expert routing.*

Harness examples named in the talk are Aider, Copilot CLI, Antigravity, Cursor, OpenCode, Claude Code, Cline, OpenHands, Codex, and Continue. The practical question is which model-harness-workflow combination serves a given domain.

### Design the interface around the task

#### Definitions

> **User interface (UI)**: The controls and representations through which people use a system.

> **Human in the loop**: A workflow where people inspect, correct, or approve system output.

> **AI-native workflow**: A workflow designed around how model assistance contributes to the task.

Putting a chat panel beside a website does not automatically integrate the model with application state. The “horseless carriage” analogy questions products that add AI while retaining structures that constrain its usefulness.

| Interface pattern | User interaction | Design implication |
|---|---|---|
| Separate chatbot | Describe the task in a chat panel | May require manually transferring application context |
| Enlarged chat panel | More room for conversation | Still needs a useful connection to workflow state |
| Integrated feature | Generate or edit the current task object | Model output becomes reviewable inside the task interface |
| Correction UI | Inspect structured fields and changes | Users can fix a specific result directly |

A task-specific “Generate tree” action and editable checks can be easier than composing repeated natural-language instructions. The conclusion “UI beats text” applies to this structured review task; conversation can still be useful for ambiguous requests.

### Client onboarding: document fields and conditional rules

#### Definitions

> **Capture field**: A document field extracted or entered for later processing.

> **Verification rule**: A check applied to document information according to business conditions.

> **Rule tree**: A hierarchy in which parent conditions determine the context for child checks.

The financial-administration client is called **FinCorp**, a pseudonym. BankCorp, CapCorp, and FundCorp supply documents processed by FinCorp with Isazi's system.

Documents are about 30 pages long, with 200-300 capture fields. A client may have 100-200 document types, approximately one rule per field. Managing this volume manually is tedious and can introduce inconsistent checks.

Typical fields include title, first/last name, birth date, email, telephone, and residential address. Investor type can distinguish an individual, joint holders, a corporate entity, or a trust/nominee.

![Client onboarding: document fields and conditional rules: document streams and processing](../../diagrams/CSC3044S-AI%20Systems/05_LLMs_In_Production/document_streams_and_processing.svg)

*The pseudonymous financial client receives several document streams for processing.*

![Client onboarding: document fields and conditional rules: conditional investor rule tree](../../diagrams/CSC3044S-AI%20Systems/05_LLMs_In_Production/conditional_investor_rule_tree.svg)

*Parent conditions scope child checks, and presence precedes comparing the name with a database record.*

The individual-investor condition scopes name and ID checks. A name-presence check precedes matching that name against a database value. Parent-child structure carries meaning; the hierarchy is not just a visual indentation style.

### Generation, review, and backend integration

#### Definitions

> **API**: A defined interface through which software components exchange requests and results.

> **JSON**: A structured data format using objects, arrays, and values.

> **Field alias**: An existing identifier connecting a rule to a known captured field.

1. A user supplies rules through the UI.
2. The application assembles a prompt with relevant context.
3. The LLM returns JSON describing checks.
4. The system renders those checks in the UI.
5. The user reviews and corrects them before importing or persisting them.

![Generation, review, and backend integration: human ui api model review](../../diagrams/CSC3044S-AI%20Systems/05_LLMs_In_Production/human_ui_api_model_review.svg)

*The application coordinates model-generated JSON, persistence, and human review through the API.*

| Component | Technology recorded in the example | Role |
|---|---|---|
| UI | Vue JS | Input, tree display, correction |
| API | Golang | Coordinate rules, model requests, storage |
| Database | Postgres | Persist structured information |
| LLM service | Azure GPT | Generate and review check structures |

The simplified harness advice for this application is:

- Avoid subagents when a simple flow suffices.
- Tool-heavy execution can loop indefinitely.
- Explicitly formatted context strings can be easier to control.

This is a case-specific engineering choice. Multiple stages do not require an open-ended agent that delegates dynamically.

> [!tip] <span style="color: #5ad4b5">Review first, generation second</span>
> The development order was **review first, generation second**. Establish review rules, then make the generator follow those same rules.  

| Review condition | What to flag |
|---|---|
| Exact duplicate sibling | Same check type and intent as a sibling |
| Parent-child inconsistency | Child refers to an entity while the parent scopes individuals |
| Missing mapping | Generated check lacks a valid field connection |
| Missing or inconsistent prerequisite | Dependent check has an inappropriate parent |

Duplicate and parent-child failure cases belong in both generation and review prompts. This makes acceptance criteria concrete before broad generation.

### Context, prompt design, and improvement

#### Definitions

> **Prompt engineering**: Designing instructions, examples, and context to guide model behavior.

> **Weight fine-tuning**: Updating model parameters using additional training.

> **Textual gradient**: Natural-language feedback describing how an intermediate output or prompt should improve.

Useful prompt context includes:

| Context block | Relevant references |
|---|---|
| Rules text | User's requirements and conditional structure |
| Available field aliases | `field_alias_id` |
| Comment presets | `comment_id` |
| Comment parameters | `comment_parameter_id` |

The prompt should require business-readable check names, valid mappings, and a `skipped_reason` when a rule is too unclear to implement faithfully.

One displayed prompt example pairs an investor-name input with a non-US-person-status output. That mismatch is a caution: examples should demonstrate the intended semantic mapping. A model can copy an inconsistent example.

Model selection must account for approval constraints, region, compliance requirements, and domain performance. The guest's limitations on fine-tuning describe the deployment options in that case; they are not a timeless statement about every model family.

1. Try the prompt on representative rules.
2. Inspect generated checks and user corrections.
3. Add instructions or aligned examples addressing recurring errors.
4. Rerun previous cases as well as new ones.
5. Retain useful changes based on output quality.

TextGrad illustrates an analogy with backpropagation: numerical gradients update neural parameters; textual feedback can instead guide revision of prompts or intermediate outputs in a black-box workflow.

![Context, prompt design, and improvement: textual feedback optimization](../../diagrams/CSC3044S-AI%20Systems/05_LLMs_In_Production/textual_feedback_optimization.svg)

*Textual feedback plays an optimization role analogous to gradients, while revision targets prompts or intermediate text.*

An additional prompt experiment uses explicit correct/forbidden examples and reward-style wording to clarify intended tool behavior. Such wording is input text, not an actual training reward or authority to change runtime permissions. Evaluate its effects within the system's real constraints.

The closing human-model-interface illustration reinforces that the LLM sits in an environment. The bonus airline interface likewise shows concrete actions such as bookings, check-in, changes, and travel services, rather than exposing all functionality only through free text.
