clear all;
close all;

m = 100;
N = 100;
p = 1/2;
M = 0:m;

 
for i = 1:length(M)
     pr(i) = binom(M(i), N, p);
end
 
plot(M, pr, 'o-')

xlabel('the number of successes m')
ylabel('P(N,m)')