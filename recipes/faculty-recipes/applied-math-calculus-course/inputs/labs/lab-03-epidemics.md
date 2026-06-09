# Lab 03: Modeling an Epidemic — The SIR Model

**Course:** Applied Mathematics 50
**Companion to:** Case 03 (Epidemics)
**Estimated time:** 2 hours
**Tools:** Python 3, NumPy, Matplotlib, SciPy

---

## Learning Goals

By the end of this lab you will be able to:
- Implement and simulate the SIR model using Euler's method and a built-in ODE solver
- Compute R₀ and the herd immunity threshold from model parameters
- Fit the model to historical epidemic data using a growth-rate estimate
- Explore how interventions (vaccination, social distancing) alter epidemic trajectories

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

rng = np.random.default_rng(7)
```

---

## Part 1: Implementing the SIR Model

### Equations

$$\frac{dS}{dt} = -\beta S I, \qquad \frac{dI}{dt} = \beta S I - \gamma I, \qquad \frac{dR}{dt} = \gamma I$$

```python
def sir_ode(t, y, beta, gamma, N):
    """Right-hand side of the SIR system."""
    S, I, R = y
    dS = -beta * S * I / N
    dI =  beta * S * I / N - gamma * I
    dR =  gamma * I
    return [dS, dI, dR]

def run_sir(N, I0, beta, gamma, t_max=200):
    """Solve the SIR model and return arrays (t, S, I, R)."""
    S0 = N - I0
    R0_init = 0
    y0 = [S0, I0, R0_init]
    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, 2000)

    sol = solve_ivp(sir_ode, t_span, y0, args=(beta, gamma, N),
                    t_eval=t_eval, method='RK45', rtol=1e-8)
    return sol.t, sol.y[0], sol.y[1], sol.y[2]
```

### First simulation

```python
N     = 10_000    # total population
I0    = 10        # initial infected
beta  = 0.30      # transmission rate (per day)
gamma = 0.10      # recovery rate (1/γ = 10-day infectious period)
R0    = beta / gamma
print(f"R₀ = β/γ = {R0:.1f}")
print(f"Herd immunity threshold: {(1 - 1/R0):.1%} of population")

t, S, I, R = run_sir(N, I0, beta, gamma)

plt.figure(figsize=(8, 5))
plt.plot(t, S, label='Susceptible (S)', color='steelblue')
plt.plot(t, I, label='Infectious (I)',  color='tomato')
plt.plot(t, R, label='Recovered (R)',   color='seagreen')
plt.xlabel('Time (days)')
plt.ylabel('Number of individuals')
plt.title(f'SIR Model  (R₀ = {R0:.1f},  N = {N:,})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sir_baseline.png', dpi=100)
plt.show()

# Epidemic peak
peak_day = t[np.argmax(I)]
peak_I   = np.max(I)
final_R  = R[-1]
print(f"\nEpidemic peak: day {peak_day:.0f},  {peak_I:.0f} infected ({peak_I/N:.1%} of population)")
print(f"Total infected (final R): {final_R:.0f} ({final_R/N:.1%} of population)")
```

**Question 1.1:** At the epidemic peak, what fraction of the population is still susceptible? Compare this to 1/R₀. Does the theory match?

**Question 1.2:** The model predicts that not everyone gets infected even when R₀ > 1. Approximately what fraction of the population escaped infection? Is this consistent with the herd immunity threshold?

---

## Part 2: Euler's Method

Implement the SIR model "from scratch" using Euler's method to see how the numerical approximation works.

```python
def euler_sir(N, I0, beta, gamma, dt=0.5, t_max=200):
    """Solve SIR using forward Euler's method."""
    t_vals = [0.0]
    S_vals = [N - I0]
    I_vals = [float(I0)]
    R_vals = [0.0]

    S, I, R = N - I0, float(I0), 0.0

    while t_vals[-1] < t_max:
        dS = -beta * S * I / N
        dI =  beta * S * I / N - gamma * I
        dR =  gamma * I

        S += dS * dt
        I += dI * dt
        R += dR * dt

        t_vals.append(t_vals[-1] + dt)
        S_vals.append(S)
        I_vals.append(I)
        R_vals.append(R)

    return np.array(t_vals), np.array(S_vals), np.array(I_vals), np.array(R_vals)

# Compare Euler (dt=0.5) vs. RK45
t_rk, S_rk, I_rk, R_rk = run_sir(N, I0, beta, gamma)
t_eu, S_eu, I_eu, R_eu = euler_sir(N, I0, beta, gamma, dt=0.5)
t_eu_coarse, S_ec, I_ec, R_ec = euler_sir(N, I0, beta, gamma, dt=5.0)

