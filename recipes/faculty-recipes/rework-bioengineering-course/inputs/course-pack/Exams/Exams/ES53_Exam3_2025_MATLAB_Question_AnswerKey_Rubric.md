# ES53_Exam3_2025_MATLAB_Question_AnswerKey_Rubric.docx — text digest

_Extracted text from 176 paragraphs. Images, tables, and formatting omitted._

ES 53: Quantitative Physiology [2025]

Exam 3 – Non-timed MATLAB Question 

INSTRUCTIONS: 

We recommend setting aside approximately 30-60 minutes to finish the final MATLAB question; however you can spend as much time as you want on it before the deadline (12:30pm Eastern Thursday Dec. 4th).

You must complete this coding task on your own without the help of others. Any AI you use is your responsibility to check and verify for correctness. No copying from others or the internet is allowed. You may however use parts of your own past code that you wrote, and you may use the online MATLAB documentation. No collaboration or TF help on this exam question is allowed. It must represent your work only and you cannot borrow code from any other peers with whom you may have worked during the semester.

Submit two files to Gradescope. Submit the graph of the output of your code as a PDF. Also submit your m-file script (not a live script). Go back and check that both files show up clearly in Gradescope. 

Good luck!

Download the .mat data file (respiratorydata.mat) from Canvas. This is just like the data you collected in lab 6.

Specifically, 

Write a single script (as opposed to a function) that imports the data and can find the peaks and valleys of the respiratory and pulse data before and during a breath hold experiment. It must be no more than 60 lines of code. Specifically, make sure it does the following and is clearly commented so that others can follow your code: 

Plot the data from the first block of each of the first two channels of data. These should be plotted in one single figure with two subplots (one for each channel). See example figure above.

Plot only the first 200 seconds of each of these channels. 

Plot the raw data in black and use appropriate axis labels and units (as shown above).

Find and plot the inhalation peaks during tidal breathing as red circles on the respiratory plot.

Find and plot the exhalation valleys during tidal breathing as green asterisks on the respiratory plot.

Find and plot the pulse peaks during the breath hold as red circles on the pulse plot.

Find the number of inhalation peaks during tidal breathing and have your code output that number to the command window. [Name this variable peakNum1]

Find the number of exhalation valleys during tidal breathing and have your code output that number to the command window. [Name this variable valleyNum1]

Find the number of pulse peaks during the breath hold and have your code output that number to the command window. [Name this variable peakNum2]

Find the respiratory rate during tidal breathing, and have your code output that number to the command window [Name this variable RR]

Find the heart rate during tidal breathing, and have your code output that number to the command window [Name this variable HR]

Do not hard code. Use variables from the mat file.

Your code must work when we download it and test it. 

It cannot contain more than 60 lines of code.

In gradescope, upload your figure as a PDF and upload your code as an m-file. 

ANSWER KEY

Example Code

%Exam 3, 2025 MATLAB Question

% Written by Linsey Moyer

clear all

close all

load('respiratorydata.mat'); % Load data and isi variables

fs = samplerate(1);               % Calculate sampling frequency (Hz)

N = round(200 * fs);         % Number of samples for 200 seconds

t = (0:N-1) * (1/fs);    % Create time vector

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

Grading rubric:

Total 9 points

Correct -0

Does the PDF match the output of the code? If no -3

Does the code run without needing revisions? If no -2 to -8 depending on severity

Is it more than 60 lines of code? Give a little leniency up to 70 lines. If longer -1

Is the correct time range properly displayed with correct labels? If no –1

Resp: mV (but don’t take off if labeled Volts, since sample labels as Volts)

Pulse: V

Are any peaks or valleys denoted outside of the tidal breathing in respiratory graph or outside of breath hold in pulse graph? If yes, -1 for each.

Are the correct numbers of peaks and valleys found? Both should be in the 35-48 range in respiratory graph, and peakNum2 should be in 50 (45-55 range) in pulse graph. If outside then -1 point per type.

Do not take off points if peakNum1 and valleyNum1 are larger due to plotting after breath hold

Do not take off points if peakNum2 is larger due to incorrect plotting (points were taken off in part 6)

Is RR calculated correctly? This should be ~ 21 bpm. (Anything from 16-26 is fine) If outside this range -1

Is HR calculated properly? This should be ~ 69 bpm. (Anything from 64-74 is fine). If outside this range -2

Was hard coding used? If yes, -0.5 (for 1-2); -1 (for 3-4); -1.5 (for 5-6); -2 (for more than 6)

Correct colors and styles used for markers? If no, -1

Are the correct variables defined? If no -1 or 2 depending on severity

peakNum1 = 40

valleyNum1 = 43

peakNum2 = 50

RR = 21.42

HR = 69.26

Did they submit an actual m file?

If no – 1
