# Reinforcement Learning Mock Exam

**Course**: CSC3041F Automated Planning  
**Topic coverage**: Reinforcement Learning notes, MCTS notes, and RL for Control notes  
**Time**: 3 hours  
**Total**: 150 marks  

---

## Instructions

- Answer all questions.
- Show working for all numerical calculations.
- Unless stated otherwise, assume finite discounted MDPs with $0 \le \gamma < 1$.
- You may use standard notation: $S,A,P,R,\gamma,\pi,V^\pi,Q^\pi,V^*,Q^*$.
- If a question asks for an explanation, formulas alone are not enough.

---

## Section A: RL Foundations And MDPs

### Question 1: Core RL Concepts [12]

1. Distinguish reinforcement learning from supervised learning and imitation learning. [3]
2. Define each of the following in the RL loop: agent, environment, action, reward, policy, return. [6]
3. Explain the credit assignment problem in RL. [2]
4. Why can a small negative per-step reward be useful in a gridworld task? [1]

### Question 2: MDP Modelling And Observability [10]

A robot moves in a gridworld. It can move `Up`, `Down`, `Left`, or `Right`. It receives $+10$ for reaching the goal, $-1$ for hitting a wall, and $-0.1$ per normal move. Some tiles become dangerous only after the robot has visited them once.

1. Give a suitable MDP tuple for this task and describe each component. [5]
2. If the state is represented only by the robot's $(x,y)$ position, does it satisfy the Markov property? Explain. [2]
3. What extra information should be added to the state to make it Markov? [1]
4. Explain the difference between a fully observable MDP and a POMDP in this scenario. [2]

### Question 3: Discounted Return And Horizon [8]

An episode produces rewards:

$$
R_1=2,\quad R_2=-1,\quad R_3=4,\quad R_4=10
$$

with $\gamma=0.5$.

1. Compute $G_0$. [3]
2. Write the general discounted return formula. [2]
3. Explain what happens behaviorally when $\gamma \to 0$ and when $\gamma \to 1$. [2]
4. Explain the difference between finite-horizon and continuing tasks. [1]

---

## Section B: Value Functions And Bellman Equations

### Question 4: Value And Action-Value Functions [12]

1. Define $V^\pi(s)$ and $Q^\pi(s,a)$. [2]
2. Write the relationship between $V^\pi(s)$ and $Q^\pi(s,a)$ for a stochastic policy. [2]
3. Write the relationship between $V^\mu(s)$ and $Q^\mu(s,a)$ for a deterministic policy $\mu$. [2]
4. Write the stochastic Bellman expectation equation for $V^\pi(s)$. [2]
5. Write the stochastic Bellman expectation equation for $Q^\pi(s,a)$. [2]
6. Define the advantage function $A^\pi(s,a)$ and explain what it measures. [2]

### Question 5: Optimal Values And Optimal Policies [10]

At state $s$, the optimal action values are:

| Action | $Q^*(s,a)$ |
|---|---:|
| Up | 3 |
| Right | 6 |
| Down | 6 |
| Left | -1 |

1. What is $V^*(s)$? [1]
2. Which actions are optimal at $s$? [2]
3. Explain the difference between $\max_a Q^*(s,a)$ and $\arg\max_a Q^*(s,a)$. [2]
4. Write the Bellman optimality equation for $V^*(s)$ in a stochastic MDP. [3]
5. Why does extracting a greedy policy from $V^*$ require a model, while extracting it from $Q^*$ does not? [2]

---

## Section C: Dynamic Programming With Known MDPs

### Question 6: Value Iteration [12]

For a state $s$, suppose $\gamma=0.9$ and the current value estimates are:

$$
V(A)=4,\quad V(B)=1,\quad V(T)=0
$$

where $T$ is terminal. From state $s$, there are three actions:

- $a_1$: go to $A$ with reward $2$.
- $a_2$: with probability $0.5$ go to $A$ with reward $0$, and with probability $0.5$ go to $B$ with reward $6$.
- $a_3$: go to terminal state $T$ with reward $5$.

1. Compute the Bellman backup value for each action. [6]
2. What is the updated value $V_{\text{new}}(s)$ under value iteration? [2]
3. Which action would the greedy policy choose after this backup? [1]
4. State whether value iteration is model-based or model-free, and justify. [1]
5. Give the per-sweep complexity of value iteration for a dense stochastic MDP. [1]
6. What property of the Bellman optimality operator explains convergence when $\gamma<1$? [1]

### Question 7: Policy Iteration And GPI [8]

1. Name the two main steps of policy iteration. [2]
2. During policy evaluation, which Bellman equation is used: expectation or optimality? Explain why. [2]
3. A policy currently chooses `Left` in state $s$. One-step lookahead gives $q_\pi(s,\text{Left})=4$ and $q_\pi(s,\text{Right})=5$. What should policy improvement do at $s$? [2]
4. What condition stops exact policy iteration? [1]
5. What is generalized policy iteration? [1]

---

## Section D: Model-Free Prediction And Control

