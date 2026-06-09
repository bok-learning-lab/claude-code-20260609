# ES53_Exam3_Example_Questions_AnswerKey.docx — text digest

_Extracted text from 247 paragraphs. Images, tables, and formatting omitted._

Name:__________________________________________________                  Examples

ES 53: Quantitative Physiology

Quiz 3 – Pulmonary and Renal Physiology 

Instructions: This is a two-part quiz. You will complete a MATLAB exercise within the next 48 hours and will complete the written portion in the next 75 minutes. 

Written:

Initial each page. 

Show all of work your work clearly! This includes any equations or assumptions you start with, calculations or intermediate steps, and a clearly marked final answer. 

Make sure to read and answer all parts of the question! 

You may use a calculator (no phones or devices that connect to the internet) and may use one, one-sided sheet of pre-written/typed notes. You may write on the blank pages, but clearly label which questions you are answering and your final answers. You will have 75 minutes to complete the written portion of the quiz. You may keep your note sheet after the quiz is over. 

There is also an extra note sheet and saturation curves on the last page of this quiz.

Non-timed MATLAB quiz question:

We recommend setting aside approximately 30-60 minutes to finish the final MATLAB question; however you can spend as much time as you want on it before the deadline (12:30pm Eastern Thursday Dec. 4th).

You must complete this coding task on your own without the help of others. You may  use parts of your own past code that you wrote, and you may use the online MATLAB documentation. No collaboration on this quiz question is allowed. It must represent your work only.

Submit two files to Canvas. Submit the graph of the output of your code as a PDF. Also submit your m-file function (not a live script). Go back and check that both files show up clearly in Canvas. 

Good luck!

I have read the instructions and understand what resources I can and cannot access for both portions of this quiz. On my honor I will follow these instructions.

Signed:______________________________ 

Date:________________

[18 pts] Consider how hyperbaric chambers increase the PO2 by increasing both the percent of air that is oxygen (from 21% up to as much as 100%) and increasing the atmospheric pressure (up to ~ 3 atm.) [You should include dissolved O2 in the blood in your calculations for this question.]

[3] What is the partial pressure of O2 in 

a dry room at sea level, 21%(760 mmHg) = ~160 mmHg

a hyperbaric chamber with 80% O2 and 2 atm of pressure80%(2*760 mmHg) = 1216 mmHg

and at the top of a mountain that has an atmospheric pressure of 0.7 atm and normal ratios of oxygen to nitrogen and carbon dioxide  21% (0.7*760 mmHg) = 112 mmHg

[2] Consider how breathing oxygen at hyperbaric (i.e. above atmospheric) pressures or high altitude would change oxygen delivery to the lungs. Calculate the alveolar PO2 (in mmHg) if the atmospheric PO2 is increased from baseline (dry, sea level) to the partial pressure you found in part (a-ii) where the O2 fraction is 80% and P=2 atm. And - part (a-iii) where P=0.7 atm.

PaO2 = 80%(2*760mmHg – 47 mmHg) – PCO2/R = 1178 mmHg – 50 mmHg = 1128 mmHg

- part (a-iii) where P=0.7 atm.

PaO2 = 21%(0.7*760 mmHg – 47 mmHg) – 50 mmHg = ~52 mmHg

[9] To treat CO poisoning, some hospital emergency rooms have hyperbaric chambers where patients can breathe at very high PO2 levels. Consider a patient with [15gHb/dL] who was exposed to an environment with a carbon monoxide such that the alveolar partial pressure of CO is 0.1 mmHg. He is then rapidly brought to the ER and put in the aforementioned hyperbaric chamber where the pressure is 2 atm. [You should include dissolved O2 in the blood in your calculations for this question.] What % O2 would be required in the chamber to allow for an O2 consumption level of 275 ml O2/min with a cardiac output of 5 L/min, while 

i) maintaining a tissue PO2 of 40 mmHg? 

ii) maintaining a tissue PO2 of 30 mmHg?

iii) maintaining a tissue PO2 of 30 mmHg if this were instead a woman ([Hb] = 12 g/dL)?

Given that this person has carbon monoxide poisoning we’re going to need to treat him/her with an oxygen partial pressure greater than normal sea-level atmospheric pressure. So that means that the inspired air in the new treatment environment must be greater than normal, and PaO2 will end up being greater than normal (where normal is ~100 mmHg for PaO2). So that means that the arterial SaO2 will always be 100% of the remaining available Hb sites.

It’s helpful to first determine what new PaO2 is required then back calculate the chamber PO2 from PaO2. Once we have the chamber PO2 we can figure out what %O2 would be required at 2 atm.

Recall )   

and CAO2 = (SaO2 · 1.34· Hb) + 0.003 · PAO2       and      CVO2 = (SaO2 · 1.34· Hb) + 0.003 · PvO2

