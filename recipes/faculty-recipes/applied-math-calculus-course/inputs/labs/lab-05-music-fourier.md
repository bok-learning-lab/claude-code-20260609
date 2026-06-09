# Lab 05: The Sound of Mathematics — Fourier Analysis and Music

**Course:** Applied Mathematics 50
**Companion to:** Case 05 (Music and Fourier Analysis)
**Estimated time:** 2 hours
**Tools:** Python 3, NumPy, Matplotlib, SciPy (and optionally sounddevice or IPython for audio playback)

---

## Learning Goals

By the end of this lab you will be able to:
- Compute Fourier coefficients analytically and numerically and verify they match
- Observe the Gibbs phenomenon in partial sums of Fourier series
- Build a simple additive synthesizer using Fourier series
- Apply the FFT to a real audio signal and interpret the frequency spectrum

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq

# Optional: audio playback
try:
    import sounddevice as sd
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False
    print("sounddevice not available — audio playback disabled")
```

---

## Part 1: Computing Fourier Coefficients

### Square Wave

The square wave with period T = 1 and amplitude 1:
- f(t) = +1 for 0 < t < 1/2
- f(t) = −1 for 1/2 < t < 1

**Analytical coefficients:** aₙ = 0 for all n; b_n = 4/(nπ) for n odd, 0 for n even.

Let's verify numerically.

```python
T = 1.0  # period
N_points = 10_000
t = np.linspace(0, T, N_points, endpoint=False)
dt = T / N_points

# Square wave
f_square = np.where(t < T / 2, 1.0, -1.0)

def fourier_coefficients(f, t, T, n_max=10):
    """Numerically compute Fourier coefficients aₙ and bₙ."""
    dt = T / len(t)
    a = []
    b = []
    for n in range(n_max + 1):
        an = (2 / T) * np.sum(f * np.cos(2 * np.pi * n * t / T)) * dt
        bn = (2 / T) * np.sum(f * np.sin(2 * np.pi * n * t / T)) * dt
        a.append(an)
        b.append(bn)
    return np.array(a), np.array(b)

a_sq, b_sq = fourier_coefficients(f_square, t, T, n_max=15)

print("Square wave Fourier coefficients (first 10 terms):")
print(f"{'n':>4}  {'aₙ (numerical)':>18}  {'bₙ (numerical)':>18}  {'4/(nπ) [analytical]':>22}")
print("-" * 72)
for n in range(1, 11):
    analytical_bn = 4 / (n * np.pi) if n % 2 == 1 else 0.0
    print(f"{n:>4}  {a_sq[n]:>18.6f}  {b_sq[n]:>18.6f}  {analytical_bn:>22.6f}")
```

**Question 1.1:** Do the numerical coefficients match the analytical values? What is the maximum absolute error? Does the error decrease if you increase N_points?

**Question 1.2:** The Fourier coefficients of the square wave decay like 1/n. The sawtooth wave (f(t) = t/T − 1/2) has coefficients that also decay like 1/n, while a triangular wave's coefficients decay like 1/n². What does faster coefficient decay imply about the smoothness of the function?

---

## Part 2: Partial Sums and the Gibbs Phenomenon

```python
def fourier_partial_sum(t, T, a_coeffs, b_coeffs, N_terms):
    """Reconstruct f from the first N_terms Fourier terms."""
    result = a_coeffs[0] / 2  # DC term
    for n in range(1, N_terms + 1):
        result += a_coeffs[n] * np.cos(2 * np.pi * n * t / T)
        result += b_coeffs[n] * np.sin(2 * np.pi * n * t / T)
    return result

# Plot partial sums with increasing numbers of terms
terms_list = [1, 3, 5, 11, 51]
t_plot = np.linspace(0, T, 5000)
a_many, b_many = fourier_coefficients(f_square, t, T, n_max=100)

