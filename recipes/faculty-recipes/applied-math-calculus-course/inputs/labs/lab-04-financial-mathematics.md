# Lab 04: Pricing the Future — Simulating Stock Prices and Options

**Course:** Applied Mathematics 50
**Companion to:** Case 04 (Financial Mathematics)
**Estimated time:** 2 hours
**Tools:** Python 3, NumPy, Matplotlib, SciPy

---

## Learning Goals

By the end of this lab you will be able to:
- Simulate geometric Brownian motion as a model of stock price evolution
- Compute Black-Scholes option prices using the closed-form formula
- Price options using Monte Carlo simulation and compare to the formula
- Explore the "Greeks" (sensitivities) and the volatility smile

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

rng = np.random.default_rng(42)
```

---

## Part 1: Simulating Stock Prices

### Geometric Brownian Motion

A stock following geometric Brownian motion has the exact solution:

$$S(t) = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W(t)\right]$$

where W(t) is a standard Brownian motion (W(t) ~ N(0, t)).

To simulate a discrete path with time step Δt:

$$S(t + \Delta t) = S(t) \cdot \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)\Delta t + \sigma \sqrt{\Delta t}\, Z\right], \quad Z \sim N(0,1)$$

```python
def simulate_gbm(S0, mu, sigma, T, n_steps, n_paths, rng):
    """
    Simulate geometric Brownian motion.
    Returns array of shape (n_paths, n_steps+1).
    """
    dt = T / n_steps
    drift  = (mu - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt)

    Z = rng.standard_normal((n_paths, n_steps))
    log_increments = drift + diffusion * Z

    log_paths = np.concatenate(
        [np.zeros((n_paths, 1)), np.cumsum(log_increments, axis=1)],
        axis=1
    )
    return S0 * np.exp(log_paths)

# Parameters
S0    = 100.0   # initial stock price ($)
mu    = 0.08    # expected annual return (8%)
sigma = 0.20    # annual volatility (20%)
T     = 1.0     # time horizon (1 year)
n_steps = 252   # daily steps

paths = simulate_gbm(S0, mu, sigma, T, n_steps, n_paths=500, rng=rng)
t_grid = np.linspace(0, T, n_steps + 1)

plt.figure(figsize=(9, 5))
plt.plot(t_grid, paths[:50].T, alpha=0.3, linewidth=0.7, color='steelblue')
plt.plot(t_grid, np.median(paths, axis=0), 'k-', linewidth=2, label='Median path')
plt.axhline(S0, color='red', linestyle='--', linewidth=1, label=f'S₀ = ${S0}')
plt.xlabel('Time (years)')
plt.ylabel('Stock price ($)')
plt.title(f'Geometric Brownian Motion: 50 of 500 simulated paths\n(μ={mu:.0%}, σ={sigma:.0%})')
plt.legend()
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig('gbm_paths.png', dpi=100)
plt.show()
```

**Question 1.1:** Plot the distribution of final stock prices S(T). Does it look symmetric or skewed? The case reading says S(T) follows a lognormal distribution. Overlay the theoretical lognormal PDF and comment on the fit.

```python
# Distribution of final prices
S_final = paths[:, -1]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left: histogram of S(T)
axes[0].hist(S_final, bins=50, density=True, color='steelblue', alpha=0.7, edgecolor='white')
from scipy.stats import lognorm
mean_log = np.log(S0) + (mu - 0.5 * sigma**2) * T
std_log  = sigma * np.sqrt(T)
x_range  = np.linspace(S_final.min(), S_final.max(), 300)
axes[0].plot(x_range, lognorm.pdf(x_range, s=std_log, scale=np.exp(mean_log)),
             'r-', linewidth=2, label='Theoretical lognormal')
axes[0].set_xlabel('S(T)')
axes[0].set_ylabel('Density')
axes[0].set_title('Distribution of Final Stock Price')
axes[0].legend()

