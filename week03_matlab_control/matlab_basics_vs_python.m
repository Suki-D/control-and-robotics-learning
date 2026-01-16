% Mass-Spring-Damper simulation using ode45
% Purpose: Python -> MATLAB transition

clear; clc;

m = 1.0;
k = 1.0;
c = 0.4;

% x1 = position
% x2 = velocity
% x1_dot = x2
% x2_dot = -(k/m)x1 - (c/m)x2

f = @(t,x) [                    % def dynamics(t,x):
    x(2);
    -(k/m)*x(1) - (c/m)*x(2)    % dxdt = np.array([v, -(k/m)x1 - (c/m)x2])
];

% Initial conditions: [initial position, initial velocity]
x0 = [1.0; 0.0];

% Time span for the simulation
tSpan = [0 20];      % Integration from 0 to 20

% Solve the ODE
[t, x] = ode45(f, tSpan, x0);

% Plot the results
figure;
plot(t, x(:, 1), 'LineWidth', 2);
xlabel('Time(s)');
ylabel('Position x');
title('Mass-Spring-Damper Response (ode45)');
grid on;