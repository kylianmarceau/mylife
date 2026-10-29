---
tags:
  - automated-planning
---

# Search Mock Exam: Marking Memo

This memo follows `Search_Mock_Exam.md`. Award equivalent marks for correct reasoning and equivalent notation.

---

## Question 1: Problem-Solving Agents And State Spaces [12]

1. AI search is systematic exploration of states, paths, actions, or assignments to find a goal or answer. [2]
2. Goal formulation, problem formulation, search, execution. [4]
3. Problem space is the general state space/actions/transition model; problem instance adds concrete initial state, goal test/state, and usually costs. [2]
4. Example state: $(\text{robot location}, A\text{-status}, B\text{-status})$. There are $2$ robot locations and $2^2$ dirt configurations, so $2\cdot4=8$ states. [2]
5. Dirt status affects future actions, goal testing, and transition/reward consequences; without it the state is incomplete and cannot predict the problem dynamics. [2]

## Question 2: Tree Search, Graph Search, Costs, And Goal States [10]

1. Tree search explores paths and may duplicate the same state; graph search tracks reached states to avoid repeated work/cycles. [2]
2. The open list/frontier is the set of generated but not yet expanded nodes. [1]
3. A reached set stores states already seen; it prevents redundant expansion and cycles. [2]
4. The goal is that both rooms are clean; the robot location no longer matters. [2]
5. Queen plan cost $=3+9=12$. Bishop plan cost $=5+3=8$. The bishop-loss plan is cheaper. [3]

---

## Question 3: BFS And Uniform-Cost Search [14]

1. BFS can return a depth-2 path such as $S\to A\to G$ under alphabetical expansion. BFS is appropriate for optimality only when all step costs are equal because it minimizes depth/action count, not path cost. [3]
2. UCS pop order with cost updates and alphabetical tie-breaking: $S(0)$, $B(1)$, $A(2)$, $C(2)$, $G(4)$. [4]
3. UCS returns $S\to B\to C\to G$ with cost $1+1+2=4$. [2]
4. UCS always expands the lowest path-cost frontier node first; with non-negative costs, the first time a goal is popped its path cost is optimal. [2]
5. BFS uses FIFO/depth ordering; UCS uses a priority queue ordered by cumulative path cost $g(n)$. [2]
6. Greedy best-first uses heuristic information $h(n)$, so it is informed. [1]

## Question 4: DFS, Depth-Limited Search, And Iterative Deepening [12]

1. DFS uses a LIFO stack: the most recently generated node is expanded next. [2]
2. Advantage: low memory, often $O(bm)$ path storage. Disadvantage: can get stuck deep, is not complete in infinite spaces, and is not generally optimal. Any one each. [2]
3. A cutoff reports that the depth limit was reached before proving failure or finding a solution below that branch. [2]
4. BFS through depth 4: $1+3+9+27+81=121$. [2]
5. IDS count: $5(1)+4(3)+3(9)+2(27)+1(81)=5+12+27+54+81=179$. [2]
6. The deepest level dominates the geometric sum, so repeated shallow work is lower-order. [1]
7. No. DFS can return a deeper or higher-cost solution before a cheaper one. [1]

---

## Question 5: Heuristics, Admissibility, And Consistency [14]

1. $h(n)$ estimates the remaining cost from node $n$ to a goal. [2]
2. Admissible means $0\le h(n)\le h^*(n)$ for all nodes, so it never overestimates true remaining cost. [2]
3. Consistent means $h(n)\le c(n,n')+h(n')$ for every edge $n\to n'$, and $h(\text{goal})=0$. [2]
4. Each tile must move at least its Manhattan distance in a sliding-tile puzzle, ignoring blocking, so the estimate is a lower bound. [2]
5. Misplaced tiles counts incorrect tiles; Manhattan sums grid distances. Manhattan is usually more informative because it measures how far tiles are, not just whether they are wrong. [2]
6. Relaxing constraints makes the problem easier; the optimal cost of the easier problem is a lower bound on the original problem. [2]
7. $\max(h_1,h_2)$ is admissible. $h_1+h_2$ is not always admissible because it may double-count cost unless the heuristics are additive over disjoint parts. [2]

## Question 6: A* Search Calculations [14]

