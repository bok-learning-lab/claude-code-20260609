# Case 01: Seeing Inside the Body — The Mathematics of Medical Imaging

**Course:** Applied Mathematics 50
**Topic block:** Weeks 1–2
**Fields:** Medical imaging, signal processing, linear algebra

---

## Overview

Every CT scan, MRI, and PET scan in use today rests on a mathematical idea: you can reconstruct the interior of an object from a collection of its projections, without cutting it open. This case studies the **Radon transform** and the **filtered back-projection algorithm** that make modern medical imaging possible. Students read a landmark paper, work through the mathematics of projection and reconstruction, and implement a simple version of the algorithm.

---

## The Central Problem

Suppose you want to know the density f(x, y) at every point inside a patient's body. You cannot measure f directly, but you *can* shine an X-ray beam along a line and measure how much intensity is absorbed — that is, you can measure the **line integral** of f along each beam direction. Given sufficiently many such measurements, can you recover f?

The answer is yes, and the mathematics is the **Radon transform**:

$$\mathcal{R}f(\ell) = \int_\ell f(x,y)\, ds$$

where the integral runs along the line ℓ. The reconstruction problem asks: given Rf for all lines ℓ, find f.

---

## Mathematical Content

### Projections and the Radon Transform
A line in the plane can be parameterized as x cos θ + y sin θ = t for angle θ ∈ [0, π) and offset t ∈ ℝ. The Radon transform of f is:

$$\mathcal{R}f(t, \theta) = \int_{-\infty}^{\infty} f(t\cos\theta - s\sin\theta,\; t\sin\theta + s\cos\theta)\, ds$$

This is the measurement a CT scanner records for one beam direction θ at offset t.

### The Fourier Slice Theorem
The key theoretical result is the **Fourier Slice Theorem** (also called the Central Slice Theorem):

> The 1D Fourier transform of a projection at angle θ equals a slice through the 2D Fourier transform of f at the same angle.

In symbols, if F = ℱ₂[f] is the 2D Fourier transform of f, and P_θ = ℱ₁[Rf(·, θ)] is the 1D Fourier transform of the projection at angle θ, then:

$$P_\theta(\omega) = F(\omega\cos\theta,\; \omega\sin\theta)$$

This means that by collecting projections at many angles, we can fill in the 2D Fourier transform of f and then invert it to recover f.

### Filtered Back-Projection
The **filtered back-projection (FBP)** algorithm is the practical implementation:
1. For each angle θ, compute the 1D Fourier transform of the projection.
2. Multiply by a **ramp filter** |ω| to compensate for the non-uniform sampling of Fourier space.
3. Invert the 1D Fourier transform to get a filtered projection.
4. **Back-project**: smear each filtered projection back across the image at its angle.
5. Sum the back-projections over all angles.

The ramp filter step connects to Unit 1 material: the Hilbert transform involves an improper integral, and the back-projection step is itself an integral over angles.

### Connection to Course Material
- **Integration** (Math 1a/1b): projections are line integrals; back-projection is integration over angles.
- **Taylor series** (Math 1b Unit 4): the ramp filter can be approximated by a finite series for numerical stability.
- **Differential equations** (Math 1b Unit 5): MRI reconstruction involves solving PDEs; the Bloch equations governing nuclear spin are ODEs.

---

## Classic Paper

**Hounsfield, Godfrey N.** "Computerized transverse axial scanning (tomography): Part 1. Description of system." *British Journal of Radiology* 46 (1973): 1016–1022.

This is the original paper describing the first clinical CT scanner. Hounsfield (who shared the 1979 Nobel Prize in Medicine) explains the physical setup and reconstruction method in accessible terms. Note: the mathematics here is presented at an engineering level; students will supply the rigorous mathematical underpinning.

**Supplementary:** Radon, Johann. "Über die Bestimmung von Funktionen durch ihre Integralwerte längs gewisser Mannigfaltigkeiten." *Berichte Sächsische Akademie der Wissenschaften* 69 (1917): 262–277. (English translation available.) — the original mathematical paper, 55 years before the scanner.

---

## Modeling Exercise

**Discrete phantom experiment.** Consider a 4×4 grid of unknown pixel values f_{ij}. A "scanner" measures the sum along each row, column, and diagonal — 10 linear equations in 16 unknowns.

1. Write the system as a matrix equation Af = b. Is the system underdetermined, overdetermined, or square?
2. Simulate measurements from a known phantom (e.g., a circle of 1s on a background of 0s). Add small random noise to b.
3. Reconstruct f using the pseudoinverse A⁺ = (AᵀA)⁻¹Aᵀ. Compare to the true phantom.
4. What happens to reconstruction quality as you increase the number of projection angles? Plot error vs. number of angles.

*(Python starter code provided separately.)*

---

## Discussion Questions

1. The Fourier Slice Theorem assumes we can measure projections at *every* angle. Real scanners use a finite number of angles. What mathematical artifacts does this cause, and how are they mitigated?

2. MRI does not use X-rays. What physical quantity does it measure, and how does the mathematical reconstruction differ from CT?

3. CT scanning exposes patients to ionizing radiation. Compressed sensing is a newer mathematical approach that can reconstruct images from far fewer measurements. What mathematical idea makes this possible, and what assumptions does it require?

4. Hounsfield's 1973 paper describes a reconstruction algorithm that takes hours on the computers of the day. Modern scanners reconstruct in real time. What changed — the mathematics, the algorithm, the hardware, or all three?

---

## Further Reading

- Kak, A. C., and Malcolm Slaney. *Principles of Computerized Tomographic Imaging.* IEEE Press, 1988. (Free PDF available from IEEE.)
- Candès, Emmanuel, and Michael Wakin. "An Introduction to Compressive Sampling." *IEEE Signal Processing Magazine* 25(2) (2008): 21–30.
- 3Blue1Brown. "But what is the Fourier Transform? A visual introduction." (YouTube)
