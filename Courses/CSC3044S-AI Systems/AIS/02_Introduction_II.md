---
tags:
  - ai-systems
---

# Introduction II: Reactive, Deliberative, And Learning Agents; Generative AI, Agents, And Assistants

**Subject**: CSC3044S AI Systems  
**Source**: `2026-CSC3044S-Lecture 2-Introduction (II) - Copy.pdf`, Geoff Nitschke, pages 1-55  
**Generated**: 2026-11-08

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Recap: Rational Agents And Agent Types|Recap: Rational Agents And Agent Types]]
  - [[#Reactive Agents: Stimulus-Response|Reactive Agents: Stimulus-Response]]
  - [[#Deliberative Agents: Sense-Plan-Act|Deliberative Agents: Sense-Plan-Act]]
  - [[#The Representation Problem|The Representation Problem]]
  - [[#Learning Agents|Learning Agents]]
  - [[#Reactive Versus Deliberative Paradigms|Reactive Versus Deliberative Paradigms]]
  - [[#Braitenberg's Vehicles|Braitenberg's Vehicles]]
  - [[#Reactive Sense-Act Controllers And The Roomba|Reactive Sense-Act Controllers And The Roomba]]
  - [[#AI Operating Systems And Virtual Assistants|AI Operating Systems And Virtual Assistants]]
  - [[#The 2026 Agent Landscape And OSWorld|The 2026 Agent Landscape And OSWorld]]
  - [[#Generative AI Versus AI Agents|Generative AI Versus AI Agents]]
  - [[#AI Agents Versus AI Assistants|AI Agents Versus AI Assistants]]
  - [[#Classifying Systems: Booking Assistant And Autonomous Vehicle|Classifying Systems: Booking Assistant And Autonomous Vehicle]]

---

## Core Content

### Recap: Rational Agents And Agent Types

#### Definitions

> **Rational**: Maximally achieving pre-defined goals.

> **Utility**: The measure in which goals are expressed — how desirable an outcome is.

> **Rational Behaviour**: Maximising your **expected utility**.

Goals are not stated as fixed targets but as the **utility** of outcomes. Because outcomes are uncertain, a rational agent picks the action whose outcomes are best on average. In the standard formulation, the agent chooses

$$
a^* = \arg\max_{a} \; \mathbb{E}[U \mid a] = \arg\max_{a} \sum_{s'} P(s' \mid a)\, U(s')
$$

where $U(s')$ is the utility of resulting state $s'$ and $P(s' \mid a)$ is the probability of reaching it after action $a$.

The three types of (rational) agents covered in this course:

| Agent Type | Also Called | Sub-types / Examples |
|---|---|---|
| **Reactive** | Reflexive | Simple and model-based reflex agents |
| **Deliberative** | Goal-based | Planning / symbolic reasoning agents |
| **Learning** | (a kind of deliberative agent) | RL, ANN, LLM-based agents |

Learning agents are presented as a sub-category under deliberative agents.

### Reactive Agents: Stimulus-Response

#### Definitions

> **Reactive (Reflexive) Agent**: An agent that just reacts to the current (sensed) environment state, with behaviour dictated by immediate sensory input and rules mapping inputs $\rightarrow$ outputs.

> **Percept**: The sensory input an agent receives from its environment.

> **Sensors**: Components through which the agent perceives the environment.

> **Actuators**: Components through which the agent acts on the environment.

> **Condition-Action Rule**: A rule of the form "if this condition holds, do this action".

> **Primitive Actions ($A$)**: The basic actions the agent is capable of doing.

Reactive agents sense their environment and react to any new information. Their key properties:

- Respond only to the **current** sensed state.
- Behaviour comes from immediate input plus fixed input $\rightarrow$ output rules.
- **No memory**, no internal state, no explicit description of the environment, and no goals.

#### Reactive Agent Architecture

The simple reflex agent runs a continuous loop: percepts come in through sensors, condition-action rules pick an action for the current view of the world, and actuators carry it out.

![Reactive agent](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/reactive_agent.svg)
*Simple reflex agent: the only inputs to the decision are the current percept and the fixed condition-action rules. There is no memory and no model.*

Mathematically, reactive behaviour is a direct mapping from states to actions:

$$
\text{action}: S \rightarrow A
$$

where $S$ is the set of environment states and $A$ is the set of primitive actions.

**Example: a thermostat (e.g., Nest)**

$$
\text{action}(s) =
\begin{cases}
\text{Heater on}, & \text{if temperature too low} \\
\text{Heater off}, & \text{otherwise}
\end{cases}
$$

The thermostat senses temperature and applies one rule. It keeps no history and has no model of how the room will change.

#### Problems With Reactive Agents

| Problem | Explanation |
|---|---|
| Handcrafted | Rules are designed by hand; development takes a lot of "tuning". |
| Single-purpose | An agent can be used only for its original purpose. |
| Scalability | It may be impossible to build large systems from hand-made rules. |
| No learning | There is no mechanism for the agent to learn or improve. |

### Deliberative Agents: Sense-Plan-Act

#### Definitions

> **Deliberative (Goal-Based) Agent**: An agent that senses its environment, generates a plan, and acts on the plan.

> **Internal State**: Information the agent keeps about the world beyond the current percept (memory).

> **Plan**: The mechanism mapping inputs $\rightarrow$ outputs, e.g., logical reasoning, symbolic manipulation, a rule-set, or an ANN.

> **Transduction Problem**: It is impractical to translate the needed information into symbolic representations, especially if the environment is changing (dynamic).

> **Symbolic AI**: AI that uses an explicitly represented, symbolic model of the world and decides via symbolic reasoning (manipulating symbols with logic, rule-sets, decision trees).

Deliberative behaviour is dictated by three things:

1. The (sensed) **environment state**.
2. The agent's **internal state**.
3. A **plan** that maps inputs to outputs.

Unlike reactive agents, deliberative agents usually have **memory**, internal state, an explicit description of the environment, and **goals**.

#### Deliberative Agent Architecture

The goal-based agent's internal components:

| Component | Role |
|---|---|
| State | Stored internal state (memory) of the world, updated from sensor input |
| How the world evolves | Model of how the environment changes on its own |
| What my actions do | Model of the effects of the agent's actions |
| What the world is like now | Current world estimate, built from sensors + State + both models |
| What it will be like if I do action A | Predicted outcome of a candidate action (look-ahead) |
| Goals | Desired outcomes |
| What action I should do now | Decision made by comparing predicted outcomes against Goals |

![Deliberative agent](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/deliberative_agent.svg)
*Goal-based agent: State and the two world models give an estimate of the current world. The agent predicts the result of each candidate action and compares it with its Goals before acting. The dashed line shows the State being updated.*

Examples of deliberative agents: car GPS navigation (e.g., Garmin), self-driving cars (e.g., Waymo), LLM-based agents (e.g., Claude), and robot vacuum cleaners (e.g., Roomba).

#### How Deliberative Agents Work

Most deliberative agents use Symbolic AI algorithms:

- They contain an **explicitly represented, symbolic model** of the world.
- They decide which actions to perform via **symbolic reasoning** — manipulating symbols with logic, rule-sets, decision trees.

The classic Symbolic AI deliberative agent is a **game-playing agent** (Chess, Go) using **top-down symbolic algorithms**. It builds a game tree from the current position and searches it for the best move:

![Game tree](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/game_tree.svg)
*Top-down symbolic search. Each position (ComputerMove) expands into every position one move away (ComputerMove2, ComputerMove3, ...), so the tree grows exponentially with depth.*

#### Problems With Deliberative Agents

| Problem | Explanation |
|---|---|
| Transduction problem | Converting real-world sensed data into symbols is impractical, especially in dynamic environments. |
| Representation problem | Hard to encode knowledge, problems, and data compactly (see next subsection). |
| Limited adaptivity | Fixed symbolic models do not adapt well to change. |
| Poor scaling | They do not scale to real-world scenarios. |

### The Representation Problem

#### Definitions

> **Knowledge Representation**: How to encode facts, rules, causality, and time in (agent) models — e.g., Bayes' rule versus neural networks.

> **Problem Representation**: How to define a task (environment) that a model must operate in — e.g., Chess versus an autonomous vehicle.

> **Data Representation**: How to translate unstructured data (captured text, images, audio) into useful data structures — e.g., high-dimensional vectors as neural network input layers.

The AI representation problem has three parts:

| Part | Question | Example Contrast |
|---|---|---|
| Knowledge | How do we encode facts, rules, causality, time? | Bayes' rule vs neural networks |
| Problem | How do we define the task/environment? | Chess (closed, well-defined) vs autonomous vehicle (open, messy) |
| Data | How do we turn raw unstructured data into usable structures? | Text/images/audio $\rightarrow$ high-dimensional input vectors |

**The general issue** is the complexity of symbol manipulation algorithms:

- Most (search-based) symbol manipulation algorithms are **highly intractable** and limited — e.g., game-playing algorithms, whose search trees grow exponentially.
- It is hard to find **compact representations** for most problems.
- This drove the rise of other agent architectures, such as **neuro-AI based** (neural network) approaches.

### Learning Agents

#### Definitions

> **Learning Agent**: An agent that improves its behaviour over time using feedback (e.g., RL, ANN, LLM agents).

> **Performance Standard**: The external standard against which the agent's behaviour is judged.

> **Critic**: Component that observes sensor input, compares it against the performance standard, and gives feedback.

> **Learning Element**: Component that uses the critic's feedback to make changes (improvements) to the performance element.

> **Performance Element**: Component that selects external actions (the "acting" part — equivalent to a whole non-learning agent).

> **Problem Generator**: Component that suggests exploratory actions (experiments) that lead to new, informative experiences.

> **Reinforcement Learning (RL) Agent**: A learning agent that interacts with an environment by taking actions and receiving a state and a scalar reward signal in return.

> **Effectors**: Components that carry out actions in the environment (same role as actuators).

#### Learning Agent Architecture

![Learning agent](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/learning_agent.svg)
*Learning agent: the critic judges outcomes against the performance standard, the learning element changes the performance element, and the problem generator proposes exploratory experiments.*

The learning cycle:

1. The **performance element** chooses actions from percepts, executed by **effectors**.
2. The **critic** compares the results (via sensors) to the **performance standard** and sends **feedback**.
3. The **learning element** uses feedback to change the performance element, drawing on its knowledge.
4. The learning element sets **learning goals** for the **problem generator**.
5. The problem generator proposes **experiments** (exploratory actions) to the performance element.

Examples of learning agents: DeepSeek (LLM), autonomous off-road vehicles (e.g., DARPA-challenge-style robot cars), AlphaFold 3 (predicts the structure and interactions of all life's molecules), AlphaGo (defeated Ke Jie at Go), and legged robots that learn to walk from scratch.

#### Reinforcement Learning Agent

![Reinforcement learning loop](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/rl_loop.svg)
*RL loop: the agent sends action $a_t$ to the environment, which returns the new state $s_t$ and the reward $R_t$.*

At each time step $t$:

1. The agent observes state $s_t$ and reward $R_t$ from the environment.
2. The agent chooses action $a_t$.
3. The environment responds with the next state $s_{t+1}$ and reward $R_{t+1}$.
4. Repeat; the agent learns to choose actions that maximise reward over time.

$$
s_t, R_t \;\xrightarrow{\text{agent}}\; a_t \;\xrightarrow{\text{environment}}\; s_{t+1}, R_{t+1}
$$

### Reactive Versus Deliberative Paradigms

#### Definitions

> **Closed World**: An environment that can be fully modelled in advance.

> **Open World**: An environment that cannot be fully modelled in advance; unexpected situations occur.

> **Top-Down Problem Solving**: Solving from an internal model and plan downward to actions.

> **Bottom-Up Problem Solving**: Behaviour emerging from simple reactions to inputs.

![Reactive versus deliberative paradigms](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/reactive_vs_deliberative.svg)
*Deliberative paradigm (top): top-down, needs a closed world. Reactive paradigm (bottom): bottom-up, works in an open world.*

| Feature | Deliberative Paradigm | Reactive Paradigm |
|---|---|---|
| Problem solving | **Top-down** | **Bottom-up** |
| World assumption | Requires a **closed world** | Works in an **open world** |
| Model | **Internal models** | **Model free** |
| Decision basis | **Look ahead** (predict outcomes) | **React to inputs** |
| Organisation | **Functional pipeline** (sense $\rightarrow$ plan $\rightarrow$ act in sequence) | **Concurrent modules** (rules run in parallel) |

### Braitenberg's Vehicles

#### Definitions

> **Braitenberg Vehicle**: A simple two-wheeled vehicle with two light sensors wired directly to its two wheel motors, whose behaviour depends only on how the sensors are wired.

The question is whether these vehicles are reactive, deliberative (no learning), or deliberative (learning). They are **reactive**: each sensor drives a motor directly, with no memory, model, plan, or learning. In simulation they still produce behaviour that *looks* purposeful, such as gathering around a light source or steering around walls.

Each vehicle has two sensors at the front and two wheels at the back. More light on a sensor makes its connected wheel turn faster (the "+" connections).

![Braitenberg vehicles](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/braitenberg_vehicles.svg)
*Vehicle 2a (uncrossed wiring) turns away from the light. Vehicle 2b (crossed wiring) turns towards it. Both have the same parts; only the wiring differs.*

| Vehicle | Wiring | Rule | Result |
|---|---|---|---|
| **2a: Avoid Light** | Uncrossed (each sensor to the wheel on the same side) | IF more light to the right $\rightarrow$ right wheel turns faster | Turns towards the left, **away** from the light |
| **2b: Goto Light** | Crossed (each sensor to the wheel on the opposite side) | IF more light to the left $\rightarrow$ right wheel turns faster | Turns towards the left, **closer** to the light |

The only difference between "fear" (2a) and "attraction" (2b) is whether the wires cross.

### Reactive Sense-Act Controllers And The Roomba

#### Definitions

> **Sense-Act Controller**: A reactive controller that maps sensed input directly to action through a set of transfer rules (behaviours), with no planning step.

> **Behaviour (Ethological View)**: A direct mapping of sensory inputs to a pattern of motor actions that are then used to achieve a task.

> **Transfer Function (Mathematical View)**: A function transforming sensory inputs into actuator commands.

A sense-act controller passes the sensed input to a set of **sense-act transfer rules** (behaviours), Rule 1 to Rule $n$. Their outputs drive **Act**, which changes the environment, and the environment is sensed again.

![Sense-act controller](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/sense_act_controller.svg)
*Sense-act controller: every behaviour rule maps sensor input directly to actuator commands, with no planning step in between.*

The rules can be run in two modes:

| Mode | Meaning |
|---|---|
| **Concurrent** | All rules run in parallel on the same input; outputs are combined. |
| **Sequential** | Rules are evaluated one after another. |

**Example sense-act controller** for a mobile robot, with five behaviours between Sense and Act:

![Example sense-act controller](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/example_sense_act_controller.svg)
*Example controller with five behaviours (Identify Objects, Monitor Changes, Explore, Wander, Avoid Objects) all fed by the same sensed input.*

#### Roomba Vacuum Cleaner

The Roomba is a practical sense-act robot. Its sensors and parts include:

| Part | Purpose |
|---|---|
| Infrared sensor | Detects obstacles/signals |
| Cliff sensors | Detect drops (e.g., stairs) so it does not fall |
| Smart bumper | Detects collisions |
| Side brush | Sweeps edges and corners |
| Handle, power button, bin release | User-facing controls |

![Roomba sensors](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/roomba_sensors.svg)
*Roomba top and bottom views. The bumper, infrared and cliff sensors supply the inputs its reactive behaviours respond to.*

Its cleaning pattern is built from simple behaviours rather than a map-based plan:

1. **Spiral** outward from the start point.
2. **Wall-follow** around room edges and furniture (sofa, table).
3. **Bounce** off obstacles in new directions, producing a dense, random-looking coverage pattern over time.

![Roomba cleaning patterns](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/roomba_coverage.svg)
*Left: a spiral from the start point, then wall-following around the furniture. Right: random bouncing, which covers the floor through many straight runs.*

### AI Operating Systems And Virtual Assistants

#### Definitions

> **AI Operating System (AI OS)**: A general-purpose OS entirely powered or managed by AI. No fully autonomous AI OS currently exists.

> **AI-Enhanced Operating System**: A traditional OS (Windows, macOS, Linux, Android) with integrated AI features.

> **AI (Virtual) Assistant**: Software that performs tasks when asked in natural language.

Deliberative agent applications include AI-driven operating systems (the film *Her*, with its AI OS "Samantha", is the popular image). In reality, there are AI-enhanced OSes:

| AI-Enhanced OS | AI Integration |
|---|---|
| Windows 11 | Copilot (based on OpenAI models) for interaction and productivity |
| macOS / iOS | Siri, photo recognition, predictive typing, system optimisations |
| Android | Google Assistant, app suggestions, adaptive battery |

A search-engine answer also lists projects aiming at AI OSes: Google Fuchsia, Microsoft Azure Sphere OS, IBM Watson OS, Ubuntu AI, Tesla's AI OS, and CosmOS. These aim to optimise machine learning, automate tasks, and personalise user experiences. Treat this list with caution — it is a search-engine claim, not a list of true AI OSes.

A **true AI OS** would involve:

- Autonomous resource management (RAM, CPU, tasks).
- A conversational interface as the shell.
- AI-driven scheduling and optimisation.
- Dynamic UI personalisation.
- Integration with agents that learn and evolve.

Projects inching towards an AI-run computing environment: AutoGPT, Open Interpreter, and agentic computing platforms.

**AI (virtual) assistants** in current OSes:

| Assistant | Platform |
|---|---|
| Braina (LLMs) | Windows PC / mobile |
| Copilot | Windows 11 |
| Invisibility, Gravity (on-device AI) | macOS |
| Siri | iOS, iPadOS, watchOS, macOS, tvOS, audioOS, visionOS |
| Amazon Alexa | Fire OS 5.0+, iOS 11.0+, Android 4.4+ |

### The 2026 Agent Landscape And OSWorld

#### Definitions

> **Computer-Use Agent**: An agent that drives a graphical interface — click, type, scroll — the way a person would, for tasks with no API.

> **OSWorld**: A scalable, real operating system environment for multi-modal agents, supporting task setup, execution-based evaluation, and interaction.

> **Execution-Based Evaluation**: Judging success by checking the final state of the environment after the agent acts, rather than comparing the agent's text output.

Agent families in 2026:

| Family | What It Does | Representative Tools (September 2026) |
|---|---|---|
| Coding agents | Read, write, run, and debug code across a whole project, often unsupervised for long stretches | Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Cline, Devin |
| **Computer-use agents** | Drive a GUI (click, type, scroll) like a person, for tasks with no API | Anthropic Computer Use, OpenAI Operator, Gemini Computer Use / Project Mariner |
| Research agents | Plan multi-step search, gather and cross-check sources, synthesise a cited report ("Deep Research" modes) | Deep Research in ChatGPT, Gemini, Claude, Perplexity; Grok DeepSearch |
| General agents | Attempt arbitrary multi-step tasks across tools and the web from a single instruction | Manus (now Meta), ChatGPT Agent, Genspark, OpenManus |
| Creative agents | Drive creative software (3D, audio, design) through tool connectors | Claude's creative connectors (Adobe, Blender, Ableton, Autodesk Fusion) |

Computer-use agents are the family most relevant to OS agents.

#### OSWorld Benchmark

Key facts:

- Evaluates **open-ended computer tasks** involving arbitrary apps.
- Benchmark of **369 real-world tasks**, with reproducible set-up and evaluation scripts.
- Source: `https://osworld-v1.xlang.ai/`.

Example tasks:

- "Update the bookkeeping sheet with my recent transactions over the past few days in the provided folder" — the agent opens receipt images and enters each transaction into a LibreOffice Calc spreadsheet.
- "Could you help me tweak the code so the snake can actually eat the food?" — the agent edits Python game code in VS Code and runs it.

![OSWorld loop](../../../diagrams/CSC3044S-AI%20Systems/AIS/02_Introduction_II/osworld_loop.svg)
*OSWorld: a config sets up the VM. The agent observes screenshots and accessibility trees and acts with the mouse and keyboard, and the final environment state is checked by execution-based evaluation.*

How an OSWorld episode runs:

1. A **task instruction** is given as input to the **agent** (e.g., GPT-4V).
2. A **task initial state setup config** sets up the initial environment state in **virtual machine(s)**.
3. The environment contains an **OS** (macOS, Ubuntu, Windows), **arbitrary apps** (browser, office, VS Code, etc.), and **interfaces** (GUI and command line).
4. The agent receives an **observation**: a screenshot and/or an accessibility (a11y) tree.
5. The agent **predicts an action** as mouse and keyboard input, which is executed in the environment.
6. Steps 4-5 repeat until the task ends.
7. The environment's **final state** is retrieved ("get env state") and scored by **execution-based evaluation**.

OSWorld leaderboard (top 10, max 100 steps):

| Rank | Model (Org, Date) | Type | Success Rate |
|---|---|---|---|
| 1 | claude-fable-5 [1m] (Anthropic, Aug 2026) | General | 86.0% |
| 2 | claude-opus-5 [1m] (Anthropic, Aug 2026) | General | 83.4% |
| 3 | Muse Spark 1.1 (Meta Superintelligence Labs, Jul 2026) | General | 80.7% |
| 4 | Holo3-35B-A3B (H Company, Apr 2026) | Specialized | 80.4 $\pm$ 2.2% |
| 5 | MiniMax M3 (MiniMax, Jun 2026) | General | 75.2% |
| 6 | Qwen 3.7 Plus (Alibaba, May 2026) | General | 73.3% |
| 7 | Kimi K2.6 (Moonshot AI, Apr 2026) | General | 73.1% |
| 8 | claude-sonnet-4-6 (Anthropic, Mar 2026) | General | 72.1% |
| 9 | Kimi K2.5 (Moonshot AI, Jan 2026) | General | 63.3% |
| 10 | claude-sonnet-4-5 (Anthropic, Oct 2025) | General | 62.9% |

### Generative AI Versus AI Agents

#### Definitions

> **Generative AI**: AI that creates original content — text, images, video, audio, or software code — in response to user prompts.

> **Deep Learning (DL)**: Using very large artificial neural networks to identify and encode patterns in huge amounts of training data.

> **Statistical Inference**: Drawing conclusions about patterns from data; the underlying mechanism of DL models.

> **Maximum Likelihood (Point) Estimation**: Choosing the single parameter value that makes the observed training data most probable.

> **AI Agent (Agentic AI)**: An AI system with greater autonomy and decision-making than generative AI, typically an LLM linked with NLP, APIs, and computational tools.

> **Large Language Model (LLM)**: A very large deep learning model trained on text, used as the core of current AI agents.

**Generative AI** properties:

- Creates original content in response to prompts.
- Uses **deep learning** models that encode patterns from huge training data — this is **statistical inference**.
- Generates high-quality text, images, code, etc. based on its training data.
- Examples: Midjourney, DALL-E, Stable Diffusion. *Space Opera Theater* (2022) is a well-known generative AI artwork.

These models are, at heart, inferential statistics. Training is a form of **maximum likelihood (point) estimation**:

$$
\hat{\theta}_{\text{MLE}} = \arg\max_{\theta} \; P(\text{data} \mid \theta)
$$

**AI agents** (agentic AI) properties:

- **Greater autonomy and decision making** than generative AI.
- Current agents use **LLMs linked with NLP, APIs, and computational tools**.
- **Autonomy** (unlike GenAI systems): the autonomy lies in *how* the agent solves the given problem (user prompt).
- **Adaptation**: e.g., reinforcement learning via user feedback, real-time fine-tuning given new training data.

| Aspect | Generative AI | AI Agent |
|---|---|---|
| Main output | Content (text, images, code, audio, video) | Actions and decisions towards a goal |
| Autonomy | Responds to the prompt; no independent problem-solving strategy | Decides how to solve the problem |
| Core technology | Deep learning models (statistical inference) | LLMs + NLP + APIs + computational tools |
| Adaptation | Fixed after training | Adapts (RL from user feedback, real-time fine-tuning) |

### AI Agents Versus AI Assistants

#### Definitions

> **Persistent Memory**: The ability to recall past interactions (previous actions, conversations) to improve future responses.

> **Harness**: The integration of external applications and tools that lets an agent act on real-time data rather than relying only on its initial training (and re-training).

> **AI Assistant**: An AI system limited to predefined functions, which requires prompts and has no persistent memory.

**AI agents: key features**

| Feature | Meaning |
|---|---|
| Persistent memory | Recall past interactions to improve future responses |
| Learning | Adjust behaviour given user feedback |
| Integrate external apps/tools (**harness**) | Act on real-time data rather than only initial training |
| $N$ interactions | Work on many sub-tasks to complete a user-defined task |

**AI assistants: key features**

- **Require prompts**: limited to predefined functions. An assistant can use a spreadsheet to make a table comparing "x versus y", but cannot independently decide to do that comparison without a specific prompt.
- **No persistent memory**: they do not retain information from past interactions and do not learn over time. They improve only when developers release updated versions.

| Aspect | AI Assistant | AI Agent |
|---|---|---|
| Initiative | Needs a specific prompt for each function | Decides sub-tasks itself |
| Functions | Predefined | Open-ended via tools/harness |
| Memory | None between interactions | Persistent |
| Learning | Only through new developer releases | Learns from user feedback |
| Task length | Single request-response | $N$ interactions over many sub-tasks |

Products in this space include Claude 4.5, ChatGPT-5, Perplexity, Grok 4, Gemini 3, DeepSeek V3.1, Microsoft 365 Copilot, Amazon Echo (Alexa), IBM watsonx, and Siri. Where each falls depends on the features above, not on the brand.

### Classifying Systems: Booking Assistant And Autonomous Vehicle

#### Personal Booking Assistant

This example (courtesy of Osamah Atif, Etera, 2025) shows **generative AI generating an assistant**.

1. A generative model (GPT-5.2) is given a long system prompt defining:
   - **Role & goal**: "You are 'Mark', a friendly and professional personal assistant. Your sole objective is to place an outbound phone call to a restaurant to successfully book a reservation on behalf of a client, Osamah."
   - **Persona & tone**: friendly and natural (warm, polite, conversational); concise; pacing — pauses between sentences using an ellipsis, e.g., "I'd like to make a reservation for two people... would 7 PM be possible?"
   - **Core instructions & conversation flow**: starting with the initial response, and so on.
2. **Output**: an automated assistant that phones restaurants to make bookings.
3. The assistant calls various restaurants in a city looking for a reservation for $N$ people with specific seating and dietary requirements (preferences).
4. The **prompt to the assistant** gives: reservation time, number of people, and dietary requirements (preferences).

The resulting system is an **assistant**: it does one predefined function and needs a prompt with the booking details each time.

#### Autonomous Vehicle

Scenario: an autonomous vehicle picks up and drops off customers in a city, given the highest-value ride requests on a mobile app. Is it an AI agent or generative AI? It has two parts:

| Component | Classification | Reason |
|---|---|---|
| **Autonomous vehicle** | Complex **AI agent** | Maps multi-modal sensory inputs (traffic, obstacles, weather, lighting conditions, ...) to motor outputs (a safe trip from pick-up to drop-off) |
| **Autonomous vehicle app** | More like an **AI assistant** (but could have been AI-generated) | Has very limited functionality |

Reading: Russell & Norvig (2021), *Artificial Intelligence: A Modern Approach*, 4th ed., Ch. 2 (Intelligent Agents); Poole & Mackworth (2023), *Artificial Intelligence: Foundations of Computational Agents*, 3rd ed., Ch. 1 (Artificial Intelligence and Agents).
