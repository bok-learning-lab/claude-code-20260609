function r = lia_mondavi(N, history, lw, lc, y)
%N, history, lw, lc, y
%inputs are:
%N = The total number of players.
%history = A list of length 100, containing the total number of choices of 
%each number across all previous rounds that have been played so far.
%lw = The winning number in the previous round. If there was no winner in 
%the previous round this will be set to 100. In the very first round, 
%before anything has been played, lw will be sest to zero.
%lc = A list of length N of all of the players? choices in the previous 
%round. In the very first round, before anything has been played, all 
%entries will be set to zero. Each player will occupy the same entry in the
%list throughout the game; for example, by repeatedly examining lc[5] you 
%could see the entire history of one particular player.
%y = Your position within the lc list. Hence lc[y] will be equal to your 
%choice in the previous round.

% Exercise 1
%play the previous winning number, lw plus randi([0,3])
r = lw+randi([-2,3]);

end