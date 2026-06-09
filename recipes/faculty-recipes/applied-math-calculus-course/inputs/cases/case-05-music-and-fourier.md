# Case 05: The Sound of Mathematics — Fourier Analysis and Music

**Course:** Applied Mathematics 50
**Topic block:** Weeks 9–10
**Fields:** Music, acoustics, signal processing, harmonic analysis

---

## Overview

Why does a concert A played on a violin sound different from the same note played on a piano, even though both vibrate at 440 Hz? The answer is Fourier analysis — one of the most powerful and widely applied ideas in all of mathematics. This case develops the theory of **Fourier series**, shows how it explains the physics of musical sound, and explores its modern applications in audio compression (MP3), noise cancellation, and music recognition (Shazam).

---

## The Central Problem

Any periodic signal f(t) — a musical note, a heartbeat, a speech waveform — can be decomposed into a sum of pure sine and cosine waves at different frequencies:

$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\!\left(\frac{2\pi n t}{T}\right) + b_n \sin\!\left(\frac{2\pi n t}{T}\right) \right]$$

The coefficients aₙ and bₙ — the **Fourier coefficients** — tell you how much of each frequency is present in the signal. Recovering them from f(t) is **Fourier analysis**; reconstructing f(t) from the coefficients is **Fourier synthesis**.

---

## Mathematical Content

### Fourier Coefficients

For a function f with period T, the Fourier coefficients are:

$$a_n = \frac{2}{T} \int_0^T f(t)\cos\!\left(\frac{2\pi n t}{T}\right) dt, \qquad b_n = \frac{2}{T} \int_0^T f(t)\sin\!\left(\frac{2\pi n t}{T}\right) dt$$

These are computed by integration — directly applying Unit 1 (integration techniques) and Unit 2 (applications of integration).

**Key property — orthogonality:** The functions {1, cos(2πnt/T), sin(2πnt/T)} are mutually orthogonal over [0, T]:

$$\int_0^T \cos\!\left(\frac{2\pi m t}{T}\right)\cos\!\left(\frac{2\pi n t}{T}\right) dt = \begin{cases} T/2 & m = n \\ 0 & m \neq n \end{cases}$$

Orthogonality is why the formula for aₙ isolates the n-th component — multiplying f(t) by cos(2πnt/T) and integrating "filters out" everything except the n-th frequency.

### Worked Example: Square Wave

Consider f(t) = +1 for 0 < t < T/2, and f(t) = −1 for T/2 < t < T (a square wave). Computing the Fourier coefficients:

$$a_n = 0 \text{ (all n)}, \qquad b_n = \begin{cases} 4/(n\pi) & n \text{ odd} \\ 0 & n \text{ even} \end{cases}$$

So: f(t) = (4/π)[sin(2πt/T) + sin(6πt/T)/3 + sin(10πt/T)/5 + ···]

This is an infinite series of odd harmonics. Notice: the series converges (it represents f everywhere except the jump discontinuities), and the coefficients decay like 1/n. **This is directly connected to the p-series** (Unit 3.3): Σ 1/n diverges, but the actual series converges because of alternating signs and the sine functions.

### Parseval's Theorem

The total energy of a signal equals the sum of squared Fourier coefficients:

$$\frac{1}{T}\int_0^T |f(t)|^2\, dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^\infty (a_n^2 + b_n^2)$$

This is a statement about infinite series (Units 3–4) and improper integrals (Unit 1.5). It is also the mathematical basis for audio compression: if most of the energy is concentrated in a few coefficients, you can discard the rest with little perceptual loss.

### The Physics of Timbre

A violin string vibrating at fundamental frequency f₀ = 440 Hz also vibrates at 2f₀, 3f₀, 4f₀, … (overtones). The **timbre** — the characteristic sound quality distinguishing violin from piano — is determined by the relative amplitudes of these overtones, i.e., by the Fourier coefficients of the sound waveform.

**Why does a plucked string produce overtones?** The string's displacement y(x, t) satisfies the **wave equation**:

$$\frac{\partial^2 y}{\partial t^2} = c^2 \frac{\partial^2 y}{\partial x^2}$$

The general solution is a Fourier series in space, where each spatial mode oscillates at a frequency nf₀. The initial shape of the pluck determines the Fourier coefficients and hence the timbre.

### MP3 and Perceptual Coding

