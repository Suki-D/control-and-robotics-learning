# Week 3: MATLAB + Control Toolbox Introduction

## Focus
- MATLAB as a control system design environment
- Control Toolbox objects: tf, ss
- Time-domain system response
- Introductory PID control (no derivations)

## Key Goal
Shift from explicit state simulation (Python-style)
to system-level modeling and analysis.

## Tool
MATLAB

## Learning Progression
### Day 1: MATLAB Basics and Python-to-MATLAB Transition
Today I reimplemented a familiar mass–spring–damper system in MATLAB
using the built-in ODE solver `ode45`.

The goal was to become comfortable with basic MATLAB syntax,
function handles, vector-based state representation,
and plotting system responses, serving as a transition
from Python-based simulation to MATLAB-based control tools.

### Day 2: Transfer functions and step response
Today I learned how to represent a physical system using a transfer
function in MATLAB and analyze its behavior using step response.

This marked a shift from state-based simulation to an input–output
control perspective, laying the foundation for classical control
analysis and design.

### Day 3: State-space models and lsim
Reformulated the mass–spring–damper system into a state-space model
and explored different system responses using MATLAB.

Compared step response, initial-condition response, and response
to arbitrary inputs, developing intuition for how the same system
behaves under different excitations.

### Day 4: Poles, damping, and frequency intuition
Explored the relationship between system poles and time-domain behavior 
using MATLAB's Control Toolbox.
By varying damping and natural frequency in second-order systems, I 
developed intuition for how pole locations determine stability, oscillatory 
behavior, and response speed.
Used pole–zero maps to connect complex-conjugate poles with oscillations 
and reinforced the criterion that system stability requires all poles to 
lie in the left half-plane.

### Day 5: PID control (tuning by behavior)
Learned how PID control affects closed-loop system behavior using MATLAB.
By tuning gains based on step response, I observed that Kp speeds up the 
response, Kd reduces overshoot and oscillations, and Ki removes steady-state 
error.
I also built intuition for which gain to adjust based on observed behavior 
(slow response, overshoot, steady-state error), focusing on understanding 
PID through system response rather than derivations.

### Day 6: Reproduction of a textbook control example
Reproduced a classic DC motor speed control example using MATLAB's Control Toolbox.
Starting from the physical model of the motor, I derived the transfer 
function and implemented an equivalent state-space representation.
I verified that the transfer function and state-space models describe the 
same system by comparing their step responses.

After establishing the open-loop behavior, I added unit feedback and 
observed the limitations of the uncontrolled system.
A PID controller was applied to improve rise time and eliminate steady-state 
error, with limited impact on oscillatory behavior due to the non-oscillatory 
nature of the plant.
This exercise helped reinforce the connection between physical modeling, 
system representation (tf vs. ss), and feedback control behavior.

### Day 7: Reflection and conceptual consolidation
This week helped me transition from simulating dynamics directly to modeling 
systems at a higher level using transfer functions and state-space 
representations, and understanding how feedback actively shapes system 
behavior.


#### process diagram：

Physical system

      ↓

Differential equations

      ↓

State-space / Transfer function

      ↓

Open-loop behavior

      ↓

Feedback (PID)

      ↓

Shaped system response
