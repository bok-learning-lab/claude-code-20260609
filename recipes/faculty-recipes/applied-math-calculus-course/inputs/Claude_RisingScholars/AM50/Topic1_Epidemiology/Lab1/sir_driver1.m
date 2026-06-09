clear all;
close all;

t0 = 0;
tf = 52;
tspan = [t0, tf];

S0 = 10000;
I0 = 1000;
R0 = 0;

y0 = [S0, I0, R0];

[t,y]=ode45(@sir_model,tspan,y0);

M = csvread('googleflu.csv', 1, 1, [1, 1, 310, 52]);
plot(M(1:52, 34), 'ro') 
hold on;
plot(t, y(:,2))




