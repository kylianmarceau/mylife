# Reinforcement Learning Mock Exam: Marking Memo

This memo follows `RL_Mock_Exam.md`. Award equivalent marks for correct reasoning even if notation differs.

---

## Question 1: Core RL Concepts [12]

1. Supervised learning learns from labelled input-output pairs; imitation learning copies expert demonstrations; RL learns by interacting with an environment and optimizing cumulative reward. [3]
2. Agent chooses actions; environment responds; action is the chosen decision; reward is scalar feedback; policy maps states/observations to actions or action probabilities; return is cumulative discounted future reward. [6]
3. Credit assignment is deciding which earlier actions caused later reward or failure, especially with delayed rewards. [2]
4. A per-step penalty encourages shorter paths and discourages wandering. [1]

## Question 2: MDP Modelling And Observability [10]

1. Suitable tuple: $S$ includes position and enough history/flags; $A=\{\text{Up, Down, Left, Right}\}$; $P$ or $T$ describes movement, walls, and dangerous tile dynamics; $R$ gives $+10,-1,-0.1$ and danger penalties if applicable; $\gamma$ discounts future rewards. [5]
2. Position alone is not Markov because future danger depends on whether tiles have been visited before, which is hidden from $(x,y)$ alone. [2]
3. Add visited/danger status for relevant tiles, and any other variables needed to predict next transitions and rewards. [1]
4. Fully observable: observation equals the complete state. POMDP: robot only observes partial information, e.g. local cells or position without hidden visited/danger status. [2]

## Question 3: Discounted Return And Horizon [8]

1. $G_0=2+0.5(-1)+0.5^2(4)+0.5^3(10)=2-0.5+1+1.25=3.75$. [3]
2. $G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$, or finite-horizon equivalent with upper limit $H$. [2]
3. $\gamma\to0$ emphasizes immediate reward; $\gamma\to1$ values long-term reward more strongly. [2]
4. Finite-horizon tasks end after a fixed or bounded number of steps; continuing tasks may not naturally terminate. [1]

---

## Question 4: Value And Action-Value Functions [12]

1. $V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ and $Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$. [2]
2. $V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a)$. [2]
3. $V^\mu(s)=Q^\mu(s,\mu(s))$. [2]
4. $V^\pi(s)=\sum_a\pi(a\mid s)\sum_{s'}P(s'\mid s,a)[r(s,a,s')+\gamma V^\pi(s')]$. [2]
5. $Q^\pi(s,a)=\sum_{s'}P(s'\mid s,a)[r(s,a,s')+\gamma\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')]$. [2]
6. $A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)$; it measures whether action $a$ is better or worse than the policy's average action at $s$. [2]

## Question 5: Optimal Values And Optimal Policies [10]

