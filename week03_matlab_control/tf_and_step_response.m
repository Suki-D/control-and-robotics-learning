clear; clc;

m = 1.0;
c = 0.4;
k = 1.0;

% mx'' + cx' + kx = u
% today focus on X(s) / U(s)
% which is: Given an input force, how will the output position change?

% Laplace Transform:
% L{x'(t)} = sX(s)
% L{x''(t)} = x^2 X(s)

num = [1];   % numerator  X(s) = ( 1 / (ms^2 + cs + k) ) * U(s)
den = [m c k];  % denominator   ms^2 + cs + k
sys = tf(num, den);

figure;
step(sys);
grid on;
title('Step Response of Mass-Spring-Damper System')