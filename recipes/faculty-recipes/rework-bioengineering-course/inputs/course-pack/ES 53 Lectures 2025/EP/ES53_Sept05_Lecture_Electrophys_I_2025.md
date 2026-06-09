# ES53_Sept05_Lecture_Electrophys_I_2025.pptx — text digest
_Extracted text from 40 slides. Images, layout, and formatting omitted._

## Slide 1
Head Instructor:
Dr. Linsey Moyer, PhD (she/her)
(You can call me Dr. Moyer  or just Linsey)
Guest Instructor:
Prof. Jennifer Lewis, PhD
Teaching Fellows:
Jonathan Rubins
CAs:
Hayden Graham     Wafiqah Zubair	Saron Meressi 	  	  Katie Ho		 Norene Williams
Armando Patino
Sarah Rose Odutola
Lab & Computational Staff/Engineers:
Avery Normandin:
ave@seas.harvard.edu
Dr. Melissa Hancock:
mhancock@seas.harvard.edu

## Slide 2
Module 1
Electrophysiology
(Sept. 5, 2025)
ES 53
2025
2

## Slide 3
Learning Objectives
1) Describe the forces governing ions inside and outside the cell.
- Define concentration gradients, selective permeability, diffusion, electrostatic force
- Understand how the cell can be bulk net neutral and still have a negative resting potential
- Describe what membrane channels are and what causes their selectivity
2) Calculate the Nernst potential (equilibrium potential) for the 4 most common ions that affect the membrane potential
- Know the qualitative (high, low) concentrations of the 3 key ions inside and outside a typical cell
- Understand how the Nernst Potential would change if concentrations changed
- Explain how membrane selectivity affects the Nernst potential
- Explain why the equilibrium potential is not typically zero
3) Determine the resting membrane potential of any cell
- Appropriately apply the GHK (membrane potential equation) equation
- Understand how the membrane potential would change if
permeabilities
/
conductances
changed
- Calculate currents (I
x
) for the common ions
- Calculate the driving voltage (
V
x
) for each ion
4) Explain what an action potential is and how and why it occurs
- Diagram an action potential as a function of voltage over time and indicate the resting potential, depolarization, repolarization, hyperpolarization, overshoot, undershoot, absolute refractory phase and relative refractory phase
- Explain and numerically model the all-or none property of action potentials
5) Use the Hodgkin-Huxley model to recreate the action potential
- Explain the gating of Na+ and K+ channels and how that affects conductance over time
- Model how the conductance of gates and their time constants affect the action potential shape
- Explain the difference between membrane changes during an action potential and during an experiment where the membrane potential is voltage-clamped
3

## Slide 4
Part I:
Cell membranes; membrane biophysics; and chemical gradients
4

## Slide 5
Why do we care about cell membranes and excitable cells?
5

## Slide 6
How do we excite cells?
Light? Electricity?
Do humans have any optically excitable cells?
Why might optically excitable cells be useful in medicine/bioengineering?
Optogenetics
are being used to study neurons, to create optically controlled prosthetics, and to create cyborg robots…
https://www.youtube.com/watch?time_continue=85&v=-D_XrRo0h20
6

## Slide 7
Why do we care about cell membranes and excitable cells?
Each cell acts as a tiny battery with the positive pole outside the plasma membrane and the negative pole inside.
The magnitude of this difference in charge, or
potential difference
,
is measured in
voltage
.
Although the voltage of this battery is very small (less than a tenth of a volt), it
is of critical importance
in such physiological processes as
muscle contraction, the regulation of the heartbeat, and the generation of nerve impulses
.
To understand these processes, we must first examine the electrical properties of cells.
K
+
K
+
K
+
K
+
+
–
–
7

## Slide 8
Two driving forces at play
Diffusion
Electrostatic
Equilibrium is the balance of these two fluxes
8
Why are cells electrically charged?

## Slide 9
What happens if we have a large amount of solute on one side of a permeable membrane?
Random motion of molecules leads to diffusion
Net movement is from region of high to low concentration
Higher
concentration
Lower
concentration
Net diffusion
Equal concentrations
No net diffusion
9

## Slide 10
More concentrated
More dilute
Solute
Water
What happens if we have a large amount of solute on one side of an
impermeable
membrane?
*Note that in cells the membrane is a lipid bilayer and it has a variety of channels and pores through which different molecules passively or actively move from one side to the other.
10

## Slide 11
Worksheet exercise #1 – ions and membranes.
11
inside
outside

## Slide 12
Worksheet exercise #1 – ions and membranes.
12
inside
outside

## Slide 13
Worksheet exercise #1 – ions and membranes.
13
inside
outside

