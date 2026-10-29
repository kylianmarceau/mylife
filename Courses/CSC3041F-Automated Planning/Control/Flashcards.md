---
tags:
  - automated-planning
---

# Control Flashcards

These cards use the Obsidian Spaced Repetition plugin inline flashcard format.

---

## Control Systems Introduction

#flashcards/CSC3041F-Automated-Planning/Control/Lecture-01-Control-Systems-Introduction

What is automation?::The use of machines or systems to perform tasks with reduced direct human intervention.
What is control?::Managing, commanding, directing, or regulating a system's behaviour to achieve a desired output.
Why is control important for automated planning?::Planning chooses what should happen; control helps make the real system behave as intended.
What is a control system?::A system that manages, commands, or regulates a device or process to achieve a desired output.
What is the input in a control system?::The reference or command given to the system.
What is the output in a control system?::The controlled variable or actual result produced by the system.
What is the plant in a control system?::The physical process or system being controlled.
What is the controller in a control system?::The mechanism or algorithm that decides what action to apply to the plant.
What is feedback in a control system?::Information about the output returned to the controller or input side of the loop.
What is a sensor in a control system?::The component that measures the current state or output of the plant.
What is a set-point?::The desired target value for a controlled variable.
What is the control error formula?::$e(t)=r(t)-y(t)$.
In $e(t)=r(t)-y(t)$, what is $r(t)$?::The reference input or desired output at time $t$.
In $e(t)=r(t)-y(t)$, what is $y(t)$?::The measured output at time $t$.
What is the controller's basic error objective?::Choose actions so that $e(t)\to0$.
What is an open-loop control system?::A control system with no feedback; it performs a fixed operation without checking the result.
What is a closed-loop control system?::A control system that uses feedback to adjust actions and maintain a desired state.
What is the open-loop control flow?::Input $\to$ Controller $\to$ Plant $\to$ Output.
What is the closed-loop control flow?::Reference $\to$ Error detector $\to$ Controller $\to$ Plant $\to$ Output $\to$ Sensor $\to$ Feedback.
What is the key difference between open-loop and closed-loop control?::Closed-loop control uses measured output to update future actions; open-loop control does not.
Why is a toaster usually open-loop?::It heats for a preset time and usually does not measure toast colour while operating.
Why is a thermostat closed-loop?::It measures room temperature, compares it to the set-point, and switches heating or cooling to reduce error.
What is an error detector?::The part of a feedback loop that compares desired input with measured feedback.
What is a common mistake when identifying a closed-loop system?::Calling any automated system closed-loop even when it does not measure output and correct error.
What are the basic closed-loop components?::Reference input, error detector, controller, plant, sensor, and feedback path.

## Open/Closed Loop Control And PID Preview

#flashcards/CSC3041F-Automated-Planning/Control/Lecture-02-Open-Closed-Loop-And-PID

