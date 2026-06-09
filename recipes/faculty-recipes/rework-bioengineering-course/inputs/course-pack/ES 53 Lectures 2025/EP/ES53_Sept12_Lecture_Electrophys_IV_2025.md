# ES53_Sept12_Lecture_Electrophys_IV_2025.pptx — text digest
_Extracted text from 21 slides. Images, layout, and formatting omitted._

## Slide 1
Module 1
Electrophysiology
(Sept. 12, 2025)
ES 53
2025
1

## Slide 2
Part IV:
Hodgkin – Huxley and Modeling the Action Potential
2

## Slide 3
Be sure to read the handout on “Modeling of the Action Potential”
3

## Slide 4
4

## Slide 5
Na
+
channels can enter an inactive state
Na
+
channels can be modeled as having two gates: an activation gate and an inactivation gate
K
+
channels only have an activation gate, which is slow
The activation gate is FAST. The inactivation gate is SLOW.

## Slide 6
The absolute refractory period is caused by inactivation of Na
+
channels
And can be mathematically modeled by the “h” gate

## Slide 7
Transient increase in Na
+
conductance
Changes in membrane
conductances
are caused
by ion channels opening and closing
Ion channels can be open or closed
Ions can only pass through open ion channels
Transient increase in the number of open Na
+
ion channels
the number of Na
+
ion channels
the probability that a Na
+
ion channel is open
the conductance of an open Na
+
ion channels
with

## Slide 8
Predicted change in
conductances
during an action potential: Hodgkin-Huxley equations
“Leak”
A fudge factor
is assumed not to depend on voltage
capacitance
Too simple for action potentials. . .

## Slide 9
9
Specifically, the
potassium conductance
is modeled as four independent n-gates that can be
activated
. Potassium current is modeled by only n gates as:
Where n is the coefficient from 0 to 1. Note that n is taken to the fourth power because the kinetics are modeled as four of these gates.
The
sodium conductance
is also modeled as a set of four gates, but is instead modeled with
three activating
m-gates and
one inactivating
h-gate. Sodium current is modeled by n and h gates as:
Where m and h are the coefficients from 0 to 1. Note that m is cubed because the kinetics are modeled as three m gates and an inactivating h gate.
Hodgkin-Huxley Model

## Slide 10
Stimulation
Slow opening of K activation gates
Fast opening of Na activation gates
Slow closing of Na inactivation gates
Gate Probabilities
(
(
(
These m, n, and h gates each have different time constants (
τ
m
,
τ
n
,
τ
h
).
They also have initial (a.k.a. resting) values (m
0
, n
0
, h
0
) between 0 and 1 related to their probability of being open, and activation values (m
∞
, n
∞
, h
∞
) associated with their probability of being open at steady state (∞).
Hodgkin-Huxley Model

## Slide 11
conductance
open probability
activation gate
inactivation gate
Parameters depend on membrane potential
Na
+
activation gate
Na
+
inactivation gate
K
+
activation gate
Steady-state probability for the activation gate to be open is
low
at the resting membrane potential
Steady-state probability for the inactivation gate to be open is
high
at the resting membrane potential
Na
+
activation gate is FAST
Na
+
inactivation gate and K
+
activation
gates are SLOW

## Slide 12
conductance
open probability
Parameters depend on membrane potential
Na
+
activation gate
Na
+
inactivation gate
K
+
activation gate
Steady-state probability for the activation gate to be open is
low
at the resting membrane potential
Steady-state probability for the inactivation gate to be open is
high
at the resting membrane potential
Na
+
activation gate is FAST
Na
+
inactivation gate and K
+
activation
gates are SLOW
For a given steady state voltage, the probabilities of the gates being open are:
(
(
(

## Slide 13
13
(
(
(
Exercise 5: Modeling gates in the Hodgkin Huxley kinetic model
What do these equations look like if we plot them?
t
m
t
h
t
n
For
n,m,h
what happens as t

0? Or as t

∞?

## Slide 14
14
MATLAB demo
& Example Problems

## Slide 15
15
Exercise 6:
There have been several neurological disorders linked to mutations of voltage-gated sodium channels.
Below are the kinetic parameters associated with changing the membrane potential of a neuron from -65 to 23 mV.
Consider these cells with abnormal Na+ channels in the following scenarios and draw how this would change the Na+ conductance curve and the resulting action potential (if at all).

## Slide 16
16

## Slide 17
17

## Slide 18
18

## Slide 19
19
Exercise 7:
Some Mutations in KV1.1(KCNA1)2 are often associated with a condition called episodic ataxia (EA), which results from a reduction in K conductance.

## Slide 20
20

## Slide 21
21
-
100
100
0
2
4
6
8
10
0
Time (
ms
)
Vmem
(mV)
0
2
4
6
8
Time (
ms
)
0
10
20
30
40
Conductance (mS/cm2)
