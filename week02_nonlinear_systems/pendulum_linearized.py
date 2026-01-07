# When initial angel is really small, sin(θ) ≈ θ
# Then, θ'' + gθ / l = 0

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 1.0

def pendulum_nonlinear_dynamics(state):
    theta, omega = state
    dtheta = omega
    domega = - (g / l) * np.sin(theta)
    return np.array([dtheta, domega])

def pendulum_linear_dynamics(state):
    theta, omega = state
    dtheta = omega
    domega = - (g / l) * theta
    return np.array([dtheta, domega])

def rk4_simulation(dynamics, x0, dt, T):
    time = np.arange(0, T, dt)
    state = np.array(x0, dtype=float)
    trajectory = []

    for t in time:
        trajectory.append(state.copy())

        k1 = dynamics(state)
        k2 = dynamics(state + 0.5 * dt * k1)
        k3 = dynamics(state + 0.5 * dt * k2)
        k4 = dynamics(state + dt * k3)

        state = state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    return time, np.array(trajectory)

# A: small angle comparison
dt = 0.01
T = 10.0

x0_small = [0.2, 0.0]

time_s, traj_nl = rk4_simulation(pendulum_nonlinear_dynamics, x0_small, dt, T)
time_s, traj_l = rk4_simulation(pendulum_linear_dynamics, x0_small, dt, T)

plt.figure(figsize=(8, 5))
plt.plot(time_s, traj_nl[:, 0], label="Nonlinear")
plt.plot(time_s, traj_l[:, 0], label="Linearized")
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Small Angle Approximation")
plt.legend()
plt.grid()
plt.show()

# B: large angle comparison
x0_large = [1.5, 0.0]

time_l, traj_nl = rk4_simulation(pendulum_nonlinear_dynamics, x0_large, dt, T)
time_l, traj_l = rk4_simulation(pendulum_linear_dynamics, x0_large, dt, T)

plt.figure(figsize=(8, 5))
plt.plot(time_l, traj_nl[:, 0], label="Nonlinear")
plt.plot(time_l, traj_l[:, 0], label="Linearized")
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Large Angle: Linear Model Breakdown")
plt.legend()
plt.grid()
plt.show()