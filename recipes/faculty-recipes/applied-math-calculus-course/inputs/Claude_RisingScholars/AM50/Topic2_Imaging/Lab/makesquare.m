function [image_square] = makesquare(image, xpix, ypix, Lx, Ly, shade)

image_square = image;
image_square(xpix: xpix + Ly, ypix: ypix + Lx) = shade;


end

