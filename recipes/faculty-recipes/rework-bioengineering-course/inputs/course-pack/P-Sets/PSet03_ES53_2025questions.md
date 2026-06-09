# PSet03_ES53_2025questions.docx — text digest

_Extracted text from 304 paragraphs. Images, tables, and formatting omitted._

ES 53 - Quantitative Physiology Fall 2025

Problem Set 3: Muscle & Hill’s Model

Due Tues. Sept. 30th        (out of 60 points)

[For the MATLAB components of this homework please include any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.][For the MATLAB components of this homework please include any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

[For the MATLAB components of this homework please include any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.

Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

[For the MATLAB components of this homework please include any code as an appendix at the end rather than only publishing your code. Please include your figures in the main body of your answer set.

Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

1. [8 pts] Consider a muscle described by Hill’s Equation. 

a) [4] If ,  and at zero load the muscle contracts with a velocity of , then what is ? Use MATLAB to plot the force velocity relationship for this muscle. [Append your code to your submission.] 

Figure only:

b) [4] Hill's model can be used to simulate different types of muscles. We will continue to investigate a muscle that contracts at  under zero load. Hold  (at the value for  you found in part a) and investigate the impact of varying the parameter . Change  from  to  in steps of . (Remember that you will have to vary  as you change  in order to fix the zero load velocity to be !). For each value of , use MATLAB to plot the force velocity relationship. [Append your code to your submission. ]

Figure only:

2. [6 pts] Compare and contrast skeletal muscle cells with cardiac muscle cells. 

a) [2] Why can tetany not be reached in cardiac muscle cells?

b) [4] On the same time scale draw the typical action potential for a skeletal muscle fiber. Draw and clearly indicate the calcium transients and the twitch force for the cell. Repeat for the cardiomocyte and draw the action potential, calcium transient and twitch force. Include time scales and label both axes.

3. [5 pts] One form of arrhythmia is fibrillation. Below is an example ECG from a patient with atrial fibrillation.

a) [2] Is atrial fibrillation or ventricular fibrillation more dangerous? Why? Explain in one sentence. 

b) [1] In the grid above, draw a representative ECG for a patient with ventricular fibrillation.

c) [1] How do you expect V-fib to affect cardiac output?  (Circle one)

IncreaseDecreaseLittle/No Change

d) [1] How do you expect V-fib to affect stroke volume?  (Circle one)

IncreaseDecreaseLittle/No Change

4. [5 pts] Work, in its simplest definition, is the product of the force applied to an object and the distance the object moves ( W = force × distance). In considering pressure-volume work, we must revise this definition. Imagine that we have a volume of blood in a syringe. If we apply a constant force to the plunger—that is, if we apply a constant pressure to the blood—the plunger moves a certain distance as we eject the blood through the needle, thereby reducing blood volume by an amount Δ V. How much work have we done? For pressure moving a fluid, the external work is W = P·ΔV

[Note: If the aortic pressure were constant, the work done with each heartbeat would be simply the product of the aortic pressure (P) and the stroke volume (Δ V = SV = EDV − ESV). Instead, to calculate stroke work we estimate this as the mean aortic (arterial) pressure (MAP) times the stroke volume (SV).]

This leaves you with units of mmHg·mL. These units are rather meaningless. 

[2] Show that the units of mmHg·mL are really the product of force (in Newtons) times a distance (in meters). [If you haven’t taken physics yet just look up these units or refer to the handy equation sheet.]

[1] Show that these units (mmHg·mL) are equivalent to Joules. In other words, show that your answer in part A is equal to the definition of a Joule in terms of kg, m, and seconds.

[2] Given a heart that performs with a MAP of 100 mmHg and ejects 75 mL per stroke, what is the stroke work in units of Joules?

5. [18 pts] Patients with congestive heart failure (CHF) have a reduced ability to pump blood which can be due to an enlarged left ventricle with a thin wall. 

Below are two pressure-volume loops corresponding to the left ventricular cardiac function of two different patients. One normal, and one with CHF. 

[4 pts] Denote the following on “Patient Y’s” P-V loops below (2nd of the 2 graphs). 

Isovolumetric contraction

Opening of the aortic valve

Systolic pressure

Diastole

Denote items in part ‘a’ on this graph.

[8] For each P-V loop above, calculate the stroke volume (SV), the ejection fraction (EF), mean arterial pressure (MAP), and the cardiac output (CO). Use reasonable units. SHOW ALL CALCULATIONS!

Patient XPatient Y             

 SV = SV = 

 EF = EF = 

 MAP = MAP = 

 CO = CO = 

[4] Calculate the stroke work (SW) in Joules for each of these patients. Which heart is doing more work per minute?

Patient XPatient Y

 [2] One patient is relatively “normal” and the other has congestive heart failure (CHF). Based on the P-V loops, and your calculations above which is likely the abnormal patient and (in a single sentence) why?

6. [14 pts] Signal processing, including peak detection, is critical in all manners of bio-signal processing. This next MATLAB signal processing technique will show up in future labs. Do not worry if it seems complicated at first. You will be a pro by the end of the semester! [Please append all code at the end].

We first want to create a sample signal (we’ll use a sinc function for this) and then find all of the positive and negative portions as well as the zero crossings. ▪ Hint: Look up the function sign() in the MATLAB documentation online

You can start with this code to generate a sinc function:

t = -30:0.001:30;

y = sinc(t);

[1 pt] Plot the sinc function in your first figure (5a).

[2 pts] Plot the derivative of this function in black (remember to include proper titles, axis labels, etc) on a second figure (5b). Mark the zero-crossing points of the derivative with yellow squares

[2 pts] Now use the information gained from the derivative analysis to plot some information on top of the original sinc function (figure 5a). In one figure:

o Plot the original function 

o Mark the peaks and troughs of the original function with yellow squares

You’ve just found peaks by determining the derivative. This works well with some types of data, but it’s not always the best approach when you have noisier data.

[6 pts] Load the data from the data file ‘ECGdata.mat’

This file is on the course site. Again, remember to keep the data file in the same folder as your MATLAB script

To visualize the ECG, plot the data (titled “pdata”) against time (titled “ptime”)

Now, to practice refining the data, use the smooth function to plot variations of the ECG. Plot all four graphs in one figure (5d) using subplots.

Plot the original data.

Plot the same ECG, smoothed, with a span of 10 points

Plot with a smoothed span of 100 points

Plot with a smoothed span of 1000 points

Make sure you understand what smoothing means and does

With comments within your script, briefly discuss the advantages and disadvantages of smoothing, by examining all 4 versions of the  graph.

Your plots should end up looking like this:

[3 pts] Create a new figure. Mark the peaks and troughs of your “best” smoothed ECG trace with yellow squares 

5a/c Figure only:

5b Figure only:

5d Figures only:

5e Figure only:

Appendices (Only include code that you wrote. Do not include the code you were already given.)

Code for Q1:

Code for Q5:
