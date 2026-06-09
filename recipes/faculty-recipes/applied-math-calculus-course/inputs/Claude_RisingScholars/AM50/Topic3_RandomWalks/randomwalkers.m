% SET UP
tmax=200; % total number of steps for the walkers
nparticles=100; % number of random walkers
x=zeros(nparticles,1); % start out all of the walkers at x=0
% SETUP FOR PLOTTING--BEGINNERS CAN IGNORE THIS! This just helps with the plots
xpoints=-20:1:20; % places where histogram centers the bins
axis([-20 20 0 50]); % sets the axes of the plots
for i=1:tmax % first loop: move each of the walkers tmax times
for j=1:nparticles % in each timestep, each of the nparticle walkers moves to the lefif rand(1,1)>0.5
x(j)=x(j)+1;
else
x(j)=x(j)-1;
end
end

%PLOTTING COMMANDS--BEGINNERS IGNORE, NOT IMPORTANT!
axis manual
nn=hist(x,xpoints); % trick for making a plot
bar(xpoints,nn); % trick for making a plot
M(i) = getframe; % trick for making a movie
pause(1/10);
% ANALYSIS COMMANDS--THIS LETS US PLOT THE
width(i)=std(x)/2; % half the standard deviation of the distribution
meanx(i)=mean(x); % mean of the distribution
end
movie(M); % plays the frames again as a movie!
Pl