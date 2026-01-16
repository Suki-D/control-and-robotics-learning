clear; clc;

m = 1.0;
c = 0.4;
k = 1.0;

% ODE -> State Space
% x1 = position
% x2 = velocity
% x1_dot = x2
% x2_dot = -(k/m)x1 - (c/m)x2 + u/m
% Then this system can be written:
% [x1'    =   [0     1      *  [x1   +   [0      * u
%  x2']       -k/m  -c/m]       x2]      1/m]


% Construct a state-space matrix
A = [0 1;
    -k/m -c/m];
B = [0; 1/m];
C = [1 0];
D = 0;

% Create a state-space system object
sys = ss(A, B, C, D);

% Step response
figure;
step(sys);
title('Step Response');

% Initial Reponse
x0 = [1; 0];

figure;
initial(sys, x0);
title('Initial Repsonse');

% lsim (any input)
t = 0:0.01:30;
u = sin(t)';  % column vector

figure;
lsim(sys, u, t);
title('Response to Sinusoidal Input')
