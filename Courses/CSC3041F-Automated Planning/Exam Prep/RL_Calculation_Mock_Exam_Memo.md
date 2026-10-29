---
tags:
  - automated-planning
---

# Reinforcement Learning Calculation Mock Exam: Marking Memo

This memo follows `RL_Calculation_Mock_Exam.md`.

---

## Question 1: Discounted Returns [12]

1. $G_0=3+0.5(-2)+0.5^2(4)+0.5^3(8)=3-1+1+1=4$. [3]
2. $G_1=-2+0.5(4)+0.5^2(8)=-2+2+2=2$. [2]
3. Infinite constant reward: $G=2/(1-0.8)=10$. [2]
4. $G_0=1+0.9+0.9^2=2.71$. [2]
5. Option B return is $8\gamma^2$. Need $8\gamma^2>5$, so $\gamma>\sqrt{5/8}\approx0.791$. [3]

## Question 2: Bellman Expectation And Optimality In A Small MDP [14]

1. $Q^\pi(s,a)=0.7[1+0.9V^\pi(s)]+0.3[5]=2.2+0.63V^\pi(s)$. [2]
2. $Q^\pi(s,b)=3$. [1]
3. $V^\pi(s)=0.6Q^\pi(s,a)+0.4Q^\pi(s,b)$  
   $=0.6(2.2+0.63V^\pi(s))+1.2=2.52+0.378V^\pi(s)$.  
   $0.622V^\pi(s)=2.52$, so $V^\pi(s)\approx4.05$. [4]
4. $Q^\pi(s,a)=2.2+0.63(4.05)\approx4.75$ and $Q^\pi(s,b)=3$. [2]
5. For $\mu(s)=a$, $V^\mu(s)=2.2+0.63V^\mu(s)$.  
   $0.37V^\mu(s)=2.2$, so $V^\mu(s)\approx5.95$. [3]
6. Since the $a$ fixed point is $\approx5.95>3$, $V^*(s)\approx5.95$ and the optimal action is $a$. [2]

## Question 3: Policy-Weighted Values, Advantages, And Action Probabilities [12]

1. $V^\pi(s)=0.2(2)+0.5(5)+0.3(-1)=0.4+2.5-0.3=2.6$. [3]
2. $A(a_1)=2-2.6=-0.6$, $A(a_2)=5-2.6=2.4$, $A(a_3)=-1-2.6=-3.6$. [3]
3. Greedy action $a_2$: $1-\varepsilon+\varepsilon/3=0.7+0.1=0.8$.  
   $a_1=0.1$, $a_3=0.1$. [3]
4. Sum $=7.389+148.413+0.368=156.170$.  
   $P(a_1)\approx0.047$, $P(a_2)\approx0.950$, $P(a_3)\approx0.002$. [3]

---

## Question 4: Value Iteration [14]

1. $V_1(A)=\max(2+0.8V_0(B),5+0.8V_0(T))=\max(2,5)=5$. [2]
2. $V_1(B)=\max(0.5[0+0.8V_0(A)]+0.5[4],1+0.8V_0(A))=\max(2,1)=2$. [3]
3. $V_2(A)=\max(2+0.8(2),5)=\max(3.6,5)=5$. [2]
4. $V_2(B)=\max(0.5[0+0.8(5)]+0.5[4],1+0.8(5))=\max(4,5)=5$. [3]
5. At $A$, greedy action is $y$. [1]
6. At $B$, greedy action is $y$. [1]
7. Residual $=\max(|5-5|,|5-2|)=3$. [2]

## Question 5: Policy Evaluation And Policy Improvement [12]

1. $V^\pi(A)=2+0.8V^\pi(B)$ and $V^\pi(B)=0.5[0+0.8V^\pi(A)]+0.5[4] =0.4V^\pi(A)+2$. [3]
2. Substitute: $V(A)=2+0.8(0.4V(A)+2)=3.6+0.32V(A)$.  
   $0.68V(A)=3.6$, so $V^\pi(A)\approx5.29$. [3]
3. $V^\pi(B)=0.4(5.29)+2\approx4.12$. [2]
4. $q(A,x)=2+0.8(4.12)\approx5.29$, $q(A,y)=5$. Improved action at $A$ is $x$. [2]
5. $q(B,x)\approx4.12$, $q(B,y)=1+0.8(5.29)\approx5.24$. Improved action at $B$ is $y$. [2]

---

## Question 6: Monte Carlo Prediction And Control [12]

1. First visit to $A$: $G=1+0.9(2)+0.9^2(-1)=1+1.8-0.81=1.99$. [2]
2. Visit to $B$: $G=2+0.9(-1)=1.1$. [2]
3. Second visit to $A$: $G=-1$. [1]
4. First-visit estimate for $V(A)$ from this episode is $1.99$. [1]
5. Every-visit estimate for $V(A)$ is $(1.99+(-1))/2=0.495$. [2]
6. $V(A)\leftarrow2+0.25(1.99-2)=1.9975$. [2]
7. Greedy actions are $R$ and $U$. Random part gives $0.2/3\approx0.0667$ each. Greedy part $0.8$ is split equally, so $P(L)=0.0667$, $P(R)=0.4667$, $P(U)=0.4667$. [2]

