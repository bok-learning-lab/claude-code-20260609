function r = simple_strategy(N, history, lw, lc, y)
% Always return 10
r = randi([0,4]);
r = r-(randi([0,2]));
r = abs(r);
if r == lw
    r = r-1;
    r= abs(r);
end
end