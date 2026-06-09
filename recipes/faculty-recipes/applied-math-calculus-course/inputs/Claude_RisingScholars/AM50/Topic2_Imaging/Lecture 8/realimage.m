clear all;
close all;

I = imread('cat.jpg');

Idouble = im2double(I);

Ibw = rgb2gray(Idouble);

imshow(Ibw)
title('black and white cat')

Icrop = Ibw(60:300, 200:500);
imshow(Icrop)

