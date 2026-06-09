# Lab 02: The Math of Winning — Run Expectancy, Hot Hands, and Optimal Sprinting

**Course:** Applied Mathematics 50
**Companion to:** Case 02 (Sports Analytics)
**Estimated time:** 2 hours
**Tools:** Python 3, NumPy, Matplotlib, SciPy

---

## Learning Goals

By the end of this lab you will be able to:
- Build a Markov chain for a simplified baseball game and solve for run expectancy
- Simulate coin-flip sequences to discover the Miller-Sanjurjo bias by experiment
- Numerically solve the Keller sprinting ODE and find the optimal race strategy

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from scipy.integrate import solve_ivp

rng = np.random.default_rng(0)
```

---

## Part 1: Run Expectancy via Markov Chains

### The Model

We consider a simplified baseball half-inning with three states:
- **State 0:** Runner on first base, 0 outs
- **State 1:** Runner on second base, 0 outs
- **State 2:** Inning over (absorbing state — no more runs possible)

Each plate appearance has three outcomes:
- **Out** (probability 0.70): outs increase by 1; for simplicity, a third out ends the inning
- **Single** (probability 0.20): batter reaches first; runner advances one base
- **Home run** (probability 0.10): batter and all runners score

The immediate run values r[s] are the runs scored on the transition *into* a new state.

### Building the Transition Matrix

```python
# States: 0 = runner on 1st (0 outs), 1 = runner on 2nd (0 outs), 2 = inning over
# Transition matrix P[i, j] = probability of going from state i to state j
# Immediate reward r[i] = expected runs scored on leaving state i

p_out    = 0.70
p_single = 0.20
p_homer  = 0.10

# From State 0 (runner on 1st, 0 outs):
#   Out     -> State 2 (inning over for simplicity), 0 runs
#   Single  -> State 0 (runner on 1st, batter arrived; original runner on 2nd -> simplify to State 1), 0 runs
#   Homer   -> State 2 (inning over, but 2 runs scored), 2 runs
# We simplify: single from state 0 -> state 1 (runner advances to 2nd)

P = np.array([
    # to S0,      to S1,      to S2
    [0.0,         p_single,   p_out + p_homer],   # from State 0
    [p_single,    0.0,        p_out + p_homer],   # from State 1
    [0.0,         0.0,        1.0             ],   # from State 2 (absorbing)
])

# Immediate runs scored when leaving each state
r_immediate = np.array([
    p_homer * 2,           # State 0: homer scores 2 (batter + runner)
    p_homer * 2 + p_homer, # State 1: homer scores 2 (batter + runner on 2nd)
    0.0,                   # State 2: absorbing, no more runs
])
# Simplify: state 1 runner on 2nd, homer scores batter + runner = 2
r_immediate = np.array([p_homer * 2, p_homer * 2, 0.0])

print("Transition matrix P:")
print(P)
print("\nImmediate run rewards r:")
print(r_immediate)
```

### Solving for Run Expectancy

The run expectancy vector RE satisfies the Bellman equation:

**RE = r + P · RE**

Rearranging: **(I − P) RE = r**

```python
n_states = 3
I = np.eye(n_states)
A = I - P

# Solve (I - P) RE = r
RE = solve(A, r_immediate)

print("\nRun Expectancy by state:")
print(f"  State 0 (runner on 1st, 0 outs): {RE[0]:.3f} expected runs")
print(f"  State 1 (runner on 2nd, 0 outs): {RE[1]:.3f} expected runs")
print(f"  State 2 (inning over):            {RE[2]:.3f} expected runs")
```

**Question 1.1:** Which state has higher run expectancy — runner on first or runner on second? By how much? Does the magnitude surprise you?

### Stolen Base Decision

A stolen base attempt transitions the runner from State 0 to State 1 (success) or increases the out count (failure, simplify as inning over).

```python
def breakeven_steal(RE, state_success, state_fail, p_success):
    """
    Compute net value of stealing given a success probability.
    Returns: (net_value, break_even_probability)
    """
    gain = RE[state_success] - RE[0]   # value gained on success
    loss = RE[state_fail]   - RE[0]    # value lost on failure (negative)

    # Break-even: p * gain + (1-p) * loss = 0  =>  p* = -loss / (gain - loss)
    p_star = (-loss) / (gain - loss)
    net_value = p_success * gain + (1 - p_success) * loss
    return net_value, p_star

# Assume runner succeeds 70% of the time
p_success = 0.70
net_val, p_star = breakeven_steal(RE, state_success=1, state_fail=2, p_success=p_success)

print(f"\nStolen base analysis:")
print(f"  Break-even success rate: {p_star:.1%}")
print(f"  Net value at 70% success: {net_val:+.3f} runs")
print(f"  Decision: {'Steal!' if net_val > 0 else 'Stay.'}")

# Plot net value vs. success probability
p_range = np.linspace(0, 1, 100)
net_values = [p * (RE[1] - RE[0]) + (1 - p) * (RE[2] - RE[0]) for p in p_range]