## Question 7: TD, N-Step TD, And Eligibility Traces [14]

1. Target $=2+0.9(4)=5.6$.  
   $\delta=5.6-6=-0.4$.  
   $V(s)\leftarrow6+0.2(-0.4)=5.92$. [4]
2. $G_t^{(3)}=1+0.5(2)+0.5^2(3)+0.5^3(10)=1+1+0.75+1.25=4$. [3]
3. Terminal target $=5$. $\delta=5-3=2$. Updated $V(s)=3+0.5(2)=4$. [3]
4. New traces: $e(A)=0.9(0.8)(1.0)=0.72$; $e(B)=0.9(0.8)(0.5)+1=1.36$.  
   Value increments: $\Delta V(A)=0.1(2)(0.72)=0.144$; $\Delta V(B)=0.1(2)(1.36)=0.272$. [4]

---

## Question 8: SARSA, Q-Learning, Expected SARSA, Epsilon-Greedy, And Softmax [16]

1. SARSA target $=1+0.8(4)=4.2$.  
   Updated $Q=2+0.5(4.2-2)=3.1$. [3]
2. Q-learning target $=1+0.8(6)=5.8$.  
   Updated $Q=2+0.5(5.8-2)=3.9$. [3]
3. Expected next value $=0.25(2)+0.75(6)=5$.  
   Target $=1+0.8(5)=5$.  
   Updated $Q=2+0.5(5-2)=3.5$. [3]
4. Greedy probability $=1-0.1+0.1/5=0.92$. Each non-greedy action has probability $0.1/5=0.02$. [2]
5. Sum $=2.718+7.389+20.085=30.192$.  
   Probabilities $\approx[0.090,0.245,0.665]$. [3]
6. Terminal target $=-2$. Updated $Q=5+0.4(-2-5)=2.2$. [2]

---

## Question 9: Function Approximation And DQN [14]

1. Prediction $\hat v=1(2)+(-1)(3)=-1$. Error $G-\hat v=5-(-1)=6$.  
   Update $w=(1,-1)+0.1(6)(2,3)=(1,-1)+(1.2,1.8)=(2.2,0.8)$. [4]
2. DQN target $y=2+0.9\max[4,1,6]=2+5.4=7.4$. [2]
3. Loss $=(7.4-5)^2=5.76$. [2]
4. Current prediction $Q_\theta=2\theta=4$. Error $y-Q=3$.  
   For $L=(y-2\theta)^2$, $\frac{dL}{d\theta}=-4(y-2\theta)=-12$.  
   $\theta\leftarrow2-0.1(-12)=3.2$. [4]
5. Online argmax is the second action because online values are $[2,5,4]$. Target-network value for that action is $1$. Double DQN target $=1+0.9(1)=1.9$. [2]

## Question 10: Policy Gradient, Actor-Critic, And PPO [14]

1. Update increment $=0.1(4)(0.5,-0.2)=(0.2,-0.08)$.  
   $\theta'=(1.2,0.92)$. [3]
2. Advantage with baseline $=G-b=4-1.5=2.5$.  
   Increment $=0.1(2.5)(0.5,-0.2)=(0.125,-0.05)$.  
   $\theta'=(1.125,0.95)$. [3]
3. $\delta=1+0.9(4)-3=1.6$. [2]
4. $r_t=0.3/0.2=1.5$. Clipped ratio $=1.2$.  
   $r_tA=3.0$, clipped term $=2.4$, contribution $=2.4$. [3]
5. Clipped ratio for $r_t=0.6$ is $0.8$.  
   $r_tA=0.6(-2)=-1.2$, clipped term $=0.8(-2)=-1.6$.  
   Minimum is $-1.6$. [3]

---

## Question 11: MCTS Calculations [12]

1. A: $0.50+1.4\sqrt{4.605/11}\approx0.50+1.4(0.647)=1.406$.  
   B: $0.70+1.4\sqrt{4.605/41}\approx0.70+1.4(0.335)=1.169$.  
   C: $0.40+1.4\sqrt{4.605/2}\approx0.40+1.4(1.517)=2.524$. [6]
2. Select C. [1]
3. $N\leftarrow5$. $Q\leftarrow0.25+(1-0.25)/5=0.40$. [2]
4. Counts sum to $40$, so policy is $[30/40,10/40,0/40]=[0.75,0.25,0]$. [2]
5. Return $=1+0.5(0)+0.5^2(2)=1.5$. [1]

## Question 12: RL For Control Calculations [4]

1. $G_0=1+0.99+0.99^2=2.9701$. [2]
2. Clip $120$ Nm to $80$ Nm. Normalized output $0.6$ scaled by $80$ Nm gives $48$ Nm. [2]

