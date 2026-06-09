# Lab 06: Predators, Prey, and Equilibrium — The Lotka-Volterra Model

**Course:** Applied Mathematics 50
**Companion to:** Case 06 (Ecology and Population Dynamics)
**Estimated time:** 2 hours
**Tools:** Python 3, NumPy, Matplotlib, SciPy

---

## Learning Goals

By the end of this lab you will be able to:
- Simulate the Lotka-Volterra predator-prey system using Euler's method and a built-in solver
- Visualize phase portraits and understand the conservation law
- Fit model parameters to the Hudson's Bay lynx-hare data
- Compare the classic model to the logistic extension and understand how carrying capacity changes dynamics

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

rng = np.random.default_rng(3)
```

---

## Part 1: Implementing the Lotka-Volterra System

### The Equations

$$\frac{dx}{dt} = \alpha x - \beta xy, \qquad \frac{dy}{dt} = \delta xy - \gamma y$$

where x = prey, y = predator.

```python
def lotka_volterra(t, state, alpha, beta, delta, gamma):
    """Lotka-Volterra predator-prey ODE system."""
    x, y = state
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

def run_lv(x0, y0, alpha, beta, delta, gamma, t_max=50, n_pts=5000):
    """Integrate the Lotka-Volterra system."""
    sol = solve_ivp(
        lotka_volterra, (0, t_max), [x0, y0],
        args=(alpha, beta, delta, gamma),
        t_eval=np.linspace(0, t_max, n_pts), rtol=1e-9
    )
    return sol.t, sol.y[0], sol.y[1]

# Parameters from Case 06 (arbitrary units)
alpha = 0.6   # prey growth rate
beta  = 0.02  # predation rate
delta = 0.01  # predator conversion efficiency
gamma = 0.4   # predator death rate

# Coexistence equilibrium
x_star = gamma / delta
y_star = alpha / beta
print(f"Coexistence equilibrium:  x* = {x_star:.1f},  y* = {y_star:.1f}")
print(f"Predicted oscillation period T = 2π/√(αγ) = {2*np.pi/np.sqrt(alpha*gamma):.2f} time units")

# Simulate from a perturbed initial condition
x0, y0 = x_star * 1.5, y_star * 0.8
t, x, y = run_lv(x0, y0, alpha, beta, delta, gamma, t_max=60)

fig, axes = plt.subplots(1, 2, figsize=(13, 4))
axes[0].plot(t, x, 'steelblue', linewidth=2, label='Prey (x)')
axes[0].plot(t, y, 'tomato',    linewidth=2, label='Predator (y)')
axes[0].axhline(x_star, color='steelblue', linestyle=':', alpha=0.5, label=f'x* = {x_star}')
axes[0].axhline(y_star, color='tomato',    linestyle=':', alpha=0.5, label=f'y* = {y_star}')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Population')
axes[0].set_title('Lotka-Volterra: Time Series')
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, y, 'purple', linewidth=1.5)
axes[1].plot(x[0], y[0], 'go', markersize=8, label='Start')
axes[1].plot(x_star, y_star, 'k*', markersize=14, label=f'Equilibrium ({x_star}, {y_star})')
axes[1].set_xlabel('Prey (x)')
axes[1].set_ylabel('Predator (y)')
axes[1].set_title('Phase Portrait')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lv_basic.png', dpi=100)
plt.show()
```

**Question 1.1:** The time series shows the predator peak *lags* behind the prey peak. Explain this biologically: why does the predator population peak after the prey population peaks?

**Question 1.2:** What is the approximate period of oscillation in your simulation? Compare to the theoretical prediction T = 2π/√(αγ). Do they agree?

---

## Part 2: The Conservation Law

The Lotka-Volterra system has a conserved quantity:

$$H(x, y) = \delta x - \gamma \ln x + \beta y - \alpha \ln y$$

```python
def conserved_H(x, y, alpha, beta, delta, gamma):
    """Compute the conservation law H(x, y)."""
    return delta * x - gamma * np.log(x) + beta * y - alpha * np.log(y)

