# Homework 5: The Sound of Mathematics — Fourier Analysis

**Course:** Applied Mathematics 50
**Topic block:** Weeks 9–10 (Case 05)
**Due:** End of Week 10
**Instructions:** Integration by parts and trigonometric integral identities may be used freely; cite which identities you use. All Fourier coefficient computations must be done by hand.

---

## Problem 1 — Computing Fourier Coefficients (30 points)

For each function below, the period is T = 2π. Compute the Fourier coefficients a₀, aₙ, and bₙ for general n ≥ 1, and write the Fourier series.

**(a)** The **sawtooth wave:**
$$f(t) = \frac{t}{\pi} \quad \text{for } -\pi < t \leq \pi$$

- Show that aₙ = 0 for all n ≥ 0.
- Show that bₙ = (−1)^{n+1} · (2/n) for all n ≥ 1.
- Write the first four nonzero terms of the Fourier series explicitly.

**(b)** The **triangular wave:**
$$f(t) = |t| \quad \text{for } -\pi \leq t \leq \pi$$

- Show that bₙ = 0 for all n ≥ 1. (Explain why without computing the integral, using a symmetry argument.)
- Show that a₀ = π and aₙ = 0 for even n, while aₙ = −4/(n²π) for odd n.
- Write the Fourier series. How quickly do the coefficients decay (as a function of n)?

**(c)** Compare the coefficient decay rates in (a) and (b). The sawtooth has a jump discontinuity; the triangle wave is continuous but has a corner (non-differentiable point). State the general principle: how does the smoothness of f(t) relate to the rate of decay of its Fourier coefficients?

**(d)** The **half-wave rectifier:** f(t) = sin(t) for 0 < t < π, f(t) = 0 for −π < t ≤ 0 (period T = 2π).

This models an AC electrical current passed through a diode. Compute a₀, a₁, b₁, and aₙ for n ≥ 2. (Hint: for aₙ with n ≥ 2, use the product-to-sum identity sin(t)cos(nt) = [sin((1+n)t) + sin((1−n)t)]/2.)

---

## Problem 2 — Parseval's Theorem and Energy (20 points)

**Parseval's theorem** states that for a function f with period T:
$$\frac{1}{T}\int_0^T |f(t)|^2\, dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}(a_n^2 + b_n^2)$$

**(a)** Prove Parseval's theorem. Start from the expression:
$$\frac{1}{T}\int_0^T \left(\frac{a_0}{2} + \sum_{n=1}^{\infty}[a_n\cos(2\pi n t/T) + b_n\sin(2\pi n t/T)]\right)^2 dt$$
and use the orthogonality relations:
$$\frac{1}{T}\int_0^T \cos(2\pi m t/T)\cos(2\pi n t/T)\, dt = \frac{1}{2}\delta_{mn}, \quad m, n \geq 1$$
to simplify. (You may assume term-by-term integration of the series is valid.)

**(b)** Apply Parseval's theorem to the sawtooth wave from Problem 1(a) to evaluate the sum:
$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$
Show your work: compute the left side of Parseval's theorem directly, equate to the right side, and solve for the sum. This famous result (Euler's Basel problem, 1734) follows from Fourier analysis.

**(c)** Apply Parseval's theorem to the triangular wave from Problem 1(b) to evaluate:
$$\sum_{n=1,3,5,...}^{\infty} \frac{1}{n^4} = \frac{\pi^4}{96}$$

**(d)** The sawtooth's Fourier coefficients satisfy bₙ = 2/n (up to sign). The tail energy after N terms is:
$$E_{\text{tail}}(N) = \frac{1}{2}\sum_{n=N+1}^{\infty} b_n^2 = \frac{1}{2}\sum_{n=N+1}^{\infty} \frac{4}{n^2}$$
Use the integral test (comparing to ∫_N^∞ 4/x² dx) to show E_tail(N) ≤ 4/N for large N. Then find the smallest N such that the tail contains less than 1% of the total energy. (The total energy of the sawtooth is π²/3.)

---

