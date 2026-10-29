---
tags:
  - ai-systems
  - flashcards
qard-deck: "AI Systems"
qard-topic: "08 — Agent Architectures IV: Beliefs, Desires, Intentions, And Probabilistic BDI"
---

# 08 — Agent Architectures IV: Beliefs, Desires, Intentions, And Probabilistic BDI

**Source note:** [Agent Architectures IV: Beliefs, Desires, Intentions, And Probabilistic BDI](../08_BDI_Agent_Architectures.md)

Exam recall cards covering concepts, definitions, methods, and qualifications. Worked examples are omitted; general proof methods are retained.

## Contents

- [[#Core Content|Core Content]]
  - [[#The Agent Paradigm And BDI Mental States|The Agent Paradigm And BDI Mental States]]
  - [[#Practical Reasoning And Bounded Rationality|Practical Reasoning And Bounded Rationality]]
  - [[#Original BDI Control Loop|Original BDI Control Loop]]
  - [[#Abstract BDI Interpreter And Plan Libraries|Abstract BDI Interpreter And Plan Libraries]]
  - [[#Implementation And Advantages|Implementation And Advantages]]
  - [[#Reconsideration, Hierarchies, And Uncertainty|Reconsideration, Hierarchies, And Uncertainty]]
  - [[#Operational Decision-Making And Probabilistic BDI|Operational Decision-Making And Probabilistic BDI]]
  - [[#The Dynamic Bayesian Decision Network|The Dynamic Bayesian Decision Network]]
  - [[#Probabilistic BDI Control Loop|Probabilistic BDI Control Loop]]
  - [[#Rational, Human-Like, Reactive, Or Deliberative?|Rational, Human-Like, Reactive, Or Deliberative?]]

## Core Content

### The Agent Paradigm And BDI Mental States

<!-- qard-id: ais-3116d3efb3ae59fd9e78 -->
> [!qard]- What is a BDI architecture?
> An architecture organized around beliefs, desires, and intentions, derived from practical-reasoning ideas and Bratman’s mental attitudes.

<!-- qard-id: ais-ba2320aa466bd0990789 -->
> [!qard]- What are beliefs in BDI?
> What the agent believes about its environment and itself, including contextual facts and inference rules; they can be incomplete, uncertain, or wrong.

<!-- qard-id: ais-9c09887096903a0b4149 -->
> [!qard]- What are desires in BDI?
> Goals or states of affairs the agent would like to achieve; they can conflict, be unrealistic, or be mutually inconsistent.

<!-- qard-id: ais-98af9d0ab457c8077233 -->
> [!qard]- What are intentions in BDI?
> Selected goals the agent is currently committed to achieving, coherent and achievable relative to its beliefs.

<!-- qard-id: ais-b581cb9e66bf6ecc6085 -->
> [!qard]- Why are intentions not simply all desirable outcomes?
> They are active commitments chosen from desires to focus planning and avoid reconsidering every possibility each step.

<!-- qard-id: ais-ed630d3396a16f9fa79e -->
> [!qard]- How do previous commitments affect BDI reasoning?
> Existing intentions influence subsequent option generation, deliberation, and plan choice.

### Practical Reasoning And Bounded Rationality

<!-- qard-id: ais-c666c4f99dfef1c59118 -->
> [!qard]- What is deliberation?
> Deciding which states of affairs to pursue from potentially conflicting desires, producing intentions.

<!-- qard-id: ais-cc0e02b9dd606efb43be -->
> [!qard]- What is means-ends reasoning?
> Deciding how to achieve selected intentions, producing an executable plan.

<!-- qard-id: ais-54a44342ddfbd6113ca7 -->
> [!qard]- What is bounded rationality?
> Decision-making subject to limits on information, time, and computation.

<!-- qard-id: ais-e92359e39df3220b823b -->
> [!qard]- What is satisficing?
> Selecting an adequate option within available constraints rather than exhaustively seeking an ideal one.

<!-- qard-id: ais-0311494ff7b7981c86d7 -->
> [!qard]- What are the steps of BDI’s cognitive loop?
> Revise beliefs from percepts, consider goals/intentions/options, commit to selected goals, find a plan, execute, then continue or revise using new observations.

<!-- qard-id: ais-56bdfabcaed63b9c859a -->
> [!qard]- How do commitments bound deliberation?
> They preserve focus on selected objectives, limiting repeated exhaustive reconsideration under resource constraints.

<!-- qard-id: ais-e3afad444e1b89c8091f -->
> [!qard]- Does maintaining beliefs, desires, and intentions guarantee global expected-utility optimality?
> No. Practical BDI commitments support bounded reasoning rather than proving an ideal fully informed optimum.

### Original BDI Control Loop

<!-- qard-id: ais-2aea917a24ff01abaf72 -->
> [!qard]- What does the belief revision function $\operatorname{brf}$ do?
> Update beliefs using the next percept.

<!-- qard-id: ais-8c547218d78231b6a453 -->
> [!qard]- What does the options function do?
> Generate candidate desires using beliefs and current intentions.

<!-- qard-id: ais-418ed1506b893b0177cb -->
> [!qard]- What does the filter function do?
> Select intentions from beliefs, candidate desires, and previous commitments.

<!-- qard-id: ais-1754016ba2a5018b1e50 -->
> [!qard]- What do $B_0$, $I_0$, $B$, $I$, $p$, $D$, and $\pi$ denote?
> Initial/current beliefs and intentions, next percept, candidate desires/options, and selected plan respectively.

<!-- qard-id: ais-25bcb361361977a91fd8 -->
> [!qard]- What formal updates define the original BDI loop?
> $B\leftarrow\operatorname{brf}(B,p)$; $D\leftarrow\operatorname{options}(B,I)$; $I\leftarrow\operatorname{filter}(B,D,I)$; $\pi\leftarrow\operatorname{plan}(B,I)$; execute $\pi$, starting from $B_0,I_0$.

<!-- qard-id: ais-f4f95c014ccbd4672808 -->
> [!qard]- What execution details are left abstract by the original BDI loop?
> Action granularity, interruption, and plan-failure reporting; the notation does not imply blindly executing a long plan before sensing again.

### Abstract BDI Interpreter And Plan Libraries

<!-- qard-id: ais-a9f3da589eb2b9c53ea7 -->
> [!qard]- What is an event in a BDI interpreter?
> A change or request triggering agent processing.

<!-- qard-id: ais-c5575b24848ae07ab524 -->
> [!qard]- What is a plan library?
> A collection of available plans selected for events and their contexts.

<!-- qard-id: ais-f05425ff7c5fc6506667 -->
> [!qard]- What state structures does the abstract BDI interpreter maintain?
> Events $E_v$, beliefs $B_{el}$, plan library $P_{lib}$, and intentions $I_{nt}$.

<!-- qard-id: ais-1cfb61ea4ecf42225472 -->
> [!qard]- What are the four stages of the abstract BDI interpreter?
> Update events, revise beliefs from events, select applicable plans using events/beliefs/library/current intentions, and execute an intention that can create new events.

<!-- qard-id: ais-025d433bd608fba4a5aa -->
> [!qard]- What is the interpreter’s plan-selection update?
> $I_{nt}\leftarrow\operatorname{SelectPlans}(E_v,B_{el},P_{lib},I_{nt})$.

<!-- qard-id: ais-d1661d2ac3217444a563 -->
> [!qard]- What is the interpreter’s intention-execution update?
> $E_v\leftarrow\operatorname{ExecuteIntention}(I_{nt},E_v)$, allowing action effects to trigger further processing.

<!-- qard-id: ais-ddf4d4ccc75911ac4171 -->
> [!qard]- How does the interpreter differ in abstraction from the original BDI loop?
> Percept revision becomes event/belief processing, option filtering becomes applicable-plan selection, and an explicit plan library supports intention execution.

<!-- qard-id: ais-982f19d6ef5d453d622e -->
> [!qard]- What do both original BDI and interpreter views retain?
> Explicit committed goal pursuit, expressed at different levels of implementation detail.

### Implementation And Advantages

<!-- qard-id: ais-0602eb9734e742a51424 -->
> [!qard]- How are AgentSpeak, JASON, and ASTRA related?
> AgentSpeak is an agent-oriented programming language; JASON implements it; ASTRA is based on it.

<!-- qard-id: ais-e2906ebb51bdfeb90563 -->
> [!qard]- What are PRS and JADEX?
> Procedural Reasoning System and a Java-based agent-programming system respectively.

<!-- qard-id: ais-4886d99a33058944be6e -->
> [!qard]- What implementation advantages can BDI languages offer?
> Rapid development, context-sensitive responses, robust behavior, and intelligibility through inspectable beliefs, plans, and commitments.

<!-- qard-id: ais-92fb9394aa2cb81e0d30 -->
> [!qard]- Why is BDI verifiability a relative advantage rather than a correctness guarantee?
> Correctness still depends on belief updates, plans, selection rules, and assumptions about the environment.

### Reconsideration, Hierarchies, And Uncertainty

<!-- qard-id: ais-71920057cce32ed3136f -->
> [!qard]- What is a reconsideration function?
> A test deciding whether to deliberate about new or revised intentions.

<!-- qard-id: ais-ba48c87538b76588232e -->
> [!qard]- Where is reconsideration inserted in the control loop?
> Immediately before generating options and filtering intentions, avoiding unnecessary full deliberation.

<!-- qard-id: ais-0498979d35ffd4469f76 -->
> [!qard]- What should be checked about current intentions at every iteration?
> Whether they remain achievable, are already achieved (including externally), and remain appropriate under the changed context.

<!-- qard-id: ais-792be70c28d523fdd4a9 -->
> [!qard]- What happens when intentions are reconsidered too often?
> Deliberation wastes time, commitments become unstable, and the agent can thrash between goals.

<!-- qard-id: ais-aab6a6f3a22c2a0bfb82 -->
> [!qard]- What happens when intentions are reconsidered too rarely?
> Outdated or impossible goals persist, and opportunities or emergencies may be missed.

<!-- qard-id: ais-e0343d11fdd0b918c2a8 -->
> [!qard]- What is a hierarchical plan?
> A plan decomposed into subgoals or smaller plans, structuring complex behavior.

<!-- qard-id: ais-a996b950db97b387684d -->
> [!qard]- What is a POMDP?
> A partially observable Markov decision process modeling uncertain state inferred from observations.

<!-- qard-id: ais-9cef3b0a48bdfebbe842 -->
> [!qard]- What is a dynamic decision network?
> A probabilistic model of changing beliefs, decisions, and utility over time.

<!-- qard-id: ais-279c0c78544db297662e -->
> [!qard]- Why extend BDI with POMDPs or dynamic decision networks?
> To use uncertain beliefs and stochastic outcomes in decision-making while retaining explicit commitments.

### Operational Decision-Making And Probabilistic BDI

<!-- qard-id: ais-4a11268261c7bb0c80ec -->
> [!qard]- What decision does the sugarcane-grower application model?
> When and how much cane to burn before cutting and mill delivery, under operational constraints in the specified supply chain.

<!-- qard-id: ais-94033031f7c4534b0ff1 -->
> [!qard]- What information constrains the grower’s decision?
> Weather/forecasts, weekly quota, cane awaiting delivery, mill delivery status, grower size, and maximum daily delivery rate.

<!-- qard-id: ais-cb94c2994e1294bac59b -->
> [!qard]- What explicit overrides appear in the grower controller?
> Emergencies and Sundays override ordinary utility-based burning decisions.

<!-- qard-id: ais-56da229a9857ea45f15d -->
> [!qard]- Why should the grower rules not be generalized into agricultural advice?
> They model one operational scenario; they are not a general prescription for burning practice.

### The Dynamic Bayesian Decision Network

<!-- qard-id: ais-4f8a05982b7c5b3d9441 -->
> [!qard]- What is Bayesian inference?
> Updating probabilities using observed evidence.

<!-- qard-id: ais-eac6fedac34789a6c7d8 -->
> [!qard]- What do decision and utility nodes represent?
> A choice available to the agent, and the desirability of outcomes respectively.

<!-- qard-id: ais-5d8b65ddd1bb70b09583 -->
> [!qard]- What temporal dependencies determine cane dryness in the DDN?
> Previous dryness and observed rain, wind, and maximum temperature influence later dryness.

<!-- qard-id: ais-f9508875035b1463c814 -->
> [!qard]- What determines burning conditions and advance requirements?
> Current weather forecasts and dryness affect conditions; next-four-day rain/wind forecasts affect advance requirements.

<!-- qard-id: ais-afac5fe2a66daf8b670d -->
> [!qard]- What determines current burning requirements and utility?
> Delivery needs and grower size relate to current requirements; utility depends on the burning decision, conditions, and requirements.

<!-- qard-id: ais-7198b1e5c78f40070b80 -->
> [!qard]- How are new observations used in the decision network?
> Enter them as evidence and revise probabilistic beliefs; forecasts are not treated as certain facts.

<!-- qard-id: ais-1061296f60d8ca9ff2ee -->
> [!qard]- What general expected-utility intention-selection expression is given?
> $I_t\in\arg\max_{i\in\mathcal I_t}\sum_sP(s\mid P_{1:t})U(i,s)$, using accumulated percepts and admissible decisions.

<!-- qard-id: ais-7f8c3392171faefa41c0 -->
> [!qard]- What numerical DDN details are absent from the source?
> The exact CPTs and utility function, so numerical optimal burning amounts cannot be reconstructed from the note alone.

### Probabilistic BDI Control Loop

<!-- qard-id: ais-08e241f6fe029afa76d2 -->
> [!qard]- How is the grower’s probabilistic BDI loop initialized?
> Set $t=0$, initial beliefs from the DDN, desire set $D$, empty intention $I_0$, grower size, and maximum daily delivery rate.

<!-- qard-id: ais-eb71ec15e218ab995a5e -->
> [!qard]- What inputs feed the named burning-requirements calculation?
> Cane awaiting delivery, delivery status, maximum daily delivery rate, and grower size; the source does not define its numerical formula.

<!-- qard-id: ais-5d76e92686f9928d43bc -->
> [!qard]- What observation-processing stages precede intention selection?
> Advance time, obtain/discretize observations, calculate requirements, enter percepts as evidence, and revise beliefs by Bayesian inference.

<!-- qard-id: ais-996a480ae48d6df67949 -->
> [!qard]- What is the grower controller’s priority order?
> Emergency first, Sunday second, milling season utility maximization third.

<!-- qard-id: ais-9253b393971207e9c862 -->
> [!qard]- What intentions and burning choices do emergency and Sunday branches select?
> Address the emergency or rest respectively, fixing the burning decision to no cane in either branch.

<!-- qard-id: ais-716339464e3cca3f2b29 -->
> [!qard]- What does the milling-season branch select?
> The decision-network state with highest utility, based on the revised beliefs and requirements.

<!-- qard-id: ais-aa2599ac70f4645ee34c -->
> [!qard]- What off-season completeness issue remains in the displayed pseudocode?
> No explicit fallback is given when no condition holds; an implementation must avoid accidentally reusing an old intention.

<!-- qard-id: ais-8e76f0ab3e7c68a1fee1 -->
> [!qard]- Are rain and wind separate priority branches in the displayed code?
> No. They influence the network’s burning conditions rather than appearing as separate branches.

### Rational, Human-Like, Reactive, Or Deliberative?

<!-- qard-id: ais-076571a39017683bcfb9 -->
> [!qard]- How does BDI relate to human-like and rational behavior?
> It draws on human practical reasoning and coherent goal pursuit; probabilistic extensions can explicitly maximize utility without guaranteeing correctness.

<!-- qard-id: ais-909cfe20f36b483e863d -->
> [!qard]- Can BDI contain reactive as well as deliberative behavior?
> Yes. Intention/plan selection is deliberative, while event-triggered plans can respond quickly; concrete systems can be hybrid.

<!-- qard-id: ais-ff46e7c20b3288f218e1 -->
> [!qard]- How does BDI differ from a pure learned policy such as deep RL?
> BDI exposes beliefs, goals, plans, and commitments; learned policies encode much behavior in parameters and can be harder to inspect.

<!-- qard-id: ais-6abdd22afbd30ce3c413 -->
> [!qard]- What engineering effort and adaptation distinguish BDI and deep RL?
> BDI requires knowledge/plan engineering and adapts through beliefs/plan selection; deep RL requires data, rewards, and exploration and adapts through learning or state features.

<!-- qard-id: ais-ee3604e645b5aa24fd3d -->
> [!qard]- Can BDI and learned policies both handle uncertainty?
> Yes. BDI can incorporate probabilistic reasoning, while learned policies can train under stochastic experience; hybrids can combine them.

<!-- qard-id: ais-c768efefae3f0a62db3c -->
> [!qard]- Does either BDI or deep RL guarantee generalization?
> No. Both require evaluation, and hybrids can retain BDI commitments while using learned perception or decision components.
