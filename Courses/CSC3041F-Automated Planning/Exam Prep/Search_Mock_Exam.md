# Search Mock Exam

**Course**: CSC3041F Automated Planning  
**Topic coverage**: Search notes 01-10  
**Time**: 3 hours  
**Total**: 150 marks  

---

## Instructions

- Answer all questions.
- Show working for all numerical and tree-search questions.
- If a question asks for a justification, a one-word answer is not enough.
- Assume ties are broken alphabetically unless the question says otherwise.

---

## Section A: State-Space Search And Problem Formulation

### Question 1: Problem-Solving Agents And State Spaces [12]

1. Define AI search in the context of problem solving. [2]
2. List the four phases of the problem-solving agent framework. [4]
3. Distinguish a problem space from a problem instance. [2]
4. A two-room vacuum world has rooms `A` and `B`. Each room may be clean or dirty, and the robot may be in either room. Give a compact state representation and compute the number of possible states. [2]
5. Why is omitting the dirt status from the vacuum-world state representation a modelling error? [2]

### Question 2: Tree Search, Graph Search, Costs, And Goal States [10]

1. Explain the difference between tree search and graph search. [2]
2. What is an open list/frontier? [1]
3. What is a reached-state set, and why is it useful? [2]
4. In a two-room vacuum world, explain why both $(A,\text{clean},\text{clean})$ and $(B,\text{clean},\text{clean})$ can be goal states. [2]
5. A plan that takes 3 moves loses a queen worth 9. Another plan takes 5 moves and loses a bishop worth 3. If total cost is moves plus lost-piece value, which plan is cheaper? Show working. [3]

---

## Section B: Uninformed Search, DFS, And Iterative Deepening

### Question 3: BFS And Uniform-Cost Search [14]

Consider the graph below. The start is $S$ and the goal is $G$.

| Edge | Cost |
|---|---:|
| $S\to A$ | 2 |
| $S\to B$ | 1 |
| $A\to C$ | 2 |
| $A\to G$ | 5 |
| $B\to C$ | 1 |
| $B\to G$ | 8 |
| $C\to G$ | 2 |

Successors are generated alphabetically.

1. Which path can BFS return, and why is BFS appropriate only when step costs are equal? [3]
2. Run uniform-cost search and list the order in which nodes are popped from the priority queue until the goal is popped. [4]
3. What path and total cost does UCS return? [2]
4. Why is UCS cost-optimal when step costs are non-negative? [2]
5. Compare BFS and UCS in terms of the queue ordering they use. [2]
6. Why is greedy best-first search not an uninformed search algorithm? [1]

### Question 4: DFS, Depth-Limited Search, And Iterative Deepening [12]

1. Explain how DFS uses a stack/open list. [2]
2. Give one advantage and one disadvantage of DFS compared with BFS. [2]
3. What is a cutoff in depth-limited search? [2]
4. A search tree has branching factor $b=3$ and a shallowest solution depth $d=4$. Compute the number of nodes BFS generates through depth 4. [2]
5. For the same tree, compute the iterative-deepening expansion count using
   $$
   \sum_{i=0}^{d}(d+1-i)b^i.
   $$
   [2]
6. Why is iterative deepening still considered $O(b^d)$ despite repeated work? [1]
7. Is DFS cost-optimal in general? Explain. [1]

---

## Section C: Heuristic Search, A*, And Beam Search

### Question 5: Heuristics, Admissibility, And Consistency [14]

1. Define a heuristic function $h(n)$. [2]
2. Define admissibility. [2]
3. Define consistency. [2]
4. Why is Manhattan distance admissible for the sliding-tile puzzle? [2]
5. Compare misplaced-tiles and Manhattan-distance heuristics. Which is usually more informative, and why? [2]
6. Explain how problem relaxation can create an admissible heuristic. [2]
7. If $h_1$ and $h_2$ are admissible, is $h(n)=\max(h_1(n),h_2(n))$ admissible? Is $h(n)=h_1(n)+h_2(n)$ always admissible? [2]

### Question 6: A* Search Calculations [14]

The A* open list contains:

| Node | $g(n)$ | $h(n)$ |
|---|---:|---:|
| $N_1$ | 4 | 6 |
| $N_2$ | 7 | 2 |
| $N_3$ | 5 | 4 |
| $N_4$ | 3 | 8 |

Ties are broken by lower $h(n)$.

1. Compute $f(n)$ for each node. [4]
2. Which node is expanded next by A*? [2]
3. How does greedy best-first search choose differently from A*? [2]
4. Given true remaining costs $h^*(A)=5$, $h^*(B)=3$, $h^*(C)=4$ and heuristic estimates $h(A)=4$, $h(B)=3$, $h(C)=5$, is this heuristic admissible? Explain. [3]
5. Check consistency for an edge $X\to Y$ with cost $2$, $h(X)=4$, and $h(Y)=1$. [2]
6. What guarantee does A* have when the heuristic is admissible and graph-search details are handled correctly? [1]

