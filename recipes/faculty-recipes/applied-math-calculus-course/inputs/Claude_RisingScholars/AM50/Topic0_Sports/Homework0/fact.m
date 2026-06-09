function [ nfact ] = fact(n)
%for non-negative integer n, calculutes n!

ints = 1:n;
nfact = prod(ints);

%one option with for loops
% nfact = 1;
% for i = 1:n
%     nfact = nfact*i;
% end

%one option with while loops


end

