function r = peter_hartnett(N, history, lw, lc ,y)

p = zeros(1, length(history));

for i = 1:length(history)
if history(i) == 0
    j = randi([3 10],1);
    r = randi([3 j],1);
else
    p(i) = history(i)/sum(history(:));
end

for i = 1:N
    if rand(1,1)>p(i)
        A(i) = i-1;
    else
        A(i) = 0;
    end
end

A = A(A~=0);
r = A(1);
end

end

