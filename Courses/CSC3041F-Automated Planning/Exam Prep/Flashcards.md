---
tags:
  - automated-planning
---

# CSC3041F Automated Planning Flashcards

## State Space Search

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-01-State-Space-Search

What is search in AI?::Systematic exploration of possible choices, paths, states, or assignments until a goal or query is satisfied.
When is AI search useful?::When the exact action sequence is not known in advance and the agent must explore possible actions.
What three broad search problem types are introduced in the course?::Single-agent path finding, game playing, and constraint-satisfaction problems.
What is goal formulation?::Choosing what counts as success so the agent can restrict the objectives and actions under consideration.
What is problem formulation?::Choosing the states, actions, transition model, costs, initial state, and goal test for a search problem.
What are the four phases of the problem-solving agent framework?::Goal formulation, problem formulation, search, and execution.
When is open-loop execution reasonable?::When the environment is fully observable, deterministic, and known, so the planned action sequence should behave as expected.
What is a closed-loop system?::A plan-execution approach that monitors percepts and reacts if the world changes.
What is a state?::One complete configuration of the problem, usually represented by variables or features.
What is a state space?::The set $S$ of all possible states in a problem.
What is the state tuple notation from the notes?::$s=(v_1,v_2,\ldots,v_n), s\in S$.
What is an action in state-space search?::A possible move or operation that can transform one state into another.
What is a transition model?::A rule or function describing the state reached after applying an action in a state.
What is the deterministic transition-model notation?::$T:S\times A\to S$.
What is a problem space?::The state space plus the actions plus the transition model.
What is a problem instance?::A concrete problem space with an initial state, goal state or goal test, and usually an action cost function.
What is the problem-instance formula?::Problem instance equals problem space plus initial state plus goal state(s) plus action cost function.
Why do action costs matter?::They let search prefer the cheapest solution, not merely the shortest sequence of actions.
What is a path?::A sequence of actions through the state space.
What is a solution?::A path from the initial state to a goal state.
What is an optimal solution?::A solution with the lowest path cost among all solutions.
What is path cost?::The sum of action costs along a complete path.
How does a graph represent a search problem?::Nodes represent states and edges represent actions or transitions.
How does tree search differ from graph search?::Tree search represents paths and can duplicate states, while graph search tracks reached states to avoid repeated work and cycles.
What is the main memory trade-off of graph search?::It avoids redundancy but must store reached-state history.
What is the naive tic-tac-toe state count?::$3^9=19,683$ board assignments.
Why is chess used as a warning about state-space size?::Its possible games are astronomically large, so naive exhaustive storage or search is infeasible.
What is the vacuum-world state-count formula for $n$ cells?::$n\cdot 2^n$, from $n$ robot positions and $2^n$ clean/dirty configurations.
What must a vacuum-world state include?::The robot location and the clean or dirty status of every cell.
Why is Sokoban a planning problem?::The agent must reason about its own movement plus box positions and spatial constraints.
What is a common mistake in state representation?::Representing only the agent location and omitting variables needed to predict future transitions.

## Uninformed Search

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-02-Uninformed-Search

What is uninformed search?::Search that does not use heuristic information about closeness to the goal.
What is a search tree?::A tree representation of paths explored from the initial state.
What is the root of a search tree?::The first node, corresponding to the initial state.
What is expansion?::Generating a node's children by applying available actions and the transition model.
What is successor generation?::Applying legal actions to compute the child states reachable in one step.
What is the openlist or frontier?::The data structure containing generated nodes waiting to be expanded.
What is a reached, history, or closed list?::Memory of states already reached or expanded.
What is a redundant path?::A path that reaches a state already reachable by another path.
What is a cycle?::A path that returns to a previously visited state.
What is the generic search loop?::Initialize the frontier, choose a node, test for a goal, expand it, add useful children, and record reached states if using graph search.
What is the main benefit of graph search over tree-like search?::It avoids redundant paths and cycles.
What extra cost does graph search pay?::It requires explicit memory for reached states.
What is completeness?::A guarantee that the algorithm finds a solution if one exists.
What is cost optimality?::A guarantee that the algorithm returns a lowest-cost solution.
What is time complexity in search?::The amount of work, often measured by the number of states or actions explored.
What is space complexity in search?::The maximum number of nodes or states the algorithm must store.
How does BFS order the frontier?::It uses a FIFO queue and expands all nodes at a shallower depth before deeper nodes.
When is BFS cost-optimal?::When all action costs are equal.
What is BFS complete under the usual finite-branching assumption?::Yes, if every node has finitely many children and a solution exists at finite depth.
What is the BFS time and space complexity in terms of branching factor $b$ and solution depth $d$?::$O(b^d)$ time and $O(b^d)$ space.
How does UCS order the frontier?::It expands nodes by increasing cumulative path cost.
What is the UCS evaluation function?::$f(n)=\mathrm{path\_cum\_cost}(n)$.
When is UCS complete and cost-optimal?::When step costs are positive and there are no zero-cost traps.
What is the UCS complexity given in the notes?::$O(b^{1+\lfloor C/c\rfloor})$, where $C$ is optimal solution cost and $c$ is the smallest positive step cost.
Why is UCS cost-optimal?::The first goal popped from the priority queue cannot be more expensive than any waiting path.
What is best-first search?::A framework that expands the node judged best by an evaluation function.
Why is greedy best-first search not uninformed?::It uses a heuristic such as distance to the goal.
What is the key difference between BFS and UCS?::BFS prioritizes shallowest depth, while UCS prioritizes cheapest cumulative path cost.

## Depth-First Search And Iterative Deepening

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-03-Depth-First-Search-And-Iterative-Deepening

