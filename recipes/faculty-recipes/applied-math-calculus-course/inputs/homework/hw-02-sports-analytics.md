# Homework 2: The Mathematics of Sports

**Course:** Applied Mathematics 50
**Topic block:** Weeks 3–4 (Case 02)
**Due:** End of Week 4
**Instructions:** Show all algebra and reasoning. For the ODE problems, present the solution method clearly — not just the answer. Collaboration is encouraged; write-ups must be your own.

---

## Problem 1 — Markov Chains and Run Expectancy (30 points)

We model a baseball half-inning with the following simplified setup. There are **four states**:

- **State A:** Bases empty, 0 outs
- **State B:** Runner on first, 0 outs
- **State C:** Runner on second, 0 outs
- **State D:** Inning over (absorbing)

From States A, B, or C, each plate appearance produces one of three outcomes:

| Outcome | Probability | Effect from State A | Effect from State B | Effect from State C |
|---------|-------------|--------------------|--------------------|-------------------|
| Out | 0.70 | → D (inning ends) | → D | → D |
| Single | 0.20 | → B (runner on 1st) | → C (runner advances) | → B (new runner on 1st, original scores: +1 run) |
| Home run | 0.10 | → A (+1 run) | → A (+2 runs) | → A (+2 runs) |

**(a)** Write the transition matrix P for this 4-state chain, where P[i,j] = probability of moving from state i to state j. Include State D as a row and column. (Note: D is absorbing, so P[D,D] = 1.)

**(b)** Let **r** be the vector of expected runs scored *on the transition out of each state* (i.e., the immediate run reward). Write out **r** explicitly for all four states.

**(c)** For the three transient states (A, B, C), the run expectancy vector **RE** satisfies:

**(I − Q) RE = r_transient**

where Q is the 3×3 submatrix of P restricted to the transient states, and **r_transient** is the immediate reward from those states. Write out (I − Q) explicitly and solve the linear system by hand (Gaussian elimination or substitution) to find RE_A, RE_B, and RE_C.

**(d)** A manager has a runner on first (State B) with 0 outs. A stolen base attempt succeeds with probability p (moving to State C) and fails with probability 1 − p (moving to State D — runner caught, inning ends). 

- Write the net expected run value of a steal attempt as a function of p.
- Find the break-even probability p* at which a steal attempt is exactly neutral.
- If a particular runner succeeds on 65% of steal attempts, should the manager send the runner? Justify using your run expectancy values.

**(e)** Extend your analysis: suppose a single advances a runner from State B to State C (as in the table), but instead of ending the inning, an out from State B moves to a new state "Runner on first, 1 out" with RE = 0.4 (given). Redo the stolen base break-even calculation. Does the manager's decision change? What does this suggest about the importance of the out count in base-running decisions?

---

## Problem 2 — The Hot Hand: A Mathematical Bias (20 points)

Miller and Sanjurjo (2016) showed that the original Gilovich-Vallone-Tversky study contained a subtle mathematical bias. This problem works through the core of their argument.

Consider a sequence of N = 4 fair coin flips. There are 2⁴ = 16 equally likely sequences.

**(a)** List all 16 sequences of length 4 (e.g., HHHH, HHHT, …).

**(b)** For each sequence, identify every position i ≥ 2 where the *preceding flip* (position i−1) was H. For each such position, record whether flip i is H or T. Compute, for each sequence, the fraction of "post-H" flips that are H. (If a sequence has no H in positions 1–3, that sequence contributes nothing.)

**(c)** Average the fractions from part (b) across all sequences that have at least one post-H flip. Call this average p̂.

