---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "01 — Introduction I: Agents, Rationality, and Computational Complexity"
---

# 01 — Introduction I: Agents, Rationality, and Computational Complexity

**Source note:** [Introduction I: Agents, Rationality, and Computational Complexity](../01_Introduction_I.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#Course organization and assessment|Course organization and assessment]]
  - [[#AI traditions and disciplinary roots|AI traditions and disciplinary roots]]
  - [[#Agents and four views of intelligence|Agents and four views of intelligence]]
  - [[#Rationality, utility, and learning|Rationality, utility, and learning]]
  - [[#Intractable problems: packing, SAT, TSP, and VRP|Intractable problems: packing, SAT, TSP, and VRP]]
  - [[#Vehicle-routing project|Vehicle-routing project]]

## Core Content

### Course organization and assessment

<!-- qard-id: ais-c3438bfe89824039aa26 -->
> [!qard]- What are the three sections of the AI Systems course?
> Agents and agent architectures; AI systems design; and human-centered AI systems and societal impacts.

<!-- qard-id: ais-1d980092b41ee176822c -->
> [!qard]- What assessment weights and DP requirement are recorded in the lecture?
> Project $25\%$, test $25\%$, exam $50\%$; DP requires a $45\%$ aggregate in practical work. These are lecture-recorded arrangements.

<!-- qard-id: ais-0207081b83a3d369d764 -->
> [!qard]- Which introductory book chapters are assigned in the notes?
> Russell and Norvig, Artificial Intelligence: A Modern Approach, fourth edition, Chapter 2; Poole and Mackworth, Artificial Intelligence: Foundations of Computational Agents, third edition, Chapter 1.

### AI traditions and disciplinary roots

<!-- qard-id: ais-46d01889ced6eb74ce9e -->
> [!qard]- What is artificial intelligence?
> Study and construction of systems exhibiting intelligent behavior, including perception, reasoning, learning, and action.

<!-- qard-id: ais-0b33c2b415c8cae85ec2 -->
> [!qard]- What is symbolic AI?
> A top-down approach using explicit symbols, logic, and rules.

<!-- qard-id: ais-489715b9b0140ec32190 -->
> [!qard]- What is neural or connectionist AI?
> A bottom-up approach using networks of connected computational units and learned representations.

<!-- qard-id: ais-4d12e07596ec0af2eab7 -->
> [!qard]- Which disciplines contribute to AI?
> Computer science, psychology, philosophy, statistics, neuroscience, and machine learning; these overlap rather than forming strict categories.

<!-- qard-id: ais-9d75694fc06ee32f224b -->
> [!qard]- How do symbolic and neural AI differ in representation and construction?
> Symbolic AI explicitly specifies facts, rules, and search states. Neural AI specifies architecture, data, and training to learn weights and representations.

<!-- qard-id: ais-d43d80eea9c10fd57fbc -->
> [!qard]- What typical difficulties distinguish symbolic and neural AI?
> Symbolic systems face representation and search complexity; neural systems face data quality, generalization, and interpretability challenges.

<!-- qard-id: ais-c8d346f7711ec77095e6 -->
> [!qard]- Which disciplinary connections are associated with Bayes’ rule, game theory, and SGD?
> Bayes’ rule: probability. Game theory: mathematics/economics. Stochastic gradient descent: statistics/optimization.

<!-- qard-id: ais-46eb552bbc45bd9b0c5d -->
> [!qard]- Which disciplinary connections are associated with value iteration, TD learning, and ANNs?
> Value iteration: control theory. Temporal-difference learning: psychology. Artificial neural networks: neuroscience.

<!-- qard-id: ais-c6c0989df8b34b55101f -->
> [!qard]- Can one agent combine symbolic and neural methods?
> Yes. Modern agents can combine symbolic reasoning, neural learning, optimization, probabilistic inference, and game theory.

### Agents and four views of intelligence

<!-- qard-id: ais-60591513f2b027c2d745 -->
> [!qard]- What is an agent?
> An entity that perceives its environment and acts on it.

<!-- qard-id: ais-08e92b1045e34376bef9 -->
> [!qard]- What are a percept and a sensor?
> A percept is information received through sensing at a particular time; a sensor is the mechanism receiving that information.

<!-- qard-id: ais-4d02b15799db03c1784e -->
> [!qard]- What is an actuator?
> A mechanism through which an agent performs actions on its environment.

<!-- qard-id: ais-1810a4006741ba418363 -->
> [!qard]- What are state and action space?
> State describes a situation relevant to decision-making; action space is the set of available actions.

<!-- qard-id: ais-6c586ec7b2a4d22b697d -->
> [!qard]- What is the agent perception-action feedback loop?
> Sensors obtain observations, a decision procedure selects actions, actuators execute them, and changed environmental conditions produce new observations.

<!-- qard-id: ais-23c35a5ce0dbe9311e84 -->
> [!qard]- What determines an agent’s decision procedure?
> Percepts, available state information, the environment, and the action space.

<!-- qard-id: ais-f1c7f432956615a4aaf2 -->
> [!qard]- What does “think humanly” evaluate?
> Whether the internal process resembles human cognition, using cognitive-science or neuroscience ideas.

<!-- qard-id: ais-ac83d2a0af1cab604205 -->
> [!qard]- What does “think rationally” evaluate?
> Whether reasoning follows valid logical rules, as in logic and automated inference.

<!-- qard-id: ais-de6b6d40388afe34508a -->
> [!qard]- What does “act humanly” evaluate?
> Whether outward behavior resembles human behavior, as in Turing-test-style evaluation and ELIZA.

<!-- qard-id: ais-a45428562411c0e8133e -->
> [!qard]- What does “act rationally” evaluate?
> Whether decisions serve the objective well, as in the intelligent-agent framework.

<!-- qard-id: ais-9ad20113608d5f12397f -->
> [!qard]- Why should human-like behavior and rationality be assessed separately?
> Human-like answers need not be rational, and rational decisions need not arise from human-like thought.

<!-- qard-id: ais-dc887f90e2fe7a4b73ae -->
> [!qard]- What historical progression of agent families is outlined?
> Symbolic reasoning from the 1950s, reactive agents from the 1980s, hybrid agents from the 1990s, and neural/cognitive agents from the 2000s in the course overview.

### Rationality, utility, and learning

<!-- qard-id: ais-96bbfd12c3eddf503a13 -->
> [!qard]- What is utility?
> A numerical measure of outcome desirability according to the agent’s goals.

<!-- qard-id: ais-8a10aa0bdfdb1a509f5d -->
> [!qard]- What is a rational agent?
> An agent selecting actions expected to maximize performance given its information and available actions.

<!-- qard-id: ais-cd497d67e615148569ce -->
> [!qard]- What factors does rationality depend on?
> Performance metric, environmental knowledge, available actions, and sensory information.

<!-- qard-id: ais-c8c73471be1ba72d0e39 -->
> [!qard]- What is expected utility?
> Utility averaged over possible outcomes, weighted by their probabilities.

<!-- qard-id: ais-d58b7413573a0815b89d -->
> [!qard]- What expected-utility action-selection formula is given?
> $a^*=\arg\max_{a\in A}\sum_oP(o\mid a,h)U(o)$, with actions $A$, outcomes $o$, available information $h$, and utility $U$.

<!-- qard-id: ais-ab0ff11772a58c3935d2 -->
> [!qard]- Can a rational decision have an unsuccessful outcome?
> Yes. Rationality is judged using available information; uncertainty can produce unlucky outcomes, while poor decisions can succeed by chance.

<!-- qard-id: ais-6be973fd23607d0d3f26 -->
> [!qard]- What can lead an agent to low-utility behavior?
> Limited information, inadequate computation, noisy inputs, or inappropriate training data.

<!-- qard-id: ais-7cd9f5d4ba83b35dc0ab -->
> [!qard]- What is reinforcement learning?
> Learning behavior through interaction with an environment and reward feedback.

<!-- qard-id: ais-ee15222038ade0c9ccde -->
> [!qard]- What is a hallucination?
> A false or unsupported generated claim that can appear plausible; fluency alone is an inadequate performance measure.

<!-- qard-id: ais-43732c10a019c832c1fe -->
> [!qard]- How do simple reflex, model-based reflex, and deliberative agents differ?
> Simple reflex uses current input; model-based reflex also retains internal state; deliberative control considers goals and future actions.

<!-- qard-id: ais-628041e9c6f9cc0a6ac4 -->
> [!qard]- Is learning a mutually exclusive alternative to reactive or deliberative control?
> No. Learning can improve either control style.

<!-- qard-id: ais-bde1a3833696d9f355e1 -->
> [!qard]- Which modern agent application families are listed?
> Coding, computer use, research, general tasks across tools/web, and creative-software workflows.

<!-- qard-id: ais-31a105742a44ca9af106 -->
> [!qard]- What kinds of tasks distinguish those application families?
> Coding edits/runs/debugs projects; computer use operates interfaces; research searches and synthesizes sources; general agents use tools across tasks; creative agents operate creative applications.

<!-- qard-id: ais-81610cb791c592372583 -->
> [!qard]- Do named products establish rationality or a current performance ranking?
> No. They illustrate application families in the lecture snapshot; rationality must be evaluated against information and objectives.

### Intractable problems: packing, SAT, TSP, and VRP

<!-- qard-id: ais-19b89e4a7a728b81b97d -->
> [!qard]- What is a decision problem?
> A problem whose answer is yes or no.

<!-- qard-id: ais-5c6de26cc3acf75fd619 -->
> [!qard]- What is polynomial time?
> Runtime bounded by a polynomial in input size.

<!-- qard-id: ais-c8390fe1eec3d1b1ff54 -->
> [!qard]- What is the class P?
> Decision problems solvable in polynomial time.

<!-- qard-id: ais-83e2a5a5043c8cb2abdc -->
> [!qard]- What is the class NP?
> Decision problems whose yes answers have certificates verifiable in polynomial time.

<!-- qard-id: ais-2438d415af296e5891f5 -->
> [!qard]- What is a polynomial-time reduction?
> A polynomial-time transformation between problems preserving their answers.

<!-- qard-id: ais-2fa33521dbf8d25ffb4d -->
> [!qard]- What does NP-hard mean?
> At least as hard as every problem in NP under polynomial-time reductions.

<!-- qard-id: ais-703e087aad16ad037190 -->
> [!qard]- What does NP-complete mean?
> A decision problem that is both in NP and NP-hard.

<!-- qard-id: ais-1253ba3ec29e4e05f071 -->
> [!qard]- How are P, NP, NP-hard, and NP-complete related?
> $\mathrm P\subseteq\mathrm{NP}$ and $\mathrm{NP\text{-}complete}=\mathrm{NP}\cap\mathrm{NP\text{-}hard}$. Whether $\mathrm P=\mathrm{NP}$ is unresolved.

<!-- qard-id: ais-b61574b47c035cec31fa -->
> [!qard]- Why is “NP” not shorthand for non-polynomial?
> It describes efficiently verifiable yes certificates; it does not assert that polynomial-time solution algorithms are impossible.

<!-- qard-id: ais-517ef9bfa76b440634be -->
> [!qard]- Why is “no efficient algorithm is known” insufficient to establish NP-hardness?
> NP-hardness requires a reduction-based hardness relationship, not merely absence of a known efficient algorithm.

<!-- qard-id: ais-084f7d4a2cce8ad8f524 -->
> [!qard]- What is an optimization problem?
> Find the best feasible solution according to an objective, such as $x^*=\arg\min_{x\in S}c(x)$.

<!-- qard-id: ais-e9939569f7392475e797 -->
> [!qard]- What is bin packing, and how can a proposed bounded solution be checked?
> Pack items into as few fixed-capacity bins as possible; verify each item appears once, capacities hold, and the bin count meets the bound.

<!-- qard-id: ais-497b2a2dabce29463827 -->
> [!qard]- What is SAT, and how is a proposed solution checked?
> Find a truth assignment satisfying a Boolean formula; substitute values and evaluate the formula.

<!-- qard-id: ais-e2c96afd6e1637cfe3e5 -->
> [!qard]- What is TSP, and what can a proposed tour certify?
> Find a minimum-length tour visiting each city and returning; a certificate can show valid coverage and length at most a bound, not global optimality.

<!-- qard-id: ais-66e46818fce085579923 -->
> [!qard]- What is VRP, and what constraints must a proposed solution satisfy?
> Find vehicle routes serving customers; check customer coverage, route constraints, and the objective value.

<!-- qard-id: ais-9f3ed1962e0d4c9cf3f7 -->
> [!qard]- How do standard optimization and decision versions of TSP and bin packing differ in complexity classification?
> Optimization versions are NP-hard; corresponding standard decision versions are NP-complete.

<!-- qard-id: ais-d5a3a24c009e92434083 -->
> [!qard]- Why does factorial exhaustive search not prove every solution algorithm is exponential?
> It shows that enumeration is costly; it is not a lower-bound proof for all possible algorithms.

<!-- qard-id: ais-2e4215003418673a0c2b -->
> [!qard]- Why does removing duplicate TSP orderings not eliminate factorial growth?
> Fixing the start and identifying reversed symmetric tours reduces duplicates but still leaves factorially many candidates.

<!-- qard-id: ais-a2beabfdef91a8c26fda -->
> [!qard]- How does dynamic routing differ from a fixed known-customer problem?
> New customers can arrive after initial routes are planned, requiring revision under changing information.

<!-- qard-id: ais-0a1577874f311ec661d1 -->
> [!qard]- Do heuristics, learning, and resource-bounded search remove worst-case hardness?
> No. They may find useful solutions without guaranteeing global optimality or changing worst-case complexity.

### Vehicle-routing project

<!-- qard-id: ais-db77dd11a90ec566d15b -->
> [!qard]- What is the VRP project’s implementation and evaluation setup?
> Build an optimizer module for a VRP framework; develop on ten known maps and average evaluation performance over ten unknown maps.

<!-- qard-id: ais-1ed51b86cf248c326ce0 -->
> [!qard]- Why evaluate a routing optimizer on unknown maps?
> To test generalization beyond known development instances and customer patterns.

<!-- qard-id: ais-5fec256cd186bbae48a6 -->
> [!qard]- What project-component weights are recorded?
> Weekly commits $5\%$, final performance $25\%$, presentation $30\%$, and session/prompt history $40\%$.

<!-- qard-id: ais-09e9817d950a6f8378e1 -->
> [!qard]- Why check a framework’s score direction before applying a performance ratio?
> A higher performance score may be better while a raw route cost is better when lower; confusing these reverses interpretation.
