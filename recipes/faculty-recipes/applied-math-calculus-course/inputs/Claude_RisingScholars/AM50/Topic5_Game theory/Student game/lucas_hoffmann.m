function [ r ] = lucas_hoffmann( N, history, lw, lc, y )

if lw == 0
    r = randi([lw,(lw+2)]);
else 
    r = randi([(lw-1),(lw+2)]);
end

end

