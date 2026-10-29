---
tags:
  - automated-planning
---

# A* Memory Usage And Beam Search

**Subject**: CSC3041F Automated Planning  
**Source**: `Lecture 5.pdf`, Zola Mahlaza, slides 1-18  
**Generated**: 2026-05-31

---

## Contents

- [[#Core Content|Core Content]]
  - [[#A* Space Complexity|A* Space Complexity]]
  - [[#Reference Counts|Reference Counts]]
  - [[#Beam Search|Beam Search]]
  - [[#Delta-Beam Search|Delta-Beam Search]]

---

## Core Content

### A* Space Complexity

#### Definitions

> **A* Search**: Informed search using $f(n)=g(n)+h(n)$. *In plain language: expand the node with the lowest estimated total path cost.*

> **Openlist / Frontier**: Nodes generated but not expanded. *In plain language: candidates waiting for exploration.*

> **Closed List / Reached List**: Expanded or reached nodes stored to avoid cycles and redundant work. *In plain language: memory of states already handled.*

A* is complete and optimal on finite search spaces when the heuristic is admissible and consistent. Its limitation is memory:

$$
\text{Space complexity}=O(b^d)
$$

where $b$ is branching factor and $d$ is depth of the goal. A* stores:

1. The openlist/frontier.
2. The closed/reached list.

Both can grow very large.

#### Diagram: A* memory sources

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["A* memory sources"]
    N1["Two boxes labeled Openlist and<br/>Closed List."]
    T --> N1
    N2["Openlist holds frontier nodes"]
    N1 --> N2
    N3["Closed List holds<br/>expanded/reached nodes."]
    N2 --> N3

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
```

Caption: A* memory grows because it stores both future candidates and past states.


### Reference Counts

#### Definitions

> **Reference Count**: A count of how many future references to a node are still needed. *In plain language: a bookkeeping number that tells when a stored node can be safely removed.*

The lecture presents reference counts as a memory-saving idea. If a node is stored in the closed list only so future paths can refer to it, it can be permanently removed once its reference count reaches zero.

Step-by-step idea:

1. Store expanded nodes in the closed list to avoid cycles and redundant work.
2. Attach a reference count to each stored node.
3. Decrement the count when a dependent branch no longer needs that node.
4. Delete the node once the count reaches zero.

This can reduce memory pressure but adds bookkeeping overhead.
### Beam Search

#### Definitions

> **Beam Search**: Search that sorts candidates by score and retains only a fixed number $k$. *In plain language: keep only the best-looking candidates and discard the rest.*

> **Beam Width ($k$)**: The number of nodes kept after pruning. *In plain language: the size of the shortlist.*

Beam search is introduced as a direct response to A* memory usage:

```text
1. Sort by f.
2. Select only the top k elements.
```

In the grid example, the agent moves from $(0,0)$ to $(3,3)$ with actions $\{\mathrm{Up},\mathrm{Down},\mathrm{Left},\mathrm{Right}\}$ and Manhattan distance as heuristic. With $k=2$, only the two best candidates survive at each step.

Beam search can be much cheaper in memory:

$$
\text{Space}=O(km)
$$

where $m$ is maximum depth. But it is not complete and not optimal.

#### Diagram: Beam search grid

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["Beam search grid"]
    N1["Grid from start to goal."]
    T --> N1
    N2["Each generated coordinate is<br/>labeled with Manhattan<br/>distance."]
    N1 --> N2
    N3["At each layer, only the two<br/>best coordinates remain in the<br/>openlist."]
    N2 --> N3

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
    class N1 outcome;
```

Caption: The diagram shows how beam search prunes candidates even when they are legal paths.



#### Diagram: Duplicate handling in beam example

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["Duplicate handling in beam<br/>example"]
    N1["The middle diagonal state can<br/>be reached from both adjacent"]
    T --> N1

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
```

Caption: Even memory-limited search still needs a policy for duplicate states.



#### Diagram: Traditional beam versus delta beam

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart LR
    N0["Traditional: sorted list"]
    N1["first fixed-width group kept"]
    N0 --> N1

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
```

Caption: Delta beam trades fixed memory for more adaptive pruning.


### Delta-Beam Search

#### Definitions

> **Delta-Beam Search**: Beam search that keeps all nodes within a chosen score distance of the best node. *In plain language: keep every candidate close enough to the current best, rather than a fixed number.*

> **Delta Threshold**: The maximum allowed score gap from the best candidate. *In plain language: how far behind the best a node may be and still survive.*

Traditional beam search keeps exactly $k$ nodes. Delta-beam search keeps every node whose score is within a threshold of the best score:

$$
\text{keep }n\text{ if }f(n)\le f(n_{\mathrm{best}})+\delta
$$

Comparison:

| Method | Keeps | Memory Behavior | Risk |
|---|---|---|---|
| Traditional beam | Best $k$ nodes | Predictable | May discard useful alternatives |
| Delta beam | Nodes close to best score | Variable | May exceed memory limits |

Delta beam is more robust because it does not force arbitrary pruning when many nodes are similarly good, but memory use is less predictable.
