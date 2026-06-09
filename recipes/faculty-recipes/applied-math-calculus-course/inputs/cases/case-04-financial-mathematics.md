# Case 04: Pricing the Future — The Mathematics of Financial Derivatives

**Course:** Applied Mathematics 50
**Topic block:** Weeks 7–8
**Fields:** Finance, economics, stochastic processes, partial differential equations

---

## Overview

In 1973, Fischer Black, Myron Scholes, and Robert Merton published a formula that transformed global financial markets. The **Black-Scholes equation** — a partial differential equation — gives the fair price of a financial option: the right to buy or sell an asset at a fixed price on a future date. Merton and Scholes received the Nobel Prize in Economics in 1997. This case develops the mathematics behind option pricing, from the concept of arbitrage-free pricing through the Black-Scholes PDE and its solution via the heat equation.

---

## The Central Problem

A **call option** on a stock gives its holder the right (but not the obligation) to buy the stock at price K (the "strike price") on date T (the "expiration date"). If the stock price at expiration is S_T, the option pays:

$$\text{Payoff} = \max(S_T - K, 0)$$

You pay nothing if the stock ends below K (the option expires worthless), and you gain S_T − K if it ends above K. What is a fair price to pay for this option today, when the stock price is S₀?

---

## Mathematical Content

### Random Walk and Geometric Brownian Motion

Stock prices are modeled as following **geometric Brownian motion**:

$$dS = \mu S\, dt + \sigma S\, dW$$

where:
- μ = expected return rate (drift)
- σ = volatility (standard deviation of returns)
- dW = increment of a Wiener process (standard Brownian motion)

This is a **stochastic differential equation**. The key property: log(S_T/S₀) is normally distributed with mean (μ − σ²/2)T and variance σ²T.

For our purposes, the important consequence is that S_T has a **lognormal distribution**, and the distribution of S_T is fully characterized by S₀, μ, σ, and T.

### The No-Arbitrage Principle

The crucial insight of Black and Scholes: the option price must be determined by **no-arbitrage** — the impossibility of making riskless profit. By continuously adjusting a portfolio of the stock and a risk-free bond, one can perfectly replicate the option's payoff. Since the replicating portfolio must cost the same as the option, the option price is uniquely determined.

This argument implies that the expected return μ *drops out* of the pricing formula. Only the volatility σ matters.

### The Black-Scholes PDE

Let V(S, t) denote the option price when the stock price is S at time t. The no-arbitrage argument leads to the **Black-Scholes PDE**:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

with boundary condition V(S, T) = max(S − K, 0) (the payoff at expiration), where r is the risk-free interest rate.

### Solving via the Heat Equation

The Black-Scholes PDE can be transformed into the classical **heat equation** from physics:

$$\frac{\partial u}{\partial \tau} = \frac{\partial^2 u}{\partial x^2}$$

by the substitutions x = ln(S/K), τ = σ²(T−t)/2, and an appropriate rescaling of V. The heat equation has the explicit solution:

$$u(x, \tau) = \frac{1}{\sqrt{4\pi\tau}} \int_{-\infty}^{\infty} u(y, 0)\, e^{-(x-y)^2/(4\tau)}\, dy$$

This integral is a **convolution** with a Gaussian kernel — precisely the kind of integral studied in Unit 1 (improper integrals) and Unit 2 (probability density functions).

### The Black-Scholes Formula

After inverting the substitution, the price of a European call option is:

$$C = S_0 N(d_1) - Ke^{-rT} N(d_2)$$

where N(·) is the standard normal CDF, and:

$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

This elegant closed-form formula requires only observable inputs (S₀, K, r, T) plus the volatility σ (which must be estimated or implied from market prices).

### Connection to Course Material

- **Improper integrals** (Unit 1.5): the solution to the heat equation is an improper integral over the real line.
- **Normal distribution** (Unit 2.4): N(d₁) and N(d₂) involve the Gaussian integral ∫e^(−x²/2) dx, which cannot be evaluated in closed form — it is computed using the Taylor series for e^(−x²) (Unit 4.1).
- **ODEs** (Unit 5): the Black-Scholes PDE reduces to a first-order ODE in special cases; the heat equation is the prototypical parabolic PDE.
- **Taylor series** (Unit 4): option pricing formulas for more complex options are computed using series expansions when closed forms are unavailable.

---

## Classic Paper

**Black, Fischer, and Myron Scholes.** "The pricing of options and corporate liabilities." *Journal of Political Economy* 81(3) (1973): 637–654.

This is one of the most cited papers in economics. The derivation (Section II) is readable after Math 1b — it requires only the concept of a portfolio, the chain rule, and the ability to solve a PDE by substitution. Students should read Sections I–III.

---

## Modeling Exercise

**Option pricing calculator.**

Suppose a stock currently trades at S₀ = $100, with volatility σ = 20% per year. The risk-free interest rate is r = 5% per year. Consider a call option with strike K = $105 and expiration T = 1 year.

1. Compute d₁ and d₂.
2. Use a table or Python to evaluate N(d₁) and N(d₂). Compute the Black-Scholes price C.
3. Interpret N(d₂) as the (risk-neutral) probability that the option expires in the money. What does it mean for this probability to be less than 50% even though the stock is expected to grow?
4. **Sensitivity analysis ("the Greeks"):** Compute ∂C/∂S₀ (delta), ∂C/∂σ (vega), and ∂C/∂T (theta) numerically by changing each parameter by 1% and observing the change in C. Which parameter has the largest effect on the option price?
5. Plot C as a function of σ ∈ [0.05, 0.60]. This is the "volatility smile" problem: market prices imply a non-constant σ across strikes. What does this suggest about the assumptions of the model?

---

## Discussion Questions

1. The Black-Scholes model assumes that stock returns are normally distributed. Empirically, large negative returns occur far more often than a normal distribution predicts ("fat tails"). What are the consequences for option pricing and financial risk management?

2. In 1998, Long-Term Capital Management — a hedge fund staffed by the inventors of the Black-Scholes model — lost $4.6 billion and required a federal bailout. Given that they had Nobel Prize-winning mathematics, what went wrong?

3. The no-arbitrage argument says that the expected return μ does not affect option prices. Does this seem intuitive? Try to explain in plain English why a riskier stock (higher σ) is worth more to an option holder, but a faster-growing stock (higher μ) is not.

4. The 2008 financial crisis was partly attributed to the mispricing of mortgage-backed securities using models similar to Black-Scholes. What mathematical assumptions underlying these models broke down, and how might better models have helped?

---

## Further Reading

- Hull, John C. *Options, Futures, and Other Derivatives.* 10th ed. Pearson, 2018. Ch. 13–15. — standard finance textbook treatment
- Wilmott, Paul, Sam Howison, and Jeff Dewynne. *The Mathematics of Financial Derivatives.* Cambridge University Press, 1995. — rigorous mathematical treatment accessible after calculus
- MacKenzie, Donald. *An Engine, Not a Camera: How Financial Models Shape Markets.* MIT Press, 2006. — sociological perspective on how the formula changed markets
- Strogatz, Steven. "Guest Column: Math and the Meltdown." *New York Times*, March 5, 2009.
