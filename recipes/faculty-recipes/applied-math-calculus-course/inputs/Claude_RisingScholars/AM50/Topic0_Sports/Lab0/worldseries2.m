function [win] = worldseries2(p, N)

win = 0; % initialize win to zero 
p_real = p + 0.05*rand(1,1); % add a small random number, which is uniformly distributed between (1,0.05), to the original probability p 
for i = 1:N % simulate N games in one series
    if rand(1,1) < p_real  % if a random number between (0,1) is less than p, this indicates the better team wins.
         win = win + 1; % add 1 to the win variable
        p_real = p + 0.05*rand(1,1); % update the winning probability, so that p changes from game to game
    end
end

end


