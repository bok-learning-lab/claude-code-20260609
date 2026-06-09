# Lab 01: Seeing Inside the Body — Reconstructing Images from Projections

**Course:** Applied Mathematics 50
**Companion to:** Case 01 (Medical Imaging)
**Estimated time:** 2 hours
**Tools:** Python 3, NumPy, Matplotlib, SciPy

---

## Learning Goals

By the end of this lab you will be able to:
- Represent a 2D density image as a matrix and simulate X-ray projections (line integrals)
- Build and solve the linear system Af = b for image reconstruction
- Observe how reconstruction quality depends on the number of projection angles
- Implement a simple back-projection algorithm and visualize the result

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq

rng = np.random.default_rng(42)  # reproducible randomness
```

---

## Part 1: Creating a Phantom

A **phantom** is a known test image used to evaluate reconstruction algorithms. We will use a small discrete phantom: a grid of pixel values representing a cross-section of an object.

```python
# 8x8 phantom: a "ring" (disk of 1s with hollow center)
N = 8
phantom = np.zeros((N, N))
cx, cy = N // 2, N // 2  # center

for i in range(N):
    for j in range(N):
        r = np.sqrt((i - cx)**2 + (j - cy)**2)
        if 1.5 <= r <= 3.0:
            phantom[i, j] = 1.0

plt.figure(figsize=(4, 4))
plt.imshow(phantom, cmap='gray', origin='lower')
plt.colorbar(label='Density')
plt.title('Ground Truth Phantom')
plt.tight_layout()
plt.savefig('phantom_ground_truth.png', dpi=100)
plt.show()
```

**Question 1.1:** Describe what the phantom looks like. What physical object might this represent in a CT scan (e.g., a cross-section of what anatomical structure)?

---

## Part 2: Simulating Projections

A projection at angle θ sums pixel values along lines perpendicular to the direction θ. For a discrete image, this means summing along diagonal strips.

We will use SciPy's `radon` transform from `skimage` if available, or build a simple version:

```python
def simple_projection(image, angle_deg):
    """Project image by rotating and summing along columns."""
    from scipy.ndimage import rotate
    rotated = rotate(image, angle_deg, reshape=False, order=1)
    return rotated.sum(axis=0)  # sum each column

# Test with a single angle
proj_0 = simple_projection(phantom, 0)    # vertical beams
proj_45 = simple_projection(phantom, 45)  # diagonal beams
proj_90 = simple_projection(phantom, 90)  # horizontal beams

angles = [0, 45, 90]
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, angle in zip(axes, angles):
    proj = simple_projection(phantom, angle)
    ax.plot(proj, marker='o')
    ax.set_title(f'Projection at {angle}°')
    ax.set_xlabel('Detector position')
    ax.set_ylabel('Integrated density')
plt.tight_layout()
plt.savefig('projections.png', dpi=100)
plt.show()
```

**Question 2.1:** At 0°, the projection sums along vertical lines. Which detector positions record the highest values, and why? Does this match the shape of the phantom?

**Question 2.2:** How does the projection change from 0° to 90°? What symmetry of the phantom explains the relationship between these two projections?

---

## Part 3: Building the Measurement Matrix

For a linear reconstruction, we need to express all projections as a single matrix equation **Af = b**, where **f** is the flattened image vector and **b** is the vector of all measurements.

```python
def build_projection_matrix(n, angles_deg):
    """
    Build matrix A such that A @ f.flatten() = measured projections.
    n: image is n x n
    angles_deg: list of projection angles
    """
    from scipy.ndimage import rotate
    num_pixels = n * n
    rows = []

    for angle in angles_deg:
        # For each angle, each detector position is a row of A
        for det in range(n):
            # Create a mask: which pixels contribute to this detector at this angle?
            mask = np.zeros((n, n))
            mask[:, det] = 1.0
            # Rotate the mask in the *opposite* direction to simulate projecting at `angle`
            rotated_mask = rotate(mask, -angle, reshape=False, order=1)
            rows.append(rotated_mask.flatten())

    return np.array(rows)

# Use 4 angles: 0, 45, 90, 135 degrees
angles = [0, 45, 90, 135]
A = build_projection_matrix(N, angles)
f_true = phantom.flatten()

# Simulate measurements with small noise
b_clean = A @ f_true
noise_level = 0.05 * np.max(np.abs(b_clean))
b_noisy = b_clean + rng.normal(0, noise_level, size=b_clean.shape)

print(f"Matrix A shape: {A.shape}  (measurements × pixels)")
print(f"System is {'underdetermined' if A.shape[0] < A.shape[1] else 'overdetermined'}")
```

**Question 3.1:** How many measurements does the matrix have? How many unknowns? Is the system underdetermined, overdetermined, or square? What does this mean for exact reconstruction?

---

## Part 4: Reconstruction via Least Squares

Since the system is overdetermined (or underdetermined), we use the **pseudoinverse** (least-squares solution):

```python
def reconstruct(A, b, n):
    """Solve A @ f = b using least squares; reshape to n x n image."""
    f_rec, residuals, rank, sv = lstsq(A, b)
    return f_rec.reshape(n, n)

