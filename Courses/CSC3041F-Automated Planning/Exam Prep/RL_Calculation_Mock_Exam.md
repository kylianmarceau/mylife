# Reinforcement Learning Calculation Mock Exam

**Course**: CSC3041F Automated Planning  
**Topic coverage**: all RL calculation skills from the RL notes, plus MCTS calculations  
**Time**: 3 hours  
**Total**: 150 marks  

---

## Instructions

- This is a calculation-only mock exam.
- Show substitutions and arithmetic.
- Do not answer with theory paragraphs unless a short calculation conclusion is required.
- Assume terminal-state value is $0$ unless stated otherwise.

---

## Section A: Returns, MDPs, Values, And Bellman Backups

### Question 1: Discounted Returns [12]

1. Given rewards $R_1=3$, $R_2=-2$, $R_3=4$, $R_4=8$ and $\gamma=0.5$, compute $G_0$. [3]
2. Using the same reward sequence, compute $G_1$. [2]
3. If a continuing task gives constant reward $c=2$ forever with $\gamma=0.8$, compute the infinite-horizon return. [2]
4. For a finite-horizon task with rewards $[1,1,1]$ and $\gamma=0.9$, compute $G_0$. [2]
5. Option A gives reward $5$ immediately. Option B gives reward $8$ after two time steps and no other rewards. Find the values of $\gamma$ for which Option B has higher return than Option A. [3]

### Question 2: Bellman Expectation And Optimality In A Small MDP [14]

There is one non-terminal state $s$ and one terminal state $T$. Let $\gamma=0.9$.

Action $a$:

- with probability $0.7$, returns to $s$ with reward $1$;
- with probability $0.3$, goes to $T$ with reward $5$.

Action $b$:

- goes to $T$ with reward $3$.

For the stochastic policy $\pi(a\mid s)=0.6$, $\pi(b\mid s)=0.4$:

1. Write $Q^\pi(s,a)$ in terms of $V^\pi(s)$. [2]
2. Write $Q^\pi(s,b)$. [1]
3. Solve for $V^\pi(s)$. [4]
4. Compute $Q^\pi(s,a)$ and $Q^\pi(s,b)$. [2]

For the deterministic policy $\mu(s)=a$:

5. Solve for $V^\mu(s)$. [3]
6. Compute $V^*(s)$ and the optimal action. [2]

### Question 3: Policy-Weighted Values, Advantages, And Action Probabilities [12]

At state $s$, action values are:

$$
Q(s,a_1)=2,\quad Q(s,a_2)=5,\quad Q(s,a_3)=-1.
$$

A stochastic policy has:

$$
\pi(a_1\mid s)=0.2,\quad \pi(a_2\mid s)=0.5,\quad \pi(a_3\mid s)=0.3.
$$

1. Compute $V^\pi(s)$. [3]
2. Compute $A^\pi(s,a_1)$, $A^\pi(s,a_2)$, and $A^\pi(s,a_3)$. [3]
3. With $\varepsilon=0.3$ and three actions, compute the $\varepsilon$-greedy probability of each action if $a_2$ is the unique greedy action and random exploration is uniform over all actions. [3]
4. Compute the softmax action probabilities with temperature $\tau=1$. Use $e^2\approx7.389$, $e^5\approx148.413$, and $e^{-1}\approx0.368$. [3]

---

## Section B: Dynamic Programming Calculations

### Question 4: Value Iteration [14]

An MDP has non-terminal states $A$ and $B$, terminal state $T$, and $\gamma=0.8$. Initial values are:

$$
V_0(A)=0,\quad V_0(B)=0,\quad V_0(T)=0.
$$

At state $A$:

- action $x$: goes to $B$ with reward $2$;
- action $y$: goes to $T$ with reward $5$.

At state $B$:

- action $x$: with probability $0.5$ goes to $A$ with reward $0$, and with probability $0.5$ goes to $T$ with reward $4$;
- action $y$: goes to $A$ with reward $1$.

Use synchronous value iteration.