fig, axes = plt.subplots(1, len(terms_list), figsize=(16, 3))
for ax, N_terms in zip(axes, terms_list):
    approx = fourier_partial_sum(t_plot, T, a_many, b_many, N_terms)
    true   = np.where(t_plot < T / 2, 1.0, -1.0)
    ax.plot(t_plot, true,   'lightgray', linewidth=2, label='True')
    ax.plot(t_plot, approx, 'steelblue', linewidth=1.2, label=f'N={N_terms}')
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'{N_terms} term{"s" if N_terms > 1 else ""}')
    ax.set_xlabel('t')
    if N_terms == 1:
        ax.set_ylabel('f(t)')
    ax.legend(fontsize=7)

plt.suptitle('Partial Sums of Fourier Series (Square Wave)', y=1.02)
plt.tight_layout()
plt.savefig('fourier_partial_sums.png', dpi=100)
plt.show()

# Measure the Gibbs overshoot
N_gibbs = 51
approx_51 = fourier_partial_sum(t_plot, T, a_many, b_many, N_gibbs)
overshoot_pct = (np.max(approx_51) - 1.0) * 100
print(f"\nGibbs overshoot with N={N_gibbs} terms: {overshoot_pct:.1f}%")
print("(Theoretical Gibbs constant: ~8.9%)")
```

**Question 2.1:** Describe the Gibbs phenomenon: what happens near the jump discontinuity as N increases? Does the overshoot get smaller with more terms?

**Question 2.2:** The Gibbs constant (≈ 8.9%) is independent of N. Compute the overshoot for N = 11, 51, 101, 501. Confirm that it does not decrease. Why might this matter for applications like audio or image compression?

```python
# Energy in the tail of the series
N_max = 100
energies = []
for N_terms in range(1, N_max + 1):
    tail_energy = 0.5 * np.sum(b_many[N_terms+1:]**2)
    energies.append(tail_energy)

plt.figure(figsize=(7, 4))
n_range = np.arange(1, N_max)
plt.loglog(n_range, energies[:N_max-1], 'steelblue', linewidth=2, label='Tail energy')
plt.loglog(n_range, 1.0 / n_range, 'r--', linewidth=1.5, label='1/N reference')
plt.xlabel('N (terms included)')
plt.ylabel('Tail energy Σ_{n>N} bₙ²/2')
plt.title('Energy in Tail of Fourier Series')
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.tight_layout()
plt.savefig('fourier_tail_energy.png', dpi=100)
plt.show()
```

**Question 2.3:** The log-log plot shows the tail energy decays approximately like 1/N. How many terms are needed to capture 99% of the total energy? 99.9%? What is the total energy of the square wave (use Parseval's theorem: it equals 1)?

---

## Part 3: Additive Synthesis — Building Instrument Sounds

Musical timbre is determined by the relative amplitudes of harmonics. We can synthesize instrument-like sounds by choosing the right amplitude envelope.

```python
sample_rate = 44100  # Hz
duration    = 2.0    # seconds
f0          = 440.0  # A4

t_audio = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

def synthesize(f0, harmonics_amplitudes, t):
    """
    Build a waveform from harmonics.
    harmonics_amplitudes: list of (harmonic_number, amplitude) tuples.
    """
    signal = np.zeros_like(t)
    for n, amp in harmonics_amplitudes:
        signal += amp * np.sin(2 * np.pi * n * f0 * t)
    # Normalize
    signal /= np.max(np.abs(signal) + 1e-10)
    return signal

# Sine (pure tone): only fundamental
sine_wave = synthesize(f0, [(1, 1.0)], t_audio)

# Clarinet model: only odd harmonics with 1/n amplitude decay
clarinet = synthesize(f0, [(n, 1/n) for n in range(1, 20, 2)], t_audio)

# Violin model: all harmonics with roughly 1/n² amplitude decay
violin = synthesize(f0, [(n, 1/n**1.5) for n in range(1, 20)], t_audio)