# Reconstruct from noisy measurements
f_reconstructed = reconstruct(A, b_noisy, N)

# Visualize side by side
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(phantom, cmap='gray', origin='lower', vmin=0, vmax=1)
axes[0].set_title('Ground Truth')
axes[1].imshow(f_reconstructed, cmap='gray', origin='lower')
axes[1].set_title(f'Reconstruction ({len(angles)} angles)')
axes[2].imshow(np.abs(phantom - f_reconstructed), cmap='hot', origin='lower')
axes[2].set_title('Absolute Error')
for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.savefig('reconstruction_comparison.png', dpi=100)
plt.show()

# Compute reconstruction error
rmse = np.sqrt(np.mean((phantom - f_reconstructed)**2))
print(f"RMSE with {len(angles)} angles: {rmse:.4f}")
```

---

## Part 5: How Many Angles Are Enough?

Real CT scanners use hundreds of projection angles. Here we study how reconstruction quality improves with more angles.

```python
angle_counts = [2, 4, 8, 16, 32]
errors = []

for n_angles in angle_counts:
    angles = np.linspace(0, 180, n_angles, endpoint=False)
    A = build_projection_matrix(N, angles)
    b = A @ f_true + rng.normal(0, noise_level, size=A.shape[0])
    f_rec = reconstruct(A, b, N)
    rmse = np.sqrt(np.mean((phantom - f_rec)**2))
    errors.append(rmse)
    print(f"{n_angles:3d} angles → RMSE = {rmse:.4f}")

plt.figure(figsize=(6, 4))
plt.plot(angle_counts, errors, 'o-', color='steelblue', linewidth=2)
plt.xlabel('Number of projection angles')
plt.ylabel('Reconstruction RMSE')
plt.title('Reconstruction Error vs. Number of Angles')
plt.grid(True)
plt.tight_layout()
plt.savefig('error_vs_angles.png', dpi=100)
plt.show()
```

**Question 5.1:** Does the error decrease monotonically with more angles? Is there a point of diminishing returns?

**Question 5.2:** The system with 2 angles is highly underdetermined (many possible images produce the same projections). With 32 angles it becomes overdetermined. How does the character of the reconstruction problem change between these regimes?

**Question 5.3:** In a real CT scanner, using more angles means more radiation exposure to the patient. Based on your error-vs-angles curve, how would you decide on the minimum number of angles that gives "good enough" reconstruction?

---

## Part 6: Simple Back-Projection (No Filter)

The industrial reconstruction algorithm is **filtered back-projection**. Here we implement the simpler (unfiltered) version to see what goes wrong without the filter.

```python
def back_project(projections_dict, n):
    """Sum rotated projections back into image space (no filter)."""
    from scipy.ndimage import rotate
    result = np.zeros((n, n))
    for angle, proj in projections_dict.items():
        # Create a 2D image where each column equals the projection
        proj_2d = np.tile(proj, (n, 1))
        # Rotate back
        result += rotate(proj_2d, angle, reshape=False, order=1)
    return result / len(projections_dict)

angles_bp = np.linspace(0, 180, 16, endpoint=False)
proj_dict = {angle: simple_projection(phantom, angle) for angle in angles_bp}
bp_image = back_project(proj_dict, N)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(phantom, cmap='gray', origin='lower')
axes[0].set_title('Ground Truth')
axes[1].imshow(bp_image, cmap='gray', origin='lower')
axes[1].set_title('Unfiltered Back-Projection (16 angles)')
for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.savefig('back_projection.png', dpi=100)
plt.show()
```

**Question 6.1:** The unfiltered back-projection produces a blurry image. Why? (Hint: think about what happens when you smear each projection back without any correction for overlapping contributions.)

**Question 6.2:** The filtered back-projection applies a "ramp filter" |ω| in Fourier space before back-projecting. Based on your knowledge of Fourier analysis (Case 05), what does multiplying by |ω| do to the frequency content of the signal? Why would this undo the blurring?

---

## Deliverables

Submit a PDF or Jupyter notebook containing:

1. Plots: ground truth phantom, three sample projections, reconstruction comparisons at 4 and 16 angles, error-vs-angles curve, back-projection result.
2. Written answers to all numbered questions above.
3. **Extension (optional):** Modify the phantom to be a filled square instead of a ring. How does the reconstruction quality compare? Why might some shapes be harder to reconstruct than others?

---

## Connection to the Case Reading

- Hounsfield's 1973 scanner used 160 projections at each of 180 angles — 28,800 measurements to reconstruct a 80×80 image (6,400 pixels). Based on your experiments, why is this level of oversampling important?
- The mathematical question "how many projections are enough?" is still an active research area, especially for compressed sensing methods that promise good reconstruction from far fewer measurements.