# Verify H is constant along a trajectory
H_values = conserved_H(x, y, alpha, beta, delta, gamma)
H_range  = H_values.max() - H_values.min()
print(f"H along trajectory — max: {H_values.max():.6f},  min: {H_values.min():.6f}")
print(f"Variation in H (should be ~0): {H_range:.2e}")

plt.figure(figsize=(6, 3))
plt.plot(t, H_values - H_values[0], 'steelblue', linewidth=1.5)
plt.xlabel('Time')
plt.ylabel('H(t) − H(0)')
plt.title('Conservation Law: Deviation from Initial Value')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('lv_conservation.png', dpi=100)
plt.show()

# Plot level curves of H in the phase plane
x_grid = np.linspace(1, 200, 300)
y_grid = np.linspace(1, 100, 300)
X, Y = np.meshgrid(x_grid, y_grid)
H_grid = conserved_H(X, Y, alpha, beta, delta, gamma)

# Simulate several trajectories from different initial conditions
plt.figure(figsize=(7, 6))
plt.contour(X, Y, H_grid, levels=25, cmap='Blues', alpha=0.6)
for scale in [0.5, 0.8, 1.2, 1.8, 2.5]:
    t_, x_, y_ = run_lv(x_star * scale, y_star * (1/scale), alpha, beta, delta, gamma, t_max=80)
    plt.plot(x_, y_, linewidth=1.2)
plt.plot(x_star, y_star, 'k*', markersize=14, zorder=5, label=f'Equilibrium')
plt.xlabel('Prey (x)')
plt.ylabel('Predator (y)')
plt.title('Phase Portrait: Closed Orbits = Level Sets of H')
plt.legend()
plt.tight_layout()
plt.savefig('lv_phase_portrait.png', dpi=100)
plt.show()
```

**Question 2.1:** The level curves of H are the phase-plane trajectories. This is exactly analogous to conservation of energy in classical mechanics, where level curves of the Hamiltonian are trajectories. In that analogy, which is "kinetic energy" and which is "potential energy" — the prey or predator terms?

**Question 2.2:** In your simulation, H is not *exactly* constant because of numerical integration error. Does the error grow over time (indicating an unstable numerical method) or remain bounded? What does this imply about using Euler's method for long-time integration of Hamiltonian systems?

---

## Part 3: Volterra's Principle

Recall from Case 06: adding a harvesting term h (fishing) shifts the equilibrium. Here we verify this numerically.

```python
def lotka_volterra_harvested(t, state, alpha, beta, delta, gamma, h):
    """Lotka-Volterra with proportional harvesting rate h."""
    x, y = state
    dxdt = (alpha - h) * x - beta * x * y
    dydt =  delta * x * y - (gamma + h) * y
    return [dxdt, dydt]

harvest_rates = np.linspace(0, 0.25, 10)
x_eq_list, y_eq_list = [], []

for h in harvest_rates:
    alpha_eff = alpha - h
    gamma_eff = gamma + h
    if alpha_eff <= 0:
        break
    x_eq = gamma_eff / delta
    y_eq = alpha_eff / beta
    x_eq_list.append(x_eq)
    y_eq_list.append(y_eq)
    valid_h = h

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
valid_rates = harvest_rates[:len(x_eq_list)]
axes[0].plot(valid_rates, x_eq_list, 'steelblue', linewidth=2, marker='o', label='Prey equilibrium x*')
axes[0].set_xlabel('Harvesting rate h')
axes[0].set_ylabel('Equilibrium population x* = (γ+h)/δ')
axes[0].set_title("Volterra's Principle: Effect on Prey")
axes[0].grid(True, alpha=0.3)

axes[1].plot(valid_rates, y_eq_list, 'tomato', linewidth=2, marker='o', label='Predator equilibrium y*')
axes[1].set_xlabel('Harvesting rate h')
axes[1].set_ylabel('Equilibrium population y* = (α−h)/β')
axes[1].set_title("Volterra's Principle: Effect on Predator")
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('volterra_principle.png', dpi=100)
plt.show()

