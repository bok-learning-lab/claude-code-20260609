%Create an array, append an item,
% and demonstrate various outputs
a = [6,3,1,4];
b = 10;
a = [a, b];

a(1)
a(1:3)

%Create an matrix, append an array,
% and demonstrate various outputs
c = [1 2; 3 4];
d = [0 0];

c_vert = cat(1, c, d)
c_horz = cat(2, c, d')



