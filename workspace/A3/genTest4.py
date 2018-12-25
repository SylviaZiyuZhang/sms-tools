import numpy as np
from genTest1 import genSine

f1 = 23
f2 = 36
f3 = 40
f4 = 100
f5 = 200
f6 = 230
f7 = 900
f8 = 1000

fs = 44100
t = 0.02
phi = 0
A = 1.0

x1 = genSine(A, f3, phi, fs, t) + genSine(A, f4, phi, fs, t) + genSine(A, f5, phi, fs, t) + genSine(A, f8, phi, fs, t)

x2 = genSine(A, f1, phi, fs, t) + genSine(A, f2, phi, fs, t) + genSine(A, f6, phi, fs, t) + genSine(A, f7, phi, fs, t)

