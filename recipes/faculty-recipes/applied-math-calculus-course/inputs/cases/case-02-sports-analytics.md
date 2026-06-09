# Case 02: The Math of Winning — Sports Analytics and Optimal Decision-Making

**Course:** Applied Mathematics 50
**Topic block:** Weeks 3–4
**Fields:** Sports analytics, probability, optimization, differential equations

---

## Overview

In 2002, the Oakland Athletics built a playoff team on a fraction of the payroll of the New York Yankees. Their secret: systematic use of statistics to find undervalued players. But the mathematics of sports goes far deeper than batting averages. This case examines three problems where applied mathematics has transformed how sports are played and managed: **expected value and win probability in baseball**, **optimal strategy in basketball** (the "hot hand" and shot selection), and **trajectory optimization in track and field**.

---

## Problem 1: Run Expectancy and Optimal Strategy in Baseball

### Setup
A baseball game state can be described by (outs, base configuration). There are 3 possible out counts and 8 possible base configurations (2³ — each of first, second, third base either occupied or empty), giving 24 distinct states (plus the end-of-inning state).

The **run expectancy matrix** RE[s] gives the expected number of runs scored from state s to the end of the inning, computed from historical data.

### Mathematical Content

**Markov chains.** The game transitions between states according to transition probabilities that depend on the batting outcome (single, double, home run, out, etc.). If P is the transition matrix and r is the vector of immediate run values, the run expectancy vector satisfies:

$$\mathbf{RE} = \mathbf{r} + P\,\mathbf{RE}$$

This is a linear system (I − P)RE = r. Solving it gives the expected runs from each state.

**Decision analysis.** Should a runner attempt to steal second base? The manager's calculus:

- Success: state transitions from (outs, runner-on-1st) to (outs, runner-on-2nd); gain = RE[new state] − RE[old state]
- Failure: outs increase by 1; loss = RE[new state] − RE[old state] (negative)
- Break-even stolen base success rate: p* = |loss| / (|loss| + gain)

A steal attempt is profitable if and only if the runner's success probability exceeds p*.

**Connection to course material:** This is a system of linear equations (linear algebra); the structure mirrors the integrating-factor method for linear ODEs (Unit 5.3) in that both involve solving (I − A)x = b for an unknown vector.

### Classic Paper
**James, Bill.** *The Bill James Baseball Abstract*, 1977–1988 (excerpts). — The foundational texts of sabermetrics, introducing concepts like runs created and win shares with explicit mathematical formulas.

---

## Problem 2: The Hot Hand and Probability in Basketball

### Setup
Does a basketball player who has made several shots in a row have an elevated probability of making the next shot? This is the "hot hand" question. It has been debated for 40 years and involves subtle mathematics.

### Mathematical Content

**The original study (1985):** Gilovich, Vallone, and Tversky analyzed shooting records and found *no* evidence of a hot hand — a player's probability of making a shot appeared independent of recent outcomes.

**The correction (2016):** Miller and Sanjurjo showed a mathematical bias in the original analysis. When you condition on a streak of k hits within a finite sequence, the expected proportion of subsequent hits is *less than* the overall hit rate, even for a fair coin. This is a subtle consequence of sampling without replacement.

**The mathematics:** Let X₁, X₂, …, Xₙ be i.i.d. Bernoulli(p) trials (shots). Define the conditional hit rate after a streak of k as:

$$\hat{p}_k = \frac{\text{# hits at position } i \text{ s.t. } X_{i-k} = \cdots = X_{i-1} = 1}{|\{i : X_{i-k} = \cdots = X_{i-1} = 1\}|}$$

Miller and Sanjurjo proved that E[p̂_k] < p for finite n, and computed the exact bias. Once corrected, several datasets show statistically significant evidence *for* a hot hand.

**The lesson:** A mathematical error hid a real effect for 30 years. Small sample sizes and improper conditioning can reverse apparent conclusions.

**Connection to course material:** Probability density functions and expected value (Unit 2.4); geometric series appear in computing expectations over streak lengths (Unit 3.2).

---

## Problem 3: Optimal Running Strategy — The Calculus of Speed

### Setup
A sprinter has a finite energy reserve. How should she allocate effort over a 400-meter race to minimize her finishing time?

### Mathematical Content

**The Keller model (1974).** Let v(t) be the runner's speed and f(t) the propulsive force per unit mass. The equations of motion are:

$$\frac{dv}{dt} = f(t) - \frac{v}{\tau}$$

where τ is a resistance constant (τ ≈ 1 s for elite sprinters). The energy constraint is:

$$\int_0^T f(t)\, dt \leq E_0 + \sigma T$$

where E₀ is the initial anaerobic energy reserve and σ is the aerobic power supply rate.

**Optimal control.** The runner minimizes T subject to the ODE and energy constraint. Using the calculus of variations, Keller showed that the optimal strategy is:

- **Sprint at maximum force** initially (anaerobic phase)
- **Maintain constant speed** once the constraint becomes binding (aerobic phase)

This predicts that 100m sprinters should accelerate for the first ~6 seconds and then hold speed — consistent with observed race data.

**Connection to course material:** First-order linear ODE (Unit 5.3); optimization under constraints (echoes of Math 1a optimization); improper integrals and energy accumulation (Unit 1.5 and 2.3).

### Classic Paper
**Keller, Joseph B.** "A theory of competitive running." *Physics Today* 26(9) (1973): 43–47. — Elegant and short; the ODE is accessible after Math 1b Unit 5.

---

## Modeling Exercise

**Run expectancy simulation.** Using a simplified model with three outcomes per plate appearance (out: 70%, single: 20%, home run: 10%), build the 24-state Markov chain by hand for a one-base model (runners advance one base on a single).

1. Write out the 3×3 transition matrix for a simplified two-state model (runner on first with 0 outs; runner on second with 0 outs; inning over).
2. Solve (I − P)RE = r for the run expectancy vector.
3. Compute the break-even stolen base percentage for a runner on first with 0 outs.
4. How does the break-even rate change with 1 out? 2 outs? Interpret the results.

---

## Discussion Questions

1. The Keller model treats the runner as a machine with a fixed energy supply. What physiological factors does it ignore, and how might you extend the model to account for them?

2. In basketball, teams now use "shot quality" metrics — expected points per shot attempt based on location and defensive pressure. How would you construct such a metric mathematically? What data would you need?

3. The hot-hand debate lasted decades because of a subtle mathematical bias. Can you think of other domains (medicine, finance, education) where a similar conditioning bias might lead to incorrect conclusions?

4. Should professional sports teams fully optimize based on mathematical models? What non-mathematical considerations might justify deviating from the optimal strategy?

---

## Further Reading

- Lewis, Michael. *Moneyball: The Art of Winning an Unfair Game.* W. W. Norton, 2003.
- Miller, Joshua Benjamin, and Adam Sanjurjo. "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers." *Econometrica* 86(6) (2018): 2019–2047.
- Keller, Joseph B. "Optimal velocity in a race." *American Mathematical Monthly* 81(5) (1974): 474–480.
- Winston, Wayne L. *Mathletics: How Gamblers, Managers, and Sports Enthusiasts Use Mathematics in Baseball, Basketball, and Football.* Princeton University Press, 2009.
