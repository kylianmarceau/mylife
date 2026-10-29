---
tags:
  - automated-planning
---

# CSC3041F Automated Planning Formula Sheet

**Subject**: CSC3041F Automated Planning  
**Source Notes**: all notes in `Search/`, `Reinforcement Learning/`, and `Control/`  
**Generated**: 2026-06-01

---

## Symbol Key

| Symbol | Meaning |
|---|---|
| $S$ | state set |
| $A$ | action set |
| $s,s'$ | current and next state |
| $a,a'$ | current and next action |
| $T$ | transition model |
| $R$ | reward function |
| $\gamma$ | discount factor |
| $b$ | branching factor |
| $d$ | depth of shallowest solution |
| $m$ | maximum depth |
| $l$ | depth limit |
| $C$ | optimal solution cost or MCTS exploration constant, depending on context |
| $c$ | smallest positive step cost |
| $g(n)$ | path cost from initial state to node $n$ |
| $h(n)$ | heuristic estimate from node $n$ to a goal |
| $h^*(n)$ | true cheapest remaining cost |
| $k$ | beam width, feature count, or return index, depending on context |
| $\delta$ | delta-beam threshold or TD error, depending on context |
| $\alpha,\beta$ | alpha-beta pruning bounds |
| $\pi$ | policy |
| $V_{\pi},Q_{\pi}$ | state-value and action-value functions under policy $\pi$ |
| $V^*,Q^*$ | optimal state-value and action-value functions |
| $\theta$ | learnable parameters |

---

## State Space And Problem Formulation

State representation:

$$
s=(v_1,v_2,\ldots,v_n),\quad s\in S
$$

Deterministic transition model:

$$
T:S\times A\to S
$$

Problem instance:

$$
\mathrm{ProblemInstance}=\mathrm{ProblemSpace}+\mathrm{InitialState}+\mathrm{GoalState(s)}+\mathrm{ActionCostFunction}
$$

Vacuum-world state count with $n$ cells:

$$
|\mathcal{S}_{\mathrm{vacuum}}|=n\cdot 2^n
$$

Tic-tac-toe naive state count:

$$
3^9=19{,}683
$$

Example vacuum transition:

$$
T((A,\mathrm{dirty},\mathrm{clean}),\mathrm{clean})=(A,\mathrm{clean},\mathrm{clean})
$$

Chess-like transition notation:

$$
s=\{(N_w:a1),(K_w:g1),(K_b:g8),\mathrm{Turn}:\mathrm{White}\}
$$

$$
A(s)=\{N\to b3,N\to c2,K\to f1,K\to f2,K\to h1,K\to h2\}
$$

$$
T(s,N\to b3)=\{(N_w:b3),(K_w:g1),(K_b:g8),\mathrm{Turn}:\mathrm{Black}\}
$$

---

## Uninformed Search

Uniform-cost search priority:

$$
f_{\mathrm{UCS}}(n)=\mathrm{path\_cum\_cost}(n)
$$

Uniform-cost search time and space:

$$
O\!\left(b^{1+\lfloor C/c\rfloor}\right)
$$

Core uninformed-search complexities:

$$
\begin{aligned}
\text{BFS time} &= O(b^d), & \text{BFS space} &= O(b^d)\\
\text{UCS time} &= O\!\left(b^{1+\lfloor C/c\rfloor}\right), & \text{UCS space} &= O\!\left(b^{1+\lfloor C/c\rfloor}\right)\\
\text{DFS time} &= O(b^m), & \text{DFS space} &= O(bm)\\
\text{Depth-limited time} &= O(b^l), & \text{Depth-limited space} &= O(bl)\\
\text{IDS time} &= O(b^d), & \text{IDS space} &= O(bd)
\end{aligned}
$$

---

## Heuristics, A*, And Beam Search

Heuristic function:

$$
h:S\to\mathbb{R}_{\ge 0}
$$

Heuristic approximation:

$$
h(n)\approx h^*(n)
$$

Admissibility:

$$
h(n)\le h^*(n)
$$

Consistency:

$$
h(n)\le c(n,a,n')+h(n')
$$

Misplaced-tile heuristic:

$$
h_1(n)=\text{number of misplaced tiles}
$$

Manhattan-distance heuristic:

$$
h_2(n)=\sum_{t\in\mathrm{tiles}}\mathrm{ManhattanDistance}(t,\mathrm{goal}(t))
$$

