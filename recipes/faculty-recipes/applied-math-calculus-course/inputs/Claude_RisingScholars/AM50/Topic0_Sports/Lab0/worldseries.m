function [win] = worldseries(p, N)
% Should they be asked to explain what each line does?

win = 0;
for i = 1:N
    if rand(1,1) < p
        win = win + 1;
    end
end

end


