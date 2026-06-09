# PSet01_ES53_2025_ANSWERKEY.docx — text digest

_Extracted text from 452 paragraphs. Images, tables, and formatting omitted._

ES 53 - Quantitative PhysiologyANSWER KEY Fall 2025

Problem Set 1: Electrical Principles of Cells- Membrane Potentials

Due Tues. Sept. 16th        (out of 60 points)

[For the MATLAB components of this homework please copy and paste any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.][For the MATLAB components of this homework please copy and paste any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

[For the MATLAB components of this homework please copy and paste any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.

Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

[For the MATLAB components of this homework please copy and paste any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.

Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

For reference, you may find these equations helpful:

Nernst Eq

-61 mV *(log(Cin/Cout))/z

Where R = the gas constant [ 8.314 J / (mol K) ]

T = absolute temperature [K]; assume body temp in constant = 310 K

F = Faraday’s constant [ 9.64 x104 J / (V mol) ] or [C/mol] 

z = valence (charge) of the ionic species 

Chord Conductance Eq  GHK Eq

A few tips for MATLAB:

To create an exponential function in MATLAB:

%first create a time vector and a time constant

t = (0:8/200:8); % time vector

tau = 1.2028;    % ms

y = exp(-t/tau); % exponential curve for e^-(t/tau)

figure, plot(t,y)% plot to visualize the curve

1. [4] Let’s practice some dimensional analysis. 

a) [2] The flow of fluids is critical to understanding the cardiovascular and pulmonary systems. Using dimensional analysis show that the dimensions of flow (volume per units time) are equivalent to a velocity times a cross sectional area. 

b) [2] Blood flow is often measured in units of milliliters per minute, whereas drugs and saline are often measured in cubic centimeters. If you’ve ever watched a medical TV drama or movie you might hear the doctors/nurses saying “Quick push 5 CC’s stat! How many milliliters are in 5 CCs? How do you convert from CC to milliliter? [Just show me that you now know this conversion.]

1 milliliter = 1 cc = 1 cm3

So 5cc = 5 mL

FYI, the “average” human has 5 liters (L) of blood 

5 L = 5000 ml = 5000 cm3 * ((1m/100cm)3) = 5000/(106) m3 = 0.005 m3 So when we talk about blood we’ll largely be using mL or cc.

2. [14 pts] A cell has the following conditions (ignore Ca+2):

[Na+]o = 140 mM [Na+]i = 10 mM

[K+]o = 4 mM [K+]i = 140 mM

[Cl-]o = 125 mM [Cl-]i = 9 mM

The relative conductances of the ions are as follows: gK = 16 gNa and gNa = 0.05 gCl

a) [3] Calculate the Nernst potentials for each ion above.

We first need the Nernst potentials for each ion. -61 mV *(log10(Cin/Cout))/z

ENa =  +69.9 mV

EK = - 94.2 mV

ECl = -69.7 mV

b) [2] Calculate Vmem at rest (hint: use the chord conductance equation)

Here we use the chord conductance equation:

Vmem = gK / (gK + gNa + gCl) EK + gNa /(gK + gNa + gCl) ENa + gCl / (gK + gNa + gCl) ECl

Inserting gK = 16 gNa and gNa = 0.05 gCl à put everything in terms of one g à gCl = 20 gNa; gK = 16gNa

we solve the denominator of each of the ratios as

gK + gNa + gCl = 16+1+20 = 37

Thus the equation becomes

Vmem = 16/37*(+69.9 mV) + 1/37*(-94.2 mV ) + 20/37 *(-69.7 mV) = -76.5 mV

c) [3] Calculate the net driving voltages (i.e. forces) (Vmem – Ex) for INa IK and ICl

The net driving forces for an ion are Vmem - Eion. These are:

For K: Vmem - EK = (-76.5 - -94) mV = 17.7 mV (ok if 18 mV)

For Na: Vmem – ENa = (-76.5 – 70) mV = -146.4 mV (ok if -146 mV)

For Cl: Vmem – ECl = (-76.5 - -70) mV = -6.8 mV (ok if -7 mV)

d) [3] Calculate the relative values of INa IK and ICl in terms of their individual conductances.

The currents are given as gi (Vmem - Ei ):

IK = 17.7 mV* gK = 17 mV* 16gNa = 282.7 gNa

INa = -146.4 mV * gNa = -146.4 mV* gNa = -146.4 gNa

ICl = -6.8 mV * gCl = -6.8 mV * 20gNa =  -136.3 gNa

Note that the sum of the currents is zero!

e) [2] Clinical case: Hypokalemia is caused by abnormally low levels of potassium in the body. Almost 98% of potassium is found inside the cells. Small changes in the level of potassium that is present outside the cells can have severe effects on the heart, nerves, and muscles. 

