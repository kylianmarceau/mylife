---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "07 — Agent Architectures III: Learned Reactive Controllers and RoboCup Team Behavior"
---

# 07 — Agent Architectures III: Learned Reactive Controllers and RoboCup Team Behavior

**Source note:** [Agent Architectures III: Learned Reactive Controllers and RoboCup Team Behavior](../07_Agent_Architectures_III.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#Multi-agent subsumption and bottom-up design|Multi-agent subsumption and bottom-up design]]
  - [[#RoboCup layers and behavior hierarchy|RoboCup layers and behavior hierarchy]]
  - [[#Pass-or-shoot network: perception and outputs|Pass-or-shoot network: perception and outputs]]
  - [[#Data collection, supervision, and backpropagation|Data collection, supervision, and backpropagation]]
  - [[#Testing and interpreting results|Testing and interpreting results]]
  - [[#Extend to dribbling and ball interception|Extend to dribbling and ball interception]]
  - [[#Combine learned behaviors and compare teams|Combine learned behaviors and compare teams]]

## Core Content

### Multi-agent subsumption and bottom-up design

<!-- qard-id: ais-44774b0a03f4cb89e583 -->
> [!qard]- What is a multi-agent system?
> Several agents interacting in a shared environment.

<!-- qard-id: ais-cbc4bb2f249d006ed597 -->
> [!qard]- What is bottom-up control?
> Building system behavior from individual competencies and their interactions.

<!-- qard-id: ais-132f5a8c4cdfefd93c57 -->
> [!qard]- What is emergent team behavior?
> Collective behavior produced by interacting local controllers rather than a prewritten trajectory for the entire team.

<!-- qard-id: ais-9c3b5bb1e67fb05891cc -->
> [!qard]- What does subsumption coordinate?
> Behavior layers through signal suppression or overriding.

<!-- qard-id: ais-134aa01086b63962cbca -->
> [!qard]- What is the bottom-up team-design procedure?
> Train or define individual skills, combine them through control, let agents interact, and evaluate the resulting team behavior.

<!-- qard-id: ais-acb68bc119b045adb8d6 -->
> [!qard]- Which applications illustrate interacting autonomous components?
> Satellite groups, small robots, drone teams, environmental monitoring, and robot soccer.

<!-- qard-id: ais-1f7d0cabe917cdb9a475 -->
> [!qard]- Can a trained neural controller still be reactive at runtime?
> Yes. Learning method and execution architecture are different axes.

### RoboCup layers and behavior hierarchy

<!-- qard-id: ais-99a06fd6a3e075ad2dc8 -->
> [!qard]- What are cooperative and adversarial behavior?
> Cooperative agents pursue compatible goals; adversarial behavior responds to opponents with conflicting goals.

<!-- qard-id: ais-4000f2193bbfe0693db6 -->
> [!qard]- What is interception?
> Movement to meet a moving ball.

<!-- qard-id: ais-a777024675a2bf9083c7 -->
> [!qard]- What five RoboCup interaction layers are described?
> Player-ball, one-to-one players, one-to-many players, team formation, and team-to-opponent interaction.

<!-- qard-id: ais-daab368d28f0c174c77c -->
> [!qard]- What competencies correspond to the five interaction layers?
> Individual interception, paired passing/shooting, several-player passing/shooting, strategic positioning, and adaptation to opponents.

<!-- qard-id: ais-aa08eb55c2eabe7804f0 -->
> [!qard]- How do individual skills support team behavior?
> Kick, dribble, and intercept skills support paired pass/intercept actions and then team choices among passing, dribbling, and shooting.

<!-- qard-id: ais-cacc7f32030044f11f59 -->
> [!qard]- Why are the five-layer table and three-tier diagram not contradictory?
> They describe the behavior hierarchy at different levels of detail.

<!-- qard-id: ais-2a0c79fcdf414d057540 -->
> [!qard]- What makes two interacting soccer teams an adversarial setting?
> Their objectives conflict, so team behavior must account for opponent decisions as well as teammate cooperation.

### Pass-or-shoot network: perception and outputs

<!-- qard-id: ais-d7afb6a6b94623fde6b6 -->
> [!qard]- What are an ANN, activation, and hidden layer?
> A weighted computational network; a node’s computed output; and processing nodes between inputs and outputs respectively.

<!-- qard-id: ais-a2b4f2207575a14825c4 -->
> [!qard]- What is normalized distance?
> Distance rescaled relative to a chosen reference.

<!-- qard-id: ais-2b916c3f9d2bda1d9ec7 -->
> [!qard]- What four features feed the pass-or-shoot network?
> $\mathbf x=(\theta_B,d_B,\theta_C,d_C)$: angle and normalized distance to teammate B and goalie C.

<!-- qard-id: ais-74a34f68bc75233c0759 -->
> [!qard]- What outputs and hidden structure are illustrated for pass-or-shoot selection?
> Four inputs connect through two hidden nodes to pass and shoot output activations.

<!-- qard-id: ais-24a05a0f26948b177017 -->
> [!qard]- What action-selection formula is used at each tick?
> $a_t=\arg\max_{a\in\{\mathrm{pass},\mathrm{shoot}\}}z_a(\mathbf x_t)$.

<!-- qard-id: ais-e9addf8893eb4a409b12 -->
> [!qard]- Are the action activations necessarily calibrated probabilities?
> No. They are scores; choosing the largest does not establish probability calibration.

<!-- qard-id: ais-d1580a1e92efcff9c2fb -->
> [!qard]- What implementation detail is needed if two action activations tie?
> A tie-breaking policy; none is specified in the source.

### Data collection, supervision, and backpropagation

<!-- qard-id: ais-e0def89089269cfbb36f -->
> [!qard]- What are a labeled example, backpropagation, and learning rate?
> Input paired with a target; computation of parameter gradients; and the step-size factor for weight updates.

<!-- qard-id: ais-95e1c1c7416263ec1a2d -->
> [!qard]- How is training data collected for the pass-or-shoot controller?
> Run $5{,}000$ randomized player/goalie simulations, randomly pass or shoot, record geometry and goal outcome, then train with backpropagation.

<!-- qard-id: ais-0496dd292f961b7c1ec5 -->
> [!qard]- What do the binary outcome labels mean?
> A scored goal is good, $1$; otherwise bad, $0$. The label is not a pass/shoot action index.

<!-- qard-id: ais-0c023e9c6395b72a46b8 -->
> [!qard]- What class imbalance is reported in the training data?
> $915$ positive and $4{,}085$ negative examples.

<!-- qard-id: ais-530abe0777a290465a48 -->
> [!qard]- What target-construction detail is missing from the displayed outcome tuple?
> It does not identify the attempted action or fully explain how outcome feedback is assigned to the two network outputs.

<!-- qard-id: ais-1550fa3a035470334070 -->
> [!qard]- Why must action-specific feedback mapping be defined for a complete implementation?
> An outcome label alone does not tell a multi-output network which attempted action’s prediction should receive that feedback.

<!-- qard-id: ais-34a33c9629dab60b3b51 -->
> [!qard]- What is MSE, and what scalar-target formula is given?
> Mean squared error is average squared prediction error: $L=\frac1N\sum_i(\hat y_i-y_i)^2$.

<!-- qard-id: ais-a6f22b042b68893fc458 -->
> [!qard]- What gradient-descent weight update is given?
> $\mathbf w\leftarrow\mathbf w-\eta\nabla_{\mathbf w}L$.

<!-- qard-id: ais-ab5d6685de3c776f5730 -->
> [!qard]- What extra aggregation must be specified for multi-output MSE?
> How losses are averaged over output dimensions as well as examples; the exact source aggregation is unspecified.

<!-- qard-id: ais-70af33657b2b4a34a1c6 -->
> [!qard]- What learning rate and training error are reported?
> $\eta=10^{-6}$ and MSE $0.0598$; these are training measures, not game-success guarantees.

### Testing and interpreting results

<!-- qard-id: ais-3d63516a652f324e549f -->
> [!qard]- What held-out simulation setup is used to test pass-or-shoot behavior?
> $2{,}000$ simulations with teammate and goalie randomized within angle range $[-60^\circ,30^\circ]$, using the same four features and maximum-activation selection.

<!-- qard-id: ais-6818f571f9c6340e983f -->
> [!qard]- What reported goal-success rates compare pass, shoot, and overall behavior?
> Pass $31.4\%$, shoot $52.1\%$, overall $40.9\%$ in the described test setup.

<!-- qard-id: ais-41369f40a90196257db6 -->
> [!qard]- Why is the reported outcome table not an action-classification confusion matrix?
> It reports good/bad game outcomes; total success also depends on how often each action is selected.

<!-- qard-id: ais-bd3f89dac8ff200b0341 -->
> [!qard]- Why should total success not be assumed to be the unweighted mean of action-success rates?
> The selected actions can occur with different frequencies, so their contributions must be weighted appropriately.

<!-- qard-id: ais-c4f1f3ac314079bdd471 -->
> [!qard]- What qualitative response occurs when the opponent blocks the goal direction?
> Shoot activation falls and passing becomes preferred in the reconstructed response curves.

<!-- qard-id: ais-aa629fa3ec2c04419cd2 -->
> [!qard]- Why distinguish training MSE from held-out game success?
> MSE measures fit to targets; game success evaluates behavior in new simulations.

### Extend to dribbling and ball interception

<!-- qard-id: ais-9158714cea71f9b8c907 -->
> [!qard]- What are discrete action selection and continuous control output?
> Discrete selection chooses from a finite action set; continuous output gives a numerical control value within a range.

<!-- qard-id: ais-ecfe8f96c512685182a9 -->
> [!qard]- How is the possession-action network extended to dribbling?
> Keep the four teammate/goalie features, add a dribble output, and select the largest of pass, dribble, and shoot activations.

<!-- qard-id: ais-ef1fc5c5605851a11a74 -->
> [!qard]- When is the pass/dribble/shoot controller used?
> When the ball is stationary or intercepted/possessed and nearby teammates/opponents matter.

<!-- qard-id: ais-a97d22aeed12158dbe32 -->
> [!qard]- What three inputs feed the interception controller?
> $\mathbf x_t^{\mathrm{intercept}}=(d_t,d_{t-1},\theta_t)$: current and previous ball distance and current ball angle.

<!-- qard-id: ais-09575a137f499489fbd1 -->
> [!qard]- What output does the interception controller produce?
> A turn angle, shown in $[0^\circ,90^\circ]$, followed by movement at a preset speed.

<!-- qard-id: ais-f645230f4a7a5f1ba2a1 -->
> [!qard]- When is interception relevant?
> When the ball is moving toward the player or the defended goal.

<!-- qard-id: ais-87ccf6d6247e30d7aa66 -->
> [!qard]- Why is this interception controller not wholly memoryless?
> It explicitly uses the previous timestep’s distance measurement.

<!-- qard-id: ais-95509eb4f94846265777 -->
> [!qard]- What test scope is reported for the extended controllers?
> Both expanded action selection and interception are tested in $2{,}000$ simulations; no additional numerical team-win rates are supplied.

### Combine learned behaviors and compare teams

<!-- qard-id: ais-fd056ad53622c31c9b29 -->
> [!qard]- What situation-dependent control loop combines the learned skills?
> Observe motion, possession, proximity, and goal threat; choose the appropriate controller; execute; repeat across agents; evaluate team interactions.

<!-- qard-id: ais-323e1150d625f8e54280 -->
> [!qard]- How do the random baseline and trained teams differ?
> The baseline uses simple movement and random possession actions; trained teams select the interception ANN or pass/shoot/dribble ANN for the situation.

<!-- qard-id: ais-575a2ebb39f0c12a23a2 -->
> [!qard]- What comparison setups are shown in the demonstrations?
> Random versus trained and trained versus trained teams, with red starting with the ball.

<!-- qard-id: ais-7072ad29b1869ef934bb -->
> [!qard]- Why can the exported demonstration frames not establish a winner or team-success rate?
> They provide no quantitative result sufficient for that inference.

<!-- qard-id: ais-8a1197fc331960d4ea53 -->
> [!qard]- Why do good local skills not guarantee good team tactics?
> Desired passing, formation, and opposition behavior depend on controller interactions and environmental conditions.

<!-- qard-id: ais-36084f3067f07b68c871 -->
> [!qard]- What adaptation limits remain in fixed task-specific layers?
> Limited planning and task adaptability; offline-trained modules do not automatically learn during play.