## Problem 3 — Orthogonality and the Fourier Basis (15 points)

**(a)** Prove the orthogonality relation:
$$\int_0^T \cos\!\left(\frac{2\pi m t}{T}\right)\sin\!\left(\frac{2\pi n t}{T}\right) dt = 0$$
for all integers m, n ≥ 0. (Use the product-to-sum identity: cos(A)sin(B) = [sin(A+B) − sin(A−B)]/2.)

**(b)** Prove:
$$\int_0^T \cos\!\left(\frac{2\pi m t}{T}\right)\cos\!\left(\frac{2\pi n t}{T}\right) dt = \begin{cases} 0 & m \neq n \\ T/2 & m = n \geq 1 \\ T & m = n = 0 \end{cases}$$

**(c)** Explain how orthogonality is the reason that the formula for aₙ (multiplying f by cos(2πnt/T) and integrating) isolates the n-th Fourier coefficient. Specifically: start from f(t) = a₀/2 + Σ aₙ cos(2πnt/T) + bₙ sin(2πnt/T), multiply both sides by cos(2πmt/T), integrate over [0, T], and show that only the m-th term survives.

---

## Problem 4 — The Wave Equation and Music (20 points)

A vibrating guitar string of length L satisfies the **wave equation**:
$$\frac{\partial^2 y}{\partial t^2} = c^2 \frac{\partial^2 y}{\partial x^2}, \quad 0 < x < L,\; t > 0$$
with boundary conditions y(0, t) = y(L, t) = 0 (string fixed at both ends).

**(a)** Seek a solution of the form y(x, t) = X(x) T(t) (separation of variables). Show that X and T must each satisfy:
$$X'' + \lambda X = 0, \qquad T'' + c^2\lambda T = 0$$
for some constant λ.

**(b)** Apply the boundary conditions X(0) = 0 and X(L) = 0 to find the allowable values of λ and the corresponding functions X(x). These are the **normal modes** of the string.

**(c)** For each allowable λ, find the corresponding T(t). Show that the normal mode frequencies are:
$$f_n = \frac{nc}{2L}, \quad n = 1, 2, 3, \ldots$$
The fundamental frequency is f₁ = c/(2L); all other frequencies are integer multiples (overtones).

**(d)** The general solution is:
$$y(x, t) = \sum_{n=1}^{\infty} \sin\!\left(\frac{n\pi x}{L}\right)\!\left[A_n \cos\!\left(\frac{n\pi c t}{L}\right) + B_n \sin\!\left(\frac{n\pi c t}{L}\right)\right]$$
Suppose the string is plucked at its midpoint: the initial displacement is y(x, 0) = h(2x/L) for 0 ≤ x ≤ L/2, and y(x, 0) = h(2(L−x)/L) for L/2 ≤ x ≤ L (a triangular pulse of height h), with ∂y/∂t|_{t=0} = 0.

Compute the coefficients Aₙ by expanding the triangular initial shape as a Fourier sine series. (Use the result from Problem 1(b) adapted for the interval [0, L].) Which harmonics are absent from the plucked-at-midpoint solution? What does this predict about the timbre of such a note?

---

## Problem 5 — Reading Response: Fourier (1822) (15 points)

Read the assigned excerpt from Fourier's *Analytical Theory of Heat* (Sections 169–186, provided on the course website). Then answer:

**(a)** Fourier introduces the idea that "any" function can be represented as a trigonometric series. His contemporaries (including Lagrange) were skeptical. What specific class of functions does Fourier seem to have in mind, and where does his argument leave gaps that require later rigorous treatment?

**(b)** Fourier derives his coefficient formulas by a "multiply and integrate" argument — the same argument you proved in Problem 3(c). Does Fourier give a rigorous justification for term-by-term integration of his infinite series? What would a modern analyst require to make this step rigorous?

**(c)** Fourier was motivated by the problem of heat conduction, not music. Yet his series now pervades signal processing, acoustics, quantum mechanics, and data science. Identify one field *other than* those discussed in the case that relies on Fourier analysis, and briefly explain how.
