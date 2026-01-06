# F = -kx = ma = m (x'')
# Let x1 = x, x2 = x'

import numpy as np
import matplotlib.pyplot as plt

def dynamics(state, m = 1.0, c = 0.2, k = 1.0):
    x, v = state
    dxdt = v
    dvdt = -(k/m) * x - (c/m) * v
    return np.array([dxdt, dvdt])

def euler_simulation(x0, dt, T):
    time = np.arange(0, T, dt)
    state = np.array(x0)
    trajectory = []

    for t in time:
        trajectory.append(state.copy())
        state = state + dt * dynamics(state)

    return time, np.array(trajectory)

def rk4_simulation(x0, dt, T):
    time = np.arange(0, T, dt)
    state = np.array(x0)
    trajectory = []

    for t in time:
        trajectory.append(state.copy())

        k1 = dynamics(state)
        k1 = dynamics(state)
        k2 = dynamics(state + 0.5 * dt * k1)
        k3 = dynamics(state + 0.5 * dt * k2)
        k4 = dynamics(state + dt * k3)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return time, np.array(trajectory)

dt = 0.01
T = 10.0
x0 = [1.0, 0.0]

time,traj = rk4_simulation(x0, dt, T)

plt.figure()
plt.plot(time, traj[:, 0], label="Position x")
plt.plot(time, traj[:, 1], label="Velocity v")
plt.xlabel("Time (s)")
plt.ylabel("State")
plt.title("Mass–Spring–Damper System")
plt.legend()
plt.grid()
plt.show()


# add control input
def dynamics(state, u = 0.0, m = 1.0, c = 0.2, k = 1.0):
    x, v = state
    dxdt = v
    dvdt = -(k/m) * x - (c/m) * v + u/m
    return np.array([dxdt, dvdt])

def pd_control(state, Kp=5.0, Kd=2.0):
    x, v = state
    return -Kp * x - Kd * v

def rk4_simulation(x0, dt, T):
    time = np.arange(0, T, dt)
    state = np.array(x0)
    trajectory = []

    for t in time:
        trajectory.append(state.copy())

        k1 = dynamics(state)
        k1 = dynamics(state)
        k2 = dynamics(state + 0.5 * dt * k1)
        k3 = dynamics(state + 0.5 * dt * k2)
        k4 = dynamics(state + dt * k3)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return time, np.array(trajectory)

def rk4_control(x0, dt, T):
    time = np.arange(0, T, dt)
    state = np.array(x0)
    trajectory = []

    for t in time:
        trajectory.append(state.copy())

        u = pd_control(state)

        k1 = dynamics(state, u)
        k1 = dynamics(state, u)
        k2 = dynamics(state + 0.5 * dt * k1, u)
        k3 = dynamics(state + 0.5 * dt * k2, u)
        k4 = dynamics(state + dt * k3, u)

        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return time, np.array(trajectory)

dt = 0.01
T = 10.0
x0 = [1.0, 0.0]

time_free,traj_free = rk4_simulation(x0, dt, T)
time_ctrl,traj_ctrl = rk4_control(x0, dt, T)

plt.figure()
plt.plot(time_free, traj_free[:, 0], label="Uncontrolled x")
plt.plot(time_ctrl, traj_ctrl[:, 0], label="Controlled x")
plt.xlabel("Time (s)")
plt.ylabel("Position x")
plt.title("Effect of PD Control")
plt.legend()
plt.grid()
plt.show()