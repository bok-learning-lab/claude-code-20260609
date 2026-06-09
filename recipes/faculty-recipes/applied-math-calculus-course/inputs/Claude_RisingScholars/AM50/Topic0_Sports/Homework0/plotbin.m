function [ probs ] = plotbin(N, p)
%plots binomial distribution as a function of N

M = 0:N;

for i = 1:length(M)
     pr(i) = binom(M(i), N, p);
end
 
plot(M, pr, 'o-')

end

