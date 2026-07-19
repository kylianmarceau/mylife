# CSC3041F FINAL Mock Exam Memo

**Total:** 180 marks

This memo gives model answers. For calculation questions, equivalent working and equivalent tie-breaking conventions should be accepted if they are stated clearly.

---

## Section A: Multiple Choice Questions

### Question 1 [20]

$$
\begin{array}{c|cccccccccccccccccccc}
\text{Question} & 1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20\\
\hline
\text{Answer} & C&B&A&C&A&B&C&C&B&A&A&B&A&A&A&A&A&B&B&B
\end{array}
$$

---

## Section B: State-Space and Heuristic Search

### Question 2 [10]

1. One valid formulation:
   - States: legal grid positions $(r,c)$ not occupied by walls.
   - Initial state: $(1,1)$.
   - Actions: $A(s)\subseteq\{U,D,L,R\}$, containing only moves that stay inside the grid and do not enter walls.
   - Result: $Result((r,c),a)$ is the neighbouring legal cell reached by action $a$.
   - Goal test: $s=(3,4)$.
   - Path cost: sum of unit step costs, so the cost is the number of moves.

2. First two search-tree levels, using legal actions:
   $$
   \begin{aligned}
   \text{Level }0 &: (1,1),\\
   \text{Level }1 &: R\to(1,2),\\
   \text{Level }2 &: D\to(2,2),\quad L\to(1,1),\quad R\to(1,3).
   \end{aligned}
   $$

3. A state is a world configuration, here a grid cell such as $(1,2)$. A node is a search data structure containing a state plus information such as parent, action, depth and path cost.

4. Graph search is preferable because the grid contains repeated states and cycles. Without a reached/explored set, tree search can keep revisiting cells such as $(1,1)\leftrightarrow(1,2)$.

### Question 3 [10]

Using graph search, alphabetical successor order and goal testing when a node is selected for expansion:

1. BFS:
   $$
   \text{Expansion order: } A,B,C,D,E,F,G,
   \qquad
   \text{Returned path: } A\to C\to G.
   $$
   If the goal is tested when generated, BFS may stop after expanding $C$, but the returned path is still $A\to C\to G$.

2. DFS:
   $$
   \text{Expansion order: } A,B,E,G,
   \qquad
   \text{Returned path: } A\to B\to E\to G.
   $$

3. Uniform-cost search:
   $$
   \text{Expansion order: } A,B,D,C,F,E,G,
   \qquad
   \text{Optimal path: } A\to B\to F\to G,
   \qquad
   1+2+3=6.
   $$

4. Iterative deepening first finds a goal at depth limit $2$:
   $$
   \text{Path: } A\to C\to G.
   $$

5. Uniform-cost search is guaranteed to return the cheapest path because it expands nodes in increasing path cost $g(n)$, assuming non-negative step costs.

### Question 4 [10]

1. After expanding $A$:
   $$
   f(B)=1+4=5,\qquad f(C)=4+3=7,\qquad f(D)=2+4=6.
   $$

2. A* graph search:
   $$
   \begin{aligned}
   &\text{Expand }A:
   &&B(f=5),\ D(f=6),\ C(f=7).\\
   &\text{Expand }B:
   &&F(g=3,f=5),\ E(g=6,f=7).\\
   &\text{Expand }F:
   &&G(g=6,f=6).\\
   &\text{Expand }D:
   &&C\text{ improves to }g=3,\ f=6.\\
   &\text{Expand }C:
   &&\text{no better route to }F\text{ or }G.\\
   &\text{Expand }G.&&
   \end{aligned}
   $$
   $$
   \text{Expansion order: }A,B,F,D,C,G.
   $$
   Final path:
   $$
   A\to B\to F\to G.
   $$
   Cost $6$.

3. True cheapest costs-to-go:
   $$
   h^*(G)=0,\ h^*(F)=3,\ h^*(E)=1,\ h^*(C)=4,\ h^*(D)=5,\ h^*(B)=5,\ h^*(A)=6.
   $$
   Given $h(A)=5,h(B)=4,h(C)=3,h(D)=4,h(E)=1,h(F)=2,h(G)=0$. Since $h(s)\le h^*(s)$ for every state, the heuristic is admissible.

4. Beam search with width $b=2$, ranking by $h$:
   $$
   \begin{aligned}
   \text{From }A &: C(h=3),\ B(h=4),\ D(h=4);
   &&\text{keep } C,B.\\
   \text{Expand }C,B &: G(h=0),\ E(h=1),\ F(h=2);
   &&\text{keep } G,E.
   \end{aligned}
   $$
   The goal is found with path:
   $$
   A\to C\to G.
   $$

