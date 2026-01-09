# Previous: θ → 0
# Goal: θ(t) → θ_ref(t)

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 1.0

def pendulum_nonlinear_dynamics(state, u):
    theta, omega = state
    dtheta = omega
    domega = - (g / l) * np.sin(theta) + u
    return np.array([dtheta, domega])

# θ_ref(t) = A * sin(ω t)
def reference(t):
    A = 0.5
    w = 0.5
    theta_ref = A * np.sin(w * t)
    omega_ref = A * w * np.cos(w * t)
    return theta_ref, omega_ref

# We want PD control know where I want to go
def pd_tracking_control(state, t, Kp, Kd):
    theta, omega = state
    theta_ref, omega_ref = reference(t)

    e = theta - theta_ref
    e_dot = omega - omega_ref

    u = -Kp * e - Kd * e_dot
    return u

def rk4_control_simulation(x0, dt, T, Kp, Kd):
    time = np.arange(0, T, dt)
    state = np.array(x0, dtype=float)
    trajectory = []
    reference_traj = []

    for t in time:
        trajectory.append(state.copy())

        theta_ref, _ = reference(t)
        reference_traj.append(theta_ref)

        u = pd_tracking_control(state, t, Kp, Kd)

        k1 = pendulum_nonlinear_dynamics(state, u)
        k2 = pendulum_nonlinear_dynamics(state + 0.5 * dt * k1, u)
        k3 = pendulum_nonlinear_dynamics(state + 0.5 * dt * k2, u)
        k4 = pendulum_nonlinear_dynamics(state + dt * k3, u)

        state = state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    return time, np.array(trajectory), np.array(reference_traj)

dt = 0.01
T = 50.0
x0 = [0.2, 0.0]

Kp = 5.0
Kd = 7.0

time, traj, ref = rk4_control_simulation(x0, dt, T, Kp, Kd)

plt.figure(figsize=(8, 5))
plt.plot(time, traj[:, 0], label = "θ")
plt.plot(time, ref, "--", label = "θ_ref")
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Tracking Control on a Nonlinear Pendulum")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(time, traj[:, 0] - ref)
plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Tracking Error")
plt.grid()
plt.show()


# Experiments: Change reference frequency
def reference(t, A= 0.5, w = 0.5):
    theta_ref = A * np.sin(w * t)
    omega_ref = A * w * np.cos(w * t)
    return theta_ref, omega_ref

# We want PD control know where I want to go
def pd_tracking_control(state, t, Kp, Kd, w):
    theta, omega = state
    theta_ref, omega_ref = reference(t, w = w)

    e = theta - theta_ref
    e_dot = omega - omega_ref

    u = -Kp * e - Kd * e_dot + (g/l)*np.sin(theta_ref) # Add gravity feedforward compensation.
    return u

def rk4_control_simulation(x0, dt, T, Kp, Kd, w):
    time = np.arange(0, T, dt)
    state = np.array(x0, dtype=float)
    trajectory = []
    reference_traj = []

    for t in time:
        trajectory.append(state.copy())

        theta_ref, _ = reference(t, w=w)
        reference_traj.append(theta_ref)

        u = pd_tracking_control(state, t, Kp, Kd, w)

        k1 = pendulum_nonlinear_dynamics(state, u)
        k2 = pendulum_nonlinear_dynamics(state + 0.5 * dt * k1, u)
        k3 = pendulum_nonlinear_dynamics(state + 0.5 * dt * k2, u)
        k4 = pendulum_nonlinear_dynamics(state + dt * k3, u)

        state = state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    return time, np.array(trajectory), np.array(reference_traj)

dt = 0.01
T = 15.0
x0 = [0.0, 0.0]

Kp = 10.0
Kd = 4.0

frequencies = [0.3, 1.0, 3.0]

plt.figure(figsize=(10, 6))

for w in frequencies:
    time, traj, ref = rk4_control_simulation(
        x0=x0, dt=dt, T=T, Kp=Kp, Kd=Kd, w=w)
    plt.plot(time, traj[:, 0], label = f"θ (ω = {w})")
    plt.plot(time, ref, "--", label=f"θ_ref (ω = {w})")


plt.xlabel("Time (s)")
plt.ylabel("Angle θ (rad)")
plt.title("Day 5: Effect of Reference Frequency on Tracking")
plt.legend()
plt.grid()
plt.show()

# Plot tracking error
plt.figure(figsize=(10, 5))
for w in frequencies:
    time, traj, ref = rk4_control_simulation(
        x0=x0, dt=dt, T=T, Kp=Kp, Kd=Kd, w=w)
    error = traj[:, 0] - ref
    plt.plot(time, error, label=f"error (ω = {w})")

plt.xlabel("Time (s)")
plt.ylabel("Tracking error (rad)")
plt.title("Tracking Error vs Reference Frequency")
plt.legend()
plt.grid()
plt.show()