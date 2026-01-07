# pendulum function: θ'' + (g / l) * sin(θ) = 0
# Let x1 = θ, x2 = θ'

import numpy as np
import matplotlib.pyplot as plt

def pendulum_dynamics(state, g = 9.81, l = 1.0):
    theta, omega = state
    dtheta = omega
    domega = - (g / l) * np.sin(theta)
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

# small angel vs. large angle
if __name__ == "__main__":
    dt = 0.01
    T = 10.0

    x0_small = [0.2, 0.0]
    x0_large = [3.0, 0.0]

    time_s, traj_s = rk4_simulation(pendulum_dynamics, x0_small, dt, T)
    time_l, traj_l = rk4_simulation(pendulum_dynamics, x0_large, dt, T)

    plt.figure(figsize=(8, 5))
    plt.plot(time_s, traj_s[:, 0], label="Small angle")
    plt.plot(time_l, traj_l[:, 0], label="Large angle")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle θ (rad)")
    plt.title("Nonlinear Pendulum Dynamics")
    plt.legend()
    plt.grid()
    plt.show()