### Question 5 [10]

1. Misplaced tiles, ignoring blank:
   $$
   \text{Wrong tiles}=\{2,8,1,6\},
   \qquad
   h_{\text{misplaced}}=4.
   $$

2. Manhattan distance:
   $$
   d(2)=1,\quad d(8)=2,\quad d(1)=1,\quad d(6)=1,
   $$
   all other non-blank tiles have distance $0$. Therefore:
   $$
   h_{\text{Manhattan}}=1+2+1+1=5.
   $$

3. Manhattan distance dominates misplaced tiles because every misplaced tile has Manhattan distance at least $1$, and some tiles may be more than one move away. It gives a value at least as large while remaining admissible.

4. Valid relaxed problems include:
   - tiles may move through each other and only distance to goal matters, giving Manhattan distance;
   - any tile can move into the blank position regardless of adjacency, giving misplaced-tile-style estimates.

5. If both heuristics are admissible, $\max(h_1,h_2)$ is still admissible and is more informed than either heuristic alone. $\min(h_1,h_2)$ is weaker because it throws away useful lower-bound information.

6. A* can use large memory because it stores the frontier and reached/explored states. Reference-count cleanup can remove ancestors no longer needed for any frontier path. Beam search keeps only the best $k$ nodes at a level/frontier, while delta-beam search keeps nodes within a chosen quality threshold.

---

## Section C: Game Search and MCTS

### Question 6 [13]

1. MAX-node values:
   $$
   A1=\max(3,12)=12,\quad A2=\max(8,2)=8,
   $$
   $$
   B1=\max(4,6)=6,\quad B2=\max(14,5)=14,
   $$
   $$
   C1=\max(2,9)=9,\quad C2=\max(0,7)=7.
   $$
   MIN-node values:
   $$
   A=\min(12,8)=8,\quad B=\min(6,14)=6,\quad C=\min(9,7)=7.
   $$
   Root:
   $$
   \max(8,6,7)=8.
   $$

2. MAX should choose action $A$.

3. Alpha-beta left to right:
   $$
   \text{Evaluated leaves: }3,12,8,2,4,6,2,9,0,7.
   $$
   $$
   \text{Pruned leaves: }14,5.
   $$
   Explanation: after $A$ returns $8$, root has $\alpha=8$. At $B$, $B1$ returns $6$, so $B$'s $\beta=6\le \alpha=8$, and $B2$ is pruned.

4. Better move ordering can make high MAX values or low MIN values appear earlier, causing cutoffs sooner. It does not change the minimax value or final optimal move, only the number of nodes evaluated.

### Question 7 [7]

1. Work bottom-up. Player 3 chooses first at the terminal-pair level.

   Under $X$:
   $$
   X_1\mapsto(5,3,7)\quad(7>2),
   \qquad
   X_2\mapsto(2,8,4)\quad(4>1).
   $$
   Player 2 then chooses between $(5,3,7)$ and $(2,8,4)$, selecting $(2,8,4)$ because $8>3$.

   Under $Y$:
   $$
   Y_1\mapsto(6,1,5)\quad(5>2),
   \qquad
   Y_2\mapsto(1,9,8)\quad(8>3).
   $$
   Player 2 selects $(1,9,8)$ because $9>1$.

   Therefore:
   $$
   X\mapsto(2,8,4),\qquad Y\mapsto(1,9,8).
   $$

2. Player 1 chooses $X$, because $2>1$ in the first utility component.

3. Evaluation functions are needed because full game trees are usually too large to search to terminal states, so cut-off states need approximate values.

4. The utilities are not constant-sum/$K$-sum because terminal utility sums are not all equal. Cooperation or shifting alliances could replace selfish component-wise backup with a coalition or weighted-utility backup, changing which branch is preferred.

### Question 8 [5]

1. The four MCTS phases are selection, expansion, simulation/rollout and backpropagation/backup. UCB is used in the selection phase.

2. With $N(s)=32$, $c_{\text{ucb}}=1.4$:
   $$
   \mathrm{UCB}(s,a_1)=0.62+1.4\sqrt{\frac{\ln 32}{1+10}}\approx 1.406,
   $$
   $$
   \mathrm{UCB}(s,a_2)=0.50+1.4\sqrt{\frac{\ln 32}{1+2}}\approx 2.005,
   $$
   $$
   \mathrm{UCB}(s,a_3)=0.70+1.4\sqrt{\frac{\ln 32}{1+20}}\approx 1.269.
   $$