What is calibration in open-loop control?::Pre-setting or tuning a system so that a chosen input should produce the expected output.
Why is open-loop control simple?::It does not need sensors, feedback logic, or online correction.
Name one advantage of open-loop control.::It is simple, cheap, and cannot over-correct through feedback.
Name one disadvantage of open-loop control.::It cannot automatically correct disturbances, noise, or environmental changes.
What does "no feedback implies no automatic correction" mean?::The system cannot adjust its action based on whether the output was wrong.
What is a feedback signal?::The measured output returned to the controller or error detector.
What is an actuating signal?::The controller's command sent toward the plant or actuator.
Why is closed-loop control useful under disturbances?::It measures the actual output and corrects future actions based on error.
List the repeated steps in a closed-loop controller.::Reference is supplied, output is sensed, error is computed, controller acts, plant responds, output is measured again.
What is state space in control?::The set of variables needed to describe the current condition of a system.
What are dynamics in control?::Rules that describe how the system state changes over time.
What is the general discrete-time state-space model?::$x_{t+1}=f(x_t,u_t)$.
What does $x_t$ mean in $x_{t+1}=f(x_t,u_t)$?::The system state at time $t$.
What does $u_t$ mean in $x_{t+1}=f(x_t,u_t)$?::The control action at time $t$.
What is the linear discrete-time state-space model?::$x_{t+1}=Ax_t+Bu_t$.
In $x_{t+1}=Ax_t+Bu_t$, what does $A$ represent?::How the current state naturally evolves.
In $x_{t+1}=Ax_t+Bu_t$, what does $B$ represent?::How the control input affects the next state.
What is stability?::The property that a system returns to equilibrium or stays bounded after a disturbance.
What is equilibrium?::A state where the system can remain without changing if no disturbance occurs.
What is noise in control?::Unwanted variation or disturbance affecting measurements or system behaviour.
What is a cost function?::A mathematical penalty that the controller tries to minimise.
What is a common squared-error tracking objective?::$J=\sum_{t=0}^{T}e_t^2$.
What objective penalises both tracking error and control effort?::$J=\sum_{t=0}^{T}(e_t^2+\lambda u_t^2)$.
In $J=\sum(e_t^2+\lambda u_t^2)$, what does $\lambda$ control?::The trade-off between accurate tracking and low control effort.
What is a mathematical model in control?::An explicit mathematical representation of a system's dynamics.
Why use a model in control?::For prediction, efficient planning, and explicit constraint handling.
What is model-based control?::Control that relies on an explicit model of the plant.
What is model-free control?::Control that does not use an explicit mathematical model of the plant.
When does model-based control work well?::When the model is accurate enough and optimisation can be solved fast enough.
When does model-based control struggle?::When the model is wrong, too complex, or missing important disturbances.
What is a PID controller?::A model-free closed-loop controller using proportional, integral, and derivative error terms.
What is the continuous-time PID equation?::$u(t)=K_p e(t)+K_i\int_0^t e(\tau)\,d\tau+K_d\frac{de(t)}{dt}$.
What does the proportional term in PID react to?::Current error.
What does the integral term in PID react to?::Accumulated past error.
What does the derivative term in PID react to?::The rate of change of error.
What is the time intuition for PID terms?::Proportional is present error, integral is past accumulated error, derivative is future trend.
What PID term helps remove steady-state offset?::The integral term.
What PID term helps reduce overshoot and damp oscillation?::The derivative term.
What PID term pushes harder when current error is large?::The proportional term.
What is the usual PID objective?::Make $e(t)\to0$ while avoiding excessive overshoot, oscillation, or slow response.
What is a common PID misconception?::Thinking PID is model-based; in these notes it is model-free feedback control.

## Model-Based, Model-Free, And PID Control

#flashcards/CSC3041F-Automated-Planning/Control/Lecture-03-Model-Based-Model-Free-And-PID-Control

