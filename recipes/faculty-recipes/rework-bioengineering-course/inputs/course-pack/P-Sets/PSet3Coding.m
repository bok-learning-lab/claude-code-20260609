% % Pset #3 2025
% 
% We first want to create a sample signal (we’ll use a sinc function for this) and then find all of the positive and negative portions as well as the zero crossings. 
% • Declare a time vector from -30 to 30, with increments of 0.001
% • Plot a sinc function using this time vector, in black (not to be confused with a sin
% function)
t = -30:0.001:30;
y = sinc(t);
figure
plot(t,y)
% • Plot the derivative of this function in black (remember to include proper titles, axis
% labels, etc) on a second figure

% • On a third figure:
% h)	o Plot the positive portions of this derivative with green points
% i)	o Plot the negative portions of this derivative with red points
% j)	o Mark the zero-crossing points of the derivative with yellow squares
% k)	▪ Hint: Look up the function sign() in the MATLAB documentation online
% l)	• Now use the data from the derivative to plot the original sinc function. In one figure:
% m)	o Plot the portions of the original function where its derivative is positive
% n)	with green points
% o)	o Plot the portions of the original function where its derivative is negative
% p)	with red points
% q)	o Mark the peaks and troughs of the original function with yellow squares


%%
ecg = load('ECGdata.mat');
figure
plot(ecg.ptime, ecg.pdata)