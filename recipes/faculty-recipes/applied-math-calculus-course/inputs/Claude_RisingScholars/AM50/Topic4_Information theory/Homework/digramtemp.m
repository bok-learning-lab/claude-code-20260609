clear all;
close all;


% s = words{1,1}{1};
% for i = 1:length(words{1})-1
%     s = [s, ' ', words{1,1}{i+1}];
% end
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



% str_arry = join(words{1,1});
% str = char(str_arry);
% str = 'ab cd ab cd ef cd'
% 
% bigrams = [str(1:end-1); str(2:end)].'
% valid = all(isletter(bigrams),2);
% bigrams = bigrams(valid,:);
%  
% [uniqueBG,~,BGnumber] = unique(bigrams,'rows')
% n = histc(BGnumber, 1:size(uniqueBG,1))
% 


%map for assigning a to 1, b to 2, ..., z to 26
stringsToMap = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
valuesToMap = 1:26;

txt = {'b', 'c', 'z', 'w'};

%converts word to all lowercase letters
txt = cellstr(lower(words{1,1}{1,1})')'

%maps words to numbers according to map
numericCodes = repmat(30, size(txt));
for whichMap = 1:numel(stringsToMap)
    locateValues = strcmp(txt, stringsToMap{whichMap});
    numericCodes(locateValues)= valuesToMap(whichMap);
end
numericCodes

