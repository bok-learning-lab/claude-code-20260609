clear all;
close all;

N = 5; 

V = eye(N);

%identity matrix: 1 = white, 0 = black
imshow(V, 'InitialMagnification', 'fit');
colorbar

%change element (2,5) to gray
V(2,5) = .5;

imshow(V, 'InitialMagnification', 'fit');
colorbar('southoutside', 'Fontsize', 15);