1. $f(N_1)=10$, $f(N_2)=9$, $f(N_3)=9$, $f(N_4)=11$. [4]
2. $N_2$ is expanded because it ties on $f=9$ with $N_3$ but has lower $h$ value. [2]
3. Greedy best-first uses lowest $h(n)$ only; A* uses $f(n)=g(n)+h(n)$. [2]
4. Not admissible because $h(C)=5>h^*(C)=4$. $A$ and $B$ are acceptable, but one overestimate is enough to break admissibility. [3]
5. Consistency requires $h(X)\le2+h(Y)=3$. Since $4\le3$ is false, it is inconsistent. [2]
6. A* returns an optimal solution when conditions are satisfied. [1]

## Question 7: A* Memory, Beam Search, And Delta Beam [10]

1. A* stores the frontier and usually a closed list/reached states; these can grow exponentially with depth. [2]
2. A closed list stores expanded states to avoid re-expansion and loops; it is important for graph search and duplicate handling. [2]
3. Beam width $k=2$ keeps A and B. [1]
4. Best score is $2.0$; keep candidates with score $\le2.8$, so A, B, and C. [2]
5. Usually completeness and/or optimality. [1]
6. Beam search is practical when memory/time are tight, the space is huge, and a good approximate solution is acceptable. [2]

---

## Question 8: Minimax Search [14]

1. Initial state, player-to-move function, actions, transition/result model, terminal test, and utility function. Any four core components. [4]
2. Opponent is assumed rational and adversarial, choosing outcomes worst for MAX. [2]
3. $L=\min(4,1,7)=1$; $R=\min(3,5)=3$; $M=\min(2,9)=2$. [3]
4. MAX chooses $R$ and the minimax value is $3$. [2]
5. Game trees have huge branching factors and depths; full minimax expansion is infeasible. [2]
6. The terminal state's utility value. [1]

## Question 9: Alpha-Beta Pruning [14]

1. $\alpha$ is the best value MAX can guarantee so far along the path; $\beta$ is the best value MIN can guarantee so far. [2]
2. $A=\min(3,5)=3$. Root $\alpha$ becomes $3$. [2]
3. At $B$, first leaf gives $\beta=2$. Since $\beta\le\alpha$ ($2\le3$), prune leaves $8$ and $9$. [3]
4. At $C$, first leaf gives $\beta=4$, no cutoff. Second leaf gives $\beta=1$. Since $1\le3$, prune leaf $6$. [3]
5. MAX chooses $A$ with value $3$. [2]
6. No. It prunes branches that cannot affect the minimax decision. [1]
7. Good ordering finds strong bounds earlier, causing more cutoffs. [1]

## Question 10: Evaluation Functions And Cutoff Search [12]

1. Full game trees are too deep/large, so cutoff search needs approximate values for non-terminal states. [2]
2. Win $=1$, draw $=0.5$, loss $=0$. [2]
3. White material $=9+5+0+6+5=25$. Black material $=0+10+3+3+6=22$. $E=25-22=3$. [3]
4. Expected value $=0.5(1)+0.3(0.5)+0.2(0)=0.65$. [2]
5. Horizon effect: cutoff hides important events just beyond the search depth, causing misleading evaluations. [2]
6. Material-only evaluation ignores tactics, king safety, forced captures, positional compensation, threats, or checkmate patterns. [1]

---

## Question 11: Multiplayer Minimax [10]

1. Each player can have a different payoff, so a scalar utility for MAX is not enough. [2]
2. At a $B$ node, choose the child maximizing the $B$ component of the utility vector. [2]
3. Player $B$ chooses $Y=(2,5,0)$ because the second component is highest. [2]
4. $(2,3,2)$ sums to $7$, so it satisfies $K=7$. $(2,3,1)$ sums to $6$, so it does not. [2]
5. Alliances can shift, may not reflect rational incentives, and can make the model brittle or wrong. [2]

## Question 12: Monte Carlo Tree Search [14]

1. Selection: descend using a selection score. Expansion: add a new child. Simulation/playout: sample a rollout outcome. Backpropagation: update visits and values along the path. [4]
2. Pure Monte Carlo samples immediate moves without maintaining a deep growing tree; MCTS selectively grows and reuses a search tree. [2]
3. $\operatorname{UCB}(s,a)=Q(s,a)+c_{\mathrm{ucb}}\sqrt{\ln N(s)/(1+N(s,a))}$. Equivalent course-note variants are acceptable. [2]
4. A: $0.60+1.4\sqrt{3.912/11}\approx0.60+1.4(0.596)=1.43$.  
   B: $0.50+1.4\sqrt{3.912/2}\approx0.50+1.4(1.399)=2.46$.  
   Select B. [3]
5. $N\leftarrow11$. $Q\leftarrow0.60+(1-0.60)/11\approx0.636$. [2]
6. The exploration bonus vanishes and selection becomes greedy on current value estimates. [1]

