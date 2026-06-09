function [ r ] = histo(N, history, lw, lc, y)

%Sum total history entries
s = sum(history);

if s == 0
    r = 0;
end

%Look for a low value in the history. We want prob(i)=history[i]/s
%to be less than 1/N. Add a random displacement from -2 to 2.
for i = 1:100
    if N*history(i) < s
        r = i - 1 + randi([-2,2], 1);
    else
        r = 99;
    end
end



end

