close all
clear all

m = 25;

p = 1/(m + 1)*ones(m+1, 1);

subplot(2,1,1)
bar(0:m, p)
xlabel('k', 'FontSize',20)
ylabel('p_k','FontSize',20)
 xlim([0, 35])