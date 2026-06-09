function [ r ] = prev_strategy( N, history, lw, lc, y )

%Choose the previous winning entry plus or minus 1
if lw > 0
    if rand > .5
        r = lw + 1;
    else
        r = lw - 1;
    end
else
    r = 1;
end

end

