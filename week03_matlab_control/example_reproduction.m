% DC Motor Speed: System Modeling
% we will assume that the input of the system is the voltage source (V) applied to the motor's armature, 
% while the output is the rotational speed of the shaft (θ'). 
% The rotor and shaft are assumed to be rigid. 
% We further assume a viscous friction model, that is, 
% the friction torque is proportional to shaft angular velocity.

% Input: voltage V(t)
% Output: angular velocity ω(t)
% Define back EMF: e(t) = K * ω(t)
% Based on KVL: V(t) = L * di/dt + R * i(t) + K * ω(t)
% Current generates torque: τ(t) = K * i(t)
% J * dω/dt + b * ω(t) = τ(t), J: Moment of inertia, b: coefficient of friction

% Laplace transform
% V(s) = (Ls + R) * I(s) + K * s * θ(s)
% (Js + b) * s * θ(s) = K * I(s)
% Eliminate I(s): V(s) = [(Js + b)(Ls + R)/K + K] * s * θ(s)]
% G(s) = θ'(s) / V(s) = K / [(Js + b)(Ls + R) + K^2]

clear; clc;

s = tf('s');

% Define parameters
J = 0.01; % Moment of inertia
b = 0.1;  % Coefficient of friction
K = 0.01; % Motot constant
R = 1;    % Resistance
L = 0.5;  % Inductance

% Defien the transfer function for DC motor
G_tf = K / ((J*s + b)*(L*s + R) + K^2);
step(G_tf)
title('Open-loop DC motor speed response') 

% State-Space Model
% d/dt [i;  =  [-R/L -K/L;  *  [i;  +  [1/L;    * V
%       ω]      K/J  -b/J]      ω]      0]
% y = [0 1] * [i; ω]

A = [-R/L   -K/L;
      K/J   -b/J];
B = [1/L;
     0];
C = [0 1];   % output = ω
D = 0;

G_ss = ss(A, B, C, D);

% Verify if tf and ss are the same system
step(G_tf, G_ss)
legend('Transfer Function', 'State Space')
grid on
title('TF vs SS: Same DC Motor System')

% Add unit feedback (without controller)
H_tf = feedback(G_tf, 1);
H_ss = feedback(G_ss, 1);

step(H_tf, H_ss)
legend('TF closed-loop', 'SS closed-loop')
grid on
title('Closed-loop without controller')

% Add PID
Kp = 100;
Ki = 200;
Kd = 10;

C = pid(Kp, Ki, Kd);

H_pid_tf = feedback(C * G_tf, 1);
H_pid_ss = feedback(C * G_ss, 1);

step(H_pid_tf, H_pid_ss)
legend('PID + TF', 'PID + SS')
grid on
title('PID Controlled DC Motor Speed')