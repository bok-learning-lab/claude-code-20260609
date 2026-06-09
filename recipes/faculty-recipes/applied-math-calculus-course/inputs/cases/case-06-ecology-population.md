# Case 06: Predators, Prey, and Equilibrium — Mathematics of Ecological Systems

**Course:** Applied Mathematics 50
**Topic block:** Weeks 11–12
**Fields:** Ecology, biology, dynamical systems, differential equations

---

## Overview

Why do animal populations cycle? Why do some ecosystems collapse suddenly while others recover from disturbance? Mathematical ecology provides precise answers using dynamical systems — systems of ODEs whose solutions describe how populations change over time. This case studies the **Lotka-Volterra predator-prey model**, one of the earliest and most famous models in mathematical biology, alongside more realistic models that incorporate carrying capacity, time delays, and harvesting. Students analyze the models qualitatively, solve special cases explicitly, and connect the mathematics to real ecological data.

---

## The Central Problem

In the 1920s, Italian mathematician Vito Volterra was asked by his son-in-law, biologist Umberto D'Ancona, to explain a puzzling observation: during World War I, when fishing in the Adriatic Sea nearly stopped, the proportion of predatory fish (sharks, rays) in the catch *increased* — even though both predator and prey populations had presumably grown without fishing pressure. Volterra's mathematical model not only explained this anomaly but founded the field of mathematical ecology.

---

## Mathematical Content

### The Lotka-Volterra Equations

Let x(t) = prey population (e.g., fish) and y(t) = predator population (e.g., sharks). The Lotka-Volterra model is:

$$\frac{dx}{dt} = \alpha x - \beta xy$$

$$\frac{dy}{dt} = \delta xy - \gamma y$$

**Parameters:**
- α = prey growth rate (birth rate in absence of predators)
- β = predation rate (rate at which predators kill prey)
- δ = conversion efficiency (prey consumed → predator births)
- γ = predator death rate (in absence of prey)

All parameters are positive.

### Equilibrium Analysis

The system has two equilibria:

1. **Trivial equilibrium:** (x*, y*) = (0, 0) — both populations extinct
2. **Coexistence equilibrium:** (x*, y*) = (γ/δ, α/β)

**Linearization near the coexistence equilibrium.** Let x = x* + u, y = y* + v with u, v small. Substituting and ignoring quadratic terms:

$$\frac{du}{dt} = -\beta x^* v = -\frac{\beta\gamma}{\delta} v$$

$$\frac{dv}{dt} = \delta y^* u = \alpha u$$

This linear system has the matrix A = [[0, −βγ/δ], [α, 0]], with characteristic equation λ² + αγ = 0, giving eigenvalues λ = ±i√(αγ).

**Pure imaginary eigenvalues** → the linearization predicts **centers** (neutrally stable oscillations). The prey and predator populations cycle with angular frequency ω = √(αγ) and period T = 2π/√(αγ).

### Conservation Law

The full nonlinear system has a conserved quantity — an integral of the equations of motion:

$$H(x, y) = \delta x - \gamma \ln x + \beta y - \alpha \ln y = \text{constant}$$

This can be verified by computing dH/dt = 0 along solutions. The level curves of H are closed curves in the (x, y) plane — every trajectory is periodic. This is directly analogous to conservation of energy in mechanics.

### Volterra's Principle

When fishing removes a constant fraction h of both predator and prey populations, the modified equations are:

$$\frac{dx}{dt} = (\alpha - h)x - \beta xy, \qquad \frac{dy}{dt} = \delta xy - (\gamma + h)y$$

The new coexistence equilibrium is (x*, y*) = ((γ+h)/δ, (α−h)/β).

**Volterra's principle:** Harvesting *increases* the prey equilibrium (x* goes up) and *decreases* the predator equilibrium (y* goes down). Conversely, stopping fishing (h → 0) shifts the equilibrium in favor of predators.

This explains D'Ancona's observation: during WWI, fishing effectively stopped (h ≈ 0), which should have increased predator proportions — exactly what was observed.

### The Logistic Predator-Prey Model

Pure Lotka-Volterra prey growth is exponential in the absence of predators, which is unrealistic. A more realistic model incorporates a carrying capacity K for the prey:

