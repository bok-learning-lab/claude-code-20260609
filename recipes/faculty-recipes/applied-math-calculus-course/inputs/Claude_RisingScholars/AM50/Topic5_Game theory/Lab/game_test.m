clear all
close all

%Play with 25 players
N = 25;
trials = 10000;
%My place in the list of N players
y = 3;

%Counters for who won
rsw = 0;  
ssw = 0;
now = 0;

%Data about the runs
history = zeros(1, 100);
lc = zeros(1, N);
lw = 0;

%Simulate many trials
for i = 1:trials
    cc = zeros(1, N);
    
    %First N-1 players use random_choice strategy
    for j = 1:N-1
        cc(j) = inrange(random_strategy());
    end
    
    %Last player uses test_strategy strategy
    %cc(N) = inrange(simple_strategy(N, history, lw, lc, y));
     cc(N) = inrange(histo(N, history, lw, lc, y));

    
    %Tally the guesses
    c = zeros(1,100);
    for k = 1:N
        for m = 1:100
            c(m) = length(find(cc == m-1));
        end
    end
    history = history + c;
 
    %Find the winning number
     k = 1;
     while k <= 100
         if c(k) == 1
             lw = k - 1;
             break
         end
         k = k + 1;
     end
     
     %See who won
     if lw == 100
         now = now + 1;
     elseif cc(N) == lw
         ssw = ssw + 1;
     else
         rsw = rsw + 1;
     end
             
     %Move this round's choices to lc
     lc = cc;
end

f = 100/trials;

%percent wins 
 simplewin = ssw*f;
 randomwin = rsw*f;
 nowin = now*f;
 

     




