---
tags:
  - ai-systems
---

# Agent Workflow

**Subject**: CSC3044S AI Systems
**Source**: `LLM Agents 4_ Agent Workflow.pdf`, Dr Francois Meyer (LLM Agents Topic 4, based on the Hugging Face Agents Course Unit 1), slides 1-35
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Building an LLM Agent From Scratch|Building an LLM Agent From Scratch]]
  - [[#AI Agents and LLM Agents|AI Agents and LLM Agents]]
  - [[#The Agent Harness|The Agent Harness]]
  - [[#What LLM Agents Do|What LLM Agents Do]]
  - [[#Tools and Tool Calls|Tools and Tool Calls]]
  - [[#ReAct|ReAct]]
  - [[#The Thought-Action-Observation Cycle|The Thought-Action-Observation Cycle]]
  - [[#Thought|Thought]]
  - [[#Action|Action]]
  - [[#Code Agents|Code Agents]]
  - [[#Observation|Observation]]
  - [[#Implementing the Cycle With the System Prompt|Implementing the Cycle With the System Prompt]]
  - [[#Weather Agent Example|Weather Agent Example]]
  - [[#Iterating to Solve Complex Problems|Iterating to Solve Complex Problems]]
  - [[#Model Training Versus Harness Engineering|Model Training Versus Harness Engineering]]

---

## Core Content

### Building an LLM Agent From Scratch

A system like Claude Code is built in four stages. Earlier topics covered the first three; this topic covers the fourth.

| Stage | What it means | Concrete version |
|---|---|---|
| 1. Scale pretraining | Train a bigger LLM on more data | Billions or trillions of parameters |
| 2. Scale generation (test-time scaling) | Let the model spend more compute reasoning at inference | **RLVR** (RL with verifiable rewards) for test-time scaling |
| 3. Enable files and tools | Let the LLM read files and call tools | Equip it with multiple tools (about 20, according to Anthropic) |
| 4. Wrap in an agentic framework | Put the LLM inside a loop that acts and observes | An agentic loop plus **harness engineering** |

The Claude Code agentic loop is a concrete instance of stage 4. The user's prompt enters a loop of gathering context, taking action and verifying results, which repeats until the task is done. The user can interrupt, steer or add context while the loop runs.

![Claude Code agentic loop](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/claude_code_agentic_loop.svg)
*Claude Code's agentic loop: gather context, take action, verify results, repeat until done, with the user able to steer mid-loop.*

### AI Agents and LLM Agents

#### Definitions

> **Agent** (Russell & Norvig): Anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.

> **LLM Agent**: A system that leverages an LLM to interact with its environment to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfil tasks.

An LLM agent combines three ingredients:

- **LLM**: the reasoning engine (the "brain").
- **Memory**: the context and state the agent carries forward.
- **Tools**: the external functions it calls to act.

![LLM agent components](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/llm_agent_components.svg)
*An AI agent is assembled from an LLM, memory and tools.*

### The Agent Harness

#### Definitions

> **Agent Harness**: Software infrastructure around an LLM that enables it to operate as an AI agent. It manages tool use, memory, state persistence, and feedback loops, as opposed to the model's internal reasoning.

The model does the reasoning; the harness does everything else needed to act in the world. Three analogies capture the split:

| Model | Harness |
|---|---|
| model | harness |
| brain | body |
| CPU | OS |

Components a harness can contain:

| Component | Role |
|---|---|
| System prompts | Instructions that define behaviour, tools and the agent loop |
| 3rd-party tools | External APIs and functions the LLM can call |
| Skills | Packaged, reusable capabilities |
| Sub-agents | Other agents the main agent can delegate to |
| Loop control | Runs the Thought-Action-Observation loop and decides when it stops |
| RAG | Retrieval of relevant documents into context |
| Context loading | Deciding what information is placed in the LLM's context |
| Code sandbox | A safe environment for executing generated code |

![Agent harness](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/agent_harness.svg)
*The LLM sits outside the harness and plugs into it; the harness supplies tools, prompts, memory/context, sandboxing and loop control.*

### What LLM Agents Do

LLM agents use the LLM as their core reasoning engine to:

- **Understand natural language**: interpret and respond to human instructions.
- **Reason and plan**: analyse information, make decisions, and devise strategies to solve problems.
- **Interact with the environment**: gather information, take actions, and observe the results of those actions.

For a coding agent, the environment interaction looks like this:

| Element | Examples |
|---|---|
| Environment | Codebase, browser, operating system |
| Observations | File contents, tool results, code output |
| Actions | Read a file, run a command, call an API, edit code |

Example applications:

| Agent | What it does |
|---|---|
| Coding agent | Reads the codebase, writes and edits files, runs tests, and iterates until the task is complete |
| Customer service chatbot | Answers questions, guides users, opens issues in databases |
| Personal virtual assistant | Reads email and calendar, drafts replies, books things |
| AI non-playable character (NPC) | Makes video-game NPCs more dynamic and able to interact with gamers contextually |

### Tools and Tool Calls

#### Definitions

> **Tool**: A function the agent can invoke to perform an action in its environment.

> **Tool Call**: Text generated by the LLM that names a tool and its arguments, which is then executed.

An agent can do any task that can be performed via **tools** to complete **actions**.

Example: a personal-assistant agent asked to "send an email to my manager to delay today's meeting" can be given email-sending code:

```python
def send_email(recipient, message):
    # Send e-mail message to a recipient
```

When it needs to, the LLM generates a tool call to run the tool:

```python
send_email("Manager", "Can we postpone today's meeting?")
```

Tool design and interfacing greatly impact the quality of the agent.

| Tool type | Example | Use |
|---|---|---|
| Task-specific | `send_email` | Required for a particular task |
| General-purpose | `web_search` | Can solve many different tasks |

### ReAct

Previous topics covered **test-time scaling** (how LLMs reason and plan) and **tools** (how to equip LLMs with tools). The complete AI agent workflow combines both in the **Thought-Action-Observation** cycle. ReAct is one example of it.

#### Definitions

> **ReAct**: A prompting technique that combines Reasoning (Thought) with Acting (Act). It encourages the model to think step-by-step and interleave actions (like using tools) between reasoning steps.

ReAct alternates between three step types:

| Step | Meaning |
|---|---|
| Thought | Internal reasoning |
| Action | Tool usage |
| Observation | Receiving tool output |

Example trace:

| Step | Content |
|---|---|
| Thought | I need to find the latest weather in Paris. |
| Action | `Search["weather in Paris"]` |
| Observation | It's 18°C and cloudy. |
| Thought | Now that I know the weather... |
| Action | Final answer: It's 18°C and cloudy in Paris. |

ReAct is a *prompting technique*. It is one example of the more general framework for agentic LLMs, the Thought-Action-Observation cycle.

### The Thought-Action-Observation Cycle

#### Definitions

> **Thought-Action-Observation (TAO) Cycle**: The continuous cycle of thinking, acting and observing in which an agent works.

The three components:

- **Thought**: the LLM part of the agent decides what the next step should be.
- **Action**: the agent performs an action, often by calling tools.
- **Observation**: the model reflects on the response from the tool.

![Thought-Action-Observation cycle](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/tao_cycle.svg)
*Thought leads to Action, Action to Observation; the Observation feeds back into the next Thought until the agent produces an Answer.*

The components work together in a continuous loop. **The loop continues until the objective of the agent has been fulfilled.**

![Thought-Action-Observation loop](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/tao_loop_flowchart.svg)
*The same loop as a flowchart: a query enters Thought, which either acts on a tool and receives an observation, or exits to the answer.*

### Thought

#### Definitions

> **Thought**: The step that uses the LLM's reasoning capacity to reason about solving the task. Its goal is to assess current observations and decide on the next action(s).

Sophisticated forms of reasoning emerge from test-time scaling. For OpenAI's o1 on AIME, pass@1 accuracy rises steadily (from roughly 20% to roughly 75%) as test-time compute increases on a log scale.

![o1 test-time scaling](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/o1_test_time_scaling.svg)
*o1 AIME pass@1 accuracy grows roughly linearly in the log of test-time compute, which is why stronger reasoning improves the Thought step.*

Types of thought:

| Type of thought | Example |
|---|---|
| Planning | "I need to break this task into three steps: 1) gather data, 2) analyze trends, 3) generate report." |
| Analysis | "Based on the error message, the issue appears to be with the database connection parameters." |
| Decision making | "Given the user's budget constraints, I should recommend the mid-tier option." |
| Problem solving | "To optimize this code, I should first profile it to identify bottlenecks." |
| Memory integration | "The user mentioned their preference for Python earlier, so I'll provide examples in Python." |
| Self-reflection | "My last approach didn't work well, I should try a different strategy." |
| Goal setting | "To complete this task, I need to first establish the acceptance criteria." |
| Prioritisation | "The security vulnerability should be addressed before adding new features." |

### Action

#### Definitions

> **Action**: The concrete steps an AI agent takes to interact with its environment.

The type of actions depends on the type of agent.

| Type of action | Description |
|---|---|
| Information gathering | Performing web searches, querying databases, or retrieving documents |
| Tool usage | Making API calls, running calculations, writing/executing code |
| Environment interaction | Manipulating digital interfaces or controlling physical devices |
| Communication | Engaging with users or collaborating with other agents |

### Code Agents

#### Definitions

> **Code Agent**: An agent that, instead of calling special tools, writes and executes code to perform the action.

> **CodeAct**: An LLM agent that uses code as its action format, in contrast to an agent that uses text/JSON tool calls as actions.

Example task: find the most cost-effective country (USA, Japan, Germany, India) to buy the smartphone "CodeAct 1", given APIs `lookup_rates`, `lookup_phone_price`, `convert_and_tax`, `estimate_shipping_cost` and `estimate_final_price`.

| | Text/JSON as action | CodeAct (code as action) |
|---|---|---|
| Actions needed | One action per API call per country, each followed by an environment response | One code block covering every country |
| Control flow | Handled by the LLM across many turns | A `for` loop over countries |
| Combining results | LLM compares values itself | Reuses Python's built-in `min(final_prices, key=final_prices.get)` |
| Result | Japan, 904.00 USD | Japan, 904.00 USD, with fewer actions required |

![Code agent vs JSON agent](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/code_agent_vs_json.svg)
*The same task done with JSON/text actions (many round trips) versus CodeAct (one code action using a loop and `min()`).*

Advantages and disadvantages of code agents:

| Advantages | Disadvantage |
|---|---|
| **Expressiveness**: code provides greater flexibility than JSON | Executing LLM-generated code may pose **security risks** (hence a code sandbox in the harness) |
| **Direct integration**: can integrate directly with external libraries, enabling more complex operations such as data processing | |
| **Modularity and reusability**: code is reusable across different actions | |

### Observation

#### Definitions

> **Observation**: How the agent perceives the consequences of its actions. Signals from the environment (e.g. API results, database changes, error messages, system logs) that guide the next cycle of thought and action.

In the observation phase, the agent:

1. **Collects feedback**: receives data on whether the action was successful or not.
2. **Appends results**: integrates the new information into its existing context, effectively *updating its memory* to adapt its strategy.

For example, if a weather API returns "partly cloudy, 15°C, 60% humidity", this observation is **appended at the end of the prompt before the LLM generates** again.

This **iterative** feedback incorporation keeps the agent dynamically aligned with its goals, constantly adjusting based on real-world outcomes.

### Implementing the Cycle With the System Prompt

#### Definitions

> **System Prompt**: Instructions prepended to the user prompt that, in many LLM agent frameworks, describe the AI agent workflow.

The system prompt can include:

- Expectations about the agent's behaviour.
- The tools the agent has access to.
- Instructions on the Thought-Action-Observation cycle.

Example system message:

```text
You are an AI assistant designed to help users efficiently and accurately. Your
primary goal is to provide helpful, precise, and clear responses.

You have access to the following tools:
Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int

You should think step by step in order to fulfill the objective with a reasoning divided into
Thought/Action/Observation steps that can be repeated multiple times if needed.

You should first reflect on the current situation using `Thought: {your_thoughts}`, then (if
necessary), call a tool with the proper JSON formatting `Action: {JSON_BLOB}`, or print your final
answer starting with the prefix `Final Answer:`
```

The fixed prefixes (`Thought:`, `Action:`, `Final Answer:`) are what let the harness tell a tool call apart from a final answer.

### Weather Agent Example

A weather agent answers "What's the current weather in New York?" using a weather API tool. The cycle unfolds as follows:

1. **Thought (model reasoning)**: the LLM's reasoning trace might be: "The user needs current weather information for New York. I have access to a tool that fetches weather data. First, I need to call the weather API to get up-to-date details."
2. **Action (tool usage)**: based on its reasoning and the tools listed in the system prompt, the LLM generates a JSON-formatted tool call:
   - "I need to check the current weather for New York."
   - `{"action": "get_weather", "action_input": {"location": "New York"}}`
3. **The LLM stops generating.** The harness parses the call and calls the tool.
4. **Observation (feedback from environment)**: the harness receives "Current weather in New York: partly cloudy, 15°C, 60% humidity." from the weather API.
5. The observation is **added to the prompt as additional context**, and the LLM is prompted to generate again, letting it update its reasoning.
6. **Thought + final answer**: "I have the weather data now. The current weather in New York is partly cloudy, 15°C and 60% humidity. Final answer: The current weather in New York is partly cloudy with a temperature of 15°C and 60% humidity."
7. The harness sees that the model has generated the final answer, extracts it and shows it to the user, closing the loop.

All of the tool execution in steps 3-5 is managed by the **harness**: it calls the tool, retrieves the response, appends it to the LLM context, and prompts the LLM to generate again. The LLM only ever generates text.

![Weather agent sequence](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/weather_agent_sequence.svg)
*Who does what in the weather example: the LLM produces thoughts, tool calls and the final answer; the harness runs the tool, appends the observation and returns the answer.*

### Iterating to Solve Complex Problems

Complex problems are solved by repeating the loop:

- Agents **iterate** through the loop (potentially many times) until, during **Thought**, the model concludes it is ready to give the final answer.
- Each cycle incorporates new information (Observations) into its reasoning (Thought), taking it closer to the final answer.
- **This behaviour can be learned with RL.**

For different types of agents the loop looks slightly different, but it can always be mapped to thoughts, actions and observations. A coding agent loop:

1. Observe the repo.
2. Plan.
3. Search/read files.
4. Edit/write patches.
5. Run tests. If they pass, the agent is done.
6. Otherwise inspect the errors and repeat, returning to search/read files (or back to planning).

![Coding agent loop](../../../diagrams/CSC3044S-AI%20Systems/LLM%20Agents/04_Agent_Workflow/coding_agent_loop.svg)
*A coding agent's loop mapped onto Thought (plan), Action (search, edit, run tests) and Observation (repo state, errors).*

### Model Training Versus Harness Engineering

#### Definitions

> **LLM Training**: Changing model behaviour through pretraining, supervised finetuning, or RL, so the model acquires capabilities combining reasoning and tool use.

> **Harness Engineering**: Changing the system around the model: prompts, tools, memory, and control flow.

| | LLM training | Harness engineering |
|---|---|---|
| What changes | The model's weights | The system around the model |
| Methods | Pretraining, supervised finetuning, RL | Prompts, tools, memory, control flow |
| Gains | Reasoning and tool-use capability inside the model | Better context, tools and loop control around the model |

**LLM agent capabilities emerge from the model-harness combination.**

Lilian Weng ("Harness Engineering for Self-Improvement") argues that many harness improvements may eventually be internalised into core model behaviour, but the interface with external context and tools should remain. Prompt engineering followed a softer version of this pattern: manual prompt tricks became less central as instruction tuning and model reasoning improved, but the need to specify goals, constraints, context and evaluation did not disappear.

Open questions for LLM agents: bigger models, better harnesses, or models that self-improve by designing harnesses for themselves?

Prescribed reading: Hugging Face Agents Course Unit 1 (the slides are the main exam resource).