What happens to the resting membrane potential of this cell if the extracellular potassium level drops to from 4 mM to 2 mM? Quantitatively show your reasoning by recalculating Vmem.

The new Nernst potential for Potassium becomes -112.5 mV

Recalculating using the chord conductance equation the new Vmem is: -84.5 mV  

f) [3] At what extracellular concentration of potassium would the membrane potential drop below -100 mV? (assume all other concentrations stay the same as listed above) Quantitatively show your reasoning and calculate the new [K+]o.

First we have to find out what Nernst potential would be required for VK to reach a Vmem of -100 mV.

Solve the chord conductance equation for EK: 

(Vmem – [gNa /(gK + gNa + gCl) ENa + gCl / (gK + gNa + gCa) ECl])* (gK + gNa + gCl) / gK = EK 

We plug in our previous Nernst potentials for Cl and Na, as well as the ratios of conductances. We use -100 for the Vmem. After plugging everything in we get: EK = -148.5 mV

Now using the Nernst potential equation we rearrange:

-61 mV *log10 (Cin/Cout) = -61 mV *[log10 (Cin) – log10(Cout)] = -148.5 mV 

and we know that Cin is 140 mM for potassium

(-148.5/ -61) - log10 (140mM) = -log10(Cout) à Cout = ~0.5 mM

3. [ pts] Myotonia is the inability to relax (a) skeletal muscle(s) after a voluntary contraction. These were initially described in medical literature in the early 1900s. Some types of myotonia are now known to be caused by mutations of voltage-gated ion channels. One specific type of myotonia is caused by “gain-of-function” changes to the voltage-dependent gating of NaV1.4 sodium channels in skeletal muscles. 

a) On the graph to the left below show how the sodium conductance curve would change, if at all, if the sodium activation gates had both i) a greater resting probability of being open due to the mutation and ii) a faster activation rate. [Assume this is for a similar experiment where the membrane potential is forced to increase to ~+23mV).

See graph. The peak should be higher. The rise should start sooner. The peak should be slightly wider.

b) On the graph to the right below draw how the resulting action potential would differ with this sodium channel mutation, if at all. Then briefly describe any differences in a few words. 

See graph. The peak should be higher. The rise should start sooner. The AP should be wider. The resting Vmem should be higher.

n0

m0

h0

n∞

m∞

h∞

τn

τm

τh

c) Which of the following kinetic parameters to the right influence the activation of the sodium channels? (Circle all that apply)

d) Write an equation for the sodium conductance as a function of time including any of the applicable kinetic parameters from above.

 Where:

e) Another mechanism behind some myotonias is a reduction of the resting chloride conductance. What, if anything, is different about the resting membrane potential of these myotonic muscle cells if the chloride conductance was 10x smaller than normal muscle cells? (Circle all that apply)

the membrane potential increases

the membrane potential is no longer at rest 

the membrane potential decreases

the membrane potential stays the sameà b/c chloride doesn’t affect the Vmem much and ECl is very close to Vmem anyway

the chloride Nernst potential increases

the chloride Nernst potential decreases

4. [12 pts] We will be investigating the Hodgkin and Huxley model in more detail in the next p set, but first let’s look at sodium and potassium conductances during a voltage clamp experiment where the membrane potential is indefinitely clamped from -65 to +23 mV. Recall that H&H determined the conductances of these ions by clamping the transmembrane potential to some desired value. To investigate this relationship, follow the supplemental reading on the HH model and create functions in MATLAB that describe the channel behavior. 

[2] Recall the equations for n(t), m(t), and h(t) as described in the handout. You’ll need to refer to the table listed in your H-H handout as well for the empirically derived constants. Create these equations in MATLAB and include all of the constants within a script.

[2] Write equations for gK(t) and gNa(t) as in terms of the individual gmax for each ion, and the equations you wrote for n(t), m(t), and h(t). Clearly include these equations in your answers for this P-set. Create these equations in MATLAB within the same script.

[3] Input your equations from part (a) and (b) into MATLAB. Create a time vector from 0 to 8 ms that includes 201 data points. Plot your functions for gK(t) and gNa(t) as a function of your time vector. Plot both of these on the same MATLAB graph and make gK(t) red and gNa(t) yellow. Label your axes and include units. Clearly include this graph in your answers for this P-set. Clearly include your MATLAB code in your appendix as opposed to publishing your code.

Figure 1.a: Conductances of Potassium and Sodium during a voltage clamp experiment applied from -65mV to +23 mV and predicted by Hodgkin-and Huxley equations for voltage-gated Channels.

[2] Explain why your graph of conductances differs from the red and yellow gK and gNa curves displayed in figure 5 of your H-H handout. Hint: Think about what is different in these two scenarios.