plt.figure(figsize=(8, 5))
plt.plot(t_rk, I_rk, 'k-',  linewidth=2.5, label='RK45 (reference)')
plt.plot(t_eu, I_eu, 'b--', linewidth=1.5, label='Euler dt=0.5 day')
plt.plot(t_eu_coarse, I_ec, 'r:',  linewidth=1.5, label='Euler dt=5 days')
plt.xlabel('Time (days)')
plt.ylabel('Infectious (I)')
plt.title('Euler vs. RK45 — Effect of Step Size')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('euler_comparison.png', dpi=100)
plt.show()
```

**Question 2.1:** With dt = 5 days, Euler's method becomes inaccurate. Describe specifically how the error manifests (wrong peak height, wrong timing, instability?). Why does a smaller dt improve accuracy?

**Question 2.2:** The SIR model satisfies S + I + R = N exactly. Check whether your Euler implementation conserves this quantity. Does the error in conservation grow over time?

---

## Part 3: The Epidemic Threshold

Explore how R₀ determines whether an epidemic occurs.

```python
R0_values = [0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]
gamma_fixed = 0.10

final_fractions = []
peak_fractions  = []

for R0_val in R0_values:
    beta_val = R0_val * gamma_fixed
    t, S, I, R = run_sir(N, I0, beta_val, gamma_fixed)
    final_fractions.append(R[-1] / N)
    peak_fractions.append(np.max(I) / N)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(R0_values, [f * 100 for f in final_fractions], 'o-', color='tomato', linewidth=2)
axes[0].axvline(1.0, color='gray', linestyle='--', label='R₀ = 1')
axes[0].set_xlabel('R₀')
axes[0].set_ylabel('Final infected (%)')
axes[0].set_title('Total Epidemic Size vs. R₀')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(R0_values, [f * 100 for f in peak_fractions], 'o-', color='steelblue', linewidth=2)
axes[1].axvline(1.0, color='gray', linestyle='--', label='R₀ = 1')
axes[1].set_xlabel('R₀')
axes[1].set_ylabel('Peak infected (%)')
axes[1].set_title('Peak Epidemic Size vs. R₀')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sir_threshold.png', dpi=100)
plt.show()
```

**Question 3.1:** Describe the behavior near R₀ = 1. Is the transition from "no epidemic" to "epidemic" sharp or gradual?

**Question 3.2:** For COVID-19, early estimates of R₀ ranged from 2.5 to 3.5. For seasonal flu, R₀ ≈ 1.3. What fraction of the population would each infect, according to your simulations? What does this imply for vaccine coverage requirements?

---

## Part 4: Fitting to Historical Data

Use the 1918 influenza data from Case 03 to estimate R₀.

```python
# Weekly deaths in London, fall 1918 (approximate, in hundreds)
weeks  = np.array([1, 2, 3, 4, 5, 6, 7, 8])
deaths = np.array([300, 800, 2400, 5100, 6200, 4900, 2300, 800])

# Assume deaths proportional to I(t): deaths[t] ≈ c * I(t)
# Early growth: deaths[t+1] / deaths[t] ≈ exp(r * 7)  (7-day weeks)
early_ratios = deaths[1:4] / deaths[0:3]
weekly_growth_rates = np.log(early_ratios) / 7  # convert to daily rate
r_estimate = np.mean(weekly_growth_rates)

# r = γ(R₀ - 1)  =>  R₀ = 1 + r/γ
gamma_1918 = 1 / 5  # 5-day infectious period
R0_1918    = 1 + r_estimate / gamma_1918
beta_1918  = R0_1918 * gamma_1918

print(f"Early growth rate r ≈ {r_estimate:.4f} per day")
print(f"Estimated R₀ = {R0_1918:.2f}")
print(f"Herd immunity threshold = {(1 - 1/R0_1918):.1%}")

# Run the model (London pop ~7 million in 1918, seed with estimated infected)
N_1918 = 7_000_000
I0_1918 = 100
t_1918, S_1918, I_1918, R_1918 = run_sir(N_1918, I0_1918, beta_1918, gamma_1918, t_max=120)

# Scale simulated I to match deaths (find best scale factor)
# Peak deaths occur at peak I — align the peaks
peak_sim_week = np.argmax(I_1918) / (len(t_1918) / 120) / 7  # approximate week of peak
scale = deaths.max() / I_1918.max()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(weeks, deaths, color='tomato', alpha=0.7, label='Observed deaths')
axes[0].set_xlabel('Week')
axes[0].set_ylabel('Deaths')
axes[0].set_title('1918 London Influenza Deaths')
axes[0].legend()

