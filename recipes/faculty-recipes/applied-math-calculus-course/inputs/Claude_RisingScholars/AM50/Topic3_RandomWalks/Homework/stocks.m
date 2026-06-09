clear all;
close all;

M = csvread('S_P_500.csv', 1, 1);

S = flip(M(:,1));
t = 1:length(S);

diff_stocks = diff(S);
percent_diff = diff_stocks./(.5*(S(1:length(S)-1) + S(2:length(S))));


stocks_5day = S(1:5:length(S),1);
diff_stocks_5day = diff(stocks_5day);
percent_diff_5day = diff_stocks_5day./(.5*(S(1:length(stocks_5day)-1) + S(2:length(stocks_5day))));


stocks_10day = S(1:10:length(S),1);
diff_stocks_10day = diff(stocks_10day);
percent_diff_10day = diff_stocks_10day./(.5*(S(1:length(stocks_10day)-1) + S(2:length(stocks_10day))));

t = [1, 5, 20];
s1 = std(percent_diff);
s5 = std(percent_diff_5day);
s10 = std(percent_diff_10day);

plot(t, [s1, s5, s10])

% % 
% % figure(1)
% % histogram(diff_stocks)
% % xlabel('distribution of prices')
% 
% figure(2)
% histogram(percent_diff_10day)
% xlabel('distribution of percentages')
% 
% % figure(3)
% % histogram(diff_stocks)
% % xlabel('distribution of prices')
% % set(gca, 'YScale', 'log')
% 
% figure(4)
% histogram(percent_diff_10day)
% xlabel('distribution of percentages -- log')
% set(gca, 'YScale', 'log')



