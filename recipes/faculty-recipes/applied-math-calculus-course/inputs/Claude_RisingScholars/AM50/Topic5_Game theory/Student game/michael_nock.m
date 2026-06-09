function r = michael_nock( N,history,lw,lc,y )
if lw>=lc(y);
    r=lc(y)+1;
else
    r=lc(y)-1;
end

