%Exam 3, 2025 MATLAB Question
% Written by Linsey Moyer
clear all
close all

load('respiratorydata.mat'); % Load data and isi variables
fs = samplerate(1);               % Calculate sampling frequency (Hz)
N = round(200 * fs);         % Number of samples for 200 seconds
t = (0:N-1) * (1/fs);    % Create time vector
% resp = data(datastart(1):datastart(1)+N-1);         % Channel 1: Respiratory Data
% pulse = data(datastart(2):datastart(2)+N-1);        % Channel 2: Pulse/Heart Data

resp = data(datastart(1,1):datastart(1,1)+fs*200-1);         % Channel 1: Respiratory Data
resp = smooth(resp, 20);
pulse = data(datastart(2,1):datastart(2,1)+fs*200-1);        % Channel 2: Pulse/Heart Data

% Detect Respiratory Peaks (Inhalation) - Min distance ~1.5s to avoid noise
mph = 1;
[~, locs_in] = findpeaks(resp(1:120*fs), 'MinPeakDistance', 1.8*fs, 'MinPeakProminence', 0.4, 'MinPeakHeight',mph);
peakthreshold = 1.7*mean(resp(1:50*fs));
locs_ptidal = find(resp(locs_in)<peakthreshold);
locs_tidalin = locs_in(locs_ptidal)
peakNum1 = length(locs_tidalin);

% Detect Respiratory Valleys (Exhalation) - Invert data to find valleys
[~, locs_ex] = findpeaks(-resp, 'MinPeakDistance', 2*fs, 'MinPeakProminence', 0.1);
valthreshold = mean(-resp(1:50*fs));
locs_vtidal = find((-1*resp(locs_ex))>valthreshold);
locs_tidalex = locs_ex(locs_vtidal)
valleyNum1 = length(locs_tidalex);

% Detect Pulse Peaks for Heart Rate - Min distance ~0.4s (Max 150 BPM)
MPH = 0.01;
MPD = fs*0.5;
MPP =.05;
% [~, locs_hr] = findpeaks(pulse,'MinPeakHeight',MPH,'MinPeakDistance',MPD, 'MinPeakProminence',MPP);
[~, locs_hr] = findpeaks(pulse(124*fs:164*fs),'MinPeakHeight',MPH,'MinPeakDistance',MPD);

% Calculate Rates (based on 200s window)
RR = (peakNum1 / fs) * 60; % This would be incorrect
RRdis = t(locs_tidalin);
RRdiff = diff(RRdis);
RR = mean(60./RRdiff)

% HR = (length(locs_hr) / 200) * 60; % incorrect
%holdtime = 124 to 164
locs_HR = locs_hr+fs*124;
HRdis = t(locs_HR);
HRdiff = diff(HRdis);
HR = mean(60./HRdiff)
% HR2 = 60*(length(locsP)/tvtime)  % ok to calculate it this way too.

% Output results to Command Window
fprintf('peakNum1: %d\nvalleyNum1: %d\nRR: %.2f\nHR: %.2f\n', peakNum1, valleyNum1, RR, HR)

% Plotting
figure;
subplot(2, 1, 1);
plot(t, resp, 'k'); hold on;
plot(t(locs_in), resp(locs_in), 'co'); % Inhalation peaks (Cyan Circles)
plot(t(locs_tidalin), resp(locs_tidalin), 'ro'); % Inhalation peaks (Red Circles)
plot(t(locs_tidalex), resp(locs_tidalex), 'g*'); % Exhalation valleys (Green Asterisks)
title('Respiratory Data (Channel 1)'); ylabel('Amplitude (AU)'); xlabel('Time (s)');

subplot(2, 1, 2);
plot(t, pulse, 'k');
hold on
title('Pulse Data (Channel 2)'); ylabel('Amplitude (AU)'); xlabel('Time (s)');
plot(t(locs_HR), pulse(locs_HR), 'co'); % Inhalation peaks (Cyan Circles)