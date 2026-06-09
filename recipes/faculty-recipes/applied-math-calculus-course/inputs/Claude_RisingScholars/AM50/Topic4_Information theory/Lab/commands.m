clear all;
close all;

%fid = fopen('gettysburg.txt');
% 
% words = textscan(fid, '%s');
% 
% words{1}
% 
% size(words{1})
% 
% unique_words = unique(words{1});
% 
% size(unique_words)

[results_g, freq_g] = wordcount('gettysburg.txt', 1000);
loglog(freq_g, 'g.')
hold on;

[results_f, freq_f] = wordcount('fox.txt', 1000);
loglog(freq_f, 'b.')

hold on;
[results_h, freq_h] = wordcount('huffington.txt', 1000);
loglog(freq_h, 'r.')