1. Compute $V_1(A)$. [2]
2. Compute $V_1(B)$. [3]
3. Compute $V_2(A)$. [2]
4. Compute $V_2(B)$. [3]
5. Give the greedy action at $A$ using $V_2$. [1]
6. Give the greedy action at $B$ using $V_2$. [1]
7. Compute the maximum residual $\max_s |V_2(s)-V_1(s)|$. [2]

### Question 5: Policy Evaluation And Policy Improvement [12]

Use the same MDP from Question 4. Consider the policy:

$$
\pi(A)=x,\quad \pi(B)=x.
$$

1. Write the two linear equations for $V^\pi(A)$ and $V^\pi(B)$. [3]
2. Solve for $V^\pi(A)$. [3]
3. Solve for $V^\pi(B)$. [2]
4. Compute $q_\pi(A,x)$ and $q_\pi(A,y)$, then give the improved action at $A$. [2]
5. Compute $q_\pi(B,x)$ and $q_\pi(B,y)$, then give the improved action at $B$. [2]

---

## Section C: Monte Carlo, TD, And Eligibility Traces

### Question 6: Monte Carlo Prediction And Control [12]

An episode is:

$$
A \xrightarrow{R=1} B \xrightarrow{R=2} A \xrightarrow{R=-1} T
$$

with $\gamma=0.9$.

1. Compute the return following the first visit to $A$. [2]
2. Compute the return following the visit to $B$. [2]
3. Compute the return following the second visit to $A$. [1]
4. Compute the first-visit MC estimate for $V(A)$ from this one episode. [1]
5. Compute the every-visit MC estimate for $V(A)$ from this one episode. [2]
6. If current $V(A)=2$, $\alpha=0.25$, and the observed first-visit return is used, compute the incremental MC update. [2]
7. In MC control, suppose $Q(s,L)=1.5$, $Q(s,R)=3.2$, and $Q(s,U)=3.2$. With $\varepsilon=0.2$ and three actions, compute the $\varepsilon$-greedy probability of each action, splitting greedy probability equally between tied greedy actions. [2]

### Question 7: TD, N-Step TD, And Eligibility Traces [14]