### Question 7: A* Memory, Beam Search, And Delta Beam [10]

1. Why can A* use a large amount of memory? [2]
2. What is a closed list, and why does A* need one? [2]
3. Beam search has candidate scores:

   | Candidate | Score |
   |---|---:|
   | A | 2.0 |
   | B | 2.3 |
   | C | 2.8 |
   | D | 3.6 |
   | E | 5.0 |

   With beam width $k=2$, which candidates are kept? [1]
4. With delta-beam threshold $\delta=0.8$, which candidates are kept? [2]
5. What guarantee is usually lost when switching from A* to beam search? [1]
6. When can beam search be a practical choice despite weak guarantees? [2]

---

## Section D: Adversarial Search, Minimax, Alpha-Beta, And Evaluation

### Question 8: Minimax Search [14]

1. List the main components needed to define a two-player deterministic game for minimax. [4]
2. Why does minimax use $\min$ at opponent nodes? [2]
3. A MAX root has three actions. Each action leads to a MIN node:

   - $L$ has terminal children $[4,1,7]$.
   - $R$ has terminal children $[3,5]$.
   - $M$ has terminal children $[2,9]$.

   Compute the backed-up value of each action. [3]
4. Which action should MAX choose, and what is the minimax value? [2]
5. Why is minimax expensive for games such as chess? [2]
6. What is the minimax value of a terminal state? [1]

### Question 9: Alpha-Beta Pruning [14]

Consider a root MAX node with three MIN children $A$, $B$, and $C$, searched left to right:

- $A$ has leaves $[3,5]$.
- $B$ has leaves $[2,8,9]$.
- $C$ has leaves $[4,1,6]$.

1. Define $\alpha$ and $\beta$. [2]
2. Search the tree using alpha-beta pruning. Show the backed-up value of $A$ and the root $\alpha$ after $A$. [2]
3. At $B$, which leaves are pruned, if any? Explain using $\alpha$ and $\beta$. [3]
4. At $C$, which leaves are pruned, if any? Explain using $\alpha$ and $\beta$. [3]
5. What final action and value does MAX choose? [2]
6. Does alpha-beta pruning change the minimax value? [1]
7. Why does good move ordering improve alpha-beta pruning? [1]

### Question 10: Evaluation Functions And Cutoff Search [12]

1. Why are evaluation functions needed in deep games? [2]
2. What should an evaluation function return at a terminal win, draw, and loss if utilities are win $1$, draw $0.5$, loss $0$? [2]
3. A simple chess-like material evaluation uses:

   $$
   \text{queen}=9,\quad \text{rook}=5,\quad \text{bishop}=3,\quad \text{knight}=3,\quad \text{pawn}=1.
   $$

   White has 1 queen, 1 rook, 0 bishops, 2 knights, and 5 pawns.  
   Black has 0 queens, 2 rooks, 1 bishop, 1 knight, and 6 pawns.

   Compute material score $E=\text{White material}-\text{Black material}$. [3]
4. A state category historically leads to win $50\%$, draw $30\%$, loss $20\%$. Using utilities win $1$, draw $0.5$, loss $0$, compute the expected-value evaluation. [2]
5. What is the horizon effect? [2]
6. Give one reason a material-only chess evaluation can fail. [1]

---

## Section E: Multiplayer Search And MCTS

### Question 11: Multiplayer Minimax [10]

1. Why are utility vectors needed in multiplayer games? [2]
2. In max-n search, how is a child selected at player $B$'s turn? [2]
3. At a $B$ node, the children have utility vectors:

   $$
   X=(4,2,1),\quad Y=(2,5,0),\quad Z=(3,4,6).
   $$

   Which child does player $B$ choose under selfish max-n backup? [2]
4. For a three-player game, check whether each vector satisfies $K=7$: $(2,3,2)$ and $(2,3,1)$. [2]
5. Why can hardcoded cooperation or fixed alliances be problematic in multiplayer search? [2]

### Question 12: Monte Carlo Tree Search [14]

1. List and briefly describe the four phases of MCTS. [4]
2. How does pure Monte Carlo search differ from MCTS? [2]
3. Write the UCB-style MCTS selection score. [2]
4. A parent node has $N(s)=50$ visits and $c_{\mathrm{ucb}}=1.4$.

   Child A has $Q(s,A)=0.60$ and $N(s,A)=10$.  
   Child B has $Q(s,B)=0.50$ and $N(s,B)=1$.

   Compute the UCB score for both children and say which one is selected. Use $\ln(50)\approx3.912$. [3]
5. A child currently has $N=10$ and $Q=0.60$. A new simulation return is $G=1$. Compute the updated visit count and mean value. [2]
6. What happens when the exploration constant is set to $0$? [1]

