import numpy as np

def genSine(A, f, phi, fs, t):
    N = t * fs
    x = A * (np.cos(2 * np.pi * f * np.arange(N) * (1.0/fs) + phi))
    return x
