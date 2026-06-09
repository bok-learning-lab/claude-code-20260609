clear all;
close all;

t0 = 0;
tf = 1000;
tspan = [t0, tf];

S0 = 80;
I0 = 20;
R0 = 0;

y0 = [S0, I0, R0];

[t,y]=ode45(@sir_model,tspan,y0);




