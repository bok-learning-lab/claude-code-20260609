M = 128; 
N = 128;
 
V = zeros(M,N); %make a matrix with all zeros
 
V= makesquare(V,48,48,32,32,1);

imshow(V)
 
sinogram = radon(V, 0:4:360);
  
 subplot(1,3,1), plot(sinogram(:, 1)); 
 subplot(1,3,2), sinogram(1:128,2); 
 subplot(1,3,3), sinogram(:,3); 