clear all;
close all;

%number of players
N = 22;
%number of games in each round
trials = 1000000;
%number of rounds
numr = 10;

totalwins = zeros(1, N);
% a = [0; 0; 0];
% save('results.mat', 'a');
for i = 1:numr
    totalwins = totalwins + game_test_real(N, trials);
    [maxim ind] = max(totalwins)
    i
%     a = [maxim; ind; trials];
%     save('results.mat', 'a', '-append');
end

[maxim ind] = max(totalwins);