What are the four main components of a control system?::Plant/process, sensor, controller, and actuator.
What is an actuator?::The component that physically carries out the controller's command.
Give examples of actuators.::Motors, valves, heaters, brakes, pumps, or steering mechanisms.
Give examples of sensors.::GPS, accelerometers, thermometers, cameras, pressure sensors, or level sensors.
What is the feedback-control relationship using a controller rule?::$u_t=\pi(y_t,r_t)$.
In $u_t=\pi(y_t,r_t)$, what does $u_t$ represent?::The control action at time $t$.
In $u_t=\pi(y_t,r_t)$, what does $\pi$ represent?::The controller rule or policy.
What is error in closed-loop classification?::The difference between desired state and actual state.
What is model mismatch?::When the mathematical model does not match the real plant.
Why can model mismatch be dangerous?::It can cause poor performance, bad predictions, or instability.
What is a differential equation in control?::An equation describing how a quantity changes continuously over time.
What is the continuous-time dynamics form?::$\dot{x}(t)=f(x(t),u(t))$.
What is Model Predictive Control (MPC)?::A model-based method that predicts future behaviour and optimises actions over a future horizon.
Why is MPC considered planner-like?::It predicts consequences before acting and chooses actions through optimisation.
Name one advantage of model-based control.::Efficiency, predictability, constraint handling, interpretability, or transferability.
Name one disadvantage of model-based control.::Model mismatch, computational cost, modelling complexity, unmodelled dynamics, or maintenance.
Why is model-based control often interpretable?::Decisions can be traced through equations, predictions, and constraints.
Why can model-based control transfer between similar systems?::A physics-based model may apply to equivalent plants with similar dynamics.
What is a policy in model-free control?::A mapping from measured state or error to action.
What is a learned policy?::A policy obtained from data, experience, simulation, or examples.
What are two model-free controller mappings?::$u_t=\pi(x_t)$ and $u_t=\pi(e_t)$.
Why is model-free control attractive?::It avoids deriving exact plant dynamics and can handle complex systems when enough data is available.
Name one advantage of model-free control.::Versatility, fast prototyping, creative learned behaviour, or usefulness for complex tasks.
Name one disadvantage of model-free control.::Exposure dependence, data hunger, unsafe exploration, or weaker safety/stability guarantees.
Why can model-free control be risky on real hardware?::Learning by exploration may require failures that damage the real system.
What is SISO?::Single-input single-output.
What is MIMO?::Multiple-input multiple-output.
What are linear dynamics?::Dynamics where superposition approximately applies.
What are non-linear dynamics?::Dynamics where responses are not proportional or additive.
What is tracking in control?::Trying to follow a desired set-point or trajectory.
What is optimisation in control?::Choosing actions to minimise or maximise an objective.
Why is PID usually described as SISO tracking control?::It is typically tuned to minimise error for one controlled output using one control input.
Why does PID work best near a set-point where behaviour is approximately linear?::Fixed gains can perform well when system response is predictable and proportional around that operating region.
Why can PID struggle with MIMO systems?::Interactions between multiple inputs and outputs make separate fixed feedback loops harder to tune.
What is a PID drawback under complex dynamics?::Fixed gains and simple error terms may not capture nonlinear interactions or high uncertainty.
What can make PID decision speed an issue?::Demanding systems with fast dynamics, many variables, or complex constraints.
In cruise control, what does proportional control do?::Pushes harder when the speed error is larger.
In cruise control, what does integral control do?::Corrects persistent speed offset over time.
In cruise control, what does derivative control do?::Damps rapid changes in speed error to reduce overshoot.
For water tank level control, what is the plant?::The water tank and its inflow/outflow dynamics.
For water tank level control, what is the controlled output?::The water level.
For water tank level control, what is a likely actuator?::A valve or pump controlling inflow/outflow.
When does model-free control make sense?::When explicit modelling is too hard, but data or simulation can safely support learning.

## Reinforcement Learning For Control

#flashcards/CSC3041F-Automated-Planning/Control/Lecture-04-Reinforcement-Learning-For-Control

