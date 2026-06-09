function [ r ] = Emily_Hume( N, history, lw, lc, y )
for lw = 0:5
    r= randi([0,3]);
    if lw > 5
        r = lw - 1;
    end
    for lw = 4:5
        r = 0;
    end
end

