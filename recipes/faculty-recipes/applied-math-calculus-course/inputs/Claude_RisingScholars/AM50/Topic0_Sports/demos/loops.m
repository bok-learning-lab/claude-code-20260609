clear all;
close all;

%create an array 1, 2, ..., 10
N = 10;
for i = 1:N
    a(i) = i;
end

%do it another way
i = 1;
while i <= 10
    b(i) = i;
    i = i + 1;
end

%do it without a loop
c = 1:N;

%print a, b, and c
a
b
c