# Bright tone: emphasize high harmonics
bright  = synthesize(f0, [(n, 1/np.sqrt(n)) for n in range(1, 20)], t_audio)

# Plot one cycle of each waveform
one_cycle = int(sample_rate / f0)
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
waveforms = [('Sine', sine_wave), ('Clarinet', clarinet),
             ('Violin', violin),  ('Bright', bright)]
for ax, (name, wave) in zip(axes.flatten(), waveforms):
    ax.plot(t_audio[:one_cycle * 3] * 1000, wave[:one_cycle * 3],
            'steelblue', linewidth=1.2)
    ax.set_title(name)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Amplitude')
    ax.grid(True, alpha=0.2)
plt.suptitle('One Period of Synthesized Waveforms at A 440 Hz', y=1.02)
plt.tight_layout()
plt.savefig('synth_waveforms.png', dpi=100)
plt.show()

# Play audio (if available)
if AUDIO_AVAILABLE:
    print("Playing clarinet synthesis...")
    # Apply a brief fade-out to avoid click
    envelope = np.exp(-t_audio / 0.8)
    sd.play((clarinet * envelope).astype(np.float32), sample_rate)
    sd.wait()
```

**Question 3.1:** The clarinet model uses only odd harmonics. Look at the waveform — does it look like a square wave? Explain the connection using what you know about Fourier series.

**Question 3.2:** The "bright" instrument uses amplitudes that decay like 1/√n rather than 1/n². More energy in high harmonics makes the sound brighter and harsher. Sketch (or compute) the spectrum for each instrument model. Which has the most energy above the 10th harmonic?

---

## Part 4: FFT Analysis of a Real Waveform

The Discrete Fourier Transform (DFT) computes the frequency content of a sampled signal. We apply it to a synthesized chord.

```python
# Synthesize a major chord: A4 (440), C#5 (554), E5 (659)
chord_freqs = [440, 554, 659]
chord = sum(np.sin(2 * np.pi * f * t_audio) for f in chord_freqs) / len(chord_freqs)

# Compute FFT
N_fft = len(chord)
spectrum = fft(chord)
freqs    = fftfreq(N_fft, d=1/sample_rate)

# Only positive frequencies
pos_mask = freqs > 0
freqs_pos    = freqs[pos_mask]
magnitude    = np.abs(spectrum[pos_mask]) / (N_fft / 2)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Time domain (first 10 ms)
show = int(0.010 * sample_rate)
axes[0].plot(t_audio[:show] * 1000, chord[:show], 'steelblue', linewidth=1)
axes[0].set_xlabel('Time (ms)')
axes[0].set_ylabel('Amplitude')
axes[0].set_title('A Major Chord — Time Domain (first 10 ms)')
axes[0].grid(True, alpha=0.3)

# Frequency domain (up to 1500 Hz)
freq_limit = freqs_pos < 1500
axes[1].plot(freqs_pos[freq_limit], magnitude[freq_limit],
             'tomato', linewidth=1.5)