3. UCT selects $a_2$, the highest UCB score.

4. Incremental mean update:
   $$
   N(s,a_2)=3,
   $$
   $$
   Q_{\text{new}}(s,a_2)=0.50+\frac{0.8-0.50}{3}=0.60.
   $$

---

## Section D: Reinforcement Learning Foundations and Dynamic Programming

### Question 9 [8]

1. The MDP tuple is:
   $$
   (S,A,P,R,\gamma),
   $$
   where $S=\{s_0,s_1,T\}$, $A=\{L,R\}$, $P$ is given by the deterministic transitions, $R$ is given by the listed rewards and $\gamma=0.9$.

2. For $s_0,R,1,s_1,R,4,T$:
   $$
   G_0=1+0.9(4)=4.6.
   $$

3. Under $\mu(s_0)=R,\mu(s_1)=R$:
   $$
   V^\mu(s_1)=4,
   $$
   $$
   V^\mu(s_0)=1+0.9V^\mu(s_1)=1+0.9(4)=4.6.
   $$

4. With partial observability, the agent would not directly know the true state. The policy may need to depend on observations, histories or belief states rather than just $s$, and the Markov property may fail for the observed signal alone.

### Question 10 [10]

1. Stochastic state-value Bellman expectation equation:
   $$
   V^\pi(s_0)=0.25[0+0.9V^\pi(s_0)]+0.75[1+0.9V^\pi(s_1)].
   $$

2. Stochastic action-value Bellman expectation equation:
   $$
   Q^\pi(s_0,R)=1+0.9V^\pi(s_1),
   $$
   where
   $$
   V^\pi(s_1)=0.4[0+0.9V^\pi(s_0)]+0.6[4].
   $$

3. Deterministic state-value Bellman expectation equation:
   $$
   V^\mu(s)=\sum_{s'}P(s'|s,\mu(s))
   \left[R(s,\mu(s),s')+\gamma V^\mu(s')\right].
   $$

