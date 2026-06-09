# Homework 3: The Mathematics of Epidemics

**Course:** Applied Mathematics 50
**Topic block:** Weeks 5–6 (Case 03)
**Due:** End of Week 6
**Instructions:** Show all mathematical steps. For proofs, clearly state each assumption. Diagrams are encouraged where they clarify reasoning.

---

## Problem 1 — Deriving the Epidemic Threshold (25 points)

The SIR model is:

$$\frac{dS}{dt} = -\frac{\beta SI}{N}, \qquad \frac{dI}{dt} = \frac{\beta SI}{N} - \gamma I, \qquad \frac{dR}{dt} = \gamma I$$

with S(0) = S₀ ≈ N, I(0) = I₀ > 0 small, R(0) = 0.

**(a)** Define R₀ = βN/γ. Show directly from the equation for dI/dt that:
$$\frac{dI}{dt} = \gamma I\!\left(\frac{S}{N/R_0} - 1\right)$$
and conclude that dI/dt > 0 (epidemic spreads) if and only if S > N/R₀.

**(b)** At t = 0, we have S ≈ N. Using part (a), prove the **epidemic threshold theorem**: an epidemic (initial growth in I) occurs if and only if R₀ > 1.

**(c)** The epidemic peaks when dI/dt = 0. Using part (a), find the value of S at the epidemic peak. Express your answer in terms of R₀ and N.

**(d)** As t → ∞, I(t) → 0 (the epidemic ends). Show that S(∞) > 0, meaning not everyone gets infected. (Hint: use the fact that S is strictly decreasing throughout the epidemic; argue that S cannot reach 0 in finite time.)

**(e)** **Final epidemic size.** From the SIR equations, derive:
$$\frac{dI}{dS} = -1 + \frac{N}{R_0 S}$$
(by dividing dI/dt by dS/dt). Integrate this equation with initial condition I = I₀ when S = S₀ ≈ N, and use I(∞) ≈ 0 to derive the **final size equation**:
$$S(\infty) = N \exp\!\left(-R_0\,\frac{N - S(\infty)}{N}\right)$$
(You may set I₀ ≈ 0 and S₀ ≈ N for simplicity.)

---

## Problem 2 — Analyzing the Final Size Equation (20 points)

The final size equation from Problem 1(e) is a **transcendental equation** — it cannot be solved in closed form, but we can analyze it.

Let u = S(∞)/N ∈ (0, 1) be the fraction of the population that escapes infection. The equation becomes:

$$u = e^{-R_0(1-u)}$$

or equivalently, define g(u) = u − e^{−R₀(1−u)}.

**(a)** Show that g(0) < 0 and g(1) = 0 for any R₀ > 0. This confirms u = 1 (no epidemic) is always a solution. Find the derivative g′(u) and show that for R₀ > 1, there is a second root u* ∈ (0, 1).

**(b)** Use Newton's method with initial guess u₀ = 0.5 to find u* for R₀ = 2.0 and R₀ = 5.0. Perform exactly two Newton iterations for each and report your estimates. (Newton's method: u_{n+1} = u_n − g(u_n)/g′(u_n).)

**(c)** Let f_infected = 1 − u* be the fraction of the population ultimately infected. Fill in the following table (use Newton's method from part (b), or any other algebraic method):

| R₀ | u* (escapes infection) | f_infected |
|----|------------------------|------------|
| 1.5 | | |
| 2.0 | | |
| 3.0 | | |
| 5.0 | | |
| 10.0 | | |

**(d)** For R₀ close to 1 (R₀ = 1 + ε, small ε > 0), use a Taylor expansion of e^{−R₀(1−u)} around u = 1 to show that f_infected ≈ 2ε/R₀² ≈ 2(R₀ − 1) for R₀ near 1. This says the epidemic size grows linearly above the threshold — confirm with your table.

---

## Problem 3 — Herd Immunity and Vaccination Strategy (25 points)

**(a)** Suppose a fraction p of the population is vaccinated before the epidemic begins, moving directly to the R compartment. The initial susceptible fraction is 1 − p. Show that the epidemic cannot spread if:
$$p \geq 1 - \frac{1}{R_0}$$
This is the **herd immunity threshold**. (Hint: apply the epidemic threshold theorem to the modified initial condition S(0) = N(1 − p).)

**(b)** Compute the herd immunity threshold for the following diseases:

| Disease | R₀ | Herd immunity threshold p* |
|---------|-----|---------------------------|
| Measles | 12–18 (use 15) | |
| Polio | 5–7 (use 6) | |
| COVID-19 (original strain) | 2.5–3.5 (use 3) | |
| Seasonal flu | 1.2–1.4 (use 1.3) | |
| Ebola | 1.5–2.5 (use 2) | |

**(c)** Vaccines are not perfectly effective. Suppose vaccine efficacy is e ∈ (0, 1): a vaccinated individual remains susceptible with probability 1 − e. If a fraction p of the population is vaccinated with efficacy e, show that the effective reproduction number is:
$$R_{\text{eff}} = R_0\,[1 - ep]$$
and find the vaccination coverage p* needed to achieve herd immunity in terms of R₀ and e.

**(d)** During the COVID-19 pandemic, mRNA vaccines had approximately 95% efficacy against transmission (e = 0.95) and R₀ ≈ 3. What vaccination coverage is required for herd immunity? How does this compare to the perfect-vaccine case from part (b)? If vaccine hesitancy limits coverage to p = 0.70, can herd immunity be achieved?

**(e)** A disease has R₀ = 4 and no vaccine exists. A public health intervention (social distancing, masks) reduces the contact rate β by 40%. Compute the effective R₀ under the intervention and determine whether it is sufficient to prevent an epidemic. If R₀ must be reduced below 1, by what percentage must β be reduced?

---

## Problem 4 — Reading Response: Kermack and McKendrick (1927) (30 points)

Read Sections 1–4 of Kermack and McKendrick (1927) (provided on the course website). Then answer:

**(a)** Kermack and McKendrick write their equations in a slightly different form than the modern SIR model. In their notation, they write:

$$\frac{dx}{dt} = -\kappa xy, \qquad \frac{dy}{dt} = \kappa xy - \ell y, \qquad \frac{dz}{dt} = \ell y$$

Identify their variables x, y, z and parameters κ, ℓ with the modern notation S, I, R, β/N, γ. (Be precise about whether κ = β or κ = β/N.)

**(b)** In their paper, Kermack and McKendrick derive an approximate solution to the epidemic equations using a sequence of simplifications. Identify the key approximation they make (around equation 13 in the original), and explain what mathematical technique this corresponds to in modern terms. Is the approximation valid at the start, peak, or end of the epidemic?

**(c)** The paper was published in 1927. Kermack and McKendrick apply their model to mortality data from the Bombay plague epidemic of 1905–1906. Does their model fit the data well? What feature of the epidemic curve does their model capture most accurately, and what does it miss?

**(d)** The Kermack-McKendrick threshold theorem (ρ > 1 for an epidemic to occur, in their notation) is arguably the single most important result in mathematical epidemiology. Yet the paper received little attention for 30 years after publication. Based on your reading, give two reasons why a practicing public health official in 1927 might have been skeptical of the model. Are those same objections valid today?
