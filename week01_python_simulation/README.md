# Week 1: Python Simulation of Dynamic Systems

## Focus:
- Ordinary Differential Equations (ODEs)
- Numerical integration
- Time-domain simulation

## Goals:
- Translate mathematical models into code
- Observe how system states evolve over time
- Build intuition for dynamic behavior

## Tools:
- Python
- NumPy
- Matplotlib


## Learning Progression
### Day 1: First ODE Simulation

Implemented a simple first-order ODE dx/dt = -x and simulated it
using Euler integration.

This experiment helped build intuition for how system state evolves
over time and how numerical integration approximates continuous dynamics.

### Day 2: Numerical Stability and Time Step Effects

Explored how the Euler method behaves with larger time steps.
Observed that even a stable continuous-time system can exhibit
unstable or unrealistic behavior when simulated with an overly
large step size.

This experiment highlighted the importance of numerical stability
in simulation-based analysis.

### Day 3: Runge–Kutta (RK4) Integration

Implemented a fourth-order Runge–Kutta (RK4) method and compared it
with Euler integration under the same time step.

Observed that RK4 provides significantly improved accuracy and stability,
even with relatively large time steps, highlighting its importance in
engineering simulations.

### Day 4: Error Analysis and Time-Step Sensitivity

Compared numerical solutions against the analytical solution
x(t) = exp(-t) to quantify integration error.

Plotted absolute error on a logarithmic scale and observed that
RK4 maintains significantly lower error than Euler over time.

Additionally explored how different time step sizes affect
numerical behavior, reinforcing that numerical instability can
arise from the integration method rather than the underlying system.

### Day 5: Second-Order Mass–Spring System

Implemented a second-order mass–spring–damper system and reformulated
it as a first-order state-space model.

Simulated the system using numerical integration and observed
oscillatory behavior with gradual energy decay due to damping.

This experiment connected physical system dynamics with the
state-space representation commonly used in control and robotics.

### Day 6: Adding Control Input (PD Control)

Extended the mass–spring–damper system by introducing an external
control input representing applied force.

Implemented a simple proportional–derivative (PD) controller and
simulated the closed-loop system.

Observed significantly faster convergence and reduced oscillations
compared to the uncontrolled system, demonstrating the effect of
feedback control.

### Day 7: Closed-Loop Behavior and Stability Intuition

Using the mass–spring–damper model with PD control developed in Days 5–6,
this day focused on understanding how control gains shape closed-loop behavior.

By varying proportional and derivative gains independently, different dynamic
responses such as oscillatory, overdamped, and near-critically damped behaviors
were observed.

Developed physical intuition for how control parameters influence system
responsiveness and stability, beyond numerical integration effects.