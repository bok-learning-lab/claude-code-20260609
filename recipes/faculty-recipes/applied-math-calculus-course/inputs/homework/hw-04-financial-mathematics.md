# Homework 4: The Mathematics of Financial Derivatives

**Course:** Applied Mathematics 50
**Topic block:** Weeks 7–8 (Case 04)
**Due:** End of Week 8
**Instructions:** Show all work. For parts requiring the normal CDF N(·), use a standard normal table (provided) or the approximation given in part 3(b). State all assumptions clearly.

---

## Problem 1 — Properties of the Lognormal Distribution (20 points)

A stock following geometric Brownian motion has terminal price:

$$S_T = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma\sqrt{T}\,Z\right], \quad Z \sim N(0,1)$$

**(a)** Let X = log(S_T / S_0). Identify the distribution of X (state the mean and variance).

**(b)** Using the moment generating function of the normal distribution (E[e^{tZ}] = e^{t²/2}), compute E[S_T]. Show your derivation and confirm that E[S_T] = S_0 e^{μT}.

**(c)** Compute the median of S_T. Show that the median equals S_0 e^{(μ − σ²/2)T}, which is *less than* the mean for σ > 0. Interpret: in what sense is the "average" return misleading as a description of the "typical" outcome?

**(d)** Compute Var(S_T). Express your answer in terms of S_0, μ, σ, T. (You will need E[S_T²]; compute this similarly to part (b).)

**(e)** For S_0 = 100, μ = 0.08, σ = 0.20, T = 1: compute E[S_T], Median(S_T), and Std(S_T). Comment on the relative magnitudes.

---

## Problem 2 — Verifying the Black-Scholes PDE (25 points)

The Black-Scholes call price is:

$$C(S, t) = S\,N(d_1) - K e^{-r(T-t)} N(d_2)$$

where:
$$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}, \qquad d_2 = d_1 - \sigma\sqrt{T-t}$$

and τ = T − t is the time remaining.

**(a)** Compute ∂C/∂S (the option's **delta**). Show that ∂C/∂S = N(d₁). (Hint: differentiate using the chain rule, noting that d₁ and d₂ both depend on S. You will need the identity SN′(d₁) = Ke^{−rτ}N′(d₂), where N′ is the standard normal PDF; prove this identity first.)

**(b)** Compute ∂²C/∂S² (the option's **gamma**). Show that:
$$\frac{\partial^2 C}{\partial S^2} = \frac{N'(d_1)}{S\sigma\sqrt{\tau}}$$

**(c)** Compute ∂C/∂t (the option's **theta**, noting that ∂τ/∂t = −1). You may leave your answer in terms of N′(d₁), d₁, d₂, and the other parameters without simplifying fully.

**(d)** Substitute your expressions from (a), (b), (c) into the Black-Scholes PDE:
$$\frac{\partial C}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + rS\frac{\partial C}{\partial S} - rC = 0$$
and verify that C satisfies the PDE. (This is the main verification step; organize your algebra clearly.)

---

## Problem 3 — Computing Option Prices by Hand (25 points)

Consider a European call option with:

S₀ = $100, K = $100 (at-the-money), T = 0.5 years, r = 0.04, σ = 0.30

**(a)** Compute d₁ and d₂ exactly (leaving logarithms and square roots in simplified form, then evaluate numerically).

**(b)** Use the following rational approximation to the normal CDF (accurate to 4 decimal places):
$$N(x) \approx 1 - n(x)(a_1 k + a_2 k^2 + a_3 k^3), \quad k = \frac{1}{1 + 0.33267 x}, \quad x \geq 0$$
where n(x) = (1/√(2π))e^{−x²/2}, a₁ = 0.4361836, a₂ = −0.1201676, a₃ = 0.9372980, and N(−x) = 1 − N(x). Compute N(d₁) and N(d₂) using this approximation.

**(c)** Compute the Black-Scholes call price C. Then use put-call parity (C − P = S₀ − Ke^{−rT}) to find the put price P.

**(d)** **Intrinsic value and time value.** The intrinsic value of a call is max(S₀ − K, 0) (its value if exercised immediately). The time value is C minus the intrinsic value. Compute both for this option. Since the option is at-the-money (S₀ = K), the entire premium is time value. Interpret: what are you paying for when you buy an at-the-money option?

**(e)** How does the call price change if volatility doubles to σ = 0.60? Recompute C. Is the relationship between price and volatility linear? Why is a higher-volatility stock worth more to a call option buyer?

---

## Problem 4 — The Heat Equation and Option Pricing (30 points)

The Black-Scholes PDE can be transformed into the classical heat equation. This problem works through the transformation.

Starting with the Black-Scholes PDE for a European call (with τ = T − t):

$$\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial S^2}\cdot S^2 + rS\frac{\partial V}{\partial S} - rV$$

**(a)** Introduce the change of variables x = ln(S/K) (so S = Ke^x). Show that:
$$S\frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}, \qquad S^2\frac{\partial^2 V}{\partial S^2} = \frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}$$
and rewrite the PDE in terms of x and τ.

**(b)** Let α = 2r/σ² and write V(x, τ) = e^{ax + bτ} u(x, τ) for constants a and b to be determined. Choose a and b to eliminate the first-derivative term (∂u/∂x) and the zero-order term (u) from the PDE. What are a and b?

**(c)** Show that with your choice of a and b, the equation for u is:
$$\frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}$$
This is the **heat equation** (or diffusion equation) with diffusion coefficient D = σ²/2.

**(d)** The general solution to the heat equation on the real line with initial data u(x, 0) = u₀(x) is:
$$u(x, \tau) = \frac{1}{\sqrt{2\pi\sigma^2\tau}}\int_{-\infty}^{\infty} u_0(y)\,e^{-(x-y)^2/(2\sigma^2\tau)}\, dy$$
This is the convolution of u₀ with a Gaussian kernel. Interpret this formula: what does it say about how information about the initial condition spreads over time? Connect this to the financial interpretation: why does option pricing involve averaging over the Gaussian distribution of future stock prices?

**(e)** The boundary condition for a call option at expiration is V(S, 0) = max(S − K, 0), which translates to u(x, 0) = u₀(x) for some function u₀. Write out u₀(x) explicitly (in terms of x = ln(S/K)). Describe the shape of u₀: is it smooth, piecewise linear, or discontinuous? What property of the boundary condition makes the heat equation integral tractable in closed form?

**(f)** Reading the Black & Scholes (1973) paper: In their original derivation, Black and Scholes derive the option price from the no-arbitrage condition and a hedging argument, *not* by solving a PDE. In one paragraph, describe the hedging argument in your own words: what portfolio do they construct, why is it riskless, and why does this determine the option price uniquely?