We need to account for the CO poisoning. The available [Hb] must be reduced due to the 0.1 mmHg PCO - which in this case is a 50% reduction (based on the given graph for CO-Hb saturation).

 = Q*[(ΔHb-O2 blood conc.) + (dissolved O2 conc.)]   = 5.5 mL O2/dL

[2] Will the aforementioned hyperbaric chamber (80% O2 and 2 atm) be sufficient to help the people in the scenario in part (c)? If yes, which one(s)? If no, which one(s)? Briefly explain how you came to these conclusions.

Yes, for all three cases since the necessary %O2 was always below 80% so the chamber will be more than sufficient for each of the three scenarios.

[2] Which is worse? Exposure of carbon monoxide at a level of 0.1 mmHg or being stranded on the arid (assume 0% humidity) mountain at 0.7 atm? Use quantitative reasoning to show why one is worse than the other. (There isn’t a single right answer here. Show me that you can quantitatively reason through this.)

CO poisoning at 0.1 mmHg is worse because 50% of the O2 carrying capacity is gone in this case. So half as much oxygen is in the arteries despite a normal PaO2. 

At 0.7 atm (which is 532 mmHg) the PaO2 is: 

This is about 70-80% saturation which is much better than 50% saturation!

2. [24 pts] Ifeoluwa is in the hospital and is undergoing testing to check their kidney function before undergoing a double kidney transplant. Ifeoluwa is also receiving an intravenous (i.v.) drip infusion of a drug at a constant rate such that her levels of drug, PAH, and inulin are all constant. She is examined over a 24 hour period and a lab has acquired the steady state blood and urine test results as listed below. Ifeoluwa is known to have a hematocrit of 45% and a hemoglobin concentration of 13 gHb/ml. She did not exercise during this 24 hour period.

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

[3] Before surgery the i.v. infusion of the drug is stopped. Once the i.v. infusion is stopped how long will it take for the plasma concentration to drop down to only 10% of its initial concentration? List your answer in minutes.

First, we need an equation that describes how the concentration in the plasma changes as a function of time once we’re no longer in steady state. 

[drug]before = 0.109 mg/ ml = P0tau = PV/Cdrug = 3300 ml/6.37 ml/min = 518 min

[drug](t) = P0 * e^(-t/tau) = 0.109 mg/ml* e^(-t/518min)

10% P0 = P0 e^(-t/518min)      ln(0.1) = -t/518 min

t = -518*ln(0.1) = 1193 min

[2] This person will now undergo a double kidney transplant. Using the plot given to you plot the Creatinine concentration ([Cre]plasma) in the plasma vs. time over 2 hours prior to surgery. Plot this in the first third of the graph. Label axes and provide units and correct numerical values. 

[3] How, if at all, does the graph of [Cre](t) change while the kidneys are disconnected from the body? Draw this in the middle of the graph between start surgery and end surgery time points. Derive an equation for the plasma creatinine concentration (Px(t)) over time starting at the beginning of surgery.

The Cre concentration increases linearly starting at the steady state concentration in the plasma.

[3] They need to finish the surgery before the blood creatinine concentration reaches 8.25 mg/dl. Will they be able to do this within two hours? Please quantitatively show how you reached your conclusion.

First we need to know the plasma concentration in order to compare.

Bx = 8.25 mg/dl so Px = 150 ug/ml or 0.15 mg/ml

[1] During surgery what happens to the clearance rate? (increase, decrease, or the same)          

It decreases since no plasma is being filtered.                      

What happens to the creatinine production rate during surgery? (increase, decrease, or the same)

It stays the same since the person is still at rest.

[2] When the surgery is complete the new kidneys are connected and each has a has a GFR of 60 ml/min. What is the new renal plasma clearance rate in ml/min? Plot the creatinine concentration over time in the patient once the new kidney is connected (do this in the third part of the graph post surgery). 

The renal plasma clearance of Cre is just GFR so 2*60ml/min = 120 ml/min

[3] Write an equation for the creatinine concentration (Px(t)) over time starting at the end of surgery. Be sure to denote the initial starting concentration at the very end of surgery.

You could start the decay from 120 minutes of the time point that you calculated for when the blood [cre] = 8.25 mg/dl. Here it is calculated from the end of the surgery (119 minutes).

where tau = 3300 ml/(120 ml/min) = 27.5 min

[2] Hemolysis, the rupture of blood cells, can occur due to several different diseases, infections, or from very high shear forces on the blood. In hemolysis, the cellular contents (primarily hemoglobin) are released into the blood plasma. Hemolysis can be dangerous to the kidneys. Given what you know about kidney function explain why this is true (Hint: Think about the effects of increased plasma concentration of hemoglobin.)

A higher protein concentration in the blood leads to a greater oncotic pressures which leads to a reduced GFR based on Starling’s equation.
