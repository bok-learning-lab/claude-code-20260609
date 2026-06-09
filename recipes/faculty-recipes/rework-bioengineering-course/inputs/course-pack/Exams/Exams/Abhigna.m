%% Q 1,2,3
s = load('respiratorydata.mat');
r = s.data(s.datastart(1,1):s.dataend(1,1));     % Respiratory
p = s.data(s.datastart(2,1):s.dataend(2,1));     % Pulse
fsR = s.samplerate(1,1);
fsP = s.samplerate(2,1);
N = round(200 * fsR);     
r = r(1:N); p = p(1:N);
t = (0:N-1)/fsR;
% For detecting inhale, hold and breathe times
labels = cellstr(s.comtext);
txtIdx = s.com(:,5);
tidalEndSample = s.com(find(s.com(:,2)==1 & strcmp(labels(txtIdx),'inhale, hold'),1),3);
tidalEndIdx    = min(N, round(tidalEndSample - s.datastart(1,1) + 1));
bhStartSample  = s.com(find(s.com(:,2)==2 & strcmp(labels(txtIdx),'inhale, hold'),1),3);
bhEndSample    = s.com(find(s.com(:,2)==2 & strcmp(labels(txtIdx),'breathe'),1),3);
bhStartP   = max(1, round(bhStartSample - s.datastart(2,1) + 1));
bhEndP     = min(N, round(bhEndSample   - s.datastart(2,1) + 1));
bhStartTime = (bhStartP-1)/fsP;
bhEndTime   = (bhEndP-1)/fsP;
figure;
subplot(2,1,1); plot(t,r,'k'); hold on; grid on; xlabel('Time (s)'); ylabel('Amplitude (mV)'); title('Respiratory Data (Channel 1)');
subplot(2,1,2); plot(t,p,'k'); hold on; grid on; xlabel('Time (s)'); ylabel('Amplitude (V)'); title('Pulse Data (Channel 2)');
%% Q 4,5,6
resp120 = r(1:tidalEndIdx);
resp_s = smooth(resp120, 11);
promR  = 0.15*(max(resp_s)-min(resp_s));
minDistR = 1.5*fsR;
[pksIn, locIn] = findpeaks(resp_s, 'MinPeakDistance',minDistR,'MinPeakProminence',promR);
[pksVal, locVal] = findpeaks(-resp_s, 'MinPeakDistance',minDistR,'MinPeakProminence',promR);
pksVal = -pksVal;
% Q 4,5
subplot(2,1,1);
plot(t(locIn),  r(locIn),  'ro','MarkerFaceColor','r');   % inhalation
plot(t(locVal), r(locVal), 'g*');                         % exhalation
%% Q 6,7,8,9,10,11
% Q 6
pulseBH = p(bhStartP:bhEndP);
pulse_s = smooth(pulseBH, 7);
promP = 0.2*(max(pulse_s)-min(pulse_s));
minDistP = 0.4*fsP;
[pksP, locP] = findpeaks(pulse_s,'MinPeakDistance',minDistP,'MinPeakProminence',promP);
locP_full = bhStart - 1 + locP;
subplot(2,1,2);
plot(t(locP_full), p(locP_full), 'ro','MarkerFaceColor','r');
% Q 7
peakNum1 = numel(locIn); fprintf('inhalation peaks) = %d\n', peakNum1);
% Q 8
valleyNum1 = numel(locVal); fprintf('exhalation troughs) = %d\n', valleyNum1);
% Q 9
peakNum2 = numel(locP); fprintf('Pulse peaks during breath hold) = %d\n', peakNum2);
% Q 10
duration_tidal_sec = (tidalEndIdx-1)/fsR; 
RR = peakNum1 / (duration_tidal_sec/60);   % breaths per min
fprintf('Respiratory Rate during tidal breathing = %.2f breaths/min\n', RR);
% Q 11
duration_bh_sec = (bhEnd - bhStart)/fsP;
HR = peakNum2 / (duration_bh_sec/60);      % beats per min
fprintf('Heart Rate during breath hold = %.2f beats/min\n', HR);