8-puzzle total arrangements:

$$
9!=362{,}880
$$

8-puzzle reachable arrangements by parity class:

$$
\frac{9!}{2}=181{,}440
$$

15-puzzle parity-class scale:

$$
\frac{15!}{2}
$$

Relaxed-problem cost bound:

$$
c_{\mathrm{relaxed}}(n,a,n')\le c(n,a,n')
$$

Relaxed-problem consistency:

$$
h(n)\le c_{\mathrm{relaxed}}(n,a,n')+h(n')
$$

Conservative admissible heuristic combination:

$$
h(n)=\max\{h_1(n),h_2(n),h_3(n),\ldots\}
$$

Source-slide weak admissible combination:

$$
h(n)=\min\{h_1(n),h_2(n),h_3(n),\ldots\}
$$

A* evaluation function:

$$
f_{A^*}(n)=g(n)+h(n)
$$

Greedy best-first score:

$$
f_{\mathrm{greedy}}(n)=h(n)
$$

A* space:

$$
\text{A* space}=O(b^d)
$$

Beam-search space:

$$
\text{Beam search space}=O(km)
$$

Delta-beam keep rule:

$$
f(n)\le f(n_{\mathrm{best}})+\delta
$$

---

## Adversarial Search And Game Search

Minimax recurrence:

$$
\begin{aligned}
\mathrm{minimax}(s)&=\mathrm{Utility}(s,\mathrm{MAX}) && \text{if }s\text{ is terminal}\\
\mathrm{minimax}(s)&=\max_a \mathrm{minimax}(\mathrm{Result}(s,a)) && \text{if }s\text{ is a MAX node}\\
\mathrm{minimax}(s)&=\min_a \mathrm{minimax}(\mathrm{Result}(s,a)) && \text{if }s\text{ is a MIN node}
\end{aligned}
$$

Minimax complexity:

$$
\text{Time}=O(b^m),\qquad \text{Space}=O(bm)
$$

Multiplayer utility vector:

$$
\mathrm{Utility}(s)=[V_A,V_B,V_C]
$$

K-sum condition:

$$
V_A+V_B+V_C=K
$$

Zero-sum special case:

$$
K=0
$$

Multiplayer game-tree time complexity:

$$
O(b^m)
$$

Alpha-beta initial bounds:

$$
\alpha_0=-\infty,\qquad \beta_0=+\infty
$$

Alpha-beta updates:

$$
\alpha\leftarrow \max(\alpha,v),\qquad \beta\leftarrow \min(\beta,v)
$$

MAX cutoff:

$$
v\ge\beta
$$

MIN cutoff:

$$
v\le\alpha
$$

Alpha-beta complexity:

$$
\text{Best-case time}=O\!\left(b^{m/2}\right),\qquad \text{Worst-case time}=O(b^m)
$$

Depth-limited search base cases:

$$
\text{if }\mathrm{IsTerminal}(s)\text{, return }\mathrm{Utility}(s)
$$

$$
\text{if }\mathrm{IsCutoff}(s,d)\text{, return }\mathrm{EVAL}(s)
$$

Weighted evaluation function:

$$
\mathrm{EVAL}(s)=w_1f_1(s)+w_2f_2(s)+\cdots+w_kf_k(s)
$$

Chess-like material evaluation from the notes:

$$
\mathrm{EVAL}(s)=1\cdot\mathrm{pawns}+3\cdot\mathrm{bishops}+3\cdot\mathrm{knights}+5\cdot\mathrm{rooks}+9\cdot\mathrm{queens}
$$

Expected utility for outcome categories:

$$
\mathbb{E}[U]=P(\mathrm{win})U(\mathrm{win})+P(\mathrm{draw})U(\mathrm{draw})+P(\mathrm{loss})U(\mathrm{loss})
$$

MCTS empirical value estimate:

$$
\widehat{V}(n)=\frac{\text{total utility}}{\text{number of simulations}}
$$

UCB-style MCTS selection score:

$$
\mathrm{score}(n)=\frac{U(n)}{N(n)}+C\sqrt{\frac{\ln N(\mathrm{parent}(n))}{N(n)}}
$$

Greedy MCTS selection:

$$
C=0\quad\text{gives greedy exploitation}
$$

---

## RL Basics And MDPs

Deterministic policy:

$$
a=\pi(s)
$$

