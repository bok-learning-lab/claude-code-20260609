% clears all the previously defined variables
% closes all previous figures
clear all;
close all;

year = 2;
name = 'Margo';

%Do different things depending on the condition
if strcmp(name, 'Eleanor') == 1
    year = 2014
elseif strcmp(name, 'Sasha') == 1
    year = 2012
else
    year = 0
end