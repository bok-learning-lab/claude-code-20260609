M = 44;
N = 7;
p = 0.65;

for n = 1:M
    team1 = worldseries1(p, N); % the number of games team1 wins each in the nth series
    team2 = N - team1; % the number of games team2 wins each in the nth series
    lose(n) = min(team1, team2); % the number of games the loser wins in the nth series
end

distribution = histogram(lose);
counts = distribution.Values;
