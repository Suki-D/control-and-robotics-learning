import numpy as np
import matplotlib.pyplot as plt

# define the ODE: dx/dt = -x
def dynamics(x):
    return -x
"""
# simulation parameters
dt = 0.01 # time step
T = 5.0 # total simulation time
time = np.arange(0, T, dt)

# initial condition
x = 1.0
trajectory = []

# Euler integration
for t in time:
    trajectory.append(x)
    x = x + dt * dynamics(x)

# Plot result
plt.figure()
plt.plot(time, trajectory)
plt.xlabel("Time (s)")
plt.ylabel("State x")
plt.title("Simulation of dx/dt = -x")
plt.grid()
plt.show()
"""
# Encapsulate into a function
def euler_simulation(x0, dt, T):
    time = np.arange(0, T, dt)
    x = x0
    trajectory = []

    for t in time:
        trajectory.append(x)
        x = x + dt * dynamics(x)

    return time, trajectory
"""
time, trajectory = euler_simulation(x0=1.0, dt=0.01, T=5.0)
plt.figure()
plt.plot(time, trajectory)
plt.xlabel("Time (s)")
plt.ylabel("State x")
plt.title("Simulation of dx/dt = -x")
plt.grid()
plt.show()
"""
# Runge-Kutta (RK4)
def rk4_simulation(x0, dt, T):
    time = np.arange(0, T, dt)
    x = x0
    trajectory = []

    for t in time:
        trajectory.append(x)

        k1 = dynamics(x)
        k2 = dynamics(x + 0.5 * dt * k1)
        k3 = dynamics(x + 0.5 * dt * k2)
        k4 = dynamics(x + dt * k3)

        x = x + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return time, trajectory

# Compare Euler vs RK4
dt = 0.5
T = 5.0

time_euler, traj_euler = euler_simulation(x0 = 1.0, dt = dt, T = T)
time_rk4, traj_rk4 = rk4_simulation(x0 = 1.0, dt = dt, T = T)

plt.figure()
plt.plot(time_euler, traj_euler, label = "Euler")
plt.plot(time_rk4, traj_rk4, label = "RK4")
plt.xlabel("Time (s)")
plt.ylabel("State x")
plt.title("Euler vs RK4 Simulation")
plt.legend()
plt.grid()
plt.show()
