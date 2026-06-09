function [ r ] = prev( N, history, lw, lc, y )

%Choose the previous winning entry plus or minus 1
if lw > 0
    r = lw + randi([-1, 1], 1);
else
    r = 1;
end

end