What is depth-first search?::A search algorithm that expands the deepest node currently in the frontier.
What data structure is normally used for DFS?::A LIFO stack.
How can DFS be viewed as best-first search?::Use $f(n)=-\mathrm{depth}(n)$ so deeper nodes are selected first.
Why is DFS memory efficient compared with BFS?::It stores the current path plus unexpanded siblings instead of an entire frontier level.
What is tree-like DFS?::DFS without reached-state checking.
What is graph DFS?::DFS with reached-state checking to avoid repeated states.
Is DFS generally complete?::No; it can fail in infinite spaces or cyclic tree search.
Is DFS cost-optimal?::No; it returns the first solution found by its traversal order.
What is DFS time complexity?::$O(b^m)$, where $m$ is maximum depth.
What is tree-like DFS space complexity?::$O(bm)$.
What is depth-limited search?::DFS with a maximum depth limit $l$.
What does cutoff mean in depth-limited search?::The depth limit stopped exploration before failure could be proved.
What are depth-limited search time and space complexities?::$O(b^l)$ time and $O(bl)$ space.
What risk comes from choosing a depth limit that is too small?::A real solution may exist deeper than the limit and be missed.
What is iterative deepening search?::Repeated depth-limited DFS with limits $0,1,2,\ldots$ until a solution is found.
Why does IDS avoid guessing the correct depth limit?::It gradually increases the depth limit until the shallowest solution depth is reached.
What are IDS time and space complexities when the solution depth is $d$?::$O(b^d)$ time and $O(bd)$ space.
Why does IDS still have $O(b^d)$ time despite repeating nodes?::In exponential trees, the deepest level dominates the total node generation.
When is IDS cost-optimal?::When all action costs are equal, because it finds the shallowest solution first.
What is the difference between $m$ and $d$?::$m$ is maximum search depth; $d$ is depth of the shallowest solution.
Why does child ordering matter in DFS?::The last child pushed onto the stack is expanded first.
Do depth limits remove cycles?::No; they prevent infinite descent but cyclic paths can still be repeated.

## Heuristic Search, A*, And Beam Search

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-04-Heuristic-Search-Astar-And-Beam

What is a heuristic?::A function estimating the remaining cost from a node to a goal.
What is $h^*(n)$?::The true lowest possible cost from node $n$ to a goal.
What is $h(n)$?::A cheaply computed estimate of $h^*(n)$.
What is the heuristic function type used in the notes?::$h:S\to\mathbb{R}_{\ge 0}$.
What is an admissible heuristic?::A heuristic that never overestimates the true cheapest remaining cost.
What is the admissibility inequality?::$h(n)\le h^*(n)$ for every node.
What is a consistent heuristic?::A heuristic whose estimate cannot drop by more than the cost of taking one action.
What is the consistency inequality?::$h(n)\le c(n,a,n')+h(n')$ for every transition.
How are admissibility and consistency related?::Consistency is stronger; with goal heuristic zero, consistency implies admissibility.
What is the n-puzzle?::A sliding-tile puzzle with numbered tiles and one blank square.
What is the 8-puzzle total arrangement count?::$9!=362,880$.
How many 8-puzzle arrangements are reachable from one parity class?::$9!/2=181,440$.
Why are heuristics crucial for the 15-puzzle?::Even one parity class, $15!/2$, is too large for naive exhaustive search.
What is the misplaced-tile heuristic?::The number of tiles not in their goal positions.
What is Manhattan distance in the n-puzzle?::The sum over tiles of horizontal plus vertical distance from current position to goal position.
What is Gaschnig distance?::A heuristic from a relaxed puzzle where tiles may move into the blank position from anywhere.
How does relaxation create admissible heuristics?::It removes constraints, so the relaxed problem can only be cheaper than or equal to the original.
Why does a relaxed problem form a supergraph?::Extra transitions are allowed, creating possible shortcuts.
What is a common admissible way to combine multiple admissible heuristics?::Use the maximum, because the max of lower bounds is still a lower bound and is more informative.
Why is the source slide's minimum combination less useful?::It preserves admissibility but usually chooses the weakest estimate.
What is A* search?::Informed best-first search using $f(n)=g(n)+h(n)$.
What is $g(n)$ in A*?::The cost from the initial state to node $n$.
What is $f(n)$ in A*?::The estimated total solution cost through node $n$.
How does greedy best-first search score nodes?::It uses $f(n)=h(n)$ and ignores accumulated path cost.
When is A* complete and optimal on finite spaces?::When the heuristic is admissible and consistent.
What is beam search?::A memory-limited search that sorts candidates by score and keeps only the best $k$.
What is beam width?::The number $k$ of nodes retained after pruning.
What guarantees does beam search lose?::Completeness and optimality.
What is approximate beam-search space complexity?::$O(km)$.
Why can beam search miss a valid solution?::It may discard the only node that leads to a goal.

## A* Memory Usage And Beam Search

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-05-Astar-Memory-And-Beam-Search

What is the main limitation of A* emphasized in Lecture 5?::Memory use.
What does A* store that causes memory growth?::The openlist/frontier and the closed or reached list.
What is A* space complexity?::$O(b^d)$.
Why does A* need a closed list?::To avoid cycles and redundant work by remembering reached or expanded states.
What is a reference count?::A bookkeeping count of how many future references to a stored node are still needed.
How can reference counts save memory?::A node can be deleted once its reference count reaches zero.
What cost do reference counts add?::Extra bookkeeping overhead.
What is beam search's basic two-step procedure?::Sort candidates by score, then keep only the top $k$.
What is the grid example's heuristic for beam search?::Manhattan distance from the current coordinate to the goal.
What is a duplicate-handling issue in beam search?::The same state may be reached from multiple predecessors and needs a policy for duplicates.
What is delta-beam search?::Beam search that keeps all nodes within a chosen score distance of the best node.
What is the delta-beam keep rule?::Keep $n$ if $f(n)\le f(n_{\mathrm{best}})+\delta$.
How does delta beam differ from traditional beam search?::Traditional beam keeps exactly $k$ nodes; delta beam keeps a variable number within a threshold.
What is the main risk of delta beam?::Memory use is variable and can exceed expectations.
When is beam search practical despite weak guarantees?::When A* is too memory-heavy and an approximate or good-enough solution is acceptable.

## Adversarial Search And Minimax

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-06-Adversarial-Search-And-Minimax

