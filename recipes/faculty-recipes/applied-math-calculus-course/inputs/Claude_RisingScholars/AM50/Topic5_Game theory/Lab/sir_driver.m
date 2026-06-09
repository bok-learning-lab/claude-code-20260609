clear all;
close all;

t0 = 0;
tf = 10;
tspan = [t0, tf];

p0 = .1;
q0 = 1 - p0;

y0 = [p0, q0];

[t,y]=ode45(@sir_model,tspan,y0);

plot(t, y)
legend('p', 'q')




