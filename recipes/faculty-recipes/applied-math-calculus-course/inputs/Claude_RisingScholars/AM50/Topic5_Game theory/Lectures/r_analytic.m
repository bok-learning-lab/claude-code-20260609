function p = r_analytic(m)

%m = 99;

k = 0:m;

p = zeros(length(k),1);

for i = 1:length(k)
    for j = k(i):m
        p(i) = p(i) + 1/(j + 1);
    end
    p(i) = p(i)/(m + 1);
end 

end


%  bar(0:m, p)
%  title('m = 99', 'FontSize', 22)
%  xlabel('k', 'FontSize',22)
%  ylabel('p_k','FontSize',22)
%  xlim([-1, 90])
