clear all;
close all;

m = 9;

trials = 100;

for i = 1:trials
    r(i) = playgame(m);
end

nbins = m + 1;
h = histogram(r, nbins);

counts = h.Values;
p_trial = counts/trials;
p_analy = r_analytic(m);

p = [p_trial', p_analy];

 bar(0:m, p)
 xlabel('k',  'FontSize',20)
 ylabel('p_k', 'FontSize',20)
 xlim([-1, m])
 
 lgd = legend('computed', 'analytic');
 lgd.FontSize = 20;
 







