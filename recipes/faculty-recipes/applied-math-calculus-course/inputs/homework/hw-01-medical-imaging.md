# Homework 1: The Mathematics of Medical Imaging

**Course:** Applied Mathematics 50
**Topic block:** Weeks 1–2 (Case 01)
**Due:** End of Week 2
**Instructions:** Show all work. Justify each step. Answers without reasoning receive no credit. You may use a calculator for arithmetic but all calculus must be done by hand.

---

## Problem 1 — Line Integrals as Projections (25 points)

The Radon transform of a function f(x, y) along the line x cos θ + y sin θ = t is:

$$\mathcal{R}f(t,\theta) = \int_{-\infty}^{\infty} f(t\cos\theta - s\sin\theta,\; t\sin\theta + s\cos\theta)\, ds$$

**(a)** Let f(x, y) = 1 inside the unit disk (x² + y² ≤ 1) and f(x, y) = 0 outside it. Compute Rf(t, θ) for an arbitrary angle θ and show that your answer is independent of θ. (Hint: the line x cos θ + y sin θ = t intersects the disk in a chord of length 2√(1 − t²) for |t| ≤ 1.)

**(b)** For the function in part (a), sketch Rf(t, θ) as a function of t for fixed θ. What does the shape of this curve tell you physically about the density of the disk?

**(c)** Now let f(x, y) = 1 inside the square [−1, 1] × [−1, 1] and 0 outside. Compute Rf(t, 0) (i.e., at θ = 0). Then compute Rf(t, π/4). Are these two projections the same? What does the difference tell you about the shape of the object?

**(d)** Explain in one paragraph why measuring Rf(t, θ) for all t at a single angle θ is not sufficient to determine f(x, y). How many angles are theoretically needed for a unique reconstruction?

---

## Problem 2 — The Fourier Slice Theorem (25 points)

The **Fourier Slice Theorem** states that the 1D Fourier transform of the projection Rf(·, θ) at angle θ equals the 2D Fourier transform of f evaluated along the line at angle θ through the origin. This problem walks you through the proof.

Define the 2D Fourier transform:
$$F(u, v) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x, y)\, e^{-2\pi i (ux + vy)}\, dx\, dy$$

and the 1D Fourier transform of the projection:
$$P_\theta(\omega) = \int_{-\infty}^{\infty} \mathcal{R}f(t, \theta)\, e^{-2\pi i \omega t}\, dt$$

**(a)** Substitute the definition of Rf(t, θ) into the expression for P_θ(ω). You will have a double integral over t and s.

**(b)** Change variables from (t, s) to (x, y) using:
$$x = t\cos\theta - s\sin\theta, \qquad y = t\sin\theta + s\cos\theta$$
Show that the Jacobian of this transformation is 1 (i.e., dx dy = dt ds).

**(c)** After the change of variables, show that the exponent becomes −2πiω(x cos θ + y sin θ). Conclude that:
$$P_\theta(\omega) = F(\omega\cos\theta,\; \omega\sin\theta)$$

**(d)** Explain in plain English what the Fourier Slice Theorem says about the relationship between taking projections of f and sampling its 2D Fourier transform. Why does this theorem suggest a reconstruction strategy?

---

## Problem 3 — Solving a Small Linear System (20 points)

Consider a 2×2 pixel image with unknown densities:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

A scanner measures the following projections:
- Row 1 sum: a + b = 3
- Row 2 sum: c + d = 5
- Column 1 sum: a + c = 4
- Column 2 sum: b + d = 4
- Main diagonal sum: a + d = 5

**(a)** Write this as a linear system A**f** = **b** where **f** = (a, b, c, d)ᵀ. Write out the matrix A and vector **b** explicitly.

**(b)** Is the system underdetermined, overdetermined, or square? Does the system have a unique solution, no solution, or infinitely many solutions? Justify your answer.

**(c)** Find all values of (a, b, c, d) consistent with the first four measurements (rows and columns only, ignoring the diagonal). Is the solution unique?

**(d)** Now include the diagonal measurement. Does this additional equation determine a unique solution? Find it, or show that the system is inconsistent.

**(e)** Suppose the diagonal measurement is corrupted by noise: instead of a + d = 5, the scanner reads a + d = 5.3. Find the least-squares solution **f** = A⁺**b** that minimizes ||A**f** − **b**||². (You may compute the pseudoinverse numerically or by hand.)

---

## Problem 4 — Reading Response: Hounsfield (1973) (30 points)

Read Sections 1–4 of Hounsfield's 1973 paper (provided on the course website). Then answer the following.

**(a)** Hounsfield describes taking 28,800 measurements to reconstruct an 80×80 image. Express the measurement matrix A as having dimensions m × n. What are m and n? Is the system overdetermined, and by what factor?

**(b)** Hounsfield's original reconstruction algorithm took several hours on 1970s computers. He describes iterating over the measurements to correct an initial estimate. This is related to the **algebraic reconstruction technique (ART)**, an iterative method for solving Af = b. In ART, one initializes **f**⁽⁰⁾ = 0 and updates:

$$\mathbf{f}^{(k+1)} = \mathbf{f}^{(k)} + \frac{b_i - \mathbf{a}_i^\top \mathbf{f}^{(k)}}{\|\mathbf{a}_i\|^2}\,\mathbf{a}_i$$

where **a**_i is the i-th row of A and b_i is the i-th measurement. Perform two steps of ART by hand on the system from Problem 3 (using the first two measurements and starting from **f**⁽⁰⁾ = **0**). What is **f**⁽²⁾?

**(c)** Hounsfield was an engineer, not a mathematician. He justified his reconstruction heuristically. Radon had provided the rigorous mathematical theory 56 years earlier but was unknown to Hounsfield. What does this episode suggest about the relationship between pure mathematics and applied technology? Give a second example from history of a similar gap between mathematical discovery and technological application.

**(d)** Modern CT scanners produce a full-body scan in under 10 seconds. Hounsfield's scanner took 9 days to compute the reconstruction. Identify two distinct reasons (one algorithmic, one hardware) that explain this improvement.
