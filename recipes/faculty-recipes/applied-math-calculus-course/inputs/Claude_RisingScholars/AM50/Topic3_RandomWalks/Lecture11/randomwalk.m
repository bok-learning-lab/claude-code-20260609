clear all;
close all;

%starting position
x = 0;

%number of steps
steps = 20;

%carry out steps
for i = 1:steps
    %print results
    disp([i, x])
    if rand(1,1) < .5
        x = x+1;
    else
        x = x-1;
    end
   % plot(i, x)
end