What is adversarial search?::Search in environments containing agents with conflicting goals.
Why are games different from single-agent pathfinding?::Another agent chooses actions too, so successor states depend on opponent decisions.
What is a game tree?::A search tree of possible moves by all players from a game state.
What game properties does basic minimax assume?::Deterministic, two-player, turn-taking, perfect-information, zero-sum games.
What is MAX?::The player whose utility the algorithm tries to maximize.
What is MIN?::The opponent modeled as minimizing MAX's utility.
What is a terminal state?::A state where the game is over.
What is a utility function in minimax?::A function assigning a numerical payoff to a terminal state.
What functions define a formal game for minimax?::Initial state, ToMove, Actions, Result, Is-terminal, and Utility.
What is ToMove(s)?::A function returning whose turn it is in state $s$.
What is Actions(s)?::The legal moves available in state $s$.
What is Result(s,a)?::The state reached after action $a$ is applied in state $s$.
What is a complete game tree?::A tree following every legal move sequence until terminal states.
What is a minimax value?::The utility of a state assuming both players play optimally from that state onward.
What is the minimax value at a terminal state?::$\mathrm{Utility}(s,\mathrm{MAX})$.
What is the minimax recurrence at a MAX node?::$\mathrm{minimax}(s)=\max_a\mathrm{minimax}(\mathrm{Result}(s,a))$.
What is the minimax recurrence at a MIN node?::$\mathrm{minimax}(s)=\min_a\mathrm{minimax}(\mathrm{Result}(s,a))$.
How are minimax values propagated?::Terminal values are backed up; MAX chooses maximum children and MIN chooses minimum children.
What is minimax time complexity?::$O(b^m)$.
What is minimax space complexity with depth-first implementation?::$O(bm)$.
When is minimax optimal?::For finite deterministic two-player zero-sum perfect-information games with a correct utility function and optimal opponent.
Why can minimax be too conservative?::It assumes the opponent always plays optimally and may ignore chances to exploit weak play.
What is a common mistake with MIN?::Thinking MIN minimizes a separate scalar rather than minimizing MAX's utility in two-player zero-sum minimax.

## Multiplayer Minimax

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-07-Multiplayer-Minimax

Why does two-player scalar minimax not directly handle multiplayer games?::More than two players can have different payoffs, so one scalar is usually insufficient.
What is a utility vector?::A vector giving one utility component per player, such as $[V_A,V_B,V_C]$.
What is a selfish agent in multiplayer game search?::An agent that chooses actions only to maximize its own utility component.
What is max-n backup?::A multiplayer minimax-style backup where the player to move chooses the child maximizing its own utility component.
At an A node in max-n, how is the child selected?::Choose the child vector with the highest A component.
At a B node in max-n, how is the child selected?::Choose the child vector with the highest B component.
What is cooperation in multiplayer search?::A situation where one or more agents care about another agent's utility as well as their own.
What is a shifting alliance?::A cooperation structure whose weights change depending on the game state.
How can cooperation be modeled simply?::By combining or weighting utilities, such as summing the scores of cooperating players.
What is the risk of hardcoded alliances?::They cannot represent alliances that change during the game.
What is a K-sum game?::A game where the sum of all players' terminal utilities equals a constant $K$.
What is the K-sum formula for three players?::$V_A+V_B+V_C=K$.
What is zero-sum as a special K-sum case?::A K-sum game with $K=0$.
What is the exam-level point of K-sum backup with cooperation?::Multiplayer games need vector utilities plus explicit assumptions about competition or cooperation.
Does multiplayer minimax remove exponential complexity?::No; time complexity remains $O(b^m)$.
Why is pruning still motivated after multiplayer minimax?::The branching and depth problem remains exponential.
What is a common multiplayer minimax mistake?::Using scalar minimax unchanged for games with more than two players.
Why must cooperation be specified mathematically?::Without a utility transform or weights, "cooperation" does not define what action a player should prefer.

## Alpha-Beta Search

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-08-Alpha-Beta-Search

What is alpha-beta pruning?::A minimax optimization that skips branches that cannot affect the final decision.
What is pruning?::Discarding part of the search tree without evaluating every leaf.
Does alpha-beta pruning change the minimax answer?::No; it returns the same decision as minimax while avoiding irrelevant work.
What does alpha represent?::The best value MAX can guarantee so far along the current search path.
What does beta represent?::The best value MIN can guarantee so far along the current search path.
What are the initial alpha and beta values?::$\alpha=-\infty$ and $\beta=+\infty$.
At which nodes is alpha updated?::MAX nodes.
At which nodes is beta updated?::MIN nodes.
What is the alpha update rule?::$\alpha\leftarrow\max(\alpha,v)$.
What is the beta update rule?::$\beta\leftarrow\min(\beta,v)$.
What is the cutoff condition at a MAX node?::Stop searching remaining children when $v\ge\beta$.
What is the cutoff condition at a MIN node?::Stop searching remaining children when $v\le\alpha$.
Why can a MIN node prune when $v\le\alpha$?::MAX already has an option at least as good elsewhere.
Why can a MAX node prune when $v\ge\beta$?::MIN already has an option that keeps MAX to beta or less elsewhere.
What is move ordering?::The order in which successor states are searched.
Why does move ordering matter for alpha-beta?::Good early moves create tighter bounds and allow more pruning.
What is alpha-beta worst-case time complexity?::$O(b^m)$.
What can alpha-beta approach with perfect move ordering?::$O(b^{m/2})$.
What practical move ordering heuristic is mentioned for chess-style games?::Search captures, then threats, then forward moves, then backward moves.
What is a common alpha-beta mistake?::Updating alpha at MIN nodes or beta at MAX nodes.
What does the source's "alpha-delta" label refer to?::It is the standard alpha-beta algorithm despite the label.

## Evaluation Functions

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-09-Evaluation-Functions

