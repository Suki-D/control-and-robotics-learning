"""
ODE Basics
- Forward Euler
- RK4
- Comparison with analytical solution
- Time-step sensitivity and stability
"""

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

x_exact = np.exp(-time_euler) # solution: x(t) = e^(-t)

plt.figure()
plt.plot(time_euler, traj_euler, label = "Euler")
plt.plot(time_rk4, traj_rk4, label = "RK4")
plt.plot(time_euler, x_exact, 'k--', label="Exact")
plt.xlabel("Time (s)")
plt.ylabel("State x")
plt.title("Euler vs RK4 Simulation")
plt.legend()
plt.grid()
plt.show()

# Calculation error = |x(numerical) - x(exact)|
error_euler = np.abs(np.array(traj_euler) - x_exact)
error_rk4 = np.abs(np.array(traj_rk4) - x_exact)

plt.figure()
plt.plot(time_euler, error_euler, label="Euler Error")
plt.plot(time_euler, error_rk4, label="RK4 Error")
plt.yscale("log")
plt.xlabel("Time (s)")
plt.ylabel("Absolute Error")
plt.legend()
plt.grid()
plt.show()

# Experiments with different dt values (stability experiments)
dt_list = [0.5, 1.0, 1.5, 2.1]
T = 5.0

plt.figure()

for dt in dt_list:
    time, traj_euler = euler_simulation(x0=1.0, dt=dt, T=T)
    plt.plot(time, traj_euler, label=f"Euler dt={dt}")

plt.plot(time_euler, x_exact, 'k--', label="Exact")
plt.xlabel("Time (s)")
plt.ylabel("State x")
plt.title("Euler Stability vs Time Step")
plt.legend()
plt.grid()
plt.show()