axes[1].plot(t_1918, I_1918 * scale, 'steelblue', linewidth=2, label=f'SIR model (R₀={R0_1918:.2f})')
axes[1].scatter(weeks * 7, deaths, color='tomato', zorder=5, label='Observed deaths (scaled)')
axes[1].set_xlabel('Day')
axes[1].set_ylabel('Deaths / Infected (scaled)')
axes[1].set_title('SIR Model vs. 1918 Data')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sir_1918_fit.png', dpi=100)
plt.show()
```

**Question 4.1:** How well does the SIR model fit the 1918 data? Where does it succeed and where does it fail?

**Question 4.2:** Your R₀ estimate for 1918 influenza should be around 2–3. The 2009 H1N1 pandemic had R₀ ≈ 1.4–1.6 and caused far fewer deaths. Using your simulations, estimate the difference in total deaths if the same fraction of the London population were infected in each scenario.

---

## Part 5: Interventions

Model the effect of vaccination and social distancing.

```python
# --- Vaccination ---
def run_sir_vaccinated(N, I0, beta, gamma, vax_fraction, t_max=200):
    """Vaccinate a fraction of the population before the epidemic starts."""
    S0 = (N - I0) * (1 - vax_fraction)
    R0_init = (N - I0) * vax_fraction  # vaccinated go directly to R
    y0 = [S0, float(I0), R0_init]
    sol = solve_ivp(sir_ode, (0, t_max), y0, args=(beta, gamma, N),
                    t_eval=np.linspace(0, t_max, 2000), rtol=1e-8)
    return sol.t, sol.y[0], sol.y[1], sol.y[2]

R0_demo   = 3.0
beta_demo = R0_demo * gamma
vax_levels = np.linspace(0, 0.95, 20)
total_infected = []

for vax in vax_levels:
    t, S, I, R = run_sir_vaccinated(N, 10, beta_demo, gamma, vax)
    total_infected.append((R[-1] - N * vax) / N)  # subtract vaccinated from R

herd_threshold = 1 - 1 / R0_demo

plt.figure(figsize=(7, 4))
plt.plot(vax_levels * 100, [x * 100 for x in total_infected],
         'steelblue', linewidth=2)
plt.axvline(herd_threshold * 100, color='red', linestyle='--',
            label=f'Herd immunity threshold ({herd_threshold:.0%})')
plt.xlabel('Vaccination coverage (%)')
plt.ylabel('Population infected in epidemic (%)')
plt.title(f'Effect of Vaccination  (R₀ = {R0_demo})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sir_vaccination.png', dpi=100)
plt.show()
```

```python
# --- Social Distancing: temporary reduction of beta ---
def run_sir_distancing(N, I0, beta, gamma, beta_reduced, t_start, t_end, t_max=300):
    """Reduce beta between t_start and t_end (social distancing period)."""
    def ode(t, y):
        b = beta_reduced if t_start <= t <= t_end else beta
        return sir_ode(t, y, b, gamma, N)

    sol = solve_ivp(ode, (0, t_max), [N - I0, float(I0), 0.0],
                    t_eval=np.linspace(0, t_max, 3000), rtol=1e-8)
    return sol.t, sol.y[0], sol.y[1], sol.y[2]

beta_base = 2.0 * gamma
t, S0_arr, I_no, R0_arr = run_sir(N, 10, beta_base, gamma, t_max=300)
t_d, Sd, Id, Rd = run_sir_distancing(N, 10, beta_base, gamma,
                                      beta_reduced=0.5 * gamma,
                                      t_start=30, t_end=90, t_max=300)

plt.figure(figsize=(8, 5))
plt.plot(t, I_no / N * 100,  'tomato',    linewidth=2, label='No intervention')
plt.plot(t_d, Id / N * 100,  'steelblue', linewidth=2, label='Distancing: days 30–90')
plt.axvspan(30, 90, alpha=0.15, color='steelblue', label='Distancing period')
plt.xlabel('Day')
plt.ylabel('Infectious (% of population)')
plt.title('Effect of Social Distancing on Epidemic Curve')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sir_distancing.png', dpi=100)
plt.show()

print(f"Total infected without intervention: {R0_arr[-1]/N:.1%}")
print(f"Total infected with distancing:      {Rd[-1]/N:.1%}")
```

**Question 5.1:** Does social distancing (temporarily reducing β) reduce the *total* number infected, or only delay the epidemic? Under what conditions does it reduce the total, and under what conditions does it only "flatten the curve"?

**Question 5.2:** For measles (R₀ ≈ 15), what vaccination coverage is needed to achieve herd immunity? For COVID-19 (R₀ ≈ 3)? What does this imply for vaccine mandate policy?

---

## Deliverables

Submit a PDF or Jupyter notebook containing:

1. All labeled plots.
2. Written answers to all numbered questions.
3. A brief summary table: for each of R₀ = 1.5, 2.0, 3.0, 5.0, report the final epidemic size (% infected), the epidemic peak (% infected), and the herd immunity threshold.
4. **Reflection (1 paragraph):** The SIR model assumes a homogeneous, well-mixed population. Real epidemics spread on social networks. Describe two ways the SIR predictions might be wrong for a real city, and how you would modify the model to address each.