# Right: histogram of log returns
log_returns = np.log(S_final / S0)
from scipy.stats import norm as norm_dist
axes[1].hist(log_returns, bins=50, density=True, color='tomato', alpha=0.7, edgecolor='white')
lr_range = np.linspace(log_returns.min(), log_returns.max(), 300)
axes[1].plot(lr_range, norm_dist.pdf(lr_range, loc=(mu - 0.5*sigma**2)*T,
                                      scale=sigma*np.sqrt(T)),
             'k-', linewidth=2, label='Theoretical normal')
axes[1].set_xlabel('log(S(T)/S₀)')
axes[1].set_ylabel('Density')
axes[1].set_title('Distribution of Log Return')
axes[1].legend()

plt.tight_layout()
plt.savefig('gbm_distribution.png', dpi=100)
plt.show()

print(f"Simulated mean S(T):   ${S_final.mean():.2f}  (theoretical: ${S0 * np.exp(mu * T):.2f})")
print(f"Simulated median S(T): ${np.median(S_final):.2f}")
```

**Question 1.2:** Why is the mean of S(T) larger than the median? What does this say about the "average" outcome vs. the "typical" outcome for a stock investment?

---

## Part 2: Black-Scholes Formula

```python
def black_scholes_call(S0, K, T, r, sigma):
    """European call option price via Black-Scholes."""
    if T <= 0 or sigma <= 0:
        return max(S0 - K, 0.0)
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return price, d1, d2

def black_scholes_put(S0, K, T, r, sigma):
    """European put option price via put-call parity."""
    call, d1, d2 = black_scholes_call(S0, K, T, r, sigma)
    put = call - S0 + K * np.exp(-r * T)
    return put

# Base case from Case 04
S0_ex = 100.0
K_ex  = 105.0
T_ex  = 1.0
r_ex  = 0.05
sig_ex = 0.20

C, d1, d2 = black_scholes_call(S0_ex, K_ex, T_ex, r_ex, sig_ex)
P = black_scholes_put(S0_ex, K_ex, T_ex, r_ex, sig_ex)

print(f"Black-Scholes Call Price: ${C:.4f}")
print(f"Black-Scholes Put  Price: ${P:.4f}")
print(f"\nd₁ = {d1:.4f},  N(d₁) = {norm.cdf(d1):.4f}  (delta)")
print(f"d₂ = {d2:.4f},  N(d₂) = {norm.cdf(d2):.4f}  (risk-neutral prob. in-the-money)")
```

**Question 2.1:** N(d₂) is the risk-neutral probability that the option expires in the money (S(T) > K). What is this probability for our base case? Does it make intuitive sense given that K > S₀?

**Question 2.2:** Compute the price of a *put* option (right to *sell* at K = $105). Which is worth more, the call or the put? Explain intuitively why.

---

## Part 3: Monte Carlo Option Pricing

We can also price the call by simulating many stock paths and averaging the payoff.

```python
def monte_carlo_call(S0, K, T, r, sigma, n_sims, rng):
    """Price a European call via Monte Carlo simulation."""
    # Simulate final stock prices under risk-neutral measure (mu = r)
    Z = rng.standard_normal(n_sims)
    S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoffs = np.maximum(S_T - K, 0)
    price = np.exp(-r * T) * np.mean(payoffs)
    std_err = np.exp(-r * T) * np.std(payoffs) / np.sqrt(n_sims)
    return price, std_err

# Price with increasing number of simulations
n_sim_list = [100, 500, 1000, 5000, 10_000, 50_000, 100_000]
mc_prices, mc_errors = [], []

for n in n_sim_list:
    price, se = monte_carlo_call(S0_ex, K_ex, T_ex, r_ex, sig_ex, n, rng)
    mc_prices.append(price)
    mc_errors.append(se)

plt.figure(figsize=(8, 5))
plt.errorbar(n_sim_list, mc_prices, yerr=[2*e for e in mc_errors],
             fmt='o-', color='steelblue', capsize=4, label='MC price ± 2σ')
