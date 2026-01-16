clear; clc;

s = tf('s');

% Define a transfer function
G = 1 / (s^2 + 0.4*s + 1);
step(G)
grid on
title("Second=order system response")

pole(G) % Get the pole point
% Output: -0.2000 + 0.9798i
%         -0.2000 - 0.9798i
% ±j -> Oscillation (frequency)
% -0.2 -> Attenuation (Damping)

pzmap(G)
grid on
title('Pole-Zero Map')

% Change damping
G1 = 1 / (s^2 + 0.2*s + 1);
G2 = 1 / (s^2 + 1.2*s + 1);

step(G1, G2)
legend('low damping', 'high damping')
grid on

pole(G1) % -0.1000 +- 0.9950i
pole(G2) % -0.6000 +- 0.8000i

% The closer the poles are to the imaginary axis,
% the stronger the oscillation and the more "unstable" the system becomes.


% Unstable system
G_unstable = 1 / (s^2 - 0.4*s + 1);
step(G_unstable)  % Diverging
pole(G_unstable)  % +0.2000 +- 0.9798i

% If there is a pole in the right half-plane, 
% then the system is definitely unstable.


% The imaginary part of the pole is approximately equal to the oscillation frequency.
G = 1 / (s^2 + 0.4*s + 4);
step(G)
pole(G) % -0.2000 +- 1.9900i