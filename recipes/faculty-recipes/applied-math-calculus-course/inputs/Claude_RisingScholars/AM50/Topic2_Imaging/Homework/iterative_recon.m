clear all;
close all;

 N = 1000;
 I = zeros(N,N);
% 
I = makecircle(I, N/2, N/2, 100, 1);

%I = imread('headshot.jpg');
%I = rgb2gray(I);
%I = im2double(I);

figure(1)
subplot(3,3,1)

imshow(I)


dtheta = [90, 60, 45, 30, 15, 5, 3, 1];
for i = 1:length(dtheta)
    R = radon(I, 0:dtheta(i):180);
    size(R);
    Irecon = iradon(R, 0:dtheta(i):180);
    
    subplot(3, 3,i+1)
    imshow(Irecon)
end


% 
% 
% 
% % %square at center of image with 40 pixel padding on each side
% % I = makesquare(I, pad, pad, 2*Lx, 2*Ly, 1);
% % % I = makesquare(I, pad+Ly, pad+1, Lx, Ly, 1);
% % % I = makesquare(I, pad+Ly, pad+Lx, Lx, Ly, 1);
% % % I = makesquare(I, pad+1, pad+Lx, Lx, Ly, 1);
% 