plt.axhline(C, color='red', linewidth=2, linestyle='--', label=f'Black-Scholes: ${C:.4f}')
plt.xscale('log')
plt.xlabel('Number of simulations')
plt.ylabel('Estimated call price ($)')
plt.title('Monte Carlo vs. Black-Scholes Option Price')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('monte_carlo_convergence.png', dpi=100)
plt.show()
```

**Question 3.1:** How many simulations are needed before the Monte Carlo price is within $0.10 of the Black-Scholes price? How does the error scale with the number of simulations? (Hint: look at the standard error formula — how does it depend on n?)

**Question 3.2:** The key difference between Part 1 and Part 3 is that in Monte Carlo pricing we use μ = r (the risk-free rate) instead of the actual expected return μ = 8%. Why? (This is the "risk-neutral pricing" argument from the case reading.)

---

## Part 4: Sensitivity Analysis — The Greeks

```python
def compute_greeks(S0, K, T, r, sigma, dS=0.01, dsig=0.001, dT=1/365):
    """Numerically estimate option Greeks."""
    C_base = black_scholes_call(S0, K, T, r, sigma)[0]

    # Delta: ∂C/∂S
    delta = (black_scholes_call(S0 + dS*S0, K, T, r, sigma)[0] -
             black_scholes_call(S0 - dS*S0, K, T, r, sigma)[0]) / (2 * dS * S0)

    # Vega: ∂C/∂σ (per 1% change in vol)
    vega  = (black_scholes_call(S0, K, T, r, sigma + dsig)[0] -
             black_scholes_call(S0, K, T, r, sigma - dsig)[0]) / (2 * dsig) * 0.01

    # Theta: ∂C/∂T (per day, note: decreasing T means losing value)
    theta = (black_scholes_call(S0, K, T - dT, r, sigma)[0] -
             black_scholes_call(S0, K, T,       r, sigma)[0]) / dT * dT  # per day

    return {'price': C_base, 'delta': delta, 'vega': vega, 'theta': theta}

greeks = compute_greeks(S0_ex, K_ex, T_ex, r_ex, sig_ex)
print("Option Greeks (base case):")
for k, v in greeks.items():
    print(f"  {k:8s} = {v:.4f}")

# Plot Delta and Price as functions of S0
S_range = np.linspace(60, 160, 200)
prices  = [black_scholes_call(s, K_ex, T_ex, r_ex, sig_ex)[0] for s in S_range]
deltas  = [compute_greeks(s, K_ex, T_ex, r_ex, sig_ex)['delta'] for s in S_range]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(S_range, prices, 'steelblue', linewidth=2, label='Call price')
axes[0].plot(S_range, np.maximum(S_range - K_ex, 0), 'r--', linewidth=1.5, label='Intrinsic value')
axes[0].axvline(K_ex, color='gray', linestyle=':', label=f'Strike K=${K_ex}')
axes[0].set_xlabel('Stock price S₀ ($)')
axes[0].set_ylabel('Call price ($)')
axes[0].set_title('Call Price vs. Stock Price')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(S_range, deltas, 'tomato', linewidth=2)
axes[1].axvline(K_ex, color='gray', linestyle=':')
axes[1].axhline(0.5, color='black', linestyle='--', linewidth=0.8, label='Δ = 0.5')
axes[1].set_xlabel('Stock price S₀ ($)')
axes[1].set_ylabel('Delta (∂C/∂S)')
axes[1].set_title('Option Delta vs. Stock Price')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('option_greeks.png', dpi=100)
plt.show()
```

**Question 4.1:** Delta measures how much the option price changes per $1 change in the stock price. For a deeply in-the-money option (S₀ >> K), what does Δ approach? For a deeply out-of-the-money option (S₀ << K)? Explain the intuition.

**Question 4.2:** Theta is negative (options lose value as expiration approaches, all else equal). Why is this the case? Under what circumstances would you *want* to hold a short-maturity option vs. a long-maturity option?

---

## Part 5: The Volatility Smile

In the real market, options with different strike prices trade at *implied volatilities* that are not constant — a phenomenon called the **volatility smile** (or smirk). Here we explore what happens when σ varies.

```python
# Plot option price and implied vol surface
strikes = np.linspace(70, 140, 100)
sigmas  = [0.10, 0.20, 0.30, 0.40]

