# Value Functions

**Subject**: CSC3041F Automated Planning  
**Source**: `RL/3RL_3041F_Edit.pdf`, Asad Jeewa, slides 1-17  
**Generated**: 2026-05-31

---

## Core Content

### Return

#### Definitions

> **Return ($G_t$)**: The cumulative discounted reward from time `t` onward. *In plain language: the total future reward the agent cares about.*

> **Horizon (`H`)**: The number of future steps included in the return. *In plain language: how far forward the sum goes.*

The return is:

$$
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots
$$

$$
G_t=\sum_{k=0}^{H}\gamma^k R_{t+k+1}
$$

The farther in the future a reward is, the less it matters when $\gamma<1$.
### Policy

#### Definitions

> **Policy ($\pi$)**: The agent's behavior rule mapping states to actions or probabilities over actions. *In plain language: the strategy the agent follows.*

> **Optimal Policy**: A policy that maximizes expected discounted return. *In plain language: the best strategy under the objective.*

Policy notation:

$$
a=\pi(s)
$$

$$
\pi(a\mid s)=P(A_t=a\mid S_t=s)
$$

$$
\sum_{a\in A}\pi(a\mid s)=1\quad\forall s\in S
$$

The RL objective:

$$
J(\pi)=\mathbb{E}_{\pi}[G_0]
$$
### State-Value Functions

#### Definitions

> **State-Value Function ($V_{\pi}(s)$)**: Expected return starting in state $s$ and following policy $\pi$. *In plain language: how good it is to be in state $s$ if you keep following this policy.*

For stochastic policies and stochastic environments:

$$
V_{\pi}(s)=\mathbb{E}_{a\sim\pi(\cdot\mid s),\,s'\sim P(\cdot\mid s,a)}\!\left[R(s,a)+\gamma V_{\pi}(s')\right]
$$

For a deterministic policy and deterministic environment:

