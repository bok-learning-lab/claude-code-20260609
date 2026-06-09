clear all;
close all;

tmax = 200;
nparticles = 500;

x = zeros(nparticles, 1); 
y = zeros(nparticles, 1); 
xmin = -30;
xmax = 30;
xpoints = xmin:xmax;
ymin = -30;
ymax = 30;
ypoints = ymin:ymax;

for i = 1:tmax
    for j = 1:nparticles
        if rand(1,1) > .5
            if rand(1,1) > .5
                x(j) = x(j) + 1;
            else
                x(j) = x(j) - 1;
            end
        else
            if rand(1,1) > .5
                y(j) = y(j) + 1;
            else
                y(j) = y(j) - 1;
            end
        end
    end    
   % histogram(x, xpoints);
     plot(x,y,'.')
       axis([xmin xmax ymin ymax]);
%     M(i) = getframe;
     pause(1/10)
    
%     width(i) = std(x)/sqrt(2);
%     meanx(i) = mean(x);
end
%max([x, y, sqrt(x.^2 + y.^2)])




