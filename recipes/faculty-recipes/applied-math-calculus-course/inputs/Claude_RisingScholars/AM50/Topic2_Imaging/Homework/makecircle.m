function [ image_circle] = makecircle(image, xcen, ycen, radius, color)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

image_circle = image;
[N, M, C] = size(image);

for i = 1:M
    for j = 1:N
        d2 = (i - xcen)^2 + (j - ycen)^2;
        if d2 <= radius^2
            image_circle(i,j,:) = color;
        end
    end
end


end

