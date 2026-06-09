clear all;
close all;

tmax = 100;
nparticles = 500;

x = zeros(nparticles, 1); 
xmin = -30;
xmax = 30;
xpoints = xmin:xmax;

for i = 1:tmax
    for j = 1:nparticles
        if rand(1,1) > .5
            x(j) = x(j) + 1;
        else
            x(j) = x(j) - 1;
        end
    end    
    histogram(x, xpoints);
    axis([xmin xmax 0 300]);
    M(i) = getframe;
    pause(1/10)
    
    width(i) = std(x)/sqrt(2);
    meanx(i) = mean(x);
end



