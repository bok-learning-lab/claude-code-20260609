%%
% 
%   for x = 1:10
%       disp(x)
%   end
% 
clear all;
close all;

N = 200;
M = 200;
V = zeros(M,N);

%location of upper left corner of image

for i = 1:10
    xpix = i*N/20;
    ypix = i*M/20;
    Lx = N - 2*xpix;
    Ly = M - 2*ypix;
    if mod(i,2) == 0
        shade = 0;
    else
        shade = 1;
    end
    V = makesquare(V, xpix, ypix, Lx, Ly, shade);
end


% shade = 1;
% V = makesquare(V, xpix, ypix, Lx, Ly, shade);
% imshow(V)
% 
% xpix = 2*N/10;
% ypix = 2*M/10;
% Lx = N - 2*xpix;
% Ly = M - 2*ypix;
% shade = 0;
% V = makesquare(V, xpix, ypix, Lx, Ly, shade);
% imshow(V)
% 
% xpix = 3*N/10;
% ypix = 3*M/10;
% Lx = N - 2*xpix;
% Ly = M - 2*ypix;
% shade = 1;
% V = makesquare(V, xpix, ypix, Lx, Ly, shade);
% imshow(V)
% 
% xpix = 4*N/10;
% ypix = 4*M/10;
% Lx = N - 2*xpix;
% Ly = M - 2*ypix;
% shade = 0;
% V = makesquare(V, xpix, ypix, Lx, Ly, shade);
imshow(V)