print(f"No harvesting (h=0):  prey* = {gamma/delta:.1f},  predator* = {alpha/beta:.1f}")
print(f"With harvesting h=0.2: prey* = {(gamma+0.2)/delta:.1f},  predator* = {(alpha-0.2)/beta:.1f}")
```

**Question 3.1:** Volterra's principle says fishing *increases* prey equilibrium and *decreases* predator equilibrium. Does this seem counterintuitive? Explain the mechanism: why does reducing all populations benefit prey relative to predators?

**Question 3.2:** Now numerically simulate the full ODE with h = 0 and h = 0.2, starting from the same initial condition. Plot both time series on the same graph. Does the time-averaged population in the simulation match the equilibrium prediction from Volterra's principle?

---

## Part 4: Fitting to Lynx-Hare Data

```python
# Hudson's Bay Company data (approximate, thousands)
years_data  = np.array([1845, 1850, 1855, 1860, 1865, 1875, 1885, 1895, 1905])
hare_data   = np.array([20,   100,    8,   80,   10,   80,    8,  100,   20])
lynx_data   = np.array([30,     4,   45,    6,   70,    4,   45,    4,   30])

plt.figure(figsize=(9, 4))
plt.plot(years_data, hare_data, 'o-', color='steelblue', linewidth=2, label='Snowshoe hare (thousands)')
plt.plot(years_data, lynx_data, 's-', color='tomato',    linewidth=2, label='Lynx (thousands)')
plt.xlabel('Year')
plt.ylabel('Population (thousands)')
plt.title('Hudson\'s Bay Company Fur Trade Data, 1845–1905')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('lynx_hare_data.png', dpi=100)
plt.show()

# Estimate parameters from the data
# Period ~10 years, so T = 2π/√(αγ) = 10  =>  αγ = (2π/10)²
T_observed = 10.0  # years
alpha_data  = 0.4  # hare doubling ~2 years
gamma_data  = (2 * np.pi / T_observed)**2 / alpha_data
print(f"Estimated γ = {gamma_data:.4f} yr⁻¹")

# From equilibrium populations
x_star_data = 30.0   # thousand hares
y_star_data  =  4.0  # thousand lynx
beta_data  = alpha_data / y_star_data
delta_data = gamma_data / x_star_data
print(f"Estimated β = {beta_data:.4f},  δ = {delta_data:.6f}")
print(f"Coexistence equilibrium: ({x_star_data}, {y_star_data}) — by construction")

# Simulate with estimated parameters
t_lv, x_lv, y_lv = run_lv(
    x0=20.0, y0=30.0,
    alpha=alpha_data, beta=beta_data,
    delta=delta_data, gamma=gamma_data,
    t_max=60, n_pts=3000
)

# Align time axis to data (start at 1845)
t_years = t_lv + 1845

fig, axes = plt.subplots(1, 2, figsize=(14, 4))
axes[0].plot(t_years, x_lv, 'steelblue', linewidth=2, label='Hare (model)')
axes[0].plot(t_years, y_lv, 'tomato',    linewidth=2, label='Lynx (model)')
axes[0].plot(years_data, hare_data, 'o', color='steelblue', markersize=7)
axes[0].plot(years_data, lynx_data, 's', color='tomato',    markersize=7)
axes[0].set_xlim(1845, 1910)
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Population (thousands)')
axes[0].set_title('Lotka-Volterra Fit to Lynx-Hare Data')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(x_lv, y_lv, 'purple', linewidth=1.5, label='Model trajectory')
axes[1].plot(hare_data, lynx_data, 'ko-', markersize=6, label='Data')
axes[1].set_xlabel('Hare (thousands)')
axes[1].set_ylabel('Lynx (thousands)')
axes[1].set_title('Phase Portrait: Model vs. Data')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lynx_hare_fit.png', dpi=100)
plt.show()
```

**Question 4.1:** How well does the model fit the data? Describe qualitatively: does it capture the period, amplitude, and phase relationships between lynx and hare?

**Question 4.2:** The Lotka-Volterra model predicts *exactly* periodic oscillations. Real population data shows irregular oscillations. What biological factors might cause irregularity, and how would you modify the model to incorporate them?

---

## Part 5: Logistic Prey — Effect of Carrying Capacity

```python
def logistic_lv(t, state, alpha, beta, delta, gamma, K):
    """Lotka-Volterra with logistic prey growth."""
    x, y = state
    dxdt = alpha * x * (1 - x / K) - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

