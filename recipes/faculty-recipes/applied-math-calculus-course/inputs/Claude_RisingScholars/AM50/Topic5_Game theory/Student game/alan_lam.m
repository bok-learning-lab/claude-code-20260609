function r = alan_lam(N, history, lw, lc, y)

if lw == 0
    r = 1;
end 

if lw > 0
    if y > N/2
        r = lw+2;
    end
    
    if y < N/2
        r = lw+1;
    end
    
    if y < 3
        r = lw-1;
    end
end
end