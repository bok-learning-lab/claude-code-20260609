function [ r ] = Alexandra_Zaoui(N, history, lw, lc, y)

%Sum total history entries
s = sum(history);

if s == 0
    r = 0;
end

%Look for a low value in the history. We want prob(i)=history[i]/s
%to be less than 1/N. Add a random displacement from -2 to 2.
for i = 1:100
    r = N*history(i);
 if r > lw
     r = r - lw;
 end
 if r < lc
     r = r - lc;
 else
     r = r;
end



end

