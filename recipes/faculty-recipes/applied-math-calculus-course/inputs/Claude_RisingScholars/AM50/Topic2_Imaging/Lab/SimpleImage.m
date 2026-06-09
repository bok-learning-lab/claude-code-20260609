clear all;
close all;

M = 9;
N = 9;

%Creates an M by N matrix of zeros (black)
V = zeros(M,N);

%Change certain entries to white
V(3,3) = 1;
V(3,7) = 1;
V(5,5) = 1;
V(6,2) = 1;
V(6,8) = 1;
V(7,3) = 1;
V(7,7) = 1;
V(8, 4:6) = 1;

%Display the image
imshow(V, 'InitialMagnification', 'fit')