Stochastic policy:

$$
\pi(a\mid s)=P(A_t=a\mid S_t=s)
$$

RL objective:

$$
J(\pi)=\mathbb{E}\!\left[\sum_t \gamma^t r(S_t,A_t)\right]
$$

Constant reward example:

$$
R(s,a)=c
$$

MDP tuple:

$$
\langle S,A,T,R,\gamma\rangle
$$

Transition function:

$$
T(s,a,s')=P(S_{t+1}=s'\mid S_t=s,A_t=a)
$$

Discount factor:

$$
\gamma\in(0,1]
$$

Markov property:

$$
P(S_{t+1}\mid S_t,A_t,S_{t-1},A_{t-1},\ldots,S_0,A_0)=P(S_{t+1}\mid S_t,A_t)
$$

Fully observable MDP:

$$
o_t=s_t
$$

Complete state snapshot:

$$
s_t=\text{complete environment snapshot}
$$

Partial observability:

$$
o_t=\text{partial view of }s_t
$$

Model prediction notation:

$$
\hat{s}_{t+1}\approx s_{t+1}
$$

$$
\hat{r}_t\approx r_t
$$

Finite-horizon discounted return:

$$
G_t=\sum_{k=0}^{H}\gamma^k R_{t+k+1}
$$

Expanded discounted return:

$$
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots
$$

Bellman return split:

$$
G_t=R_{t+1}+\gamma G_{t+1}
$$

---

## Value Functions

Policy action:

$$
a=\pi(s)
$$

Policy distribution:

$$
\pi(a\mid s)=P(A_t=a\mid S_t=s)
$$

Policy probabilities sum to one:

$$
\sum_{a\in A}\pi(a\mid s)=1\quad\forall s\in S
$$

Policy objective:

$$
J(\pi)=\mathbb{E}_{\pi}[G_0]
$$

State-value function:

$$
V_{\pi}(s)=\mathbb{E}_{\pi}[G_t\mid S_t=s]
$$

Stochastic Bellman expectation equation:

$$
V_{\pi}(s)=\mathbb{E}_{a\sim\pi(\cdot\mid s),\,s'\sim P(\cdot\mid s,a)}\!\left[R(s,a)+\gamma V_{\pi}(s')\right]
$$

Deterministic Bellman expectation equation:

