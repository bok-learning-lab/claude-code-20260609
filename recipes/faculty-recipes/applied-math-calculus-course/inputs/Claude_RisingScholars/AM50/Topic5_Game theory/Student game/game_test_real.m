function wins = game_test_real(N, trials)

%Play with 22 players
%N = 22;
%trials = 100;
% %My place in the list of N players
% y = 3;

%Counters for who won
wins = zeros(1,N);
now = 0;

%Data about the runs
history = zeros(1, 100);
lc = zeros(1, N);
lw = 0;

%Simulate many trials
for i = 1:trials
    cc = zeros(1, N);
   
    cc(1) = alan_lam(N, history, lw, lc, 1);
    cc(2) = Alexandra_Zaoui(N, history, lw, lc, 2);
    cc(3) = anna_zhou( N,history,lw,lc,3 );
    cc(4) = Ben_Kruteck(N, history, lw, lc, 4);
    cc(5) = caitlin_weigel(N, history, lw, lc, 5);
    cc(6) = Emily_Hume(N, history, lw, lc, 6);
    cc(7) = franci_vanrhyn(N, history, lw, lc, 7);
    cc(8) = Grant_Harvey(N, history, lw, lc, 8);
    cc(9) = jacob_bindman(N, history, lw, lc, 9);
    cc(10) = jenny_golden(N,history, lw, lc, 10);
    cc(11) = joshua_sopher(N,history, lw, lc, 11);
    cc(12) = Laura_Medina(N,history, lw, lc, 12);
    cc(13) = lia_mondavi(N, history, lw, lc, 13);
    cc(14) = lj_barlow(N,history, lw, lc, 14);
    cc(15) = lucas_hoffmann(N,history, lw, lc, 15);
    cc(16) = Matt_Bouchard(N,history, lw, lc, 16);
    cc(17) = michael_nock(N,history, lw, lc, 17);
    cc(18) = peter_hartnett(N,history, lw, lc, 18);
    cc(19) = rachael_harkavy(N,history, lw, lc, 19);
    cc(20) = tamilyn_chen(N,history, lw, lc, 20);
    cc(21) = valerie_yoshimura(N,history, lw, lc, 21);
    cc(22) = zahra_rawji(N,history, lw, lc, 22);
    
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
     else
         for ind = 1:N
             if cc(ind) == lw
                 wins(ind) = wins(ind) + 1;
                 break
             end
         end
     end
     
%      if lw == 100
%          now = now + 1;
%      elseif cc(N) == lw
%          ssw = ssw + 1;
%      else
%          rsw = rsw + 1;
%      end
           
     %Move this round's choices to lc
     lc = cc;
end
end

%wins = wins/trials;
% f = 100/trials;
% 
% %percent wins 
%  simplewin = ssw*f;
%  randomwin = rsw*f;
%  nowin = now*f;
 

     




