function [ x] = inrange( x )
%check that x is in the allowable range, integers from 0 to 99

if x < 0
    x = 0;
elseif x > 99
    x = 99;
end

end

