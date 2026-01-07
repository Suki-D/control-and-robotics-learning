# PD control
# u = - Kp * θ - Kd * θ'

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 1.0

def pendulum_nonlinear_dynamics(state, u):
    theta, omega = state
    dtheta = omega
    domega = - (g / l) * np.sin(theta) + u
    return np.array([dtheta, domega])

def pd_control(state, Kp, Kd):
    theta, omega = state
    return -Kp * theta -Kd * omega

def rk4_control_simulation(x0, dt, T, Kp, Kd):
    time = np.arange(0, T, dt)
    state = np.array(x0, dtype=float)
    trajectory = []

    for t in time:
        trajectory.append(state.copy())

        # u = pd_control(state, Kp, Kd)
        u = np.clip(pd_control(state, Kp, Kd), -5.0, 5.0)

        k1 = pendulum_nonlinear_dynamics(state, u)
        k2 = pendulum_nonlinear_dynamics(state + 0.5 * dt * k1, u)
        k3 = pendulum_nonlinear_dynamics(state + 0.5 * dt * k2, u)
        k4 = pendulum_nonlinear_dynamics(state + dt * k3, u)

        state = state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    return time, np.array(trajectory)

# A: small angle comparison
dt = 0.01
T = 10.0
x0_small = [0.2, 0.0]

Kp = 5.0
Kd = 7.0

time_s, traj = rk4_control_simulation(x0_small, dt, T, Kp, Kd)

plt.figure(figsize=(8, 5))
plt.plot(time_s, traj[:, 0])
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("PD Control on Nonlinear Pendulum (Small Angle)")
plt.grid()
plt.show()


# B: large angle comparison
x0_large = [3.0, 0.0]

time_l, traj = rk4_control_simulation(x0_large, dt, T, Kp, Kd)

plt.figure(figsize=(8, 5))
plt.plot(time_l, traj[:, 0])
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("PD Control on Nonlinear Pendulum (Large Angle)")
plt.grid()
plt.show()
