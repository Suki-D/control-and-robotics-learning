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