What is an evaluation function?::A heuristic function estimating the payoff of a non-terminal game state.
Why are evaluation functions needed in game search?::Searching all the way to terminal states is often impossible even with alpha-beta pruning.
What is a cutoff test?::A test deciding whether search should stop before a terminal state and use EVAL.
How does depth-limited minimax extend the terminal base case?::It returns Utility at terminal states and EVAL at cutoff states.
What should EVAL return at terminal states?::It should match the terminal utility.
What are the main requirements of a good EVAL?::It should be cheap, correlated with winning, and assign higher scores to better prospects.
What does "chance" mean in deterministic perfect-information evaluation?::Uncertainty caused by limited search, not randomness in the game.
What is a feature in game evaluation?::A measurable property of a game state used by EVAL.
What is a weighted evaluation function?::A sum of weighted feature values.
What is the weighted EVAL formula?::$\mathrm{EVAL}(s)=w_1f_1(s)+w_2f_2(s)+\cdots+w_kf_k(s)$.
What chess-like features might an evaluator use?::Material, pawn location, king safety, piece strength, and endgame category.
Why can independent feature weights be an approximation?::Feature value can depend on interactions such as king safety or endgame type.
What is probability-style evaluation?::Estimating expected utility from win, draw, and loss probabilities for similar states.
What is the expected-utility EVAL formula?::$\mathbb{E}[U]=P(win)U(win)+P(draw)U(draw)+P(loss)U(loss)$.
What are drawbacks of probability-style evaluation?::Too many state categories, need for historical data, and poor scaling to complex games.
What is a neural evaluation function?::A learned model mapping a state to an estimated value.
What is the horizon effect?::A search error where an important event lies just beyond the cutoff depth.
How can the horizon effect be mitigated?::Search unstable tactical positions deeper, use problem-specific cutoffs, iterative deepening, and better move ordering.
Why can material-only chess evaluation fail?::It can miss tactics, king safety, or imminent material changes just beyond the cutoff.
What is a common EVAL mistake?::Making EVAL so expensive that it defeats the purpose of cutting off search.

## Monte Carlo Tree Search

#flashcards/CSC3041F-Automated-Planning/Search/Lecture-10-Monte-Carlo-Tree-Search

What is Monte Carlo Tree Search?::A search algorithm that estimates action values with repeated simulated play and selectively grows a tree.
What is a simulation or playout?::A complete simulated game from a state to a terminal outcome.
Why does alpha-beta struggle in games like Go?::The branching factor is huge and static evaluation functions are weak.
What is the basic simulation value estimate?::$\widehat{V}(s)=\text{total utility from simulations}/\text{number of simulations}$.
How is the value estimate interpreted in binary win/loss games?::As an estimated win percentage.
What is pure Monte Carlo search?::A flat method that runs simulations for each immediate move and chooses the best estimated move.
How does pure Monte Carlo differ from MCTS?::Pure Monte Carlo does not maintain a deep growing search tree.
What is a playout policy?::The rule used to choose moves during simulations.
Why might random playouts be insufficient?::In complex games they can be too noisy to estimate useful values.
What is exploitation in MCTS?::Choosing actions that currently look best.
What is exploration in MCTS?::Trying less-tested actions to learn whether they may be better.
What is UCB in MCTS?::A selection rule balancing average reward with an exploration bonus.
What is the UCB-style score from the notes?::$U(n)/N(n)+C\sqrt{\ln N(parent(n))/N(n)}$.
What does $U(n)$ represent in the MCTS score?::Total utility from simulations passing through node $n$.
What does $N(n)$ represent in the MCTS score?::The number of visits or simulations involving node $n$.
What does $C=0$ do in UCB-style MCTS?::It removes exploration and makes selection greedy.
What theoretical exploration constant value is mentioned?::About $1.41$.
What are the four phases of MCTS?::Selection, expansion, simulation, and back-propagation.
What happens during selection?::The algorithm follows the current tree policy from the root to a promising node.
What happens during expansion?::A new child node is added to the search tree.
What happens during simulation?::A playout is run from the new node to an outcome.
What happens during back-propagation?::The simulation result updates statistics along the path back to the root.
What makes MCTS an anytime algorithm?::It can return an action after any time or iteration budget.
What are MCTS's main strengths?::It samples huge state spaces, needs little handcrafted evaluation in principle, explores to variable depths, and works under time limits.
What is a common MCTS mistake?::Treating simulation estimates as exact values rather than noisy samples.

## RL Introduction

#flashcards/CSC3041F-Automated-Planning/RL/RL-01-RL-Introduction

What is reinforcement learning?::Learning through trial and error from interaction with an environment using rewards or penalties.
How does RL differ from supervised learning?::RL is not given correct actions for every state; it discovers behavior through interaction and feedback.
What is imitation learning?::Learning to predict actions from states using demonstrations.
Why is imitation learning limited compared with RL?::It is limited to demonstrated behavior and may fail in states outside the dataset.
What is behavior learning?::Learning a mapping from states to actions.
What is sequential decision making?::Decision making where current actions affect future states and rewards.
What is an agent in RL?::The learner or decision maker.
What is the environment in RL?::The world the agent acts in and receives states and rewards from.
What is a state or observation $s_t$?::The agent's current view or representation of the environment at time $t$.
What is an action $a_t$?::A decision made by the agent.
What is a reward $r_t$?::A scalar feedback signal returned by the environment.
What are the steps in the RL loop?::Observe state, choose action, environment updates, receive reward, and improve future behavior.
What is a policy?::The agent's behavior rule mapping states to actions or action probabilities.
What is a deterministic policy?::A policy where each state maps to one action.
What is a stochastic policy?::A policy giving a probability distribution over actions.
What is deterministic policy notation?::$a=\pi(s)$.
What is stochastic policy notation?::$\pi(a\mid s)=P(A_t=a\mid S_t=s)$.
What is the RL objective $J(\pi)$?::$J(\pi)=\mathbb{E}[\sum_t \gamma^t r(S_t,A_t)]$.
What is a reward function?::A scoring rule associating behavior with reward or penalty.
What is sparse reward?::A reward signal that appears rarely.
What is delayed reward?::A reward that arrives long after the action that caused it.
What is credit assignment?::Deciding which earlier actions caused later rewards or penalties.
What is the reward-function notation $R(s,a)=c$ saying?::Taking action $a$ in state $s$ gives scalar reward $c$.
What are environment dynamics?::The rule or probability model for how the next state follows from the current state and action.
<!--SR:!2026-06-06,3,250-->
What does $T(s_{t+1}\mid s_t,a_t)$ represent?::The probability of next state $s_{t+1}$ after state $s_t$ and action $a_t$.
What are Gridworld states and actions in the notes?::States are grid positions; actions are Up, Down, Left, and Right.
Why can a per-step penalty be useful in Gridworld?::It discourages wandering and encourages efficient paths to the goal.
What are common RL challenges?::High-dimensional spaces, sparse or delayed rewards, safety, limited interaction, and unpredictable environments.

