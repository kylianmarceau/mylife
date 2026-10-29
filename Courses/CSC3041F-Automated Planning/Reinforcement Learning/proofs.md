---
tags:
  - automated-planning
---

# Proofs

These are the three proof and derivation patterns from the reinforcement learning source notes:

- Bellman equation derivation
- Bellman optimality derivation
- Bellman optimality contraction and convergence

Main source note sections:

- `03_Value_Functions.md`: Bellman equation derivation
- `04_Optimal_Value_Functions.md`: Bellman optimality derivation
- `05_Value_Iteration.md`: convergence and contraction

---

## Contents

- [[#1. Bellman Equation Derivation|1. Bellman Equation Derivation]]
- [[#2. Bellman Optimality Derivation|2. Bellman Optimality Derivation]]
- [[#3. Convergence Contraction Proof|3. Convergence Contraction Proof]]

---

## 1. Bellman Equation Derivation

### Target equation

For a fixed policy $\pi$, the Bellman expectation equation says:

$$
V_{\pi}(s)=\mathbb{E}_{a\sim\pi(\cdot\mid s),\,s'\sim P(\cdot\mid s,a)}\!\left[R(s,a)+\gamma V_{\pi}(s')\right]
$$

In words:

$$
\text{current value}=\text{immediate reward}+\gamma\cdot\text{future value}
$$

### Proof

Start with the definition of the state-value function:

$$
V_{\pi}(s)=\mathbb{E}_{\pi}[G_t\mid S_t=s]
$$

Use the return split from the notes:

$$
G_t=R_{t+1}+\gamma G_{t+1}
$$

Substitute this into the value-function definition:

$$
V_{\pi}(s)=\mathbb{E}_{\pi}[R_{t+1}+\gamma G_{t+1}\mid S_t=s]
$$

After the agent takes an action from policy $\pi$ and moves to the next state $s'$, the expected future return from $s'$ is the value of that next state:

$$
\mathbb{E}_{\pi}[G_{t+1}\mid S_{t+1}=s']=V_{\pi}(s')
$$

So:

$$
V_{\pi}(s)=\mathbb{E}_{\pi}[R(s,a)+\gamma V_{\pi}(s')]
$$

Writing out the stochastic policy and stochastic transition explicitly gives:

$$
V_{\pi}(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_{\pi}(s')]
$$

The deterministic version from the notes is:

$$
V_{\pi}(s)=R(s,\pi(s))+\gamma V_{\pi}(s')
$$

The key move is replacing the rest of the return, $G_{t+1}$, with the value function at the next state, $V_{\pi}(s')$.

---

## 2. Bellman Optimality Derivation

### Target equation

The stochastic Bellman optimality equation is:

$$
V^*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')]
$$

It is also true that:

$$
V^*(s)=\max_a Q^*(s,a)
$$

### Proof

Start with the definition of optimal value:

$$
V^*(s)=\max_{\pi}V_{\pi}(s)
$$

Replace $V_{\pi}(s)$ with the expected return under policy $\pi$:

$$
V^*(s)=\max_{\pi}\mathbb{E}_{\pi}[G_t\mid S_t=s]
$$

Use the Bellman return split:

$$
G_t=R_{t+1}+\gamma G_{t+1}
$$

For optimal control, choose the best first action, then behave optimally afterward:

$$
V^*(s)=\max_a\mathbb{E}[R_{t+1}+\gamma G_{t+1}\mid S_t=s,A_t=a]
$$

If behavior after the first action is optimal, the expected future return from the next state is $V^*(S_{t+1})$:

$$
V^*(s)=\max_a\mathbb{E}[R_{t+1}+\gamma V^*(S_{t+1})\mid S_t=s,A_t=a]
$$

Writing out the expectation over possible next states and rewards gives:

$$
V^*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')]
$$

Because the optimal action-value function scores taking action $a$ first and then acting optimally:

$$
Q^*(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')]
$$

Therefore:

$$
V^*(s)=\max_a Q^*(s,a)
$$

The key move from the notes is optimizing over the first action separately, then assuming optimal behavior afterward.

---

## 3. Convergence Contraction Proof

### Target equation

The Bellman optimality operator is a contraction when $0\le\gamma<1$:

$$
\|\mathcal{T}V-\mathcal{T}U\|_{\infty}\le \gamma\|V-U\|_{\infty}
$$

where:

$$
\|V-U\|_{\infty}=\max_s |V(s)-U(s)|
$$

### Bellman optimality operator

From the value-iteration notes:

$$
(\mathcal{T}V)(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]
$$

and:

$$
(\mathcal{T}U)(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma U(s')]
$$

### Proof

Assume a finite MDP and $0\le\gamma<1$. The proof uses:

$$
|\max_a x_a-\max_a y_a|\le \max_a |x_a-y_a|
$$

For a fixed state $s$, compare the two Bellman backups:

$$
\begin{aligned}
|(\mathcal{T}V)(s)-(\mathcal{T}U)(s)|
&=
\left|
\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]
-
\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma U(s')]
\right|\\
&\le
\max_a
\left|
\sum_{s',r}p(s',r\mid s,a)\left([r+\gamma V(s')]-[r+\gamma U(s')]\right)
\right|\\
&=
\max_a
\left|
\sum_{s',r}p(s',r\mid s,a)\gamma [V(s')-U(s')]
\right|\\
&\le
\gamma\max_a
\sum_{s',r}p(s',r\mid s,a)|V(s')-U(s')|\\
&\le
\gamma\|V-U\|_{\infty}
\end{aligned}
$$

The last step works because $\|V-U\|_{\infty}$ is the largest possible state-value difference, and the transition probabilities sum to $1$.

Since this is true for every state $s$, take the maximum over states:

$$
\max_s |(\mathcal{T}V)(s)-(\mathcal{T}U)(s)|
\le
\gamma\|V-U\|_{\infty}
$$

So:

$$
\|\mathcal{T}V-\mathcal{T}U\|_{\infty}\le \gamma\|V-U\|_{\infty}
$$

Because $0\le\gamma<1$, applying $\mathcal{T}$ shrinks the largest difference between value functions. Repeated Bellman optimality updates therefore converge to a unique fixed point, and that fixed point is $V^*$.

In value iteration, this is why:

$$
V_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_k(s')]
$$

converges as $k$ increases. As the notes emphasize, $k$ is the iteration number, not the environment timestep.
