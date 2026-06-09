clear all;
close all;

N = 128;
angles = 0:1/2:180;

image = zeros(N,N);
image(N/2 - 16:N/2 + 16, N/2 - 16:N/2 + 16) = 1;

 imshow(image, 'InitialMagnification', 'fit')
 sinogram = radon(image, angles);
 
 subplot(3,1,1)
 plot(sinogram(:,1))
 subplot(3,1,2)
 plot(sinogram(:,2))
 subplot(3,1,3)
 plot(sinogram(:,3))


image_recon = iradon(sinogram, angles);
subplot(1,2,1)
imshow(image)
subplot(1,2,2)
imshow(image_recon)
% 
% %diff = image - image_recon;
% %subplot(1,3,3)
% %imshow(diff)
% 
% clear all;
% close all;
% 
% I = [1 2; 3 4];