The conductances you’ve just plotted correspond to a cell membrane (a giant squid axon in the case of the first studies by Hodgkin and Huxley) that underwent an experiment where the voltage was clamped from -65 to +23 mV. In the body there are no voltage clamps that control and maintain such a state. In the body a cell undergoes a short action potential due to some other stimulus (e.g. from another neuron). 

[3] Now, create an expression for Vmem(t) based on gK(t) and gNa(t), and the chord conductance equation. Plot Vmem(t) in MATLAB and label your axes. Clearly include this graph in your answers for this P-set. Clearly include your MATLAB code in your appendix. Explain briefly why your graph of Vmem(t) differs from what you would expect for an action potential. You’ll recall that the Chord conductance equation doesn’t hold for a membrane that is not at rest. 

Equation:

Graph:

Caption: Figure 1.e: The membrane potential of a cell as predicted by the chord conductance equation. This does not accurately predict the action potential because it assumes that the net current is zero. However, during an action potential the net current is not zero and the membrane potential changes.

5. [12 pts] Calculating derivatives as a way of finding peaks in data, Examples of these figures are shown below. Be sure to create your own and append your code to your p-set submission.

Declare a time vector from -30 to 30, with increments of 0.001

[2] Plot a sinc function using this time vector, in black (not to be confused with a sin

function) (Fig. 5a)

[2] Plot the derivative of this function in black (remember to include proper titles, axis labels, etc) on a second figure (Fig. 5b)

On a third figure: (Fig. 5c)

[1] Plot the positive portions of this derivative with green points

[1] Plot the negative portions of this derivative with red points

[2] Mark the zero-crossing points of the derivative with yellow squares

-Hint: Look up the function sign in the MATLAB documentation online

Now use the data from the derivative to plot the original sinc function. In one figure: (Fig. 5d)

[1] Plot the portions of the original function where its derivative is positive with green points

[1] Plot the portions of the original function where its derivative is negative with red points

[2] Mark the peaks and troughs of the original function with yellow squares

-Hint: your code finding the zero-crossing points in the  previous section should prove helpful

Figure 5a

Figure 5b

Figure 5c

Figure 5d

6. [10 pts] Understanding our biases and recognizing when our peers are being biased against in a negative way is a step toward better teamwork and better diversity and inclusion for engineers. Go to “Project Implicit” and take two of the tests. In a few sentences or a paragraph explain: 

a) what you learned from the test (any insights you gained), 

b) how you think these types of tests might be useful when designing engineering teams, 

c) how these tests might help engineers at a company create a more inclusive working environment.

Project implicit link: https://implicit.harvard.edu/implicit/takeatest.html

Note: You do not need to create an account, and you should not post your results in your p-set. Just tell us about what you learned.

The answer key is not applicable for this question. Keep in mind that we should always be checking our biases and trying to create as inclusive an environment as we can. 

Appendices

Code for Q4:

Code for Q5:

% Derivatives as a way of finding zero crossings and peaks

% Figure 1: Sinc function

t = [-30:0.001:30];

x = sinc(t);

figure;

plot(t, x, '-k')

title('Sinc Function')

xlabel('Time (t)')

ylabel('sinc(t) (x)')

legend('sinc(t)');

% Figure 2: Derivative of Sinc function

dx = diff(x);

dt = diff(t);

derivative = dx./dt;

avgTs = mean([t(1:end-1);t(2:end)]);

figure;

plot(avgTs,derivative,'-k');

title('Derivative of Sinc Function');

xlabel('Time (t)');

ylabel('d(sinc(t))/dt');

legend('d(sinc(t))/dt');

% Figure 3: Color-coded derivative of Sinc function

signDerivative = sign(derivative);

negIndices = find(signDerivative == -1);

posIndices = find(signDerivative == 1);

zeroIndices = find(signDerivative == 0);

figure;

hold on;

zeroCrossTs = avgTs(abs(diff(signDerivative)) == 2);

plot(avgTs(negIndices), derivative(negIndices), '.r');

plot(avgTs(posIndices), derivative(posIndices), '.g');

plot(zeroCrossTs, zeros(1,length(zeroCrossTs)), 'sy', 'linewidth', 1);

title('Derivative of Sinc Function');

xlabel('Time (t)');

ylabel('dx/dt');

legend('Negative derivative','Positive derivative','Zero-crossing point');

hold off;

% Figure 4: Color-coded Sinc function

figure;

hold on;

plot(t(negIndices), x(negIndices), '.r');

plot(t(posIndices), x(posIndices), '.g');

plot(zeroCrossTs, x(abs(diff(signDerivative)) == 2), 'sy', 'linewidth', 1);

title('Sinc Function');

xlabel('Time (t)');

ylabel('Sinc(t) (x)');

legend('Negative derivative','Positive derivative','Peaks/Troughs');

hold off;
