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

time, trajectory = euler_simulation(x0=1.0, dt=0.01, T=5.0)
plt.figure()
plt.plot(time, trajectory)
plt.xlabel("Time (s)")
plt.ylabel("State x")
plt.title("Simulation of dx/dt = -x")
plt.grid()
plt.show()