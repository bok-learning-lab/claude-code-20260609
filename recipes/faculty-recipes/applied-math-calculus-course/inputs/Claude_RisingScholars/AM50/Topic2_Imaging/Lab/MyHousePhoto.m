clear all;

%load the variable I that we saved above as I.mat
load I

%display image
imshow(I);

Icrop = imcrop

% Icrop = I(100:125, 80:200, :);
% I1 = Icrop(:, 1:60, :);
% I2 = Icrop(:, 61:121,:);
% 
% Inew = [I2, I1];
% 
% imshow(Inew)


%imshow(Icrop)

% %change image from color to black-and-white
% Ibw = rgb2gray(I);
% %display black-and-white image
% imshow(Ibw)
% 
% %convert the entries in Ibw to double
% Ibw = im2double(Ibw);
% 
% 
% 
% 

