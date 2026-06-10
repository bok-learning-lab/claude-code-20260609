# Week 1: Limits and Continuity via Discrete-Time Disease Spread

**AM50 thread for the week.** A new flu strain arrives on a small island. Each day, some infected people recover and some new people get sick. Students build a discrete-time SIR model on day 1, and over the course of the week we ask: what happens as the time step shrinks? When does the discrete model become continuous? Where does it break?

---

## Monday — Day 1: From discrete updates to the idea of a limit

**Lecture (45 min).** Open with the island flu problem. Write the day-by-day update rule for the infected count: $I_{n+1} = I_n + \beta S_n I_n / N - \gamma I_n$. Ask: what would it mean to ask for $I(t)$ at a non-integer time? This motivates the **limit** — what the sequence "approaches" as we shrink the step. Define $\lim_{n \to \infty}$ informally, then formally (epsilon–N).

**Active practice (75 min).**

- *(pure calc)* Compute $\lim_{n \to \infty} \frac{3n+1}{n+5}$ by inspection, then by formal definition.
- *(bridge)* Given the SIR update rule with $\beta = 0.3, \gamma = 0.1, N = 100, I_0 = 1$, simulate 30 days by hand on a calculator. Tabulate.
- *(application)* What appears to be the long-run value of $I_n$? Can you predict it without simulating? (Sets up fixed points later.)
- *(pure calc)* Show $\lim_{n \to \infty} (1 + 1/n)^n$ converges. (Foreshadow $e$.)

**HW support (60 min).** Likely sticking points: (1) confusion between "limit exists" and "limit equals the value of the function" — pre-empt with a one-sided-limit example; (2) algebra errors in $\frac{\infty}{\infty}$ forms — show the "divide numerator and denominator by the highest power" trick.

---

## Tuesday — Day 2: Continuity and the intermediate value theorem

**Lecture (45 min).** Plot the SIR trajectories from Monday's HW. Notice they look like smooth curves even though they are sequences of discrete points. What does "smooth" mean? Define **continuity** at a point. State the **Intermediate Value Theorem** with the question: "did the infection count ever pass exactly 50?" The discrete model can never answer yes; the continuous model can.

**Active practice (75 min).**

- *(pure calc)* Which of $f(x) = 1/x$, $g(x) = |x|$, $h(x) = \lfloor x \rfloor$ are continuous on $[-1, 1]$? Where do they fail?
- *(bridge)* The SIR sequence $I_n$ hits values 45 and 56 on consecutive days. Did $I$ "ever equal 50"? Defend both answers.
- *(application)* A clinician asks: "when does the epidemic cross 50% of the population?" — frame this as an IVT question on a continuous interpolation.

**HW support (60 min).** Sticking points: (1) students confuse "continuous" with "defined everywhere" — give the removable-discontinuity counterexample; (2) IVT requires a closed interval and continuity — students forget the hypotheses.

---

## Wednesday — Day 3: Average rate of change → instantaneous rate

**Lecture (45 min).** Take the SIR trajectory. Compute the **average growth rate** $(I_{n+k} - I_n) / k$ for $k = 5, 2, 1$. As $k$ shrinks, what does the rate approach? This is the **difference quotient**, and its limit is the **derivative**. Define $f'(a) = \lim_{h \to 0} (f(a+h) - f(a))/h$.

**Active practice (75 min).**

- *(pure calc)* Compute $f'(2)$ from the definition for $f(x) = x^2$, then for $f(x) = 1/x$.
- *(bridge)* For the continuous SIR interpolation $I(t)$, estimate $I'(10)$ from a table of values using forward, backward, and centered differences. Which is most accurate?
- *(application)* What are the units of $I'(t)$? Write a one-sentence interpretation for a public-health audience.

**HW support (60 min).** Sticking points: (1) algebra in the difference quotient — students drop minus signs; (2) confusing $f'(a)$ (a number) with $f'(x)$ (a function).

---

## Thursday — Day 4: The derivative as a function + quiz

**Lecture (30 min).** Build $I'(t)$ at every $t$, not just one point. Connect to the **continuous SIR ODE** $dI/dt = \beta S I / N - \gamma I$. Preview: next week we will solve it.

**Active practice (60 min).**

- *(pure calc)* Find $f'(x)$ from the definition for $f(x) = x^3$ and $f(x) = \sqrt{x}$.
- *(bridge)* Given $I'(t) = 0.2 \cdot I(t) - 0.1 \cdot I(t)$, what does $I(t)$ look like? (Foreshadow exponential growth.)
- *(application)* On a public-health dashboard, you see $dI/dt > 0$ for two weeks, then $dI/dt < 0$. What story does this tell?

**Weekly quiz (60 min).** Five questions, 30 min written + 30 min review.

1. *(pure calc)* Compute $\lim_{x \to 3} (x^2 - 9)/(x-3)$.
2. *(pure calc)* Is $f(x) = (x^2 - 4)/(x - 2)$ continuous at $x = 2$? Justify.
3. *(application)* Given a table of $I_n$ values, estimate the instantaneous growth rate at $n = 7$ two different ways.
4. *(bridge)* For what values of $\beta$ does the IVT guarantee the infection passed 50%?
5. *(reflection)* In one sentence: when does it matter whether you use the discrete or the continuous model?

---

## End-of-week assets to hand the instructor

- Week 1 lecture slides (4 decks).
- Active-practice worksheet (one per day) with answer key.
- HW set with starred problems flagged for HW-support session.
- Weekly quiz + rubric.
- A "What's coming next week" teaser tying continuous SIR into differentiation rules and the chain rule.