1. $V^*(s)=6$. [1]
2. `Right` and `Down` are optimal. [2]
3. $\max$ returns the best value; $\arg\max$ returns the action or actions attaining that value. [2]
4. $V^*(s)=\max_a\sum_{s'}P(s'\mid s,a)[r(s,a,s')+\gamma V^*(s')]$. Equivalent $p(s',r\mid s,a)$ form is acceptable. [3]
5. From $Q^*$, actions are directly ranked by $Q^*(s,a)$. From $V^*$, one must use the transition/reward model to compute one-step lookahead action values. [2]

---

## Question 6: Value Iteration [12]

1. $a_1: 2+0.9(4)=5.6$.  
   $a_2: 0.5[0+0.9(4)]+0.5[6+0.9(1)]=0.5(3.6)+0.5(6.9)=5.25$.  
   $a_3: 5+0.9(0)=5$. [6]
2. $V_{\text{new}}(s)=\max(5.6,5.25,5)=5.6$. [2]
3. Choose $a_1$. [1]
4. Model-based, because it needs transition probabilities and rewards. [1]
5. Dense stochastic per-sweep complexity: $O(|S|^2|A|)$. [1]
6. The Bellman optimality operator is a contraction under the sup norm when $\gamma<1$. [1]

## Question 7: Policy Iteration And GPI [8]

1. Policy evaluation and policy improvement. [2]
2. Bellman expectation equation, because the policy is fixed during evaluation rather than optimized at each state. [2]
3. Switch from `Left` to `Right`, since $5>4$. [2]
4. Stop when the policy is stable: no state changes action after improvement. [1]
5. Generalized policy iteration is the repeated interaction of partial policy evaluation and policy improvement. [1]

---

## Question 8: Monte Carlo Methods [10]

1. First-visit estimate: $(5+8+(-1))/3=4$. [2]
2. Every-visit estimate: $(5+2+8-1+4)/5=18/5=3.6$. [2]
3. $V(S)\leftarrow3+0.2(9-3)=4.2$. [2]
4. MC needs the full return, which is known only after the episode ends. [1]
5. Control must compare actions in a state; $V(s)$ alone does not tell which action caused high return without a model. [2]
6. High variance and/or requires episodic termination. [1]

## Question 9: Temporal Difference Learning [10]

1. TD target $=R+\gamma V(s')=2+0.5(12)=8$. [2]
2. $\delta=8-10=-2$. [2]
3. $V(s)\leftarrow10+0.1(-2)=9.8$. [2]
4. $G_t^{(2)}=1+0.5(2)+0.5^2(10)=1+1+2.5=4.5$. [2]
5. MC does not bootstrap, is less biased but often higher variance; TD bootstraps from current estimates, is biased but often lower variance and can update online. [2]

## Question 10: SARSA, Q-Learning, Expected SARSA, And Exploration [12]

1. SARSA target $=1+0.9(3)=3.7$.  
   Update $=4+0.5(3.7-4)=3.85$. [3]
2. Q-learning target $=1+0.9(5)=5.5$.  
   Update $=4+0.5(5.5-4)=4.75$. [3]
3. Expected next value $=0.7(3)+0.3(5)=3.6$.  
   Target $=1+0.9(3.6)=4.24$.  
   Update $=4+0.5(4.24-4)=4.12$. [3]
4. On-policy learns about the behavior policy being followed; off-policy learns about a target policy that can differ from behavior, often greedy. [2]
5. Greedy action probability $=1-\varepsilon+\varepsilon/4=0.8+0.05=0.85$. [1]

---

## Question 11: Function Approximation And DQN [12]

1. Tables become impossible when states/actions are huge, continuous, or unseen at training time; they do not generalize. [2]
2. $\theta$ is the parameter vector of the approximator, e.g. neural-network weights. [1]
3. DQN target $y=1+0.9\max[2,5,3]=1+4.5=5.5$. [2]
4. Loss $=(5.5-4.0)^2=2.25$. [2]
5. Naive DQN is unstable because targets depend on changing network parameters and sequential samples are correlated. [2]
6. Replay buffers randomize/decorrelate training data and improve sample reuse; target networks hold the target calculation fixed for a while, reducing moving-target instability. [3]

## Question 12: Modern RL Families And Extensions [12]

1. DQN requires maximizing over discrete action values, which is awkward or impossible over continuous actions. Suitable algorithms: DDPG, TD3, SAC. Any two. [3]
2. True model-based RL learns or uses a transition/reward model for planning; model-free RL learns values or policies directly from experience without explicitly modelling dynamics. [2]
3. Policy gradients directly optimize a parameterized policy; value-based methods learn value/action-value functions and derive a policy from them. [2]
4. Actor: policy that chooses actions. Critic: value function estimating how good states/actions are and providing learning signal. [2]
5. Advantage measures action quality relative to a baseline value, reducing variance and focusing updates on better-than-expected actions. [1]
6. Offline RL can extrapolate to out-of-distribution actions with unreliable value estimates; without interaction, bad policy choices may not be corrected safely. [2]

---

## Question 13: Monte Carlo Tree Search [12]

1. Selection: traverse tree using a selection rule such as UCB. Expansion: add a new child node. Simulation/playout: roll out to estimate outcome. Back-propagation: update visit counts and values along the path. [4]
2. $\operatorname{UCB}(s,a)=Q(s,a)+c_{\mathrm{ucb}}\sqrt{\ln N(s)/(1+N(s,a))}$. Equivalent forms without $+1$ are acceptable if explained. [2]
3. Using $\ln100\approx4.605$:  
   A: $0.65+1.4\sqrt{4.605/21}\approx0.65+1.4(0.468)=1.31$.  
   B: $0.55+1.4\sqrt{4.605/3}\approx0.55+1.4(1.239)=2.28$.  
   Select B. [4]
4. $c=0$ removes exploration bonus and selection becomes greedy with respect to current value. [1]
5. MCTS samples promising parts of huge game trees, works under time budgets, and does not require exhaustive search or handcrafted evaluation to the same extent. [1]

## Question 14: RL For Control, Safety, And Applications [10]

1. Cartpole state can include cart position, cart velocity, pole angle, and pole angular velocity. Actions can be left/right force or continuous force. Reward can be $+1$ per balanced time step or penalties for falling/large angle. [3]
2. PID is natural first choice because the heater is roughly linear, low-dimensional, and set-point based. [2]
3. RL can handle nonlinear dynamics, continuous actions, delayed rewards, and complex objectives where hand-designed PID is insufficient. [2]
4. Safety layer should clip/override the action to the safe limit, e.g. apply at most $80$ Nm. [1]
5. Example: RL chooses a target speed or steering angle; PID tracks that target at actuator level. [1]
6. Valid example: robotics, traffic signal control, energy management, drone control, mining/autonomous vehicles, grid/load control. Safety concern: unsafe exploration, hardware damage, constraint violation, sim-to-real mismatch, or human risk. [1]

