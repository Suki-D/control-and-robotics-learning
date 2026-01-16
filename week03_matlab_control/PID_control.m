clear; clc;

s = tf('s');
G = 1 / (s^2 + 0.4*s + 1);

H0 = feedback(G, 1);
step(H0)
grid on
title('Baseline closed-loop (no PID)')

% Only add Kp
Kp = 5; 
C = Kp;
H = feedback(C*G, 1);
step(H)
grid on
title('Proportional Control Only')
% try Kp = 20
% The larger the Kp value, the more "aggressive" the system becomes, 
% but the more prone it is to overshoot and oscillation.

% Add Kd
Kp = 20;
Kd = 5;

C = Kp + Kd*s;
H = feedback(C*G, 1);
step(H)
grid on
title('PD Control')
% Overshoot is reduced.
% Oscillations are reduced.
% It stabilizes faster.

% Add Ki
Kp = 20;
Ki = 10;
Kd = 5;

C = Kp + Ki/s + Kd*s;
H = feedback(C*G, 1);
step(H)
grid on
title('Full PID Control')
% Final value (strictly) = 1
% Clean response
% Oscillation is controlled
% When try Ki = 50, oscillations reappeared.


% Key observations included:
% Increasing Kp improves rise time but can introduce overshoot and oscillations.
% Adding Kd increases damping, reducing overshoot and oscillatory behavior without significantly affecting steady-state accuracy.
% Introducing Ki eliminates steady-state error, but excessive integral action can destabilize the system.

% Through iterative tuning, I established a practical mapping between response behavior and controller adjustments 
% e.g., slow response -> increase Kp; 
% large overshoot -> increase Kd / decrease Kp; 
% steady-state error -> increase Ki;
% Severe oscillation -> decrease Ki / increase Kd.

