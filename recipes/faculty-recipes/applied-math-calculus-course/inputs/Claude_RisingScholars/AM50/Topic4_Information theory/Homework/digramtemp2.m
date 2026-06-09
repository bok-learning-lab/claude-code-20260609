clear all;
close all;

fid = fopen('gettysburg.txt');

words = textscan(fid, '%s');

% Get rid of all the characters that are not letters or numbers
for i=1:numel(words{1,1})
    ind = find(isstrprop(words{1,1}{i,1}, 'alphanum') == 0);
    words{1,1}{i,1}(ind)=[];
end

% Remove entries in words that have zero characters
for i = 1:numel(words{1,1})
    if size(words{1,1}{i,1}, 2) == 0
        words{1,1}{i,1} = ' ';
    end
end

s = words{1,1}{1};
for i = 1:length(words{1})-1
    s = [s, ' ', words{1,1}{i+1}];
end
processed = lower(s);

%s = strcat(words{1,1}{:});
%processed = lower(s);

processed = lower(s);
processed = char(processed);
temp = mat2cell(processed, 1, ones(1, numel(processed)));
newprocessed = strjoin(temp, ' ');

%bigrams = ngrams(newprocessed, 2);
delimiters = {' ', '!', '''', ',', '-', '.',... % word boundary characters
    ':', ';', '?', '\r', '\n', '--', '&'};
biMdl = bigramClass(delimiters);                % instantiate the class
biMdl.build(newprocessed); 

%cell array of bigrams in document
bigrams = biMdl.bigrams; 
bigramCount = biMdl.biCount;

M = zeros(26, 26);
m = 1;
while m <= length(bigrams)
    pair = bigrams{m};
    for i = 1:26
        for j = 1:26
            if lower(char(i + 65 - 1, '', j + 65 - 1))' == pair
              M(i,j) = bigramCount(m)/sum(bigramCount);
            end
        end
    end
    m = m + 1;
end

figure;
pcolor(M);
colorbar

%map for assigning a to 1, b to 2, ..., z to 26
%stringsToMap = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
%valuesToMap = 1:26;

% %map for assigning strings to numbers
% for i = 1:26
%     for j = 1:26
%         stringsToMap{i,j} = char(i + 65 - 1, j + 65 - 1)';
%         valuesToMap{i,j} = [i, j] ;
%     end
% end
% stringsToMap = lower(stringsToMap);



% txt = {'b', 'c', 'z', 'w'};
% numericCodes = repmat(30, size(txt));
% for whichMap = 1:numel(stringsToMap)
%     locateValues = strcmp(txt, stringsToMap{whichMap});
%     numericCodes(locateValues)= valuesToMap(whichMap);
% end
% numericCodes