def run_logistic_lv(x0, y0, alpha, beta, delta, gamma, K, t_max=150):
    sol = solve_ivp(
        logistic_lv, (0, t_max), [x0, y0],
        args=(alpha, beta, delta, gamma, K),
        t_eval=np.linspace(0, t_max, 5000), rtol=1e-9
    )
    return sol.t, sol.y[0], sol.y[1]

# Compare different carrying capacities
K_values = [50, 100, 150, 300]
fig, axes = plt.subplots(2, 2, figsize=(13, 8))

for ax, K in zip(axes.flatten(), K_values):
    t_log, x_log, y_log = run_logistic_lv(
        x0=40, y0=10,
        alpha=alpha_data, beta=beta_data,
        delta=delta_data, gamma=gamma_data, K=K
    )
    ax.plot(t_log, x_log, 'steelblue', linewidth=1.5, label='Hare')
    ax.plot(t_log, y_log, 'tomato',    linewidth=1.5, label='Lynx')
    x_eq_log = gamma_data / delta_data
    y_eq_log = alpha_data / beta_data * (1 - x_eq_log / K) if K > x_eq_log else 0
    ax.axhline(x_eq_log, color='steelblue', linestyle=':', alpha=0.5)
    ax.axhline(y_eq_log, color='tomato',    linestyle=':', alpha=0.5)
    ax.set_title(f'K = {K} thousand hares')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population (thousands)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 150)

plt.suptitle('Effect of Prey Carrying Capacity on Population Dynamics', y=1.01)
plt.tight_layout()
plt.savefig('logistic_lv_K.png', dpi=100)
plt.show()
```

**Question 5.1:** For small K (K = 50), what happens to the populations? For large K (K = 300)? Is there a critical value of K where the qualitative behavior changes?

**Question 5.2:** For K = 150, do the oscillations damp out toward the equilibrium, or persist forever? Compare to the pure Lotka-Volterra model (which oscillates forever). Why does adding a carrying capacity change the stability of the equilibrium?

```python
# Phase portraits for different K
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, K in zip(axes, K_values):
    t_log, x_log, y_log = run_logistic_lv(
        x0=40, y0=10,
        alpha=alpha_data, beta=beta_data,
        delta=delta_data, gamma=gamma_data, K=K, t_max=200
    )
    ax.plot(x_log, y_log, 'purple', linewidth=1, alpha=0.8)
    ax.plot(x_log[0], y_log[0], 'go', markersize=7, label='Start')
    ax.plot(x_log[-1], y_log[-1], 'rs', markersize=7, label='End')
    ax.set_title(f'K = {K}')
    ax.set_xlabel('Prey (x)')
    ax.set_ylabel('Predator (y)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

plt.suptitle('Phase Portraits: Logistic Lotka-Volterra for Different K', y=1.02)
plt.tight_layout()
plt.savefig('logistic_phase_portraits.png', dpi=100)
plt.show()
```

**Question 5.3:** The phase portrait for intermediate K shows a spiral converging to the equilibrium. What does the shape of the spiral tell you about the *rate* of convergence (slow or fast)? How would you estimate the damping time from the figure?

---

## Deliverables

Submit a PDF or Jupyter notebook containing:

1. All labeled plots (time series, phase portraits, conservation law, Volterra's principle, lynx-hare fit, logistic comparisons).
2. Answers to all numbered questions.
3. A table: for each K ∈ {50, 100, 150, 300}, state whether the long-run behavior is extinction, periodic oscillation, or damped oscillation, and estimate the equilibrium population of each species.
4. **Reflection (1 paragraph):** The Lotka-Volterra model is deterministic — given exact initial conditions, the future is perfectly predictable. Real ecosystems have stochastic events (droughts, disease outbreaks, random birth and death). Describe one way stochasticity might change the predictions of the model, and how you would introduce randomness into the simulation.