## Markov Decision Processes

#flashcards/CSC3041F-Automated-Planning/RL/RL-02-Markov-Decision-Processes

What is a Markov Decision Process?::A formal model of sequential decision making with states, actions, transitions, rewards, and a discount factor.
What is the MDP tuple?::$\langle S,A,T,R,\gamma\rangle$.
What is the state set $S$?::The set of possible environment configurations.
What is the action set $A$?::The set of decisions available to the agent.
What is the transition function $T$?::A probability model for the next state given the current state and action.
What is the transition-probability notation?::$T(s,a,s')=P(S_{t+1}=s'\mid S_t=s,A_t=a)$.
What is the reward function $R$?::The immediate feedback signal or score received for acting.
What is the discount factor $\gamma$?::A value in $(0,1]$ controlling how much future rewards matter.
What is the Markov property?::The future depends only on the current state and action, not the full history.
What is the formal Markov property statement?::$P(S_{t+1}\mid S_t,A_t,\text{history})=P(S_{t+1}\mid S_t,A_t)$.
What must be true of the state for the Markov property to hold?::It must contain all relevant information from the past needed to predict the future.
What is a Markov chain?::A sequence of states satisfying the Markov property without actions or rewards.
How does an MDP extend a Markov chain?::It adds actions, rewards, and agent control.
What is a discrete action space?::A finite set of actions, such as left, right, or jump.
What is a continuous action space?::A real-valued action space, such as steering angle or motor torque.
What is a high-dimensional state space?::A large complex representation such as images or sensor arrays.
What is a fully observable MDP?::A setting where the agent observes the complete environment state.
What is a POMDP?::A partially observable MDP where the agent sees observations that may omit hidden state information.
What is the fully observable relation between observation and state?::$o_t=s_t$.
What does $\gamma\to0$ mean behaviorally?::The agent becomes myopic and focuses on immediate rewards.
What does $\gamma\to1$ mean behaviorally?::The agent values future rewards nearly as much as immediate rewards.
Why is $\gamma$ mathematically useful?::It can keep return finite and support convergence and stability.
What is exploration?::Trying actions to discover new information.
What is exploitation?::Using current knowledge to choose actions believed to be best.
Name common exploration approaches.::Epsilon-greedy, softmax, random perturbations, uncertainty estimation, and curiosity or intrinsic motivation.
What is cumulative discounted return?::The discounted sum of future rewards from time $t$.
What is the finite-horizon return formula?::$G_t=\sum_{k=0}^{H}\gamma^k R_{t+k+1}$.
Why does the return formula start with $R_{t+1}$?::Rewards are observed after actions.
What is model-based RL?::RL that knows or learns a model of transitions and rewards and plans with it.
What is model-free RL?::RL that learns behavior or values directly from experience without using a transition/reward model for planning.
What does a model predict in RL?::Approximate next state $\hat{s}_{t+1}$ and reward $\hat{r}_t$.

## Value Functions

#flashcards/CSC3041F-Automated-Planning/RL/RL-03-Value-Functions

