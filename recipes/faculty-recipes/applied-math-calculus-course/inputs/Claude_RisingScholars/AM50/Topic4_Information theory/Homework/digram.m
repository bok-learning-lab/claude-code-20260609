clear all;
close all;

fid = fopen('ge_siddartha.txt');
words = textscan(fid, '%s');
fclose(fid);

% Get rid of all the characters that are not letters or numbers
for i=1:numel(words{1,1})
    ind = find(isstrprop(words{1,1}{i,1}, 'alphanum') == 0);
    words{1,1}{i,1}(ind)=[];
end

% combine all the words into one string
% Matlab 2015 users: replace join command by strjoin
s = join(words{1,1});   
%make all letters lowercase
s = lower(s);
s = strcat(s);

P = zeros(27, 27);
 
%compare each possible digram to the digram in the text and assign
%frequency to matrix element P(i,j), ie, P(1,1) = frequency of 'aa', etc
for i = 1:26
    for j = 1:26
        pair = lower(char(i+65-1,j+65-1))';
        k = strfind(s, pair);
        P(i,j) = length(k);
    end
end

%to deal with spaces ' a', ' b', etc.
for i = 1:26
    pair = lower(char(i+65-1,127))';
    k = strfind(s, pair);
    P(i,27) = length(k);
end

for j = 1:26
    pair = lower(char(127, j+65-1))';
    k = strfind(s, pair);
    P(27,j) = length(k);
end

P = P/sum(sum(P));

pcolor(P);
colormap(jet)
colorbar

xticks(1.5:27.5)
xticklabels({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'})
% Matlab 2015 users: replace the above two commands by the three lines below.
% These commands will also work for 2016 Matlab users
% ax = gca;
% ax.XTick = [1.5:28.5];
% ax.XTickLabel = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
xlabel('second letter in digram')
yticks(1.5:28.5)
yticklabels({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'})
% Matlab 2015 users: replace the above two commands by two lines below.
% These commands will also work for 2016 Matlab users
% ax.YTick = [1.5:28.5];
% ax.YTickLabel = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
ylabel('first letter in digram')