plt.figure(figsize=(8, 5))
for sig in sigmas:
    prices_k = [black_scholes_call(S0_ex, K, T_ex, r_ex, sig)[0] for K in strikes]
    plt.plot(strikes, prices_k, linewidth=2, label=f'σ = {sig:.0%}')

plt.axvline(S0_ex, color='gray', linestyle=':', label=f'S₀ = ${S0_ex}')
plt.xlabel('Strike price K ($)')
plt.ylabel('Call price ($)')
plt.title('Black-Scholes Call Price for Different Volatilities')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('vol_surface.png', dpi=100)
plt.show()

# Simulate the implied volatility smile from a Student-t model
from scipy.optimize import brentq

def implied_vol(market_price, S0, K, T, r):
    """Back out implied vol from a market price using Black-Scholes."""
    try:
        return brentq(
            lambda sig: black_scholes_call(S0, K, T, r, sig)[0] - market_price,
            1e-4, 5.0
        )
    except ValueError:
        return np.nan

# Generate "market prices" from a fat-tailed (Student-t) distribution
from scipy.stats import t as student_t
df_t = 5  # degrees of freedom — fatter tails than normal

n_mc = 200_000
Z_fat = student_t.rvs(df=df_t, size=n_mc, random_state=42)
# Rescale so variance matches GBM
Z_fat = Z_fat / np.sqrt(df_t / (df_t - 2))
S_T_fat = S0_ex * np.exp((r_ex - 0.5 * sig_ex**2) * T_ex + sig_ex * np.sqrt(T_ex) * Z_fat)

strikes_smile = np.arange(75, 135, 5)
impl_vols = []

for K in strikes_smile:
    payoffs = np.maximum(S_T_fat - K, 0)
    mkt_price = np.exp(-r_ex * T_ex) * np.mean(payoffs)
    iv = implied_vol(mkt_price, S0_ex, K, T_ex, r_ex)
    impl_vols.append(iv)

plt.figure(figsize=(7, 4))
plt.plot(strikes_smile, [iv * 100 if iv else np.nan for iv in impl_vols],
         'o-', color='tomato', linewidth=2)
plt.axvline(S0_ex, color='gray', linestyle=':', label=f'ATM (S₀=${S0_ex})')
plt.axhline(sig_ex * 100, color='steelblue', linestyle='--',
            label=f'True σ = {sig_ex:.0%}')
plt.xlabel('Strike price K ($)')
plt.ylabel('Implied Volatility (%)')
plt.title('Volatility Smile from Fat-Tailed Returns (t₅ distribution)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('vol_smile.png', dpi=100)
plt.show()
```

**Question 5.1:** The volatility smile shows that out-of-the-money options (especially puts) imply higher volatility than at-the-money options. What does this tell us about market participants' beliefs regarding the probability of large negative stock moves?

**Question 5.2:** The fat-tailed Student-t distribution generates higher prices for out-of-the-money options than the normal distribution. Explain why: what feature of the distribution matters for the price of an option that only pays off in extreme events?

---

## Deliverables

Submit a PDF or Jupyter notebook containing:

1. All plots with captions.
2. Answers to all numbered questions.
3. A table: for S₀ ∈ {80, 90, 100, 110, 120} with K = 105 fixed, report the call price, delta, and the risk-neutral probability N(d₂) that the option expires in the money.
4. **Reflection (1 paragraph):** The Black-Scholes formula requires only five inputs (S₀, K, T, r, σ). Of these, σ must be estimated — it is not directly observable. Discuss two methods a practitioner might use to estimate σ, and the pros and cons of each.
