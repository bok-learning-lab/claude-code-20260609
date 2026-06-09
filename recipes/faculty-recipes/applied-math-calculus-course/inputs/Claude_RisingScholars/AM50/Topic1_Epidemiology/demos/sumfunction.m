function [ sums, gauss_sum ] = sumfunction(N)
%function that sums the first N integers

sums = 0;

nums = 1:N;
sums = sum(nums);

gauss_sum = N*(N + 1)/2;


end