4. Deterministic action-value Bellman expectation equation:
   $$
   Q^\mu(s,a)=\sum_{s'}P(s'|s,a)
   \left[R(s,a,s')+\gamma Q^\mu(s',\mu(s'))\right].
   $$

5. The advantage function is:
   $$
   A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s).
   $$
   A positive advantage means action $a$ is better than the policy's average action choice at state $s$.

### Question 11 [12]

1. Initialize $V_0(s_0)=V_0(s_1)=V_0(T)=0$.

   First iteration:
   $$
   V_1(s_0)=\max(0+0.9V_0(s_0),1+0.9V_0(s_1))=\max(0,1)=1,
   $$
   $$
   V_1(s_1)=\max(0+0.9V_0(s_0),4)=\max(0,4)=4.
   $$

   Second iteration:
   $$
   V_2(s_0)=\max(0+0.9V_1(s_0),1+0.9V_1(s_1))
   =\max(0.9,4.6)=4.6,
   $$
   $$
   V_2(s_1)=\max(0+0.9V_1(s_0),4)
   =\max(0.9,4)=4.
   $$

2. Greedy policy from $V_2$:
   $$
   \pi(s_0)=R,\qquad \pi(s_1)=R.
   $$

3. Under $\mu_0(s_0)=L,\mu_0(s_1)=R$:
   $$
   V^{\mu_0}(s_0)=0+0.9V^{\mu_0}(s_0),
   $$
   so $V^{\mu_0}(s_0)=0$. Also:
   $$
   V^{\mu_0}(s_1)=4.
   $$

4. Greedy improvement using $V^{\mu_0}$:
   $$
   Q(s_0,L)=0+0.9(0)=0,\qquad Q(s_0,R)=1+0.9(4)=4.6,
   $$
   so $s_0$ changes from $L$ to $R$. At $s_1$:
   $$
   Q(s_1,L)=0+0.9(0)=0,\qquad Q(s_1,R)=4,
   $$
   so $s_1$ stays $R$. Improved policy:
   $$
   \mu_1(s_0)=R,\qquad \mu_1(s_1)=R.
   $$

5. Policy evaluation estimates $V^\pi$ for a fixed policy. Policy improvement changes the policy greedily using the current value estimates.

---

## Section E: Model-Free, Deep and Modern Reinforcement Learning

### Question 12 [10]

1. First-visit return for $A$ at $t=0$:
   $$
   G_0=2+0.9(-1)+0.9^2(3)=2-0.9+2.43=3.53.
   $$

2. Every-visit returns for $A$:
   $$
   G_0=3.53,\qquad G_2=3.
   $$

3. TD(0) update at $t=0$:
   $$
   \delta_0=2+0.9V(B)-V(A)=2+0.9(0.5)-1.0=1.45.
   $$
   $$
   V(A)\leftarrow 1.0+0.2(1.45)=1.29.
   $$

4. Two-step return from $t=0$, using the current pre-update estimate $V(A)=1.0$:
   $$
   G_0^{(2)}=R_1+\gamma R_2+\gamma^2V(S_2)
   =2+0.9(-1)+0.9^2(1.0)=1.91.
   $$

5. Accumulating eligibility trace:
   $$
   e_t(s)=\gamma\lambda e_{t-1}(s)+\mathbf{1}\{S_t=s\},
   $$
   with updates such as:
   $$
   V(s)\leftarrow V(s)+\alpha\delta_t e_t(s).
   $$
   $\lambda=0$ gives TD(0)-style one-step updates. $\lambda=1$ approaches Monte Carlo-style full-return credit assignment in episodic tasks.

### Question 13 [10]

Old value: $Q(s,a_1)=1.0$.

1. SARSA target uses the action actually taken, $a_3$:
   $$
   y=2+0.9Q(s',a_3)=2+0.9(2.0)=3.8.
   $$
   $$
   Q(s,a_1)\leftarrow 1.0+0.1(3.8-1.0)=1.28.
   $$

2. Q-learning target uses the greedy next action:
   $$
   \max_{a'}Q(s',a')=\max(3.0,1.0,2.0)=3.0.
   $$
   $$
   y=2+0.9(3.0)=4.7.
   $$
   $$
   Q(s,a_1)\leftarrow 1.0+0.1(4.7-1.0)=1.37.
   $$

3. Expected SARSA:
   $$
   \mathbb{E}_{a'\sim\pi}Q(s',a')
   =0.5(3.0)+0.2(1.0)+0.3(2.0)=2.3.
   $$
   $$
   y=2+0.9(2.3)=4.07.
   $$
   $$
   Q(s,a_1)\leftarrow 1.0+0.1(4.07-1.0)=1.307.
   $$

4. With $\epsilon=0.2$ and $|A|=3$, using the common convention that the random action is chosen uniformly from all actions:
   $$
   P(\text{greedy})=1-\epsilon+\frac{\epsilon}{|A|}
   =0.8+\frac{0.2}{3}=0.867.
   $$
   If exploration is defined as choosing only among non-greedy actions, the answer would be $0.8$.

5. Softmax/Boltzmann selection:
   $$
   \pi(a|s)=\frac{\exp(Q(s,a)/\tau)}{\sum_b\exp(Q(s,b)/\tau)}.
   $$
   Smaller $\tau$ makes the policy more greedy. Larger $\tau$ makes it more uniform/random.

### Question 14 [10]

1. For $V_w(s)=w^\top x(s)$:
   $$
   L(w)=\frac{1}{2}(y-V_w(s))^2,
   $$
   $$
   w\leftarrow w+\alpha(y-w^\top x(s))x(s).
   $$

2. DQN target:
   $$
   y=r+\gamma\max_{a'}Q_{\theta^-}(s',a').
   $$
   Squared loss:
   $$
   L(\theta)=\left(y-Q_\theta(s,a)\right)^2.
   $$
   Replay buffers reduce sample correlation and allow reuse of experience. Target networks keep $\theta^-$ fixed for a while, stabilizing the bootstrapped target.

3. REINFORCE estimate:
   $$
   G_t\nabla_\theta\log\pi_\theta(a|s)=5(1,-2)=(5,-10).
   $$

4. With baseline $b(s)=3$, multiplier:
   $$
   G_t-b(s)=5-3=2.
   $$
   Gradient estimate:
   $$
   2(1,-2)=(2,-4).
   $$
   Baselines reduce variance because the expected baseline term is zero:
   $$
   \mathbb{E}_{a\sim\pi}[\nabla_\theta\log\pi_\theta(a|s)b(s)]
   =b(s)\nabla_\theta\sum_a\pi_\theta(a|s)=0.
   $$

5. PPO clipped surrogate objective:
   $$
   L^{CLIP}(\theta)
   =\mathbb{E}_t\left[
   \min\left(
   r_t(\theta)A_t,
   \mathrm{clip}(r_t(\theta),1-\epsilon,1+\epsilon)A_t
   \right)
   \right],
   $$
   where:
   $$
   r_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}.
   $$

### Question 15 [10]

1. Tabular $Q(s,a)$ does not scale to continuous control because there are infinitely many or extremely many states/actions. It would require impossible table storage and cannot generalize to unseen states.

2. In actor-critic:
   - the actor learns the policy $\pi_\theta(a|s)$;
   - the critic learns a value estimate such as $V_w(s)$, $Q_w(s,a)$ or an advantage estimate.

3. Examples:
   - Double DQN reduces overestimation bias from the max operator.
   - Dueling DQN separates state value and action advantage.
   - Prioritized replay samples more informative transitions more often.

4. True model-based RL learns or uses a transition/reward model and can be more sample efficient, but it can suffer from model bias if the model is wrong. Model-free RL avoids explicit model bias but usually needs much more experience.

5. Offline RL risk: the learned policy may choose out-of-distribution actions whose values are poorly estimated. Multi-agent RL risk: other agents make the environment non-stationary. Multi-objective RL risk: objectives may conflict and reward weights may encode the wrong trade-off.

---

## Section F: Control Systems and RL for Control

### Question 16 [15]

1. Error:
   $$
   e_t=r_t-y_t=10-8=2.
   $$
   Integral:
   $$
   I_t=I_{t-1}+e_t\Delta t=4+2(1)=6.
   $$
   Derivative:
   $$
   \frac{e_t-e_{t-1}}{\Delta t}=\frac{2-1}{1}=1.
   $$
   PID terms:
   $$
   P=K_pe_t=0.6(2)=1.2,
   $$
   $$
   I=K_iI_t=0.1(6)=0.6,
   $$
   $$
   D=K_d\frac{e_t-e_{t-1}}{\Delta t}=0.2(1)=0.2.
   $$
   Control output:
   $$
   u_t=1.2+0.6+0.2=2.0.
   $$

2. This is closed-loop control because the action depends on the measured distance $y_t$ through the feedback error $e_t=r_t-y_t$.

3. State update:
   $$
   Ax_t=
   \begin{bmatrix}1&1\\0&1\end{bmatrix}
   \begin{bmatrix}2\\3\end{bmatrix}
   =
   \begin{bmatrix}5\\3\end{bmatrix},
   \qquad
   Bu_t=
   \begin{bmatrix}0\\1\end{bmatrix}(-1)
   =
   \begin{bmatrix}0\\-1\end{bmatrix}.
   $$
   $$
   x_{t+1}=
   \begin{bmatrix}5\\2\end{bmatrix}.
   $$
   Since the question asks for $y_t=Cx_t$:
   $$
   y_t=\begin{bmatrix}1&0\end{bmatrix}
   \begin{bmatrix}2\\3\end{bmatrix}=2.
   $$
   If asked for $y_{t+1}$, it would be $5$.

4. Model-based control uses an explicit model of the plant dynamics to choose actions. Model-free control learns a controller directly from data or experience without explicitly modelling the dynamics. Model predictive control repeatedly solves a finite-horizon optimization problem using a model and the current state.

5. Advantage: RL can learn complex nonlinear controllers from interaction and optimize delayed rewards. Risk: real-world exploration can be unsafe, expensive or transfer poorly from simulation.

6. Valid techniques include domain randomization, system identification, sim-to-real fine-tuning, safety filters/shields or training with realistic noise/disturbances.

### Question 17 [10]

1. Suitable cartpole formulation:
   - State: cart position, cart velocity, pole angle and pole angular velocity.
   - Action: push left/right, or a continuous horizontal force.
   - Reward: positive reward for keeping the pole upright and cart inside bounds, with penalties for falling, leaving bounds or excessive control effort.

2. Automation follows a fixed or pre-programmed procedure under expected conditions. Autonomy adapts decisions online based on state, goals and feedback, especially when conditions vary.

3. Valid integrations include:
   - RL chooses high-level setpoints while PID controls low-level actuators;
   - a safety shield overrides unsafe RL actions;
   - RL learns a residual correction on top of a classical controller;
   - MPC uses a learned model or RL policy inside planning.

4. A practical pipeline:
   $$
   \text{simulator}\to\text{train policy}\to
   \text{validate with noise/domain randomization}\to
   \text{safe hardware tests}\to
   \text{monitor and fine-tune}.
   $$

5. Valid South African application areas include power-grid/load-shedding control, traffic-light optimization, mining automation, water distribution, irrigation or renewable-energy management.

---

## Memo Coverage Check

The memo covers all 17 questions and matches the 180-mark final mock exam.