What is return $G_t$?::The cumulative discounted reward from time $t$ onward.
What is the infinite-style return expansion?::$G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots$.
What is the finite-horizon return formula?::$G_t=\sum_{k=0}^{H}\gamma^k R_{t+k+1}$.
What happens to future rewards when $\gamma<1$?::Farther future rewards matter less.
What is a policy $\pi$?::The agent's behavior rule mapping states to actions or action probabilities.
<!--SR:!2026-06-05,4,270-->
What constraint must stochastic policy probabilities satisfy?::$\sum_{a\in A}\pi(a\mid s)=1$ for every state.
What is the RL objective in terms of $G_0$?::$J(\pi)=\mathbb{E}_{\pi}[G_0]$.
<!--SR:!2026-06-05,4,270-->
What is an optimal policy?::A policy that maximizes expected discounted return.
<!--SR:!2026-06-01,0,230-->
What is $V_{\pi}(s)$?::Expected return starting in state $s$ and following policy $\pi$.
What is the deterministic Bellman form for $V_{\pi}$?::$V_{\pi}(s)=R(s,\pi(s))+\gamma V_{\pi}(s')$.
<!--SR:!2026-06-05,4,270-->
What is the Bellman equation in words?::Current value equals immediate reward plus discounted expected future value.
What is the return split used in Bellman equations?::$G_t=R_{t+1}+\gamma G_{t+1}$.
What is $Q_{\pi}(s,a)$?::Expected return after taking action $a$ in state $s$, then following policy $\pi$.
Why is $Q$ useful for control?::It directly compares actions in the same state.
<!--SR:!2026-06-05,4,270-->
How is $V_{\pi}(s)$ computed from $Q_{\pi}(s,a)$ for a stochastic policy?::$V_{\pi}(s)=\sum_a\pi(a\mid s)Q_{\pi}(s,a)$.
How can $Q_{\pi}(s,a)$ be written using next-state value?::$Q_{\pi}(s,a)=\mathbb{E}[R(s,a,s')+\gamma V_{\pi}(s')]$.
<!--SR:!2026-06-05,4,270-->
When should you use $V$ rather than $Q$?::When evaluating how good states are under a policy.
When should you use $Q$ rather than $V$?::When choosing or improving actions.
Are values always probabilities?::No; their scale depends on rewards and discounting.
What is a common mistake with $V$ and $Q$?::Treating them as interchangeable even though $V$ scores states and $Q$ scores state-action pairs.
What happens to values if all rewards are multiplied by 10?::Values also scale by 10 for the same policy and dynamics.
<!--SR:!2026-06-05,4,270-->

## Optimal Value Functions

#flashcards/CSC3041F-Automated-Planning/RL/RL-04-Optimal-Value-Functions

What is policy evaluation?::Computing expected return for a fixed policy.
What is optimal control?::Finding a policy that maximizes expected return.
How does optimal control change the Bellman question?::It replaces policy averaging with maximizing over actions.
What is $V^*(s)$?::The maximum expected return achievable from state $s$.
What is $Q^*(s,a)$?::The maximum expected return after taking action $a$ in state $s$ and then acting optimally.
What is the deterministic optimal state-value equation?::$V^*(s)=\max_a[R(s,a)+\gamma V^*(s')]$.
What is the deterministic optimal action-value equation?::$Q^*(s,a)=R(s,a)+\gamma\max_{a'}Q^*(s',a')$.
What is the stochastic Bellman optimality equation for $V^*$?::$V^*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^*(s')]$.
What is an optimal policy $\pi^*$?::A policy that achieves the optimal value function.
What is policy domination?::$\pi_1\ge\pi_2$ if $V_{\pi_1}(s)\ge V_{\pi_2}(s)$ for all states.
Is $V^*$ unique?::Yes, under the usual finite discounted MDP assumptions.
Is the optimal policy always unique?::No; multiple actions can tie for the same optimal value.
What does $\max_a Q^*(s,a)$ return?::The best value.
What does $\arg\max_a Q^*(s,a)$ return?::The action that achieves the best value.
How do you extract $\pi^*$ from $Q^*$?::$\pi^*(s)=\arg\max_a Q^*(s,a)$.
How do you extract $\pi^*$ from $V^*$?::Use one-step lookahead with the transition and reward model.
Why does extracting a policy from $V^*$ require a model?::You must evaluate each action's expected reward plus next-state value.
What is the key move in the Bellman optimality derivation?::Optimize over the first action, then assume optimal behavior afterward.
What challenges make exact MDP solving hard?::Large state spaces, continuous spaces, and expensive maximization over actions.

## Value Iteration

#flashcards/CSC3041F-Automated-Planning/RL/RL-05-Value-Iteration

What is value iteration?::A dynamic programming algorithm that repeatedly applies Bellman optimality updates to approximate $V^*$.
What is dynamic programming?::Solving overlapping subproblems and reusing their solutions.
What assumptions does tabular value iteration make?::Finite states, finite actions, known transition model, and known reward function.
What is the goal of value iteration?::Find or approximate an optimal policy $\pi^*$ that maximizes expected return.
What is the Bellman optimality update in value iteration?::$V_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_k(s')]$.
What does $k$ mean in $V_k$?::The iteration number, not the environment timestep.
What is the value-iteration stopping threshold $\theta$ used for?::Stopping when value changes become small.
How is a policy extracted after value iteration?::$\pi(s)=\arg\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]$.
What is a synchronous update?::Compute all next values from a frozen old value table.
What is an asynchronous update?::Update values in place and reuse latest values immediately.
What is the benefit of synchronous updates?::They are consistent and parallelizable.
What is the benefit of asynchronous updates?::They often converge faster in practice.
What is value iteration complexity per sweep in stochastic MDPs?::$O(|S|^2|A|)$.
Why does stochastic value iteration have $O(|S|^2|A|)$ per sweep?::For each state and action, the update may sum over all next states.
What is a contraction?::An operator that brings value functions closer together by a factor less than 1.
What is the Bellman contraction inequality?::$\|\mathcal{T}V-\mathcal{T}U\|_{\infty}\le\gamma\|V-U\|_{\infty}$.
What does the contraction property guarantee?::Convergence to a unique fixed point, $V^*$, when $0\le\gamma<1$.
What is a major limitation of value iteration?::It requires a known model and can be infeasible in huge or continuous spaces.
What is a common value-iteration mistake?::Forgetting the max over actions in the Bellman optimality update.
Why does one sweep usually not give $V^*$?::Values typically need repeated sweeps to converge.

## Policy Iteration

#flashcards/CSC3041F-Automated-Planning/RL/RL-06-Policy-Iteration

What is policy iteration?::A dynamic programming algorithm that alternates between evaluating a policy and improving it.
How does policy iteration differ from value iteration?::Policy iteration maintains an explicit policy, while value iteration mainly updates values then derives a policy.
What are the two main steps in policy iteration?::Policy evaluation and policy improvement.
What does policy evaluation compute?::$V_{\pi}$ for the current fixed policy.
What Bellman equation is used in policy evaluation?::The Bellman expectation equation.
What is the policy-evaluation formula?::$V_{\pi}(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_{\pi}(s')]$.
What is policy improvement?::Updating the policy to choose actions greedily according to the current value function.
What is the policy-improvement formula?::$\pi_{\mathrm{new}}(s)=\arg\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V_{\pi}(s')]$.
What does it mean for a policy to be stable?::Policy improvement changes no state's action.
What happens when exact policy iteration reaches a stable policy?::The policy is optimal for the finite MDP.
What is synchronous policy iteration?::Fully evaluate all states, then improve the policy for all states.
What is asynchronous policy iteration?::Interleave evaluation and improvement for individual states or partial batches.
What is the policy improvement theorem?::Greedifying correctly with respect to a value function cannot make the policy worse and leads to optimality in finite tabular policy iteration.
What is generalized policy iteration?::A framework where evaluation and improvement interact, possibly partially or approximately.
Why is GPI important?::Many modern RL algorithms are forms of partial or approximate evaluation plus improvement.
When can policy iteration be attractive?::When a reasonable initial policy exists and explicit policy improvement is useful.
What is a common policy-iteration mistake?::Confusing Bellman expectation for fixed-policy evaluation with Bellman optimality.
Why can policy iteration iterations be expensive?::Policy evaluation may require solving or repeatedly sweeping the whole value function.

## Monte Carlo Methods

#flashcards/CSC3041F-Automated-Planning/RL/RL-07-Monte-Carlo-Methods

What is model-free RL?::RL that learns from experience without a known transition and reward model for planning.
What is experience in RL?::Observed states, actions, rewards, and next states from interacting with the environment.
What is a Monte Carlo method?::A method that estimates quantities by averaging random samples.
What is an episode?::A complete trajectory from a starting state to a terminal state.
What is Monte Carlo prediction?::Estimating $V_{\pi}(s)$ for a fixed policy from sampled episodes.
When does Monte Carlo update values?::After the episode ends and full returns can be computed.
Does Monte Carlo bootstrap?::No; it updates toward sampled full returns.
What full return does MC use for updates?::$G_t=R_{t+1}+\gamma R_{t+2}+\cdots$.
What kind of tasks are classic Monte Carlo methods most natural for?::Episodic tasks.
Why can Monte Carlo have high variance?::Full trajectories include many random events.
What is first-visit Monte Carlo?::Use only the return after the first occurrence of a state in an episode.
What is every-visit Monte Carlo?::Use returns after every occurrence of a state in an episode.
What is the sample-average MC value estimate?::$V(s)=\frac{1}{N(s)}\sum_{i=1}^{N(s)}G_i(s)$.
What is the incremental MC update?::$V(s)\leftarrow V(s)+\alpha[G_t-V(s)]$.
What can $\alpha$ be for sample averages?::$1/N(s)$.
What is Monte Carlo control?::Learning action values from episode returns and improving the policy.
Why does MC control need $Q(s,a)$?::Policy improvement requires comparing actions in a state.
What is the MC action-value estimate?::$Q(s,a)=\frac{1}{N(s,a)}\sum_{i=1}^{N(s,a)}G_i(s,a)$.
Why is exploration required in MC control?::Useful state-action pairs must be sampled to learn their returns.
What is a common MC mistake?::Trying to update classic MC values before the episode has finished.

## Temporal Difference Learning

#flashcards/CSC3041F-Automated-Planning/RL/RL-08-Temporal-Difference-Learning

What is temporal difference learning?::Model-free learning that updates estimates using observed rewards plus current estimates of successor values.
What is an online update?::Updating during an episode rather than waiting for it to finish.
Why is TD useful for long or continuing tasks?::It can update after each transition and does not require episode termination.
What is a TD target?::The one-step target $R+\gamma V(s')$.
What is a TD error?::The difference between the TD target and the current estimate.
What is the TD error formula?::$\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)$.
What is the TD(0) value update?::$V(S_t)\leftarrow V(S_t)+\alpha\delta_t$.
How does TD differ from Monte Carlo?::TD bootstraps and updates step by step; MC uses full returns after episode end.
Is TD generally biased or unbiased?::Generally biased because it bootstraps from current estimates.
Why can TD have lower variance than Monte Carlo?::It uses shorter targets with less trajectory randomness.
What is learning rate $\alpha$?::A step size controlling how much new evidence changes an estimate.
What is the generic update pattern?::New estimate equals old estimate plus $\alpha$ times target minus old estimate.
What is n-step TD?::A method using $n$ rewards before bootstrapping from a later value estimate.
What is the n-step return formula?::$G_t^{(n)}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^nV(S_{t+n})$.
How does increasing $n$ affect bias and variance?::Bootstrapping bias decreases and variance increases.
What is TD prediction?::Estimating $V_{\pi}(s)$ for a fixed policy using TD updates.
What is TD control?::Estimating $Q(s,a)$ and improving the policy from TD experience.
What is a target policy?::The policy being learned or evaluated.
What is a behavior policy?::The policy used to generate actions and data.
What is on-policy learning?::Learning about the same policy used to act.
What is off-policy learning?::Learning a target policy different from the behavior policy.
What is SARSA?::An on-policy TD control algorithm using $(S,A,R,S',A')$.
What is Q-learning?::An off-policy TD control algorithm that updates toward the best next action.
What is the SARSA update?::$Q(S,A)\leftarrow Q(S,A)+\alpha[R+\gamma Q(S',A')-Q(S,A)]$.
What is the Q-learning update?::$Q(S,A)\leftarrow Q(S,A)+\alpha[R+\gamma\max_a Q(S',a)-Q(S,A)]$.
What is the key target difference between SARSA and Q-learning?::SARSA uses the actual next action; Q-learning uses the greedy best next action.
Why is SARSA often more conservative?::It learns from exploratory behavior actually taken.
Why is Q-learning often more aggressive?::It learns as if the agent will act greedily next.

## Function Approximation And DQN

#flashcards/CSC3041F-Automated-Planning/RL/RL-09-Function-Approximation-And-DQN

What is tabular RL?::RL that stores one value for every state or state-action pair.
Why do tabular methods fail in large spaces?::Memory explodes, most states are never visited, and tables cannot generalize.
What is function approximation?::Replacing a value table with a parameterized function that predicts values.
What is the function-approximation replacement for tabular Q?::$Q(s,a)\to Q(s,a;\theta)$.
What does $\theta$ represent?::Learnable model parameters.
What is generalization in function approximation?::Using learned structure from seen states to make predictions for unseen states.
Name common value-function approximators.::Linear models, decision trees, and neural networks.
What is the TD error for Q-learning with function approximation?::$\delta=r+\gamma\max_{a'}Q(s',a';\theta)-Q(s,a;\theta)$.
What is gradient descent?::An optimization method that updates parameters to reduce a loss function.
What is the gradient descent update?::$\theta\leftarrow\theta-\alpha\nabla_{\theta}L(\theta)$.
What is a loss function?::A function measuring prediction error.
What is a Deep Q-Network?::A neural network approximation of the Q-function trained with Q-learning targets.
What is the DQN target?::$y=r+\gamma\max_{a'}Q(s',a';\theta)$.
What is the DQN MSE loss?::$L(\theta)=(y-Q(s,a;\theta))^2$.
Why can DQN be unstable?::Samples are correlated, targets are non-stationary, and bootstrapping errors can feed back.
What are correlated samples?::Consecutive transitions that are similar and produce noisy or biased gradients.
Why are DQN targets non-stationary?::The network's changing predictions help define the target.
What is experience replay?::Storing transitions and sampling them randomly for training.
What transition tuple is stored in replay?::$(s,a,r,s')$.
How does experience replay help?::It breaks sample correlation, reuses data, and smooths learning.
What is a target network?::A separate, slower-updated network used to compute targets.
How does a target network stabilize DQN?::It keeps the bootstrapped target steadier while the online network learns.
What is gradient-based Monte Carlo?::Training a differentiable value function using full sampled returns rather than TD targets.
What is the difference between Gradient MC and DQN targets?::Gradient MC targets full return $G_t$; DQN uses bootstrapped targets.
What is a common DQN mistake?::Applying tabular convergence intuition directly to nonlinear neural networks.

## Modern Reinforcement Learning

#flashcards/CSC3041F-Automated-Planning/RL/RL-10-Modern-Reinforcement-Learning

What foundations does modern RL extend in this course?::RL basics, MDPs, value functions, DP, Monte Carlo, TD, Q-learning, function approximation, and DQN.
What is a continuous state space?::A state space where states are real-valued vectors rather than finite categories.
What is a continuous action space?::An action space where actions are real-valued, such as torque or steering.
What complications appear beyond discrete Gridworld?::Continuous states/actions, images, sparse rewards, stochastic dynamics, noisy observations, long horizons, and safe exploration.
Why do image states often need convolutional neural networks?::They require feature extraction from high-dimensional visual input.
What is continuous control?::RL where actions are continuous values.
Why is vanilla DQN not naturally suited to continuous actions?::It relies on maximizing over discrete action values.
Name common continuous-control algorithms.::DDPG, TD3, and SAC.
What is true model-based RL?::Learning an environment model from data and using it for planning.
How does true model-based RL differ from earlier model-based planning?::Earlier planning assumed $T$ and $R$ were known; true model-based RL learns them.
What is Dyna?::A model-based RL idea combining real experience with simulated planning updates.
What is the main risk of learned-model planning?::Model errors can compound during simulated planning.
What is n-step bootstrapping?::Using $n$ rewards before bootstrapping from a value estimate.
What is the n-step value update?::$V(S_t)\leftarrow V(S_t)+\alpha[G_t^{(n)}-V(S_t)]$.
What is an eligibility trace?::A decaying memory of recently visited states or actions for assigning credit online.
What is Double DQN?::A DQN variant that reduces overestimation bias by separating action selection from action evaluation.
What is Dueling DQN?::A DQN variant that separates state value from action advantage.
What is prioritized replay?::Sampling more important or high-learning-signal experiences more often.
What is Rainbow DQN?::A combined DQN system incorporating multiple DQN improvements.
What is a policy gradient method?::A method that optimizes a parameterized policy directly for expected reward.
What is REINFORCE?::A basic Monte Carlo policy-gradient algorithm that increases probabilities of actions that led to high returns.
What is policy-gradient policy notation?::$\pi(a\mid s;\theta)$.
Why can policy gradients work well for continuous actions?::They avoid a discrete max over action values and optimize the policy directly.
What is an actor-critic method?::A method with a policy learner called the actor and a value estimator called the critic.
What is the actor?::The policy component that chooses actions.
What is the critic?::The value-function component that evaluates states or actions.
Why use actor-critic methods?::They combine policy optimization with value estimation and can reduce variance.
What is multi-agent RL?::RL with multiple learning agents that affect each other.
Why is MARL non-stationary?::Other agents are learning and changing the environment dynamics from each agent's perspective.
What is multi-objective RL?::RL with multiple objectives represented by vector rewards.
What is a MORL challenge?::Objectives can conflict and preferences must be specified or learned.
What is offline RL?::Learning from a fixed dataset without new environment interaction.
Why is offline RL useful?::It applies when live interaction is expensive or dangerous.
Why is offline RL difficult?::It faces distribution shift, unseen-action overestimation, and limited exploration.
Name practical RL tooling from the notes.::Stable-Baselines3, CleanRL, Gymnasium, RLlib, PettingZoo, MORL-Baselines, MO-Gymnasium, CORL, and Minari.

## Formula Sheet

#flashcards/CSC3041F-Automated-Planning/Formula-Sheet

What does $S$ denote in the formula sheet?::The state set.
What does $A$ denote in the formula sheet?::The action set.
What do $s$ and $s'$ denote?::The current state and next state.
What do $a$ and $a'$ denote?::The current action and next action.
What does $T$ denote?::The transition model.
What does $R$ denote?::The reward function.
What does $\gamma$ denote?::The discount factor.
What does $b$ denote in search complexity?::The branching factor.
What does $d$ denote in search complexity?::The depth of the shallowest solution.
What does $m$ denote in search complexity?::The maximum search depth.
What does $l$ denote in depth-limited search?::The depth limit.
What can $C$ denote in the notes?::Optimal solution cost in UCS or the exploration constant in MCTS, depending on context.
What does $c$ denote in UCS complexity?::The smallest positive step cost.
What does $g(n)$ denote?::Path cost from the initial state to node $n$.
What does $h(n)$ denote?::A heuristic estimate from node $n$ to a goal.
What does $h^*(n)$ denote?::The true cheapest remaining cost from node $n$ to a goal.
What does $k$ denote in beam search?::The beam width.
What can $\delta$ denote?::The delta-beam threshold or TD error, depending on context.
What do $\alpha$ and $\beta$ denote in game search?::Alpha-beta pruning bounds.
What does $\pi$ denote?::A policy.
What are $V_{\pi}$ and $Q_{\pi}$?::State-value and action-value functions under policy $\pi$.
What are $V^*$ and $Q^*$?::Optimal state-value and action-value functions.
What does $\theta$ denote?::Learnable parameters.
What is the conservative admissible heuristic combination?::$h(n)=\max\{h_1(n),h_2(n),h_3(n),\ldots\}$.
What is the source-slide weak admissible heuristic combination?::$h(n)=\min\{h_1(n),h_2(n),h_3(n),\ldots\}$.
What is the A* evaluation formula?::$f_{A^*}(n)=g(n)+h(n)$.
What is the greedy best-first score?::$f_{\mathrm{greedy}}(n)=h(n)$.
What are BFS time and space complexities?::$O(b^d)$ time and $O(b^d)$ space.
What are DFS time and space complexities?::$O(b^m)$ time and $O(bm)$ space.
What are IDS time and space complexities?::$O(b^d)$ time and $O(bd)$ space.
What is the beam-search space formula?::$O(km)$.
What is the delta-beam keep formula?::$f(n)\le f(n_{\mathrm{best}})+\delta$.
What is the MCTS value estimate?::$\widehat{V}(n)=\text{total utility}/\text{number of simulations}$.
What is the MC incremental update formula?::$V(s)\leftarrow V(s)+\alpha[G_t-V(s)]$.
What is the TD(0) update formula?::$V(S_t)\leftarrow V(S_t)+\alpha[R_{t+1}+\gamma V(S_{t+1})-V(S_t)]$.
What is the DQN loss formula?::$L(\theta)=(y-Q(s,a;\theta))^2$.
