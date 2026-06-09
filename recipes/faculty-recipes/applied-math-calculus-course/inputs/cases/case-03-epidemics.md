# Case 03: The Mathematics of Epidemics — Modeling the Spread of Infectious Disease

**Course:** Applied Mathematics 50
**Topic block:** Weeks 5–6
**Fields:** Epidemiology, public health, differential equations, probability

---

## Overview

How fast will a new disease spread? When will an epidemic peak? Will vaccination eliminate an infection entirely? These are not merely biological questions — they are mathematical ones. This case develops the **SIR model** of infectious disease, the foundational framework of mathematical epidemiology. Students derive the model from first principles, analyze it qualitatively and quantitatively, fit it to real outbreak data, and explore how interventions (vaccination, social distancing) alter the trajectory of an epidemic.

---

## The Central Problem

At the start of an outbreak, a small number of infected individuals enter a susceptible population. Each infected person contacts others, transmitting the disease at some rate; eventually infected individuals recover and become immune. The central question: will the infection spread widely (an epidemic) or die out quickly? The answer depends on a single number — **R₀**, the basic reproduction number.

---

## Mathematical Content

### The SIR Model

Divide the population N into three compartments:
- **S(t):** susceptible (not yet infected, not immune)
- **I(t):** infectious (currently infected and able to transmit)
- **R(t):** recovered/removed (immune or deceased)

With S + I + R = N (constant), the model is:

$$\frac{dS}{dt} = -\beta S I$$

$$\frac{dI}{dt} = \beta S I - \gamma I$$

$$\frac{dR}{dt} = \gamma I$$

**Parameters:**
- β = transmission rate (contacts per day × probability of transmission per contact)
- γ = recovery rate (1/γ = average infectious period in days)

This is a system of nonlinear first-order ODEs. It cannot be solved in closed form, but yields rich qualitative and quantitative analysis.

### The Basic Reproduction Number R₀

Define R₀ = βN/γ. This is the average number of secondary infections caused by one infectious individual in a fully susceptible population.

**Epidemic threshold theorem:**
- If R₀ > 1: the infection spreads (dI/dt > 0 initially), causing an epidemic.
- If R₀ ≤ 1: the infection dies out (dI/dt ≤ 0), no epidemic.

**Proof:** At t = 0, S(0) ≈ N, so dI/dt ≈ I(βN − γ) = γI(R₀ − 1). The sign of dI/dt is determined by R₀ − 1.

### Qualitative Analysis

**Phase plane analysis.** Plot S on the horizontal axis and I on the vertical axis. The system's trajectories satisfy:

$$\frac{dI}{dS} = \frac{\beta SI - \gamma I}{-\beta SI} = -1 + \frac{\gamma}{\beta S} = -1 + \frac{1}{R_0} \cdot \frac{N}{S}$$

Integrating: I = −S + (N/R₀) ln S + C.

This gives the **epidemic curve** in phase space. The epidemic peaks when S = N/R₀ (i.e., when dI/dt = 0), and the final epidemic size S(∞) satisfies the transcendental equation:

$$S(\infty) = N e^{-R_0 (1 - S(\infty)/N)}$$

### Herd Immunity

If a fraction p of the population is vaccinated (and thus moved to R at t = 0), the effective reproduction number becomes R_eff = R₀(1 − p). The epidemic cannot spread if R_eff ≤ 1, i.e., if:

$$p \geq 1 - \frac{1}{R_0}$$

This is the **herd immunity threshold**. For measles (R₀ ≈ 15), p ≥ 93%. For seasonal flu (R₀ ≈ 1.3), p ≥ 23%.

### Connection to Course Material

- **Separable ODEs** (Unit 5.2): the R equation dR/dt = γI can be integrated once I(t) is known.
- **Linear approximation** (Unit 5.3): near the disease-free equilibrium, the linearized system gives exponential growth I(t) ≈ I₀ e^(γ(R₀−1)t).
- **Exponential and logistic growth** (Unit 5.2): early epidemic growth is approximately exponential; the full SIR trajectory resembles logistic growth followed by decline.
- **Taylor series** (Unit 4): the final size equation S(∞) = N e^(−R₀(1−S(∞)/N)) can be approximated by Newton's method, which uses Taylor expansion.

---

## Classic Paper

**Kermack, W. O., and A. G. McKendrick.** "A contribution to the mathematical theory of epidemics." *Proceedings of the Royal Society A* 115(772) (1927): 700–721.

This is the paper that introduced the SIR model. Written in 1927, it derives the threshold theorem and final epidemic size formula. The mathematics is accessible after Math 1b; the physical reasoning is elegant. Students should read Sections 1–4.

---

## Modeling Exercise

**Fitting the SIR model to the 1918 influenza pandemic.**

The table below gives weekly influenza deaths in London, fall 1918 (approximate):

| Week | Deaths |
|------|--------|
| 1 | 300 |
| 2 | 800 |
| 3 | 2400 |
| 4 | 5100 |
| 5 | 6200 |
| 6 | 4900 |
| 7 | 2300 |
| 8 | 800 |

1. Assume deaths are proportional to I(t). Use the ratio of consecutive death counts to estimate the initial exponential growth rate r = γ(R₀ − 1).
2. Assume γ = 1/5 (5-day infectious period). Estimate R₀.
3. Numerically solve the SIR model using Euler's method with your estimated parameters. Plot S(t), I(t), R(t).
4. What fraction of the population was infected? Compare to the final-size formula.
5. What vaccination coverage would have been needed to prevent the epidemic?

*(Python starter code provided separately.)*

---

## Discussion Questions

1. The SIR model assumes a homogeneous, well-mixed population. Real epidemics spread on social networks. How would you modify the model to account for network structure, and what new parameters would you need?

2. During the COVID-19 pandemic, governments imposed social distancing policies that effectively reduced β. How does a temporary reduction in β affect the final epidemic size? Does "flattening the curve" reduce total infections, or only spread them out over time?

3. Some diseases (influenza, COVID-19) mutate rapidly, so that recovered individuals may be reinfected. How would you modify the SIR model to capture this, and how does it change the epidemic threshold analysis?

4. R₀ is often described in news coverage as the key number determining whether an epidemic grows. Is this a fair summary? What does R₀ *not* capture?

---

## Further Reading

- Anderson, Roy M., and Robert M. May. *Infectious Diseases of Humans: Dynamics and Control.* Oxford University Press, 1991. — the standard advanced reference
- Strogatz, Steven H. *Nonlinear Dynamics and Chaos.* Westview Press, 2015. Ch. 6. — SIR model as an example of phase-plane analysis
- Martcheva, Maia. *An Introduction to Mathematical Epidemiology.* Springer, 2015.
- Biggerstaff, Matthew, et al. "Estimates of the reproduction number for seasonal, pandemic, and zoonotic influenza: a systematic review of the literature." *BMC Infectious Diseases* 14 (2014): 480.
