function r = Ben_Kruteck(N, history, lw, lc, y)
rem = mod(lw,2);
A = zeros(30);
for i = 1:30
    A(i) = history(i);
end
count1 = 0;

Anew = sort(A);

if rem == 0
    for i = 1:(size(A) - 1)
       if Anew(i) == Anew(i+1)
           count1 = count1+1;
       end
    end
    q = floor((lw + count1)/6);  
    v = rand(1);
    r = floor((q * v) + (N * (1-v)/3));
elseif rem == 1
    r = randi([5,9]);
end

end