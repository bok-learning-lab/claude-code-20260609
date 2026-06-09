clear all;
close all;

%number of walkers
N = 10;

%starting position
x = zeros(1,N);

%number of steps
steps = 10000;

 %carry out steps
 for j = 1:N
    for i = 2:steps
        if rand(1,1) < .5
             x(i,j) = x(i-1,j)+1;
        else
             x(i,j) = x(i-1,j)-1;
        end
    end
 end
 plot(x, 'LineWidth',2)
 ax = gca
 ax.FontSize = 13;
 xlabel('step number', 'FontSize', 20)
 ylabel('position', 'FontSize', 20)
    