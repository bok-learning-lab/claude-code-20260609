function r = caitlin_weigel( N, history, lw, lc, y )

% r = the winning number from the previous number plus the number that the
% 5th person picked the previous round, then this number modulo 9. So r
% will always be a number between 0 and 9, just with differing
% probabilities.
r = mod(lw + lc(5), 9); 

end