**(d)** Is p̂ equal to 1/2, greater than 1/2, or less than 1/2? Explain why this result is surprising. (The coin is fair, so shouldn't the fraction of heads always average to 1/2?)

**(e)** Generalize: explain in words, without equations, why conditioning on a streak within a finite sequence creates a downward bias in the estimated subsequent hit rate. (Hint: think about which positions *can* be both in the streak and the subsequent flip simultaneously.)

**(f)** The original Gilovich-Tversky study used roughly N = 100 shots per player and k = 3 (conditioning on a streak of 3). If the true hot-hand effect increases a player's probability from 0.50 to 0.55 after a streak of 3, and the Miller-Sanjurjo bias is approximately −0.04 for N = 100, k = 3: would the corrected analysis detect the hot-hand effect? What sample size N would be needed to reliably detect an effect of this magnitude?

---

## Problem 3 — The Keller Sprinting Model (30 points)

The Keller model for a sprinter is:

$$\frac{dv}{dt} = f(t) - \frac{v}{\tau}, \quad v(0) = 0$$

where v(t) is speed, f(t) is propulsive force per unit mass, and τ = 1 s is a resistance constant.

**(a)** This is a first-order linear ODE. Use the integrating factor method to find the general solution v(t) for an arbitrary forcing function f(t). (Do not assume f is constant yet.)

**(b)** For the special case of constant maximum force f(t) = F (a sprinter exerting full effort throughout), find the explicit solution v(t) with v(0) = 0. What is the terminal velocity v_∞ = lim_{t→∞} v(t)?

**(c)** The distance covered by time T is x(T) = ∫₀ᵀ v(t) dt. Using the solution from part (b), compute x(T) exactly. Show that for large T, x(T) ≈ F·τ·T − F·τ² (i.e., the runner approaches constant speed and the position grows linearly).

**(d)** The world record for the 100m sprint is approximately 9.58 s (Usain Bolt, 2009). Using your formula from part (c) with τ = 1 s, find the value of F (maximum force) that predicts a 100m time of exactly 9.58 s. (Set x(T) = 100 and solve for F given T = 9.58.)

**(e)** Keller showed that the optimal strategy for a *longer* race involves applying maximum force initially and then maintaining a constant speed determined by the energy constraint. Suppose a runner has:
- Anaerobic energy reserve: E₀ = 60 m²/s² (equivalent to about 6 seconds of maximum sprint)
- Aerobic power supply rate: σ = 10 m²/s³

The energy constraint is: ∫₀ᵀ f(t) dt ≤ E₀ + σT.

For a 400m race, argue (without calculus of variations) that the optimal strategy is:
- Phase 1 (0 ≤ t ≤ t₁): apply maximum force F
- Phase 2 (t₁ ≤ t ≤ T): apply constant force f* = σ (exactly matching aerobic supply)

Find the constant speed v* achieved in Phase 2 (set dv/dt = 0 in the ODE with f = σ). Then write an equation relating t₁ and T to the constraint that x(T) = 400. (You do not need to solve this equation explicitly.)

**(f)** The Keller model ignores fatigue: in reality, a runner's maximum force decreases over time. If F(t) = F₀ e^(−t/T_f) where T_f = 60 s is a fatigue time constant, write the modified ODE and find the terminal velocity in Phase 1. Is the predicted 100m time longer or shorter than in part (d)? (Qualitative answer with brief justification is sufficient.)

---

## Problem 4 — Reading Response: Keller (1973) (20 points)

Read Keller's 1973 paper "A theory of competitive running" (provided on the course website). Then answer:

**(a)** Keller applies his model to several running events from the 100m to the mile. His predicted times match world records of the era remarkably well. List two specific predictions he makes and compare to the actual world records at the time of writing.

**(b)** Keller's model is a *continuous* optimization — it treats the race as a smooth dynamical system. Real races involve discrete events (reactions to other runners, tactical decisions, pacing judgment). Identify one prediction of the Keller model that you think would *fail* for a tactical 1500m race that ends in a sprint finish, and explain why.

**(c)** Keller's paper appeared in *Physics Today*, not a biology or sports science journal. What does this publication venue suggest about the intended audience, and how does it influence the level of biological detail in the model? Give one biological omission that a sports scientist would likely criticize.