plt.figure(figsize=(6, 4))
plt.plot(p_range, net_values, 'steelblue', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(p_star, color='red', linewidth=1.5, linestyle=':', label=f'Break-even = {p_star:.1%}')
plt.xlabel('Stolen base success probability')
plt.ylabel('Net run value')
plt.title('Value of a Stolen Base Attempt')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('stolen_base_value.png', dpi=100)
plt.show()
```

**Question 1.2:** If an average baserunner succeeds on 68% of steal attempts, should they attempt the steal in this model? What would a manager need to believe about the runner's ability to justify the attempt?

**Question 1.3:** Real MLB data puts the break-even stolen base success rate at around 72–75%. How does your simplified model compare? What features of the model might cause it to underestimate or overestimate this threshold?

---

## Part 2: The Hot Hand — Discovering a Bias by Simulation

The Miller-Sanjurjo result says: if you flip a fair coin N times and look only at flips that *follow* a streak of k heads, the expected fraction of heads among those next flips is *less than* 50%, even though the coin is fair.

We will discover this bias experimentally.

```python
def conditional_hit_rate(sequence, k):
    """
    In `sequence` (list of 0/1), find all positions i where
    positions i-k through i-1 are all 1. Return the fraction of
    such positions i where sequence[i] is also 1.
    """
    n = len(sequence)
    qualifying = []
    for i in range(k, n):
        if all(sequence[i - j - 1] == 1 for j in range(k)):
            qualifying.append(sequence[i])
    if len(qualifying) == 0:
        return np.nan
    return np.mean(qualifying)

# Simulate many sequences of N fair coin flips
N_flips = 20
N_sims  = 50_000
k       = 3   # streak length to condition on

rates = []
for _ in range(N_sims):
    seq = rng.integers(0, 2, size=N_flips).tolist()
    rate = conditional_hit_rate(seq, k)
    if not np.isnan(rate):
        rates.append(rate)

mean_rate = np.mean(rates)
print(f"Simulated conditional hit rate after k={k} consecutive heads:")
print(f"  Mean = {mean_rate:.4f}  (expected 0.5 if no bias)")
print(f"  Bias = {mean_rate - 0.5:+.4f}")

plt.figure(figsize=(6, 4))
plt.hist(rates, bins=30, color='steelblue', edgecolor='white', density=True)
plt.axvline(0.5, color='red', linewidth=2, label='Fair coin (0.50)')
plt.axvline(mean_rate, color='orange', linewidth=2, linestyle='--',
            label=f'Simulated mean ({mean_rate:.3f})')
plt.xlabel('Conditional hit rate after 3 consecutive heads')
plt.ylabel('Density')
plt.title(f'Miller-Sanjurjo Bias: N={N_flips} flips, k={k}')
plt.legend()
plt.tight_layout()
plt.savefig('hot_hand_bias.png', dpi=100)
plt.show()
```

**Question 2.1:** Is the simulated mean significantly below 0.50? Run the simulation for k = 1, 2, 3, 4. How does the bias change with k?

```python
# Explore bias as a function of k and N
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Vary k (fixed N = 20)
ks = [1, 2, 3, 4, 5]
biases_k = []
for k in ks:
    rates = [conditional_hit_rate(rng.integers(0, 2, size=20).tolist(), k)
             for _ in range(20_000)]
    rates = [r for r in rates if not np.isnan(r)]
    biases_k.append(np.mean(rates) - 0.5)

axes[0].bar(ks, biases_k, color='steelblue')
axes[0].axhline(0, color='black', linewidth=0.8)
axes[0].set_xlabel('Streak length k')
axes[0].set_ylabel('Bias (mean − 0.50)')
axes[0].set_title('Bias vs. Streak Length (N=20 flips)')

# Vary N (fixed k = 3)
Ns = [10, 20, 50, 100, 200]
biases_N = []
for N in Ns:
    rates = [conditional_hit_rate(rng.integers(0, 2, size=N).tolist(), 3)
             for _ in range(10_000)]
    rates = [r for r in rates if not np.isnan(r)]
    biases_N.append(np.mean(rates) - 0.5)

axes[1].plot(Ns, biases_N, 'o-', color='steelblue', linewidth=2)
axes[1].axhline(0, color='black', linewidth=0.8)
axes[1].set_xlabel('Sequence length N')
axes[1].set_ylabel('Bias (mean − 0.50)')
axes[1].set_title('Bias vs. Sequence Length (k=3)')

plt.tight_layout()
plt.savefig('hot_hand_bias_sensitivity.png', dpi=100)
plt.show()
```

**Question 2.2:** What happens to the bias as N → ∞? Interpret: does the original Gilovich-Tversky study (N ≈ 100 shots per player) have enough data to detect a real hot-hand effect even after correcting for the bias?

**Question 2.3:** This bias arises purely from a mathematical property of finite sequences, with no psychology involved. What does this tell us about the difficulty of detecting patterns in noisy data?

---

## Part 3: The Keller Sprinting Model

### The ODE

The Keller model for a sprinter:

**dv/dt = f(t) − v/τ**

where v(t) is speed, f(t) is the propulsive force per unit mass, and τ = 1 s is a resistance constant.

The optimal strategy for a short race (≤ 400 m) is: apply maximum force f_max for the entire race.

```python
# Parameters (roughly calibrated to elite 100m sprinters)
tau     = 1.0          # resistance time constant (s)
f_max   = 12.2         # maximum propulsive force (m/s²)
v0      = 0.0          # start from rest

def keller_ode(t, state, f):
    """state = [v, x]; f = propulsive force (m/s²)"""
    v, x = state
    dvdt = f - v / tau
    dxdt = v
    return [dvdt, dxdt]

# Solve for a 100m sprint at maximum force
t_span = (0, 15)
t_eval = np.linspace(0, 15, 500)
sol = solve_ivp(keller_ode, t_span, [v0, 0], args=(f_max,),
                t_eval=t_eval, dense_output=True)

# Find finish time (when x = 100)
x = sol.y[1]
v = sol.y[0]
t = sol.t

finish_idx = np.searchsorted(x, 100)
if finish_idx < len(t):
    t_finish = t[finish_idx]
    v_finish = v[finish_idx]
    print(f"100m finish time: {t_finish:.2f} s")
    print(f"Speed at finish:  {v_finish:.2f} m/s ({v_finish * 3.6:.1f} km/h)")

# Plot velocity and position
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(t, v, 'steelblue', linewidth=2)
axes[0].axvline(t_finish, color='red', linestyle='--', label=f'Finish at {t_finish:.2f}s')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Speed (m/s)')
axes[0].set_title('Sprint Speed vs. Time (100m)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(t, x, 'steelblue', linewidth=2)
axes[1].axhline(100, color='red', linestyle='--', label='100m mark')
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Distance (m)')
axes[1].set_title('Sprint Distance vs. Time')
axes[1].legend()
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sprint_100m.png', dpi=100)
plt.show()
```

**Question 3.1:** What is the terminal velocity the model predicts (the speed approached as t → ∞)? Derive this analytically from the ODE by setting dv/dt = 0. Does it match your simulation?

### Analytical Solution

The ODE dv/dt = f − v/τ is a first-order linear ODE (Math 1b Unit 5.3). Solve it:

```python
# Analytical solution: v(t) = f_max * tau * (1 - exp(-t/tau))
t_ana = np.linspace(0, 15, 500)
v_ana = f_max * tau * (1 - np.exp(-t_ana / tau))

plt.figure(figsize=(6, 4))
plt.plot(t, v, 'steelblue', linewidth=3, label='Numerical (solve_ivp)')
plt.plot(t_ana, v_ana, 'r--', linewidth=2, label='Analytical solution')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.title('Keller Model: Numerical vs. Analytical Solution')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sprint_analytical.png', dpi=100)
plt.show()
```

**Question 3.2:** Verify analytically that v(t) = f_max · τ · (1 − e^(−t/τ)) solves the ODE with v(0) = 0. Show your work.

### Comparing Race Distances

```python
distances = [100, 200, 400]
colors = ['steelblue', 'orange', 'green']

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

for dist, color in zip(distances, colors):
    # Solve until the runner covers `dist` meters
    sol = solve_ivp(keller_ode, (0, 120), [0, 0], args=(f_max,),
                    t_eval=np.linspace(0, 120, 5000))
    x_arr = sol.y[1]
    v_arr = sol.y[0]
    t_arr = sol.t

    idx = np.searchsorted(x_arr, dist)
    if idx < len(t_arr):
        t_fin = t_arr[idx]
        avg_speed = dist / t_fin
        axes[0].bar(str(dist) + 'm', t_fin, color=color, label=f'{dist}m: {t_fin:.1f}s')
        axes[1].bar(str(dist) + 'm', avg_speed, color=color, label=f'{dist}m: {avg_speed:.2f} m/s')

axes[0].set_ylabel('Finish Time (s)')
axes[0].set_title('Predicted Finish Times')
axes[1].set_ylabel('Average Speed (m/s)')
axes[1].set_title('Average Speed by Race Distance')
plt.tight_layout()
plt.savefig('sprint_distances.png', dpi=100)
plt.show()
```

**Question 3.3:** The model predicts that a 400m runner maintains approximately constant speed after the initial acceleration. Real 400m runners show a significant slowdown in the final 100m. What physical phenomenon does the model omit that would explain this?

**Question 3.4 (Extension):** Modify the ODE to include a time-varying maximum force: f_max(t) = f_max · e^(−t/T_fatigue), where T_fatigue = 60 s. How does this change the predicted 400m time? Adjust T_fatigue to match the world record of 43.03 s.

---

## Deliverables

Submit a PDF or Jupyter notebook containing:

1. All plots with brief captions.
2. Written answers to all numbered questions.
3. A table summarizing: break-even steal % from the Markov model, hot-hand bias for k = 1, 2, 3, 4, analytical terminal velocity for the Keller model.
4. **Reflection (1 paragraph):** Each of the three models in this lab involves a different type of approximation or simplification. Identify one key simplification in each model and explain what additional data or more complex model would be needed to address it.