for f in chord_freqs:
    axes[1].axvline(f, color='gray', linestyle='--', alpha=0.7, linewidth=0.8)
    axes[1].text(f + 5, magnitude[np.argmin(np.abs(freqs_pos - f))] * 1.05,
                 f'{f} Hz', fontsize=8)
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Magnitude')
axes[1].set_title('A Major Chord — Frequency Domain (FFT)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('chord_fft.png', dpi=100)
plt.show()
```

**Question 4.1:** The FFT correctly identifies the three frequencies in the chord as sharp peaks. In a real recording, these peaks would be broader and surrounded by noise. What causes the broadening, and what does it mean for pitch detection algorithms?

**Question 4.2:** The FFT has O(N log N) complexity, while the naive DFT is O(N²). For a CD-quality audio file (44,100 samples/second × 3 minutes), compare the number of operations required. By what factor is the FFT faster?

```python
# Spectrogram: FFT over sliding windows
def spectrogram(signal, sample_rate, window_size=2048, hop=512):
    """Compute a short-time Fourier transform (spectrogram)."""
    n_frames = (len(signal) - window_size) // hop
    freqs_sg = fftfreq(window_size, 1 / sample_rate)[:window_size // 2]
    S = np.zeros((window_size // 2, n_frames))
    window = np.hanning(window_size)
    for i in range(n_frames):
        segment = signal[i * hop : i * hop + window_size] * window
        S[:, i] = np.abs(fft(segment)[:window_size // 2])
    return freqs_sg, S

# Synthesize a melody: A4 → C#5 → E5, each 0.5 seconds
melody = np.concatenate([
    np.sin(2 * np.pi * 440 * t_audio[:sample_rate // 2]),
    np.sin(2 * np.pi * 554 * t_audio[:sample_rate // 2]),
    np.sin(2 * np.pi * 659 * t_audio[:sample_rate // 2]),
])

freqs_sg, S = spectrogram(melody, sample_rate)

plt.figure(figsize=(10, 4))
t_sg = np.linspace(0, len(melody) / sample_rate, S.shape[1])
plt.pcolormesh(t_sg, freqs_sg[:100], 20 * np.log10(S[:100] + 1e-8),
               shading='auto', cmap='inferno')
plt.colorbar(label='Power (dB)')
plt.ylim(0, 800)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram of A → C# → E Melody')
plt.tight_layout()
plt.savefig('spectrogram.png', dpi=100)
plt.show()
```

**Question 4.3:** The spectrogram shows how the frequency content changes over time. Describe what you see: when does each note appear, and are there harmonics visible above the fundamental? What would the spectrogram look like for a spoken vowel vs. a consonant?

---

## Part 5: Exploring Parseval's Theorem

```python
# Verify Parseval's theorem numerically
signals = {
    'Square wave':   f_square,
    'Sine wave':     np.sin(2 * np.pi * t / T),
    'Sawtooth':      2 * (t / T - np.floor(t / T + 0.5)),
    'Triangle':      2 * np.abs(2 * (t / T - np.floor(t / T + 0.5))) - 1,
}

print(f"{'Signal':20s}  {'Time domain':14s}  {'Fourier (N=200)':16s}  {'Match?':8s}")
print("-" * 65)
for name, sig in signals.items():
    a_c, b_c = fourier_coefficients(sig, t, T, n_max=200)
    # Time-domain energy
    E_time = np.mean(sig**2)
    # Fourier-domain energy (Parseval)
    E_fourier = a_c[0]**2 / 4 + 0.5 * np.sum(a_c[1:]**2 + b_c[1:]**2)
    match = '✓' if abs(E_time - E_fourier) < 0.01 else '✗'
    print(f"{name:20s}  {E_time:14.6f}  {E_fourier:16.6f}  {match:8s}")
```

**Question 5.1:** Parseval's theorem says the energy computed in the time domain equals the energy computed in the Fourier domain. Verify this numerically for all four signals. Why does the theorem require infinitely many terms for an exact match, and where does the small residual error in your computation come from?

---

## Deliverables

Submit a PDF or Jupyter notebook containing:

1. All labeled plots.
2. Answers to all numbered questions.
3. The Parseval's theorem verification table.
4. **Creative synthesis (optional):** Design your own instrument by choosing an amplitude envelope for harmonics 1–15. Plot the spectrum and waveform, and play the sound if audio is available. Describe what it sounds like and why.
5. **Reflection (1 paragraph):** Fourier analysis decomposes a signal into frequencies. But musical notes have *time-varying* spectra — the "attack" of a piano note sounds different from its "decay" even at the same pitch. The spectrogram addresses this. Describe one musical or scientific application where the spectrogram (time-frequency representation) is more useful than the static Fourier spectrum, and explain why.
