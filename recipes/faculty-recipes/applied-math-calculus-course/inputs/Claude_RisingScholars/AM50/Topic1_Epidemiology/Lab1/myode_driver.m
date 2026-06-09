%Script that solves the differential equation dy/dt = cos(t) subject to the
%initial condition y(0) = 2.  The script calls myode, a function that
%defines the differential equation dy/dt = cos(t).

clear all
close all

%Initial value of y as defined by the initial condition.  
y0 = 2;

%Independent variable t.  The first entry in tspan, t0, is the initial 
%value of the t variable, as defined by the initial condition.  The last
%entry, tf,is up to you.
t0 = 0;
tf = 2*pi;
tspan = [t0, tf];

%Solve the differential equation dy/dt = cos(t) subject to y(0) = 2.
[t, y] = ode45(@myode, tspan, y0);

%Plot the solution y(t) versus t
xlabel('t')
ylabel('y')
%change the x and y axis limits 
xlim([t0, tf])
ylim([0, 4])




