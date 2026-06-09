# Homework 6: Predators, Prey, and Equilibrium

**Course:** Applied Mathematics 50
**Topic block:** Weeks 11–12 (Case 06)
**Due:** End of Week 12
**Instructions:** Show all derivations step by step. Phase-plane sketches should be clearly labeled with equilibria, nullclines, and flow directions.

---

## Problem 1 — Equilibria and Nullclines (20 points)

The Lotka-Volterra system is:

$$\frac{dx}{dt} = \alpha x - \beta xy, \qquad \frac{dy}{dt} = \delta xy - \gamma y$$

with α, β, δ, γ > 0 and x, y ≥ 0 (prey and predator populations).

**(a)** Find all equilibria (steady states) of the system by setting dx/dt = dy/dt = 0. Show that there are exactly two: the **trivial equilibrium** (0, 0) and the **coexistence equilibrium** (x*, y*). Express x* and y* in terms of the parameters.

**(b)** Find the **nullclines** of the system:
- The *x-nullclines* are the curves in the (x, y) plane where dx/dt = 0.
- The *y-nullclines* are the curves where dy/dt = 0.

Identify all nullclines and describe them geometrically (are they lines, curves, etc.?).

**(c)** Use the nullclines to divide the positive quadrant (x > 0, y > 0) into four regions. In each region, determine the signs of dx/dt and dy/dt, and indicate with arrows the direction of flow. Sketch the resulting phase portrait (rough sketch; no computation needed).

**(d)** Using your phase portrait from (c), describe qualitatively the expected dynamics starting from (x, y) = (2x*, y*/2) — a point with twice the prey equilibrium and half the predator equilibrium. Does the trajectory spiral inward, spiral outward, or form a closed loop? What does this suggest about the stability of the coexistence equilibrium?

---

## Problem 2 — The Conservation Law (25 points)

Define the function:

$$H(x, y) = \delta x - \gamma \ln x + \beta y - \alpha \ln y$$

**(a)** Compute dH/dt along trajectories of the Lotka-Volterra system. Show that dH/dt = 0, i.e., H is constant along every solution. (Hint: use the chain rule: dH/dt = (∂H/∂x)(dx/dt) + (∂H/∂y)(dy/dt).)

**(b)** Find the minimum of H(x, y) over the positive quadrant by setting ∂H/∂x = 0 and ∂H/∂y = 0. Show that the minimum occurs exactly at the coexistence equilibrium (x*, y*) and find H(x*, y*).

**(c)** Since H achieves its minimum at (x*, y*) and is conserved, all trajectories lie on level curves {H = c} for c ≥ H(x*, y*). What shape are these level curves near the minimum? (Hint: expand H in a Taylor series to second order around (x*, y*) and identify the resulting quadratic form.)

**(d)** From part (c), the level curves near the equilibrium are approximately ellipses. Find the equation of the tangent ellipse. What are the semi-axis lengths in the x and y directions? Express them in terms of α, β, δ, γ.

**(e)** The conservation law H implies that trajectories are *exactly* periodic — not just approximately. However, real predator-prey systems show *damped* oscillations that converge to the equilibrium. Name one biological mechanism that would break conservation of H and cause damping, and explain qualitatively which term in the ODE you would modify to capture it.

---

## Problem 3 — Linearization and Stability (25 points)

To analyze the stability of the coexistence equilibrium (x*, y*), we linearize the system.

**(a)** Let x = x* + u and y = y* + v, where u, v are small perturbations. Substitute into the Lotka-Volterra equations, expand to first order in u and v, and show that the linearized system is:

$$\frac{du}{dt} = -\beta x^* v, \qquad \frac{dv}{dt} = \delta y^* u$$

**(b)** Write this as a matrix system d/dt (u, v)ᵀ = A(u, v)ᵀ and identify the Jacobian matrix A. Compute the eigenvalues of A. Show that they are purely imaginary: λ = ±iω where ω = √(αγ).

**(c)** Purely imaginary eigenvalues indicate a **center** in the linearized system: trajectories near the equilibrium are ellipses traversed periodically with angular frequency ω. Find the period T = 2π/ω in terms of α and γ.

**(d)** Now linearize the system at the **trivial equilibrium** (0, 0). Compute the Jacobian there and find its eigenvalues. Classify the origin as stable, unstable, or saddle. Interpret biologically: what does this stability classification mean for the fate of a very small population of prey (with no predators) vs. a very small population of predators (with prey present)?

**(e)** The eigenvalues at the coexistence equilibrium are purely imaginary, meaning the linearization is *neutrally stable* — it neither attracts nor repels. This is a degenerate case where linearization alone cannot determine the nonlinear stability. Explain why the conservation law H from Problem 2 *does* resolve the stability question, and what it tells you about the coexistence equilibrium.

---

## Problem 4 — Volterra's Principle (15 points)

During World War I, fishing in the Adriatic Sea nearly ceased, and the proportion of predatory fish (sharks, rays) in catches increased after the war. Vito Volterra's model explains this.

Add proportional harvesting at rate h to both predator and prey:

$$\frac{dx}{dt} = (\alpha - h)x - \beta xy, \qquad \frac{dy}{dt} = \delta xy - (\gamma + h)y$$

**(a)** Find the new coexistence equilibrium (x*_h, y*_h) as a function of h. Express your answer in terms of α, β, δ, γ, and h. (Assume h < α so that the prey growth rate remains positive.)

**(b)** Show that x*_h is an increasing function of h (fishing increases the prey equilibrium) and y*_h is a decreasing function of h (fishing decreases the predator equilibrium). Compute dx*_h/dh and dy*_h/dh.

**(c)** Interpret part (b) in terms of the original fishing anomaly. When fishing stops (h → 0), which direction does the equilibrium shift? Is this consistent with D'Ancona's observation that predator proportions increased during the fishing moratorium?

**(d)** Volterra's principle applies only to proportional harvesting (both species harvested equally). Suppose instead that only the **prey** is harvested: dx/dt = (α − h)x − βxy, dy/dt = δxy − γy. Find the new equilibrium. Does fishing only the prey still benefit predators? Compare to the symmetric harvesting case.

---

## Problem 5 — Reading Response: Lotka (1920) and Volterra (1926) (15 points)

Read both Lotka (1920) and the excerpt from Volterra (1926) (provided on the course website). Then answer:

**(a)** Lotka and Volterra discovered essentially the same model independently. Lotka was motivated by chemistry (oscillating chemical reactions), while Volterra was motivated by ecology. Does the model look the same in both papers, or are there differences in formulation or emphasis? Identify one notable difference.

**(b)** Volterra states his "three laws" of fluctuation in predator-prey systems. State all three laws in your own words and verify mathematically that each follows from the ODE system (using the equilibrium analysis and conservation law from Problems 1–4).

**(c)** Volterra's model was criticized by the ecologist G. F. Gause in the 1930s based on laboratory experiments with *Paramecium* (prey) and *Didinium* (predator). Gause found that the predator always drove the prey to extinction rather than oscillating. What modification to the Lotka-Volterra model (one that you have studied in this course) could explain Gause's experimental result? (Hint: consider what happens when the prey population is very small and there is no spatial refuge.)