## Slide 14
Many molecules in cells and tissues move by diffusion
Some molecules, such as O
2
and CO
2
, can freely diffuse in and out of cells
Other molecules cannot freely diffuse in and out of cells
which is why the concentration of ions, proteins, nucleic acids, etc. . . can be different inside and outside of cells
How can we understand this?

## Slide 15
Cells are surrounded by a membrane
Outside
Inside
Plasma membrane
The plasma membrane acts as a barrier and separates the inside and outside of the cell
basically a thin sheet of oil

## Slide 16
from Physical Biology of the Cell, Phillips, et al
Subcellular organelles
are also surrounded
by membranes
Mitochondria, the nucleolus, lysosomes, peroxisomes, vesicles, the endoplasmic reticulum, etc. . .
Membranes acts as barriers and separate the inside of organelles and the rest of the cell

## Slide 17
Cells are surrounded by a membrane
Outside
Inside
Plasma membrane
The plasma membrane acts as a barrier and separates the inside and outside of the cell
What determines how easily molecules directly
diffuse through the membrane?
basically a thin sheet of oil
Model by diffusion through a thin sheet of oil. . .

## Slide 18
Diffusion through a sheet of oil
as a model for a cell membrane
Outside
Inside
Membrane
oil
water
Some molecules are
more soluble in oil
Some molecules are
more soluble in water
At equilibrium
Partition Coefficient

## Slide 19
Permeability
From our simple model
Charged molecules and polar molecules strongly prefer water
Nonpolar, oily molecules prefer oil
Permeability depends linearly on
More oil soluble molecules can pass through membranes
Membranes are impermeable to most
charged and polar molecules
Strong implications for drug delivery

## Slide 20
20
Quick dimensional analysis check
What are the units of permeability (P)?
How does this affect molar flux (J)?

## Slide 21
Diffusion through a sheet of oil
as a model for a cell membrane
Outside
Inside
Membrane
What is the flux of molecules through the membrane at steady-state?
Fick’s law
permeability
with

## Slide 22
What are the units of flux?
Fick’s law
permeability
with
The greater the permeability, the greater the flux
Permeability is a measure of how easily something
crosses the membrane.

## Slide 23
Transport of charged molecules
K
+
Cl
–
Intracellular fluid
concentrations
Extracellular fluid
concentrations
145
mM
5
mM
125
mM
2.5
mM
0.0001 mM
9
mM
150
mM
12
mM
Na
+
Ca
2+
Many molecules of interest are charged, which strongly impacts their movement
Ions are
nonuniformly
distributed
The movement of ions play many important roles in cell physiology and signaling:
Muscle contraction, heart beat, nerve impulses, fertilization, apoptosis, gene expression, etc. . .
Ions can pass through
the membrane by moving through specialized channels
Ions Channels
Different channels are specialized for different ions

## Slide 24
Different types of membrane transport
Direct diffusion through the membrane
Diffusion through a channel in the membrane
Uses energy from ATP hydrolysis to drive molecules across the membrane
Simultaneously moves different molecules in opposite directions
Molecules always move down
concentration gradients
Can move molecules up
concentration gradients

## Slide 25
Part II:
Nernst potential, membrane potential, driving voltages
25

## Slide 26
Permeability (P) refers to how easily a substance can cross through the membrane. Units are in cm/sec.
Conductance (g) refers to ions and how easily they flow through the membrane. Conductance is also defined as the degree to which the membrane conducts electricity (or ions). Units are in
siemens
.
Resistance (R) is the inverse of conductance. Units are in ohms.
Voltage (V), or voltage potential is the difference in charge across some barrier, and in our case the barrier is the cell membrane.
Current (I) is the flow of ions.
Recall
V = I*R
or
I = V*g
26
(For reference) Permeability, conductance, voltage, current

## Slide 27
Be sure to check out the membrane potential tutorial:
https://www.st-andrews.ac.uk/~wjh/neurotut/mempot.html
27

## Slide 28
Where do transmembrane electrical potentials (voltages) come from?
Let’s consider a very simple model of a cell membrane…
28

## Slide 29
-
The Nernst equilibrium potential
The
Nernst potential
(
equilibrium potential
) is the intracellular electrical voltage that would produce a current that would be equal in magnitude but opposite in direction to that produced by the process of diffusion.
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+
When will the negatively charged molecules stop entering the cell?
-
29

## Slide 30
+
+
+
+
+
+
–
Plasma membrane
Fixed anions
What are these fixed anions?
What happens within a cell?
What ion is most prevalent inside the cell?
Where do the positive ions want to go?
30

## Slide 31
+
+
+
+
+
+
+
+
+
+
+
+
–
Plasma membrane
Concentration gradient
Fixed anions
What happens within a cell?
Where do the positive ions want to go?
Electrical attraction
Two driving forces set up the electrochemical potential.
31