### Question 8: Monte Carlo Methods [10]

State $S$ appears in sampled episodes with the following returns after visits:

- Episode 1: first visit return $5$, later visit return $2$.
- Episode 2: first visit return $8$.
- Episode 3: first visit return $-1$, later visit return $4$.

1. Compute the first-visit Monte Carlo estimate of $V(S)$. [2]
2. Compute the every-visit Monte Carlo estimate of $V(S)$. [2]
3. If the current estimate is $V(S)=3$, a new return is $G=9$, and $\alpha=0.2$, compute the incremental MC update. [2]
4. Why does Monte Carlo prediction usually wait until the episode ends? [1]
5. Why does Monte Carlo control estimate $Q(s,a)$ rather than only $V(s)$? [2]
6. State one main disadvantage of Monte Carlo methods. [1]

### Question 9: Temporal Difference Learning [10]

Suppose:

$$
V(s)=10,\quad R=2,\quad V(s')=12,\quad \gamma=0.5,\quad \alpha=0.1
$$

1. Compute the TD target. [2]
2. Compute the TD error $\delta$. [2]
3. Compute the TD(0) update for $V(s)$. [2]
4. For $n=2$, $R_{t+1}=1$, $R_{t+2}=2$, $V(S_{t+2})=10$, and $\gamma=0.5$, compute the 2-step TD target. [2]
5. Compare Monte Carlo and TD in terms of bootstrapping, bias, and variance. [2]

### Question 10: SARSA, Q-Learning, Expected SARSA, And Exploration [12]

Suppose:

$$
Q(s,a)=4,\quad R=1,\quad \gamma=0.9,\quad \alpha=0.5
$$

At the next state $s'$:

- The actual next action chosen has value $Q(s',a')=3$.
- The best next action has value $5$.
- A stochastic policy chooses action $b_1$ with probability $0.7$ and value $3$, and action $b_2$ with probability $0.3$ and value $5$.

1. Compute the SARSA target and updated $Q(s,a)$. [3]
2. Compute the Q-learning target and updated $Q(s,a)$. [3]
3. Compute the Expected SARSA target and updated $Q(s,a)$. [3]
4. Explain the key difference between on-policy and off-policy learning. [2]
5. In an $\varepsilon$-greedy policy with four actions and $\varepsilon=0.2$, what is the probability of choosing the greedy action if random exploration is uniform over all four actions? [1]

---

## Section E: Function Approximation And Modern RL

### Question 11: Function Approximation And DQN [12]

1. Why do tabular value methods fail in very large or continuous state spaces? [2]
2. What does $\theta$ represent in $Q(s,a;\theta)$? [1]
3. Given $r=1$, $\gamma=0.9$, and next-state Q-values $[2,5,3]$, compute the DQN target. [2]
4. If the current prediction is $Q(s,a;\theta)=4.0$, compute the squared error loss using your target from part 3. [2]
5. Explain why DQN can be unstable if trained naively. [2]
6. Explain how replay buffers and target networks improve DQN stability. [3]

### Question 12: Modern RL Families And Extensions [12]

1. Why is vanilla DQN not naturally suited to continuous action spaces? Name two algorithms more suitable for continuous control. [3]
2. What does true model-based RL learn, and how is it different from model-free RL? [2]
3. Explain the difference between a policy-gradient method and a value-based method. [2]
4. What are the actor and critic in actor-critic methods? [2]
5. What is the purpose of an advantage estimate in policy-gradient updates? [1]
6. Why is offline RL risky when the learned policy chooses actions rarely present in the logged dataset? [2]

---

## Section F: MCTS And RL For Control

### Question 13: Monte Carlo Tree Search [12]

1. List and briefly describe the four phases of MCTS. [4]
2. Write the UCB score used in UCB-style MCTS selection. [2]
3. A parent node has $N(s)=100$ visits. Use $c_{\mathrm{ucb}}=1.4$.

   Child A has $Q(s,A)=0.65$ and $N(s,A)=20$.  
   Child B has $Q(s,B)=0.55$ and $N(s,B)=2$.

   Compute the UCB score for both children and choose the selected child. [4]
4. What happens when the exploration constant is set to $0$? [1]
5. Give one reason MCTS is useful for games such as Go compared with exhaustive alpha-beta search. [1]

### Question 14: RL For Control, Safety, And Applications [10]

1. For cartpole, give a reasonable state representation, action representation, and reward function. [3]
2. A room heater controls temperature near a fixed set-point and behaves roughly linearly. Would PID or RL be the natural first choice? Justify. [2]
3. A robot arm must output continuous torque values in a nonlinear environment. Why might RL be more suitable than PID? [2]
4. An RL policy suggests motor torque $a_t^{\mathrm{RL}}=120$ Nm, but the hardware limit is $80$ Nm. What should a safety layer do? [1]
5. Explain hierarchical control using an example where RL is high-level and PID is low-level. [1]
6. Give one real-world application where RL-based control could be useful, and state one safety concern. [1]

