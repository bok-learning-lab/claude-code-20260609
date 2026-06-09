# PSet09_ES53_2025_ANSWERKEY.docx — text digest

_Extracted text from 169 paragraphs. Images, tables, and formatting omitted._

ES 53 - Quantitative PhysiologyANSWER KEY Fall 2025

Problem Set 9: Renal Filtration Modeling

Due Tues. Nov. 25th           (out of 30 points)

Make sure you show all of your work and include units throughout your calculations. Be sure to keep all of your answers within the boxes provided. Be sure to clearly CIRLCLE your final answers.For Question 3, be sure to include MATLAB images, but you do not need to include code.Make sure you show all of your work and include units throughout your calculations. Be sure to keep all of your answers within the boxes provided. Be sure to clearly CIRLCLE your final answers.For Question 3, be sure to include MATLAB images, but you do not need to include code.

Make sure you show all of your work and include units throughout your calculations. 

Be sure to keep all of your answers within the boxes provided. 

Be sure to clearly CIRLCLE your final answers.

For Question 3, be sure to include MATLAB images, but you do not need to include code.

Make sure you show all of your work and include units throughout your calculations. 

Be sure to keep all of your answers within the boxes provided. 

Be sure to clearly CIRLCLE your final answers.

For Question 3, be sure to include MATLAB images, but you do not need to include code.

1. [9 pts] Biftu is in the hospital and is undergoing testing to check her kidney function before undergoing a double kidney transplant. Biftu is also receiving an intravenous (i.v.) drip infusion of a drug at a constant rate such that her levels of drug, PAH, and inulin are all constant. She is examined over a 24 hour period and a lab has acquired the steady state blood and urine test results as listed below. Biftu is known to have a hematocrit of 45% and a hemoglobin concentration of 13 gHb/ml. She did not exercise during this 24 hour period.

urine volume = 1.0 L

urine [inulin] = 2.0 mg/mL

urine [drug] = 1 mg/mL

urine [PAH] = 30 mg/mL

urine [creatinine] = 2.0 mg/ml

blood volume = 6 Lplasma volume = 6000 mL * 55% = 3300 ml

blood [inulin] = 0.055 mg/mLplasma [inulin] = (0.055 mg/ml)/55% = 0.100 mg/ml

blood [drug] = 6 mg/dLplasma [drug] = (6 mg/ 100ml)/55% = 0.109 mg/ml

blood [PAH] = 0.09 mg/mLplasma [PAH] = (0.09 mg/ml)/55% = 0.164 mg/ml

blood [creatinine] = 5.5 mg/dLplasma [creatinine] = (5.5 mg/ 100 ml)/55% = 0.100 mg/ml

The clearances are all calculated as Ux* / Px,      where  = rate of urine flow in mL/min 

You can calculate  from the total urine volume created in the 24 hour period. There are 1440 minutes in a 24 hour period, so  = 1.0 L/1440 min

[1] What is the renal plasma flow (RPF) in mL/min?

RPF, the effective renal plasma flow, is the clearance of PAH because PAH is completely secreted.

RPF = CPAH = 30 mg/mL * (1.0 L/1440 min ) / 0.164 mg/L =  127 mL/min

[1] What is the glomerular filtration rate (GFR) in mL/min? Is this a relatively normal GFR? Please comment.

GFR is the clearance of inulin because inulin is freely filtered, but not reabsorbed or secreted.

GFR = Cinulin = 2.0 mg/mL * (1.0 L/1440 min ) / 0.100 mg/L =  13.9 mL/min

[1] What is the rate of excretion of creatinine in mg/min? 

The rate of creatinine excretion is  * Ucre = (1.0 L/1440 min ) * 2 mg/mL =  1.39 mg/min

[1] What is the rate of creatinine production in mg/min?

At steady state the rate of creatinine production is equivalent to the rate of creatinine excretion. Therefore  * Ucre  = Ccre * Pcre and since Ccre = GFR then the production is also equal to GFR * Pcre

Rate of production of creatinine is 1.39 mg/min

[1] What is the plasma clearance rate of creatinine in mL/min?

Ccre = 2.0 mg/mL * (1.0 L/1440 min ) / 0.100 mg/L = 13.9 mL/min

[2] Assuming the drug is freely filtered is the drug also: Reabsorbed? Excreted? Secreted? Or none of these? How do you know?

First, we’d need to know the clearance of the drug  Cdrug = 1.0 mg/mL * (1.0 L/1440 min ) / 0.109 mg/mL = 6.37 mL/min

Since the clearance of the drug is lower than the clearance of inulin (GFR) then this drug is partially reabsorbed.

[2] Hemolysis, the rupture of blood cells, can occur due to several different diseases, infections, or from very high shear forces on the blood. In hemolysis, the cellular contents (primarily hemoglobin) are released into the blood plasma. Hemolysis can be dangerous to the kidneys. Given what you know about kidney function explain why this is true (Hint: Think about the effects of increased plasma concentration of hemoglobin.)

A higher protein concentration in the blood leads to a greater oncotic pressures which leads to a reduced GFR based on Starling’s equation.

2. [16 pts] Sanna is considering donating a kidney to her twin sibling. Before doing so she must first undergo some diagnostic renal function tests. While at the clinic she has been getting steady infusions of PAH and inulin such that her blood levels have reached steady state. She has been at rest this whole time. The following test results were obtained over a 24-hour period:

Blood volume = 4000 ml

Hematocrit = 40%

Hemoglobin concentration = 14.4 gHb/dL

urine volume = 2.0 L

urine [cre] = 1.44 mg/mL

urine [inulin] = 1.44 mg/mL

urine [PAH] = 5.75 mg/mL

plasma [cre] = 20.0 µg/mL

plasma [inulin] = 20.0 µg/mL

plasma [PAH] = 20.0 µg/mL

Please be sure to show your calculations and include all units!

[1] What is Sanna’s glomerular filtration rate?

[1] What is Sanna’s renal plasma flow?

[2] Sanna also needs to take a special drug while receiving the inulin and PAH infusions. It is known that her kidneys clear it at a rate of 120 mL/min. What infusion rate should she receive if she needs to maintain a plasma concentration of 10 µg/mL? List your answer is appropriate units.

[3] Draw the plasma concentrations of creatitine (Pcre) and the drug (Pdrug) on the graph below. Add labels to differentiate the two. Use appropriate units and values on all axes. Denote the plasma concentrations before and after infusions stop.

[3] Determine equations for the plasma concentrations of creatitine (Pcre) the drug (Pdrug) as a function of time starting from the time the infusions were stopped and for the next ~ 30 minutes. [Clearly indicate your two equations. Do not leave any variable other than time in your equations.]

[2] The clinical team wants to determine if they can start a kidney transplant before the plasma concentration of the drug reaches 2 µg/mL. How much time will the clinical team have? What is the time constant associated with this process? Please answer both questions.

[1] After one half hour since the infusions stopped one of the kidneys is removed. What happens to the creatinine and drug concentrations in the plasma over time? Please indicate your answers by drawing these on the graph on the previous page.

[3] Determine new equations for the plasma concentrations of creatitine (Pcre) and drug (Pdrug) starting just after the kidney is removed. Be sure to clearly indicate and define any time constants.

3. [5 pts]  Use the renal MATLAB code from lab this week to assess kidney filtration of inulin and answer the following questions. Specifically:

a. [1] In what ways is inulin similar to creatinine in terms of filtration, secretion, reabsorption, and excretion?

Inulin is similar to creatinine in that it is freely filtered from the glomerulus into Bowman’s space, but it is not secreted, or reabsorbed. Inulin’s excretion follows the same path as creatinine. The major difference is that the body does not endogenously produce inulin, instead it must be injected. 

b. [1] Using the renal sim code, set the variables to mimic inulin instead of creatinine. Set these variables such that you have zero “creatinine” (inulin) at baseline to mimic the level of inulin in the blood in a normal human. Recall that the body does not produce inulin. Run the simulation under these conditions and collect a screen shot of the GUI with your plots. 

To mimic inulin we know that it should be filtered the same way as creatinine, so GFR should be the same as what was used for creatinine. For this simulation GFR is will be set to 1.25 dL/min, which is roughly normal physiological GFR (recall in class we assumed 1 L/min of blood goes to the kidney, hematocrit is 0.4, and about 20% gets filtered into Bowman’s space). Before inulin is injected there is no inulin in the blood. First we must simulate this scenario by setting the initial concentration to zero, and the inflow (rate in, a.k.a. Creatinine/inulin added over time) to zero. This should yield flat lines for all four graphs in the simulator. 

c. [1] Using the renal sim code, set the variables to mimic a 200mg bolus injection of inulin. List how you set all your variables, run the simulation, and collect a screen shot. Recall that inulin is filtered the same way that creatinine is and removed from the blood the same way that creatinine is removed. 

Next, we will simulate a bolus injection of inulin as a bolus injection of creatinine. We are asked to mimic a 200 mg bolus injection so the “Bolus In” tab should be set to 200. No other tabs should be altered. The initial amount of inulin should still be zero and the Rate In should be zero (since the body does not produce inulin and because we aren’t infusing inulin over an extended period of time). 

d. [2] How long does it take for 63% of the blood to be cleared of inulin? In other words, what is the time constant, τ? You can read this off of your graph from part c. 

When the concentration has been reduced by 63% that is the same as having 37% remaining. (Recall e-1 = 0.3679) Since our concentration starts at 4 mg/dL we are looking for the time at which the concentration is equal to 4*0.37 = 1.48. By simply reading the graph we see that the time at which this occurs is ~41.3 minutes (the units aren’t labeled in this simulator, so they are arbitrary time units, but most likely are in minutes). This means that τ = 41.3 minutes. 

**Your final answer will depend on what you chose for GFR. For example, if you chose 2 dL/min then your answer will be 26.4 time units. If you chose another value, your tau, τ, will be different.**

e. [2] What happens to the length of time that it takes to clear 63% of the inulin from the blood if you double the amount of the inulin bolus? 

When the bolus amount doubles to 400 mg this should increase the total amount of time required to filter out all of the inulin from the blood, however, since GFR is constant, the time it takes to reach 37% of the initial concentration is still the same. This means that τ is still 41.3 time units. You can check by searching for the time at which the concentration is equal to 8*0.37 = 2.96 mg/dL. 

You can see that τ is linearly related to GFR and is independent of the amount of inulin injected.