What are plant characteristics?::Properties of the controlled system that affect controller choice.
List three plant characteristics that affect controller design.::Linearity, model availability, uncertainty, external forces, task repetitiveness, and number of inputs/outputs.
What is superposition?::The property that combined inputs produce the sum of their separate effects.
What is an external force in control?::A disturbance or influence from outside the controller-plant pair.
What is a repetitive task?::A task with repeated, predictable structure.
What is uncertainty in control?::Incomplete knowledge about state, dynamics, environment, or future disturbances.
When is classical control usually more natural than RL?::When dynamics are linear, a strong model exists, uncertainty is limited, and the task is mostly fixed tracking.
When is RL often more natural than classical PID?::For non-linear, uncertain, MIMO, adaptive tasks where explicit modelling is difficult.
How does PID compare with RL on SISO versus MIMO?::PID is usually SISO; RL can handle MIMO more naturally.
How does PID compare with RL on linearity?::PID is strongest near linear operating regions; RL can learn non-linear control policies.
How does PID compare with RL on adaptability?::PID is fixed after tuning; RL can continue learning or adapt if designed for online learning.
What is reinforcement learning in control?::Learning by interaction where a controller-agent chooses actions and receives rewards.
What is an RL agent in control?::The decision-making learner choosing control actions.
What is an RL policy?::A mapping from states to actions or action probabilities.
What is online learning?::Learning that continues while the system is operating.
What is the deterministic RL control-policy equation?::$a_t=\pi(s_t)$.
What is the stochastic RL control-policy equation?::$a_t\sim\pi(\cdot\mid s_t)$.
What is the RL objective for control?::$J(\pi)=\mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty}\gamma^t r_t\right]$.
In the RL objective, what does $\gamma$ do?::It discounts future rewards.
What is cartpole?::A benchmark task where a controller moves a cart to keep a hinged pole upright.
What is a typical cartpole state?::$s_t=(x_t,\dot{x}_t,\theta_t,\dot{\theta}_t)$.
In cartpole, what is $x_t$?::Cart position.
In cartpole, what is $\dot{x}_t$?::Cart velocity.
In cartpole, what is $\theta_t$?::Pole angle from upright.
In cartpole, what is $\dot{\theta}_t$?::Pole angular velocity.
What is a typical cartpole action?::A force $F_t$ or a discrete push-left/push-right action.
What is the cartpole control goal?::Keep $\theta_t\approx0$ while keeping the cart on the track.
How does a tuned PID controller often behave initially on cartpole?::Smooth if tuned well.
How can an early RL agent behave on cartpole?::Jittery or sub-optimal before enough training.
Why can debugging PID be easier than debugging neural RL?::PID equations and gains are inspectable; neural RL policies are often black-box.
What is automation?::Following predefined rules for a repetitive task.
What is autonomy?::Adapting behaviour to achieve goals in uncertain or changing environments.
When is automation appropriate?::When the environment and task are stable and repetitive.
When is autonomy more appropriate?::When the system must decide under changing or uncertain conditions.
What is a direct RL controller?::An RL agent that directly outputs low-level control signals.
What is a benefit of direct RL control?::It can learn complex non-linear movements.
What is a risk of direct RL control?::Safety is hard to guarantee and the policy may be a black box.
What is hierarchical control?::Low-level controllers handle fast tracking while a high-level controller sets goals or set-points.
How can RL and PID be combined hierarchically?::RL chooses high-level set-points or decisions; PID handles low-level tracking.
What is system identification?::Learning or estimating a model of a system from data.
How can RL support system identification?::It can learn model parameters such as $A$ and $B$ in $x_{t+1}=Ax_t+Bu_t$.
After learning $A$ and $B$, what can use the model?::A model-based controller such as MPC.
What is simulation in the RL-control pipeline?::Training or testing a controller in a virtual environment.
Why use simulation before hardware deployment?::It is safer and allows large-scale data collection.
What is domain randomisation?::Randomising simulation parameters to make the learned controller robust to real-world variation.
Why does domain randomisation help sim-to-real transfer?::Training under many simulated conditions makes the real world less surprising.
What is deployment?::Running the controller on the real system.
Why is deployment risky?::Real sensors, delays, actuators, and failures may differ from simulation.
What is LIDAR?::A sensing technology that measures distance using light pulses.
What is a micro-grid?::A local energy grid that manages distributed energy sources and loads.
What is disturbance rejection?::A controller's ability to compensate for external disturbances.
Why can RL fit autonomous underground mining vehicles?::Tunnels are uncertain and difficult to model completely.
Why can RL fit micro-grid load balancing?::Renewable wind and solar supply are non-linear and unpredictable.
Why can RL fit precision spraying drones?::Wind disturbances and orchard conditions require real-time adaptation.
What is Safe RL?::RL designed to avoid unsafe actions during learning or deployment.
What is shielding in Safe RL?::A mechanism that blocks unsafe actions proposed by an RL agent.
What is a safety layer?::A layer between the RL agent and actuator that overrides physically dangerous actions.
What is the safe-RL action flow?::RL action $\to$ safety layer $\to$ motor command.
What does $a_t^{\mathrm{safe}}\ne a_t^{\mathrm{RL}}$ mean?::The safety layer overrode the RL action.
Why is safety a major issue in RL control?::Exploration can damage real hardware, and deep RL usually lacks classical stability proofs.
Why does classical control often have stronger safety arguments than deep RL?::Classical controllers can sometimes be analysed with mathematical stability proofs.
What should a safety layer do if RL suggests torque above hardware limits?::Clip or override the action to a safe torque.
What is a common mistake when comparing PID and RL?::Treating RL as always better; PID is often better for simple, near-linear SISO tracking.
What is a common mistake in RL-control deployment?::Assuming simulation performance will transfer directly to real hardware without robustness testing.
What is a common mistake about hierarchical control?::Thinking RL must replace PID entirely instead of using RL for high-level decisions and PID for low-level tracking.