$$\frac{dx}{dt} = rx\!\left(1 - \frac{x}{K}\right) - \beta xy$$

$$\frac{dy}{dt} = \delta xy - \gamma y$$

This system can exhibit more complex behavior, including stable spirals (oscillations that damp to the equilibrium), limit cycles, and — for some parameter values — chaos.

### Connection to Course Material

- **Separable ODEs** (Unit 5.2): the prey equation with y = 0 is logistic growth (dx/dt = rx(1 − x/K)), solved by partial fractions.
- **Linear systems** (Unit 5.4): linearization near the equilibrium gives a 2×2 linear ODE system; eigenvalues determine stability.
- **Taylor series** (Unit 4): linearization *is* a first-order Taylor expansion of the nonlinear equations around the equilibrium.
- **Improper integrals and probability** (Units 1.5, 2.4): population distributions over space lead to integral equations.

---

## Classic Paper

**Lotka, Alfred J.** "Fluctuations in the numbers of animals: a mathematical discussion." *Proceedings of the National Academy of Sciences* 6 (1920): 410–415.

This is Lotka's original paper (independent of Volterra). It is short, clearly written, and derives the oscillation period formula T = 2π/√(αγ). Students can verify Lotka's calculation directly using the linearization above.

**Supplementary:** Volterra, Vito. "Fluctuations in the abundance of a species considered mathematically." *Nature* 118 (1926): 558–560. — Volterra's paper explaining D'Ancona's fishing data.

---

## Modeling Exercise

**Lynx and snowshoe hare.**

The Hudson's Bay Company recorded annual fur trade data from 1845–1935, showing regular oscillations in lynx and hare populations with a period of approximately 10 years. The data below are approximate population sizes (in thousands):

| Year | Hare | Lynx |
|------|------|------|
| 1845 | 20 | 30 |
| 1850 | 100 | 4 |
| 1855 | 8 | 45 |
| 1860 | 80 | 6 |
| 1865 | 10 | 70 |

1. From the observed period T ≈ 10 years, use T = 2π/√(αγ) to obtain a constraint on the parameters α and γ. Assume α ≈ 0.4 yr⁻¹ (hare doubling time ≈ 2 years in absence of lynx). Solve for γ.

2. Using the coexistence equilibrium values x* = 30 (thousand hares) and y* = 4 (thousand lynx), determine β and δ.

3. Numerically integrate the Lotka-Volterra equations using Euler's method with your estimated parameters. Compare the simulated trajectories to the data table.

4. How does adding a carrying capacity K = 150 thousand for the hare change the trajectories? Does the system still oscillate? Try K = 50 and K = 300.

*(Python starter code provided separately.)*

---

## Discussion Questions

1. The Lotka-Volterra model predicts that predator-prey oscillations are *neutrally stable* — the amplitude of oscillations depends on initial conditions and is preserved forever. Real ecosystems show damped oscillations that converge to equilibrium. What biological mechanism could cause damping, and how would you incorporate it into the model?

2. Volterra's principle says that fishing benefits predators. But in the real world, overfishing frequently leads to predator collapse. What assumption of the model fails in the overfishing scenario?

3. Some ecosystems show "trophic cascades" where removing a top predator causes unexpected downstream effects — for example, the reintroduction of wolves to Yellowstone altered river courses. Can the Lotka-Volterra framework explain trophic cascades? What extension would be needed?

4. The Hudson's Bay lynx-hare data are beautiful and famous — but some ecologists argue they reflect the economics of the fur trade as much as actual population dynamics. What does this say about using empirical data to validate mathematical models?

---

## Further Reading

- Murray, J. D. *Mathematical Biology I: An Introduction.* 3rd ed. Springer, 2002. Ch. 3. — the standard graduate reference
- Strogatz, Steven H. *Nonlinear Dynamics and Chaos.* Westview Press, 2015. Ch. 5–6. — beautiful qualitative treatment with phase-plane methods
- Elton, Charles. *Animal Ecology.* University of Chicago Press, 1927. — the classic observational text on animal population cycles
- Turchin, Peter. *Complex Population Dynamics.* Princeton University Press, 2003. — modern empirical and theoretical treatment
