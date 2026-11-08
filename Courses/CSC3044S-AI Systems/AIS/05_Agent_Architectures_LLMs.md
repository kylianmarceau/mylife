---
tags:
  - ai-systems
---

# Agent Architectures (LLMs): Putting LLMs Into Production

**Subject**: CSC3044S AI Systems  
**Source**: `2026-CSC3044S-Lecture 5-Agent Architectures (LLMs).pdf`, "Putting LLMs into Production: Lessons from my work at Isazi" (September 2026), pages 1-67  
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Lecture Framing And Roadmap|Lecture Framing And Roadmap]]
  - [[#LLM Architectures Recap|LLM Architectures Recap]]
  - [[#Harnesses|Harnesses]]
  - [[#Choosing For A Domain|Choosing For A Domain]]
  - [[#Interacting With People Beyond The Chatbot|Interacting With People Beyond The Chatbot]]
  - [[#AI Horseless Carriages|AI Horseless Carriages]]
  - [[#Case Study Client Onboarding Compliance Rules|Case Study Client Onboarding Compliance Rules]]
  - [[#Human-UI-LLM Design And UI Beats Text|Human-UI-LLM Design And UI Beats Text]]
  - [[#Human In The Loop|Human In The Loop]]
  - [[#Backend System Overview|Backend System Overview]]
  - [[#Harness Design Keep Things Simple|Harness Design Keep Things Simple]]
  - [[#AI Review And Generation Agents|AI Review And Generation Agents]]
  - [[#Context And Prompt Design|Context And Prompt Design]]
  - [[#Choosing The Right Model|Choosing The Right Model]]
  - [[#LLM Fine-Tuning Vs Prompt Fine-Tuning|LLM Fine-Tuning Vs Prompt Fine-Tuning]]
  - [[#Textual Gradients (TextGrad)|Textual Gradients (TextGrad)]]
  - [[#Creative Prompting With Rewards And Penalties|Creative Prompting With Rewards And Penalties]]
  - [[#The LLM Sits In An Environment|The LLM Sits In An Environment]]
  - [[#Bonus Menu-Driven Chat Interfaces|Bonus Menu-Driven Chat Interfaces]]

---

## Core Content

### Lecture Framing And Roadmap

#### Definitions

> **Large Language Model (LLM)**: A neural network (in practice a transformer) trained on large amounts of text that predicts the next token, and can therefore generate text, code, and structured output such as JSON.

> **Harness**: The software wrapped around an LLM that turns it into a usable agent: it builds the prompts, supplies tools and context, runs the loop of model calls, and connects the model to the user and the rest of the system. Claude Code, Cursor, and OpenCode are examples.

> **Putting an LLM into production**: Deploying an LLM inside a real software product used by real people, where reliability, compliance, cost, and usability matter, not only model quality.

This lecture is a practitioner's view of building LLM-based systems, drawn from client work at Isazi (a South African AI company). Its main claim is that an AI system is more than the model: the surrounding software and the people using it still matter.

The lecture has three parts:

1. **LLMs and harnesses (recap)**: what the models look like inside, and what tools wrap them.
2. **Software and people**: how an LLM should interact with (a) people and (b) the backend.
3. **Worked example**: a client onboarding / compliance-rules system built at Isazi.

The two core ingredients of any LLM product:

| Ingredient | What it is | Example |
|---|---|---|
| LLM | The trained model that maps input text to output text | Transformer from "Attention Is All You Need" (Vaswani et al.) |
| Harness | The program around the model that makes it act as an agent | Claude Code (mascot "Clawd") |

### LLM Architectures Recap

#### Definitions

> **Transformer**: The neural architecture from "Attention Is All You Need" (Vaswani et al.) built from stacked attention and feed-forward blocks. Almost all modern LLMs are variants of it.

> **Token Embedding Layer**: Maps each input token ID to a dense vector of size $d_{\text{model}}$ (the embedding dimension).

> **Positional Encoding**: Information added to embeddings so the model knows token order, since attention itself is order-agnostic.

> **RoPE (Rotary Positional Embedding)**: A positional scheme that rotates query and key vectors by an angle depending on token position. Used by Llama, DeepSeek, and Gemma.

> **Multi-Head Attention**: Attention run in parallel over several "heads", each with its own query/key/value projections, so the model can attend to different relationships at once.

> **Masked (Causal) Attention**: Attention in which each token can only see earlier tokens. This is what makes decoder-only LLMs generate left to right.

> **Grouped-Query Attention (GQA)**: Attention in which several query heads share one key/value head, reducing the memory needed for the key-value cache.

> **Multi-Head Latent Attention (MLA)**: DeepSeek's attention variant that compresses keys and values into a smaller latent representation to save memory.

> **Sliding-Window (Local) Attention**: Attention in which each token only attends to a fixed window of nearby tokens, rather than the whole sequence (global / full attention).

> **RMSNorm**: Root-mean-square layer normalisation, a cheaper alternative to LayerNorm used before/after sub-layers.

> **QK-Norm**: Normalisation applied to queries and keys before attention, used in Gemma 4 to stabilise training.

> **Feed-Forward (FFN) Module**: The per-token MLP in each transformer block. In modern LLMs it is a gated unit: two linear layers in parallel, one passed through an activation (SiLU or GELU), multiplied element-wise, then a final linear layer (SwiGLU / GeGLU style).

> **Mixture of Experts (MoE)**: A layer that replaces one large FFN with many smaller expert FFNs plus a **router** that picks a few experts per token, so only a fraction of the parameters is active for each token.

> **Vocabulary Size**: The number of distinct tokens the model can read and produce.

> **Context Length**: The maximum number of tokens the model can process in one input.

#### The Original Transformer

The original transformer has an encoder stack and a decoder stack, each repeated $N\times$:

| Stack | Sub-layers per block (bottom to top) |
|---|---|
| Encoder | Input embedding + positional encoding, then Multi-Head Attention, Add & Norm, Feed Forward, Add & Norm |
| Decoder | Output embedding (outputs shifted right) + positional encoding, then Masked Multi-Head Attention, Add & Norm, Multi-Head (cross) Attention over the encoder output, Add & Norm, Feed Forward, Add & Norm |
| Output head | Linear layer, then Softmax, giving output probabilities over the vocabulary |

![Original transformer](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/transformer_encoder_decoder.svg)
*Encoder and decoder stacks, each repeated N times; the encoder output feeds the decoder's cross-attention, and the decoder output passes through Linear and Softmax.*

"Add & Norm" is a residual connection followed by normalisation. Modern LLMs are **decoder-only**: they keep the masked-attention + feed-forward block and drop the encoder.

#### The Modern Decoder Block

Every model in the LLM Architecture Gallery follows roughly the same flow:

1. Tokenise the input text.
2. Pass tokens through the token embedding layer.
3. Repeat a transformer block $N$ times:
   1. RMSNorm 1.
   2. Masked attention (with RoPE applied to queries/keys), plus a residual connection.
   3. RMSNorm 2.
   4. Feed-forward (or MoE) layer, plus a residual connection.
4. Apply a final RMSNorm.
5. Apply the linear output layer, giving one score per vocabulary token.

![Modern decoder block](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/modern_decoder_block.svg)
*Generic decoder-only block shared by Llama, DeepSeek and Gemma: RMSNorm, masked attention with RoPE, and a gated feed-forward (or MoE) layer, each wrapped in a residual connection.*

#### Three Example Architectures

The models differ in scale and in which attention, normalisation, and FFN variants they use:

| Feature | Llama 3.2 (3B) | DeepSeek V3/R1 (671B) | Gemma 4 (31B) |
|---|---|---|---|
| Total parameters | $3\text{B}$ | $671\text{B}$ | $31\text{B}$ |
| Transformer blocks | $28$ | $61$ | $60$ |
| Attention type | Masked grouped-query attention | Multi-head **latent** attention | Mix of sliding-window (local) and global attention, with GQA |
| Attention heads | $24$ | $128$ | Local: $32$ heads, $16$ KV heads. Global: $32$ heads, $4$ KV heads |
| Positional scheme | RoPE | RoPE | RoPE, plus QK-Norm |
| Normalisation | RMSNorm 1, RMSNorm 2, final RMSNorm | RMSNorm 1, RMSNorm 2, final RMSNorm | Pre- and Post-RMSNorm around both attention and FFN, final RMSNorm |
| FFN | Gated FFN with SiLU, hidden dim $8{,}192$ | MoE of SwiGLU experts, intermediate dim $2{,}048$ each | Gated FFN with GELU, input dim $5{,}376$, intermediate dim $21{,}504$ |
| Embedding dimension | $3{,}072$ | $7{,}168$ | $5{,}376$ |
| Vocabulary size | $128\text{k}$ | $129\text{k}$ | $262\text{k}$ |
| Context length | $128\text{k}$ tokens | $128\text{k}$ tokens | $256\text{k}$ tokens |

Model-specific details:

- **DeepSeek V3/R1 MoE layer**: a router sends each token to $1$ shared expert plus $8$ of $256$ routed experts. The first $3$ blocks use a dense FFN (hidden size $18{,}432$) instead of MoE.
![DeepSeek MoE layer](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/deepseek_moe_layer.svg)
*DeepSeek V3/R1 MoE layer: the router activates the shared expert plus a few routed experts per token, so only about 37B of 671B parameters are used per step.*

- **DeepSeek resource savings**: the model has $671\text{B}$ parameters, but only about $37\text{B}$ are active per inference step, i.e. $\frac{37}{671} \approx 5.5\%$ of the weights per token.
- **Gemma 4 attention mix**: local (sliding-window) and global (full-attention) layers in a $5:1$ ratio. Local layers are cheap; the occasional global layer lets information travel across the whole context.

#### LLM Architecture Gallery

The **LLM Architecture Gallery** (Sebastian Raschka) is a curated reference of modern language-model architectures. It compares architecture diagrams, implementation links, release dates, attention mechanisms, decoder types, and fact sheets, and covered $103$ models at the time of the lecture.

The takeaway: there are a great many models, and they share one basic decoder-only design with variations in attention, normalisation, and MoE.

### Harnesses

#### Definitions

> **Coding Agent / Agentic Harness**: A harness built for software work that lets an LLM read files, edit code, and run commands in a loop until a task is done.

There are many harnesses. Ten common ones are listed in the lecture:

1. Aider
2. Copilot-cli
3. Antigravity
4. Cursor
5. OpenCode
6. Claude Code
7. Cline
8. OpenHands
9. Codex
10. Continue

The same model can behave quite differently depending on the harness, because the harness controls the prompts, tools, context, and loop.

### Choosing For A Domain

The landscape problem is summed up as: so many models, so many harnesses, so little time. Nobody can evaluate every combination, so the practical question becomes:

> For a given domain, what works best?

Answering this means deciding how the LLM should interact with two things:

| Interface | Question |
|---|---|
| **People** (Part 1) | How do users give the model instructions and receive its output? |
| **Backend** (Part 2) | How does the model plug into the APIs, databases, and services of the system? |

### Interacting With People Beyond The Chatbot

#### Definitions

> **Chatbot**: A conversational text interface where the user types messages and the model replies in text.

> **AI Assistant**: A general-purpose conversational AI product, such as Microsoft Copilot or Google Gemini, or a site-specific chatbot such as UCT's AI Chatbot or Kudubot.

The default way to add AI to a product is to bolt a chatbot onto an existing website. The evolution of this pattern:

![Chatbot to integrated LLM](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/chatbot_to_integrated_llm.svg)
*From a chatbot bolted onto a website, to a chatbot that acts on the app, to an LLM built directly into the app.*

1. **Small chatbot widget**: a website with a small chatbot box in the corner.
2. **Larger chatbot panel**: the same, but with the chat panel given more space.
3. **AI assistants**: general assistants (Copilot, Gemini) and site assistants (UCT's AI Chatbot, Kudubot) that converse with the user, still separate from the main app.
4. **Chatbot acting on the app**: the chatbot sits beside the website/app and pushes changes into it, so the chat can drive the application.

In all of these the chatbot is a separate layer bolted onto existing software. This leads to the question: can the agent be meshed more tightly into the codebase?

### AI Horseless Carriages

#### Definitions

> **AI Horseless Carriage**: An AI application that copies old ways of building software and therefore needlessly constrains the AI model inside it. The term comes from Pete Koomen's essay "AI Horseless Carriages".

> **Horseless Carriage**: Early motor cars that were designed like horse-drawn carriages with an engine added, rather than redesigned around the engine.

Koomen observed that using AI to build software feels like a power tool: you can create almost anything quickly. Many AI apps do not feel like that. Their AI features feel tacked-on, useless, or even counter-productive.

The analogy:

| Horseless carriage | AI horseless carriage |
|---|---|
| Carriage design kept, engine bolted on underneath | Existing app kept, LLM bolted on as a chatbot |
| Engine's potential limited by the old carriage form | LLM's potential limited by old software patterns |
| Better: redesign the vehicle around the engine | Better: redesign the software around the AI |

The final step of the argument replaces the chatbot entirely: the LLM feeds directly into the website/app. The model becomes part of the software rather than a separate conversational window.

The guiding principle for the rest of the lecture:

> **Build the software around the AI**, and make the UI AI-friendly.

### Case Study Client Onboarding Compliance Rules

#### Definitions

> **Client Onboarding**: The process a financial firm follows when accepting a new investor: capturing their details from forms and verifying them against compliance requirements.

> **Capture Field**: A single input on a form, such as First name, Date of birth, or an Investor type checkbox.

> **Verification Rule (Check)**: A rule that validates one captured field, such as "Check if Name Present".

> **Compliance Tree (Validation Tree)**: A hierarchical arrangement of verification rules in which child checks only apply if their parent check holds.

The client is a financial administration company, called "FinCorp" here (not its real name). FinCorp administers investments on behalf of several financial product providers.

Provider companies (BankCorp, CapCorp, FundCorp in the example) each send their own onboarding documents to FinCorp. FinCorp must capture and verify the investor data in them, and engages Isazi to build the system that does this.

![Onboarding document flow](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/onboarding_document_flow.svg)
*Several providers send differently formatted onboarding documents to FinCorp, which engages Isazi to automate capture and verification.*

The forms contain sections like:

| Section | Example fields |
|---|---|
| 1. Investor | Title, First name, Last name, Date of birth, Email, Telephone, Residential address |
| 4. Investor type | Checkboxes: Individual (personal capacity); Joint holders (jointly and severally); Corporate entity (company or legal person); Trust or nominee (disclosed beneficiary) |

Verification rules form a tree. For example:

![Verification rule tree](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/verification_rule_tree.svg)
*A compliance tree: the name and ID checks apply only to individual investors, and the DB lookup applies only if a name is present.*

So the name lookup is only run if a name is present, and those checks only apply if the investor is an individual.

#### Why Manual Rule-Writing Is Slow

The scale of the problem:

| Quantity | Value |
|---|---|
| Pages per document | $\sim 30$ |
| Document types per client | $100\text{–}200$ |
| Capture fields per document | $200\text{–}300$ |
| Rules per field | $1$ |

So one client needs on the order of

$$
(100\text{–}200) \times (200\text{–}300) \times 1 \approx 20{,}000\text{–}60{,}000 \text{ rules}
$$

Writing these by hand takes a very long time, which motivates using an LLM to generate them.

### Human-UI-LLM Design And UI Beats Text

#### Definitions

> **AI-Friendly UI**: A user interface designed so AI actions are triggered by ordinary UI controls (buttons, forms, trees) and their results appear directly in the app, instead of through a free-text chat box.

> **Structured Output**: Model output in a fixed machine-readable format, here JSON, that software can parse directly.

The better design places the UI between the human and the LLM. The human never talks to the LLM directly:

1. The **human** supplies rules (the compliance requirements) through the UI.
2. The **UI** turns those rules into a **prompt** for the LLM.
3. The **LLM** returns **JSON** describing generated checks.
4. The **UI** parses the JSON and shows the result back to the human as **rules** in the compliance tree.

![Human, UI and LLM loop](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/human_ui_llm_loop.svg)
*The UI mediates in both directions: rules become a prompt on the way in, and JSON becomes rules on the way out.*

The resulting application ("Compliance Trees") has validation trees and process trees, a rules editor with a check name field, and buttons for **Expand All**, **Collapse All**, **Generate Tree**, **AI Review**, and **Create Compliance check**. AI is invoked from a button, not a chat.

Comparison of the two approaches:

| Aspect | AI-friendly UI ("Generate Tree" button) | Chatbot (e.g. an "AVA" chat window) |
|---|---|---|
| How the user triggers AI | Click a button in context | Type a free-text message |
| What the user must know | Nothing about prompting | How to phrase requests |
| Output | Structured results inserted into the app | Text the user must read and act on |
| Fit with the software | Part of the workflow | Separate window bolted on |

Principle: **UI beats text.**

### Human In The Loop

#### Definitions

> **Human in the Loop (HITL)**: A design in which a person reviews, corrects, and approves AI output before it takes effect.

> **Confidence Label**: A rating (e.g. "Confidence: high") attached to each generated item to help the reviewer decide what to trust.

LLM output is not always correct, so a person must check it. Two requirements:

- You need a **UI to make corrections**.
- Again, **prefer UI to text** for those corrections.

The "Confirm Generated Checks" dialog shows how this works:

1. The system reports how many checks were generated (e.g. "Generated 3 new checks").
2. Each check has a checkbox so the user selects which to import ("Select all" is available).
3. Each check shows its name and editable metadata: template type (e.g. PresenceCheck), type (presence), data type (text), mapped fields, comments, and a confidence label.
4. The user can edit a check inline (Edit/Done), fix field mappings, and remove wrong mappings.
5. Only the selected, corrected checks are imported into the tree.

### Backend System Overview

The backend extends the Human-UI-LLM design with an API layer and a database:

| Component | Technology | Role |
|---|---|---|
| UI | Vue JS | Front end where users manage rules and trees |
| API | Golang | Backend that builds prompts, calls the LLM, and stores results |
| DB | Postgres | Stores rules, trees, field aliases, and related data; read and written by the API |
| LLM | Azure GPT | Generates checks as JSON |

![Backend system overview](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/backend_system_overview.svg)
*The API sits at the centre: it exchanges rules with the UI, reads and writes Postgres (e.g. to fetch field aliases), sends prompts to Azure GPT and receives JSON back.*

The LLM is one component among ordinary software components, not the centre of the system.

### Harness Design Keep Things Simple

#### Definitions

> **Subagent**: A separate LLM agent launched by a parent agent to handle part of a task.

> **Tool (Tool Call)**: A function the harness exposes to the LLM so it can take actions or fetch data, such as querying a database.

> **Infinite Loop (Agentic)**: When an agent keeps calling tools without ever converging on a final answer.

> **Formatted String Prompt**: A prompt template with placeholders (e.g. `%s` in Go) filled in by code with the needed data before the call.

Lessons for building the harness:

1. **Don't use subagents.** They add complexity and make behaviour harder to control.
2. **Tools can cause infinite loops.** An agent with tools may keep calling them without ever finishing.
3. **Formatted strings are better.** Instead of giving the model tools to fetch data, the code puts the data straight into the prompt template.

| Approach | How the model gets data | Risk |
|---|---|---|
| Tool calling | Model decides when to call tools to fetch data | Loops, unpredictable number of calls |
| Formatted string | Code inserts all needed data into the prompt up front | Predictable; one call per task |

### AI Review And Generation Agents

#### Definitions

> **Review Agent**: An LLM prompt that inspects existing checks and reports errors and warnings with suggestions.

> **Generation Agent**: An LLM prompt that creates new checks from rule text, written to follow the same rules the review agent enforces.

> **Failure Situation**: A known way the output can be wrong, written explicitly into a prompt so the model can detect or avoid it.

The build order mattered:

1. **First build a review agent.** It examines a tree and reports issues. Example output: "AI Review Results: Rules, 2 errors, 11 warnings", e.g. ERROR on "Check if investment amount is provided": field mapping is missing; suggestion: set the Investment Amount field alias.
2. **Then build the generation agent**, which follows the review rules. Because the review rules already describe what "bad" looks like, the generator can be told to avoid exactly those failures.

**Failure situations are written into both prompts.** Example review rules:

1. If a check is an exact duplicate of a sibling (same check type and intent), it should be flagged.
2. Highlight discrepancies in parent-child relationships. For example, if a child check has "entity" in the name but the parent check has "individual", this should be flagged.

The same rules tell the reviewer what to flag and the generator what not to produce.

![Review and generation agents](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/review_and_generation_agents.svg)
*One set of failure situations drives both prompts: the review agent flags them in the tree, and the generation agent avoids them when adding checks.*

### Context And Prompt Design

#### Definitions

> **Context**: All information given to the LLM in its prompt, such as the source text, available identifiers, and examples.

> **Few-Shot Example**: An input/output example included in the prompt to show the model the expected output format and style.

> **Field Alias**: An identifier (`field_alias_id`) for a captured form field that a generated check must reference.

> **Comment Preset**: A predefined comment (`comment_id`, with parameters `comment_parameter_id`) that can be linked to a check.

**Context is key:**

1. Include as much context as possible.
2. Rather have too much than too little.

The context section of the generation prompt is a formatted string with labelled placeholders:

```text
Rules text:
%s

Available field aliases (use field_alias_id to reference them):
%s

Available comment presets (link checks to comments using comment_id, map parameters using comment_parameter_id):
%s
```

Each `%s` is filled by the API with data from the database, so the model can map rules to real IDs.

**Prompt tips**, illustrated by the generation prompt:

- Give explicit **examples** with labelled Input and Output:

```text
## Examples
- Input: "Section 3A, Whether the Investor Name is provided."
  Output: {"check_name": "Check if non-us person status one option is selected",
  "check_type": "presence", "check_data_type": "text",
  "check_description": "Check if non-us person status one option is selected"}
```

- Give numbered **instructions**:
  1. Generate check names for rules that can be understood by a non-technical business user.
  2. If a rule is very unclear, set `skipped_reason` instead of generating a check.
  3. For each generated check, map rule text to field aliases from the existing aliases above.

Design points shown by these instructions:

- Output is JSON with fixed keys (`check_name`, `check_type`, `check_data_type`, `check_description`), so code can parse it.
- Write for the end user: names must make sense to non-technical business users.
- Give the model a way out: `skipped_reason` lets it decline unclear rules instead of inventing a check.
- Constrain references: aliases must come from the supplied list.

### Choosing The Right Model

Model choice in production is driven by more than benchmark scores:

1. **Compliance is a concern.** Financial clients have strict rules about where data goes and who processes it.
2. **Limited by region and approvals.** Only models available in approved regions and approved by the client can be used (here, GPT via Azure).
3. **More recent is generally better.** Among allowed models, newer ones usually perform better.

### LLM Fine-Tuning Vs Prompt Fine-Tuning

#### Definitions

> **LLM Fine-Tuning**: Further training a model's weights on task-specific data.

> **Open-Weights Model**: A model whose trained weights are published, so it can be self-hosted and fine-tuned.

> **Prompt Fine-Tuning**: Improving system behaviour by iteratively revising the prompt instead of the model weights.

Weight fine-tuning is often not an option:

- Modern models **don't allow** it (e.g. the GPT-5/6 series).
- Open-weights models can be fine-tuned, but that is **complex**.

Prompt fine-tuning is the practical alternative:

1. Iteratively test and tune the prompt.
2. Add points to the prompt based on **interaction** with the LLM (when you see a failure, add an instruction that addresses it).
3. Use end-user **feedback**, which is very helpful.

| Aspect | LLM fine-tuning | Prompt fine-tuning |
|---|---|---|
| What changes | Model weights | Prompt text |
| Availability | Blocked for many closed models; possible for open weights | Always available |
| Effort | Complex (data, training, hosting) | Iterative testing and editing |
| Feedback source | Training dataset | Observed LLM behaviour and end-user feedback |

### Textual Gradients (TextGrad)

#### Definitions

> **TextGrad (Textual Gradients)**: A method for automatically optimising prompts and other text in an AI system by using an LLM to write natural-language "gradients": critiques saying how a piece of text should change to reduce the loss.

> **Backpropagation**: In neural networks, the algorithm that computes the gradient of the loss with respect to each parameter, moving backwards from the output.

TextGrad treats an LLM pipeline like a neural network and "backpropagates" feedback in words instead of numbers.

| Aspect | Neural network backpropagation | TextGrad |
|---|---|---|
| System | Layers of neurons with numeric weights | Blackbox AI components: LLM calls, search engine, tool caller |
| Variables optimised | Weights and activations | Prompts, queries, tool prompts, responses |
| Loss | Numeric loss on the output | An LLM evaluates the final output against an evaluation instruction |
| Gradient | Number, e.g. $\frac{\partial \mathcal{L}}{\partial v_1} = 0.124$, $\frac{\partial \mathcal{L}}{\partial h_1} = 0.267$ | Text, e.g. $\frac{\partial \mathcal{L}}{\partial \text{Response}} =$ "this response can be improved by..." |
| Update | Subtract gradient times learning rate | Rewrite the text following the critique |

![TextGrad versus backpropagation](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/textgrad_backpropagation.svg)
*(a) Numeric gradients flow back through a neural network; (b) TextGrad passes natural-language critiques back through a pipeline of LLM, search and tool components.*

In the numeric case, gradients flow from the loss back through the output and hidden layer to the inputs. In TextGrad, the flow is:

1. Inputs (a prompt, a query, a tool prompt) are sent to components (LLM, search engine, tool caller), producing intermediate outputs.
2. These feed another LLM that produces the final output.
3. An LLM evaluates the final output against an evaluation instruction, giving the loss.
4. Feedback is passed backwards: first $\frac{\partial \mathcal{L}}{\partial \text{Response}}$ ("this response can be improved by..."), then $\frac{\partial \mathcal{L}}{\partial \text{Prompt}}$ ("this prompt can be improved by...").
5. Each prompt is revised using its textual gradient, and the process repeats.

This automates the prompt fine-tuning loop from the previous section.

### Creative Prompting With Rewards And Penalties

Prompts can use creative devices to steer behaviour. An example from a coding-harness system prompt (shown beside the Claude Code mascot, so apparently from Claude Code):

```text
### EXAMPLES

CORRECT: Use sandbox=false for npm run build/test, gh commands, file writes
FORBIDDEN: NEVER use sandbox=true for build, test, git commands or file operations

## REWARDS

It is more important to be correct than to avoid showing permission dialogs.
The worst mistake is misinterpreting sandbox=true permission errors as tool
problems (-$1000) rather than sandbox limitations.
```

Techniques shown:

- **Labelled examples**: CORRECT vs FORBIDDEN cases make the boundary explicit.
- **Emphatic wording**: "NEVER" in capitals marks hard rules.
- **Priorities**: stating what matters more (correctness over avoiding dialogs).
- **Fictional rewards/penalties**: a "$-\$1000$" penalty signals which mistake is worst, even though no money is involved.

The message: be creative and have fun when writing prompts.

### The LLM Sits In An Environment

The closing point of the lecture: **the LLM is not alone.** It sits in an environment made of:

| Element | Role |
|---|---|
| Human | Gives goals and rules, reviews and corrects output |
| LLM | Generates content |
| UI / software | Connects the two, structures input and output |

![LLM in its environment](../../../diagrams/CSC3044S-AI%20Systems/AIS/05_Agent_Architectures_LLMs/llm_in_environment.svg)
*The LLM sits between the human and the UI/software, with two-way links to each.*

Good LLM systems come from designing the whole environment, not just picking a model.

The vision is human-AI collaboration: a person and an AI working together as partners, with the AI becoming highly skilled (shown as a robot partnering a human, then a robot with a black belt).

### Bonus Menu-Driven Chat Interfaces

A FlySafair chat interface is shown as a good pattern: even inside a chat, the user is offered a **menu** of structured options instead of free text:

| Option | Purpose |
|---|---|
| My Bookings | View and manage your bookings |
| Check In | Don't miss your flight |
| New Booking | Book a flight to any of the destinations |
| Travel Services | Book airport services |
| Modifications | Flight changes, seat changes, name changes, adding services |

This applies the same principle as "UI beats text": structured choices are clearer and more reliable than open-ended typing.