The MP3 audio format exploits the Fourier transform to compress audio by a factor of 10:1 with minimal audible loss. The algorithm:

1. Divide the audio signal into short overlapping windows (~20 ms).
2. Compute the Fourier transform of each window (using the Fast Fourier Transform, FFT).
3. Apply a **psychoacoustic model**: discard frequency components that are inaudible because they are masked by louder nearby frequencies or fall below the hearing threshold.
4. Encode the remaining coefficients with fewer bits.

The mathematics here is the **discrete Fourier transform (DFT)**: the continuous integral is replaced by a finite sum over N samples:

$$\hat{f}_k = \sum_{n=0}^{N-1} f_n\, e^{-2\pi i kn/N}, \qquad k = 0, 1, \ldots, N-1$$

The **FFT** computes all N coefficients in O(N log N) operations rather than O(N²) — one of the most important algorithms in applied mathematics.

### Connection to Course Material

- **Integration techniques** (Unit 1): computing Fourier coefficients requires integration by parts (§1.1) and trigonometric integrals (§1.2).
- **Infinite series** (Unit 3): Fourier series are infinite series of functions; convergence questions are subtle and important.
- **Taylor series vs. Fourier series** (Unit 4): both represent functions as infinite series, but Taylor series use polynomials (good for smooth functions near a point) while Fourier series use sinusoids (good for periodic functions globally).
- **ODEs and PDEs** (Unit 5): the wave equation and heat equation are both solved using Fourier series.

---

## Classic Paper

**Fourier, Joseph.** *Théorie analytique de la chaleur* (The Analytical Theory of Heat), 1822. Chapter III, §§169–186 (excerpts in English translation).

Fourier developed his series to solve the heat equation for heat conduction in a metal plate. His claim that *any* function could be represented as a trigonometric series was initially controversial — it took decades for mathematicians to make it rigorous. The excerpt shows the original derivation of the coefficients and a worked example.

---

## Modeling Exercise

**Build a synthesizer.**

1. Compute the first 5 Fourier coefficients (b₁, b₃, b₅, b₇, b₉) of a square wave with period T = 1 and amplitude 1.
2. Plot the partial sums S₁, S₃, S₅, S₉ (including terms up to the 1st, 3rd, 5th, 9th harmonic). Observe the **Gibbs phenomenon** — the overshoot near the discontinuity that never goes away.
3. A clarinet produces primarily odd harmonics (like a square wave). A violin produces both odd and even harmonics. Using the formulas above and a Python audio library, synthesize one second of A 440 Hz for each instrument model. Can you hear the difference?
4. **Error estimation:** The energy in the tail of the Fourier series (terms n > N) is Σ_{n>N} b_n². For the square wave, use the p-series test to show this decays like 1/N, and compute how many terms are needed to capture 99% of the total energy.

---

## Discussion Questions

1. Fourier claimed in 1807 that every function could be represented by a trigonometric series. This claim was false as stated — there are pathological functions whose Fourier series diverge. Does this undermine the practical usefulness of Fourier analysis? What does it say about the relationship between mathematical rigor and applied utility?

2. The human ear perceives sound logarithmically: doubling the frequency raises the pitch by one octave, and halving the amplitude reduces the loudness by a fixed number of decibels. How does this logarithmic perception affect how we should think about the Fourier representation of music?

3. Auto-Tune uses Fourier analysis to detect and correct the pitch of a singer's voice in real time. What ethical issues does this raise in music production? Is there an analogue in other fields where applied mathematics enables similar interventions?

4. The FFT was rediscovered by Cooley and Tukey in 1965. Gauss had discovered essentially the same algorithm in 1805 but never published it. What does this history suggest about the relationship between pure and applied mathematics?

---

## Further Reading

- Körner, T. W. *Fourier Analysis.* Cambridge University Press, 1988. — rigorous and witty; includes music, heat, and probability
- Strang, Gilbert. "The Discrete Cosine Transform." *SIAM Review* 41(1) (1999): 135–147. — the mathematics of JPEG compression
- Benson, Dave. *Music: A Mathematical Offering.* Cambridge University Press, 2007. (Free online.) — comprehensive treatment of Fourier analysis in music
- Smith, Julius O. "Mathematics of the Discrete Fourier Transform." (Online textbook, ccrma.stanford.edu) — free, thorough, with audio examples
