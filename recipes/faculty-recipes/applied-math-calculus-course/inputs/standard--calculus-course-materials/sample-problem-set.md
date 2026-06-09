# Math 1b — Sample Problem Set: Integration Techniques and Series

**Instructions:** Show all work. Answers without justification receive no credit. You may use a calculator to check numerical answers but must present an analytic solution.

---

## Part A: Integration Techniques

**1.** Evaluate the following integrals.

(a) ∫ x² eˣ dx

(b) ∫ sin³(x) cos²(x) dx

(c) ∫ dx / (x² − 5x + 6)

(d) ∫₀^∞ x e^(−x) dx

(e) ∫ √(9 − x²) dx  *(use trigonometric substitution)*

---

**2.** A biologist models the concentration C(t) of a drug in the bloodstream by the integral

$$C(t) = \int_0^t s\, e^{-ks}\, ds$$

where k > 0 is a clearance constant.

(a) Evaluate C(t) using integration by parts.

(b) Find lim_{t→∞} C(t) and interpret your answer in context.

(c) At what time t* is C(t) maximized? Does your answer depend on k?

---

**3.** Determine whether each improper integral converges or diverges. If it converges, find its value.

(a) ∫₁^∞ 1/x^(3/2) dx

(b) ∫₀^1 ln(x) dx

(c) ∫₋∞^∞ 1/(1 + x²) dx

---

## Part B: Sequences and Series

**4.** For each sequence, determine whether it converges or diverges. If it converges, find the limit.

(a) aₙ = (3n² + 2n) / (5n² − 1)

(b) aₙ = n^(1/n)

(c) aₙ = (−1)ⁿ · n / (n + 1)

---

**5.** Determine whether each series converges or diverges. State clearly which test you use and verify its hypotheses.

(a) Σ_{n=1}^∞ 1 / (n² + 4)

(b) Σ_{n=1}^∞ n / 3ⁿ

(c) Σ_{n=1}^∞ (−1)ⁿ / √n

(d) Σ_{n=1}^∞ n! / nⁿ

---

**6.** Find the interval of convergence (including endpoints) of the power series

$$\sum_{n=1}^{\infty} \frac{(x-2)^n}{n \cdot 4^n}$$

---

**7.** (Taylor series)

(a) Write the Maclaurin series for f(x) = e^(−x²) and give the interval of convergence.

(b) Use this series to express ∫₀^1 e^(−x²) dx as an infinite series. Then estimate the integral to within 0.001 by finding how many terms are needed.

(c) Compute lim_{x→0} (e^(−x²) − 1 + x²) / x⁴ using series (without L'Hôpital's rule).

---

## Part C: Application and Modeling

**8.** A population of bacteria grows according to the logistic model

$$\frac{dP}{dt} = 0.4P\!\left(1 - \frac{P}{1000}\right), \quad P(0) = 100.$$

(a) Solve this separable ODE for P(t).

(b) Find lim_{t→∞} P(t) and interpret the result biologically.

(c) At what time does the population reach half its carrying capacity? At what time is growth fastest?

---

**9.** *(Challenge)* Prove that the series Σ_{n=1}^∞ 1/n diverges using the integral test, and then use the Alternating Series Test to prove that Σ_{n=1}^∞ (−1)^(n+1)/n converges. Reconcile these two results: what does this say about absolute vs. conditional convergence?
