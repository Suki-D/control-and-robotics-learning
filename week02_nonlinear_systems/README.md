# Week 2: # Week 1: Python Simulation of Dynamic Systems

## Focus:
- Nonlinear dynamic systems
- Feedback control
- Reference tracking
- Feedforward compensation
- Frequency-domain intuition in time-domain simulation

## Goals:
- Apply feedback control to nonlinear systems
- Extend regulation control to trajectory tracking
- Understand steady-state tracking error and its causes
- Study how reference frequency affects tracking performance
- Build intuition for control bandwidth and model-based compensation

## Tools:
- Python
- NumPy
- Matplotlib

## Learning Progression
### Day 1: Nonlinear Pendulum Dynamics

Implemented the full nonlinear pendulum model without small-angle
approximations.

Simulated both small-angle and large-angle motions using RK4 integration
to observe how nonlinear effects alter system behavior.

This experiment establishes the foundation for later linearization and
control of nonlinear systems.

For large initial angles, the pendulum motion remains periodic but
exhibits a longer period compared to the small-angle approximation,
highlighting the amplitude-dependent dynamics of nonlinear systems.

### Day 2: Linearization and Model Mismatch

Compared nonlinear pendulum dynamics with its linearized approximation
under small and large initial angles.

Observed that linearization provides an accurate model near equilibrium
but breaks down for large-angle motion, highlighting the importance of
model validity and the risks of model mismatch in control design.

### Day 3: Linear Control on a Nonlinear System

Designed a PD controller based on a linearized pendulum model and applied
it to the full nonlinear dynamics.

Interestingly, when the PD gains were increased to achieve near-critical 
damping in the linearized model, the performance difference between small 
and large initial angles became less pronounced.
This occurs because strong linear damping can dominate the nonlinear dynamics 
of a naturally stable pendulum, effectively masking the limitations of linear 
control in an idealized simulation without actuator saturation or model 
uncertainty.

To better reflect realistic control constraints, actuator saturation was then 
introduced by limiting the control input. With this modification, the small-angle 
response remained well-behaved, while the large-angle case exhibited noticeable 
oscillations and slower convergence. This behavior is more consistent with the 
expected degradation of linear control performance away from the linearization 
point, as input saturation prevents the controller from fully compensating for 
large deviations and allows nonlinear dynamics to play a more significant role.

### Day 4: Tracking Control on a Nonlinear Pendulum

Extended the PD controller from regulation to trajectory tracking by
introducing a time-varying reference angle.

Demonstrated that a controller designed only for stabilization fails
to track non-zero references, even though the system remains stable.

By reformulating the PD controller in terms of tracking error and
reference velocity, the pendulum was able to follow a sinusoidal
trajectory with bounded error, revealing the additional challenges
introduced by tracking control compared to point stabilization.

### Day 5: Reference Tracking on a Nonlinear Pendulum

In this experiment, a PD tracking controller was applied to a nonlinear 
pendulum to follow a sinusoidal reference trajectory with different frequencies. 
The initial expectation was that lower reference frequencies would lead to smaller 
tracking errors, since slower trajectories are generally easier to follow.

However, the simulation results showed the opposite trend: the tracking error for 
low-frequency references remained relatively large, while higher-frequency references 
exhibited smaller error amplitudes. This behavior was unexpected and suggested that factors 
other than tracking dynamics were dominating the system response.

The discrepancy was caused by the absence of gravity compensation in the control law. 
Without a feedforward term, the PD controller had to rely on a persistent tracking error 
to generate sufficient torque to counteract gravity when the reference angle was nonzero. 
As a result, low-frequency references effectively behaved like slowly varying equilibrium 
points, leading to quasi-static steady-state errors that did not diminish with decreasing 
frequency.

To address this issue, a gravity feedforward term based on the reference trajectory was 
added to the controller. This modification removed the steady-state bias caused by gravity, 
allowing the PD controller to focus solely on correcting dynamic tracking errors. After this 
change, the system behavior aligned with intuition: low-frequency references were tracked 
accurately, while tracking performance degraded as the reference frequency increased.

### Day 6: Closed-Loop Bandwidth and Frequency Limitations

With gravity feedforward included, the PD tracking controller exhibits
good performance for low-frequency reference trajectories.

In this experiment, the reference frequency was systematically varied
to examine the fundamental frequency limitations of the closed-loop
system.

As the reference frequency increased, tracking error increased despite
unchanged controller structure and gains. This behavior reflects the
finite bandwidth of the closed-loop system: beyond a certain frequency,
the system cannot respond quickly enough to follow the reference.

At high frequencies, the actual pendulum motion exhibited reduced
amplitude compared to the reference. While this can appear as a smaller
tracking error in the time domain, it is in fact a result of attenuation
rather than successful tracking.

This experiment reinforced the concept of closed-loop bandwidth and
highlighted the importance of interpreting tracking error in the
context of system dynamics rather than time-domain appearance alone.

### Future Work
Possible extensions beyond Week 2 include:
- Adding actuator saturation to study realistic control constraints
- Introducing model mismatch or disturbances to test robustness
- Implementing feedback linearization for nonlinear systems
- Comparing PD control with PID or state feedback
- Extending tracking control to multi-link or underactuated systems

These directions naturally lead toward modern nonlinear and optimal
control methods.