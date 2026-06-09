# PSet04_ES53_2025draft.docx — text digest

_Extracted text from 301 paragraphs. Images, tables, and formatting omitted._

ES 53 - Quantitative Physiology Fall 2025

Problem Set 4: Cardio and Vascular Physiology

[For the MATLAB components of this assignment please include any code where indicated, such as in a specific box. Please include your figures in the main body of your answer set where indicated.Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.][For the MATLAB components of this assignment please include any code where indicated, such as in a specific box. Please include your figures in the main body of your answer set where indicated.Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]Due Tues. Oct. 14th         (out of 48 points)

[For the MATLAB components of this assignment please include any code where indicated, such as in a specific box. Please include your figures in the main body of your answer set where indicated.

Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

[For the MATLAB components of this assignment please include any code where indicated, such as in a specific box. Please include your figures in the main body of your answer set where indicated.

Be sure to keep all of your answers with the boxes provided and be sure to clearly CIRLCLE your final answers.]

[3 pts] If a person has a cardiac output of 6 L/min, and a blood pressure of 120/80 what is the total peripheral resistance of this person’s systemic vascular network? Computer your answer both in mmHg·min/mL and in Pa·s/cm3. Be sure to show how you converted your units.

[7 pts] Use the MATLAB data in PVloop.mat to answer the following questions. The first row of data is a set of volumes (in mL), and the second is a set of corresponding pressures (in mmHg) for a single cardiac cycle.

[2] In MATLAB plot the pressure vs. the volume. It should look similar to the graph on the right. Label your axes. 

[2] Calculate stroke work based on the estimate of mean arterial pressure (MAP). Use units of Joules for your answer. Either show your work by hand or include your code where you use MATLAB (preferred) to calculate work.

[Figure here]MATLAB code or calculations by hand:

[Caption here]

[2] Now use MATLAB to calculate the stroke work as the area inside the PV loop. Use units of Joules for your answer. List your answer below and include your MATLAB code in the box.

[Figure here]MATLAB code:

[Caption here]

[1] Do these estimates of stroke work differ at all? If there is a difference, what accounts for it?

[11 pts] Two important metrics for cardiac function are the ejection fraction (EF) and cardiac power output (CPO). Cardiac power output is the energy (work) that the heart produces per unit time. Below are the Wigger’s diagrams for two different patients. Please show your work for each sub-question. 

[3] Which patient’s heart is producing more power? Calculate the power in Watts (Joules/second) for each patient. 

[2] Which heart has a better ejection fraction? Calculate the EF for each patient and indicate which is better.

[2] Which heart does more work to pump 5 liters of blood? Calculate the work (in Joules) to pump 5 liters of blood for each heart and indicate which does more work.

[4] Draw the corresponding PV loops for each of these on the same set of axes. Could these two patients possibly have the same ESPVR and EDPVR relationships? Why or why not?

[Yes/No & Why or why  not?]

[6 pts] Mitral regurgitation leads to reduced cardiac efficiency. The MitraClip by Abott Vascular attempts to address this by placing a small clip on the mitral valve. 

[2] You are given a “normal” PV loop. Indicate on the graph how the PV loop would differ for someone with mitral regurgitation, if at all.

[2] What specifically is different about the PV loop in mitral regurgitation vs. the PV loop of a person with a normal valve?

[2] What happens to the pressure in the pulmonary circulation when the pressure builds up in the left atrium?  [increase, decrease, or remain the same] Why?

[11 pts] Let’s simplify the body into the following resistive networks. In the diagram below you are given the % blood flow through each network. The total cardiac output is 6 L/min. For simplicity, assume the pressure drop across the heart is equal to the mean arterial pressure. The systolic pressure of this heart is 110 mmHg and the diastolic pressure is 70 mmHg. The percentage of that total CO is shown above/below each organ.  

a) [2] Draw a resistive network that represents the organs (note that they are modeled as being in parallel with each other). 

b) [3] What is the total peripheral resistance (TPR) of this whole network of organs in N·s/m5? 

c) [2] What is the individual resistance (in N·s/m5) of each of the following organs? Kidneys and Brain 

d) [2] What is the pressure drop (in mmHg) of each of the following organs? Kidneys and Brain 

e) [2] What is the flow (in mL/min) of each of the following organs? Kidneys and Brain 

KidneysBrain

[10 pts] In lab you measured the average velocity of blood flowing in one of your carotid arteries. The ultrasound system measured the average velocity between the two green cursors, but could never measure the absolute max velocity. Assume that you had a right carotid artery with a diameter of 6 mm. Assume you had a cardiac output of 5 L/min and 5% of that flow went to your right carotid artery. [Hint: it will be helpful to watch the vimeo video or read the corresponding notes in order to derive the right equations for this question.]

[2] Calculate the average velocity in this carotid artery assuming laminar flow? (Base your answer only on the information given. Don’t use the color bars on the images). List your answer in cm/s.

[2] What portion of the flow is in the center 2 mm (diameter = 2 mm) of the artery (e.g r = 0 to r = 1 mm)?

[2] What is the average velocity of this flow in the center portion? List your answer in units of cm/s.

[2] Given all of the information above that you either calculated or were given, what should Vmax be? List your answer in units of cm/s.

[2] What is the velocity of blood that is at a radius of 1 mm in this vessel?

Appendices for Code
