% example of loop
% sum the first N integers
clear all;
close all;

N = 10;

sums = 0;

% while loop
i = 1; 
while i <= N
    sums = sums + i;
    i = i + 1;
end

sums = 0;
% for loop
for i = 1:N
    sums = sums + i;
end

gauss_sum = N*(N + 1)/2;

sums = 0;
sums = sum(1:N);

[s, gs] =  sumfunction(10)
%sumfunction(15)
%sumfunction(20)






