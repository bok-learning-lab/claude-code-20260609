clear all
close all

N = 500;
I = zeros(N,N,3);
xcen = N/20;
ycen = N/20;
radius = N/20;
cx = 1;
cy = 1;
dcx = .08;
dcy = .08;

I = makecircle(I, xcen, ycen, radius, [0 cx cy]);
for i = 1:10
    for j = 1:10
        I = makecircle(I, xcen + 2*(i-1)*radius, ycen + 2*(j-1)*radius, radius, [0 cx - i*dcy cy- j*dcx]);
        if i < 10 && j < 10
        I = makecircle(I, 2*i*xcen, 2*j*ycen, radius/3, [1 - i*dcx 0 1 - j*dcy]);  
        end
    end
end

imshow(I)
