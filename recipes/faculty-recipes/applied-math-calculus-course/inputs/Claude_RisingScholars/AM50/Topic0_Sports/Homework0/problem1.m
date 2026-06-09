clear all;
close all;

p = 0.5:.01:1;

S1 = p;
S2 = p.^3 + 3*p.^2.*(1 - p);

plot(p, S1, p, S2)

xlabel('p')
ylabel('Probability')

legend('S(p,1)', 'S(p,3)', 'Location','southeast')