$$
V_{\pi}(s)=R(s,\pi(s))+\gamma V_{\pi}(s')
$$

Short Bellman equation:

$$
\text{current value}=\text{immediate reward}+\gamma\cdot\text{future value}
$$

Action-value function:

$$
Q_{\pi}(s,a)=\mathbb{E}_{s'\sim P(\cdot\mid s,a)}\!\left[R(s,a)+\gamma\mathbb{E}_{a'\sim\pi(\cdot\mid s')}Q_{\pi}(s',a')\right]
$$

Deterministic action-value equation:

$$
Q_{\pi}(s,a)=R(s,a)+\gamma Q_{\pi}(s',a')
$$

State value as policy-weighted action value:

$$
V_{\pi}(s)=\mathbb{E}_{a\sim\pi}[Q_{\pi}(s,a)]
$$

$$
V_{\pi}(s)=\sum_a \pi(a\mid s)Q_{\pi}(s,a)
$$

Action value from next-state value:

$$
Q_{\pi}(s,a)=\mathbb{E}_{s'\sim P}\!\left[R(s,a,s')+\gamma V_{\pi}(s')\right]
$$

Example V-Q calculation pattern:

$$
V_{\pi}(3,3)=0.8(0.999)+0.2(-0.001)+0(-0.001)
$$

---

## Optimal Value Functions

Policy evaluation:

$$
V_{\pi}(s)=\sum_a \pi(a\mid s)\left[R(s,a)+\gamma V_{\pi}(s')\right]
$$

Optimal deterministic Bellman equation:

$$
V^*(s)=\max_a\left[R(s,a)+\gamma V^*(s')\right]
$$

Optimal value over policies:

$$
V^*(s)=\max_{\pi}V_{\pi}(s)
$$

Policy domination:

$$
\pi_1\ge \pi_2\quad\text{if}\quad V_{\pi_1}(s)\ge V_{\pi_2}(s)\quad\forall s
$$

Optimal Bellman equation for stochastic transitions:

$$
V^*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma V^*(s')\right]
$$

Optimal action-value equation:

$$
Q^*(s,a)=R(s,a)+\gamma\max_{a'}Q^*(s',a')
$$

Best value:

$$
\max_a Q^*(s,a)
$$

Best action:

$$
\arg\max_a Q^*(s,a)
$$

Extracting the optimal policy from $Q^*$:

$$
\pi^*(s)=\arg\max_a Q^*(s,a)
$$

Extracting the optimal policy from $V^*$:

$$
\pi^*(s)=\arg\max_a\mathbb{E}\left[R_{t+1}+\gamma V^*(s')\right]
$$

Bellman optimality derivation:

$$
\begin{aligned}
V^*(s)&=\max_{\pi}V_{\pi}(s)\\
&=\max_{\pi}\mathbb{E}_{\pi}[G_t\mid S_t=s]\\
G_t&=R_{t+1}+\gamma G_{t+1}\\
V^*(s)&=\max_a\mathbb{E}[R_{t+1}+\gamma G_{t+1}\mid S_t=s,A_t=a]\\
&=\max_a\mathbb{E}[R_{t+1}+\gamma V^*(S_{t+1})\mid S_t=s,A_t=a]\\
&=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')]\\
&=\max_a Q^*(s,a)
\end{aligned}
$$

---

## Dynamic Programming: Value Iteration And Policy Iteration

Value iteration update:

$$
V_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_k(s')]
$$

Greedy policy extraction after value iteration:

$$
\pi(s)=\arg\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]
$$

Value-iteration complexity per sweep:

$$
\text{Complexity per sweep}=O(|S|^2|A|)
$$

Bellman optimality contraction:

$$
\|\mathcal{T}V-\mathcal{T}U\|_{\infty}\le \gamma\|V-U\|_{\infty}
$$

Infinity norm:

$$
\|V-U\|_{\infty}=\max_s |V(s)-U(s)|
$$

Contraction condition:

$$
0\le\gamma<1
$$

Policy evaluation in policy iteration:

$$
V_{\pi}(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_{\pi}(s')]
$$

Policy improvement:

$$
\pi_{\mathrm{new}}(s)=\arg\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_{\pi}(s')]
$$

Policy stability condition:

$$
\pi_{\mathrm{new}}(s)=\pi(s)\quad\forall s
$$

---

## Monte Carlo Methods

Monte Carlo state-value sample average:

$$
V(s)=\frac{1}{N(s)}\sum_{i=1}^{N(s)}G_i(s)
$$

Monte Carlo incremental state-value update:

$$
V(s)\leftarrow V(s)+\alpha\left[G_t-V(s)\right]
$$

Sample-average learning rate:

$$
\alpha=\frac{1}{N(s)}
$$

Monte Carlo action-value sample average:

$$
Q(s,a)=\frac{1}{N(s,a)}\sum_{i=1}^{N(s,a)}G_i(s,a)
$$

---

## Temporal Difference Learning

TD error:

$$
\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)
$$

TD value update:

$$
V(S_t)\leftarrow V(S_t)+\alpha\delta_t
$$

N-step return:

$$
G_t^{(n)}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^nV(S_{t+n})
$$

N-step value update:

$$
V(S_t)\leftarrow V(S_t)+\alpha\left[G_t^{(n)}-V(S_t)\right]
$$

SARSA update:

$$
Q(S,A)\leftarrow Q(S,A)+\alpha\left[R+\gamma Q(S',A')-Q(S,A)\right]
$$

Q-learning update:

$$
Q(S,A)\leftarrow Q(S,A)+\alpha\left[R+\gamma\max_a Q(S',a)-Q(S,A)\right]
$$

---

## Function Approximation, DQN, And Modern RL

Tabular-to-parameterized value function:

$$
Q(s,a)\to Q(s,a;\theta)
$$

DQN / Q-learning TD error with function approximation:

$$
\delta=r+\gamma\max_{a'}Q(s',a';\theta)-Q(s,a;\theta)
$$

Gradient descent update:

$$
\theta\leftarrow\theta-\alpha\nabla_{\theta}L(\theta)
$$

DQN target:

$$
y=r+\gamma\max_{a'}Q(s',a';\theta)
$$

DQN squared loss:

$$
L(\theta)=\left(y-Q(s,a;\theta)\right)^2
$$

Policy-gradient policy notation:

$$
\pi(a\mid s;\theta)
$$