1. Given $V(s)=6$, $R=2$, $V(s')=4$, $\gamma=0.9$, and $\alpha=0.2$, compute the TD target, TD error, and updated $V(s)$. [4]
2. For $R_{t+1}=1$, $R_{t+2}=2$, $R_{t+3}=3$, $V(S_{t+3})=10$, $\gamma=0.5$, compute the 3-step TD target. [3]
3. For a terminal next state with $R=5$, $V(s)=3$, $\gamma=0.9$, and $\alpha=0.5$, compute the TD error and updated $V(s)$. [3]
4. Eligibility traces before a step are $e(A)=1.0$ and $e(B)=0.5$. Let $\gamma=0.9$, $\lambda=0.8$, current state $S_t=B$, TD error $\delta=2$, and $\alpha=0.1$. Using accumulating traces,
   $$
   e_t(s)=\gamma\lambda e_{t-1}(s)+\mathbf 1\{S_t=s\},
   $$
   compute the new traces and the value increments for $A$ and $B$. [4]

---

## Section D: TD Control And Exploration

### Question 8: SARSA, Q-Learning, Expected SARSA, Epsilon-Greedy, And Softmax [16]

Suppose:

$$
Q(s,a)=2,\quad R=1,\quad \gamma=0.8,\quad \alpha=0.5.
$$

At the next state:

- the actual next action has value $4$;
- the best next action has value $6$;
- a stochastic policy gives action $b_1$ probability $0.25$ and value $2$, and action $b_2$ probability $0.75$ and value $6$.

1. Compute the SARSA target and updated $Q(s,a)$. [3]
2. Compute the Q-learning target and updated $Q(s,a)$. [3]
3. Compute the Expected SARSA target and updated $Q(s,a)$. [3]
4. With five actions and $\varepsilon=0.1$, compute the probability of the unique greedy action and each non-greedy action under $\varepsilon$-greedy exploration. [2]
5. Compute softmax probabilities for action values $[1,2,3]$ with $\tau=1$. Use $e^1\approx2.718$, $e^2\approx7.389$, $e^3\approx20.085$. [3]
6. A terminal transition has $Q(s,a)=5$, $R=-2$, and $\alpha=0.4$. Compute the terminal Q-learning update. [2]

---

## Section E: Function Approximation, DQN, Policy Gradients, And PPO

### Question 9: Function Approximation And DQN [14]

1. A linear value function is $\hat v_w(s)=w_1x_1+w_2x_2$. Let $w=(1,-1)$, $x=(2,3)$, target $G=5$, and $\alpha=0.1$. Compute the prediction error and updated weights using
   $$
   w \leftarrow w+\alpha(G-\hat v_w(s))x.
   $$
   [4]
2. Given $r=2$, $\gamma=0.9$, and target-network next-state Q-values $[4,1,6]$, compute the DQN target. [2]
3. If the current DQN prediction is $Q(s,a;\theta)=5$, compute the squared error loss using your target from part 2. [2]
4. A one-parameter approximator is $Q_\theta(s,a)=2\theta$. Let $\theta=2$, target $y=7$, and $\alpha=0.1$. Using squared error loss $(y-Q_\theta)^2$, compute one gradient-descent update for $\theta$. [4]
5. Double DQN uses online next-state values $[2,5,4]$ and target-network next-state values $[10,1,3]$. With $r=1$ and $\gamma=0.9$, compute the Double DQN target. [2]

### Question 10: Policy Gradient, Actor-Critic, And PPO [14]

1. Let $\theta=(1,1)$, $\nabla_\theta\log\pi_\theta(a\mid s)=(0.5,-0.2)$, return $G=4$, and $\alpha=0.1$. Compute the REINFORCE update. [3]
2. Starting again from $\theta=(1,1)$, use baseline $b=1.5$ with the same gradient and return. Compute the baseline policy-gradient update. [3]
3. In actor-critic, let $R=1$, $\gamma=0.9$, $V(s')=4$, and $V(s)=3$. Compute the TD-error advantage estimate. [2]
4. PPO case 1: $\pi_{\text{old}}(a\mid s)=0.2$, $\pi_\theta(a\mid s)=0.3$, $A=2$, and $\epsilon=0.2$. Compute $r_t$, the clipped ratio, and the clipped surrogate contribution
   $$
   \min(r_tA,\operatorname{clip}(r_t,1-\epsilon,1+\epsilon)A).
   $$
   [3]
5. PPO case 2: $r_t=0.6$, $A=-2$, and $\epsilon=0.2$. Compute the clipped surrogate contribution. [3]

---

## Section F: MCTS And RL Control Calculations

### Question 11: MCTS Calculations [12]

A parent node has $N(s)=100$ visits and $c_{\mathrm{ucb}}=1.4$. Use $\ln(100)\approx4.605$.

| Child | $Q(s,a)$ | $N(s,a)$ |
|---|---:|---:|
| A | 0.50 | 10 |
| B | 0.70 | 40 |
| C | 0.40 | 1 |

1. Compute the UCB score for A, B, and C using
   $$
   \operatorname{UCB}(s,a)=Q(s,a)+c_{\mathrm{ucb}}\sqrt{\frac{\ln N(s)}{1+N(s,a)}}.
   $$
   [6]
2. Which child is selected? [1]
3. A child has $N=4$ and $Q=0.25$. A new simulation return is $G=1$. Compute the updated visit count and mean value. [2]
4. Compute the visit-count policy for counts $[30,10,0]$ with $\tau=1$. [2]
5. Compute a rollout return for rewards $[1,0,2]$ with $\gamma=0.5$. [1]

### Question 12: RL For Control Calculations [4]

1. A cartpole reward function gives $+1$ for each balanced time step. If it survives for three steps and $\gamma=0.99$, compute $G_0$ over those three rewards. [2]
2. A safety layer clips torque to the range $[-80,80]$ Nm. Compute the safe torque for an RL action of $120$ Nm. Then compute the torque if a normalized policy output $0.6$ is scaled by a maximum torque of $80$ Nm. [2]