## Slide 32
K
+
K
+
–90 mV
Voltmeter
Intracellular
electrode
Charge
attraction
Diffusion
Fixed anions
K
+
K
+
K
+
K
+
K
+
Extracellular
electrode
+
–
–
(electrical flux)
(chemical flux)
What is the equilibrium potential for K+?
32
The K
+
equilibrium potential (E
K
) is the electrical potential that counters the diffusion of K
+

## Slide 33
At equilibrium, electrically-driven and
diffusion-driven flows cancel one another
E
X
= Nernst voltage for species x
R = the gas constant [ 8.314 J / (mol K) ]
T = absolute temperature [K]
F = Faraday
’
s constant [ 9.64 x10
4
J / (V
mol
) ] or [C/
mol
]
z
X
= valence (charge) of the ionic species x
C
oX
,
C
iX
= outer & inner concentrations of species x
zFE
X
=       ln
RT
C
oX
C
iX
Electromotive Free Energy
=
Chemical Free Energy
E
X
=         ln
C
oX
C
iX
RT
zF
Solving for E
X
yields
the
Nernst equation
:
The Potassium Nernst potential (E
K
) is the  K
+
equilibrium potential that counters the diffusion of K
+

## Slide 34
(For reference only) Modeling diffusion of ions through an ion channel
For a single ion, when the membrane potential is
electrostatic forces and diffusion balance so there is no net flux
This charge potential is called the Nernst potential, or the equilibrium potential, and it is different for different ions
The Nernst potential for ion
with charge
, inner concentration
, and outer concentration
Often written in “molar” units
is the gas constant [ 8.314 J / (mol K) ]
is absolute temperature [K]
is Faraday
’
s constant [ 9.64 x10
4
J / (V
mol
) ] or [C/
mol
]
is valence (charge) of the ionic species x
is Boltzmann’s constant

## Slide 35
Example for reference: The Nernst potential for potassium
is the gas constant [ 8.314 J / (mol K) ]
is absolute temperature [K]
is Faraday
’
s constant [ 9.64 x10
4
J / (V
mol
) ] or [C/
mol
]
is valence (charge) of the ionic species x
For potassium
If this was the membrane potential then potassium ions would exhibit no net flux
Changing membrane potential requires moving very, very few ions across the membrane channels.
Therefore, the movement of ions can result in changes to membrane potential without appreciably changing ion concentrations.
So, if potassium was the only ion that could pass across the membrane, then the membrane potential would become

## Slide 36
The Potassium Nernst Potential
Example (K
+
):
C
o
= 4
mM
and C
i
= 140
mM
E
K
= -(61/1) log(140/4)
E
K
= -61mV * log(35)
E
K
= -94 mV
E
K
=
-
(61) log
10
C
iX
C
oX
So, if the membrane were permeable only to K+,
V
mem
would be -94 mV
…also called the equilibrium potential
E
X
=  -        ln
C
iX
C
oX
RT
z
X
F
36

## Slide 37
E
x
=
-
(61) log
10
C
iX
C
oX
E
X
=  -        ln
C
iX
C
oX
RT
z
X
F
How do I switch from one form to the other?
E
X
=         ln
C
oX
C
iX
RT
zF
First, changing the numerator and denominator just switches the sign to negative. This
z
x

## Slide 38
E
X
=  -        ln
C
iX
C
oX
RT
z
X
F
How do I switch from one form to the other?
Recall ln(x) = ln(10)*log
10
(x) =~2.3*log
10
(x)
We will use ln to indicate the natural log. We will use log and log
10
interchangeably in discussion and equations, BUT
MATLAB uses “log” to calculate the natural log and “log10” to calculate the log base ten. MATLAB does not recognize “ln”.

## Slide 39
E
X
=  -        ln
C
iX
C
oX
RT
z
X
F
How do I switch from one form to the other?
R = the gas constant [ 8.314 J / (mol K) ]
T = absolute temperature [K]; assume body temp in constant = 310 K
F = Faraday
’
s constant [ 9.64 x10
4
J / (V mol) ] or [C/mol]
z
X
= valence (charge) of the ionic species x
-2.3       log
10
C
iX
C
oX
RT
z
X
F
Plug in constants.
E
x
=
-
(61) log
10
C
iX
C
oX
z
x

## Slide 40
1) Which way does diffusion push K+?
2) Which way does the electrical flux push K+?
3) What is the Nernst potential for K+?
Worksheet exercise #2 – Nernst equilibrium potentials
K
+
Cl
–
Intracellular fluid
concentrations
Extracellular fluid
concentrations
145
mM
5
mM
125
mM
2.5
mM
0.0001 mM
9
mM
150
mM
12
mM
Na
+
Ca
2+
