function [win] = worldseries1(p, N)
% Comments for humans to make the code easier for humans to understand.

win = 0;
for i = 1:N
    if rand(1,1) < p
        win = win + 1;
    end
end

end


