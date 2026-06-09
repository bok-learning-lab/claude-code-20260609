clear all;
close all;

%theoretical value of D = dx^2/(2dt) = 2.
D = 2;
tmax = 100;
nparticles = 500;

x = zeros(nparticles, 1); 
xmin = -30;
xmax = 30;
xpoints = xmin:xmax;

for i = 1:tmax
    for j = 1:nparticles
        if rand(1,1) > .5
            x(j) = x(j) + 2;
        else
            x(j) = x(j) - 2;
        end
    end    
  %  histogram(x, xpoints);
   % axis([xmin xmax 0 300]);
   % M(i) = getframe;
    %pause(1/10)
    
    width(i) = std(x)/sqrt(2);
    meanx(i) = mean(x);
end

t = 1:tmax;
figure(1)
plot(t, width, 'o--')
hold on;
plot(t, sqrt(D*t))

figure(2)
loglog(t, width, 'o')

%slope = (log(width(length(t))) - log(width(1)))/(log(tmax) - log(1));





