function [ prob ] = binom(m, N, p)
%calculates P(m; N, p) = N!/((N - m)! m!) p^m(1 - p)^{N - m}

prob = fact(N)/(fact(N - m)*fact(m))*p^m*(1 - p)^(N - m);

end