$$
V_{\pi}(s)=R(s,\pi(s))+\gamma V_{\pi}(s')
$$

The value function is not automatically bounded between $0$ and $1$; its range depends on reward scale and discount factor.
### Bellman Equation

#### Definitions

> **Bellman Equation**: A recursive equation defining value as immediate reward plus discounted future value. *In plain language: today's value equals reward now plus the value of what comes next.*

Derivation:

$$
V_{\pi}(s)=\mathbb{E}_{\pi}[G_t\mid S_t=s]
$$

$$
G_t=R_{t+1}+\gamma G_{t+1}
$$

$$
V_{\pi}(s)=\mathbb{E}_{\pi}[R_{t+1}+\gamma G_{t+1}\mid S_t=s]
$$

$$
V_{\pi}(s)=\mathbb{E}_{\pi}[R(s,a)+\gamma V_{\pi}(s')]
$$

Short version:

$$
\text{current value}=\text{immediate reward}+\gamma\cdot\text{future value}
$$

#### Diagram: Bellman equation

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["Bellman equation"]
    N1["Current state points to<br/>action, reward, next state,<br/>and next state va"]
    T --> N1

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
```

Caption: The diagram shows that value is recursive: immediate reward plus discounted value of what follows.


### Action-Value Functions

#### Definitions

> **Action-Value Function ($Q_{\pi}(s,a)$)**: Expected return after taking action $a$ in state $s$, then following policy $\pi$. *In plain language: how good this specific action is from this state.*

For stochastic dynamics:

$$
Q_{\pi}(s,a)=\mathbb{E}_{s'\sim P(\cdot\mid s,a)}\!\left[R(s,a)+\gamma\mathbb{E}_{a'\sim\pi(\cdot\mid s')}Q_{\pi}(s',a')\right]
$$

For deterministic dynamics and policy:

$$
Q_{\pi}(s,a)=R(s,a)+\gamma Q_{\pi}(s',a')
$$

$Q$ is useful when you need to compare actions directly.
### Relationship Between V And Q

The value of a state is the policy-weighted average of its action values:

$$
V_{\pi}(s)=\mathbb{E}_{a\sim\pi}[Q_{\pi}(s,a)]
$$

$$
V_{\pi}(s)=\sum_a \pi(a\mid s)Q_{\pi}(s,a)
$$

The action value can be written using the next state's value:

$$
Q_{\pi}(s,a)=\mathbb{E}_{s'\sim P}\!\left[R(s,a,s')+\gamma V_{\pi}(s')\right]
$$

Use $V$ when evaluating states. Use $Q$ when choosing or improving actions.

#### Diagram: V versus Q

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["V versus Q"]
    N1["$V(s)$ sits at a state.<br/>$Q(s,a)$ sits on an action<br/>edge leaving that"]
    T --> N1

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
```

Caption: `V` values states; `Q` values state-action choices.



#### Diagram: Gridworld values

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
flowchart TD
    T["Gridworld values"]
    N1["Grid cells contain values"]
    T --> N1
    N2["actions from a cell have<br/>action values based on rewards"]
    N1 --> N2

    classDef default fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a;
    classDef focus fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0f172a;
    classDef outcome fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#052e16;
    classDef warning fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef muted fill:#f1f5f9,stroke:#94a3b8,stroke-width:1px,color:#334155;
    class T focus;
```

Caption: Gridworld shows how values propagate backward from rewarding or terminal states.

## Worked Examples

### Example 1: Bellman Return Split

**Problem**: Show why $G_t=R_{t+1}+\gamma G_{t+1}$.

**Step 1: Expand $G_t$**  
$G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots$

**Step 2: Expand $G_{t+1}$**  
$G_{t+1}=R_{t+2}+\gamma R_{t+3}+\cdots$

**Step 3: Substitute**  
$\gamma G_{t+1}=\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots$

**Answer**: $G_t=R_{t+1}+\gamma G_{t+1}$.

### Example 2: Gridworld Q And V Calculation

**Problem**: Given $\gamma=0.9$, at state $(3,3)$:

$$
\pi(\mathrm{Right}\mid(3,3))=0.8,\quad \pi(\mathrm{Down}\mid(3,3))=0.2,\quad \pi(\mathrm{Left}\mid(3,3))=0
$$

$$
Q((3,3),\mathrm{Right})=0.999,\quad Q((3,3),\mathrm{Down})=-0.001,\quad Q((3,3),\mathrm{Left})=-0.001
$$

**Step 1: Use the V-Q relationship**  
$V_{\pi}(s)=\sum_a\pi(a\mid s)Q_{\pi}(s,a)$.

**Step 2: Substitute**  
$V_{\pi}(3,3)=0.8(0.999)+0.2(-0.001)+0(-0.001)$.

**Step 3: Compute**  
$0.8\cdot0.999=0.7992$; $0.2(-0.001)=-0.0002$.

**Answer**: $V_{\pi}(3,3)=0.799$.

---

## Common Mistakes / Gotchas

- Confusing reward with return. Reward is one feedback signal; return is a discounted sum.
- Forgetting that rewards are indexed after actions: $R_{t+1}$ follows action at time $t$.
- Treating $V$ and $Q$ as interchangeable. $V$ scores states; $Q$ scores state-action pairs.
- Assuming values are probabilities. They depend on reward scale.
- Forgetting to weight action values by policy probabilities when computing $V$.
- Using Bellman equations without specifying the policy being evaluated.

---

## Summary / Cheat Sheet

| Term | Meaning |
|---|---|
| Return $G_t$ | Discounted future reward |
| Policy $\pi$ | Behavior rule |
| $V_{\pi}(s)$ | Expected return from state `s` under $\pi$ |
| $Q_{\pi}(s,a)$ | Expected return after action `a` in state `s`, then $\pi$ |
| Bellman equation | Recursive value definition |

**Key Formulas**:

$$
G_t=\sum_{k=0}^{H}\gamma^k R_{t+k+1}
$$

$$
V_{\pi}(s)=\mathbb{E}[R(s,a)+\gamma V_{\pi}(s')]
$$

$$
Q_{\pi}(s,a)=\mathbb{E}[R(s,a)+\gamma\mathbb{E}_{a'\sim\pi}Q_{\pi}(s',a')]
$$

$$
V_{\pi}(s)=\sum_a \pi(a\mid s)Q_{\pi}(s,a)
$$

$$
Q_{\pi}(s,a)=\mathbb{E}[R(s,a,s')+\gamma V_{\pi}(s')]
$$

**Key Takeaways**:

- Return defines what the agent tries to maximize.
- Value functions assign expected return to states or actions.
- Bellman equations make value recursive.
- `Q` is often more directly useful for action selection.

---

## Practice Questions

**Q1**: What is the difference between $V_{\pi}(s)$ and $Q_{\pi}(s,a)$?  
> Answer: $V_{\pi}(s)$ values a state under policy $\pi$; $Q_{\pi}(s,a)$ values taking action `a` in state `s` and then following $\pi$.

**Q2**: Why does $V_{\pi}(s)$ average over actions for a stochastic policy?  
> Answer: Because the policy may choose different actions with different probabilities, and each action has its own expected return.

**Q3**: What does the Bellman equation say in words?  
> Answer: A state's value equals immediate reward plus discounted expected value of the next state.

**Q4**: If all rewards are multiplied by 10, what happens to values?  
> Answer: Values also scale by 10, assuming the same policy and dynamics.
