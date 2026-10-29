---
tags:
  - automated-planning
---

# Monte Carlo Tree Search

**Subject**: CSC3041F Automated Planning  
**Source**: `Lecture 10.pdf`, Zola Mahlaza, slides 1-35  
**Generated**: 2026-05-31

---

## Contents

- [[#Core Content|Core Content]]
  - [[#Limits Of Alpha-Beta|Limits Of Alpha-Beta]]
  - [[#Pure Monte Carlo Search|Pure Monte Carlo Search]]
  - [[#Playout Policies|Playout Policies]]
  - [[#Exploration And Exploitation|Exploration And Exploitation]]
  - [[#The Four MCTS Phases|The Four MCTS Phases]]
  - [[#MCTS Example Structure|MCTS Example Structure]]
  - [[#Strengths Of MCTS|Strengths Of MCTS]]

---

## Core Content

### Limits Of Alpha-Beta

#### Definitions

> **Monte Carlo Tree Search (MCTS)**: A search algorithm that estimates action values by repeated simulated play and selectively grows a search tree. *In plain language: try many possible futures, learn which moves tend to survive, and focus search there.*

> **Simulation / Playout**: A complete simulated game from a state to a terminal outcome. *In plain language: play the game out, possibly using a simple policy, to see what happens.*

Alpha-beta pruning struggles in games with enormous branching factors and weak static evaluation functions. The lecture uses Go as motivation: the branching factor begins very high, and material-style evaluation is not reliable because positions remain fluid until the endgame.

MCTS replaces heavy handcrafted evaluation with simulations:

$$
\widehat{V}(s)=\frac{\text{total utility from simulations starting at }s}{\text{number of simulations from }s}
$$

For binary win/loss games, the estimated value can be interpreted as a win percentage.
### Pure Monte Carlo Search

#### Definitions

> **Pure Monte Carlo Search**: A flat search method that runs `N` simulations from the current state for each candidate move and chooses the move with the best estimated outcome. *In plain language: test each immediate move by rollouts, but do not maintain a deep search tree.*

Pure Monte Carlo search:

1. Start at the current game state.
2. For each available action, run simulations.
3. Estimate the action value from simulation outcomes.
4. Choose the action with the highest estimated value.

It differs from MCTS because it does not need to keep a growing tree. It is flatter and less structured.

#### Diagram: Pure Monte Carlo flat search

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["Pure Monte Carlo flat search"]
    N1["Root expands immediate<br/>actions, each labeled with<br/>estimated values su"]
    T --> N1
    N2["No deep tree needs to be<br/>stored."]
    N1 --> N2

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
```

Caption: Pure Monte Carlo evaluates immediate moves by simulations without structured tree growth.


### Playout Policies

#### Definitions

> **Playout Policy**: The policy used to choose moves during simulations. *In plain language: the rule for how simulated players act.*

> **Self-Play**: Training or evaluation where agents play against copies of themselves. *In plain language: the system generates experience by playing itself.*

In simple games, playout actions may be random. In harder games, random play can be too noisy, so playout policies may use:

1. Simple game-specific heuristics.
2. Self-play generated data.
3. Learned models from game histories.

The lecture describes an unintelligent agent playing itself, assigning scores to positions from game histories, and using that data to improve the model.
### Exploration And Exploitation

#### Definitions

> **Exploitation**: Choosing actions that currently look best. *In plain language: use what you already believe is good.*

> **Exploration**: Trying less-tested actions to learn whether they may be better. *In plain language: test uncertain options instead of always choosing the current favorite.*

> **Upper Confidence Bound (UCB)**: A selection rule balancing average reward with an exploration bonus. *In plain language: prefer moves that are good or not yet tested enough.*

A greedy strategy is pure exploitation. If $C=0$, selection ignores exploration and chooses the currently best estimated move. MCTS needs a selection policy that balances:

1. High average utility.
2. Sufficient exploration of less-visited nodes.

A standard UCB-style score is:

$$
\mathrm{score}(n)=\frac{U(n)}{N(n)}+C\sqrt{\frac{\ln N(\mathrm{parent}(n))}{N(n)}}
$$

where:

| Symbol | Meaning |
|---|---|
| $U(n)$ | Total utility from simulations passing through node $n$ |
| $N(n)$ | Number of simulations/visits at node $n$ |
| $N(\mathrm{parent})$ | Visits to the parent node |
| $C$ | Exploration constant greater than zero |

The lecture notes $C=0$ as greedy and mentions a theoretical value around $1.41$ for balancing exploration and exploitation.
### The Four MCTS Phases

#### Definitions

> **Selection**: Starting at the root and following the selection policy to a promising node. *In plain language: walk down the current tree using the UCB-style score.*

> **Expansion**: Adding a new child node to the tree. *In plain language: grow the tree by one unexplored move.*

> **Simulation**: Running a playout from the new node to an outcome. *In plain language: play the game out from there.*

> **Back-Propagation**: Updating statistics on the path from the simulated node back to the root. *In plain language: send the simulation result back up the tree.*

MCTS repeats these phases until a time limit or iteration limit is reached:

```text
while time remains:
    leaf = SELECT(root)
    child = EXPAND(leaf)
    result = SIMULATE(child)
    BACKPROPAGATE(child, result)
return best root action
```

The returned action is usually the root child with the best visit/value statistic.

#### Diagram: MCTS four-phase loop

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart LR
    N0["Selection"]
    N1["Expansion"]
    N2["Simulation"]
    N3["Back-propagation, repeated<br/>until time or iteration limit"]
    N0 --> N1
    N1 --> N2
    N2 --> N3

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
```

Caption: This is the complete control flow of MCTS.



#### Diagram: Back-propagation path

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["Back-propagation path"]
    N1["Simulation result from a leaf<br/>updates the leaf, its parent,"]
    T --> N1

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
    class N1 outcome;
```

Caption: Back-propagation lets one playout affect future selection at every level it passed through.


### MCTS Example Structure

In the lecture example:

1. $C=0$, so selection is greedy.
2. Each simulation batch has $10$ simulations.
3. Node labels use $utility/number\_of\_simulations$, such as $8/10$.
4. After a child is simulated, its result is back-propagated to ancestors.

If a root child has $8/10$, another has $6/10$, and another has $4/10$, greedy selection chooses the $8/10$ child. Later simulations may reveal that a deeper branch changes the average, and back-propagation updates the root statistics.

#### Diagram: MCTS node labels

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["MCTS node labels"]
    N1["Nodes are labeled with<br/>utility-over-visit-count<br/>statistics."]
    T --> N1

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
```

Caption: MCTS decisions are based on accumulated statistics, not exact minimax values.


### Strengths Of MCTS

The lecture emphasizes:

| Strength | Explanation |
|---|---|
| Handles massive state spaces | It samples futures instead of enumerating all leaves |
| Heuristic-free in principle | It can use simulations instead of handcrafted EVAL |
| Variable-depth exploration | Different parts of the tree can be explored to different depths |
| Anytime behavior | Can return an action after a time or iteration limit |
